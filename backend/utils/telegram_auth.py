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
    """Формирует строку для проверки подписи."""
    filtered = {k: v for k, v in items.items() if k != "hash"}
    lines = [f"{k}={filtered[k]}" for k in sorted(filtered.keys())]
    return "\n".join(lines)


def verify_init_data(raw: str, bot_token: Optional[str] = None, max_age: int | None = 600) -> Dict[str, Any]:
    """Проверка Telegram WebApp init data по официальной спецификации."""
    logger.info("RAW init_data: %s", raw)

    data_map = parse_init_data(raw)
    logger.info("Parsed init_data: %s", data_map)

    provided_hash = data_map.get("hash")
    if not provided_hash:
        logger.warning("Missing hash in init data")
        raise TelegramAuthError("Missing hash in init data")

    token = bot_token or BOT_TOKEN
    if not token:
        logger.error("Bot token not configured")
        raise TelegramAuthError("Bot token not configured")

    logger.info("Using BOT_TOKEN: %s", token)

    # ✅ Правильное формирование secret_key
    secret_key = hmac.new(
        key=b"WebAppData",       # фиксированная строка
        msg=token.encode(),      # токен бота
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
        logger.warning("Invalid init data signature: provided != calculated")
        raise TelegramAuthError("Invalid init data signature")

    # Проверка свежести auth_date
    auth_date_raw = data_map.get("auth_date")
    auth_date_int: Optional[int] = None
    if auth_date_raw and auth_date_raw.isdigit():
        auth_date_int = int(auth_date_raw)
        logger.info("Auth date: %s (%s)", auth_date_int, time.ctime(auth_date_int))
        if max_age is not None:
            now = int(time.time())
            logger.info("Now: %s (%s)", now, time.ctime(now))
            if now - auth_date_int > max_age:
                logger.warning("Init data expired")
                raise TelegramAuthError("Init data expired")

    # Разбор user JSON
    user_raw = data_map.get("user")
    user_obj: Dict[str, Any] = {}
    if user_raw:
        try:
            user_obj = json.loads(user_raw)
            logger.info("Parsed user object: %s", user_obj)
        except json.JSONDecodeError:
            logger.warning("Failed to decode user JSON: %s", user_raw)

    return {"user": user_obj, "auth_date": auth_date_int, "raw": data_map}