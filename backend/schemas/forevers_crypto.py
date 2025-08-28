from pydantic import BaseModel, Field
from typing import List, Optional

class CryptoItem(BaseModel):
    code: str
    amount: int
    usdRate: float
    totalCost: float

class CryptoInitRequest(BaseModel):
    total_usd: float = Field(..., gt=0)
    items: List[CryptoItem]

class CryptoInitTransaction(BaseModel):
    to: str
    amount: int  # nanoTONs
    payload: Optional[str] = None
    validUntil: int

class CryptoInitResponse(BaseModel):
    status: str
    reference: str
    txid: str
    transaction: CryptoInitTransaction

class CryptoVerifyRequest(BaseModel):
    total_usd: float = Field(..., gt=0)
    items: List[CryptoItem]
    address: Optional[str] = None  # payer wallet address
    boc: Optional[str] = None
    reference: Optional[str] = None
    valid_until: Optional[int] = None

class CryptoVerifyResponse(BaseModel):
    status: str
    message: str
    tx_hash: Optional[str] = None
    tx_lt: Optional[int] = None
    tx_utime: Optional[int] = None
    deposit_id: Optional[int] = None
    txid: Optional[str] = None
