from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters.command import CommandObject
from aiogram.types import Message, PreCheckoutQuery
from fluent.runtime import FluentLocalization


async def pre_checkout_query(query: PreCheckoutQuery) -> None:
    await query.answer(ok=True)
    # TODO: cancel when balance < refunt amount


async def cmd_refund(
    message: Message, bot: Bot, command: CommandObject, l10n: FluentLocalization
) -> None:
    t_id = command.args
    from_user = message.from_user

    if t_id is None:
        await message.answer(l10n.format_value("donate-refund-input-error"))
        return

    if from_user is None:
        await message.answer(l10n.format_value("donate-refund-input-error"))
        return

    try:
        await bot.refund_star_payment(
            user_id=from_user.id, telegram_payment_charge_id=t_id
        )
        await message.answer(l10n.format_value("donate-refund-success"))

    except TelegramBadRequest as e:
        err_text = l10n.format_value("donate-refund-code-not-found")

        if "CHARGE_ALREADY_REFUNDED" in e.message:
            err_text = l10n.format_value("donate-refund-already-refunded")

        await message.answer(err_text)
        return
