from pydantic import BaseModel
from decimal import Decimal
from typing import Optional, List

class DepositItem(BaseModel):
    txid: Optional[str]  # contract id
    processed_on: Optional[int]  # date
    forevers: Decimal  # amount / rate_at_deposit
    price: Decimal  # rate_at_deposit
    type: str  # UAE, KZ, DE, PL, UA
    paid: Decimal  # amount
    access: Decimal  # activated_forevers (need clarification)
    participation: Decimal  # activated_loyalty (need clarification)

class UserDepositsData(BaseModel):
    user_id: int
    deposits: List[DepositItem]
    total_count: int

class UserDepositsResponse(BaseModel):
    status: str
    data: Optional[UserDepositsData] = None
    message: Optional[str] = None

# Legacy compatibility schema
class DepositByType(BaseModel):
    type: str  # UAE, KZ, DE, PL, UA
    total_amount: Decimal
    total_usd_value: Decimal  # rate_at_deposit * amount

class UserDepositsSummaryData(BaseModel):
    user_id: int
    deposits_by_type: List[DepositByType]
    total_usd_value: Decimal

class UserDepositsSummaryResponse(BaseModel):
    status: str
    data: Optional[UserDepositsSummaryData] = None
    message: Optional[str] = None
