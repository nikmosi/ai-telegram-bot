from aiogram.fsm.state import State, StatesGroup


class UserMainMenu(StatesGroup):
    menu = State()
    taro = State()
    chat = State()
