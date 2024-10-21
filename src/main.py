import asyncio

from aiogram import Bot, Dispatcher

from ai_telegram_bot.config import Settings
from ai_telegram_bot.TelegramBotAI import main_route

dp = Dispatcher()
settings = Settings()


async def main():
    print("start main")
    print(f"proxy: {settings.proxy}")
    bot = Bot(token=settings.token)
    dp.startup.register(lambda: print("bot startup"))
    dp.shutdown.register(lambda: print("bot shutdown"))
    dp.include_router(main_route)
    await dp.start_polling(bot)
    print("end main")


if __name__ == "__main__":
    asyncio.run(main())