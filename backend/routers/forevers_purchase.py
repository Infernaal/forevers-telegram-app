from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
import logging

from db.database import get_db
from dependencies.current_user import get_current_user_id
from schemas.forevers_purchase import (
    ForeversPurchaseRequest,
    ForeversPurchaseResponse,
    ForeversPurchaseData
)
from services.forevers_purchase_service import ForeversPurchaseService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/forevers", tags=["Forevers Purchase"])


@router.post("/purchase", response_model=ForeversPurchaseResponse)
async def purchase_forevers(
    purchase_data: ForeversPurchaseRequest,
    request: Request,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    """
    Purchase Forevers using bonus or loyalty program (rent) wallet.
    
    This endpoint processes the purchase of Forevers by:
    1. Validating the purchase data
    2. Checking wallet balance
    3. Deducting from the selected wallet
    4. Creating deposit, transaction, and activity records
    5. Recording exchange statistics
    
    Args:
        purchase_data: Purchase details including wallet type, forever type, amounts
        request: FastAPI request object to get client IP
        current_user_id: ID of the authenticated user
        db: Database session
        
    Returns:
        ForeversPurchaseResponse with success/failure status and transaction details
    """
    try:
        # Get client IP address
        client_ip = request.client.host
        if hasattr(request, 'headers'):
            # Try to get real IP from headers (for proxy/load balancer scenarios)
            forwarded_for = request.headers.get('X-Forwarded-For')
            real_ip = request.headers.get('X-Real-IP')
            client_ip = forwarded_for or real_ip or client_ip

        # Log purchase attempt for security audit
        logger.info(f"Purchase attempt: user_id={current_user_id}, ip={client_ip}, "
                   f"wallet_type={purchase_data.wallet_type}, forever_type={purchase_data.forever_type}, "
                   f"amount={purchase_data.forevers_amount}, rate={purchase_data.final_rate}, "
                   f"usd={purchase_data.usd_amount}")
        
        # Process the purchase
        success, result_data, message = await ForeversPurchaseService.process_purchase(
            user_id=current_user_id,
            wallet_type=purchase_data.wallet_type,
            forever_type=purchase_data.forever_type,
            forevers_amount=purchase_data.forevers_amount,
            final_rate=purchase_data.final_rate,
            usd_amount=purchase_data.usd_amount,
            ip_address=client_ip,
            db=db
        )
        
        if success:
            logger.info(f"Purchase successful: user_id={current_user_id}, txid={result_data.get('txid')}")
            return ForeversPurchaseResponse(
                status="success",
                message=message,
                txid=result_data.get('txid'),
                data=result_data
            )
        else:
            logger.warning(f"Purchase failed: user_id={current_user_id}, ip={client_ip}, reason={message}")
            return ForeversPurchaseResponse(
                status="failed",
                message=message
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in purchase endpoint: user_id={current_user_id}, error={str(e)}", exc_info=True)
        return ForeversPurchaseResponse(
            status="failed",
            message=f"An unexpected error occurred: {str(e)}"
        )
