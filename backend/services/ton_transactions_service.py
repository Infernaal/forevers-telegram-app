import aiohttp
import asyncio
import logging
import time
from decimal import Decimal
from typing import Dict, Any, List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from datetime import datetime

from models.models import (
    Deposits, Transactions, Activity, Forevers, 
    ForeversLogs, ForeversExchangeStats
)
from utils.random_hash import random_hash

logger = logging.getLogger(__name__)

# TON Configuration
TON_CENTER_API_KEY = "e708de5ba87a75a37477cb89d6eef609dfe4ac47618c7707e3ce27beed3ae434"
TON_RECIPIENT_ADDRESS = "0QBgEwEKpmG4yPvn7-_VqljYE2s88oI6v7R2Vu_E8TvHjMGG"  # Replace with actual address
TON_NETWORK = "testnet"  # testnet or mainnet
TON_CENTER_BASE_URL = f"https://{TON_NETWORK}.toncenter.com/api/v2"


class TonTransactionService:

    @staticmethod
    async def get_usd_to_ton_conversion(usd_amount: Decimal) -> Dict[str, Any]:
        """
        Get USD to TON conversion rate using TonCenter API
        """
        try:
            # For testnet, we'll use a mock rate since real rates might not be available
            # In production, you would fetch from a real price API
            if TON_NETWORK == "testnet":
                # Mock rate: 1 TON = $6.50 USD (adjust as needed for testing)
                mock_ton_rate = Decimal("6.50")
                ton_amount = usd_amount / mock_ton_rate
                
                return {
                    "ton_amount": round(ton_amount, 9),  # TON has 9 decimal places
                    "ton_rate": mock_ton_rate,
                    "rate_source": "mock_testnet",
                    "rate_timestamp": int(time.time())
                }
            
            # For mainnet, fetch real rate
            async with aiohttp.ClientSession() as session:
                # You can use CoinGecko, CoinMarketCap, or other price APIs
                url = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd"
                
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        ton_price_usd = Decimal(str(data["the-open-network"]["usd"]))
                        ton_amount = usd_amount / ton_price_usd
                        
                        return {
                            "ton_amount": round(ton_amount, 9),
                            "ton_rate": ton_price_usd,
                            "rate_source": "coingecko",
                            "rate_timestamp": int(time.time())
                        }
                    else:
                        raise Exception(f"Failed to fetch TON price: {response.status}")
                        
        except Exception as e:
            logger.error(f"Error getting USD to TON conversion: {e}")
            # Fallback to mock rate
            mock_ton_rate = Decimal("6.50")
            ton_amount = usd_amount / mock_ton_rate
            
            return {
                "ton_amount": round(ton_amount, 9),
                "ton_rate": mock_ton_rate,
                "rate_source": "fallback_mock",
                "rate_timestamp": int(time.time())
            }

    @staticmethod
    async def initiate_ton_transaction(
        user_id: int,
        usd_amount: Decimal,
        ton_amount: Decimal,
        wallet_address: str,
        forevers_details: List[Dict],
        ip_address: str,
        db: AsyncSession
    ) -> Dict[str, Any]:
        """
        Initiate TON transaction and create deposit record
        """
        try:
            # Generate transaction IDs
            txid = f'TON{random_hash(12)}'
            reference_number = f'TON{random_hash(8).upper()}'
            current_time = int(time.time())

            # Validate forevers details
            if not forevers_details:
                return {"success": False, "error": "No forevers details provided"}

            # Calculate total forevers amount and validate
            total_forevers_usd = sum(Decimal(str(detail.get('total_cost', 0))) for detail in forevers_details)
            
            if abs(total_forevers_usd - usd_amount) > Decimal('0.01'):
                return {
                    "success": False,
                    "error": f"Amount mismatch: expected ${total_forevers_usd}, got ${usd_amount}"
                }

            # Create deposit record for TON payment
            deposit = Deposits(
                uid=user_id,
                txid=txid,
                method=8,  # Crypto gateway ID
                amount=str(usd_amount),
                currency='USD',
                requested_on=current_time,
                processed_on=0,  # Will be set when verified
                reference_number=reference_number,
                status=0,  # Pending verification
                is_exchange=0,  # This is a real deposit, not wallet exchange
                type=forevers_details[0].get('code', 'UAE'),  # Use first forever type
                ip_address=ip_address,
                gateway_txid='',  # Will be set when transaction is confirmed
                payment_data=f"wallet_address:{wallet_address},ton_amount:{ton_amount}"
            )
            
            db.add(deposit)
            await db.flush()  # Get the ID
            deposit_id = deposit.id

            # Create transaction record
            description = f"TON payment for Forevers (User ID: {user_id}, Wallet: {wallet_address})"
            transaction = Transactions(
                txid=txid,
                type=1,  # Deposit transaction type
                sender=0,  # External sender (blockchain)
                recipient=user_id,
                description=description,
                deposit_via=8,  # Crypto gateway
                amount=str(usd_amount),
                currency='USD',
                fee='',
                status=0,  # Pending
                created=current_time
            )
            db.add(transaction)

            # Create activity record
            activity = Activity(
                txid=txid,
                type=1,  # Deposit activity
                uid=user_id,
                deposit_via=8,
                u_field_1=str(deposit_id),
                u_field_2=wallet_address,
                u_field_3=str(ton_amount),
                amount=str(usd_amount),
                currency='USD',
                status=0,  # Pending
                created=current_time
            )
            db.add(activity)

            await db.commit()

            logger.info(f"TON transaction initiated: user_id={user_id}, txid={txid}, "
                       f"deposit_id={deposit_id}, ton_amount={ton_amount}")

            return {
                "success": True,
                "deposit_id": deposit_id,
                "txid": txid,
                "recipient_address": TON_RECIPIENT_ADDRESS,
                "ton_amount": ton_amount,
                "expires_at": current_time + 1800  # 30 minutes expiry
            }

        except Exception as e:
            await db.rollback()
            logger.error(f"Error initiating TON transaction: {e}")
            return {"success": False, "error": str(e)}

    @staticmethod
    async def verify_ton_transaction_on_blockchain(tx_hash: str) -> Dict[str, Any]:
        """
        Verify TON transaction on blockchain using TonCenter API
        """
        try:
            async with aiohttp.ClientSession() as session:
                # Get transaction details from TonCenter
                url = f"{TON_CENTER_BASE_URL}/getTransactions"
                params = {
                    "address": TON_RECIPIENT_ADDRESS,
                    "limit": 100,
                    "api_key": TON_CENTER_API_KEY
                }
                
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        if not data.get("ok"):
                            return {"verified": False, "error": "TonCenter API error"}
                        
                        transactions = data.get("result", [])
                        
                        # Look for our transaction
                        for tx in transactions:
                            # In a real implementation, you would match by transaction hash
                            # For now, we'll do a simplified verification
                            if tx.get("transaction_id", {}).get("hash") == tx_hash:
                                return {
                                    "verified": True,
                                    "transaction": tx,
                                    "amount_received": tx.get("in_msg", {}).get("value", "0"),
                                    "confirmation_time": tx.get("utime", 0)
                                }
                        
                        # If not found, it might be pending or failed
                        return {"verified": False, "error": "Transaction not found on blockchain"}
                    
                    else:
                        return {"verified": False, "error": f"TonCenter API error: {response.status}"}
                        
        except Exception as e:
            logger.error(f"Error verifying TON transaction: {e}")
            return {"verified": False, "error": str(e)}

    @staticmethod
    async def verify_and_complete_transaction(
        tx_hash: str,
        deposit_id: int,
        user_id: int,
        db: AsyncSession
    ) -> Dict[str, Any]:
        """
        Verify TON transaction and complete the purchase by crediting forevers
        """
        try:
            # Get deposit record
            stmt = select(Deposits).where(
                Deposits.id == deposit_id,
                Deposits.uid == user_id,
                Deposits.status == 0  # Pending
            )
            result = await db.execute(stmt)
            deposit = result.scalar_one_or_none()
            
            if not deposit:
                return {"success": False, "error": "Deposit not found or already processed"}

            # Verify transaction on blockchain
            verification = await TonTransactionService.verify_ton_transaction_on_blockchain(tx_hash)
            
            if not verification.get("verified"):
                return {
                    "success": False,
                    "error": f"Transaction verification failed: {verification.get('error', 'Unknown error')}"
                }

            # Update deposit status
            current_time = int(time.time())
            
            update_deposit_stmt = update(Deposits).where(
                Deposits.id == deposit_id
            ).values(
                status=1,  # Completed
                processed_on=current_time,
                gateway_txid=tx_hash
            )
            await db.execute(update_deposit_stmt)

            # Update transaction status
            update_tx_stmt = update(Transactions).where(
                Transactions.txid == deposit.txid
            ).values(
                status=1,  # Completed
                updated=current_time
            )
            await db.execute(update_tx_stmt)

            # Update activity status
            update_activity_stmt = update(Activity).where(
                Activity.txid == deposit.txid
            ).values(
                status=1,  # Completed
                updated=current_time
            )
            await db.execute(update_activity_stmt)

            # Parse forevers details from deposit and credit forevers
            forevers_credited = await TonTransactionService.credit_forevers_from_deposit(
                deposit, user_id, db
            )

            await db.commit()

            logger.info(f"TON transaction completed: deposit_id={deposit_id}, tx_hash={tx_hash}, "
                       f"forevers_credited={forevers_credited}")

            return {
                "success": True,
                "verified": True,
                "deposit_id": deposit_id,
                "forevers_credited": forevers_credited,
                "tx_hash": tx_hash,
                "verification_details": verification
            }

        except Exception as e:
            await db.rollback()
            logger.error(f"Error completing TON transaction: {e}")
            return {"success": False, "error": str(e)}

    @staticmethod
    async def credit_forevers_from_deposit(
        deposit: Deposits,
        user_id: int,
        db: AsyncSession
    ) -> Dict[str, Decimal]:
        """
        Credit forevers to user account based on deposit
        This mirrors the logic from forevers_purchase_service but for TON payments
        """
        try:
            # For now, we'll credit based on the deposit amount and type
            # In a full implementation, you'd parse the original forevers_details
            
            usd_amount = Decimal(deposit.amount)
            forever_type = deposit.type or 'UAE'
            
            # Get or create user's forevers record
            stmt = select(Forevers).where(Forevers.user_id == user_id)
            result = await db.execute(stmt)
            user_forevers = result.scalar_one_or_none()
            
            if not user_forevers:
                user_forevers = Forevers(user_id=user_id)
                db.add(user_forevers)
                await db.flush()

            # Calculate forevers amount based on type and current rates
            # You should get these rates from your settings or rate service
            forever_rates = {
                'UAE': Decimal('4.00'),
                'KZ': Decimal('10.00'),
                'DE': Decimal('10.00'),
                'PL': Decimal('1.25'),
                'UA': Decimal('0.75')
            }
            
            rate = forever_rates.get(forever_type, Decimal('4.00'))
            forevers_amount = usd_amount / rate
            
            # Update balance based on type
            balance_field = f'balance_{forever_type.lower()}'
            current_balance = getattr(user_forevers, balance_field, Decimal('0'))
            new_balance = current_balance + forevers_amount
            setattr(user_forevers, balance_field, new_balance)
            
            # Create forevers log
            forever_log = ForeversLogs(
                user_id=user_id,
                txid=deposit.txid,
                forever_value=rate,
                forever_balance=new_balance,
                action='credit',
                date_credited=datetime.now(),
                description=f'TON payment - {forever_type} Forevers credited',
                type=forever_type
            )
            db.add(forever_log)
            
            return {forever_type: forevers_amount}
            
        except Exception as e:
            logger.error(f"Error crediting forevers: {e}")
            raise e
