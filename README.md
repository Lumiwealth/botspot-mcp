# BotSpot MCP Server — AI Trading Bots & Backtesting

[![MCP Server](https://img.shields.io/badge/MCP-Server-blue)](https://mcp.botspot.trade/mcp)
[![Website](https://img.shields.io/badge/Website-botspot.trade-green)](https://botspot.trade)
[![Lumibot](https://img.shields.io/badge/Built%20on-Lumibot-orange)](https://github.com/Lumiwealth/lumibot)

**The only AI trading MCP server that takes you from strategy idea to live bot in one conversation.**

Generate trading strategies from plain English, backtest on real historical data, and deploy live to 10+ brokers. No coding required. Stocks, options, crypto, and futures.

## Quick Start

### Claude (Settings > Connectors)
1. Open Claude **Settings > Connectors**
2. Click **Add custom connector**
3. Paste: `https://mcp.botspot.trade`
4. Click **Connect** and complete OAuth login

### ChatGPT (Developer Mode)
1. Open ChatGPT **Settings > Connectors > Advanced > Developer Mode**
2. Go to **Connectors > Create**
3. Paste: `https://mcp.botspot.trade/mcp/public`
4. Complete OAuth login

### Claude Code (CLI)
```bash
claude mcp add --transport http botspot https://mcp.botspot.trade/mcp \
  -H "Authorization: Bearer botspot_YOUR_API_KEY"
```

### Cursor
Add to `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "botspot": {
      "url": "https://mcp.botspot.trade/mcp",
      "headers": {
        "Authorization": "Bearer botspot_YOUR_API_KEY"
      }
    }
  }
}
```

Get an API key at [botspot.trade/account-settings](https://botspot.trade/account-settings) (Account Settings > API Keys).

## What You Can Do

### AI Strategy Generation
Describe a trading strategy in plain English. The AI generates production-ready Python code using [Lumibot](https://github.com/Lumiwealth/lumibot) (1,300+ GitHub stars, MIT license).

### Backtesting
Run backtests with configurable date ranges, starting capital, and parameters. Query results with SQL (DuckDB). See equity curves, drawdowns, win rates, trade logs.

### Live Deployment & Monitoring
Deploy to 10+ supported brokers. Monitor positions, performance, and equity curves in real time.

### Strategy Marketplace
Browse proven community strategies with real performance data. Clone and modify.

## Supported Brokers

Charles Schwab, Interactive Brokers, Alpaca, Tradier, Tradeovate, Coinbase, Binance, Kraken, KuCoin, NinjaTrader

## Supported Assets

Stocks, options, crypto, futures

## 32 MCP Tools

| Category | Tools |
|----------|-------|
| **Strategy Generation** | `generate_strategy`, `refine_strategy`, `generation_status`, `generate_other_code` |
| **Strategy Management** | `list_strategies`, `get_strategy`, `update_strategy`, `delete_strategy`, `get_code`, `list_revisions`, `set_strategy_revision` |
| **Backtesting** | `start_backtest`, `stop_backtest`, `backtest_status`, `list_backtests`, `get_backtest_artifact`, `query_csv` |
| **Deployment** | `list_deployments`, `get_deployment_logs`, `get_bot_performance`, `get_bot_positions`, `get_portfolio_series` |
| **Visuals** | `get_strategy_visuals`, `get_backtest_visuals`, `get_backtest_chart_series` |
| **Marketplace** | `list_public_bots`, `share_strategy`, `publish_to_marketplace`, `unpublish_from_marketplace`, `clone_strategy` |
| **Account** | `get_account_status`, `get_tool_call_metrics` |
| **Data** | `set_data_provider` |

## Free Tier

- 10 AI messages per month
- 2 strategy generations per month
- 30 minutes of backtesting per month
- No credit card required

## Pricing

- **Free:** Limited usage (above)
- **Starter:** $99/month
- **Pro:** $199/month
- **All Access:** $399/month
- **Enterprise:** Custom pricing

See [botspot.trade/pricing](https://botspot.trade/pricing)

## Technical Details

- **Transport:** Streamable HTTP (JSON response mode)
- **Auth:** OAuth 2.1 with Dynamic Client Registration (browser) or API key bearer token (CLI/IDE)
- **Endpoints:**
  - `https://mcp.botspot.trade/mcp` — Full tool set (Claude, CLI, IDE)
  - `https://mcp.botspot.trade/mcp/public` — Commerce-filtered (ChatGPT Apps SDK)
- **OAuth Discovery:** `https://mcp.botspot.trade/.well-known/oauth-protected-resource`

## Links

- [Website](https://botspot.trade)
- [Setup Guide](https://botspot.trade/agents)
- [Pricing](https://botspot.trade/pricing)
- [Marketplace](https://botspot.trade/marketplace)
- [Enterprise](https://botspot.trade/enterprise)
- [Lumibot Framework](https://github.com/Lumiwealth/lumibot)
- [Privacy Policy](https://botspot.trade/privacy)
- [Terms of Service](https://botspot.trade/terms)

## License

The BotSpot MCP Server is a commercial product. The underlying trading engine ([Lumibot](https://github.com/Lumiwealth/lumibot)) is open-source under the MIT license.
