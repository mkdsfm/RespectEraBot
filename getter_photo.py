import os
import random

IMAGE_DIR = "images"
IMAGE_PATHS = [os.path.join(IMAGE_DIR, file) for file in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, file))]

async def get_random_photo_async():
    # gigachad_photo = await getter_gigachad.get_gigachad_photo(bot, message.from_user.id)
    # if gigachad_photo:
    #     await message.answer_photo(photo=types.FSInputFile(gigachad_photo), caption=compliment)
    image_path = random.choice(IMAGE_PATHS)
    return image_path