from pydantic import BaseModel
from typing import Optional

class ActivateForeversRequest(BaseModel):
    deposit_id: int
    txid: str

class ActivateForeversResponse(BaseModel):
    status: str
    message: Optional[str] = None
