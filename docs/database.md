Database Design

Core tables (Postgres)
- messages(id PK, chat_id, message_id, sender_id, text, timestamp, is_spike, tokens[], caller_id, importance_score, category, alerted, needs_ai)
- alerts(alert_id PK, time_sent, category, chat_id, message_id, summary)
- callers(user_id PK, username, rating, calls_made, calls_success, last_active)
- chats(chat_id PK, name, rating, avg_msg_per_min, last_spike, alerts_today)
- user_config(user_id, config_key, config_value, PK(user_id, config_key))
- tokens(token_id PK, symbol, name, last_price, last_mcap, last_updated, chain)
 - topics(chat_id PK, urgent_topic_id, interesting_topic_id, overview_topic_id, sol_topic_id, misc_topic_id)

Indexes
- messages(chat_id, timestamp), messages(sender_id), messages(needs_ai)

Retention
- Keep important/flagged; prune trivial after TTL; keep summary stats.


