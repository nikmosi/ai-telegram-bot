from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters.command import CommandObject
from aiogram.types import CallbackQuery, LabeledPrice, Message, PreCheckoutQuery
from fluent.runtime import FluentLocalization

from ai_telegram_bot.keyboards.donate import create as create_donate_kb


async def cmd_donate(
    message: Message, command: CommandObject, l10n: FluentLocalization
) -> None:
    if (
        command.args is None
        or not command.args.isdigit()
        or not 1 <= int(command.args) <= 2500
    ):
        await message.answer(l10n.format_value("donate-input-error"))
        return

    amount = int(command.args)

    kb = create_donate_kb(amount)
    prices = [LabeledPrice(label="XTR", amount=amount)]

    await message.answer_invoice(
        title=l10n.format_value("donate-invoice-title"),
        description=l10n.format_value("donate-invoice-description", {"amount": amount}),
        prices=prices,
        provider_token="",
        payload=f"{amount}_stars",
        currency="XTR",
        reply_markup=kb,
    )


async def on_donate_cancel(callback: CallbackQuery, l10n: FluentLocalization) -> None:
    await callback.answer(l10n.format_value("donate-cancel-payment"))
    message = callback.message
    if message is not None and isinstance(message, Message):
        await message.delete()


async def cmd_paysupport(message: Message, l10n: FluentLocalization) -> None:
    await message.answer(l10n.format_value("donate-paysupport-message"))


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


async def pre_checkout_query(query: PreCheckoutQuery) -> None:
    await query.answer(ok=True)
    # TODO: cancel when balance < refunt amount


async def on_successfull_payment(message: Message, l10n: FluentLocalization) -> None:
    payment = message.successful_payment
    if payment is None:
        await message.answer(l10n.format_value("payment-none-error"))
        return
    await message.answer(
        l10n.format_value(
            "donate-successful-payment",
            {"t_id": payment.telegram_payment_charge_id},
        ),
        message_effect_id="5159385139981059251",
    )
