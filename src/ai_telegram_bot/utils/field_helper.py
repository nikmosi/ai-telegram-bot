from aiogram.client.bot import Bot
from aiogram.types import Message

from ai_telegram_bot.exceptions import CantGetFieldException


def get_file_id(message: Message) -> str:
    voice = message.voice
    if voice is None:
        raise CantGetFieldException(field_name=f"{message.voice=}")
    return voice.file_id


def get_bot(message: Message) -> Bot:
    bot = message.bot
    if bot is None:
        raise CantGetFieldException(field_name=f"{message.bot=}")
    return bot
