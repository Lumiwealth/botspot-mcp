# BotSpot: strategies, backtests and bot monitoring

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=botspot&config=eyJ1cmwiOiJodHRwczovL21jcC5ib3RzcG90LnRyYWRlL21jcCIsImhlYWRlcnMiOnsiWC1Cb3RTcG90LUF0dHJpYnV0aW9uIjoidXRtX3NvdXJjZT1naXRodWImdXRtX21lZGl1bT1yZWFkbWUmdXRtX2NhbXBhaWduPWJvdHNwb3RfbWNwIn19)
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_BotSpot-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=botspot&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.botspot.trade%2Fmcp%22%2C%22headers%22%3A%7B%22X-BotSpot-Attribution%22%3A%22utm_source%3Dgithub%26utm_medium%3Dreadme%26utm_campaign%3Dbotspot_mcp%22%7D%7D)
[![Add to Claude](https://img.shields.io/badge/Claude-Add_connector-D97757?style=flat-square&logo=anthropic&logoColor=white)](#claude)

Claude Code, one command:

```sh
claude mcp add --transport http botspot https://mcp.botspot.trade/mcp
```

Connect your AI assistant to your own [BotSpot](https://botspot.trade) account. Create and edit [LumiBot](https://github.com/Lumiwealth/lumibot) strategies, run historical backtests, analyze results and monitor bots.

**Free to connect.** Signing in creates a free BotSpot account. Paid plans unlock heavier backtests, live bots and real-money trades; see [current pricing](https://botspot.trade/pricing) and the [setup guide](https://botspot.trade/agents?utm_source=github&utm_medium=readme&utm_campaign=botspot_mcp). Broker access, data subscriptions, regional availability and account permissions depend on the workflow.

## Quick start

1. Click a button above, or run the Claude Code command.
2. Sign in with BotSpot when your app asks. No API key needed; signing in creates your free account.
3. Ask: "List my BotSpot strategies and latest completed backtests. Do not create, edit, deploy or trade."
4. Then try: "Create a simple moving-average LumiBot strategy and run a historical backtest."

Want your coding agent to write [LumiBot](https://github.com/Lumiwealth/lumibot) strategies well? Add the free [LumiBot trading skills](https://github.com/Lumiwealth/lumibot-trading-skills).

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
