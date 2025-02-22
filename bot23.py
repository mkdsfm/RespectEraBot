import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
import getter_text
import getter_photo
import getter_audio

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

    compliment = await getter_text.get_random_text_async(first_name)

    photo_path = await getter_photo.get_random_photo_async()
    photo = FSInputFile(photo_path)

    voice_path = getter_audio.get_audio(compliment)
    voice = FSInputFile(voice_path)

    await message.answer_photo(photo=photo, caption=compliment)
    await message.answer_audio(audio=voice)
    os.remove(voice_path)
       

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())