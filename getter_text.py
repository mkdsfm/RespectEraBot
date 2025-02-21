import json
import random
from gigachat import GigaChat
import os

# Загрузка настроек из config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

COMPLIMENTS = config.get("COMPLIMENTS", [])

PERSON_DESCRIPTIONS = config.get("PERSON_DESCRIPTIONS", {})
DEFAULT_NAME = "default"

AI_AUTH_KEY = os.getenv("AI_AUTH_KEY")

giga = GigaChat(
   credentials=AI_AUTH_KEY,
   scope="GIGACHAT_API_PERS",
   model="GigaChat",
   ca_bundle_file="russian_trusted_root_ca.cer"
)

PROMPT = """Составь комплимент-респект в виде дифирамбов для {first_name} на основе следующего описания: {description}. 
Комплимент-респект должен быть подчеркивающим профессионализм в несколько предложений. Обращайся на ты."""

async def get_ai_response(username, first_name):
    """Отправляет комплимент, сгенерированный Гига-чат"""
    description = PERSON_DESCRIPTIONS.get(f"@{username}", PERSON_DESCRIPTIONS[DEFAULT_NAME])
    prompt = PROMPT.format(first_name=first_name, description=description)

    response = giga.chat(prompt)
    return response.choices[0].message.content + " (c) ai"

async def get_random_compliment(first_name):
    return random.choice(COMPLIMENTS).format(first_name=first_name)