from aiogram import F, Router
from aiogram.filters import Command

from ai_telegram_bot.filters import ChatTypeFilter

from .donate import cmd_donate, on_donate_cancel, on_successfull_payment
from .paysupport import cmd_paysupport
from .refund import cmd_refund, pre_checkout_query


def prepare_router() -> Router:
    donate_router = Router(name="donate_router")
    donate_router.message.filter(ChatTypeFilter("private"))

    donate_router.message.register(cmd_donate, Command("donate"))
    donate_router.message.register(cmd_paysupport, Command("paysupport"))
    donate_router.message.register(cmd_refund, Command("refund"))
    donate_router.pre_checkout_query.register(pre_checkout_query)
    donate_router.callback_query.register(
        on_donate_cancel, F.data == "cancel_donateion"
    )
    donate_router.message.register(on_successfull_payment, F.successful_payment)

    return donate_router
