from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from dependencies.current_user import get_current_user_id
from schemas.crypto_purchase import (
    CryptoInitiateRequest,
    CryptoInitiateResponse,
    CryptoConfirmRequest,
    CryptoConfirmResponse
)
from services.ton_crypto_service import TonCryptoService

router = APIRouter(prefix="/forevers/crypto", tags=["Forevers Crypto"])


@router.post('/initiate', response_model=CryptoInitiateResponse)
async def initiate_crypto(
    body: CryptoInitiateRequest,
    request: Request,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    ip = request.client.host
    data = await TonCryptoService.initiate_order(
        user_id=current_user_id,
        items=[{
            'code': i.code,
            'amount': i.amount,
            'usdRate': str(i.usdRate),
            'totalCost': str(i.totalCost)
        } for i in body.forevers_details],
        ton_address=body.ton_address,
        ip_address=ip,
        slippage_percent=body.slippage_percent or 2.0,
        db=db
    )
    return CryptoInitiateResponse(
        status='success',
        message='Crypto order initiated',
        order_id=data['order_id'],
        to_address=data['to_address'],
        amount_nano=data['amount_nano'],
        valid_until=data['valid_until'],
        ton_price_usd=data['ton_price_usd']
    )


@router.post('/confirm', response_model=CryptoConfirmResponse)
async def confirm_crypto(
    body: CryptoConfirmRequest,
    current_user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    success, message, tx_hash, ids = await TonCryptoService.confirm_order(
        user_id=current_user_id,
        order_id=body.order_id,
        from_address=body.from_address,
        db=db
    )
    status = 'success' if success else 'failed'
    return CryptoConfirmResponse(status=status, message=message, tx_hash=tx_hash, deposit_ids=ids)
