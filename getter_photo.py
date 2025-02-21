import os
import random
from aiogram.types import FSInputFile

IMAGE_DIR = "images"
IMAGE_PATHS = [os.path.join(IMAGE_DIR, file) for file in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, file))]

async def get_random_photo_async():
    image_path = random.choice(IMAGE_PATHS)
    return FSInputFile(image_path)