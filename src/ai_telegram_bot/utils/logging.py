from __future__ import annotations

import loguru
from loguru import logger


def setup_logger() -> loguru.Logger:
    logger.add(
        "logs/telegram_bot.log",
        level="DEBUG",
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="100 KB",
        compression="zip",
    )
    return logger
