from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter

from ai_telegram_bot import states
from ai_telegram_bot.filters import ChatTypeFilter, TextFilter

from . import clear, start, taro, text, voice
from .donate import prepare_router as prepare_donate_router


def prepare_router() -> Router:
    user_router = Router(name="user_router")
    user_router.message.filter(ChatTypeFilter("private"))

    user_router.message.register(start.start, CommandStart())
    user_router.message.register(
        start.start,
        TextFilter("🏠В главное меню"),
        StateFilter(states.user.UserMainMenu.menu),
    )

    gpt_router = Router(name="gpt_router")

    gpt_router.message.register(taro.play, Command("taro"))
    gpt_router.message.register(clear.process_clear_command, Command("clear"))
    gpt_router.message.register(text.handle_message, F.text)
    gpt_router.message.register(voice.handle_voice_message, F.voice)

    user_router.include_router(prepare_donate_router())
    user_router.include_router(gpt_router)

    return user_router
