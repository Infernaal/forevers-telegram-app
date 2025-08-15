import os
import hmac
import json
import time
import hashlib
from typing import Dict, Any, Optional
from urllib.parse import parse_qsl
import logging

logger = logging.getLogger(__name__)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class TelegramAuthError(Exception):
    pass

def verify_init_data(raw: str, bot_token: Optional[str] = None, max_age: Optional[int] = 600) -> Dict[str, Any]:
    """
    Проверка подписи initData в стиле aiogram.
    """
    # Парсим строку initData в decoded dict
    try:
        parsed: Dict[str, str] = dict(parse_qsl(raw, keep_blank_values=True))
    except ValueError:
        raise TelegramAuthError("Init data is not a valid query string")

    provided_hash = parsed.pop("hash", None)
    if not provided_hash:
        raise TelegramAuthError("Missing hash in init data")

    token = (bot_token or BOT_TOKEN or "").strip()
    if not token:
        raise TelegramAuthError("Bot token not configured")

    # Собираем data_check_string
    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(parsed.items()))

    # Формируем секретный ключ
    secret_key = hmac.new(
        key=b"WebAppData",
        msg=token.encode(),
        digestmod=hashlib.sha256
    ).digest()

    # Считаем хэш
    calc_hash = hmac.new(
        key=secret_key,
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    if calc_hash != provided_hash:
        raise TelegramAuthError("Invalid init data signature")

    # Проверка времени (TTL)
    try:
        auth_date = int(parsed.get("auth_date", "0"))
    except ValueError:
        auth_date = 0

    if max_age and auth_date and (time.time() - auth_date > max_age):
        raise TelegramAuthError("Init data expired")

    # Декодируем user
    user_obj: Dict[str, Any] = {}
    if "user" in parsed:
        try:
            user_obj = json.loads(parsed["user"])
        except Exception:
            pass

    return {
        "user": user_obj,
        "auth_date": auth_date,
        "raw": parsed
    }
