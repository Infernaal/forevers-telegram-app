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
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть DBDC Capital Forevers Bot",
            web_app=WebAppInfo(url="https://dbdc-mini.dubadu.com/")
        )]
    ])
    await message.answer("Добро пожаловать в Dubadu!", reply_markup=kb)

async def main():
    logger.info("🤖 DBDC Capital Forevers Bot запущен и работает!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
