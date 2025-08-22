from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from decimal import Decimal
import time
from datetime import datetime
from typing import Tuple, Optional

from models.models import (
    UsersWallets, Deposits, Transactions, Activity,
    ForeversExchangeStats, Forevers, Settings
)
from utils.random_hash import random_hash


class ForeversPurchaseService:

    @staticmethod
    async def validate_purchase_data(
        wallet_type: str,
        forever_type: str,
        forevers_amount: int,
        final_rate: Decimal,
        usd_amount: Decimal,
        db: AsyncSession
    ) -> Tuple[bool, str]:
        """Validate purchase data"""
        
        # Validate wallet type
        if wallet_type not in ['bonus', 'rent']:
            return False, "Invalid wallet type selected."
        
        # Validate forever type
        if forever_type not in ['UAE', 'KZ', 'DE', 'PL', 'UA']:
            return False, "Invalid Forever type selected."
        
        # Validate forevers amount
        if forevers_amount <= 0:
            return False, "Please enter a valid amount of Forevers (greater than 0)."
        
        # Validate rate and amount consistency
        expected_usd = round(forevers_amount * final_rate, 2)
        if abs(float(usd_amount) - float(expected_usd)) > 0.01:  # Allow small floating point differences
            return False, "USD amount doesn't match the calculated amount."
        
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
            # Validate inputs
            is_valid, error_msg = await ForeversPurchaseService.validate_purchase_data(
                wallet_type, forever_type, forevers_amount, final_rate, usd_amount, db
            )
            if not is_valid:
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
