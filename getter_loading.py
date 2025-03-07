import os
import random
from enum import Enum

DIR_23 = "23_animations"
PATHS_23 = [os.path.join(DIR_23, file) for file in os.listdir(DIR_23) if os.path.isfile(os.path.join(DIR_23, file))]

DIR_8 = "8_animations"
PATHS_8 = [os.path.join(DIR_8, file) for file in os.listdir(DIR_8) if os.path.isfile(os.path.join(DIR_8, file))]

class LoadingTag(Enum):
    ManDay = 23
    WomanDay = 8

async def get_random_loading(tag = LoadingTag.ManDay):
    # gigachad_photo = await getter_gigachad.get_gigachad_photo(bot, message.from_user.id)
    # if gigachad_photo:
    #     await message.answer_photo(photo=types.FSInputFile(gigachad_photo), caption=compliment)
    if tag == LoadingTag.ManDay:
        path = random.choice(PATHS_23)
    if tag == LoadingTag.WomanDay:
        path = random.choice(PATHS_8)

    return path