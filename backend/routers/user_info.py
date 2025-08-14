from fastapi import APIRouter, Depends, Request, Response, Header
import logging
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from db.database import get_db
from models.models import Users
from schemas.user_info import (
    UserInfoResponse,
    UserInfoResponseWrapper,
    AuthByEmailRequest,
    AuthByEmailResponse,
)
from services.get_rank_service import get_user_rank
from dependencies.current_user import get_current_user_id
from sessions.redis_session import create_session, delete_session, init_redis, get_user_id_by_session

router = APIRouter(prefix="/user", tags=["User Info"])
logger = logging.getLogger("dbdc.user")


@router.get("/me", response_model=UserInfoResponseWrapper, summary="Current authorized user info")
async def get_my_user_info(current_user_id: int = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    try:
        stmt = select(Users).where(Users.id == current_user_id)
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()

        if user is None:
            return UserInfoResponseWrapper(
                status="failed",
                message="User not found"
            )

        rank = await get_user_rank(current_user_id, db)

        return UserInfoResponseWrapper(
            status="success",
            data=UserInfoResponse(
                full_name=f"{user.first_name or ''} {user.last_name or ''}".strip(),
                first_name=user.first_name or "",
                rank=rank or "None",
                avatar=f"https://dbdcusa.com/uploads/avatars/{user.avatar}" if user.avatar else ""
            )
        )
    except Exception as e:
        logger.exception("Failed to get current user info")
        return UserInfoResponseWrapper(
            status="failed",
            message="A server error occurred while retrieving user info."
        )


@router.get("/auth/by-telegram/{telegram_id}", response_model=UserInfoResponseWrapper, summary="Auth (existence) by Telegram ID (Telegram WebApp init data verified)")
async def get_user_by_telegram(
    telegram_id: int,
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db),
    x_telegram_init_data: str | None = Header(default=None, alias="X-Telegram-Init-Data"),
):
    from utils.telegram_auth import verify_init_data, TelegramAuthError

    # Early exit: already have a valid session cookie
    existing_session_id = request.cookies.get("session_id")
    if existing_session_id:
        try:
            await init_redis()
            existing_user_id = await get_user_id_by_session(existing_session_id)
            if existing_user_id:
                return UserInfoResponseWrapper(status="success")
        except Exception:
            pass  # fall back to normal flow if redis check fails

    raw_init_data = x_telegram_init_data or request.query_params.get("init_data")
    if not raw_init_data:
        logger.warning("Auth by telegram: init data missing")
        return UserInfoResponseWrapper(status="failed", message="init data missing")
    try:
        parsed = verify_init_data(raw_init_data)
        user_obj = parsed.get("user") or {}
        real_tg_id = user_obj.get("id")
        if not real_tg_id:
            logger.warning("Auth by telegram: user id missing in init data")
            return UserInfoResponseWrapper(status="failed", message="user id missing")
        stmt = select(Users.id).where(Users.telegram_id == str(real_tg_id)).limit(1)
        result = await db.execute(stmt)
        user_id = result.scalar_one_or_none()
        if user_id is None:
            logger.info(f"Auth by telegram: telegram_id={real_tg_id} not found")
            return UserInfoResponseWrapper(status="failed")
        await init_redis()
        session_id = await create_session(int(user_id))
        response.set_cookie(key="session_id", value=session_id, httponly=True, secure=True, samesite="None", max_age=10800)
        return UserInfoResponseWrapper(status="success")
    except TelegramAuthError:
        logger.warning("Auth by telegram: init data verification failed")
        return UserInfoResponseWrapper(status="failed")
    except Exception as e:
        logger.exception("Auth by telegram: unexpected error")
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

        if not payload.telegram_id:
            return AuthByEmailResponse(status="success", target="/favorites")

        provided_tg = str(payload.telegram_id)
        if not user.telegram_id:
            upd = (update(Users)
                   .where(Users.id == user.id)
                   .values(telegram_id=provided_tg))
            await db.execute(upd)
            await db.commit()
            return AuthByEmailResponse(status="success", target="/favorites")

        if user.telegram_id == provided_tg:
            return AuthByEmailResponse(status="success", target="/favorites")

        return AuthByEmailResponse(status="failed", target="/telegram-mismatch", message="Email already linked to another Telegram account")
    except Exception as e:
        logger.exception("Auth by email failed")
        raise HTTPException(status_code=500, detail="Internal error")


@router.post("/logout")
async def logout(request: Request, response: Response):
    try:
        session_id = request.cookies.get("session_id")
        if session_id:
            await init_redis()
            await delete_session(session_id)
        # Overwrite cookie to remove
        response.set_cookie(
            key="session_id",
            value="",
            httponly=True,
            secure=True,
            samesite="None",
            max_age=0,
        )
        return {"status": "success"}
    except Exception as e:
        logger.exception("Logout error (ignored)")
        return {"status": "success"}  # even on error do not block client

