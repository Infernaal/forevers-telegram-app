from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class RegistrationRequest(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    country: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=50)
    ref: Optional[int] = Field(None, description="Parent (referrer) user id")
    telegram_init_data: Optional[str] = Field(None, description="Raw Telegram WebApp initData for signature verification")


class RegistrationResponse(BaseModel):
    status: str
    message: str
    email_verification_required: bool = False
