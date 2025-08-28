import json
import time
from decimal import Decimal
from typing import Tuple, Optional, Dict, Any
import logging

import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update

from models.models import Deposits, Transactions, Activity
from utils.random_hash import random_hash
from sessions.redis_session import init_redis
from services.ton_rate_service import get_ton_rate_usd

logger = logging.getLogger(__name__)

TON_TESTNET_RECEIVER = "0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG"
DEFAULT_NETWORK_FEE_TON = Decimal('0.02')  # conservative estimate, wallet pays fee separately
TONAPI_BASE = "https://testnet.tonapi.io"

class ForeversCryptoService:
    @staticmethod
    async def init_payment(user_id: int, usd_amount: Decimal, wallet_address: str, forevers_price: Optional[Decimal] = None, forevers_type: Optional[str] = None) -> Tuple[bool, Dict[str, Any], str]:
        try:
            if usd_amount <= 0:
                return False, {}, "Invalid amount"

            # Fetch rate (USD per TON)
            usd_per_ton, _ = await get_ton_rate_usd()
            # Convert: TON amount w/o network fee
            amount_ton = (Decimal(usd_amount) / usd_per_ton).quantize(Decimal('0.000000001'))
            # Separate network fee (not included in conversion)
            network_fee_ton = DEFAULT_NETWORK_FEE_TON
            total_ton = amount_ton + network_fee_ton

            # Build TonConnect tx (amount in nanotons, fee is not included here, wallet pays on top)
            nanotons = int((amount_ton * Decimal(1_000_000_000)).to_integral_value())
            valid_until = int(time.time()) + 600

            verify_id = f"TON{random_hash(10)}"

            # Cache expected payment in Redis for later verification
            redis = await init_redis()
            cache_key = f"crypto:verify:{verify_id}"
            cache_value = {
                "user_id": user_id,
                "usd_amount": float(Decimal(usd_amount)),
                "usd_per_ton": float(usd_per_ton),
                "amount_ton": float(amount_ton),
                "network_fee_ton": float(network_fee_ton),
                "total_ton": float(total_ton),
                "receiver": TON_TESTNET_RECEIVER,
                "wallet_address": wallet_address,
                "forevers_price": float(forevers_price) if forevers_price is not None else None,
                "forevers_type": forevers_type or None,
                "created_at": int(time.time())
            }
            await redis.set(cache_key, json.dumps(cache_value), ex=1800)  # 30 min

            data = {
                "verify_id": verify_id,
                "rate_usd_per_ton": float(usd_per_ton),
                "amount_ton": float(amount_ton),
                "network_fee_ton": float(network_fee_ton),
                "total_ton": float(total_ton),
                "forevers_price": float(forevers_price) if forevers_price is not None else None,
                "forevers_type": forevers_type or None,
                "ton_connect_tx": {
                    "validUntil": valid_until,
                    "messages": [
                        {"address": TON_TESTNET_RECEIVER, "amount": str(nanotons)}
                    ]
                }
            }
            return True, data, "OK"
        except Exception as e:
            logger.exception("init_payment failed")
            return False, {}, str(e)

    @staticmethod
    async def _fetch_incoming(receiver: str) -> Optional[list]:
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                url = f"{TONAPI_BASE}/v2/blockchain/accounts/{receiver}/transactions?limit=50"
                r = await client.get(url)
                r.raise_for_status()
                j = r.json()
                txs = j.get("transactions") or j
                return txs
        except Exception as e:
            logger.warning(f"Fetch transactions failed: {e}")
            return None

    @staticmethod
    def _extract_incoming_amount_and_hash(tx: Dict[str, Any]) -> Tuple[Optional[Decimal], Optional[str], Optional[str]]:
        try:
            # tonapi structure: {hash, in_msg: {source, value}, utime}
            in_msg = tx.get("in_msg") or {}
            value = in_msg.get("value")
            source = in_msg.get("source")
            if value is not None:
                # value in nanotons
                amt = Decimal(value) / Decimal(1_000_000_000)
                return amt, tx.get("hash"), source
            # fallback: operations list
            ops = tx.get("out_msgs") or []
            for m in ops:
                pass
            return None, None, None
        except Exception:
            return None, None, None

    @staticmethod
    async def verify_payment(verify_id: str, db: AsyncSession) -> Tuple[bool, Dict[str, Any], str]:
        try:
            redis = await init_redis()
            cache_key = f"crypto:verify:{verify_id}"
            raw = await redis.get(cache_key)
            if not raw:
                return False, {}, "Verification data not found or expired"
            exp = json.loads(raw)

            # Always recalc from current rate to prevent tampering
            usd_per_ton_now, _ = await get_ton_rate_usd()
            expected_ton_now = (Decimal(exp["usd_amount"]) / usd_per_ton_now).quantize(Decimal('0.000000001'))

            # Fetch latest on-chain tx for receiver
            txs = await ForeversCryptoService._fetch_incoming(exp["receiver"]) or []
            found_tx = None
            for tx in txs:
                amt, tx_hash, source = ForeversCryptoService._extract_incoming_amount_and_hash(tx)
                if not amt or not tx_hash:
                    continue
                # Match by close amount only (any sender allowed)
                diff = abs(amt - expected_ton_now)
                if expected_ton_now > 0 and (diff / expected_ton_now) <= Decimal('0.01'):
                    found_tx = {"hash": tx_hash, "amount_ton": float(amt), "source": source, "ts": tx.get("utime")}
                    break

            if not found_tx:
                return False, {"reason": "not_found"}, "Transaction not found or amount mismatch"

            # Resolve price per 1 Forevers to store in rate_at_deposit
            resolved_type = (exp.get("forevers_type") or "UAE").upper()
            resolved_price = exp.get("forevers_price")
            try:
                if resolved_price is None:
                    from services.forevers_prices_service import extract_base_prices
                    from services.discount_service import apply_discounts
                    base_prices = await extract_base_prices(db)
                    if base_prices:
                        discounted_prices, discounts = await apply_discounts(db, base_prices)
                        match = next((p for p in discounted_prices if str(p.type).upper() == resolved_type), None)
                        if match:
                            resolved_price = float(match.value)
                        else:
                            fallback = next((p for p in base_prices if str(p.type).upper() == resolved_type), None) or (base_prices[0] if base_prices else None)
                            if fallback:
                                resolved_price = float(fallback.value)
                if resolved_price is None:
                    resolved_price = float(Decimal(exp["usd_amount"]))
            except Exception:
                resolved_price = float(Decimal(exp["usd_amount"]))

            # Persist deposit and transaction records
            now = int(time.time())
            txid = f"TON{random_hash(12)}"

            # Create deposit
            deposit = Deposits(
                uid=int(exp["user_id"]),
                txid=txid,
                method=777,  # TON crypto gateway
                amount=str(Decimal(exp["usd_amount"]).quantize(Decimal('0.01'))),
                currency='USD',
                requested_on=now,
                processed_on=now,
                reference_number=verify_id,
                status=1,
                type=resolved_type if resolved_type in {"UAE","KZ","DE","PL","UA"} else "UAE",
                rate_at_deposit=Decimal(str(resolved_price)).quantize(Decimal('0.01')),
                payment_data=json.dumps([
                    {
                        "transaction_id": found_tx["hash"],
                        "wallet_address": exp.get("wallet_address"),
                        "amount_TON": found_tx["amount_ton"],
                        "amount_USD": float(Decimal(exp["usd_amount"]).quantize(Decimal('0.01'))),
                        "status": "confirmed",
                        "timestamp": found_tx.get("ts") or now,
                        "expected_amount_TON": float(expected_ton_now),
                        "network_fee_TON": float(exp.get("network_fee_ton", 0.0)),
                        "receiver": exp.get("receiver")
                    }
                ])
            )
            db.add(deposit)
            await db.flush()

            # Create transaction record (USD)
            transaction = Transactions(
                txid=txid,
                type=1,
                sender=int(exp["user_id"]),
                recipient=deposit.id,
                description=f"TON deposit (verify_id={verify_id})",
                deposit_via=777,
                amount=str(Decimal(exp["usd_amount"]).quantize(Decimal('0.01'))),
                currency='USD',
                fee='',
                status=1,
                created=now
            )
            db.add(transaction)

            # Add activity for audit
            activity = Activity(
                txid=txid,
                type=1,
                uid=int(exp["user_id"]),
                deposit_via=777,
                u_field_1=str(deposit.id),
                amount=str(Decimal(exp["usd_amount"]).quantize(Decimal('0.01'))),
                currency='USD',
                status=3,
                created=now
            )
            db.add(activity)

            await db.commit()
            await redis.delete(cache_key)

            return True, {"deposit_id": deposit.id, "tx_hash": found_tx["hash"]}, "Verified"
        except Exception as e:
            logger.exception("verify_payment failed")
            try:
                await db.rollback()
            except Exception:
                pass
            return False, {}, str(e)
