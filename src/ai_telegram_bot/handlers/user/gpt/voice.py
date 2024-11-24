from aiogram.types import Message

from ai_telegram_bot.utils import convert_voice_to_text
from ai_telegram_bot.utils.gpt_provider import GptProvider

from .text import handle_message


async def handle_voice_message(message: Message, gpt_provider: GptProvider) -> None:
    if message.from_user is None:
        return
    answer = await message.reply("Распознаю...")
    recognition_text = await convert_voice_to_text(message)
    message_with_text = message.model_copy(update={"text": recognition_text})
    await answer.edit_text(f"{recognition_text=}")
    await handle_message(message_with_text, gpt_provider)
