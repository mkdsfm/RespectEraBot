from enum import Enum
import random
from gtts import gTTS
from pydub import AudioSegment
import tempfile

import os

DIR_23 = "23_audio"
PATHS_23 = [os.path.join(DIR_23, file) for file in os.listdir(DIR_23) if os.path.isfile(os.path.join(DIR_23, file))]

DIR_8 = "8_audio"
PATHS_8 = [os.path.join(DIR_8, file) for file in os.listdir(DIR_8) if os.path.isfile(os.path.join(DIR_8, file))]

class AudioTag(Enum):
    ManDay = 23
    WomanDay = 8


def get_audio(text, filename, tag=AudioTag.ManDay):
    
    tts_path = get_tts_audio_path(text)

    audio_tts = AudioSegment.from_file(tts_path)
    audio_tts = audio_tts + 10
    tts_track_length = len(audio_tts)

    audio_back = get_back_audio(tts_track_length, tag)

    if len(audio_tts) > len(audio_back):
        audio_back = audio_back + AudioSegment.silent(duration=len(audio_tts) - len(audio_back))
    else:
        audio_tts = audio_tts + AudioSegment.silent(duration=len(audio_back) - len(audio_tts))

    mixed_audio = audio_tts.overlay(audio_back)

    # Экспортируем результат
    mixed_audio.export(filename, format="mp3")

    os.remove(tts_path)

    return filename

def get_back_audio(lenght_hight, tag = AudioTag.ManDay):
    if tag == AudioTag.ManDay:
        audio_background_path = random.choice(PATHS_23)
    if tag == AudioTag.WomanDay:
        audio_background_path = random.choice(PATHS_8)

    audio_back = AudioSegment.from_file(audio_background_path)
    audio_back = audio_back - 10

    # Разделяем первую дорожку на две части:
    # 1. Часть до окончания второй дорожки
    # 2. Часть после окончания второй дорожки
    part1_back = audio_back[:lenght_hight]  # Первая часть (до окончания второй дорожки)
    part2_back = audio_back[lenght_hight:]  # Вторая часть (после окончания второй дорожки)
    part2_back = part2_back.fade_in(1000)  # Плавное увеличение громкости в течение 1 секунды (1000 мс)
    part2_back = part2_back + 10 

    audio_back_final = part1_back + part2_back

    return audio_back_final


def get_tts_audio_path(text):
    tts_path = tempfile.mktemp(suffix=".mp3")

    tts = gTTS(text=text, lang='ru')
    tts.save(tts_path)

    return tts_path