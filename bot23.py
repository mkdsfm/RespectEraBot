import logging
import random
import asyncio
import os
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

# Твой токен бота (замени на реальный)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Загружаем настройки из config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

GENERAL_COMPLIMENTS = config.get("GENERAL_COMPLIMENTS", [])
PERSONAL_COMPLIMENTS = config.get("PERSONAL_COMPLIMENTS", {})

IMAGE_DIR = "images"

IMAGE_PATHS = [os.path.join(IMAGE_DIR, file) for file in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, file))]


# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция для проверки, является ли имя женским
def is_feminine(name: str) -> bool:
    # Приводим имя к нижнему регистру и проверяем на окончание
    name = name.lower()
    feminine_endings = [
        'а', 'я', 'ева', 'ина', 'слава', 'ля', 'вика', 'сиса', 'цка',  # Русский
        'a', 'ya', 'eva', 'ina', 'slava', 'lya', 'vika', 'sisa', 'ya', 'tska'  # Транслит
    ]
    return any(name.endswith(ending) for ending in feminine_endings)

# Обработчик команды /compliment
@dp.message()
async def send_compliment(message: types.Message):
    username = message.from_user.username
    first_name = message.from_user.first_name or "Товарищ"

    if is_feminine(first_name) and f"@{username}" not in PERSONAL_COMPLIMENTS:
            return  # Пропустить отправку комплимента для этих пользователей
    
    if random.choice([True, False]):    
        if username and f"@{username}" in PERSONAL_COMPLIMENTS:
            compliment = random.choice(PERSONAL_COMPLIMENTS[f"@{username}"]).format(first_name=first_name)
        else:
            compliment = random.choice(GENERAL_COMPLIMENTS).format(first_name=first_name)

        await message.answer(compliment)
    else:
        if IMAGE_PATHS:
            image_path = random.choice(IMAGE_PATHS)
            photo = FSInputFile(image_path)  # Используем InputFile для корректной отправки
            await message.answer_photo(photo=photo)
                   
# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
