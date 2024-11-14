from random import sample

from aiogram.types import Message

from ai_telegram_bot.data.constants import tarot_deck


async def play(message: Message) -> None:
    past, present, future = sample(tarot_deck, 3)
    await message.reply(
        "\n".join([f"Прошлое: {past}", f"Настоящее: {present}", f"Будущее: {future}"])
    )
