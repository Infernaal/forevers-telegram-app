from pydantic import BaseModel
from typing import Optional

class ActivateLoyaltyRequest(BaseModel):
    deposit_id: int
    txid: str

class ActivateLoyaltyResponse(BaseModel):
    status: str
    message: Optional[str] = None
