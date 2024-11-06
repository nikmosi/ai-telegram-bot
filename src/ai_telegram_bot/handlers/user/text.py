from aiogram.types import Message

from ai_telegram_bot.services.gpt import answer_on_text
from ai_telegram_bot.utils.gpt_provider import GptProvider


async def handle_message(message: Message, gpt_provider: GptProvider) -> None:
    if message.from_user is None:
        return
    if message.text is None:
        return
    gpt = gpt_provider.get(message.from_user.id)
    text = message.text
    response = await answer_on_text(text, gpt)
    await message.reply(response)
