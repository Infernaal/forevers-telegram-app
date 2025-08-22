from pydantic import BaseModel, Field
from typing import Literal, Optional
from decimal import Decimal


class ForeversPurchaseRequest(BaseModel):
    wallet_type: Literal["bonus", "rent"] = Field(..., description="Type of wallet to use for purchase")
    forever_type: Literal["UAE", "KZ", "DE", "PL", "UA"] = Field(..., description="Type of forevers to purchase")
    forevers_amount: int = Field(..., gt=0, description="Amount of forevers to purchase")
    final_rate: Decimal = Field(..., gt=0, description="Exchange rate for forevers")
    usd_amount: Decimal = Field(..., gt=0, description="USD amount for purchase")


class ForeversPurchaseResponse(BaseModel):
    status: Literal["success", "failed"]
    message: str
    txid: Optional[str] = None
    data: Optional[dict] = None


class ForeversPurchaseData(BaseModel):
    txid: str
    wallet_type: str
    forever_type: str
    forevers_amount: int
    usd_amount: Decimal
    final_rate: Decimal
    new_wallet_balance: Decimal
    exchange_stats_id: int
