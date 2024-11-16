from aiogram.types import Message
from fluent.runtime import FluentLocalization


async def cmd_paysupport(message: Message, l10n: FluentLocalization) -> None:
    await message.answer(l10n.format_value("donate-paysupport-message"))
