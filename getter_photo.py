import os
import random
from enum import Enum

IMAGE_DIR_23 = "23_images"
IMAGE_PATHS_23 = [os.path.join(IMAGE_DIR_23, file) for file in os.listdir(IMAGE_DIR_23) if os.path.isfile(os.path.join(IMAGE_DIR_23, file))]

IMAGE_DIR_8 = "8_images"
IMAGE_PATHS_8 = [os.path.join(IMAGE_DIR_8, file) for file in os.listdir(IMAGE_DIR_8) if os.path.isfile(os.path.join(IMAGE_DIR_8, file))]

class ImageTag(Enum):
    ManDay = 23
    WomanDay = 8

async def get_random_photo_async(tag = ImageTag.ManDay):
    # gigachad_photo = await getter_gigachad.get_gigachad_photo(bot, message.from_user.id)
    # if gigachad_photo:
    #     await message.answer_photo(photo=types.FSInputFile(gigachad_photo), caption=compliment)
    if tag == ImageTag.ManDay:
        image_path = random.choice(IMAGE_PATHS_23)
    if tag == ImageTag.WomanDay:
        image_path = random.choice(IMAGE_PATHS_8)

    return image_path