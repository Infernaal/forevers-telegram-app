from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from decimal import Decimal
import time
import logging
from datetime import datetime
from typing import Tuple, Optional

from models.models import (
    UsersWallets, Deposits, Transactions, Activity,
    ForeversExchangeStats, Forevers
)
from utils.random_hash import random_hash

logger = logging.getLogger(__name__)


class ForeversPurchaseService:

    @staticmethod
    async def validate_purchase_data(
        wallet_type: str,
        forever_type: str,
        forevers_amount: int,
        final_rate: Decimal,
        usd_amount: Decimal,
        user_id: int,
        db: AsyncSession
    ) -> Tuple[bool, str]:
        """Validate purchase data with security checks"""

        # Log validation attempt for audit
        logger.info(f"Validating purchase: user_id={user_id}, wallet_type={wallet_type}, "
                   f"forever_type={forever_type}, amount={forevers_amount}, rate={final_rate}, usd={usd_amount}")

        # Validate wallet type
        if wallet_type not in ['bonus', 'rent']:
            logger.warning(f"Invalid wallet type attempt: user_id={user_id}, wallet_type={wallet_type}")
            return False, "Invalid wallet type selected."

        # Validate forever type (basic validation - just check it's not empty)
        if not forever_type or not forever_type.strip():
            return False, "Forever type is required."

        # Validate forevers amount
        if forevers_amount <= 0:
            return False, "Please enter a valid amount of Forevers (greater than 0)."

        # Security check: validate amount is not suspiciously high
        max_forevers_per_transaction = 1000000  # Adjust as needed
        if forevers_amount > max_forevers_per_transaction:
            logger.warning(f"Suspicious high amount attempt: user_id={user_id}, amount={forevers_amount}")
            return False, f"Amount too high: {forevers_amount}. Maximum allowed per transaction: {max_forevers_per_transaction}"

        # Validate rate and amount consistency (CRITICAL SECURITY CHECK)
        # Recalculate the expected USD amount on backend to prevent tampering
        expected_usd = round(Decimal(forevers_amount) * final_rate, 2)
        actual_usd = round(usd_amount, 2)

        # Check if amounts match (allow small floating point differences)
        if abs(actual_usd - expected_usd) > Decimal('0.01'):
            logger.error(f"SECURITY ALERT - Amount mismatch: user_id={user_id}, "
                        f"expected=${expected_usd}, received=${actual_usd}, "
                        f"calculation={forevers_amount}×{final_rate}=${expected_usd}")
            return False, f"Security validation failed: USD amount mismatch. Expected: ${expected_usd}, Received: ${actual_usd}. Calculation: {forevers_amount} × {final_rate} = ${expected_usd}"

        # Additional validation: ensure final_rate is positive and reasonable
        if final_rate <= 0:
            logger.warning(f"Invalid rate attempt: user_id={user_id}, rate={final_rate}")
            return False, "Invalid exchange rate: must be greater than 0."

        # Additional validation: ensure final_rate is not suspiciously high (anti-fraud)
        max_reasonable_rate = Decimal('1000.00')  # Adjust this limit as needed
        if final_rate > max_reasonable_rate:
            logger.warning(f"Suspicious high rate attempt: user_id={user_id}, rate={final_rate}")
            return False, f"Exchange rate too high: ${final_rate}. Maximum allowed: ${max_reasonable_rate}"

        # Log successful validation
        logger.info(f"Purchase validation passed: user_id={user_id}, expected_usd=${expected_usd}")
        return True, "Valid"
    
    @staticmethod
    async def check_wallet_balance(
        user_id: int,
        wallet_type: str,
        required_amount: Decimal,
        db: AsyncSession
    ) -> Tuple[bool, Optional[dict], str]:
        """Check if user has sufficient wallet balance"""
        
        stmt = select(UsersWallets).where(
            UsersWallets.uid == user_id,
            UsersWallets.wallet_type == wallet_type
        )
        result = await db.execute(stmt)
        wallet = result.scalar_one_or_none()
        
        if not wallet:
            return False, None, "Selected wallet not found."
        
        if wallet.amount < required_amount:
            wallet_display = "Loyalty Program" if wallet_type == "rent" else "Bonus Reward"
            return False, None, f"Insufficient balance in {wallet_display} wallet."
        
        return True, {
            'id': wallet.id,
            'amount': wallet.amount,
            'currency': wallet.currency
        }, "Sufficient balance"
    
    @staticmethod
    async def process_purchase(
        user_id: int,
        wallet_type: str,
        forever_type: str,
        forevers_amount: int,
        final_rate: Decimal,
        usd_amount: Decimal,
        ip_address: str,
        db: AsyncSession
    ) -> Tuple[bool, dict, str]:
        """Process the forevers purchase transaction"""
        
        try:
            # Validate inputs with security checks
            is_valid, error_msg = await ForeversPurchaseService.validate_purchase_data(
                wallet_type, forever_type, forevers_amount, final_rate, usd_amount, user_id, db
            )
            if not is_valid:
                logger.warning(f"Purchase validation failed for user {user_id}: {error_msg}")
                return False, {}, error_msg
            
            # Check wallet balance
            has_balance, wallet_data, balance_msg = await ForeversPurchaseService.check_wallet_balance(
                user_id, wallet_type, usd_amount, db
            )
            if not has_balance:
                return False, {}, balance_msg
            
            # Generate transaction IDs
            txid = f'EXCH{random_hash(12)}'
            reference_number = f'EXCH{random_hash(8).upper()}'

            current_time = int(time.time())
            current_datetime = datetime.now()

            # Final security check: re-verify calculation before database operations
            final_verification_usd = round(Decimal(forevers_amount) * final_rate, 2)
            if abs(usd_amount - final_verification_usd) > Decimal('0.01'):
                logger.critical(f"CRITICAL SECURITY BREACH: Final verification failed for user {user_id}. "
                               f"Transaction blocked. Expected: {final_verification_usd}, Got: {usd_amount}")
                return False, {}, "Transaction blocked: Final security verification failed"

            # Log transaction initiation
            logger.info(f"Initiating purchase transaction: user_id={user_id}, txid={txid}, "
                       f"amount={forevers_amount} {forever_type}, usd=${usd_amount}, wallet={wallet_type}")
            
            # Update wallet balance
            new_wallet_amount = wallet_data['amount'] - usd_amount
            
            update_wallet_stmt = update(UsersWallets).where(
                UsersWallets.uid == user_id,
                UsersWallets.wallet_type == wallet_type
            ).values(
                amount=new_wallet_amount,
                updated=current_time
            )
            await db.execute(update_wallet_stmt)
            
            # Create deposit record
            deposit = Deposits(
                uid=user_id,
                txid=txid,
                method=998,  # Exchange gateway ID
                amount=str(usd_amount),
                currency='USD',
                requested_on=current_time,
                processed_on=0,
                reference_number=reference_number,
                status=1,
                rate_at_deposit=final_rate,
                is_exchange=1,
                type=forever_type,
                ip_address=ip_address
            )
            db.add(deposit)
            await db.flush()  # Get the ID without committing
            
            deposit_id = deposit.id
            
            # Create transaction record
            description = f"Forevers {forever_type} purchased from {wallet_type} wallet (User ID: {user_id})"
            transaction = Transactions(
                txid=txid,
                type=3,
                sender=user_id,
                recipient=deposit_id,
                description=description,
                deposit_via=998,
                amount=str(usd_amount),
                currency='USD',
                fee='',
                status=1,
                created=current_time
            )
            db.add(transaction)
            
            # Create activity record
            activity = Activity(
                txid=txid,
                type=3,
                uid=user_id,
                deposit_via=998,
                u_field_1=str(deposit_id),
                amount=str(usd_amount),
                currency='USD',
                status=3,
                created=current_time
            )
            db.add(activity)
            
            # Create exchange stats record
            exchange_stats = ForeversExchangeStats(
                user_id=user_id,
                wallet_type=wallet_type,
                forevers_amount=Decimal(forevers_amount),
                usd_amount=usd_amount,
                exchange_rate=final_rate,
                txid=txid,
                date_exchanged=current_datetime,
                ip_address=ip_address,
                forever_type=forever_type
            )
            db.add(exchange_stats)
            await db.flush()
            
            # Commit all changes
            await db.commit()

            # Log successful transaction
            logger.info(f"Purchase transaction completed successfully: user_id={user_id}, txid={txid}, "
                       f"forevers={forevers_amount} {forever_type}, usd=${usd_amount}, "
                       f"new_balance=${new_wallet_amount}, stats_id={exchange_stats.id}")

            return True, {
                'txid': txid,
                'wallet_type': wallet_type,
                'forever_type': forever_type,
                'forevers_amount': forevers_amount,
                'usd_amount': usd_amount,
                'final_rate': final_rate,
                'new_wallet_balance': new_wallet_amount,
                'exchange_stats_id': exchange_stats.id
            }, f"Successfully purchased {forevers_amount} {forever_type} Forevers"
            
        except Exception as e:
            await db.rollback()
            return False, {}, f"An error occurred during purchase: {str(e)}"
