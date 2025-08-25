from pydantic import BaseModel, Field
from typing import Literal, Optional, List, Dict, Any
from decimal import Decimal


class TONPaymentRequest(BaseModel):
    wallet_address: str = Field(..., description="TON wallet address of the user")
    purchase_details: Dict[str, Any] = Field(..., description="Purchase details from frontend")
    ton_price: Optional[Decimal] = Field(None, description="Current TON price in USD")


class TONPaymentResponse(BaseModel):
    status: Literal["success", "failed"]
    message: str
    payment_id: Optional[str] = None
    recipient_address: Optional[str] = None
    amount_ton: Optional[Decimal] = None
    amount_usd: Optional[Decimal] = None
    memo: Optional[str] = None
    expires_at: Optional[str] = None


class TONConfirmPaymentRequest(BaseModel):
    payment_id: str = Field(..., description="Payment ID from create payment request")
    transaction_hash: str = Field(..., description="TON transaction hash (BOC)")
    wallet_address: str = Field(..., description="Sender wallet address")


class TONConfirmPaymentResponse(BaseModel):
    status: Literal["success", "failed", "pending"]
    message: str
    txid: Optional[str] = None
    forevers_purchased: Optional[int] = None
    total_usd_spent: Optional[Decimal] = None
    data: Optional[Dict[str, Any]] = None


class TONTransactionStatus(BaseModel):
    transaction_hash: str
    status: Literal["pending", "confirmed", "failed"]
    confirmations: int
    block_height: Optional[int] = None
    timestamp: Optional[int] = None


class TONWalletInfo(BaseModel):
    address: str
    balance_ton: Decimal
    balance_usd: Optional[Decimal] = None
    is_active: bool


class TONPaymentData(BaseModel):
    payment_id: str
    user_id: int
    wallet_address: str
    recipient_address: str
    amount_ton: Decimal
    amount_usd: Decimal
    ton_price: Decimal
    purchase_details: Dict[str, Any]
    transaction_hash: Optional[str] = None
    status: Literal["created", "pending", "confirmed", "failed", "expired"]
    created_at: str
    expires_at: str
    confirmed_at: Optional[str] = None


class TONPurchaseResult(BaseModel):
    """Result of completed TON purchase with forevers details"""
    payment_id: str
    transaction_hash: str
    forevers_purchased: List[Dict[str, Any]]
    total_forevers: int
    total_usd_spent: Decimal
    total_ton_spent: Decimal
    exchange_rate: Decimal
    deposit_records: List[Dict[str, Any]]
    wallet_balances: Dict[str, Decimal]


class TONRateRequest(BaseModel):
    """Request for current TON exchange rate"""
    amount_usd: Optional[Decimal] = Field(None, description="USD amount to convert to TON")


class TONRateResponse(BaseModel):
    """Current TON exchange rate response"""
    ton_price_usd: Decimal = Field(..., description="Current TON price in USD")
    amount_ton: Optional[Decimal] = Field(None, description="TON amount for requested USD")
    last_updated: str = Field(..., description="Timestamp of last price update")
    source: str = Field(..., description="Price source (e.g., 'coingecko')")


class TONTransactionVerification(BaseModel):
    """TON transaction verification data"""
    transaction_hash: str
    from_address: str
    to_address: str
    amount_nanotons: str
    memo: Optional[str] = None
    block_height: int
    timestamp: int
    confirmations: int
    is_valid: bool
    verification_source: str
