import os
import json
import time
import hmac
import hashlib
import logging
import urllib.parse as up
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# ── setup ──────────────────────────────────────────────────────────────────────
logger = logging.getLogger(__name__)
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class TelegramAuthError(Exception):
    pass

# ── utils ──────────────────────────────────────────────────────────────────────
def parse_init_data_raw(raw: str) -> Dict[str, str]:
    """Парсим initData в dict, сохраняя значения в RAW (URL-encoded) виде."""
    items: Dict[str, str] = {}
    if not raw:
        return items
    for p in raw.split("&"):
        if "=" in p:
            k, v = p.split("=", 1)
            items[k] = v
    return items

def _join_decoded(d: Dict[str, str]) -> str:
    return "\n".join(
        f"{k}={up.unquote_plus(d[k])}"
        for k in sorted(k for k in d if k not in ("hash", "signature"))
    )

def _join_raw(d: Dict[str, str]) -> str:
    return "\n".join(
        f"{k}={d[k]}"
        for k in sorted(k for k in d if k not in ("hash", "signature"))
    )

def _join_mixed_user_raw(d: Dict[str, str]) -> str:
    # Все значения decoded, КРОМЕ user (оставляем RAW)
    return "\n".join(
        f"{k}={(d[k] if k == 'user' else up.unquote_plus(d[k]))}"
        for k in sorted(k for k in d if k not in ("hash", "signature"))
    )

def _secret_key(bot_token: str) -> bytes:
    # ВАЖНО: key=bot_token, msg=b"WebAppData"
    return hmac.new(bot_token.encode(), b"WebAppData", hashlib.sha256).digest()

def _hmac_hex(secret: bytes, s: str) -> str:
    return hmac.new(secret, s.encode(), hashlib.sha256).hexdigest()

# ── main ───────────────────────────────────────────────────────────────────────
def verify_init_data(raw: str, bot_token: Optional[str] = None, max_age: Optional[int] = 600) -> Dict[str, Any]:
    """
    Устойчивая проверка подписи initData.
    Пробуем несколько канонизаций строки. Логируем, какой вариант дал MATCH.
    """
    logger.info("RAW init_data: %r", raw)

    raw_map = parse_init_data_raw(raw)
    logger.info("Parsed init_data (raw map): %s", raw_map)

    provided_hash = raw_map.get("hash")
    if not provided_hash:
        raise TelegramAuthError("Missing hash in init data")

    token = (bot_token or BOT_TOKEN or "").strip()
    if not token:
        raise TelegramAuthError("Bot token not configured")

    secret = _secret_key(token)

    # ── Диагностика user.photo_url (ищем потерю точки в 't.me') ───────────────
    user_dec = up.unquote_plus(raw_map.get("user", ""))
    photo_url = ""
    if user_dec:
        try:
            uobj = json.loads(user_dec)
            photo_url = uobj.get("photo_url", "") or ""
        except Exception:
            pass
    if photo_url:
        if "t.me" not in photo_url:
            logger.error("user.photo_url decoded has NO 't.me': %r", photo_url)
        if "tme" in photo_url and "t.me" not in photo_url:
            logger.error("Suspicious 'tme' fragment in photo_url: %r", photo_url)

    # ── Готовим варианты строки для HMAC ───────────────────────────────────────
    variants: Dict[str, str] = {
        "decoded": _join_decoded(raw_map),
        "raw": _join_raw(raw_map),
        "mixed_user_raw": _join_mixed_user_raw(raw_map),
    }

    # Точечный dot-fix ТОЛЬКО внутри user.photo_url (если по дороге потеряли '.')
    if user_dec:
        try:
            u = json.loads(user_dec)
            if (
                isinstance(u, dict)
                and "photo_url" in u
                and "tme/" in u["photo_url"]
                and "t.me/" not in u["photo_url"]
            ):
                u_fix = dict(u)
                u_fix["photo_url"] = u_fix["photo_url"].replace("tme/", "t.me/")
                user_fix_raw = up.quote_plus(
                    json.dumps(u_fix, ensure_ascii=False, separators=(",", ":"))
                )
                patched = dict(raw_map)
                patched["user"] = user_fix_raw
                variants["decoded_user_dotfix"] = _join_decoded(patched)
        except Exception:
            pass

    # ── Считаем хэши по всем вариантам и ищем совпадение ──────────────────────
    matched_name = None
    matched_check_string = None
    for name, check_str in variants.items():
        h = _hmac_hex(secret, check_str)
        logger.info("Variant %-18s hash=%s %s", name, h, "(MATCH)" if h == provided_hash else "")
        if h == provided_hash:
            matched_name = name
            matched_check_string = check_str
            break

    if not matched_name:
        # Ни один вариант не совпал — логируем каноничный decoded и падаем
        data_check_string = variants["decoded"]
        logger.info("Data check string (decoded & sorted): %r", data_check_string)
        logger.info("Provided hash:   %s", provided_hash)
        calc_hash = _hmac_hex(secret, data_check_string)
        logger.info("Calculated hash: %s", calc_hash)
        raise TelegramAuthError("Invalid init data signature")

    # ── TTL ────────────────────────────────────────────────────────────────────
    auth_date = int(raw_map.get("auth_date", "0"))
    if max_age and (time.time() - auth_date > max_age):
        raise TelegramAuthError("Init data expired")

    # ── Удобный результат ─────────────────────────────────────────────────────
    decoded_map = {k: up.unquote_plus(v) for k, v in raw_map.items()}
    user_obj = {}
    if "user" in decoded_map:
        try:
            user_obj = json.loads(decoded_map["user"])
        except Exception:
            pass

    logger.info("Matched variant used for verification: %s", matched_name)
    return {
        "user": user_obj,
        "auth_date": auth_date,
        "raw": decoded_map,
        "matched_variant": matched_name,        # ← оставлю, пригодится в логах/UI
    }
