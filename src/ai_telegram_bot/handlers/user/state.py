from aiogram.fsm.context import FSMContext
from aiogram.types import Message


async def cmd_state(message: Message, state: FSMContext) -> None:
    user_state = await state.get_state()
    await message.reply(f"{user_state=}")
