import os
import time
from decimal import Decimal
from typing import Tuple
import json
import httpx
from sessions.redis_session import init_redis

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd"
CACHE_KEY = "ton:rate:usd"
CACHE_TTL = 60  # seconds

async def get_ton_rate_usd() -> Tuple[Decimal, int]:
    """Return (usd_per_ton, timestamp)
    Uses Redis cache for 60s and fetches from Coingecko when expired.
    """
    redis = await init_redis()
    now = int(time.time())

    cached = await redis.get(CACHE_KEY)
    if cached:
        try:
            obj = json.loads(cached)
            if now - int(obj.get("ts", 0)) < CACHE_TTL:
                return Decimal(str(obj["rate"])), int(obj["ts"]) 
        except Exception:
            pass

    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(COINGECKO_URL)
        r.raise_for_status()
        data = r.json()
        usd = Decimal(str(data["the-open-network"]["usd"]))
        await redis.set(CACHE_KEY, json.dumps({"rate": float(usd), "ts": now}), ex=CACHE_TTL)
        return usd, now
