from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter

from ai_telegram_bot import states
from ai_telegram_bot.filters import ChatTypeFilter, TextFilter

from . import clear, donate, start, taro, text, voice


def prepare_router() -> Router:
    user_router = Router(name="user_router")
    user_router.message.filter(ChatTypeFilter("private"))

    user_router.message.register(start.start, CommandStart())
    user_router.message.register(
        start.start,
        TextFilter("🏠В главное меню"),
        StateFilter(states.user.UserMainMenu.menu),
    )

    user_router.message.register(taro.play, Command("taro"))
    user_router.message.register(clear.process_clear_command, Command("clear"))
    user_router.message.register(text.handle_message, F.text)
    user_router.message.register(voice.handle_voice_message, F.voice)

    user_router.message.register(donate.cmd_donate, Command("donate"))
    user_router.message.register(donate.cmd_paysupport, Command("paysupport"))
    user_router.message.register(donate.cmd_refund, Command("refund"))
    user_router.pre_checkout_query.register(donate.pre_checkout_query)
    user_router.callback_query.register(
        donate.on_donate_cancel, F.data == "donate_cancel"
    )
    user_router.message.register(donate.on_successfull_payment, F.successful_payment)

    return user_router
