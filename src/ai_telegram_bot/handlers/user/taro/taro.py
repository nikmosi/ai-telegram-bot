from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from redis.asyncio import Redis

from ai_telegram_bot.services.gpt import answer_on_text
from ai_telegram_bot.services.taro import get_prediction
from ai_telegram_bot.states import user
from ai_telegram_bot.utils.gpt_provider import GptProvider


async def cmd_taro(message: Message, state: FSMContext) -> None:
    await message.reply(
        "\n".join(
            [
                "Начинаю мешать колоду",
                "Вы можете рассказать дополнительную инфромацию для трактовки.",
                "Либо введите /continue, чтобы получить расклад.",
            ]
        )
    )
    await state.set_state(user.UserTaro.wait_info)


async def cmd_taro_end(
    message: Message, redis: Redis, state: FSMContext, gpt_provider: GptProvider
) -> None:
    if not message.from_user:
        return
    user_id = message.from_user.id
    additional_info = (await redis.get(f"taro_{user_id}")).decode()
    taro_gpt = gpt_provider.get_taro_gpt(user_id)
    promt = ""

    prediction = get_prediction()
    promt += f"# предсказание таро: \n{prediction}\n\n"
    if additional_info:
        promt += f"# допольнительная информация от пользователя\n {additional_info}\n"
        gpt_answer = await answer_on_text(promt, taro_gpt)
        await message.answer(f"{prediction}\n\n{gpt_answer}")
    else:
        await message.answer(prediction)
    await state.set_state(user.UserGpt.taro)
