from aiogram.types import Message

from ai_telegram_bot.handlers.user.text import handle_message
from ai_telegram_bot.utils import convert_voice_to_text
from ai_telegram_bot.utils.gpt_provider import GptProvider


async def handle_voice_message(message: Message, gpt_provider: GptProvider):
    if message.from_user is None:
        return
    recognition_text = await convert_voice_to_text(message)
    message_with_text = message.copy(update={"text": recognition_text})
    await handle_message(message_with_text, gpt_provider)
