from collections.abc import Awaitable, Callable
from typing import Any, override

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from ai_telegram_bot.models import db_helper


class CounterMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    @override
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async with db_helper.session() as session:
            data["db_session"] = session
            return await handler(event, data)
