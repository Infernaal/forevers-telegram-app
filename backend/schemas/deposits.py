from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class DepositItem(BaseModel):
    txid: str  # contract id
    processed_on: Optional[datetime]  # date
    forevers: Decimal  # amount / rate_as_deposit
    price: Decimal  # rate_as_deposit
    type: str  # deposit type (UAE, KZ, etc.)
    paid: Decimal  # amount
    access: bool  # activated_forevers
    participation: bool  # activated_loyalty

    class Config:
        from_attributes = True

class DepositsData(BaseModel):
    user_id: int
    deposits: List[DepositItem]
    total_count: int

class DepositsResponse(BaseModel):
    status: str
    data: Optional[DepositsData] = None
    message: Optional[str] = None
