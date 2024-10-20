import asyncio

from aiogram import Bot, Dispatcher

from ai_telegram_bot.config import Settings
from ai_telegram_bot.TelegramBotAI import main_route

dp = Dispatcher()
settings = Settings()


async def main():
    bot = Bot(token=settings.token)
    dp.include_router(main_route)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
