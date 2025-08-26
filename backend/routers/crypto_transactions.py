from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any

from dependencies.current_user import get_current_user
from db.database import get_db
from schemas.crypto_transactions import (
    CryptoInitRequest, CryptoInitResponse,
    CryptoVerifyRequest, CryptoVerifyResponse
)
from services.ton_transactions_service import TonTransactionService
from models.models import Users

router = APIRouter(prefix="/forevers/crypto", tags=["Crypto Transactions"])


@router.post("/init", response_model=CryptoInitResponse)
async def init_crypto_transaction(
    request: CryptoInitRequest,
    current_user: Users = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Initialize crypto transaction with USD to TON conversion and create deposit record
    """
    try:
        # Get USD to TON conversion rate
        conversion_data = await TonTransactionService.get_usd_to_ton_conversion(
            request.usd_amount
        )
        
        # Initiate transaction with converted TON amount
        result = await TonTransactionService.initiate_ton_transaction(
            user_id=current_user.id,
            usd_amount=request.usd_amount,
            ton_amount=conversion_data["ton_amount"],
            wallet_address=request.wallet_address,
            forevers_details=request.forevers_details,
            ip_address=request.ip_address or "0.0.0.0",
            db=db
        )
        
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
            
        return {
            "status": "success",
            "deposit_id": result["deposit_id"],
            "txid": result["txid"],
            "recipient_address": result["recipient_address"],
            "ton_amount": result["ton_amount"],
            "ton_rate": conversion_data["ton_rate"],
            "rate_source": conversion_data["rate_source"],
            "expires_at": result["expires_at"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transaction initialization failed: {str(e)}")


@router.post("/verify", response_model=CryptoVerifyResponse)
async def verify_crypto_transaction(
    request: CryptoVerifyRequest,
    current_user: Users = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Verify crypto transaction on blockchain and complete purchase
    """
    try:
        result = await TonTransactionService.verify_and_complete_transaction(
            tx_hash=request.tx_hash,
            deposit_id=request.deposit_id,
            user_id=current_user.id,
            db=db
        )
        
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
            
        return {
            "status": "success",
            "verified": result["verified"],
            "deposit_id": result["deposit_id"],
            "forevers_credited": result["forevers_credited"],
            "tx_hash": result["tx_hash"],
            "verification_details": result.get("verification_details", {})
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transaction verification failed: {str(e)}")
