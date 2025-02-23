from gtts import gTTS
import os

def get_audio(text, filename):
    tts = gTTS(text=text, lang='ru')
    tts.save(filename)
    return filename