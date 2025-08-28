import asyncio
from decimal import Decimal
import logging
import httpx

logger = logging.getLogger(__name__)

COINGECKO_URLS = [
    "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd",
    "https://api.coingecko.com/api/v3/simple/price?ids=toncoin&vs_currencies=usd",
]
TONAPI_URL = "https://tonapi.io/v2/rates?tokens=ton&currencies=usd"

async def _fetch_json(client: httpx.AsyncClient, url: str):
    r = await client.get(url, timeout=10)
    r.raise_for_status()
    return r.json()

async def get_ton_usd_price() -> Decimal:
    async with httpx.AsyncClient() as client:
        # Try CoinGecko variants
        for url in COINGECKO_URLS:
            try:
                data = await _fetch_json(client, url)
                if "the-open-network" in data and "usd" in data["the-open-network"]:
                    return Decimal(str(data["the-open-network"]["usd"]))
                if "toncoin" in data and "usd" in data["toncoin"]:
                    return Decimal(str(data["toncoin"]["usd"]))
            except Exception as e:
                logger.warning(f"CoinGecko fetch failed from {url}: {e}")
        # Fallback to tonapi
        try:
            data = await _fetch_json(client, TONAPI_URL)
            # tonapi format: {"rates": {"ton": {"prices": {"usd": 2.3}}}}
            usd = (
                data.get("rates", {})
                .get("ton", {})
                .get("prices", {})
                .get("usd")
            )
            if usd:
                return Decimal(str(usd))
        except Exception as e:
            logger.error(f"TONAPI fetch failed: {e}")
    raise RuntimeError("Unable to fetch TON/USD price from external sources")
