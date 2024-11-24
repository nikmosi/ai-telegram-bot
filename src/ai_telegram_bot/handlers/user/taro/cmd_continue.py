from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from redis.asyncio import Redis

from ai_telegram_bot.states import user
from ai_telegram_bot.utils.gpt_provider import GptProvider

from .taro import cmd_taro_end


async def cmd_continue(
    message: Message, redis: Redis, state: FSMContext, gpt_provider: GptProvider
) -> None:
    await state.set_state(user.UserTaro.play)
    await cmd_taro_end(message, redis, state, gpt_provider)
