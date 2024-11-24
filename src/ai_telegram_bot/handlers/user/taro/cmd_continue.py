from aiogram.fsm.context import FSMContext

from ai_telegram_bot.states import user

from .taro import cmd_taro_end


async def cmd_continue(state: FSMContext, **kwargs) -> None:
    await state.set_state(user.UserTaro.play)
    await cmd_taro_end(**kwargs)
