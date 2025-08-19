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
from dependencies.current_user import get_current_user
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

router = APIRouter(tags=["referral"])

class InviteResponse(BaseModel):
    invite_link: str
    qr_code: str  # Base64 encoded QR code image
    user_id: int
    code: str


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
async def get_invite_data(current_user_id: int = Depends(get_current_user)):
    """
    Единый endpoint для получения реферальной ссылки и QR-кода
    Возвращает invite_link и qr_code (base64) в одном ответе
    """
    try:
        # Генерируем уникальный 6-значный код
        unique_code = generate_unique_code()

        # Формируем параметры реферальной ссылки
        ref_params = f"ref={current_user_id}&code={unique_code}"

        # Получаем BASE_URL из переменной окружения или используем значение по умолчанию
        base_url = os.getenv("BASE_URL", "https://yourdomain.com")

        # Создаем короткую ссылку для отображения с вашим адресом
        display_link = f"{base_url}?{ref_params}"

        # Создаем полную ссылку для QR-кода и шаринга (Telegram bot)
        telegram_bot_url = os.getenv("TELEGRAM_BOT_URL", "https://t.me/your_bot_name")
        full_link = f"{telegram_bot_url}?start={ref_params}"

        # Генерируем QR-код как base64 (используем display_link для QR-кода)
        qr_code_base64 = generate_qr_code_base64(display_link)

        logger.info(f"Generated invite data for user {current_user_id}: {display_link}")

        return InviteResponse(
            invite_link=display_link,
            qr_code=qr_code_base64,
            user_id=current_user_id,
            code=unique_code
        )
    except Exception as e:
        logger.error(f"Error generating invite data for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate invite data")
