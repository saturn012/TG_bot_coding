Configuration and Commands

Config (YAML/JSON)
- telegram: api_id, api_hash, session_name, output_chat, category_topics
- analysis: thresholds, spike window, network focus, ai flags, intervals
- ratings: defaults and formulas
- callers: initial list with ratings

Runtime Commands (via control chat)
- /help, /callers [days], /listcallers
- /addcaller <user> <rating>, /setrating <user> <rating>
- /spikesedit <threshold> [window]
- /togglenetwork <chain>, /aiinterval <hours>
- /pause, /resume, /reload
 - /filtr <min_mcap> <min_liq> [chain] — adjust token filters on the fly (e.g., `/filtr 50000 1000 base`).

Hot-reload or persist command changes to DB/config.


