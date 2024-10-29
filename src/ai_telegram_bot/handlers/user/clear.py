from aiogram.types import Message

from ai_telegram_bot.utils.gpt_provider import GptProvider


async def process_clear_command(message: Message, gpt_provider: GptProvider):
    if message.from_user is None:
        return
    gpt = gpt_provider.get(message.from_user.id)
    gpt.clear_history()
    await message.answer("История диалога очищена.")
