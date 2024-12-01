from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter

from ai_telegram_bot.filters import ChatTypeFilter, TextFilter
from ai_telegram_bot.states import user

from . import clear, start, state
from .donate import prepare_router as prepare_donate_router
from .gpt import prepare_router as prepare_gpt_router
from .taro import prepare_router as prepare_taro_router


def prepare_router() -> Router:
    user_router = Router(name="user_router")
    user_router.message.filter(ChatTypeFilter("private"))

    user_router.message.register(start.start, CommandStart())
    user_router.message.register(
        start.start,
        TextFilter("🏠В главное меню"),
        StateFilter(user.UserMainMenu.menu),
    )

    user_router.message.register(state.cmd_state, Command("state"))
    user_router.message.register(state.cmd_chat, Command("chat"))
    user_router.message.register(state.cmd_taro, Command("taro"))
    user_router.message.register(clear.process_clear_command, Command("clear"))

    user_router.include_router(prepare_donate_router())
    user_router.include_router(prepare_gpt_router())
    user_router.include_router(prepare_taro_router())

    return user_router
