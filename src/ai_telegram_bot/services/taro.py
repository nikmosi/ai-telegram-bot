from random import sample

from ai_telegram_bot.data.constants import tarot_deck


def get_prediction() -> str:
    past, present, future = sample(tarot_deck, 3)
    return "\n".join(
        [f"Прошлое: {past}", f"Настоящее: {present}", f"Будущее: {future}"]
    )
