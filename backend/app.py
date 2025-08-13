from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from db.database import init_db
import uvicorn
from routers.forevers_user_balance import router as forevers_user_balance_router
from routers.forevers_prices import router as forevers_price_router
from routers.user_info import router as user_info_router
from routers.email_verification import router as email_verification_router
from fastapi.openapi.utils import get_openapi

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Bot is ready")
    yield

# 👇 FastAPI с lifespan
app = FastAPI(
    title="DBDC Telegram Bot Backend",
    description="Backend для Telegram WebApp, который обрабатывает финансовые данные пользователей, включая баланс forevers.",
    version="1.0.0",
    contact={
        "name": "Dubadu Developers",
        "url": "https://dubadu.com",
        "email": "support@dubadu.com",
    },
    # Переносим пути документации под основной API префикс
    docs_url="/api/v1/dbdc/docs",
    redoc_url="/api/v1/dbdc/redoc",
    openapi_url="/api/v1/dbdc/openapi.json",
    lifespan=lifespan
)

# 👇 CORS-настройки
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

app.include_router(forevers_user_balance_router, prefix="/api/v1/dbdc")
app.include_router(forevers_price_router, prefix="/api/v1/dbdc")
app.include_router(user_info_router, prefix="/api/v1/dbdc")
app.include_router(email_verification_router, prefix="/api/v1/dbdc")
