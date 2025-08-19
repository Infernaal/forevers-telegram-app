from fastapi import APIRouter, Depends, Request, Response, Header
import logging
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from db.database import get_db
from models.models import Users, UsersWallets, Settings, Forevers
from utils.generate_password import generate_strong_password
from schemas.user_info import (
    UserInfoResponse,
    UserInfoResponseWrapper,
    AuthByEmailRequest,
    AuthByEmailResponse,
)
from schemas.registration import RegistrationRequest, RegistrationResponse
from services.get_rank_service import get_user_rank
from dependencies.current_user import get_current_user_id
from sessions.redis_session import create_session, delete_session, init_redis, get_user_id_by_session
import bcrypt
import time
import uuid
from datetime import datetime
import json
import decimal

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
                id=user.id,
                full_name=f"{user.first_name or ''} {user.last_name or ''}".strip(),
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
        # Optional: ensure path telegram_id matches provided user id (defense-in-depth)
        if real_tg_id != telegram_id:
            logger.warning("Auth by telegram: path telegram_id mismatch")
            return UserInfoResponseWrapper(status="failed")
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
    except TelegramAuthError as e:
        logger.warning(f"Auth by telegram: init data verification failed: {e}")
        return UserInfoResponseWrapper(status="failed")


@router.post("/auth/by-email", response_model=AuthByEmailResponse, summary="Auth by email + optional telegram binding (with Telegram signature verification)")
async def auth_by_email(payload: AuthByEmailRequest, response: Response, db: AsyncSession = Depends(get_db)):
    """Authenticate existence via email and optional Telegram binding logic.

    Rules:
    - If email not found -> target = /email-not-registered, status=failed.
    - If found and user.telegram_id is NULL -> set telegram_id (if provided) and target=/favorites.
    - If found and user.telegram_id equals provided -> target=/favorites.
    - If found and user.telegram_id not null and differs from provided -> target=/email-linked-other-account (fallback view).
    If telegram_id is not provided we still only check email existence (success -> favorites else email-not-registered).
    """
    try:
        # 1. Load user by email
        stmt = select(Users).where(Users.email == payload.email).limit(1)
        res = await db.execute(stmt)
        user: Users | None = res.scalar_one_or_none()
        if user is None:
            return AuthByEmailResponse(status="failed", target="/email-not-registered", message="Email not registered")

        # 2. Determine telegram id via verified init data if provided
        verified_telegram_id: str | None = None
        if payload.telegram_init_data:
            try:
                from utils.telegram_auth import verify_init_data, TelegramAuthError
                parsed = verify_init_data(payload.telegram_init_data)
                verified_telegram_id = str(parsed.get("user", {}).get("id")) if parsed.get("user", {}).get("id") else None
            except Exception as verr:  # broad: treat any verify error as no telegram binding allowed
                logger.warning(f"Auth by email: telegram init data verify failed: {verr}")
                # If init data provided but invalid -> force mismatch style failure to prevent silent spoof
                return AuthByEmailResponse(status="failed", target="/telegram-signature-invalid", message="Invalid Telegram signature")

        # 3. Fallback to plain telegram_id (legacy) only if no signed data provided
        if not verified_telegram_id and payload.telegram_id:
            # Accept raw provided id (not verified) for backward compatibility; could tighten later
            try:
                verified_telegram_id = str(payload.telegram_id)
            except Exception:
                verified_telegram_id = None

        # 4. If no telegram id at all -> just success (email exists)
        if not verified_telegram_id:
            # Success WITHOUT telegram id is not allowed per updated rule
            return AuthByEmailResponse(status="failed", target="/account-check", message="Telegram authorization required")

        # 5. Binding / comparison logic
        provided_tg = verified_telegram_id
        if not user.telegram_id:
            # Bind new telegram id
            upd = (update(Users)
                   .where(Users.id == user.id)
                   .values(telegram_id=provided_tg))
            await db.execute(upd)
            await db.commit()
            try:
                await init_redis()
                session_id = await create_session(int(user.id))
                response.set_cookie(
                    key="session_id",
                    value=session_id,
                    httponly=True,
                    secure=True,
                    samesite="None",
                    max_age=10800,
                )
            except Exception as se:
                logger.warning(f"Auth by email: session create (bind tg) failed: {se}")
            return AuthByEmailResponse(status="success", target="/favorites")

        if user.telegram_id == provided_tg:
            # Already bound, create session
            try:
                await init_redis()
                session_id = await create_session(int(user.id))
                response.set_cookie(
                    key="session_id",
                    value=session_id,
                    httponly=True,
                    secure=True,
                    samesite="None",
                    max_age=10800,
                )
            except Exception as se:
                logger.warning(f"Auth by email: session create (matched tg) failed: {se}")
            return AuthByEmailResponse(status="success", target="/favorites")

        return AuthByEmailResponse(status="failed", target="/email-linked-other-account", message="Email already linked to another Telegram account")
    except Exception:
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


