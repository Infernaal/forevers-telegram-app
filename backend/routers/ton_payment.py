from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import logging
from typing import Optional

from db.database import get_db
from dependencies.current_user import get_current_user_id
from schemas.ton_payment import (
    TONPaymentRequest,
    TONPaymentResponse,
    TONConfirmPaymentRequest,
    TONConfirmPaymentResponse,
    TONRateRequest,
    TONRateResponse,
    TONTransactionStatus,
    TONWalletInfo
)
from services.ton_payment_service import TONPaymentService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/ton", tags=["TON Payments"])


@router.post("/create-payment", response_model=TONPaymentResponse)
async def create_ton_payment(
    payment_request: TONPaymentRequest,
    request: Request,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    """
    Create TON payment request for Forevers purchase.
    
    This endpoint:
    1. Validates the payment request and purchase details
    2. Calculates required TON amount based on current exchange rate
    3. Creates a payment record with expiration time
    4. Returns payment details including recipient address and amount
    
    Args:
        payment_request: TON payment request with wallet address and purchase details
        request: FastAPI request object to get client IP
        current_user_id: ID of the authenticated user
        db: Database session
        
    Returns:
        TONPaymentResponse with payment details or error message
    """
    try:
        # Get client IP address
        client_ip = request.client.host
        if hasattr(request, 'headers'):
            # Try to get real IP from headers (for proxy/load balancer scenarios)
            forwarded_for = request.headers.get('X-Forwarded-For')
            real_ip = request.headers.get('X-Real-IP')
            client_ip = forwarded_for or real_ip or client_ip

        # Log payment creation attempt
        logger.info(f"Creating TON payment: user_id={current_user_id}, ip={client_ip}, "
                   f"wallet={payment_request.wallet_address}")
        
        # Create payment
        success, payment_data, message = await TONPaymentService.create_payment(
            user_id=current_user_id,
            wallet_address=payment_request.wallet_address,
            purchase_details=payment_request.purchase_details,
            ton_price=payment_request.ton_price,
            ip_address=client_ip,
            db=db
        )
        
        if success:
            logger.info(f"TON payment created: user_id={current_user_id}, payment_id={payment_data.get('payment_id')}")
            return TONPaymentResponse(
                status="success",
                message=message,
                payment_id=payment_data.get('payment_id'),
                recipient_address=payment_data.get('recipient_address'),
                amount_ton=payment_data.get('amount_ton'),
                amount_usd=payment_data.get('amount_usd'),
                memo=payment_data.get('memo'),
                expires_at=payment_data.get('expires_at')
            )
        else:
            logger.warning(f"TON payment creation failed: user_id={current_user_id}, reason={message}")
            return TONPaymentResponse(
                status="failed",
                message=message
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in create TON payment: user_id={current_user_id}, error={str(e)}", exc_info=True)
        return TONPaymentResponse(
            status="failed",
            message=f"An unexpected error occurred: {str(e)}"
        )


@router.post("/confirm-payment", response_model=TONConfirmPaymentResponse)
async def confirm_ton_payment(
    confirm_request: TONConfirmPaymentRequest,
    request: Request,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    """
    Confirm TON payment and process Forevers purchase.
    
    This endpoint:
    1. Verifies the TON transaction on blockchain
    2. Validates transaction matches payment request
    3. Processes Forevers purchase
    4. Creates deposit and transaction records
    5. Updates user wallet balances
    
    Args:
        confirm_request: Payment confirmation with transaction hash
        request: FastAPI request object to get client IP
        current_user_id: ID of the authenticated user
        db: Database session
        
    Returns:
        TONConfirmPaymentResponse with confirmation status and purchase details
    """
    try:
        # Get client IP address
        client_ip = request.client.host
        if hasattr(request, 'headers'):
            forwarded_for = request.headers.get('X-Forwarded-For')
            real_ip = request.headers.get('X-Real-IP')
            client_ip = forwarded_for or real_ip or client_ip

        # Log confirmation attempt
        logger.info(f"Confirming TON payment: user_id={current_user_id}, ip={client_ip}, "
                   f"payment_id={confirm_request.payment_id}, tx={confirm_request.transaction_hash}")
        
        # Confirm payment
        success, result_data, message = await TONPaymentService.confirm_payment(
            user_id=current_user_id,
            payment_id=confirm_request.payment_id,
            transaction_hash=confirm_request.transaction_hash,
            wallet_address=confirm_request.wallet_address,
            ip_address=client_ip,
            db=db
        )
        
        if success:
            logger.info(f"TON payment confirmed: user_id={current_user_id}, "
                       f"payment_id={confirm_request.payment_id}, "
                       f"forevers={result_data.get('forevers_purchased')}")
            return TONConfirmPaymentResponse(
                status="success",
                message=message,
                txid=result_data.get('txid'),
                forevers_purchased=result_data.get('forevers_purchased'),
                total_usd_spent=result_data.get('total_usd_spent'),
                data=result_data
            )
        else:
            # Check if payment is still pending verification
            if "pending" in message.lower():
                logger.info(f"TON payment pending: user_id={current_user_id}, payment_id={confirm_request.payment_id}")
                return TONConfirmPaymentResponse(
                    status="pending",
                    message=message
                )
            else:
                logger.warning(f"TON payment confirmation failed: user_id={current_user_id}, reason={message}")
                return TONConfirmPaymentResponse(
                    status="failed",
                    message=message
                )
            
    except Exception as e:
        logger.error(f"Unexpected error in confirm TON payment: user_id={current_user_id}, error={str(e)}", exc_info=True)
        return TONConfirmPaymentResponse(
            status="failed",
            message=f"An unexpected error occurred: {str(e)}"
        )


@router.get("/rate", response_model=TONRateResponse)
async def get_ton_rate(
    amount_usd: Optional[float] = None,
    current_user_id: int = Depends(get_current_user_id)
):
    """
    Get current TON exchange rate.
    
    Args:
        amount_usd: Optional USD amount to convert to TON
        current_user_id: ID of the authenticated user
        
    Returns:
        TONRateResponse with current exchange rate
    """
    try:
        rate_data = await TONPaymentService.get_current_rate(amount_usd)
        
        return TONRateResponse(
            ton_price_usd=rate_data['ton_price_usd'],
            amount_ton=rate_data.get('amount_ton'),
            last_updated=rate_data['last_updated'],
            source=rate_data['source']
        )
        
    except Exception as e:
        logger.error(f"Error getting TON rate: user_id={current_user_id}, error={str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get TON rate: {str(e)}")


@router.get("/transaction/{transaction_hash}", response_model=TONTransactionStatus)
async def get_transaction_status(
    transaction_hash: str,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    """
    Get TON transaction status and confirmation details.
    
    Args:
        transaction_hash: TON transaction hash to check
        current_user_id: ID of the authenticated user
        db: Database session
        
    Returns:
        TONTransactionStatus with transaction details
    """
    try:
        status_data = await TONPaymentService.get_transaction_status(
            transaction_hash=transaction_hash,
            user_id=current_user_id,
            db=db
        )
        
        return TONTransactionStatus(**status_data)
        
    except Exception as e:
        logger.error(f"Error getting transaction status: user_id={current_user_id}, "
                    f"tx={transaction_hash}, error={str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get transaction status: {str(e)}")


@router.get("/wallet/{wallet_address}", response_model=TONWalletInfo)
async def get_wallet_info(
    wallet_address: str,
    current_user_id: int = Depends(get_current_user_id)
):
    """
    Get TON wallet information including balance.
    
    Args:
        wallet_address: TON wallet address
        current_user_id: ID of the authenticated user
        
    Returns:
        TONWalletInfo with wallet details
    """
    try:
        wallet_data = await TONPaymentService.get_wallet_info(wallet_address)
        
        return TONWalletInfo(**wallet_data)
        
    except Exception as e:
        logger.error(f"Error getting wallet info: user_id={current_user_id}, "
                    f"wallet={wallet_address}, error={str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get wallet info: {str(e)}")


@router.delete("/payment/{payment_id}")
async def cancel_payment(
    payment_id: str,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    """
    Cancel pending TON payment.
    
    Args:
        payment_id: Payment ID to cancel
        current_user_id: ID of the authenticated user
        db: Database session
        
    Returns:
        Success/failure response
    """
    try:
        success, message = await TONPaymentService.cancel_payment(
            payment_id=payment_id,
            user_id=current_user_id,
            db=db
        )
        
        if success:
            return {"status": "success", "message": message}
        else:
            raise HTTPException(status_code=400, detail=message)
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error canceling payment: user_id={current_user_id}, "
                    f"payment_id={payment_id}, error={str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to cancel payment: {str(e)}")
