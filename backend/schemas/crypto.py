from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class CryptoInitRequest(BaseModel):
    usd_amount: float = Field(..., gt=0)
    wallet_address: str = Field(..., min_length=10)
    forevers_price: Optional[float] = None
    forevers_type: Optional[str] = None

class TonMessage(BaseModel):
    address: str
    amount: str
    payload: Optional[str] = None

class TonConnectTx(BaseModel):
    validUntil: int
    messages: List[TonMessage]

class CryptoInitResponse(BaseModel):
    status: str
    message: str
    verify_id: str
    rate_usd_per_ton: float
    amount_ton: float
    network_fee_ton: float
    total_ton: float
    ton_connect_tx: TonConnectTx
    data: Optional[Dict[str, Any]] = None

class CryptoVerifyResponse(BaseModel):
    status: str
    message: str
    verified: bool
    deposit_id: Optional[int] = None
    tx_hash: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
