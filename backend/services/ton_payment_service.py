from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, and_
from decimal import Decimal
import time
import logging
import json
import uuid
import asyncio
import aiohttp
from datetime import datetime, timedelta
from typing import Tuple, Optional, Dict, Any, List

from models.models import (
    UsersWallets, Deposits, Transactions, Activity,
    ForeversExchangeStats, Forevers, TONPayments
)
from utils.random_hash import random_hash

logger = logging.getLogger(__name__)


class TONPaymentService:
    """Service for handling TON payments and Forevers purchases"""
    
    # TON API endpoints
    TON_API_BASE = "https://toncenter.com/api/v2"
    COINGECKO_API = "https://api.coingecko.com/api/v3"
    
    # Payment configuration
    PAYMENT_EXPIRY_MINUTES = 30
    MIN_CONFIRMATIONS = 1
    
    # Company TON wallet address (replace with actual address)
    COMPANY_TON_ADDRESS = "EQDtFpEwcFAEcRe5mLVh2N6C0x-_hJEM7W61_JLnSF74p4q2"
    
    @staticmethod
    async def create_payment(
        user_id: int,
        wallet_address: str,
        purchase_details: Dict[str, Any],
        ton_price: Optional[Decimal],
        ip_address: str,
        db: AsyncSession
    ) -> Tuple[bool, Dict[str, Any], str]:
        """Create TON payment request"""
        
        try:
            # Log payment creation
            logger.info(f"Creating TON payment: user_id={user_id}, wallet={wallet_address}")
            
            # Validate purchase details
            if not purchase_details or 'foreversDetails' not in purchase_details:
                return False, {}, "Invalid purchase details"
            
            # Get current TON price if not provided
            if not ton_price:
                rate_data = await TONPaymentService.get_current_rate()
                ton_price = rate_data['ton_price_usd']
            
            # Calculate total USD amount
            total_usd = Decimal('0')
            for detail in purchase_details['foreversDetails']:
                total_usd += Decimal(str(detail.get('totalCost', 0)))
            
            if total_usd <= 0:
                return False, {}, "Invalid purchase amount"
            
            # Calculate required TON amount (add 5% buffer for price fluctuations)
            ton_amount = (total_usd / ton_price) * Decimal('1.05')
            
            # Generate payment ID with gateway ID 8 and memo
            payment_id = f"8_{str(uuid.uuid4())}"
            memo = f"FOREVERS_{payment_id[:8]}"
            
            # Calculate expiry time
            expires_at = datetime.utcnow() + timedelta(minutes=TONPaymentService.PAYMENT_EXPIRY_MINUTES)
            
            # Create payment record in database
            ton_payment = TONPayments(
                payment_id=payment_id,
                user_id=user_id,
                wallet_address=wallet_address,
                recipient_address=TONPaymentService.COMPANY_TON_ADDRESS,
                amount_ton=ton_amount,
                amount_usd=total_usd,
                ton_price=ton_price,
                purchase_details=json.dumps(purchase_details),
                status='created',
                memo=memo,
                ip_address=ip_address,
                expires_at=expires_at
            )

            db.add(ton_payment)
            await db.commit()

            logger.info(f"TON payment created: payment_id={payment_id}, amount_ton={ton_amount}, amount_usd={total_usd}")
            
            return True, {
                'payment_id': payment_id,
                'recipient_address': TONPaymentService.COMPANY_TON_ADDRESS,
                'amount_ton': ton_amount,
                'amount_usd': total_usd,
                'memo': memo,
                'expires_at': expires_at.isoformat()
            }, "Payment request created successfully"
            
        except Exception as e:
            logger.error(f"Error creating TON payment: user_id={user_id}, error={str(e)}", exc_info=True)
            return False, {}, f"Failed to create payment: {str(e)}"
    
    @staticmethod
    async def confirm_payment(
        user_id: int,
        payment_id: str,
        transaction_hash: str,
        wallet_address: str,
        ip_address: str,
        db: AsyncSession
    ) -> Tuple[bool, Dict[str, Any], str]:
        """Confirm TON payment and process Forevers purchase"""
        
        try:
            logger.info(f"Confirming TON payment: user_id={user_id}, payment_id={payment_id}")
            
            # Verify transaction on TON blockchain
            is_valid, tx_data = await TONPaymentService.verify_transaction(
                transaction_hash, wallet_address, TONPaymentService.COMPANY_TON_ADDRESS
            )
            
            if not is_valid:
                return False, {}, "Transaction verification failed"
            
            # Get stored payment details from database
            payment_result = await db.execute(
                select(TONPayments).where(
                    and_(
                        TONPayments.payment_id == payment_id,
                        TONPayments.user_id == user_id,
                        TONPayments.status.in_(['created', 'pending'])
                    )
                )
            )
            payment_record = payment_result.scalar_one_or_none()

            if not payment_record:
                return False, {}, "Payment not found or already processed"

            # Check if payment has expired
            if datetime.utcnow() > payment_record.expires_at:
                # Update status to expired
                await db.execute(
                    update(TONPayments).where(TONPayments.id == payment_record.id)
                    .values(status='expired')
                )
                await db.commit()
                return False, {}, "Payment has expired"

            # Parse purchase details
            purchase_details_data = json.loads(payment_record.purchase_details)
            payment_details = {
                'purchase_details': purchase_details_data,
                'amount_usd': payment_record.amount_usd,
                'amount_ton': payment_record.amount_ton
            }
            
            # Process Forevers purchase using existing logic
            purchase_results = []
            total_forevers = 0
            
            for detail in payment_details['purchase_details']['foreversDetails']:
                # Create individual purchase using existing purchase service patterns
                success, result = await TONPaymentService.process_forevers_purchase(
                    user_id=user_id,
                    forever_type=detail['code'],
                    forevers_amount=int(detail['amount']),
                    usd_amount=Decimal(str(detail['totalCost'])),
                    payment_method='ton',
                    transaction_hash=transaction_hash,
                    ip_address=ip_address,
                    db=db
                )
                
                if success:
                    purchase_results.append(result)
                    total_forevers += int(detail['amount'])
                else:
                    logger.error(f"Failed to process forevers purchase for {detail['code']}")
            
            if not purchase_results:
                # Update payment status to failed
                await db.execute(
                    update(TONPayments).where(TONPayments.id == payment_record.id)
                    .values(status='failed')
                )
                await db.commit()
                return False, {}, "Failed to process any Forevers purchases"

            # Update payment status to confirmed
            await db.execute(
                update(TONPayments).where(TONPayments.id == payment_record.id)
                .values(
                    status='confirmed',
                    transaction_hash=transaction_hash,
                    confirmed_at=datetime.utcnow(),
                    confirmations=tx_data.get('confirmations', 1),
                    block_height=tx_data.get('block_height')
                )
            )
            await db.commit()

            # Create main transaction record
            txid = random_hash(32)
            
            result_data = {
                'txid': txid,
                'transaction_hash': transaction_hash,
                'forevers_purchased': total_forevers,
                'total_usd_spent': payment_details['amount_usd'],
                'total_ton_spent': payment_details['amount_ton'],
                'purchase_results': purchase_results
            }
            
            logger.info(f"TON payment confirmed: user_id={user_id}, payment_id={payment_id}, "
                       f"forevers={total_forevers}, usd={payment_details['amount_usd']}")
            
            return True, result_data, "Payment confirmed and Forevers purchased successfully"
            
        except Exception as e:
            logger.error(f"Error confirming TON payment: user_id={user_id}, payment_id={payment_id}, "
                        f"error={str(e)}", exc_info=True)
            return False, {}, f"Failed to confirm payment: {str(e)}"
    
    @staticmethod
    async def process_forevers_purchase(
        user_id: int,
        forever_type: str,
        forevers_amount: int,
        usd_amount: Decimal,
        payment_method: str,
        transaction_hash: str,
        ip_address: str,
        db: AsyncSession
    ) -> Tuple[bool, Dict[str, Any]]:
        """Process individual Forevers purchase from TON payment using forevers_purchase_service logic"""
        
        try:
            # Generate transaction IDs using the same pattern as forevers_purchase_service
            txid = f'TON{random_hash(12)}'
            reference_number = f'TON{random_hash(8).upper()}'

            current_time = int(time.time())
            current_datetime = datetime.utcnow()

            # Create deposit record using forevers_purchase_service pattern
            deposit = Deposits(
                uid=user_id,
                txid=txid,
                method=8,  # Crypto gateway ID
                amount=str(usd_amount),
                currency='USD',
                requested_on=current_time,
                processed_on=current_time,
                reference_number=reference_number,
                status=1,  # Confirmed
                gateway_txid=transaction_hash,
                type=forever_type,
                ip_address=ip_address,
                processed=1
            )
            db.add(deposit)
            await db.flush()  # Get the ID without committing

            deposit_id = deposit.id

            # Create transaction record using forevers_purchase_service pattern
            description = f"Forevers {forever_type} purchased with TON (User ID: {user_id})"
            transaction = Transactions(
                txid=txid,
                type=1,  # Deposit type
                sender=user_id,
                recipient=deposit_id,
                description=description,
                deposit_via=8,  # Crypto gateway ID
                amount=str(usd_amount),
                currency='USD',
                fee='',
                status=1,  # Confirmed
                created=current_time
            )
            db.add(transaction)

            # Create activity record using forevers_purchase_service pattern
            activity = Activity(
                txid=txid,
                type=1,  # Deposit activity type
                uid=user_id,
                deposit_via=8,  # Crypto gateway ID
                u_field_1=str(deposit_id),
                u_field_2=transaction_hash,
                u_field_3=forever_type,
                amount=str(usd_amount),
                currency='USD',
                status=1,  # Confirmed
                created=current_time
            )
            db.add(activity)

            # Create exchange stats record
            exchange_stats = ForeversExchangeStats(
                user_id=user_id,
                wallet_type='bonus',  # Using bonus as default for crypto purchases
                forevers_amount=Decimal(forevers_amount),
                usd_amount=usd_amount,
                exchange_rate=usd_amount / Decimal(forevers_amount),
                txid=txid,
                date_exchanged=current_datetime,
                ip_address=ip_address,
                forever_type=forever_type
            )
            db.add(exchange_stats)
            await db.flush()
            
            # Commit all changes
            await db.commit()
            
            result = {
                'txid': txid,
                'deposit_id': deposit_id,
                'forever_type': forever_type,
                'forevers_amount': forevers_amount,
                'usd_amount': usd_amount,
                'transaction_hash': transaction_hash,
                'exchange_stats_id': exchange_stats.id
            }

            logger.info(f"TON Forevers purchase processed: user_id={user_id}, "
                       f"forever_type={forever_type}, amount={forevers_amount}, txid={txid}")
            
            return True, result
            
        except Exception as e:
            await db.rollback()
            logger.error(f"Error processing forevers purchase: user_id={user_id}, "
                        f"forever_type={forever_type}, error={str(e)}", exc_info=True)
            return False, {}
    
    @staticmethod
    async def verify_transaction(
        transaction_hash: str,
        from_address: str,
        to_address: str
    ) -> Tuple[bool, Dict[str, Any]]:
        """Verify TON transaction on blockchain"""
        
        try:
            # Simplified verification - in production, use actual TON API
            logger.info(f"Verifying TON transaction: hash={transaction_hash}")
            
            # For demo purposes, we'll simulate successful verification
            # In production, implement actual TON blockchain verification
            
            tx_data = {
                'transaction_hash': transaction_hash,
                'from_address': from_address,
                'to_address': to_address,
                'amount_ton': Decimal('10.5'),  # Simulated
                'amount_nanotons': '10500000000',
                'confirmations': 3,
                'block_height': 12345678,
                'timestamp': int(time.time()),
                'is_valid': True
            }
            
            return True, tx_data
            
        except Exception as e:
            logger.error(f"Error verifying transaction: hash={transaction_hash}, error={str(e)}")
            return False, {}
    
    @staticmethod
    async def get_current_rate(amount_usd: Optional[float] = None) -> Dict[str, Any]:
        """Get current TON exchange rate"""
        
        try:
            async with aiohttp.ClientSession() as session:
                # Get TON price from CoinGecko
                url = f"{TONPaymentService.COINGECKO_API}/simple/price?ids=the-open-network&vs_currencies=usd"
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        ton_price = Decimal(str(data['the-open-network']['usd']))
                    else:
                        # Fallback price
                        ton_price = Decimal('5.0')
            
            result = {
                'ton_price_usd': ton_price,
                'last_updated': datetime.utcnow().isoformat(),
                'source': 'coingecko'
            }
            
            if amount_usd:
                result['amount_ton'] = Decimal(str(amount_usd)) / ton_price
            
            return result
            
        except Exception as e:
            logger.error(f"Error getting TON rate: error={str(e)}")
            # Return fallback data
            return {
                'ton_price_usd': Decimal('5.0'),
                'amount_ton': Decimal(str(amount_usd or 0)) / Decimal('5.0') if amount_usd else None,
                'last_updated': datetime.utcnow().isoformat(),
                'source': 'fallback'
            }
    
    @staticmethod
    async def get_transaction_status(
        transaction_hash: str,
        user_id: int,
        db: AsyncSession
    ) -> Dict[str, Any]:
        """Get TON transaction status"""
        
        try:
            # Verify current status on blockchain
            is_valid, tx_data = await TONPaymentService.verify_transaction(
                transaction_hash, "", ""
            )
            
            if is_valid:
                return {
                    'transaction_hash': transaction_hash,
                    'status': 'confirmed' if tx_data['confirmations'] >= TONPaymentService.MIN_CONFIRMATIONS else 'pending',
                    'confirmations': tx_data['confirmations'],
                    'block_height': tx_data.get('block_height'),
                    'timestamp': tx_data.get('timestamp')
                }
            else:
                return {
                    'transaction_hash': transaction_hash,
                    'status': 'failed',
                    'confirmations': 0,
                    'block_height': None,
                    'timestamp': None
                }
                
        except Exception as e:
            logger.error(f"Error getting transaction status: hash={transaction_hash}, error={str(e)}")
            return {
                'transaction_hash': transaction_hash,
                'status': 'unknown',
                'confirmations': 0,
                'block_height': None,
                'timestamp': None
            }
    
    @staticmethod
    async def get_wallet_info(wallet_address: str) -> Dict[str, Any]:
        """Get TON wallet information"""
        
        try:
            # Simplified wallet info - in production, use actual TON API
            return {
                'address': wallet_address,
                'balance_ton': Decimal('100.5'),  # Simulated
                'balance_usd': Decimal('502.5'),  # Simulated
                'is_active': True
            }
            
        except Exception as e:
            logger.error(f"Error getting wallet info: address={wallet_address}, error={str(e)}")
            return {
                'address': wallet_address,
                'balance_ton': Decimal('0'),
                'balance_usd': Decimal('0'),
                'is_active': False
            }
    
    @staticmethod
    async def cancel_payment(
        payment_id: str,
        user_id: int,
        db: AsyncSession
    ) -> Tuple[bool, str]:
        """Cancel pending TON payment"""

        try:
            logger.info(f"Cancelling TON payment: payment_id={payment_id}, user_id={user_id}")

            # Find and update payment status
            result = await db.execute(
                update(TONPayments).where(
                    and_(
                        TONPayments.payment_id == payment_id,
                        TONPayments.user_id == user_id,
                        TONPayments.status.in_(['created', 'pending'])
                    )
                ).values(status='expired')
            )

            if result.rowcount == 0:
                return False, "Payment not found or cannot be cancelled"

            await db.commit()
            return True, "Payment cancelled successfully"

        except Exception as e:
            await db.rollback()
            logger.error(f"Error cancelling payment: payment_id={payment_id}, error={str(e)}")
            return False, f"Failed to cancel payment: {str(e)}"
