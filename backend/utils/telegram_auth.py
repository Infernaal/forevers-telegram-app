import hashlib
import hmac
import json
import time
import logging
from typing import Dict, Any, Optional
from urllib.parse import unquote_plus
import os
from dotenv import load_dotenv

# Настраиваем логгер
logger = logging.getLogger(__name__)

# Загрузка .env
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


class TelegramAuthError(Exception):
    pass


def parse_init_data(raw: str) -> Dict[str, str]:
    """Парсит строку initData вида key=value&key=value (URL-encoded)."""
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
    """Формирует строку для проверки подписи (по документации Telegram)."""
    filtered = {k: v for k, v in items.items() if k not in ("hash", "signature")}
    lines = [f"{k}={filtered[k]}" for k in sorted(filtered.keys())]
    return "\n".join(lines)


def verify_init_data(raw: str, bot_token: Optional[str] = None, max_age: int | None = 600) -> Dict[str, Any]:
    logger.info("RAW init_data: %s", raw)

    data_map = parse_init_data(raw)
    logger.info("Parsed init_data: %s", data_map)

    provided_hash = data_map.get("hash")
    if not provided_hash:
        raise TelegramAuthError("Missing hash in init data")

    token = bot_token or BOT_TOKEN
    if not token:
        raise TelegramAuthError("Bot token not configured")

    logger.info("Using BOT_TOKEN: %s", token)

    # ✅ Формируем secret_key по спецификации
    secret_key = hmac.new(
        key=token.encode(),
        msg=b"WebAppData",
        digestmod=hashlib.sha256
    ).digest()

    data_check_string = build_data_check_string(data_map)
    logger.info("Data check string: %s", data_check_string)

    calc_hash = hmac.new(
        secret_key,
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    logger.info("Provided hash: %s", provided_hash)
    logger.info("Calculated hash: %s", calc_hash)

    if not hmac.compare_digest(calc_hash, provided_hash):
        raise TelegramAuthError("Invalid init data signature")

    # Проверка свежести
    auth_date_raw = data_map.get("auth_date")
    auth_date_int = int(auth_date_raw) if auth_date_raw and auth_date_raw.isdigit() else None
    if auth_date_int and max_age is not None:
        if int(time.time()) - auth_date_int > max_age:
            raise TelegramAuthError("Init data expired")

    user_obj = {}
    if data_map.get("user"):
        try:
            user_obj = json.loads(data_map["user"])
        except json.JSONDecodeError:
            pass

    return {"user": user_obj, "auth_date": auth_date_int, "raw": data_map}