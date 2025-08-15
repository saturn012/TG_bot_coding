import asyncio
import os
from typing import Any

import asyncpg


async def connect() -> asyncpg.Connection:
    dsn = os.getenv("DATABASE_URL")
    if not dsn:
        raise RuntimeError("DATABASE_URL is not set")
    return await asyncpg.connect(dsn)


async def ensure_schema() -> None:
    path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()
    conn = await connect()
    try:
        await conn.execute(sql)
    finally:
        await conn.close()


