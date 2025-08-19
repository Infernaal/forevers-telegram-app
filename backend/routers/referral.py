from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import secrets
import string
import qrcode
from io import BytesIO
import base64
import logging
from dependencies.current_user import get_current_user

logger = logging.getLogger(__name__)

router = APIRouter(tags=["referral"])

class InviteResponse(BaseModel):
    invite_link: str
    qr_code: str  # Base64 encoded QR code image
    user_id: int
    code: str

class ReferralLinkResponse(BaseModel):
    referral_link: str
    user_id: int
    code: str

class QRCodeRequest(BaseModel):
    referral_link: str

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

        # Создаем короткую ссылку для отображения
        display_link = f"vm.dubadu/{unique_code}"

        # Создаем полную ссылку для QR-кода и шаринга
        # В production замените на ваш реальный домен/бота
        full_link = f"https://t.me/your_bot_name?start={ref_params}"

        # Генерируем QR-код как base64
        qr_code_base64 = generate_qr_code_base64(full_link)

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

@router.get("/referral-link", response_model=ReferralLinkResponse)
async def generate_referral_link(current_user_id: int = Depends(get_current_user)):
    """
    Генерирует реферальную ссылку для текущего пользователя
    Формат: ?ref=user_id&code={6 digits}
    """
    try:
        # Генерируем уникальный 6-значный код
        unique_code = generate_unique_code()
        
        # Формируем реферальную ссылку
        referral_link = f"?ref={current_user_id}&code={unique_code}"
        
        logger.info(f"Generated referral link for user {current_user_id}: {referral_link}")
        
        return ReferralLinkResponse(
            referral_link=referral_link,
            user_id=current_user_id,
            code=unique_code
        )
    except Exception as e:
        logger.error(f"Error generating referral link for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate referral link")

@router.post("/generate-qr-code")
async def generate_qr_code(request: QRCodeRequest):
    """
    Генерирует QR-код на основе реферальной ссылки
    Возвращает изображение QR-кода в формате PNG
    """
    try:
        # Создаем полную ссылку для QR-кода
        # В production замените на ваш реальный домен
        base_url = "https://t.me/your_bot_name?start="
        full_url = f"{base_url}{request.referral_link.lstrip('?')}"
        
        # Создаем QR-код
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(full_url)
        qr.make(fit=True)
        
        # Создаем изображение QR-кода
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Сохраняем в BytesIO
        img_buffer = BytesIO()
        qr_img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        
        logger.info(f"Generated QR code for link: {full_url}")
        
        return StreamingResponse(
            BytesIO(img_buffer.getvalue()), 
            media_type="image/png",
            headers={"Content-Disposition": "inline; filename=qr_code.png"}
        )
    except Exception as e:
        logger.error(f"Error generating QR code: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate QR code")

@router.get("/full-referral-link")
async def get_full_referral_link(current_user_id: int = Depends(get_current_user)):
    """
    Возвращает полную реферальную ссылку для отображения в интерфейсе
    """
    try:
        # Генерируем уникальный код
        unique_code = generate_unique_code()
        
        # Формируем параметры
        ref_params = f"ref={current_user_id}&code={unique_code}"
        
        # Возвращаем короткую ссылку для отображения
        display_link = f"vm.dubadu/{unique_code}"
        
        logger.info(f"Generated display link for user {current_user_id}: {display_link}")
        
        return {
            "display_link": display_link,
            "full_link": f"https://t.me/your_bot_name?start={ref_params}",
            "qr_params": f"?{ref_params}",
            "user_id": current_user_id,
            "code": unique_code
        }
    except Exception as e:
        logger.error(f"Error generating full referral link for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate referral link")
