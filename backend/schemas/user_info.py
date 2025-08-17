from pydantic import BaseModel, EmailStr
from typing import Optional, Union

class UserInfoResponse(BaseModel):
    id: int
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
    # Raw Telegram WebApp init data string (signed). If provided it will be verified
    # and the embedded user.id will override telegram_id for binding logic.
    telegram_init_data: Optional[str] = None


class AuthByEmailResponse(BaseModel):
    status: str  # success | failed
    target: str  # frontend route to redirect
    message: Optional[str] = None