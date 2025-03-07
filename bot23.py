import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
import getter_text
import getter_photo
import getter_audio
from datetime import datetime
import json
import getter_loading


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

# Загрузка настроек из config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

PERSON_DESCRIPTIONS = config.get("PERSON_DESCRIPTIONS", {})
DEFAULT_NAME = "default"

@dp.message(Command("getrespect"))
async def send_compliment(message: types.Message):
    """Обработчик команды /getrespect."""
    username = message.from_user.username
    first_name = message.from_user.first_name or "Товарищ"

    person_info = PERSON_DESCRIPTIONS.get(f"@{username}", PERSON_DESCRIPTIONS[DEFAULT_NAME])
    description = person_info["description"].format(first_name=first_name)
    if person_info["tag"] == "ManDay":
        loading_tag = getter_loading.LoadingTag.ManDay
        image_tag = getter_photo.ImageTag.ManDay
        audio_tag = getter_audio.AudioTag.ManDay
    if person_info["tag"] == "WomanDay":
        loading_tag = getter_loading.LoadingTag.WomanDay
        image_tag = getter_photo.ImageTag.WomanDay
        audio_tag = getter_audio.AudioTag.WomanDay

    loading_path = await getter_loading.get_random_loading(loading_tag)
    loading = FSInputFile(loading_path)
    loading_msg = await message.answer_animation(loading)


    compliment = await getter_text.get_random_text_async(description)

    logging.info(f"username: {username}")
    logging.info(f"compliment: {compliment}")

    photo_path = await getter_photo.get_random_photo_async(image_tag)
    photo = FSInputFile(photo_path)

    voice_path = getter_audio.get_audio(text=compliment, filename=f"{username}_{datetime.now().timestamp()}.mp3", tag = audio_tag)
    voice = FSInputFile(voice_path)

    await loading_msg.delete()

    await message.answer_photo(photo=photo, caption=compliment)
    await message.answer_audio(audio=voice)
    os.remove(voice_path)
       

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())