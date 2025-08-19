from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.filters import Command
import asyncio
import os
import logging
from dotenv import load_dotenv

# Загрузка .env, если используешь
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))  # ✅ Aiogram 3.x фильтр
async def start(message: Message):
    # Extract referral parameter from /start command
    command_args = message.text.split(maxsplit=1)
    referral_param = command_args[1] if len(command_args) > 1 else None

    # Build Web App URL with referral parameter
    web_app_url = "https://dbdc-mini.dubadu.com/"
    if referral_param and referral_param.startswith('ref_'):
        web_app_url += f"?startapp={referral_param}"

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть DBDC Capital Forevers Bot",
            web_app=WebAppInfo(url=web_app_url)
        )]
    ])

    welcome_text = "Добро пожаловать в Dubadu!"
    if referral_param:
        welcome_text += f"\n🎁 Вы перешли по реферальной ссылке!"

    await message.answer(welcome_text, reply_markup=kb)


# Handle any text message to always show the app button
@dp.message()
async def any_message(message: Message):
    # For any message, show the app button
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть DBDC Capital Forevers Bot",
            web_app=WebAppInfo(url="https://dbdc-mini.dubadu.com/")
        )]
    ])

    await message.answer("Используйте кнопку ниже, чтобы открыть приложение:", reply_markup=kb)

async def main():
    logger.info("🤖 DBDC Capital Forevers Bot запущен и работает!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
