from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from models import init_db  # Убедись, что функция доступна

# 👇 Lifespan запускается при старте приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Bot is ready")
    yield

# 👇 FastAPI с lifespan
app = FastAPI(
    title="DBDC Telegram Bot Backend",
    lifespan=lifespan
)

# 👇 CORS-настройки
origins = [
    "https://web.telegram.org",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
