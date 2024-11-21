from asyncio import TaskGroup

from aiogram.types import Message

from ai_telegram_bot.handlers.user.taro import play
from ai_telegram_bot.services.gpt import answer_on_text, determine_taro_request
from ai_telegram_bot.utils.gpt_provider import GptProvider


async def handle_message(message: Message, gpt_provider: GptProvider) -> None:
    if message.from_user is None or message.text is None:
        return

    user_id = message.from_user.id
    text = message.text
    gpt = gpt_provider.get(user_id)
    taro = gpt_provider.get_taro_gpt(user_id)

    async with TaskGroup() as tg:
        taro_task = tg.create_task(determine_taro_request(text, taro))
        gpt_task = tg.create_task(answer_on_text(text, gpt))

    is_taro_request = await taro_task
    response = await gpt_task

    if "да" in is_taro_request:
        await play(message)
    else:
        await message.reply(response)
