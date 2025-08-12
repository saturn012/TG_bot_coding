Logging and Monitoring

Logging
- Structured logs with context (chat, token, severity). Rotate logs; adjustable verbosity.
- Key lines: listener events, analysis results, alert sends, API errors, AI errors.

Resilience
- Retry/backoff on HTTP errors; queue internal processing; pause unstable sources; watchdog for reconnects.

Ops
- Process manager restarts, optional Sentry; health summaries; optional notifications to control chat on critical errors.


