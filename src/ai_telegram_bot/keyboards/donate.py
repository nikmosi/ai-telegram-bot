from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create(amount: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text=f"Оплатить {amount} XTR", pay=True)
    kb.button(text="Отменить операцию", callback_data="cancel_donateion")
    kb.adjust(1)
    return kb.as_markup()
