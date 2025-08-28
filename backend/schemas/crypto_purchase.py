from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional
from enum import Enum


class CryptoInitRequest(BaseModel):
    """Request model for initializing crypto purchase"""
    amount_usd: Decimal = Field(..., gt=0, description="Amount in USD to purchase")
    user_wallet: str = Field(..., min_length=1, description="User's wallet address (sender)")
    receiver_wallet: str = Field(..., min_length=1, description="Receiver wallet address")
    rate_as_deposit: Optional[Decimal] = Field(None, gt=0, description="Rate per Forever if provided, otherwise from settings")


class CryptoInitResponse(BaseModel):
    """Response model for crypto purchase initialization"""
    status: str = Field(..., description="Success or failed")
    message: str = Field(..., description="Response message")
    data: Optional[dict] = Field(None, description="Transaction data if successful")


class CryptoVerifyRequest(BaseModel):
    """Request model for verifying crypto transaction"""
    request_id: str = Field(..., description="Request ID from init response")


class CryptoVerifyResponse(BaseModel):
    """Response model for crypto transaction verification"""
    status: str = Field(..., description="Success, failed, pending, or invalid")
    message: str = Field(..., description="Response message")
    transaction_status: Optional[str] = Field(None, description="Transaction status from blockchain")
    data: Optional[dict] = Field(None, description="Transaction verification data")


class TransactionStatus(str, Enum):
    """Enum for transaction statuses"""
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    INVALID = "invalid"
    TIMEOUT = "timeout"
