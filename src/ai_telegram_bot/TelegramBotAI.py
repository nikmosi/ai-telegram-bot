from collections import defaultdict
from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
from tempfile import NamedTemporaryFile
from typing import Any

import ffmpeg
import speech_recognition as sr
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from gpt import Gpt, GptArgs

from ai_telegram_bot.config import Settings

main_route = Router()
settings = Settings()
gpts = defaultdict(
    lambda: Gpt(
        GptArgs(
            model=settings.model,
            provider=settings.provider,
            proxy=settings.proxy,
            api_key=settings.api_key,
        )
    )
)


@contextmanager
def convert_audio_format(
    input_path: str, output_format: str = "wav"
) -> Generator[str, Any]:
    with NamedTemporaryFile(suffix=output_format) as tmp_file:
        output_path = tmp_file.name
        ffmpeg.input(input_path).output(output_path).run(overwrite_output=False)
        yield output_path


def recognize_audio(file_path: str) -> dict:
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="ru-RU")
        return {"text": text, "error": None}
    except sr.UnknownValueError:
        return {"text": None, "error": "Не удалось распознать голос."}
    except sr.RequestError:
        return {"text": None, "error": "Ошибка сервиса распознавания."}
    except Exception as e:
        return {"text": None, "error": str(e)}


def get_user_id(message: Message) -> int:
    user = message.from_user
    if user is None:
        raise Exception("from_user is None")
    return user.id


def get_user_text(message: Message) -> str:
    text = message.text
    if text is None:
        raise Exception("text is None")
    return text


def get_file_id(message: Message):
    voice = message.voice
    if voice is None:
        raise Exception("voice is None")
    return voice.file_id


def get_bot(message: Message):
    bot = message.bot
    if bot is None:
        raise Exception("bot is None")
    return bot


def trim_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history


@main_route.message(Command("clear"))
async def process_clear_command(message: Message):
    user_id = get_user_id(message)
    gpts.pop(user_id)
    await message.answer("История диалога очищена.")


@main_route.message(F.text)
async def handle_message(message: Message):
    user_id = get_user_id(message)
    user_text = get_user_text(message)
    gpt = gpts[user_id]

    try:
        response = await gpt.ask(user_text)
    except Exception:
        response = "Извините, произошла ошибка."
    await message.answer(response)


@asynccontextmanager
async def download_voice(message: Message) -> AsyncGenerator[str, Any]:
    file_id = get_file_id(message)
    bot = get_bot(message)
    file = await bot.get_file(file_id)
    if file.file_path is None:
        raise Exception("file_path is None")
    with NamedTemporaryFile(suffix=".ogg") as tmp_file:
        temp_path = tmp_file.name
        await bot.download_file(file.file_path, temp_path)
        yield temp_path


def convert_voice_to_text(voice: str) -> str:
    with convert_audio_format(voice) as converted_file:
        result = recognize_audio(converted_file)

        if result.get("error"):
            raise Exception(result.get("error"))
        return result["text"]


@main_route.message(F.voice)
async def handle_voice_message(message: Message):
    user_id = get_user_id(message)
    gpt = gpts[user_id]
    async with download_voice(message) as voice:
        text = convert_voice_to_text(voice)

        try:
            response = await gpt.ask(text)
        except Exception:
            response = "Извините, произошла ошибка."
        await message.answer(response)
