from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from redis.asyncio import Redis

from ai_telegram_bot.states import user
from ai_telegram_bot.utils import convert_voice_to_text

from .taro import cmd_taro_end


async def handle_message(
    message: Message, redis: Redis, state: FSMContext, **kwargs
) -> None:
    if message.from_user is None or message.text is None:
        return

    user_id = message.from_user.id
    redis.set(f"taro_{user_id}", message.text)
    await state.set_state(user.UserTaro.play)
    await cmd_taro_end(message, redis, **kwargs)


async def handle_voice_message(message: Message, **kwargs) -> None:
    if message.from_user is None:
        return
    answer = await message.reply("Распознаю...")
    recognition_text = await convert_voice_to_text(message)
    message_with_text = message.model_copy(update={"text": recognition_text})
    await answer.edit_text(f"{recognition_text=}")
    await handle_message(message_with_text, **kwargs)
