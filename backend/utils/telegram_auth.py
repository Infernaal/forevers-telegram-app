import hashlib
import hmac, hashlib
import urllib.parse as up
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

def calc_hash_variants(raw_map: dict, bot_token: str):
    secret = hmac.new(bot_token.encode(), b"WebAppData", hashlib.sha256).digest()

    # A) твоя правильная стратегия: DECODED для всех ключей
    s_dec = "\n".join(f"{k}={up.unquote_plus(raw_map[k])}"
                      for k in sorted(k for k in raw_map if k not in ("hash","signature")))
    h_dec = hmac.new(secret, s_dec.encode(), hashlib.sha256).hexdigest()

    # B) decoded для всех, КРОМЕ user (user берём как в raw, без unquote_plus)
    s_mixed = "\n".join(
        f"{k}={(raw_map[k] if k=='user' else up.unquote_plus(raw_map[k]))}"
        for k in sorted(k for k in raw_map if k not in ("hash","signature"))
    )
    h_mixed = hmac.new(secret, s_mixed.encode(), hashlib.sha256).hexdigest()

    # C) вообще RAW значения без декодирования
    s_raw = "\n".join(f"{k}={raw_map[k]}"
                      for k in sorted(k for k in raw_map if k not in ("hash","signature")))
    h_raw = hmac.new(secret, s_raw.encode(), hashlib.sha256).hexdigest()

    return {
        "decoded": (s_dec, h_dec),
        "raw": (s_raw, h_raw),
        "mixed_user_raw": (s_mixed, h_mixed),
    }

def assert_user_url_intact(raw_map: dict):
    u_raw = raw_map.get("user","")
    u_dec = up.unquote_plus(u_raw)
    if "t.me" not in u_dec:
        logger.error("user JSON decoded lost dot: expected 't.me' in: %r", u_dec)
    # На всякий: покажем 40 символов вокруг
    idx = u_dec.find("tme")
    if idx != -1:
        frag = u_dec[max(0, idx-20): idx+20]
        logger.error("suspicious fragment around 'tme': %r", frag)

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
    filtered = {k: v for k, v in items.items() if k not in ("hash","signature")}
    lines = [f"{k}={up.parse.unquote_plus(filtered[k])}" for k in sorted(filtered)]
    return "\n".join(lines)


def verify_init_data(raw: str, bot_token: Optional[str] = None, max_age: Optional[int] = 600) -> Dict[str, Any]:
    logger.info("RAW init_data: %r", raw)

    raw_map = parse_init_data_raw(raw)
    logger.info("Parsed init_data (raw map): %s", raw_map)

    assert_user_url_intact(raw_map)

    provided_hash = raw_map.get("hash")
    if not provided_hash:
        raise TelegramAuthError("Missing hash in init data")

    token = bot_token or BOT_TOKEN
    if not token:
        raise TelegramAuthError("Bot token not configured")

    variants = calc_hash_variants(raw_map, token)
    provided = raw_map.get("hash","")
    for name, (s, h) in variants.items():
        logger.info("Variant %-14s hash=%s  %s", name, h, "MATCH" if h==provided else "")
        if h == provided:
            logger.info("Matched variant: %s", name)

    # 1) secret_key: HMAC_SHA256("WebAppData", key=bot_token)
    secret_key = hmac.new(token.encode(), b"WebAppData", hashlib.sha256).digest()

    # 2) data_check_string (ИСПОЛЬЗУЕМ функцию с decoded значениями)  # ★
    data_check_string = build_data_check_string(raw_map)  # ★
    logger.info("Data check string (decoded & sorted): %r", data_check_string)

    # 3) calc hash
    calc_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    logger.info("Provided hash:   %s", provided_hash)
    logger.info("Calculated hash: %s", calc_hash)

    if calc_hash != provided_hash:
        raise TelegramAuthError("Invalid init data signature")

    # 4) TTL (по умолчанию 10 минут — можно увеличить)
    auth_date = int(raw_map.get("auth_date", "0"))
    if max_age and (time.time() - auth_date > max_age):
        raise TelegramAuthError("Init data expired")

    # 5) Распарсим удобное представление
    from urllib.parse import unquote_plus
    decoded_map = {k: unquote_plus(v) for k, v in raw_map.items()}

    user_obj = {}
    if "user" in decoded_map:
        try:
            user_obj = json.loads(decoded_map["user"])
        except Exception:
            pass

    return {"user": user_obj, "auth_date": auth_date, "raw": decoded_map}