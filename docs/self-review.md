Self-Review Notes

Backend
- Async processing with task offloading for slow APIs; strict error boundaries.

Architecture
- Use Redis for counters and short-lived state; DB for durable state.

QA
- Unit tests for parsers/scoring; integration tests for spike scenarios; plumbing tests for AI batch.

DB
- Indices on hot paths; consider composite keys (chat_id, message_id) for uniqueness.

PM/UX
- Clear thread naming and message formatting; avoid notification fatigue with throttling.


