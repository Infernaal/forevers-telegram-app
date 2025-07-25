from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.filters import Command
import asyncio
import os
from dotenv import load_dotenv

# Загрузка .env, если используешь
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7824657603:AAG8LihPnR1P2aM8RjRCOQw76VbrZnA8VR8")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))  # ✅ Aiogram 3.x фильтр
async def start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть Dubadu App",
            web_app=WebAppInfo(url="https://dubadu.com/ru")
        )]
    ])
    await message.answer("Добро пожаловать в Dubadu!", reply_markup=kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
