AI Delayed/Batch Analysis

Flow
- Flag borderline/complex messages for AI review.
- Cron every 4–6h batches items per chat/topic; summarize spikes, consolidate token mentions.
- Post summaries to Overview; raise late alerts if AI finds missed important items.
 - Interval is adjustable (/aiinterval). Prefer lower frequency if non‑AI filters perform well; otherwise increase with prefiltering to cap volume.

Cost/Performance
- Batch prompts; cap volume; retries and graceful skip on errors.

Feedback
- Use AI results to adjust thresholds/rules; optional rating updates.


