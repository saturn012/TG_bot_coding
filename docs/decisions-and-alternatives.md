Decisions and Alternatives

Userbot vs Bot API
- Decision: MVP uses Bot API where possible, plus userbot later for private groups.
- Alternative: Only userbot (maximum access) — higher ops risk and ToS gray area.

Scoring Strategy
- Decision: Heuristics + optional gated AI; batch AI summaries.
- Alternative: Full realtime AI on every message — higher cost/latency.

Data Source Mix
- Decision: Dexscreener/GeckoTerminal + CoinGecko; Honeypot.is; Etherscan/GoPlus; cache aggressively.
- Alternative: On-chain nodes/subgraphs only — higher complexity/cost to maintain.

Storage
- Decision: Postgres (Supabase) primary; Redis optional for counters.
- Alternative: NoSQL only — simpler early, harder for analytics/ranking queries.

Delivery
- Decision: Telegram forum threads per category.
- Alternative: Separate chats or inline keyboards via official bot for control UI.

AI cadence
- Decision: Start with batch AI on adjustable schedule; realtime AI only if proven necessary.
- Alternative: Always-on realtime AI — higher cost and latency.


