from aiogram.types import Message

from ai_telegram_bot.handlers.user.taro import play
from ai_telegram_bot.services.gpt import Gpt, answer_on_text
from ai_telegram_bot.utils.gpt_provider import GptProvider


async def handle_message(message: Message, gpt_provider: GptProvider) -> None:
    if message.from_user is None or message.text is None:
        return

    user_id = message.from_user.id
    text = message.text
    gpt = gpt_provider.get(user_id)

    is_taro_request = await determine_taro_request(text, gpt)

    if is_taro_request:
        await play(message)
    else:
        response = await answer_on_text(text, gpt)
        await message.reply(response)


async def determine_taro_request(text: str, gpt: Gpt) -> bool:
    prompt = (
        f"Определи, является ли запрос '{text}' запросом к таро. Ответь 'Да' или 'Нет'."
    )
    response = await answer_on_text(prompt, gpt)

    return "Да" in response.strip()
