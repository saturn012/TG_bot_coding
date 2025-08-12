Future: Multi-user and Subscriptions

Model
- One userbot session per user for private chats; strong isolation (process/container) and encrypted sessions.
- DB partitioning by user_id; quotas by plan; per-user API keys/limits.

Scaling
- Queue workers for analysis/AI; pool external API calls; shard Telegram connections.

UX
- Per-user alert channel/group setup; per-user config commands; onboarding flow.


