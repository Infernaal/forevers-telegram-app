from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class UAEDepositsData(BaseModel):
    user_id: int
    total_uae_deposits: Decimal
    
class UAEDepositsResponse(BaseModel):
    status: str
    data: Optional[UAEDepositsData] = None
    message: Optional[str] = None
