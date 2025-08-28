from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import logging

from db.database import get_db
from dependencies.current_user import get_current_user_id
from schemas.crypto_purchase import (
    CryptoInitRequest,
    CryptoInitResponse,
    CryptoVerifyRequest,
    CryptoVerifyResponse
)
from services.crypto_purchase_service import CryptoPurchaseService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/forevers/crypto", tags=["Crypto Purchase"])


@router.post("/init", response_model=CryptoInitResponse)
async def init_crypto_purchase(
    purchase_data: CryptoInitRequest,
    request: Request,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    """
    Initialize a crypto purchase transaction for TON Connect
    
    This endpoint:
    1. Validates the purchase request
    2. Converts USD to TON at current market rate
    3. Creates a pending deposit record
    4. Returns transaction data for Ton Connect
    
    Args:
        purchase_data: Purchase details including USD amount and wallet addresses
        request: FastAPI request object to get client IP
        current_user_id: ID of the authenticated user
        db: Database session
        
    Returns:
        CryptoInitResponse with transaction data for Ton Connect or error message
    """
    try:
        # Get client IP address for logging
        client_ip = request.client.host
        if hasattr(request, 'headers'):
            forwarded_for = request.headers.get('X-Forwarded-For')
            real_ip = request.headers.get('X-Real-IP')
            client_ip = forwarded_for or real_ip or client_ip

        # Log crypto purchase initialization attempt
        logger.info(f"Crypto purchase init: user_id={current_user_id}, ip={client_ip}, "
                   f"amount_usd={purchase_data.amount_usd}, "
                   f"user_wallet={purchase_data.user_wallet[:10]}..., "
                   f"receiver_wallet={purchase_data.receiver_wallet[:10]}...")

        # Process the initialization
        success, result_data, message = await CryptoPurchaseService.init_crypto_purchase(
            user_id=current_user_id,
            amount_usd=purchase_data.amount_usd,
            user_wallet=purchase_data.user_wallet,
            receiver_wallet=purchase_data.receiver_wallet,
            rate_as_deposit=purchase_data.rate_as_deposit,
            db=db
        )

        if success:
            logger.info(f"Crypto purchase init successful: user_id={current_user_id}, "
                       f"request_id={result_data.get('request_id')}, "
                       f"deposit_id={result_data.get('deposit_id')}")
            
            return CryptoInitResponse(
                status="success",
                message=message,
                data=result_data
            )
        else:
            logger.warning(f"Crypto purchase init failed: user_id={current_user_id}, "
                          f"ip={client_ip}, reason={message}")
            
            return CryptoInitResponse(
                status="failed",
                message=message
            )

    except Exception as e:
        logger.error(f"Unexpected error in crypto init endpoint: "
                    f"user_id={current_user_id}, error={str(e)}", exc_info=True)
        
        return CryptoInitResponse(
            status="failed",
            message=f"An unexpected error occurred: {str(e)}"
        )


@router.post("/verify", response_model=CryptoVerifyResponse)
async def verify_crypto_transaction(
    verify_data: CryptoVerifyRequest,
    request: Request,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    """
    Verify a crypto transaction and update deposit status
    
    This endpoint:
    1. Finds the pending deposit by request_id
    2. Verifies the transaction on TON blockchain
    3. Updates deposit status based on verification result
    4. Creates transaction records if successful
    5. Handles idempotent operations
    
    Args:
        verify_data: Verification request with request_id
        request: FastAPI request object to get client IP
        current_user_id: ID of the authenticated user
        db: Database session
        
    Returns:
        CryptoVerifyResponse with verification status and transaction details
    """
    try:
        # Get client IP address for logging
        client_ip = request.client.host
        if hasattr(request, 'headers'):
            forwarded_for = request.headers.get('X-Forwarded-For')
            real_ip = request.headers.get('X-Real-IP')
            client_ip = forwarded_for or real_ip or client_ip

        # Log verification attempt
        logger.info(f"Crypto transaction verify: user_id={current_user_id}, "
                   f"ip={client_ip}, request_id={verify_data.request_id}")

        # Process the verification
        success, result_data, message = await CryptoPurchaseService.verify_crypto_transaction(
            user_id=current_user_id,
            request_id=verify_data.request_id,
            db=db
        )

        if success:
            transaction_status = result_data.get("transaction_status", "unknown")
            
            logger.info(f"Crypto transaction verify result: user_id={current_user_id}, "
                       f"request_id={verify_data.request_id}, status={transaction_status}")
            
            return CryptoVerifyResponse(
                status="success",
                message=message,
                transaction_status=transaction_status,
                data=result_data
            )
        else:
            logger.warning(f"Crypto transaction verify failed: user_id={current_user_id}, "
                          f"request_id={verify_data.request_id}, reason={message}")
            
            return CryptoVerifyResponse(
                status="failed",
                message=message,
                transaction_status="failed"
            )

    except Exception as e:
        logger.error(f"Unexpected error in crypto verify endpoint: "
                    f"user_id={current_user_id}, request_id={verify_data.request_id}, "
                    f"error={str(e)}", exc_info=True)
        
        return CryptoVerifyResponse(
            status="failed",
            message=f"An unexpected error occurred: {str(e)}",
            transaction_status="failed"
        )


@router.get("/status/{request_id}", response_model=CryptoVerifyResponse)
async def get_crypto_transaction_status(
    request_id: str,
    request: Request,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    """
    Get the current status of a crypto transaction
    
    This is a convenience endpoint that provides the same functionality as verify
    but uses GET method for easier polling from frontend
    
    Args:
        request_id: The request ID from the init response
        request: FastAPI request object
        current_user_id: ID of the authenticated user
        db: Database session
        
    Returns:
        CryptoVerifyResponse with current transaction status
    """
    try:
        # Reuse the verify logic
        success, result_data, message = await CryptoPurchaseService.verify_crypto_transaction(
            user_id=current_user_id,
            request_id=request_id,
            db=db
        )

        if success:
            transaction_status = result_data.get("transaction_status", "unknown")
            
            return CryptoVerifyResponse(
                status="success",
                message=message,
                transaction_status=transaction_status,
                data=result_data
            )
        else:
            return CryptoVerifyResponse(
                status="failed",
                message=message,
                transaction_status="failed"
            )

    except Exception as e:
        logger.error(f"Error getting crypto transaction status: "
                    f"user_id={current_user_id}, request_id={request_id}, "
                    f"error={str(e)}", exc_info=True)
        
        return CryptoVerifyResponse(
            status="failed",
            message=f"An unexpected error occurred: {str(e)}",
            transaction_status="failed"
        )
