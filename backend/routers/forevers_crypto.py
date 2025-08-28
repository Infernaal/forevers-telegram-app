from fastapi import APIRouter, Depends, HTTPException
from fastapi import Request
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from dependencies.current_user import get_current_user_id
from schemas.crypto import CryptoInitRequest, CryptoInitResponse, CryptoVerifyResponse
from services.forevers_crypto_service import ForeversCryptoService

router = APIRouter(prefix="/forevers/crypto", tags=["Forevers Crypto"])

@router.post("/init", response_model=CryptoInitResponse)
async def init_crypto_payment(
    payload: CryptoInitRequest,
    current_user_id: int = Depends(get_current_user_id)
):
    ok, data, msg = await ForeversCryptoService.init_payment(
        current_user_id,
        Decimal(str(payload.usd_amount)),
        payload.wallet_address,
        Decimal(str(payload.forevers_price)) if getattr(payload, "forevers_price", None) is not None else None,
        getattr(payload, "forevers_type", None)
    )
    if not ok:
        raise HTTPException(status_code=400, detail=msg)
    return CryptoInitResponse(
        status="success",
        message="OK",
        verify_id=data["verify_id"],
        rate_usd_per_ton=data["rate_usd_per_ton"],
        amount_ton=data["amount_ton"],
        network_fee_ton=data["network_fee_ton"],
        total_ton=data["total_ton"],
        ton_connect_tx=data["ton_connect_tx"],
        data=data
    )

@router.get("/verify", response_model=CryptoVerifyResponse)
async def verify_crypto_payment(
    id: str,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    ok, data, msg = await ForeversCryptoService.verify_payment(id, db)
    if not ok:
        return CryptoVerifyResponse(status="failed", message=msg, verified=False, data=data)
    return CryptoVerifyResponse(status="success", message="Verified", verified=True, deposit_id=data.get("deposit_id"), tx_hash=data.get("tx_hash"), data=data)
