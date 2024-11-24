from aiogram import F, Router
from aiogram.filters import Command, StateFilter

from src.ai_telegram_bot.states import user

from .additional_info import handle_message, handle_voice_message
from .cmd_continue import cmd_continue
from .taro import cmd_taro


def prepare_router() -> Router:
    taro_router = Router(name="user_router")
    taro_router.message.filter(StateFilter(user.UserGpt.taro, user.UserTaro))

    taro_router.message.register(cmd_taro, Command("play"))

    taro_router.message.register(
        handle_message, StateFilter(user.UserTaro.wait_info), F.text
    )
    taro_router.message.register(
        handle_voice_message, StateFilter(user.UserTaro.wait_info), F.voice
    )

    taro_router.message.register(
        cmd_continue, StateFilter(user.UserTaro.wait_info), Command("continue")
    )

    return taro_router
