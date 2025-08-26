import os
import time
import json
from decimal import Decimal, ROUND_UP
from typing import Tuple, List

import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, select

from models.models import Deposits, Transactions, Activity
from utils.random_hash import random_hash

TONCENTER_API_V2_TESTNET = "https://testnet.toncenter.com/api/v2"
COINGECKO_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd"

GATEWAY_ID = 8  # TON gateway id


class TonCryptoService:
    @staticmethod
    def _env(name: str, default: str | None = None) -> str | None:
        return os.getenv(name, default)

    @staticmethod
    async def get_ton_price_usd() -> Decimal:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(COINGECKO_PRICE_URL)
            resp.raise_for_status()
            data = resp.json()
            price = data.get('the-open-network', {}).get('usd')
            if price is None:
                raise ValueError('TON price not available')
            return Decimal(str(price))

    @staticmethod
    def compute_nano_amount(usd_total: Decimal, ton_price_usd: Decimal, slippage_percent: float) -> Tuple[int, Decimal]:
        ton_amount = (usd_total / ton_price_usd) * Decimal(1 + (slippage_percent or 0) / 100)
        # round up to nanotons
        nano = int((ton_amount * Decimal(1_000_000_000)).to_integral_value(rounding=ROUND_UP))
        return nano, ton_amount

    @staticmethod
    async def initiate_order(user_id: int, items: List[dict], ton_address: str, ip_address: str, slippage_percent: float, db: AsyncSession):
        receiver = TonCryptoService._env('TON_RECEIVER_ADDRESS')
        if not receiver:
            raise ValueError('TON_RECEIVER_ADDRESS is not set')

        ton_price = await TonCryptoService.get_ton_price_usd()
        usd_total = sum(Decimal(str(i['totalCost'])) for i in items)
        amount_nano, ton_amount = TonCryptoService.compute_nano_amount(Decimal(usd_total), ton_price, slippage_percent)

        group_txid = f"CRPT{random_hash(10)}"
        order_id = f"CRP{random_hash(8).upper()}"
        now = int(time.time())
        valid_until = now + 15 * 60  # 15 minutes

        payment_payload = {
            'order_id': order_id,
            'group_txid': group_txid,
            'receiver': receiver,
            'ton_price_usd': str(ton_price),
            'usd_total': str(usd_total),
            'expected_amount_nano': amount_nano,
            'slippage_percent': slippage_percent,
            'valid_until': valid_until
        }

        # Create one deposit per item (pending)
        created_ids: List[int] = []
        for it in items:
            dep = Deposits(
                uid=user_id,
                txid=group_txid,
                method=GATEWAY_ID,
                amount=str(Decimal(str(it['totalCost']))),
                currency='USD',
                requested_on=now,
                processed_on=0,
                reference_number=order_id,
                status=0,
                rate_at_deposit=Decimal(str(it['usdRate'])),
                is_exchange=0,
                type=it['code'],
                ip_address=ip_address,
                payment_data=json.dumps(payment_payload)
            )
            db.add(dep)
            await db.flush()
            created_ids.append(dep.id)

        await db.commit()

        return {
            'order_id': order_id,
            'to_address': receiver,
            'amount_nano': amount_nano,
            'valid_until': valid_until,
            'ton_price_usd': ton_price,
            'deposit_ids': created_ids
        }

    @staticmethod
    async def _find_incoming_tx(from_address: str, to_address: str, min_amount_nano: int) -> Tuple[str, int] | None:
        api_key = TonCryptoService._env('TONCENTER_API_KEY')
        params = {
            'address': to_address,
            'limit': 20,
            'api_key': api_key
        }
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.get(f"{TONCENTER_API_V2_TESTNET}/getTransactions", params=params)
            r.raise_for_status()
            data = r.json()
            txs = data.get('result', [])
            for tx in txs:
                in_msg = tx.get('in_msg') or {}
                source = in_msg.get('source')
                value = int(in_msg.get('value') or 0)
                if not source or source.lower() != from_address.lower():
                    continue
                if value >= min_amount_nano:
                    # Return hash; v2 returns transaction_id dict
                    tid = tx.get('transaction_id') or {}
                    hash_hex = tid.get('hash')
                    lt = int(tid.get('lt') or 0)
                    if hash_hex:
                        return hash_hex, lt
            return None

    @staticmethod
    async def confirm_order(user_id: int, order_id: str, from_address: str, db: AsyncSession):
        # Load deposits for this order
        stmt = select(Deposits).where(Deposits.uid == user_id, Deposits.reference_number == order_id, Deposits.status == 0)
        res = await db.execute(stmt)
        deps: List[Deposits] = list(res.scalars().all())
        if not deps:
            return False, "Order not found or already processed", None, []

        # Read payment payload
        try:
            payload = json.loads(deps[0].payment_data or '{}')
        except Exception:
            payload = {}
        receiver = payload.get('receiver') or TonCryptoService._env('TON_RECEIVER_ADDRESS')
        expected_nano = int(payload.get('expected_amount_nano') or 0)
        if not receiver or expected_nano <= 0:
            return False, "Invalid order state", None, []

        found = await TonCryptoService._find_incoming_tx(from_address, receiver, expected_nano)
        if not found:
            return False, "Matching TON transaction not found yet", None, []
        tx_hash, lt = found

        now = int(time.time())
        deposit_ids: List[int] = []

        for d in deps:
            upd = update(Deposits).where(Deposits.id == d.id).values(
                processed_on=now,
                status=1,
                gateway_txid=tx_hash
            )
            await db.execute(upd)
            deposit_ids.append(d.id)

            # Create related records
            desc = f"Forevers {d.type} purchased via TON (User ID: {user_id})"
            tr = Transactions(
                txid=d.txid,
                type=3,
                sender=user_id,
                recipient=d.id,
                description=desc,
                deposit_via=GATEWAY_ID,
                amount=d.amount,
                currency=d.currency,
                fee='',
                status=1,
                created=now
            )
            db.add(tr)

            act = Activity(
                txid=d.txid,
                type=3,
                uid=user_id,
                deposit_via=GATEWAY_ID,
                u_field_1=str(d.id),
                amount=d.amount,
                currency=d.currency,
                status=3,
                created=now
            )
            db.add(act)

        await db.commit()
        return True, "Payment confirmed", tx_hash, deposit_ids