@router.post("/register", response_model=RegistrationResponse, summary="Register a new user")
async def register_user(payload: RegistrationRequest, request: Request, response: Response, db: AsyncSession = Depends(get_db)):
    """Register a new user replicating legacy PHP logic (simplified).

    Steps:
    - Ensure email & phone unique.
    - Hash password (bcrypt like PHP password_hash default).
    - Prepare qualification_data & structural_data JSON blobs.
    - Insert user row.
    - Create default bonus wallet (amount 0, default currency from settings).
    - If settings.require_email_verify == 1 -> mark status=2 (pending), email_verified=0, generate email_hash.
    Returns status + flags.
    """
    try:
        logger.info(f"/register attempt email={payload.email} ip={request.client.host if request.client else '?'}")

        # Uniqueness checks
        res = await db.execute(select(Users.id).where(Users.email == payload.email).limit(1))
        if res.scalar_one_or_none():
            logger.info(f"/register email exists: {payload.email}")
            return RegistrationResponse(status="failed", message="Email already registered", target="/email-already-registered")
        if payload.phone:
            pres = await db.execute(select(Users.id).where(Users.phone_number == payload.phone).limit(1))
            if pres.scalar_one_or_none():
                logger.info(f"/register phone exists: {payload.phone}")
                return RegistrationResponse(status="failed", message="Phone already registered", target="/phone-already-registered")

        # Settings & constants
        settings = (await db.execute(select(Settings).limit(1))).scalar_one_or_none()
        default_currency = settings.default_currency if settings and settings.default_currency else "USD"

        # Генерация надёжного пароля
        generated_password = generate_strong_password(14)
        hashed = bcrypt.hashpw(generated_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        ip_addr = request.client.host if request.client else ""
        signup_time = int(time.time())
        user_token_id = str(uuid.uuid4())

        # Telegram verification (optional)
        telegram_id_verified: str | None = None
        if payload.telegram_init_data:
            try:
                from utils.telegram_auth import verify_init_data
                parsed = verify_init_data(payload.telegram_init_data)
                tg_user = parsed.get("user") or {}
                if tg_user.get("id"):
                    telegram_id_verified = str(tg_user["id"])
                    logger.info(f"/register telegram verified id={telegram_id_verified} email={payload.email}")
            except Exception as e:
                logger.warning(f"Registration: telegram init data verification failed: {e}")

        # Qualification & structural JSON templates
        qualification_data = {
            "current_rank": "None",
            "possible_rank": "BRONZE",
            "current_pct": 0,
            "pct": 0,
            "real_nct": 0,
            "capped_nct": 0,
            "prev_nct": 0,
            "prevMonthStart": "",
            "prevMonthEnd": "",
            "bonus": 0,
            "ranks": {
                "BRONZE": {"PCT": 500, "NCT": 10000, "structure": [], "bonus": 0},
                "SILVER": {"PCT": 1000, "NCT": 25000, "structure": [], "bonus": 500},
                "GOLD": {"PCT": 2000, "NCT": 50000, "structure": ["BRONZE"], "bonus": 1000},
                "DIAMOND": {"PCT": 3000, "NCT": 100000, "structure": ["BRONZE", "SILVER"], "bonus": 2000},
                "DOUBLE DIAMOND": {"PCT": 5000, "NCT": 500000, "structure": ["SILVER", "GOLD"], "bonus": 5000},
                "AMBASSADOR": {"PCT": 10000, "NCT": 2000000, "structure": ["BRONZE", "SILVER", "GOLD"], "bonus": 20000},
                "ROYAL AMBASSADOR": {"PCT": 15000, "NCT": 5000000, "structure": ["DIAMOND", "GOLD", "GOLD"], "bonus": 50000},
            },
            "pct_progress_percentage": 0,
            "nct_progress_percentage": 0,
            "remaining_pct": 500,
            "remaining_nct": 10000,
            "structure_details": [],
            "referral_structure": [],
            "current_rank_image": "/assets/images/norank.svg",
            "next_rank": "",
            "next_rank_image": "/assets/images/award_bronze.svg"
        }
        structural_data = {
            "current_rank": "None",
            "bonus_percentage": 0,
            "total_bonus": 0,
            "current_month_bonus": 0,
            "branches": []
        }

        # Email verification disabled entirely
        email_verified = 1
        status_code = 1
        email_hash = None

        # Create user
        user = Users(
            password=hashed,
            email=payload.email,
            phone_number=payload.phone,
            email_verified=email_verified,
            status=status_code,
            account_type=0,
            ip=ip_addr,
            signup_time=signup_time,
            first_name=payload.first_name,
            last_name=payload.last_name,
            country=payload.country,
            parent_id=payload.ref,
            qualification_data=json.dumps(qualification_data, separators=(",", ":")),
            qualification_data_updated=datetime.utcnow(),
            structural_data=json.dumps(structural_data, separators=(",", ":")),
            structural_data_updated=datetime.utcnow(),
            user_token_id=user_token_id,
            email_hash=email_hash,
            telegram_id=telegram_id_verified,
        )
        db.add(user)
        await db.flush()
        logger.info(f"/register created user id={user.id} email={payload.email}")

        db.add(Forevers(
            user_id=user.id,
            exchange_rate=settings.forevers_value,
            updated_at=datetime.utcnow(),
            balance_uae=decimal.Decimal("0.00000000"),
            balance_kz=decimal.Decimal("0.00000000"),
            balance_de=decimal.Decimal("0.00000000"),
            balance_pl=decimal.Decimal("0.00000000"),
            balance_ua=decimal.Decimal("0.00000000")
        ))
        await db.flush()
        
        # Wallet
        db.add(UsersWallets(
            uid=user.id,
            amount=0,
            currency=default_currency,
            wallet_type='bonus',
            updated=int(time.time())
        ))
        await db.commit()
        logger.info(f"/register committed user id={user.id} email={payload.email}")

        # Session cookie
        try:
            await init_redis()
            session_id = await create_session(int(user.id))
            response.set_cookie(
                key="session_id",
                value=session_id,
                httponly=True,
                secure=True,
                samesite="None",
                max_age=10800,
            )
        except Exception as se:
            logger.warning(f"Registration: session creation failed: {se}")

        return RegistrationResponse(
            status="success",
            message="Registered successfully",
            email_verification_required=False,
            generated_password=generated_password
        )
    except Exception:
        await db.rollback()
        logger.exception("Registration failed")
        return RegistrationResponse(status="failed", message="Registration failed due to server error", target="/registration-error")

