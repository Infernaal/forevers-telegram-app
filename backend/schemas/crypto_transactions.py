from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from decimal import Decimal


class ForeversDetail(BaseModel):
    code: str = Field(..., description="Forever type code (UAE, KZ, DE, PL, UA)")
    country: str = Field(..., description="Country name")
    amount: int = Field(..., gt=0, description="Amount of forevers")
    usd_rate: Decimal = Field(..., gt=0, description="USD rate per forever")
    total_cost: Decimal = Field(..., gt=0, description="Total cost for this type")


class CryptoInitRequest(BaseModel):
    usd_amount: Decimal = Field(..., gt=0, description="Total USD amount")
    wallet_address: str = Field(..., description="User's TON wallet address")
    forevers_details: List[ForeversDetail] = Field(..., description="Details of forevers being purchased")
    ip_address: Optional[str] = Field(None, description="User's IP address")


class CryptoInitResponse(BaseModel):
    status: str
    deposit_id: int
    txid: str
    recipient_address: str
    ton_amount: Decimal
    ton_rate: Decimal
    rate_source: str
    expires_at: int


class CryptoVerifyRequest(BaseModel):
    tx_hash: str = Field(..., description="Transaction hash from blockchain")
    deposit_id: int = Field(..., description="Deposit ID from init response")


class CryptoVerifyResponse(BaseModel):
    status: str
    verified: bool
    deposit_id: int
    forevers_credited: Dict[str, Decimal]
    tx_hash: str
    verification_details: Dict[str, Any]
