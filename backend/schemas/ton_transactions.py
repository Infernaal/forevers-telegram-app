from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from decimal import Decimal


class TonConversionRequest(BaseModel):
    usd_amount: Decimal = Field(..., gt=0, description="Amount in USD to convert")


class TonConversionResponse(BaseModel):
    status: str
    usd_amount: Decimal
    ton_amount: Decimal
    ton_rate: Decimal
    rate_source: str
    rate_timestamp: int


class ForeversDetail(BaseModel):
    code: str = Field(..., description="Forever type code (UAE, KZ, DE, PL, UA)")
    country: str = Field(..., description="Country name")
    amount: int = Field(..., gt=0, description="Amount of forevers")
    usd_rate: Decimal = Field(..., gt=0, description="USD rate per forever")
    total_cost: Decimal = Field(..., gt=0, description="Total cost for this type")


class TonInitiateRequest(BaseModel):
    usd_amount: Decimal = Field(..., gt=0, description="Total USD amount")
    ton_amount: Decimal = Field(..., gt=0, description="Total TON amount") 
    wallet_address: str = Field(..., description="User's TON wallet address")
    forevers_details: List[ForeversDetail] = Field(..., description="Details of forevers being purchased")
    ip_address: Optional[str] = Field(None, description="User's IP address")


class TonInitiateResponse(BaseModel):
    status: str
    deposit_id: int
    txid: str
    recipient_address: str
    ton_amount: Decimal
    expires_at: int


class TonVerifyRequest(BaseModel):
    tx_hash: str = Field(..., description="Transaction hash from blockchain")
    deposit_id: int = Field(..., description="Deposit ID from initiate response")


class TonVerifyResponse(BaseModel):
    status: str
    verified: bool
    deposit_id: int
    forevers_credited: Dict[str, Decimal]
    tx_hash: str
    verification_details: Dict[str, Any]
