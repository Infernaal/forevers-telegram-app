from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.database import get_db
from models.models import Users
from schemas.user_info import UserInfoResponse, UserInfoResponseWrapper
from services.get_rank_service import get_user_rank

router = APIRouter(prefix="/user", tags=["User Info"])

@router.get("/info/{user_id}", response_model=UserInfoResponseWrapper, summary="Information about user")
async def get_user_info(user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        stmt = select(Users).where(Users.id == user_id)
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()

        if user is None:
            return UserInfoResponseWrapper(
                status="failed",
                message="User not found"
            )

        rank = await get_user_rank(user_id, db)

        return UserInfoResponseWrapper(
            status="success",
            data=UserInfoResponse(
                full_name=f"{user.first_name or ''} {user.last_name or ''}".strip(),
                first_name=user.first_name or "",
                rank=rank or "None",
                avatar=f"https://dbdcusa.com/uploads/avatars/{user.avatar}" if user.avatar else ""
            )
        )
    except Exception:
        return UserInfoResponseWrapper(
            status="failed",
            message="A server error occurred while retrieving user info."
        )