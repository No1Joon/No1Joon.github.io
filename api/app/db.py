import logging

from pymongo import ASCENDING, DESCENDING, AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from app.config import Settings

log = logging.getLogger(__name__)

_client: AsyncMongoClient | None = None


async def init_db(settings: Settings) -> AsyncDatabase:
    global _client
    if not settings.mongo_uri:
        raise RuntimeError("MONGO_URI is not set")

    if _client is None:
        _client = AsyncMongoClient(
            settings.mongo_uri,
            maxPoolSize=settings.mongo_pool_size,
            serverSelectionTimeoutMS=5000,
            retryWrites=True,
        )
        await _client.admin.command("ping")
        log.info("MongoDB connected (db=%s, pool=%d)", settings.mongo_db, settings.mongo_pool_size)

    db = _client[settings.mongo_db]
    await ensure_indexes(db)
    return db


async def ensure_indexes(db: AsyncDatabase) -> None:
    await db.comments.create_index(
        [("post_slug", ASCENDING), ("status", ASCENDING), ("created_at", DESCENDING)],
        name="post_status_created",
    )
    await db.comments.create_index("status", name="status")
    await db.comments.create_index("ip_hash", name="ip_hash")


async def close_db() -> None:
    global _client
    if _client is not None:
        await _client.close()
        _client = None
