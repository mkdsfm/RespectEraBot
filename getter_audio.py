from gtts import gTTS
import os

def get_audio(text):
    tts = gTTS(text=text, lang='ru')
    filename = 'output.mp3'
    tts.save(filename)
    return filename