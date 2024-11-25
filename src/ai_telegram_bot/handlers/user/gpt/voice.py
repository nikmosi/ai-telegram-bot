from aiogram.types import Message

from ai_telegram_bot.handlers.shared import extract_text_from_voice
from ai_telegram_bot.utils.gpt_provider import GptProvider

from .text import handle_message


async def handle_voice_message(message: Message, gpt_provider: GptProvider) -> None:
    message_with_text = await extract_text_from_voice(message)
    await handle_message(message_with_text, gpt_provider)
