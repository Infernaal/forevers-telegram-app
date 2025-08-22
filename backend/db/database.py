import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.exc import OperationalError, DisconnectionError
from typing import AsyncGenerator
import asyncio
import logging
from functools import wraps

logger = logging.getLogger(__name__)

# 🔐 Загрузка переменных окружения
load_dotenv()

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST", "localhost")
DB_PORT = os.getenv("MYSQL_PORT", "3306")
DB_NAME = os.getenv("MYSQL_DATABASE")

DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ⚙️ Создание async-движка с настройками переподключения
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=20,
    max_overflow=30,
    pool_timeout=30,
    pool_recycle=3600,  # Переподключаться каждый час
    pool_pre_ping=True,  # Проверять соединение перед использованием
    connect_args={
        "connect_timeout": 60,
    }
)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

# 📦 Базовый класс для моделей
class Base(AsyncAttrs, DeclarativeBase):
    pass

# 🔁 И��ициализация базы данных
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# 🔄 Декоратор для повторных попыток при сбоях соединения с БД
def db_retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except (OperationalError, DisconnectionError) as e:
                    last_exception = e
                    error_msg = str(e).lower()

                    # Проверяем, что это именно ошибка соединения
                    connection_errors = [
                        'lost connection',
                        'server has gone away',
                        'connection was killed',
                        'broken pipe',
                        'timeout',
                        'can\'t connect',
                        'connection refused'
                    ]

                    is_connection_error = any(err in error_msg for err in connection_errors)

                    if is_connection_error and attempt < max_attempts - 1:
                        logger.warning(f"Database connection error on attempt {attempt + 1}: {e}")
                        await asyncio.sleep(delay * (2 ** attempt))  # Экспоненциальная задержка
                        continue
                    else:
                        raise
                except Exception as e:
                    # Для других ошибок не повторяем
                    raise

            # Если все попытки исчерпаны
            raise last_exception
        return wrapper
    return decorator

# 🧪 Асинхронный генератор сессии для Depends с retry
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            async with async_session() as session:
                yield session
                break
        except (OperationalError, DisconnectionError) as e:
            if attempt < max_attempts - 1:
                logger.warning(f"Database session creation failed on attempt {attempt + 1}: {e}")
                await asyncio.sleep(1.0 * (2 ** attempt))
                continue
            else:
                raise

# 🔧 Ф��нкция для выполнения запросов с retry
async def execute_with_retry(session: AsyncSession, stmt, max_attempts: int = 3):
    """Выполняет SQL запрос с повторными попытками при сбоях соединения"""
    last_exception = None
    for attempt in range(max_attempts):
        try:
            return await session.execute(stmt)
        except (OperationalError, DisconnectionError) as e:
            last_exception = e
            error_msg = str(e).lower()

            connection_errors = [
                'lost connection',
                'server has gone away',
                'connection was killed',
                'broken pipe',
                'timeout',
                'can\'t connect',
                'connection refused'
            ]

            is_connection_error = any(err in error_msg for err in connection_errors)

            if is_connection_error and attempt < max_attempts - 1:
                logger.warning(f"Database execute error on attempt {attempt + 1}: {e}")
                await asyncio.sleep(1.0 * (2 ** attempt))
                # Создаем новую сессию для следующей попытки
                await session.rollback()
                continue
            else:
                raise

    raise last_exception
