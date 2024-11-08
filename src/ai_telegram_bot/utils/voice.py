from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from tempfile import NamedTemporaryFile
from typing import Any

from aiogram.types import Message

from ai_telegram_bot.exceptions import CantGetFieldException, RecognizeException
from ai_telegram_bot.utils.audio import convert_audio_format, recognize_audio
from ai_telegram_bot.utils.field_helper import get_bot, get_file_id


@asynccontextmanager
async def download_voice(message: Message) -> AsyncGenerator[str, Any]:
    file_id = get_file_id(message)
    bot = get_bot(message)
    file = await bot.get_file(file_id)
    if file.file_path is None:
        raise CantGetFieldException(field_name=f"{file.file_path=}")
    with NamedTemporaryFile(suffix=".ogg") as tmp_file:
        temp_path = tmp_file.name
        await bot.download_file(file.file_path, temp_path)
        yield temp_path


async def convert_voice_to_text(message: Message) -> str:
    async with download_voice(message) as voice:
        with convert_audio_format(voice) as converted_file:
            result = recognize_audio(converted_file)

            if err_text := result.get("error"):
                raise RecognizeException(result=err_text)
            text = result["text"]
            return text if text else ""
