from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import secrets
import string
import qrcode
from io import BytesIO
import base64
import logging
import os
from dependencies.current_user import get_current_user_id
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.database import get_db
from models.models import Users

load_dotenv()
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/referral", tags=["Referral"])

class InviteResponse(BaseModel):
    invite_link: str
    qr_code: str  # Base64 encoded QR code image
    user_id: int
    code: str

class ReferrerInfoResponse(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str


def generate_unique_code(length: int = 6) -> str:
    """Генерирует уникальный 6-значный код из букв и цифр"""
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def generate_qr_code_base64(data: str) -> str:
    """Генерирует QR-код и возвращает его как base64 строку"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Создаем изображение QR-кода
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Конвертируем в base64
    img_buffer = BytesIO()
    qr_img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    # Конвертируем в base64 строку
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{img_base64}"

@router.get("/invite", response_model=InviteResponse)
async def get_invite_data(current_user_id: int = Depends(get_current_user_id)):
    """
    Единый endpoint для получения реферальной ссылки и QR-кода
    Возвращает invite_link и qr_code (base64) в одном ответе
    """
    try:
        # Генерируем уникальный 6-значный код
        unique_code = generate_unique_code()

        # Формируем Telegram WebApp ссылку в правильном формате
        # Формат: https://t.me/dbdc_test_bot/app?startapp=ref_4344_code_52J01Z
        telegram_bot_name = os.getenv("TELEGRAM_BOT_NAME", "dbdc_test_bot")
        telegram_webapp_link = f"https://t.me/{telegram_bot_name}/?startapp=ref_{current_user_id}_code_{unique_code}"

        # Генерируем QR-код как base64 (используем telegram_webapp_link для QR-кода)
        qr_code_base64 = generate_qr_code_base64(telegram_webapp_link)

        logger.info(f"Generated invite data for user {current_user_id}: {telegram_webapp_link}")

        return InviteResponse(
            invite_link=telegram_webapp_link,
            qr_code=qr_code_base64,
            user_id=current_user_id,
            code=unique_code
        )
    except Exception as e:
        logger.error(f"Error generating invite data for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate invite data")

@router.get("/referrer/{ref_id}", response_model=ReferrerInfoResponse)
async def get_referrer_info(ref_id: int, db: AsyncSession = Depends(get_db)):
    """
    Get referrer information by referral ID
    """
    try:
        result = await db.execute(
            select(Users).where(Users.id == ref_id)
        )
        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=404, detail="Referrer not found")

        return ReferrerInfoResponse(
            user_id=user.id,
            first_name=user.first_name or "",
            last_name=user.last_name or "",
            email=user.email or ""
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting referrer info for ref_id {ref_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get referrer information")
