import os
import time
import json
import logging
from decimal import Decimal, ROUND_UP
from typing import Tuple, Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from models.models import Deposits, Transactions, Activity
from utils.random_hash import random_hash
from .ton_price_service import get_ton_usd_price
from .toncenter_service import TonCenter

logger = logging.getLogger(__name__)

RECIPIENT_ADDRESS = os.getenv("TON_RECIPIENT")
TON_NETWORK = os.getenv("TON_NETWORK", "testnet").lower()

if not RECIPIENT_ADDRESS:
    # You must configure TON_RECIPIENT via environment
    logger.warning("TON_RECIPIENT is not set; crypto init will fail until configured")

NANO = Decimal(10) ** 9
VALIDITY_SECONDS = 15 * 60
GATEWAY_ID = 8  # Fixed gateway id per requirements

async def init_crypto_transaction(user_id: int, total_usd: Decimal, items: List[Dict[str, Any]], db: AsyncSession) -> Tuple[bool, Dict[str, Any], str]:
    if total_usd <= 0:
        return False, {}, "Invalid total"
    if not RECIPIENT_ADDRESS:
        return False, {}, "TON recipient address is not configured"

    price = await get_ton_usd_price()  # USD per TON
    # TON amount = USD / price
    ton_amount = (total_usd / price).quantize(Decimal("0.000000001"), rounding=ROUND_UP)
    nano_amount = int((ton_amount * NANO).to_integral_value(rounding=ROUND_UP))

    now = int(time.time())
    valid_until = now + VALIDITY_SECONDS

    # Only prepare client transaction; no DB writes at init
    reference = f"TON{random_hash(8).upper()}"

    tx = {
        "to": RECIPIENT_ADDRESS,
        "amount": nano_amount,
        "payload": None,
        "validUntil": valid_until
    }
    return True, {"reference": reference, "transaction": tx}, "OK"

async def verify_crypto_transaction(user_id: int, total_usd: Decimal, items: List[Dict[str, Any]], payer_address: str | None, db: AsyncSession, reference: str | None = None, ip_address: str = "") -> Tuple[bool, Dict[str, Any], str]:
    # Determine expected nano from provided USD as hint
    price = await get_ton_usd_price()
    hint_ton_amount = (total_usd / price).quantize(Decimal("0.000000001"), rounding=ROUND_UP)
    expected_nano = int((hint_ton_amount * NANO).to_integral_value(rounding=ROUND_UP))

    # Load deposit by reference if provided
    deposit = None
    if reference:
        result = await db.execute(select(Deposits).where(Deposits.uid == user_id, Deposits.reference_number == reference))
        deposit = result.scalar_one_or_none()

    # Fetch recent txs to our recipient
    txs = await TonCenter.get_transactions(RECIPIENT_ADDRESS, limit=25)

    matched = None
    for tx in txs:
        to_addr = TonCenter.extract_incoming_to_address(tx)
        if not to_addr:
            continue
        if payer_address:
            src = TonCenter.extract_source_address(tx)
            if not src or src != payer_address:
                continue
        value = TonCenter.extract_value_nano(tx)
        if value >= expected_nano:
            matched = tx
            break

    if not matched:
        return False, {}, "Matching on-chain transaction not found yet"

    # Create records AFTER verify only
    now = int(time.time())

    paid_nano = TonCenter.extract_value_nano(matched)
    paid_ton = Decimal(paid_nano) / NANO
    usd_paid = (paid_ton * price).quantize(Decimal("0.01"), rounding=ROUND_UP)

    # Single on-chain tx, but create per-item records in DB
    items_total = sum(Decimal(str(i.get("totalCost", 0))) for i in items)
    if items_total <= 0:
        return False, {}, "Invalid items total"
    # Log discrepancy if any
    if abs(items_total - usd_paid) > Decimal("1.00"):
        logger.warning(f"USD paid on-chain ({usd_paid}) differs from items total ({items_total}) by > $1.00")

    txid = f"TON{random_hash(12)}"
    chain_hash = str(matched.get('transaction_id', {}).get('hash'))

    first_deposit_id = None

    for i in items:
        item_usd = Decimal(str(i.get("totalCost", 0)))
        rate = Decimal(str(i.get("usdRate", 0)))
        code = str(i.get("code", "UAE"))
        forevers_amount = Decimal(str(i.get("amount", 0)))

        deposit = Deposits(
            uid=user_id,
            txid=txid,
            method=GATEWAY_ID,
            amount=str(item_usd),
            currency='USD',
            requested_on=now,
            processed_on=now,
            reference_number=reference or f"TON{random_hash(8).upper()}",
            status=1,
            is_exchange=0,
            ip_address=ip_address or '',
            gateway_txid=chain_hash,
            payment_data=json.dumps({
                "forevers_amount": str(forevers_amount),
                "usd_rate": str(rate),
                "paid_nano": int(paid_nano),
                "paid_ton": str(paid_ton)
            }),
            rate_at_deposit=rate,
            type=code
        )
        db.add(deposit)
        await db.flush()
        if first_deposit_id is None:
            first_deposit_id = deposit.id

        description = f"Forevers {code} purchased via TON crypto (User ID: {user_id})"
        transaction = Transactions(
            txid=txid,
            type=3,
            sender=user_id,
            recipient=deposit.id,
            description=description,
            deposit_via=GATEWAY_ID,
            amount=str(item_usd),
            currency='USD',
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
            amount=str(item_usd),
            currency='USD',
            status=3,
            created=now
        )
        db.add(activity)

    await db.commit()

    return True, {
        "tx_hash": matched.get('transaction_id', {}).get('hash'),
        "tx_lt": matched.get('transaction_id', {}).get('lt'),
        "tx_utime": matched.get('utime'),
        "deposit_id": first_deposit_id,
        "txid": txid
    }, "Verified"
