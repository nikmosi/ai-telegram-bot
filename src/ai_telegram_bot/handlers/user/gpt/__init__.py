from aiogram import F, Router
from aiogram.filters import StateFilter

from src.ai_telegram_bot.states import user

from . import text, voice


def prepare_router() -> Router:
    gpt_router = Router(name="gpt_router")
    gpt_router.message.filter(StateFilter(user.UserGpt.chat))

    gpt_router.message.register(text.handle_message, F.text)
    gpt_router.message.register(voice.handle_voice_message, F.voice)

    return gpt_router
