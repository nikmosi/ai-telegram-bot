import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from ai_telegram_bot.data.config import Settings
from ai_telegram_bot.TelegramBotAI import main_route

dp = Dispatcher()
settings = Settings()


@logger.catch
async def main():
    logger.info("start main")
    logger.info(f"proxy: {settings.proxy}")
    bot = Bot(token=settings.token)
    dp.startup.register(lambda: logger.info("bot startup"))
    dp.shutdown.register(lambda: logger.info("bot shutdown"))
    dp.include_router(main_route)
    await dp.start_polling(bot)
    logger.info("end main")


if __name__ == "__main__":
    asyncio.run(main())
