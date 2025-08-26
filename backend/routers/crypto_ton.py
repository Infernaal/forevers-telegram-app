from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Tuple

from db.database import get_db
from dependencies.current_user import get_current_user_id
from schemas.crypto_ton import TonInitRequest, TonInitResponse, TonVerifyRequest, TonVerifyResponse
from services.crypto_ton_service import CryptoTonService

router = APIRouter(prefix="/crypto/ton", tags=["TON Crypto"])

@router.post("/init", response_model=TonInitResponse)
async def init_ton_purchase(
    payload: TonInitRequest,
    request: Request,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    client_ip = request.client.host
    ok, data, msg = await CryptoTonService.init_transaction(
        db=db,
        user_id=current_user_id,
        forever_type=payload.forever_type,
        forevers_amount=payload.forevers_amount,
        final_rate=payload.final_rate,
        usd_amount=payload.usd_amount,
        ip_address=client_ip
    )
    status = "success" if ok else "failed"
    txid = data.get('txid') if data else None
    return TonInitResponse(status=status, message=msg, txid=txid, data=data if ok else None)

@router.post("/verify", response_model=TonVerifyResponse)
async def verify_ton_purchase(
    payload: TonVerifyRequest,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    ok, data, msg = await CryptoTonService.verify_and_finalize(
        db=db,
        user_id=current_user_id,
        txid=payload.txid,
        wallet_address=payload.wallet_address
    )
    status = "success" if ok else "failed"
    return TonVerifyResponse(status=status, message=msg, data=data if ok else { 'confirmed': False })
