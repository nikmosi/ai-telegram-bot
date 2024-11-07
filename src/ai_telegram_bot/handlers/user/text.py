from aiogram.types import Message
from ai_telegram_bot.services.gpt import answer_on_text
from ai_telegram_bot.utils.gpt_provider import GptProvider
from ai_telegram_bot.handlers.user.taro import play


async def handle_message(message: Message, gpt_provider: GptProvider):
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


async def determine_taro_request(text: str, gpt) -> bool:
    prompt = f"Определи, является ли запрос '{text}' запросом к таро. Ответь 'Да' или 'Нет'."
    response = await gpt.ask(prompt)

    return "Да" in response.strip()

