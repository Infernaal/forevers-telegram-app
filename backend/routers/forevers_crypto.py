from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from decimal import Decimal
from db.database import get_db
from dependencies.current_user import get_current_user_id
from schemas.forevers_crypto import (
    CryptoInitRequest, CryptoInitResponse, CryptoVerifyRequest, CryptoVerifyResponse
)
from services.crypto_payment_service import init_crypto_transaction, verify_crypto_transaction

router = APIRouter(prefix="/forevers/crypto", tags=["Forevers Crypto"])

@router.post("/init", response_model=CryptoInitResponse)
async def crypto_init(
    data: CryptoInitRequest,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    ok, payload, msg = await init_crypto_transaction(
        user_id=current_user_id,
        total_usd=Decimal(str(data.total_usd)),
        items=[i.model_dump() for i in data.items],
        db=db
    )
    if not ok:
        return CryptoInitResponse(status="failed", reference="", txid="", transaction={"to":"","amount":0,"payload":None,"validUntil":0})
    return CryptoInitResponse(status="success", reference=payload["reference"], txid=payload["txid"], transaction=payload["transaction"]) 

@router.post("/verify", response_model=CryptoVerifyResponse)
async def crypto_verify(
    data: CryptoVerifyRequest,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    ok, payload, msg = await verify_crypto_transaction(
        user_id=current_user_id,
        total_usd=Decimal(str(data.total_usd)),
        items=[i.model_dump() for i in data.items],
        payer_address=data.address,
        db=db,
        reference=data.reference
    )
    if not ok:
        return CryptoVerifyResponse(status="failed", message=msg)
    return CryptoVerifyResponse(status="success", message="ok", **payload)
