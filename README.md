# BotSpot: strategies, backtests and bot monitoring

Connect your AI assistant to your own [BotSpot](https://botspot.trade) account. Create and edit [LumiBot](https://github.com/Lumiwealth/lumibot) strategies, run historical backtests, analyze results and monitor bots.

**Free to connect.** Signing in creates a free BotSpot account. Paid plans unlock heavier backtests, live bots and real-money trades; see [current pricing](https://botspot.trade/pricing) and the [setup guide](https://botspot.trade/agents). Broker access, data subscriptions, regional availability and account permissions depend on the workflow.

## Connect

Use the Streamable HTTP endpoint **`https://mcp.botspot.trade/mcp`**. Sign in through BotSpot OAuth. Never paste credentials into a chat or commit them to a repository.

### Claude

Open **Customize → Connectors → Add custom connector**. Name it BotSpot, enter the endpoint above and complete sign-in. This is a custom connection; it does not establish a public directory listing.

### Claude Code

```sh
claude mcp add --transport http botspot https://mcp.botspot.trade/mcp
```

Run `/mcp` to finish OAuth sign-in. The repository also includes a Claude-compatible plugin manifest and MCP configuration for plugin hosts, including Grok Build.

### Cursor

Add this to your MCP configuration and use Cursor's sign-in control:

```json
{
  "mcpServers": {
    "botspot": {
      "url": "https://mcp.botspot.trade/mcp"
    }
  }
}
```

This repository also contains a portable Agent Plugins package (`plugin.json` and `mcp.json`) for hosts supporting that standard. A marketplace application is separate from installing this configuration manually.

### ChatGPT and Codex

For a custom ChatGPT connection, open **Plugins → Add custom MCP server**, enter the endpoint above and complete OAuth. Custom connections and local plugin packages are separate from the public directory. Public OpenAI review has additional requirements, including restrictions on investment-trade execution; this current full-capability connection is not yet qualified for that listing.

For Codex CLI, add the same remote endpoint through its MCP settings and complete the normal OAuth flow. See the [official Codex MCP documentation](https://developers.openai.com/codex/mcp).

### Grok and Muse

MCP support and public distribution differ by product. Grok Build accepts Claude-compatible plugin packages; its official marketplace requires a reviewed catalog pull request pinned to an exact public commit. Grok Bot has separate product surfaces. Muse accepts approved connectors, and its current finance policy excludes new trade-order tools. A working custom connection is not a store approval.

## Trading skills for your AI

Free, MIT-licensed LumiBot trading skills that teach Claude Code, Codex, Cursor and other agents to write, backtest and fix strategies: [Lumiwealth/lumibot-trading-skills](https://github.com/Lumiwealth/lumibot-trading-skills).

```sh
npx skills add Lumiwealth/lumibot-trading-skills
```

## Example requests

- “List my BotSpot strategies and show the latest saved revision.”
- “Create a simple moving-average strategy, save its files and run a historical backtest.”
- “Open my latest backtest, report its status and summarize the available trade and performance artifacts.”
- “Show performance and positions for my existing bot.”

Backtests are historical simulations and do not guarantee future returns. Missing data is unknown. Ask your assistant to wait for confirmed results before claiming a backtest or deployment completed.

## Capabilities and permissions

The live server discovers its current tool list at connection time. Strategy workflows use `create_strategy` and direct file/revision tools. Backtest workflows use `start_backtest`, `backtest_status` and artifact tools. Monitoring includes deployments, broker snapshots and portfolio reports.

The direct connection also exposes writes, including trading and deployment actions. Account ownership, plan entitlements and product approvals apply. Connecting an account does not itself authorize a trade. Directory eligibility must be verified against the tools actually offered; do not describe this full connection as read-only.

## Package and license

- `plugin.json` and `mcp.json`: portable Agent Plugins package.
- `.claude-plugin/plugin.json` and `.mcp.json`: compatibility package for Claude-format plugin hosts.
- `server.json`: official MCP Registry metadata.
- `smithery.yaml` and `glama.json`: directory metadata.
- `assets/botspot.png`: existing BotSpot brand asset, used unchanged.

No server executable, hooks or credentials are bundled. The host contacts `mcp.botspot.trade` and discovers BotSpot's authorization provider at `botspot.us.auth0.com`. The hosted service remains commercial; see [LICENSE](LICENSE), [privacy](https://botspot.trade/privacy), [terms](https://botspot.trade/terms) and [support](mailto:contact@botspot.trade).

## Validate the package

```sh
python3 -m unittest discover -s tests -v
```

[Distribution status and requirements](docs/distribution-status.md) tracks evidence separately for live, submitted, prepared and blocked destinations.
