from pydantic import BaseModel
from typing import Optional

class UserInfoResponse(BaseModel):
    full_name: str
    rank: str
    avatar: str

class UserInfoResponseWrapper(BaseModel):
    status: str
    data: Optional[UserInfoResponse] = None
    message: Optional[str] = None