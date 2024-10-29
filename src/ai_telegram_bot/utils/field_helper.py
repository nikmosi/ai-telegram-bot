from aiogram.types import Message

from ai_telegram_bot.exceptions import CantGetFieldException


def get_file_id(message: Message):
    voice = message.voice
    if voice is None:
        raise CantGetFieldException(field_name=f"{message.voice=}")
    return voice.file_id


def get_bot(message: Message):
    bot = message.bot
    if bot is None:
        raise CantGetFieldException(field_name=f"{message.bot=}")
    return bot
