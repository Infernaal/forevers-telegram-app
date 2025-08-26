from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional, Any, Dict

class TonInitRequest(BaseModel):
    forever_type: str
    forevers_amount: int
    final_rate: Decimal
    usd_amount: Decimal

class TonInitResponse(BaseModel):
    status: str
    message: str
    txid: Optional[str] = None
    data: Optional[Dict[str, Any]] = None

class TonVerifyRequest(BaseModel):
    txid: str
    wallet_address: str

class TonVerifyResponse(BaseModel):
    status: str
    message: str
    data: Optional[Dict[str, Any]] = None
