from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import update
from db.database import get_db
from models.models import Users
from schemas.user_info import (
    UserInfoResponse,
    UserInfoResponseWrapper,
    AuthByEmailRequest,
    AuthByEmailResponse,
)
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


@router.get("/auth/by-telegram/{telegram_id}", response_model=UserInfoResponseWrapper, summary="Auth (existence) by Telegram ID")
async def get_user_by_telegram(telegram_id: int, db: AsyncSession = Depends(get_db)):
    """Lightweight existence check by Telegram ID.
    Returns only status=success if a user with given telegram id exists, otherwise status=failed.
    No user data is included to keep response minimal.
    """
    try:
        stmt = select(Users.id).where(Users.telegram_id == str(telegram_id)).limit(1)
        result = await db.execute(stmt)
        user_id = result.scalar_one_or_none()
        if user_id is None:
            return UserInfoResponseWrapper(status="failed")
        return UserInfoResponseWrapper(status="success")
    except Exception:
        return UserInfoResponseWrapper(status="failed")


@router.post("/auth/by-email", response_model=AuthByEmailResponse, summary="Auth by email + optional telegram binding")
async def auth_by_email(payload: AuthByEmailRequest, db: AsyncSession = Depends(get_db)):
    """Authenticate existence via email and optional Telegram binding logic.

    Rules:
    - If email not found -> target = /email-not-registered, status=failed.
    - If found and user.telegram_id is NULL -> set telegram_id (if provided) and target=/favorites.
    - If found and user.telegram_id equals provided -> target=/favorites.
    - If found and user.telegram_id not null and differs from provided -> target=/telegram-mismatch (new fallback view).
    If telegram_id is not provided we still only check email existence (success -> favorites else email-not-registered).
    """
    try:
        stmt = select(Users).where(Users.email == payload.email).limit(1)
        res = await db.execute(stmt)
        user: Users | None = res.scalar_one_or_none()
        if user is None:
            return AuthByEmailResponse(status="failed", target="/email-not-registered", message="Email not registered")

        # If no telegram id supplied treat as success (maybe later will ask) 
        if not payload.telegram_id:
            return AuthByEmailResponse(status="success", target="/favorites")

        provided_tg = str(payload.telegram_id)
        # No tg bound yet -> bind and success
        if not user.telegram_id:
            upd = (update(Users)
                   .where(Users.id == user.id)
                   .values(telegram_id=provided_tg))
            await db.execute(upd)
            await db.commit()
            return AuthByEmailResponse(status="success", target="/favorites")

        # Already bound matches
        if user.telegram_id == provided_tg:
            return AuthByEmailResponse(status="success", target="/favorites")

        # Bound but mismatch
        return AuthByEmailResponse(status="failed", target="/telegram-mismatch", message="Email already linked to another Telegram account")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal error")

