from pydantic import BaseModel
from decimal import Decimal
from datetime import date
from typing import List, Optional

class PriceItem(BaseModel):
    type: str
    value: Decimal

class DiscountItem(BaseModel):
    type: str
    start_date: date
    end_date: date
    discount: Decimal

class ForeversPricesData(BaseModel):
    prices: List[PriceItem]
    discounts: List[DiscountItem]
    discounted_prices: Optional[List[PriceItem]] = None

class ForeversPricesResponse(BaseModel):
    status: str
    data: Optional[ForeversPricesData] = None
    message: Optional[str] = None