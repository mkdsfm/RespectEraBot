import json
import random
from gigachat import GigaChat
import os
from gigachat.models import Chat, Messages, MessagesRole

AI_AUTH_KEY = os.getenv("AI_AUTH_KEY")

# Загрузка настроек из config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

COMPLIMENTS = config.get("COMPLIMENTS", [])

PERSON_DESCRIPTIONS = config.get("PERSON_DESCRIPTIONS", {})
DEFAULT_NAME = "default"

giga = GigaChat(
   credentials=AI_AUTH_KEY,
   scope="GIGACHAT_API_PERS",
   model="GigaChat",
   ca_bundle_file="russian_trusted_root_ca.cer"
)

PROMPT = """Составь комплимент-респект в виде дифирамбов на основе следующего описания: {description}. 
Комплимент-респект должен быть в 4-5 предложений с разными эмоджи в контексте. Обращайся на ты."""

async def get_ai_response_async(username):
    """Отправляет комплимент, сгенерированный Гига-чат"""
    description = PERSON_DESCRIPTIONS.get(f"@{username}", PERSON_DESCRIPTIONS[DEFAULT_NAME])
    prompt = PROMPT.format(description=description)

    payload = Chat(
        messages=[
            Messages(
                role=MessagesRole.USER,
                content=prompt
            )
        ],
        temperature=0.7,
        max_tokens=150,
    )

    response = giga.chat(payload)
    return response.choices[0].message.content + " (c) ai"

async def get_random_compliment_async(first_name):
    return random.choice(COMPLIMENTS).format(first_name=first_name)


async def get_random_text_async(username, first_name):
    choice = random.choice([True, False])

    if f"@{username}" in PERSON_DESCRIPTIONS or choice:
        return await get_ai_response_async(username)
    else:
        return await get_random_compliment_async(first_name)