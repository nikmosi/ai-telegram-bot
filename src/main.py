import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from loguru import logger

from ai_telegram_bot.data.config import Settings
from ai_telegram_bot.handlers.user import prepare_router as prepare_user_router
from ai_telegram_bot.middlewares.logging import LoggingMiddleware
from ai_telegram_bot.utils import gpt_provider
from ai_telegram_bot.utils.logging import setup_logger

settings = Settings()


def setup_logging(dispatcher: Dispatcher) -> None:
    dispatcher["aiogram_logger"] = setup_logger()


def setup_gpt_provider(dispatcher: Dispatcher) -> None:
    dispatcher["gpt_provider"] = gpt_provider.setup_gpt_provider()


async def setup_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(prepare_user_router())


def setup_middlewares(dispatcher: Dispatcher) -> None:
    dispatcher.update.outer_middleware(LoggingMiddleware())


async def setup_aiogram(dispatcher: Dispatcher) -> None:
    setup_logging(dispatcher)
    setup_gpt_provider(dispatcher)
    logger = dispatcher["aiogram_logger"]

    logger.debug("Configuring aiogram")
    await setup_handlers(dispatcher)
    setup_middlewares(dispatcher)
    logger.info("Configured aiogram")


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    await setup_aiogram(dispatcher)
    dispatcher["aiogram_logger"].info("Started polling")


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    dispatcher["aiogram_logger"].debug("Stopping polling")
    dispatcher["aiogram_logger"].info("Stopped polling")


async def main():
    dp = Dispatcher()
    bot = Bot(token=settings.token, default=DefaultBotProperties(parse_mode="HTML"))
    logger.add(
        "logs/telegram_bot.log",
        level="DEBUG",
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="100 KB",
        compression="zip",
    )
    dp.startup.register(aiogram_on_startup_polling)
    dp.shutdown.register(aiogram_on_shutdown_polling)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
