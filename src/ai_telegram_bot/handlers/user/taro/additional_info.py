from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from redis.asyncio import Redis

from ai_telegram_bot.handlers.shared.voice import extract_text_from_voice
from ai_telegram_bot.states import user
from ai_telegram_bot.utils.gpt_provider import GptProvider

from .taro import cmd_taro_end


async def handle_message(
    message: Message, redis: Redis, state: FSMContext, gpt_provider: GptProvider
) -> None:
    if message.from_user is None or message.text is None:
        return

    user_id = message.from_user.id
    await redis.set(f"taro_{user_id}", message.text)
    await state.set_state(user.UserTaro.play)
    await cmd_taro_end(message, redis, state, gpt_provider)


async def handle_voice_message(
    message: Message, redis: Redis, state: FSMContext, gpt_provider: GptProvider
) -> None:
    message_with_text = await extract_text_from_voice(message)
    await handle_message(message_with_text, redis, state, gpt_provider)
