from collections import defaultdict

import g4f
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from g4f import Provider

from ai_telegram_bot.config import Settings

main_route = Router()
conversation_history = defaultdict(list)
settings = Settings()


def trim_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history


@main_route.message(Command("clear"))
async def process_clear_command(message: Message):
    user = message.from_user
    if user is None:
        print("from_user is None")
        return
    user_id = user.id
    conversation_history[user_id] = []
    await message.answer("История диалога очищена.")


@main_route.message(F.text)
async def handle_message(message: Message):
    user = message.from_user
    if user is None:
        print("from_user is None")
        return
    user_id = user.id
    user_input = message.text
    print(user_id)

    conversation_history[user_id].append({"role": "user", "content": user_input})
    conversation_history[user_id] = trim_history(conversation_history[user_id])

    chat_history = conversation_history[user_id]
    using_provider = Provider.Bing

    try:
        chat_gpt_response = await g4f.ChatCompletion.create_async(
            model=settings.model,
            messages=[chat_history[-1]],
            provider=using_provider,
            proxy=settings.proxy,
        )
    except Exception as e:
        print(f"{using_provider.__name__}:", e)
        chat_gpt_response = "Извините, произошла ошибка."

    conversation_history[user_id].append(
        {"role": "assistant", "content": chat_gpt_response}
    )
    await message.answer(chat_gpt_response)
