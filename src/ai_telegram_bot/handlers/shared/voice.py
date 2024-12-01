from aiogram.types import Message

from ai_telegram_bot.exceptions.exceptions import CantGetFieldException
from ai_telegram_bot.utils import convert_voice_to_text


async def extract_text_from_voice(message: Message) -> Message:
    if message.from_user is None:
        raise CantGetFieldException(field_name="message.from_user")
    answer = await message.reply("Распознаю...")
    recognition_text = await convert_voice_to_text(message)
    message_with_text = message.model_copy(update={"text": recognition_text})
    await answer.edit_text(f"{recognition_text=}")
    return message_with_text
