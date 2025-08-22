from pydantic import BaseModel
from decimal import Decimal
from typing import Optional, List

class DepositByType(BaseModel):
    type: str  # UAE, KZ, DE, PL, UA
    total_amount: Decimal
    total_usd_value: Decimal  # rate_at_deposit * amount

class UserDepositsData(BaseModel):
    user_id: int
    deposits_by_type: List[DepositByType]
    total_usd_value: Decimal

class UserDepositsResponse(BaseModel):
    status: str
    data: Optional[UserDepositsData] = None
    message: Optional[str] = None
