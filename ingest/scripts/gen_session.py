import os
from telethon import TelegramClient
from telethon.sessions import StringSession


def main() -> None:
    api_id = int(os.getenv("TELEGRAM_API_ID", "0"))
    api_hash = os.getenv("TELEGRAM_API_HASH", "")
    session_path = os.getenv("TELEGRAM_SESSION_PATH", ".telegram/crypto_userbot.session")

    os.makedirs(os.path.dirname(session_path), exist_ok=True)

    # Interactive login
    client = TelegramClient(session_path, api_id, api_hash)
    client.parse_mode = None
    client.start()
    print("Session created at:", session_path)


if __name__ == "__main__":
    main()

