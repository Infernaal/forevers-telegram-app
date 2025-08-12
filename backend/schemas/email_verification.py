from pydantic import BaseModel, EmailStr
from typing import Optional

class SendVerificationCodeRequest(BaseModel):
    email: EmailStr

class VerifyCodeRequest(BaseModel):
    email: EmailStr
    code: str

class EmailVerificationResponse(BaseModel):
    status: str
    message: str
    data: Optional[dict] = None

class SendCodeResponseWrapper(BaseModel):
    status: str
    message: str
    expires_in_minutes: Optional[int] = None

class VerifyCodeResponseWrapper(BaseModel):
    status: str
    message: str
    valid: Optional[bool] = None
