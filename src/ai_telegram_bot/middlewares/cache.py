from collections.abc import Awaitable, Callable
from typing import Any, override

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from ai_telegram_bot.utils.cache import setup_redis_cache


class CacheMiddleware(BaseMiddleware):
    @override
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async with setup_redis_cache() as redis:
            data["redis"] = redis
            return await handler(event, data)
