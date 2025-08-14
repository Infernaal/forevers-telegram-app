import hashlib
import hmac
import json
import time
import logging
from typing import Dict, Any, Optional
import os
from dotenv import load_dotenv

# Настраиваем логгер
logger = logging.getLogger(__name__)

# Загрузка .env
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


class TelegramAuthError(Exception):
    pass


def parse_init_data_raw(raw: str) -> Dict[str, str]:
    """Парсит initData, сохраняя значения в исходном URL-encoded виде (для подписи)."""
    result: Dict[str, str] = {}
    if not raw:
        return result
    for p in raw.split("&"):
        if not p or "=" not in p:
            continue
        k, v = p.split("=", 1)
        result[k] = v  # ❗ без decode
    return result


def build_data_check_string(items: Dict[str, str]) -> str:
    """Формирует строку для проверки подписи (по документации Telegram)."""
    filtered = {k: v for k, v in items.items() if k not in ("hash", "signature")}
    lines = [f"{k}={filtered[k]}" for k in sorted(filtered.keys())]
    return "\n".join(lines)


def verify_init_data(raw: str, bot_token: Optional[str] = None, max_age: Optional[int] = 600) -> Dict[str, Any]:
    logger.info("RAW init_data: %s", raw)

    # Оставляем оригинальные значения для подписи
    raw_map = parse_init_data_raw(raw)
    logger.info("Parsed init_data (raw values): %s", raw_map)

    provided_hash = raw_map.get("hash")
    if not provided_hash:
        raise TelegramAuthError("Missing hash in init data")

    token = bot_token or BOT_TOKEN
    if not token:
        raise TelegramAuthError("Bot token not configured")

    logger.info("Using BOT_TOKEN: %s", token)

    # Формируем secret_key (WebAppData + bot_token)
    secret_key = hmac.new(
        key=token.encode(),       # bot_token
        msg=b"WebAppData",        # "WebAppData"
        digestmod=hashlib.sha256
    ).digest()

    # Строка для подписи
    data_check_string = build_data_check_string(raw_map)
    logger.info("Data check string: %s", data_check_string)

    # Хэш
    calc_hash = hmac.new(
        secret_key,
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    logger.info("Provided hash: %s", provided_hash)
    logger.info("Calculated hash: %s", calc_hash)

    if not hmac.compare_digest(calc_hash, provided_hash):
        raise TelegramAuthError("Invalid init data signature")

    # Проверка свежести auth_date
    auth_date_raw = raw_map.get("auth_date")
    auth_date_int = int(auth_date_raw) if auth_date_raw and auth_date_raw.isdigit() else None
    if auth_date_int and max_age is not None:
        if int(time.time()) - auth_date_int > max_age:
            raise TelegramAuthError("Init data expired")

    # Декодирование значений уже после успешной валидации
    from urllib.parse import unquote_plus
    decoded_map = {k: unquote_plus(v) for k, v in raw_map.items()}

    # Преобразуем user в объект
    user_obj = {}
    if decoded_map.get("user"):
        try:
            user_obj = json.loads(decoded_map["user"])
        except json.JSONDecodeError:
            pass

    return {"user": user_obj, "auth_date": auth_date_int, "raw": decoded_map}
