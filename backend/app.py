from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from db.database import init_db
import uvicorn
import re
from routers.forevers_user_balance import router as forevers_user_balance_router
from routers.forevers_prices import router as forevers_price_router
from routers.user_info import router as user_info_router
from routers.ton_payment import router as ton_payment_router
from fastapi.openapi.utils import get_openapi
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Bot is ready")
    yield

API_PREFIX = "/api/v1/dbdc"
DOCS_UNDER_PREFIX = os.getenv("DOCS_UNDER_PREFIX", "true").lower() == "true"

docs_url = f"{API_PREFIX}/docs" if DOCS_UNDER_PREFIX else "/docs"
redoc_url = f"{API_PREFIX}/redoc" if DOCS_UNDER_PREFIX else "/redoc"
openapi_url = f"{API_PREFIX}/openapi.json" if DOCS_UNDER_PREFIX else "/openapi.json"

app = FastAPI(
    title="DBDC Telegram Bot Backend",
    description="Backend для Telegram WebApp, который обрабатывает финансовые данные пользователей, включая баланс forevers.",
    version="1.0.0",
    contact={
        "name": "Dubadu Developers",
        "url": "https://dubadu.com",
        "email": "support@dubadu.com",
    },
    docs_url=docs_url,
    redoc_url=redoc_url,
    openapi_url=openapi_url,
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
    allow_origin_regex=r"^https://([a-z0-9-]+\.)*(builder\.io|builder\.codes|fly\.dev)$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(forevers_user_balance_router, prefix=API_PREFIX)
app.include_router(forevers_price_router, prefix=API_PREFIX)
app.include_router(user_info_router, prefix=API_PREFIX)
app.include_router(ton_payment_router, prefix=API_PREFIX)

# Normalize duplicate slashes to avoid //api issues
@app.middleware("http")
async def normalize_slashes(request, call_next):
    original_path = request.scope.get('path', '')
    normalized = re.sub(r'//+', '/', original_path)
    if normalized != original_path:
        request.scope['path'] = normalized
    response = await call_next(request)
    return response
