Alerting, Threads, and Delivery

Threads
- Use a private forum group with topics for categories: Urgent, Interesting, Overview, Misc/Sol.
- Maintain category→topic_id mapping; default/fallback to main if missing.
 - Store topic IDs in DB (see `database.md`) so they can be created later and updated without code changes.

Formatting
- Concise alerts with markdown; include emojis for urgency; include token stats/safety if available.
- Avoid spam: aggregate near-duplicates; throttle Interesting; batch Overview via scheduler.
 - Weight repeated alerts lower: if the second post repeats the first within a short window, down-weight unless posted by a high‑rated caller or adds substantial detail.
 - No user mentions/pings by default.

Rate Control
- Sleep/batching to respect Telegram rate limits; flood-wait handling.


