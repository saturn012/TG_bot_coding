Message Analysis Pipeline

Steps
1. Pre-process: normalize text, collect metadata, skip excluded senders.
2. Spike detection: sliding window msg/min vs baseline; dynamic multiplier or fixed threshold.
3. Token parsing: tickers, names, CA detection; resolve chain (Base/Ethereum), watch/ignore lists.
4. Verified caller check: lookup sender in `callers` with rating.
5. Content analysis: keyword heuristics + optional realtime AI (gated by heuristics).
6. Scoring & categorization: combine spike/token/caller/AI/keywords into score → Urgent/Interesting/Queue/Ignore.
7. Alert formatting: source link, snippet, token data, safety notes, flags (spike/caller).
8. Dispatch: send to output chat thread by category.
9. Persist: save message, decision, events; mark for batch AI if needed.

Optimizations
- Cache token data; debounce duplicate alerts; aggregate near-duplicate mentions.
- Use background tasks for external APIs; enforce rate limits.


