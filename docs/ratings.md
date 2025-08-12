Reputation and Ratings

Callers
- Store caller `user_id`, `username`, `rating`, counters for calls/success.
- Formula configurable (e.g., weight base rating + success rate).

Chats
- Maintain chat quality score (alerts per msg, presence of top callers, scam rate).

Usage
- Weight importance score by caller/chat rating; adjust thresholds by chat quality.
 - Caller success evaluation (no manual rating changes): multi-horizon growth metrics (1d/7d/30d), total growth, presence of explanation, drawdown severity (e.g., "ukatalsya"), and sell-call quality (timeliness). Combine into a configurable formula; expose formula edits via config, not per-caller manual changes.

Updates
- Periodic adjustment based on outcomes (price action, alert utility) or manual commands.


