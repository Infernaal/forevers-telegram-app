from typing import Optional, List
from pydantic import BaseModel
from decimal import Decimal

class DepositsHistoryItem(BaseModel):
    id: int
    txid: Optional[str]
    amount: Optional[str]
    rate_at_deposit: Optional[Decimal]
    requested_on: Optional[int]
    deal_status: Optional[int]
    status: Optional[int]
    activated_forevers: Optional[int]
    activated_loyalty: Optional[int]
    type: Optional[str]
    forevers_activation_date: Optional[int]
    forevers_reactivate_date: Optional[int]
    loyalty_activation_date: Optional[int]
    is_expired: int
    is_not_fully_activated: int

    class Config:
        from_attributes = True

class DepositsHistoryData(BaseModel):
    user_id: int
    deposits: List[DepositsHistoryItem]
    total_count: int

class DepositsHistoryResponse(BaseModel):
    status: str
    data: Optional[DepositsHistoryData] = None
    message: Optional[str] = None
