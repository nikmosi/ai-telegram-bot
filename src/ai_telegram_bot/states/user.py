from aiogram.fsm.state import State, StatesGroup


class UserMainMenu(StatesGroup):
    menu = State()


class UserGpt(StatesGroup):
    taro = State()
    chat = State()


class UserTaro(StatesGroup):
    play = State()
    wait_info = State()
