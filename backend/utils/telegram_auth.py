import hashlib
import hmac
import json
import time
from typing import Dict, Any, Optional
from urllib.parse import unquote_plus
import os
from dotenv import load_dotenv

# Загрузка .env, если используешь
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


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


def verify_init_data(raw: str, bot_token: Optional[str] = None, max_age: int | None = 600) -> Dict[str, Any]:
    """Verify Telegram WebApp init data per official spec.

    Steps (https://core.telegram.org/bots/webapps#validating-data-received-via-the-mini-app):
      1. Parse query-string like data into key/value pairs.
      2. Construct data_check_string from all fields except hash sorted alphabetically as lines 'key=value'.
      3. Derive secret key: HMAC_SHA256(key=<bot_token>, data="WebAppData").
      4. Compute HMAC_SHA256(data_check_string, secret_key) hex digest and constant-time compare with provided hash.
      5. Optionally validate auth_date is recent (max_age seconds) to mitigate replay (default 10 minutes).
    Returns dict with user object, auth_date (int), raw map.
    Raises TelegramAuthError on any validation problem.
    """
    data_map = parse_init_data(raw)
    provided_hash = data_map.get("hash")
    if not provided_hash:
        raise TelegramAuthError("Missing hash in init data")

    token = bot_token or BOT_TOKEN
    if not token:
        raise TelegramAuthError("Bot token not configured")

    # ✅ Correct derivation: bot_token is the HMAC key, "WebAppData" is the message
    secret_key = hmac.new(
        key=token.encode(),
        msg=b"WebAppData",
        digestmod=hashlib.sha256,
    ).digest()

    data_check_string = build_data_check_string(data_map)
    calc_hash = hmac.new(
        secret_key,
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(calc_hash, provided_hash):
        raise TelegramAuthError("Invalid init data signature")

    # Freshness check (optional per spec, enabled by default) to prevent replay
    auth_date_raw = data_map.get("auth_date")
    auth_date_int: Optional[int] = None
    if auth_date_raw and auth_date_raw.isdigit():
        auth_date_int = int(auth_date_raw)
        if max_age is not None:
            now = int(time.time())
            if now - auth_date_int > max_age:
                raise TelegramAuthError("Init data expired")

    # Extract user json if present
    user_raw = data_map.get("user")
    user_obj: Dict[str, Any] = {}
    if user_raw:
        try:
            user_obj = json.loads(user_raw)
        except json.JSONDecodeError:
            pass

    return {"user": user_obj, "auth_date": auth_date_int, "raw": data_map}
