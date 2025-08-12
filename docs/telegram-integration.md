Telegram Integration (Userbot/Bot)

Approach
- MVP collection via Bot API where allowed (public or bot-friendly groups).
- User account (Telethon/Pyrogram) for private groups; sessions encrypted at rest.

Notes
- Respect flood-wait and rate limits; implement backoff and batching.
- Configure allow-lists per source; deduplicate by {source_type, chat_id, message_id, hash(text)}.
- Output to private forum group with topics for categories; map category→topic_id.

Security
- Store `.session` encrypted (Fernet/age), key in ENV, file mode 600, separate system user, 2FA on the account; firewall + fail2ban.

MVP Flags
- features.ingestion.bot = on
- features.ingestion.user_secondary = off
- features.ingestion.user_primary = off

Later Phases
- Enable user_secondary for a second user account (read-only test), then user_primary for super-private chats.


