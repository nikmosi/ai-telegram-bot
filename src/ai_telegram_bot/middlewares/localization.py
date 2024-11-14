from collections.abc import Awaitable, Callable
from typing import Any, override

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from fluent.runtime import FluentLocalization


# Inner-middleware for message
class L10nMiddleware(BaseMiddleware):
    def __init__(self, locale: FluentLocalization):
        self.locale = locale

    @override
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        data["l10n"] = self.locale
        return await handler(event, data)
