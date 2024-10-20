import asyncio
import logging

import g4f
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import Settings
from g4f import Provider

logging.basicConfig(level=logging.INFO)

settings = Settings()
bot = Bot(token=settings.token)
dp = Dispatcher()


ADMIN_ID = settings.admin_id


conversation_history = {}


def trim_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history


@dp.message(Command("clear"))
async def process_clear_command(message: Message):
    user = message.from_user
    if user is None:
        logging.info("from_user is None")
        return
    user_id = user.id
    conversation_history[user_id] = []
    await message.answer("История диалога очищена.")


@dp.message(F.text)
async def handle_message(message: Message):
    user = message.from_user
    if user is None:
        logging.info("from_user is None")
        return
    user_id = user.id
    user_input = message.text

    if user_id not in conversation_history:
        conversation_history[user_id] = []

    conversation_history[user_id].append({"role": "user", "content": user_input})
    conversation_history[user_id] = trim_history(conversation_history[user_id])

    chat_history = conversation_history[user_id]

    using_provider = Provider.Bing
    try:
        response = await g4f.ChatCompletion.create_async(
            model="gpt-4",
            messages=chat_history,
            provider=using_provider,
        )
        chat_gpt_response = response
    except Exception as e:
        print(f"{using_provider.__name__}:", e)
        chat_gpt_response = "Извините, произошла ошибка."

    conversation_history[user_id].append(
        {"role": "assistant", "content": chat_gpt_response}
    )
    await message.answer(chat_gpt_response)

    admin_message = f"Пользователь @{user.username} (ID: {user_id}) отправил сообщение:\n\n{user_input}"
    await bot.send_message(chat_id=ADMIN_ID, text=admin_message)


async def on_startup(dispatcher):
    logging.info("Бот запущен и готов к работе.")


async def on_shutdown(dispatcher):
    logging.info("Бот остановлен.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
