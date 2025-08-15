-- Core tables
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    chat_id BIGINT NOT NULL,
    message_id BIGINT NOT NULL,
    sender_id BIGINT,
    text TEXT,
    timestamp TIMESTAMPTZ NOT NULL,
    is_spike BOOLEAN DEFAULT FALSE,
    tokens TEXT[],
    caller_id BIGINT,
    importance_score REAL,
    category VARCHAR(20),
    alerted BOOLEAN DEFAULT FALSE,
    needs_ai BOOLEAN DEFAULT FALSE
);
CREATE INDEX IF NOT EXISTS idx_messages_chat_time ON messages(chat_id, timestamp);

CREATE TABLE IF NOT EXISTS alerts (
    alert_id SERIAL PRIMARY KEY,
    time_sent TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    category VARCHAR(20),
    chat_id BIGINT,
    message_id BIGINT,
    summary TEXT
);

CREATE TABLE IF NOT EXISTS callers (
    user_id BIGINT PRIMARY KEY,
    username TEXT,
    rating REAL DEFAULT 5.0,
    calls_made INT DEFAULT 0,
    calls_success INT DEFAULT 0,
    last_active TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS chats (
    chat_id BIGINT PRIMARY KEY,
    name TEXT,
    rating REAL DEFAULT 5.0,
    avg_msg_per_min REAL,
    last_spike TIMESTAMPTZ,
    alerts_today INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS user_config (
    user_id BIGINT DEFAULT 0,
    config_key TEXT NOT NULL,
    config_value TEXT NOT NULL,
    PRIMARY KEY(user_id, config_key)
);

CREATE TABLE IF NOT EXISTS tokens (
    token_id TEXT PRIMARY KEY,
    symbol TEXT,
    name TEXT,
    last_price REAL,
    last_mcap REAL,
    last_updated TIMESTAMPTZ,
    chain TEXT
);

CREATE TABLE IF NOT EXISTS topics (
    chat_id BIGINT PRIMARY KEY,
    urgent_topic_id BIGINT,
    interesting_topic_id BIGINT,
    overview_topic_id BIGINT,
    sol_topic_id BIGINT,
    misc_topic_id BIGINT
);

-- Defaults
INSERT INTO user_config(user_id, config_key, config_value)
    VALUES (0,'min_mcap','50000') ON CONFLICT DO NOTHING;
INSERT INTO user_config(user_id, config_key, config_value)
    VALUES (0,'min_liq','1000') ON CONFLICT DO NOTHING;
INSERT INTO user_config(user_id, config_key, config_value)
    VALUES (0,'spike_threshold','20') ON CONFLICT DO NOTHING;
INSERT INTO user_config(user_id, config_key, config_value)
    VALUES (0,'spike_window_sec','300') ON CONFLICT DO NOTHING;
INSERT INTO user_config(user_id, config_key, config_value)
    VALUES (0,'ai_interval_hours','6') ON CONFLICT DO NOTHING;

