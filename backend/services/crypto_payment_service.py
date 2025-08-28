import os
import os
import time
import json
import logging
import asyncio
from decimal import Decimal, ROUND_UP
from typing import Tuple, Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from models.models import Deposits, Transactions, Activity
from utils.random_hash import random_hash
from .ton_price_service import get_ton_usd_price
from .toncenter_service import TonCenter
from .forevers_prices_service import extract_base_prices
from .discount_service import apply_discounts

logger = logging.getLogger(__name__)

RECIPIENT_ADDRESS = os.getenv("TON_RECIPIENT")
TON_NETWORK = os.getenv("TON_NETWORK", "testnet").lower()

if not RECIPIENT_ADDRESS:
    # You must configure TON_RECIPIENT via environment
    logger.warning("TON_RECIPIENT is not set; crypto init will fail until configured")

NANO = Decimal(10) ** 9
VALIDITY_SECONDS = 15 * 60
GATEWAY_ID = 8  # Fixed gateway id per requirements

async def _get_price_map(db: AsyncSession) -> dict[str, Decimal]:
    base = await extract_base_prices(db)
    if base is None:
        raise RuntimeError("Pricing data unavailable")
    discounted, _ = await apply_discounts(db, base)
    return {p.type: Decimal(p.value) for p in discounted}

def _calc_items_total_usd(items: List[Dict[str, Any]], price_map: dict[str, Decimal]) -> Decimal:
    total = Decimal('0')
    for i in items:
        code = str(i.get('code', 'UAE'))
        amt = Decimal(str(i.get('amount', 0)))
        if code not in price_map:
            raise RuntimeError(f"Unknown forevers type: {code}")
        total += (amt * price_map[code])
    return total.quantize(Decimal('0.01'), rounding=ROUND_UP)

async def init_crypto_transaction(user_id: int, total_usd: Decimal, items: List[Dict[str, Any]], db: AsyncSession) -> Tuple[bool, Dict[str, Any], str]:
    if not RECIPIENT_ADDRESS:
        return False, {}, "TON recipient address is not configured"

    # Compute payable total on backend
    price_map = await _get_price_map(db)
    server_total = _calc_items_total_usd(items, price_map)

    # Optional: compare client-provided total to server
    if total_usd and abs(server_total - total_usd) > Decimal('0.01'):
        # Prefer server value regardless
        logger.warning(f"Client total_usd {total_usd} != server_total {server_total}, using server value")

    # Convert USD->TON using external rate
    price = await get_ton_usd_price()  # USD per TON
    ton_amount = (server_total / price).quantize(Decimal("0.000000001"), rounding=ROUND_UP)
    nano_amount = int((ton_amount * NANO).to_integral_value(rounding=ROUND_UP))

    now = int(time.time())
    valid_until = now + VALIDITY_SECONDS

    reference = f"CRPT{random_hash(8).upper()}"

    tx = {
        "to": RECIPIENT_ADDRESS,
        "amount": nano_amount,
        "payload": None,
        "validUntil": valid_until
    }
    return True, {"reference": reference, "transaction": tx}, "OK"

async def verify_crypto_transaction(user_id: int, total_usd: Decimal, items: List[Dict[str, Any]], payer_address: str | None, db: AsyncSession, reference: str | None = None, valid_until: int | None = None, ip_address: str = "") -> Tuple[bool, Dict[str, Any], str]:
    # Determine expected nano from provided USD as hint
    price = await get_ton_usd_price()
    hint_ton_amount = (total_usd / price).quantize(Decimal("0.000000001"), rounding=ROUND_UP)
    expected_nano = int((hint_ton_amount * NANO).to_integral_value(rounding=ROUND_UP))

    # Load deposit by reference if provided (reserved for future use)
    if reference:
        _ = await db.execute(select(Deposits.id).where(Deposits.uid == user_id, Deposits.reference_number == reference))

    # Try a few times to let indexers catch up
    matched = None
    attempts = 3
    for _try in range(attempts):
      # Fetch recent txs to our recipient
      txs = await TonCenter.get_transactions(RECIPIENT_ADDRESS, limit=50)

      candidates: List[Tuple[int, Dict[str, Any]]] = []
      for tx in txs:
          to_addr = TonCenter.extract_incoming_to_address(tx)
          if not to_addr:
              continue
          if payer_address:
              src = TonCenter.extract_source_address(tx)
              if not src or src != payer_address:
                  continue
          value = TonCenter.extract_value_nano(tx)
          # Accept values that are close or higher than expected (±2%)
          lower_bound = int(expected_nano * 0.98)
          upper_bound = int(expected_nano * 1.05)
          if lower_bound <= value <= upper_bound or value >= expected_nano:
              diff = abs(value - expected_nano)
              candidates.append((diff, tx))
      if candidates:
          candidates.sort(key=lambda x: x[0])
          matched = candidates[0][1]
          break
      # brief wait before next attempt
      await asyncio.sleep(2)

    if not matched:
        return False, {}, "Matching on-chain transaction not found yet"

    # Create records AFTER verify only
    now = int(time.time())

    paid_nano = TonCenter.extract_value_nano(matched)
    paid_ton = Decimal(paid_nano) / NANO
    usd_paid = (paid_ton * price).quantize(Decimal("0.01"), rounding=ROUND_UP)
    server_valid_until = valid_until if valid_until else (now + VALIDITY_SECONDS)

    # Server-side recompute to prevent tampering
    price_map = await _get_price_map(db)
    server_items_total = _calc_items_total_usd(items, price_map)

    # Optional: compare client-sent sum of totalCost
    client_items_total = sum(Decimal(str(i.get("totalCost", 0))) for i in items)

    # Validate totals
    if abs(server_items_total - client_items_total) > Decimal("0.01"):
        return False, {}, "Client totals mismatch server calculation"

    # Validate paid amount with dynamic tolerance (max of $0.50 or 2% of total)
    tolerance = max(Decimal("0.50"), (server_items_total * Decimal("0.02")).quantize(Decimal("0.01"), rounding=ROUND_UP))
    if abs(server_items_total - usd_paid) > tolerance:
        return False, {}, "Paid amount does not match expected total"

    txid = f"CRPT{random_hash(8).upper()}"
    chain_hash = str(matched.get('transaction_id', {}).get('hash'))

    first_deposit_id = None

    for i in items:
        code = str(i.get("code", "UAE"))
        forevers_amount = Decimal(str(i.get("amount", 0)))
        server_rate = price_map[code]
        item_usd = (forevers_amount * server_rate).quantize(Decimal('0.01'), rounding=ROUND_UP)

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
                "order_id": reference or f"CRPT{random_hash(8).upper()}",
                "group_txid": txid,
                "receiver": RECIPIENT_ADDRESS,
                "ton_price_usd": str(price),
                "usd_total": str(server_items_total),
                "expected_amount_nano": expected_nano,
                "slippage_percent": 2.0,
                "valid_until": server_valid_until,
                "forevers_amount": str(forevers_amount),
                "usd_rate": str(server_rate),
                "paid_nano": int(paid_nano),
                "paid_ton": str(paid_ton)
            }),
            rate_at_deposit=server_rate,
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
