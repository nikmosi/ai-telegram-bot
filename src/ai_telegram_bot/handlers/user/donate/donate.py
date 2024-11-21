from aiogram.filters.command import CommandObject
from aiogram.types import CallbackQuery, LabeledPrice, Message
from fluent.runtime import FluentLocalization
from loguru import Logger

from ai_telegram_bot.keyboards.donate import create as create_donate_kb


async def cmd_donate(
    message: Message,
    command: CommandObject,
    l10n: FluentLocalization,
    aiogram_logger: Logger,
) -> None:
    aiogram_logger.debug("donate")
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


async def on_donate_cancel(callback: CallbackQuery, l10n: FluentLocalization) -> None:
    await callback.answer(l10n.format_value("donate-cancel-payment"))
    message = callback.message
    if message is not None and isinstance(message, Message):
        await message.delete()
