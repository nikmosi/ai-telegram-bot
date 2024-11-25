from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import ConnectionPool, Redis

from ai_telegram_bot.data import settings


def setup_redis(db: int) -> Redis:
    rc = settings.redis

    return Redis(
        connection_pool=ConnectionPool.from_url(
            f"redis://{rc.username}:{rc.password}@{rc.host}:{rc.port}/{db}"
        )
    )


def setup_redis_storage() -> RedisStorage:
    redis = setup_redis(settings.redis.db_storage)
    return RedisStorage(redis)


@asynccontextmanager
async def setup_redis_cache() -> AsyncGenerator[Redis, None]:
    redis = setup_redis(settings.redis.db_cache)
    try:
        yield redis
    finally:
        await redis.close()
