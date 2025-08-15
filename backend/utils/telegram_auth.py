import os
import hmac
import json
import time
import hashlib
import logging
from typing import Dict, Any, Optional
from urllib.parse import parse_qsl

logger = logging.getLogger(__name__)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class TelegramAuthError(Exception):
    pass

def verify_init_data(raw: str, bot_token: Optional[str] = None, max_age: Optional[int] = 600) -> Dict[str, Any]:
    """
    Валидация initData в стиле aiogram:
      1) parse_qsl -> decoded пары
      2) сортировка по ключу, склейка 'k=v' через '\n'
      3) secret_key = HMAC_SHA256(key="WebAppData", msg=bot_token)
      4) calc = HMAC_SHA256(key=secret_key, msg=data_check_string)
    """
    logger.info("RAW init_data: %r", raw)

    # 1) Разобрать query-string в decoded dict (без реконструкции JSON!)
    try:
        parsed: Dict[str, str] = dict(parse_qsl(raw, keep_blank_values=True))
    except ValueError:
        raise TelegramAuthError("Init data is not a valid query string")

    logger.info("Parsed init_data (decoded): %s", parsed)

    provided_hash = parsed.pop("hash", None)
    if not provided_hash:
        raise TelegramAuthError("Missing hash in init data")

    token = (bot_token or BOT_TOKEN or "").strip()
    if not token:
        raise TelegramAuthError("Bot token not configured")

    # 2) Сформировать data_check_string (из decoded значений)
    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(parsed.items()))
    logger.info("Data check string: %r", data_check_string)

    # 3) Секретный ключ и итоговый HMAC (как в aiogram)
    secret_key = hmac.new(key=b"WebAppData", msg=token.encode(), digestmod=hashlib.sha256).digest()
    calc_hash = hmac.new(key=secret_key, msg=data_check_string.encode(), digestmod=hashlib.sha256).hexdigest()

    logger.info("Provided hash:   %s", provided_hash)
    logger.info("Calculated hash: %s", calc_hash)

    if calc_hash != provided_hash:
        raise TelegramAuthError("Invalid init data signature")

    # 4) TTL (опционально)
    try:
        auth_date = int(parsed.get("auth_date", "0"))
    except ValueError:
        auth_date = 0
    if max_age and auth_date and (time.time() - auth_date > max_age):
        raise TelegramAuthError("Init data expired")

    # 5) Вернём user/прочее
    user_obj: Dict[str, Any] = {}
    user_str = parsed.get("user")
    if user_str:
        try:
            user_obj = json.loads(user_str)
        except Exception:
            logger.warning("Failed to json-parse user: %r", user_str[:200])

    return {"user": user_obj, "auth_date": auth_date, "raw": parsed}
