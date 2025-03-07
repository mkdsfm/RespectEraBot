from gigachat import GigaChat
import os
from gigachat.models import Chat, Messages, MessagesRole

AI_AUTH_KEY = os.getenv("AI_AUTH_KEY")

giga = GigaChat(
   credentials=AI_AUTH_KEY,
   scope="GIGACHAT_API_PERS",
   model="GigaChat",
   ca_bundle_file="russian_trusted_root_ca.cer"
)

SYSTEM_PROMPT = """Ты создаёшь развернутые, искренние комплименты на основе входных данных.  
1. Во входных данных будет роль человка (в формате *роль*) и описание качеств.  
2. Обращайся по имени, делай комплимент персональным.  
3. Используй яркие эпитеты, метафоры и примеры из описания.  
4. Делай комплимент щедрым, вдохновляющим и развернутым.  
5. Обязательно добавляй эмоджи для выразительности. 😊  
6. Комплимент должен состоять менее чем из 1024 символов
Пример:  
Вход: *коллега*, Аня лучший руководитель, поддерживает команду.  
Ответ: Анна, ты — не просто руководитель, ты — настоящий лидер! 🌟 Твоя способность поддерживать и вдохновлять команду просто восхищает. 💖 С тобой каждый чувствует себя важным и ценным, а это дорогого стоит. 💪 Ты умеешь находить подход к каждому, мотивировать на новые свершения и заряжать энергией даже в самые сложные дни. 🚀 Твоя мудрость, доброта и профессионализм делают тебя незаменимой! 🌈 Спасибо за то, что ты есть у нас — с тобой мы можем горы свернуть! 😊 

Теперь твоя очередь! Создай запоминающийся комплимент. 😉"""

payload = Chat(
        messages=[
            Messages(
                role=MessagesRole.SYSTEM,
                content=SYSTEM_PROMPT
            )
        ],
        temperature=0.7
    )

async def get_ai_response_async(description):
    """Отправляет комплимент, сгенерированный Гига-чат"""

    if len(payload.messages) > 1:
        payload.messages.pop(1)  # Удаляем элемент с индексом 1

    payload.messages.append(
            Messages(
                role=MessagesRole.USER,
                content=description
            ))
    
    response = giga.chat(payload)
    return response.choices[0].message.content + " (c) ai"


async def get_random_text_async(description):

    return await get_ai_response_async(description)