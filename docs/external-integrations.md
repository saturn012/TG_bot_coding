External Token/Data Integrations

Market Data
- CoinGecko or GeckoTerminal/Dexscreener for price, mcap, FDV, supply.

Safety/Contract
- Honeypot checks (e.g., Honeypot.is for ETH/Base).
- Etherscan/GoPlus for verification and risky functions.

DEX/liquidity
- Uniswap subgraph, Dexscreener for pools/liquidity/price.

Caching & Backoff
- In-memory cache with TTL; periodic refresh for active tokens; retry with jitter and fallbacks.


