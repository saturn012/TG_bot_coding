Ingest service (Telethon)

Env vars (see docs/README.md)
- TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_SESSION_PATH
- BOT_TOKEN, OUTPUT_CHAT_ID, ALLOW_CHAT_IDS
- DATABASE_URL
- MIN_MCAP, MIN_LIQ, AI_INTERVAL_HOURS

Setup
- python -m venv .venv && source .venv/bin/activate
- pip install -r requirements.txt
- create .env with the keys above
- run: python scripts/gen_session.py (first login), then: python app.py

