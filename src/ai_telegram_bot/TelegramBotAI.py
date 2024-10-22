from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from collections import defaultdict
import g4f
from aiogram import F, Router, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from g4f import Provider
import speech_recognition as sr
import ffmpeg
import os
import logging
from ai_telegram_bot.config import Settings

main_route = Router()
conversation_history = defaultdict(list)
settings = Settings()

def convert_audio(input_path: str, output_format: str = 'wav') -> str:
    output_path = f"voice_converted.{output_format}"

    # Используем ffmpeg для конвертации
    ffmpeg.input(input_path).output(output_path).run(overwrite_output=True)

    return output_path

def recognize_audio(file_path: str) -> dict:
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language='ru-RU')
        return {'text': text, 'error': None}
    except sr.UnknownValueError:
        return {'text': None, 'error': 'Не удалось распознать голос.'}
    except sr.RequestError:
        return {'text': None, 'error': 'Ошибка сервиса распознавания.'}
    except Exception as e:
        return {'text': None, 'error': str(e)}

def trim_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history

@main_route.message(Command("clear"))
async def process_clear_command(message: Message):
    user = message.from_user
    if not user:
        return
    user_id = user.id
    conversation_history[user_id] = []
    await message.answer("История диалога очищена.")

@main_route.message(F.text)
async def handle_text_message(message: Message):
    user = message.from_user
    if not user:
        return
    user_id = user.id
    user_input = message.text

    conversation_history[user_id].append({"role": "user", "content": user_input})
    conversation_history[user_id] = trim_history(conversation_history[user_id])

    chat_history = conversation_history[user_id]
    using_provider = settings.provider

    try:
        chat_gpt_response = await g4f.ChatCompletion.create_async(
            messages=chat_history,
            model=settings.model,
            provider=using_provider,
            proxy=settings.proxy,
            api_key=settings.api_key,
        )
    except Exception as e:
        chat_gpt_response = "Извините, произошла ошибка."

    conversation_history[user_id].append(
        {"role": "assistant", "content": chat_gpt_response}
    )
    await message.answer(chat_gpt_response)

@main_route.message(F.voice)
async def handle_voice_message(message: Message):
    user = message.from_user
    if not user:
        return
    user_id = user.id

    voice = message.voice
    file_id = voice.file_id
    file = await message.bot.get_file(file_id)
    await message.bot.download_file(file.file_path, 'voice.ogg')

    # Конвертируем аудио из OGG в WAV
    converted_file = convert_audio('voice.ogg')

    # Распознаем текст из аудио
    result = recognize_audio(converted_file)

    if result.get('error'):
        await message.answer(result['error'])
        return

    user_input = result['text']

    # Добавляем распознанный текст в историю общения

    conversation_history[user_id].append({"role": "user", "content": user_input})
    conversation_history[user_id] = trim_history(conversation_history[user_id])

    chat_history = conversation_history[user_id]
    using_provider = Provider.ChatGptEs

    try:
        chat_gpt_response = await g4f.ChatCompletion.create_async(
            model="gpt-4o",  # Учтите, что модель должна быть корректна
            messages=chat_history,
            provider=using_provider,
            proxy=settings.proxy,
        )
    except Exception as e:
        chat_gpt_response = "Извините, произошла ошибка."

    conversation_history[user_id].append(
        {"role": "assistant", "content": chat_gpt_response}
    )
    await message.answer(chat_gpt_response)