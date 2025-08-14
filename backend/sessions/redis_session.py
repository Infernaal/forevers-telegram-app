import os
import uuid
from typing import Optional
from datetime import datetime

from redis.asyncio import Redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
SESSION_TTL_SECONDS = int(os.getenv("SESSION_TTL", "10800"))  # 3 hours default

redis_client: Optional[Redis] = None


async def init_redis():
    global redis_client
    if redis_client is None:
        redis_client = Redis.from_url(REDIS_URL, decode_responses=True)
    return redis_client


async def close_redis():
    global redis_client
    if redis_client is not None:
        await redis_client.close()
        redis_client = None


async def create_session(user_id: int) -> str:
    """Create new session and return session id."""
    if redis_client is None:
        raise RuntimeError("Redis not initialized")
    session_id = uuid.uuid4().hex
    key = f"sess:{session_id}"
    # Store as simple hash
    now_ts = str(int(datetime.utcnow().timestamp()))
    await redis_client.hset(key, mapping={
        "user_id": str(user_id),
        "created_at": now_ts,
        "last_activity": now_ts,
    })
    await redis_client.expire(key, SESSION_TTL_SECONDS)
    return session_id


async def get_user_id_by_session(session_id: str) -> Optional[int]:
    if not session_id or redis_client is None:
        return None
    key = f"sess:{session_id}"
    if not await redis_client.exists(key):
        return None
    data = await redis_client.hgetall(key)
    user_id = data.get("user_id")
    return int(user_id) if user_id else None


async def refresh_session(session_id: str):
    if not session_id or redis_client is None:
        return
    key = f"sess:{session_id}"
    if await redis_client.exists(key):
        await redis_client.hset(key, "last_activity", str(int(datetime.utcnow().timestamp())))
        await redis_client.expire(key, SESSION_TTL_SECONDS)


async def delete_session(session_id: str):
    if not session_id or redis_client is None:
        return
    await redis_client.delete(f"sess:{session_id}")
