from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from decimal import Decimal
import time
from datetime import datetime
import json
import urllib.request
import urllib.parse
import logging
from typing import Tuple, Optional
import os

from models.models import Deposits, Transactions, Activity

logger = logging.getLogger(__name__)

TONCENTER_BASE = os.getenv("TONCENTER_BASE_URL", "https://testnet.toncenter.com/api/v2")
TONCENTER_API_KEY = os.getenv("TONCENTER_API_KEY")
RECEIVER_ADDRESS = "0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG"  # Provided testnet address
GATEWAY_ID = 8

class CryptoTonService:
    @staticmethod
    def _http_get_json(url: str, params: Optional[dict] = None) -> dict:
        if params:
            url = f"{url}?{urllib.parse.urlencode(params)}"
        headers = {
            'User-Agent': 'DBDC-Bot/1.0'
        }
        if TONCENTER_API_KEY:
            headers['X-API-Key'] = TONCENTER_API_KEY
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode('utf-8'))

    @staticmethod
    def _fetch_ton_usd_rate() -> Decimal:
        try:
            data = CryptoTonService._http_get_json(
                "https://api.coingecko.com/api/v3/simple/price",
                {"ids": "the-open-network", "vs_currencies": "usd"}
            )
            usd = data.get("the-open-network", {}).get("usd")
            if usd is None:
                raise ValueError("Invalid rate response")
            return Decimal(str(usd))
        except Exception as e:
            logger.error(f"Failed to fetch TON/USD rate: {e}")
            # Fallback to Toncenter price endpoint if available in future
            raise

    @staticmethod
    async def init_transaction(
        db: AsyncSession,
        user_id: int,
        forever_type: str,
        forevers_amount: int,
        final_rate: Decimal,
        usd_amount: Decimal,
        ip_address: str
    ) -> Tuple[bool, dict, str]:
        # Calculate and create pending deposit
        try:
            # Security: validate amounts coherence
            expected_usd = (Decimal(forevers_amount) * final_rate).quantize(Decimal('0.01'))
            usd_amount_q = usd_amount.quantize(Decimal('0.01'))
            if abs(expected_usd - usd_amount_q) > Decimal('0.01'):
                return False, {}, "USD amount mismatch"

            rate_usd_per_ton = CryptoTonService._fetch_ton_usd_rate()
            ton_amount = (usd_amount / rate_usd_per_ton).quantize(Decimal('0.000000001'))  # 9 dp
            amount_nano = int((ton_amount * Decimal(1_000_000_000)).to_integral_value())

            txid = f"TON{int(time.time())}{user_id}"
            now = int(time.time())

            deposit = Deposits(
                uid=user_id,
                txid=txid,
                method=GATEWAY_ID,
                amount=str(forevers_amount),
                currency='USD',
                requested_on=now,
                processed_on=0,
                reference_number=txid,
                status=0,
                rate_at_deposit=final_rate,
                is_exchange=1,
                type=forever_type,
                ip_address=ip_address
            )
            db.add(deposit)
            await db.flush()
            await db.commit()

            return True, {
                'to_address': RECEIVER_ADDRESS,
                'amount_ton': str(ton_amount),
                'amount_nano': amount_nano,
                'rate_usd_per_ton': str(rate_usd_per_ton),
                'txid': txid,
                'requested_on': now
            }, "Initiated"
        except Exception as e:
            await db.rollback()
            logger.error(f"TON init failed for user {user_id}: {e}", exc_info=True)
            return False, {}, f"Init failed: {str(e)}"

    @staticmethod
    def _find_matching_tx(to_addr: str, from_addr: str, amount_nano: int, since_unix: int) -> Optional[dict]:
        try:
            data = CryptoTonService._http_get_json(
                f"{TONCENTER_BASE}/getTransactions",
                {"address": to_addr, "limit": 25}
            )
            if not data.get('ok'):
                return None
            for tx in data.get('result', []):
                in_msg = tx.get('in_msg') or {}
                src = in_msg.get('source', '')
                val = int(in_msg.get('value') or 0)
                utime = int(tx.get('utime') or 0)
                if utime < since_unix:
                    continue
                # allow small variance (+/- 1e6 nanotons ~ 0.001 TON)
                if src == from_addr and abs(val - amount_nano) <= 1_000_000:
                    return { 'hash': tx.get('hash'), 'lt': tx.get('lt'), 'utime': utime, 'value': val }
            return None
        except Exception as e:
            logger.warning(f"getTransactions failed: {e}")
            return None

    @staticmethod
    async def verify_and_finalize(
        db: AsyncSession,
        user_id: int,
        txid: str,
        wallet_address: str
    ) -> Tuple[bool, dict, str]:
        try:
            # Load pending deposit
            res = await db.execute(select(Deposits).where(Deposits.txid == txid, Deposits.uid == user_id))
            deposit = res.scalar_one_or_none()
            if not deposit:
                return False, {}, "Unknown txid"
            if deposit.status == 1:
                return True, {'confirmed': True, 'already_confirmed': True}, "Already confirmed"

            # Determine expected amount and init time
            forevers_amount = Decimal(str(deposit.amount))
            usd_amount = (forevers_amount * Decimal(str(deposit.rate_at_deposit))).quantize(Decimal('0.01'))
            rate_usd_per_ton = CryptoTonService._fetch_ton_usd_rate()
            ton_amount = (usd_amount / rate_usd_per_ton).quantize(Decimal('0.000000001'))
            amount_nano = int((ton_amount * Decimal(1_000_000_000)).to_integral_value())

            match = CryptoTonService._find_matching_tx(RECEIVER_ADDRESS, wallet_address, amount_nano, int(deposit.requested_on))
            if not match:
                return False, {'confirmed': False}, "Not found yet"

            now = int(time.time())
            # Mark deposit completed
            deposit.processed_on = now
            deposit.status = 1
            await db.flush()

            # Create transaction and activity + exchange stats
            transaction = Transactions(
                txid=txid,
                type=3,
                sender=user_id,
                recipient=deposit.id,
                description=f"Forevers {deposit.type} purchased via TON (User ID: {user_id})",
                deposit_via=GATEWAY_ID,
                amount=str(forevers_amount),
                currency='FOREVERS',
                fee='',
                status=1,
                created=now
            )
            db.add(transaction)

            activity = Activity(
                txid=txid,
                type=3,
                uid=user_id,
                deposit_via=GATEWAY_ID,
                u_field_1=str(deposit.id),
                amount=str(forevers_amount),
                currency='FOREVERS',
                status=3,
                created=now
            )
            db.add(activity)

            await db.commit()

            return True, {
                'confirmed': True,
                'hash': match.get('hash'),
                'lt': match.get('lt'),
                'ton_amount_nano': amount_nano
            }, "Confirmed"
        except Exception as e:
            await db.rollback()
            logger.error(f"Verification failed for {txid}: {e}", exc_info=True)
            return False, {}, f"Verification failed: {str(e)}"
