import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from ai_telegram_bot.data import settings
from ai_telegram_bot.handlers.user import prepare_router as prepare_user_router
from ai_telegram_bot.middlewares import (
    L10nMiddleware,
    LoggingMiddleware,
    SessionMiddleware,
)
from ai_telegram_bot.utils import cache, gpt_provider
from ai_telegram_bot.utils.fluent import get_fluent_localization
from ai_telegram_bot.utils.logging import setup_logger


def setup_logging(dispatcher: Dispatcher) -> None:
    dispatcher["aiogram_logger"] = setup_logger()


def setup_gpt_provider(dispatcher: Dispatcher) -> None:
    dispatcher["gpt_provider"] = gpt_provider.setup_gpt_provider()


def setup_redis_cache(dispatcher: Dispatcher) -> None:
    dispatcher["redis"] = cache.setup_redis_cache()


async def setup_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(prepare_user_router())


def setup_middlewares(dispatcher: Dispatcher) -> None:
    dispatcher.update.outer_middleware(LoggingMiddleware())
    dispatcher.update.outer_middleware(L10nMiddleware(get_fluent_localization()))
    dispatcher.update.outer_middleware(SessionMiddleware())


async def setup_aiogram(dispatcher: Dispatcher) -> None:
    setup_logging(dispatcher)
    setup_gpt_provider(dispatcher)
    setup_redis_cache(dispatcher)
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


async def main() -> None:
    redis = cache.setup_redis_storage()
    dp = Dispatcher(storage=redis)
    bot = Bot(token=settings.token, default=DefaultBotProperties(parse_mode="HTML"))
    dp.startup.register(aiogram_on_startup_polling)
    dp.shutdown.register(aiogram_on_shutdown_polling)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
