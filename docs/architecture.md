Architecture Overview

High-level system for analyzing Telegram crypto chats and delivering categorized alerts:

- Telegram Clients: User account client (Telethon/Pyrogram) and optional Bot API client for MVP collection/output.
- Processing Core: Async pipeline for spike detection, token parsing, caller identification, NLP scoring, and categorization.
- Alert Delivery: Posts to private forum group with threads per category (Urgent, Interesting, Overview, etc.).
- External Integrations: Market data, honeypot/safety checks, contract verification, DEX pricing/liquidity.
- Data Storage: SQL (e.g., Postgres/Supabase) for messages, alerts, ratings, config; optional Redis for counters.
- Scheduler & AI: Periodic jobs for batch AI summaries and late reclassification.
- Commands: Admin adjustments via chat (e.g., /spikesedit, /callers 30).
- Logging/Monitoring: Structured logs, retries, flood-wait handling.

Related:
- Telegram integration: ./telegram-integration.md
- Pipeline: ./pipeline.md
- External integrations: ./external-integrations.md
- Alerting: ./alerting.md
- Ratings: ./ratings.md
- AI delayed analysis: ./ai-delayed-analysis.md
- Database: ./database.md
- Configuration: ./configuration.md
- Logging/Monitoring: ./logging-monitoring.md
- Future/multi-user: ./future-multi-user.md
- Decisions and alternatives: ./decisions-and-alternatives.md


