from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from typing import Optional, List, Literal, Dict

class WalletItem(BaseModel):
    type: Literal["bonus", "loyalty_program"]
    currency: str
    amount: Decimal

class ForeversBalanceData(BaseModel):
    user_id: int
    balance_uae: Decimal
    balance_kz: Decimal
    balance_de: Decimal
    balance_pl: Decimal
    balance_ua: Decimal
    balance: Decimal

class ForeversBalance(BaseModel):
    status: str
    forevers_balance: Optional[ForeversBalanceData] = None
    wallets: List[WalletItem] = []
    available_forevers: Optional[Dict[str, Optional[int]]] = None
    message: Optional[str] = None
