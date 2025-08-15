import asyncio
import os
from dataclasses import dataclass
from typing import List, Set

from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import FloodWaitError
from ingest.db import ensure_schema, connect
from ingest.commands import register_command_handlers


@dataclass(frozen=True)
class Settings:
    api_id: int
    api_hash: str
    session_path: str
    allow_chat_ids: Set[int]


def load_settings() -> Settings:
    api_id = int(os.getenv("TELEGRAM_API_ID", "0"))
    api_hash = os.getenv("TELEGRAM_API_HASH", "")
    session_path = os.getenv("TELEGRAM_SESSION_PATH", ".telegram/crypto_userbot.session")
    allow_raw = os.getenv("ALLOW_CHAT_IDS", "")
    allow_chat_ids = {int(x.strip()) for x in allow_raw.split(",") if x.strip()}
    return Settings(api_id=api_id, api_hash=api_hash, session_path=session_path, allow_chat_ids=allow_chat_ids)


async def main() -> None:
    settings = load_settings()
    os.makedirs(os.path.dirname(settings.session_path), exist_ok=True)

    # DB schema
    await ensure_schema()

    client = TelegramClient(settings.session_path, settings.api_id, settings.api_hash)
    await client.start()
    me = await client.get_me()
    print(f"Userbot connected as: {me.username or me.id}")

    if settings.allow_chat_ids:
        print(f"Allow-list enabled: {len(settings.allow_chat_ids)} chats")

    @client.on(events.NewMessage())
    async def handler(event):
        try:
            chat_id = event.chat_id
            if settings.allow_chat_ids and chat_id not in settings.allow_chat_ids:
                return

            msg = event.message
            text = msg.message or ""
            # persist basic message row
            conn = await connect()
            try:
                await conn.execute(
                    """
                    INSERT INTO messages(chat_id, message_id, sender_id, text, timestamp)
                    VALUES($1,$2,$3,$4,$5)
                    ON CONFLICT DO NOTHING
                    """,
                    chat_id,
                    msg.id,
                    int(getattr(msg, 'sender_id', 0) or 0),
                    text,
                    msg.date,
                )
            finally:
                await conn.close()
            print(f"[{msg.date}] chat={chat_id} id={msg.id} saved")

        except FloodWaitError as fw:
            await asyncio.sleep(int(fw.seconds) + 1)
        except Exception as ex:
            print(f"Handler error: {ex}")

    print("Listening for new messages...")
    # register commands in the same client (control chat)
    register_command_handlers(client)
    await client.run_until_disconnected()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

