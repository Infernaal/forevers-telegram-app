from pydantic import BaseModel, EmailStr
from typing import Optional, Union

class UserInfoResponse(BaseModel):
    full_name: str
    rank: str
    avatar: str

class UserInfoResponseWrapper(BaseModel):
    status: str
    data: Optional[UserInfoResponse] = None
    message: Optional[str] = None


class AuthByEmailRequest(BaseModel):
    email: EmailStr
    telegram_id: Optional[Union[int, str]] = None


class AuthByEmailResponse(BaseModel):
    status: str  # success | failed
    target: str  # frontend route to redirect
    message: Optional[str] = None