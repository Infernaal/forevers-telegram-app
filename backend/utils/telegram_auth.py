import hashlib
import hmac
import json
from typing import Dict, Any, Optional
from urllib.parse import unquote_plus
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # must be set in environment


class TelegramAuthError(Exception):
    pass


def parse_init_data(raw: str) -> Dict[str, str]:
    """Parse the raw init data string from Telegram header or query.
    Format: key=value&key=value (URL-encoded). Values are percent-decoded.
    """
    result: Dict[str, str] = {}
    if not raw:
        return result
    parts = raw.split("&")
    for p in parts:
        if not p or "=" not in p:
            continue
        k, v = p.split("=", 1)
        result[k] = unquote_plus(v)
    return result


def build_data_check_string(items: Dict[str, str]) -> str:
    filtered = {k: v for k, v in items.items() if k != "hash"}
    lines = [f"{k}={filtered[k]}" for k in sorted(filtered.keys())]
    return "\n".join(lines)


def verify_init_data(raw: str, bot_token: Optional[str] = None) -> Dict[str, Any]:
    data_map = parse_init_data(raw)
    provided_hash = data_map.get("hash")
    if not provided_hash:
        raise TelegramAuthError("Missing hash in init data")
    token = bot_token or BOT_TOKEN
    if not token:
        raise TelegramAuthError("Bot token not configured")
    secret_key = hashlib.sha256(token.encode()).digest()
    data_check_string = build_data_check_string(data_map)
    h = hmac.new(secret_key, msg=data_check_string.encode(), digestmod=hashlib.sha256).hexdigest()
    if h != provided_hash:
        raise TelegramAuthError("Invalid init data signature")
    # Extract user json if present
    user_raw = data_map.get("user")
    user_obj: Dict[str, Any] = {}
    if user_raw:
        try:
            user_obj = json.loads(user_raw)
        except json.JSONDecodeError:
            pass
    return {"user": user_obj, "auth_date": data_map.get("auth_date"), "raw": data_map}
