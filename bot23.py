import logging
import random
import asyncio
import os
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Твой токен бота (замени на реальный)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Загружаем настройки из config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

GENERAL_COMPLIMENTS = config.get("GENERAL_COMPLIMENTS", [])
PERSONAL_COMPLIMENTS = config.get("PERSONAL_COMPLIMENTS", {})

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /compliment
@dp.message(Command("compliment"))
async def send_compliment(message: types.Message):
    username = message.from_user.username
    first_name = message.from_user.first_name or "Друг"
    
    if username and f"@{username}" in PERSONAL_COMPLIMENTS:
        compliment = random.choice(PERSONAL_COMPLIMENTS[f"@{username}"]).format(first_name=first_name)
    else:
        compliment = random.choice(GENERAL_COMPLIMENTS)
    
    await message.answer(compliment)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
