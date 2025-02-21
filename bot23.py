import logging
import random
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import getter_text
import getter_photo

# Конфигурация
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Константы для выбора типа ответа
TEXT_COMPLIMENT = 0
GPT_COMPLIMENT = 1
IMAGE_RESPONSE = 2

@dp.message(Command("getrespect"))
async def send_compliment(message: types.Message):
    """Обработчик команды /getrespect."""
    username = message.from_user.username
    first_name = message.from_user.first_name or "Товарищ"

    choice = random.choice([TEXT_COMPLIMENT, TEXT_COMPLIMENT, IMAGE_RESPONSE])
    
    if choice == TEXT_COMPLIMENT:
        compliment = await getter_text.get_random_text_async(username, first_name)
        await message.answer(compliment)
    else:
        photo = await getter_photo.get_random_photo_async()
        await message.answer_photo(photo=photo)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())