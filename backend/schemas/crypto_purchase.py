from pydantic import BaseModel, Field, conlist
from decimal import Decimal
from typing import List, Optional


class CryptoForeversItem(BaseModel):
    code: str
    amount: int
    usdRate: Decimal = Field(..., alias='usdRate')
    totalCost: Decimal


class CryptoInitiateRequest(BaseModel):
    forevers_details: conlist(CryptoForeversItem, min_items=1) = Field(..., alias='foreversDetails')
    ton_address: str = Field(..., alias='tonAddress')
    slippage_percent: Optional[float] = Field(2.0, alias='slippagePercent')


class CryptoInitiateResponse(BaseModel):
    status: str
    message: str
    order_id: str
    to_address: str
    amount_nano: int
    valid_until: int
    ton_price_usd: Decimal


class CryptoConfirmRequest(BaseModel):
    order_id: str
    from_address: str = Field(..., alias='fromAddress')
    amount_nano: Optional[int] = Field(None, alias='amountNano')


class CryptoConfirmResponse(BaseModel):
    status: str
    message: str
    tx_hash: Optional[str] = None
    deposit_ids: Optional[List[int]] = None
