from fastapi import FastAPI, Request
import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from contextlib import asynccontextmanager
from db.database import init_db
import uvicorn
from routers.forevers_user_balance import router as forevers_user_balance_router
from routers.forevers_prices import router as forevers_price_router
from routers.forevers_purchase import router as forevers_purchase_router
from routers.forevers_crypto import router as forevers_crypto_router
from routers.user_info import router as user_info_router
from routers.email_verification import router as email_verification_router
from routers.referral import router as referral_router
from fastapi.openapi.utils import get_openapi

from sessions.redis_session import init_redis, close_redis, refresh_session, get_user_id_by_session

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger("dbdc.app")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    await init_redis()
    logger.info("Application started and Redis initialized")
    yield
    await close_redis()
    logger.info("Application shutdown complete")

app = FastAPI(
    title="DBDC Telegram Bot Backend",
    description="Backend для Telegram WebApp, который обрабатывает финансовые данные пользователей, включая баланс forevers.",
    version="1.0.0",
    contact={
        "name": "Dubadu Developers",
        "url": "https://dubadu.com",
        "email": "support@dubadu.com",
    },
    docs_url="/api/v1/dbdc/docs",
    redoc_url="/api/v1/dbdc/redoc",
    openapi_url="/api/v1/dbdc/openapi.json",
    lifespan=lifespan
)

origins = [
    "https://web.telegram.org",
    "http://localhost:3000",
    "https://dbdc-mini.dubadu.com",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https:\/\/.*\.fly\.dev",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SessionRefreshMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        session_id = request.cookies.get("session_id")
        if session_id:
            try:
                await refresh_session(session_id)
                user_id = await get_user_id_by_session(session_id)
                if user_id:
                    request.state.user_id = user_id
            except Exception as e:
                logger.warning(f"Session refresh failed: {e}")
        response = await call_next(request)
        return response

app.add_middleware(SessionRefreshMiddleware)

app.include_router(forevers_user_balance_router, prefix="/api/v1/dbdc")
app.include_router(forevers_price_router, prefix="/api/v1/dbdc")
app.include_router(forevers_purchase_router, prefix="/api/v1/dbdc")
app.include_router(user_info_router, prefix="/api/v1/dbdc")
app.include_router(email_verification_router, prefix="/api/v1/dbdc")
app.include_router(referral_router, prefix="/api/v1/dbdc")
app.include_router(forevers_crypto_router, prefix="/api/v1/dbdc")
