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
    logger.info("RAW init_data: %r", raw)

    raw_map = parse_init_data_raw(raw)
    logger.info("Parsed init_data: %s", raw_map)

    provided_hash = raw_map.get("hash")
    if not provided_hash:
        raise TelegramAuthError("Missing hash in init data")

    token = bot_token or BOT_TOKEN
    if not token:
        raise TelegramAuthError("Bot token not configured")

    # 1. Генерируем secret_key
    secret_key = hmac.new(token.encode(), b"WebAppData", hashlib.sha256).digest()

    # 2. Собираем data_check_string
    data_check_string = "\n".join(
        f"{k}={raw_map[k]}"
        for k in sorted(raw_map.keys())
        if k != "hash"
    )
    logger.info("Data check string (exact): %r", data_check_string)

    # 3. Вычисляем hash
    calc_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    logger.info("Provided hash: %s", provided_hash)
    logger.info("Calculated hash: %s", calc_hash)

    if calc_hash != provided_hash:
        raise TelegramAuthError("Invalid init data signature")

    # 4. Проверка времени
    auth_date = int(raw_map.get("auth_date", "0"))
    if max_age and (time.time() - auth_date > max_age):
        raise TelegramAuthError("Init data expired")

    # 5. Декодируем
    from urllib.parse import unquote_plus
    decoded_map = {k: unquote_plus(v) for k, v in raw_map.items()}

    user_obj = {}
    if "user" in decoded_map:
        try:
            user_obj = json.loads(decoded_map["user"])
        except Exception:
            pass

    return {"user": user_obj, "auth_date": auth_date, "raw": decoded_map}