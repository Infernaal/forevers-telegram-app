from sqlalchemy import select
from decimal import Decimal, ROUND_HALF_UP
import time
import logging
import json
import uuid
from datetime import datetime
from typing import Tuple, Optional, Dict, Any
import httpx
import os

from models.models import Deposits, Transactions, Settings, Activity
from services.forevers_purchase_service import ForeversPurchaseService
from utils.random_hash import random_hash
from sqlalchemy.ext.asyncio import AsyncSession

# Use Redis to keep init data until verification succeeds
from sessions.redis_session import init_redis

logger = logging.getLogger(__name__)

# Fixed receiver wallet address for TON testnet as specified in requirements
FIXED_RECEIVER_WALLET = "0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG"
CRYPTO_INIT_TTL_SECONDS = int(os.getenv("CRYPTO_INIT_TTL_SECONDS", "7200"))  # 2 hours


def _redis_key(txid: str) -> str:
    return f"crypto:init:{txid}"


class CryptoPurchaseService:
    """Service for handling TON cryptocurrency purchases"""

    @staticmethod
    async def get_ton_usd_rate() -> Decimal:
        """
        Get current TON to USD exchange rate from external API
        Returns rate for 1 TON in USD (mainnet rate used for testnet as well)
        """
        try:
            # Using CoinGecko API for TON price
            # Note: Using mainnet price for testnet calculations as testnet TON has no real value
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd",
                    timeout=10.0
                )

                if response.status_code == 200:
                    data = response.json()
                    rate = Decimal(str(data["the-open-network"]["usd"]))
                    logger.info(f"Fetched TON/USD rate from CoinGecko: {rate}")
                    return rate
                else:
                    logger.warning(f"Failed to fetch TON price, status: {response.status_code}")
        except Exception as e:
            logger.error(f"Error fetching TON price from CoinGecko: {e}")

        # Fallback rate if API fails (update this periodically)
        fallback_rate = Decimal("2.50")  # Approximate TON price in USD
        logger.warning(f"Using fallback TON/USD rate: {fallback_rate}")
        return fallback_rate

    @staticmethod
    async def get_network_fee_estimate() -> Decimal:
        """
        Get estimated network fee for TON transaction
        Returns fee in TON
        """
        # Standard TON transaction fee (approximately 0.01-0.02 TON)
        return Decimal("0.015")

    @staticmethod
    async def get_forevers_rate(db: AsyncSession, rate_as_deposit: Optional[Decimal] = None) -> Decimal:
        """
        Get the rate for 1 Forever in USD
        If rate_as_deposit is provided, use it, otherwise get from Settings
        """
        if rate_as_deposit is not None:
            return rate_as_deposit

        try:
            stmt = select(Settings).limit(1)
            result = await db.execute(stmt)
            settings = result.scalar_one_or_none()

            if settings and settings.forevers_value:
                return settings.forevers_value
            else:
                # Fallback value if no settings found
                return Decimal("4.00")
        except Exception as e:
            logger.error(f"Error fetching forevers rate: {e}")
            return Decimal("4.00")

    @staticmethod
    async def init_crypto_purchase(
        user_id: int,
        amount_usd: Decimal,
        user_wallet: str,
        receiver_wallet: str,
        rate_as_deposit: Optional[Decimal],
        db: AsyncSession
    ) -> Tuple[bool, Dict[str, Any], str]:
        """
        Initialize a crypto purchase transaction without DB writes.
        Data is persisted temporarily in Redis until verification.
        """
        try:
            client = await init_redis()

            # Validate receiver wallet is the fixed address
            if receiver_wallet != FIXED_RECEIVER_WALLET:
                logger.warning(f"Invalid receiver wallet attempt: user_id={user_id}, wallet={receiver_wallet}")
                return False, {}, f"Invalid receiver wallet. Must use: {FIXED_RECEIVER_WALLET}"

            # Validate user wallet format (basic validation)
            if not user_wallet or len(user_wallet) < 10:
                return False, {}, "Invalid user wallet address format"

            # Validate amount
            if amount_usd <= 0:
                return False, {}, "Amount must be greater than 0"

            # Security check: validate amount is not suspiciously high
            max_usd_per_transaction = Decimal("50000.00")  # $50,000 limit
            if amount_usd > max_usd_per_transaction:
                logger.warning(f"Suspicious high amount attempt: user_id={user_id}, amount_usd={amount_usd}")
                return False, {}, f"Amount too high: ${amount_usd}. Maximum allowed: ${max_usd_per_transaction}"

            # Get current rates
            ton_usd_rate = await CryptoPurchaseService.get_ton_usd_rate()
            forevers_rate = await CryptoPurchaseService.get_forevers_rate(db, rate_as_deposit)
            network_fee = await CryptoPurchaseService.get_network_fee_estimate()

            # Convert USD to TON (without network fee)
            amount_ton = (amount_usd / ton_usd_rate).quantize(Decimal('0.000000001'), rounding=ROUND_HALF_UP)

            # Calculate network fee in USD for reference
            network_fee_usd = (network_fee * ton_usd_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            # Generate unique transaction ID and reference number
            txid = f"CRPT{random_hash(8)}"
            reference_number = f"CRPT{random_hash(8).upper()}"
            current_time = int(time.time())

            # Prepare transaction data to keep in Redis until success
            transaction_data = {
                "txid": txid,
                "reference_number": reference_number,
                "transaction_id": None,
                "user_id": user_id,
                "user_wallet": user_wallet,
                "receiver_wallet": receiver_wallet,
                "amount_usd": str(amount_usd),
                "amount_ton": str(amount_ton),
                "ton_usd_rate": str(ton_usd_rate),
                "forevers_rate": str(forevers_rate),
                "network_fee_estimate": str(network_fee),
                "network_fee_usd": str(network_fee_usd),
                "status": "pending",
                "timestamp": current_time,
                "created_at": datetime.now().isoformat(),
                "verification_count": 0
            }

            # Save to Redis (ephemeral, no DB writes yet)
            await client.setex(_redis_key(txid), CRYPTO_INIT_TTL_SECONDS, json.dumps(transaction_data))

            # Prepare response data for Ton Connect
            response_data = {
                "to": receiver_wallet,
                "amount_ton": str(amount_ton),
                "amount_usd": str(amount_usd),
                "ton_usd_rate": str(ton_usd_rate),
                "network_fee": str(network_fee),
                "network_fee_usd": str(network_fee_usd),
                "txid": txid,
                "reference_number": reference_number,
                "forevers_rate": str(forevers_rate),
                "payload": f"Forever purchase - {txid}"
            }

            logger.info(
                f"Crypto purchase initialized (no DB write): user_id={user_id}, txid={txid}, "
                f"reference_number={reference_number}, amount_usd=${amount_usd}, amount_ton={amount_ton}"
            )

            return True, response_data, "Crypto purchase initialized successfully"

        except Exception as e:
            logger.error(
                f"Error initializing crypto purchase (no DB write): user_id={user_id}, error={str(e)}",
                exc_info=True
            )
            return False, {}, f"Failed to initialize crypto purchase: {str(e)}"

    @staticmethod
    async def verify_crypto_transaction(
        user_id: int,
        txid: str,
        db: AsyncSession
    ) -> Tuple[bool, Dict[str, Any], str]:
        """
        Verify a crypto transaction and update system state.
        Creates DB records only when verification is successful.
        """
        try:
            client = await init_redis()

            # Load init data from Redis
            raw = await client.get(_redis_key(txid))
            if not raw:
                logger.warning(f"Init data not found in Redis: user_id={user_id}, txid={txid}")
                return False, {}, "Transaction not found or expired"

            try:
                payment_data = json.loads(raw)
            except json.JSONDecodeError:
                logger.error(f"Invalid Redis JSON for txid={txid}")
                return False, {}, "Invalid transaction data"

            if payment_data.get("user_id") != user_id:
                logger.warning(
                    f"User mismatch in verify: actual_user={user_id}, stored_user={payment_data.get('user_id')}"
                )
                return False, {}, "Access denied"

            current_status = payment_data.get("status", "pending")
            if current_status in ["success", "failed", "invalid"]:
                return True, {
                    "transaction_status": current_status,
                    "txid": txid,
                    "last_updated": payment_data.get("last_verified", "unknown")
                }, f"Transaction status: {current_status}"

            # Perform real blockchain verification on TON testnet
            logger.info(
                f"Starting blockchain verification for txid={txid}, user_id={user_id}"
            )

            is_verified, blockchain_data = await CryptoPurchaseService._verify_on_blockchain(
                payment_data.get("user_wallet"),
                payment_data.get("receiver_wallet"),
                payment_data.get("amount_ton"),
                payment_data.get("transaction_id")
            )

            logger.info(
                f"Blockchain verification result: is_verified={is_verified}, txid={txid}"
            )

            current_time = int(time.time())
            payment_data["last_verified"] = current_time
            payment_data["verification_count"] = int(payment_data.get("verification_count", 0)) + 1

            if is_verified:
                # Create DB records now (only on success)
                payment_data["status"] = "success"
                payment_data["verified_at"] = current_time
                payment_data["blockchain_data"] = blockchain_data

                # Create deposit
                deposit_txid = payment_data.get("txid", txid)
                deposit = Deposits(
                    uid=user_id,
                    txid=deposit_txid,
                    method=8,  # Crypto gateway ID
                    amount=str(payment_data.get("amount_usd")),
                    currency='USD',
                    requested_on=payment_data.get("timestamp", current_time),
                    processed_on=current_time,
                    status=1,  # Success
                    rate_at_deposit=Decimal(str(payment_data.get("forevers_rate", "0"))),
                    reference_number=payment_data.get("reference_number"),
                    is_exchange=0,
                    type='UAE',
                    payment_data=json.dumps(payment_data),
                    ip_address="0.0.0.0"
                )
                db.add(deposit)
                await db.flush()

                # Create transaction record
                description = f"Crypto purchase - {txid}"
                transaction = Transactions(
                    txid=deposit.txid,
                    type=1,
                    sender=0,
                    recipient=user_id,
                    description=description,
                    amount=deposit.amount,
                    currency='USD',
                    fee='',
                    deposit_via=8,
                    status=1,
                    created=current_time
                )
                db.add(transaction)

                # Create activity record (gateway id 8)
                activity = Activity(
                    txid=deposit.txid,
                    type=1,
                    uid=user_id,
                    deposit_via=8,
                    u_field_1=str(deposit.id),
                    amount=str(deposit.amount),
                    currency='USD',
                    status=3,
                    created=current_time
                )
                db.add(activity)

                await db.commit()

                # Cleanup Redis
                await client.delete(_redis_key(txid))

                logger.info(
                    f"Crypto transaction verified successfully: user_id={user_id}, txid={txid}, deposit_id={deposit.id}"
                )

                return True, {
                    "transaction_status": "success",
                    "deposit_id": deposit.id,
                    "txid": txid,
                    "reference_number": payment_data.get("reference_number"),
                    "amount_usd": payment_data.get("amount_usd"),
                    "verified_at": current_time
                }, "Transaction verified and processed successfully"

            else:
                # Timeout logic
                time_since_creation = current_time - int(payment_data.get("timestamp", current_time))
                timeout_seconds = 3600  # 1 hour

                if time_since_creation > timeout_seconds:
                    payment_data["status"] = "failed"
                    payment_data["failure_reason"] = "Transaction timeout"
                    # Update Redis and keep for some TTL for later reads
                    await client.setex(
                        _redis_key(txid), CRYPTO_INIT_TTL_SECONDS, json.dumps(payment_data)
                    )

                    return True, {
                        "transaction_status": "failed",
                        "txid": txid,
                        "failure_reason": "Transaction timeout"
                    }, "Transaction failed due to timeout"

                # Still pending; just update Redis
                await client.setex(_redis_key(txid), CRYPTO_INIT_TTL_SECONDS, json.dumps(payment_data))

                return True, {
                    "transaction_status": "pending",
                    "txid": txid,
                    "verification_count": payment_data.get("verification_count", 0)
                }, "Transaction still pending verification"

        except Exception as e:
            try:
                await db.rollback()
            except Exception:
                pass
            logger.error(
                f"Error verifying crypto transaction: user_id={user_id}, txid={txid}, error={str(e)}",
                exc_info=True
            )
            return False, {}, f"Failed to verify transaction: {str(e)}"

    @staticmethod
    async def _verify_on_blockchain(
        user_wallet: str,
        receiver_wallet: str,
        expected_amount_ton: str,
        transaction_id: Optional[str]
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        Verify transaction on TON testnet blockchain using TONCenter API

        Args:
            user_wallet: Sender wallet address
            receiver_wallet: Receiver wallet address
            expected_amount_ton: Expected amount in TON
            transaction_id: Transaction hash/ID if available

        Returns:
            Tuple of (is_verified, blockchain_data)
        """

        try:
            # TonAPI testnet endpoint (no fallback)
            base_url = "https://testnet.tonapi.io"

            # Convert expected amount to nanotons for comparison (1 TON = 1,000,000,000 nanotons)
            expected_amount_nanotons = int(float(expected_amount_ton) * 1000000000)

            # Allow some tolerance for gas fees and rounding differences
            # Tolerance: minimum 0.01 TON or 1% of expected amount, whichever is larger
            tolerance = max(10000000, int(expected_amount_nanotons * 0.01))  # 0.01 TON = 10,000,000 nanotons
            min_amount = expected_amount_nanotons - tolerance
            max_amount = expected_amount_nanotons + tolerance

            logger.info(f"Verifying transaction: from={user_wallet[:10]}... to={receiver_wallet[:10]}... "
                        f"expected={expected_amount_ton} TON ({expected_amount_nanotons} nanotons)")

            async with httpx.AsyncClient(timeout=30.0) as client:
                headers = {}
                token = os.getenv("TONAPI_TOKEN")
                if token:
                    headers["Authorization"] = f"Bearer {token}"

                # Normalize addresses to raw (workchain:hex)
                try:
                    rcv = await client.get(f"{base_url}/v2/blockchain/accounts/{receiver_wallet}", headers=headers)
                    receiver_raw = rcv.json().get("address", receiver_wallet) if rcv.status_code == 200 else receiver_wallet
                except Exception:
                    receiver_raw = receiver_wallet
                try:
                    usr = await client.get(f"{base_url}/v2/blockchain/accounts/{user_wallet}", headers=headers)
                    user_raw = usr.json().get("address", user_wallet) if usr.status_code == 200 else user_wallet
                except Exception:
                    user_raw = user_wallet

                # Get transactions for the receiver wallet via TonAPI
                response = await client.get(
                    f"{base_url}/v2/blockchain/accounts/{receiver_raw}/transactions",
                    params={
                        "limit": 50
                    },
                    headers=headers
                )

                if response.status_code != 200:
                    logger.error(f"TonAPI error: {response.status_code} - {response.text}")
                    return False, {"error": f"API request failed: {response.status_code}"}

                data = response.json()

                # TonAPI returns list in 'transactions'
                transactions = data.get("transactions", []) or data.get("result", [])
                logger.info(f"TonAPI: found {len(transactions)} recent transactions for receiver wallet")

                # Look for matching transaction
                for tx in transactions:
                    try:
                        # Get transaction details
                        # TonAPI transaction schema
                        in_msg = tx.get("in_msg") or tx.get("in_msg_value") or tx.get("in_msg_data") or {}
                        if not in_msg:
                            # TonAPI also exposes 'in_msg' fields at top-level sometimes
                            in_msg = {
                                "source": tx.get("in_msg", {}).get("source") if isinstance(tx.get("in_msg"), dict) else None,
                                "destination": tx.get("in_msg", {}).get("destination") if isinstance(tx.get("in_msg"), dict) else None,
                                "value": (tx.get("in_msg", {}) or {}).get("value") if isinstance(tx.get("in_msg"), dict) else None
                            }

                        # Resolve fields from TonAPI structure variants
                        src_obj = in_msg.get("source") or {}
                        dst_obj = in_msg.get("destination") or {}
                        source = (src_obj.get("address") if isinstance(src_obj, dict) else src_obj) or ""
                        destination = (dst_obj.get("address") if isinstance(dst_obj, dict) else dst_obj) or ""
                        raw_value = in_msg.get("value") or (tx.get("in_msg", {}) or {}).get("value") or 0
                        try:
                            value = int(raw_value)
                        except Exception:
                            value = int(float(raw_value)) if raw_value else 0

                        # Check if transaction matches our criteria (destination already filtered by endpoint)
                        if (source == user_raw and
                            min_amount <= value <= max_amount):

                            # Get additional transaction info
                            tx_hash = tx.get("hash", "") or (tx.get("transaction_id", {}) or {}).get("hash", "")
                            lt = tx.get("lt", "") or (tx.get("transaction_id", {}) or {}).get("lt", "")
                            utime = tx.get("utime", 0) or tx.get("now", 0) or tx.get("timestamp", 0)
                            fee_field = tx.get("total_fees")
                            if isinstance(fee_field, dict):
                                fee = int(fee_field.get("value", 0) or 0)
                            elif fee_field is not None:
                                fee = int(fee_field)
                            else:
                                fee = int(tx.get("fee", 0) or 0)

                            # Check transaction age (must be recent - within last 30 minutes)
                            current_time = int(time.time())
                            max_age = 1800  # 30 minutes

                            if current_time - utime > max_age:
                                logger.info(f"Transaction too old: {current_time - utime} seconds")
                                continue

                            # Transaction found and verified!
                            blockchain_data = {
                                "transaction_hash": tx_hash,
                                "logical_time": lt,
                                "utime": utime,
                                "source_address": source,
                                "destination_address": destination or receiver_raw,
                                "value_nanotons": value,
                                "value_tons": value / 1000000000,
                                "fee_nanotons": fee,
                                "fee_tons": fee / 1000000000,
                                "expected_nanotons": expected_amount_nanotons,
                                "expected_tons": float(expected_amount_ton),
                                "tolerance_nanotons": tolerance,
                                "verified_at": current_time,
                                "age_seconds": current_time - utime,
                                "api_source": "tonapi_testnet"
                            }

                            logger.info(f"Transaction verified successfully: "
                                        f"hash={tx_hash[:16]}..., value={value} nanotons, "
                                        f"expected={expected_amount_nanotons}±{tolerance} nanotons")

                            return True, blockchain_data

                    except (ValueError, KeyError, TypeError) as e:
                        logger.warning(f"Error parsing transaction: {e}")
                        continue

                # No matching transaction found
                logger.info(f"TonAPI: no matching transaction found. Checked {len(transactions)} transactions.")
                return False, {
                    "verification_failed": True,
                    "reason": "No matching transaction found",
                    "searched_transactions": len(transactions),
                    "expected_amount_nanotons": expected_amount_nanotons,
                    "tolerance": tolerance,
                    "source_wallet": user_raw,
                    "destination_wallet": receiver_raw,
                    "api_source": "tonapi_testnet"
                }

        except httpx.TimeoutException:
            logger.error("Timeout while verifying transaction on blockchain")
            return False, {"error": "Blockchain API timeout"}

        except httpx.RequestError as e:
            logger.error(f"Network error while verifying transaction: {e}")
            return False, {"error": f"Network error: {str(e)}"}

        except Exception as e:
            logger.error(f"Unexpected error in blockchain verification: {e}", exc_info=True)
            return False, {"error": f"Verification error: {str(e)}"}
