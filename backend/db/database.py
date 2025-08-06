import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator

# 🔐 Загрузка переменных окружения
load_dotenv()

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST", "localhost")
DB_PORT = os.getenv("MYSQL_PORT", "3306")
DB_NAME = os.getenv("MYSQL_DATABASE")

DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ⚙️ Создание async-движка и async-сессии
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

# 📦 Базовый класс для моделей
class Base(AsyncAttrs, DeclarativeBase):
    pass

# 🔁 Инициализация базы данных
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# 🧪 Асинхронный генератор сессии для Depends
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session