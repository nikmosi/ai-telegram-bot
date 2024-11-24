from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from ai_telegram_bot.states import user


async def cmd_state(message: Message, state: FSMContext) -> None:
    user_state = await state.get_state()
    await message.reply(f"{user_state=}")


async def cmd_taro(message: Message, state: FSMContext) -> None:
    await state.set_state(user.UserGpt.taro)
    await message.reply("Вы перешли в режим таро)")


async def cmd_chat(message: Message, state: FSMContext) -> None:
    await state.set_state(user.UserGpt.chat)
    await message.reply("Вы перешли в режим чата)")
