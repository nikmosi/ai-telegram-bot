from aiogram.types import Message

from ai_telegram_bot.services.gpt import answer_on_text
from ai_telegram_bot.utils.gpt_provider import GptProvider


async def handle_message(message: Message, gpt_provider: GptProvider) -> None:
    if message.from_user is None or message.text is None:
        return

    user_id = message.from_user.id
    text = message.text
    gpt = gpt_provider.get(user_id)

    response = await answer_on_text(text, gpt)

    await message.reply(response)
