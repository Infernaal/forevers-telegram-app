import os
import logging
import httpx
from typing import Optional, Dict, Any, List

logger = logging.getLogger(__name__)

TONCENTER_API_KEY = os.getenv("TONCENTER_API_KEY")
TON_NETWORK = os.getenv("TON_NETWORK", "testnet").lower()
BASE_URL = "https://toncenter.com/api/v2" if TON_NETWORK == "mainnet" else "https://testnet.toncenter.com/api/v2"

class TonCenter:
    @staticmethod
    async def get_transactions(address: str, limit: int = 20) -> List[Dict[str, Any]]:
        params = {"address": address, "limit": limit}
        if TON_NETWORK == "testnet":
            params["testnet"] = 1
        headers = {"Accept": "application/json"}
        if TONCENTER_API_KEY:
            headers["X-API-Key"] = TONCENTER_API_KEY
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{BASE_URL}/getTransactions", params=params, headers=headers, timeout=15)
            r.raise_for_status()
            data = r.json()
            return data.get("result", [])

    @staticmethod
    def extract_incoming_to_address(tx: Dict[str, Any]) -> Optional[str]:
        try:
            return tx.get("in_msg", {}).get("destination")
        except Exception:
            return None

    @staticmethod
    def extract_source_address(tx: Dict[str, Any]) -> Optional[str]:
        try:
            return tx.get("in_msg", {}).get("source")
        except Exception:
            return None

    @staticmethod
    def extract_value_nano(tx: Dict[str, Any]) -> int:
        try:
            val = tx.get("in_msg", {}).get("value")
            return int(val) if val is not None else 0
        except Exception:
            return 0
