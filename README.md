# BotSpot: strategies, backtests and bot monitoring

Connect your AI assistant to your own [BotSpot](https://botspot.trade) account. Create and edit [LumiBot](https://github.com/Lumiwealth/lumibot) strategies, run historical backtests, analyze results and monitor bots.

**A paid BotSpot plan is required.** Check [current pricing](https://botspot.trade/pricing). This page is the maintained setup guide. Broker access, data subscriptions, regional availability and account permissions depend on the workflow.

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

### Cline

Open **MCP Servers → Remote Servers**. Enter BotSpot and the endpoint above, select **Streamable HTTP**, add the server and complete its OAuth authorization. Verify the tools appear and run the account check below. This manual setup has not yet been qualified in Cline; the marketplace application is pending.

### ChatGPT and Codex

For a custom ChatGPT connection, open **Plugins → Add custom MCP server**, enter the endpoint above and complete OAuth. Custom connections and local plugin packages are separate from the public directory. Public OpenAI review has additional requirements, including restrictions on investment-trade execution; this current full-capability connection is not yet qualified for that listing.

For Codex CLI:

```sh
codex mcp add botspot --url https://mcp.botspot.trade/mcp
codex mcp login botspot
```

In Codex, use `/mcp` to check the connection. See the [official Codex MCP documentation](https://developers.openai.com/codex/mcp).

### Grok and Muse

MCP support and public distribution differ by product. Grok Build accepts Claude-compatible plugin packages; its official marketplace requires a reviewed catalog pull request pinned to an exact public commit. Grok Bot has separate product surfaces. Muse accepts approved connectors, and its current finance policy excludes new trade-order tools. A working custom connection is not a store approval.

## Your first useful result

Start with an account check, then build one historical example. No brokerage connection is needed for this example when your plan includes the required historical data.

1. **Check the connection:** “Check my BotSpot account access and list my strategies. Do not change anything.”
2. **Create and backtest:** “Create a strategy called SPY Hold Example. Buy SPY once using 50% of starting cash, keep the other half in cash, and hold. Run a historical backtest for October 5–11, 2026 with $10,000. Include a price chart. Do not start a trading deployment or place brokerage orders.”
3. **Read the result:** “For that exact backtest, wait for a terminal status, then report the tested revision, dates, filled trade count, return and drawdown. Show its equity chart. Say plainly if any result is missing.”

The assistant should create a workspace, save a new revision, read it back and start the backtest from that newest revision. A queued job is still running. Keep the same backtest ID when inspecting its status, chart and trade artifacts.

For existing work, ask: “Show performance and positions for my existing bot without changing it.”

Backtests are historical simulations and do not guarantee future returns. Missing data is unknown. Ask your assistant to wait for confirmed results before claiming a backtest or deployment completed.

## Capabilities and permissions

The live server discovers its current tool list at connection time. Strategy workflows use `create_strategy` and direct file/revision tools. Backtest workflows use `start_backtest`, `backtest_status` and artifact tools. Monitoring includes deployments, broker snapshots and portfolio reports.

The direct connection also exposes writes, including trading and deployment actions. Account ownership, plan entitlements and product approvals apply. Connecting an account does not itself authorize a trade. Directory eligibility must be verified against the tools actually offered; do not describe this full connection as read-only.

Public store approval is pending. The planned store connection supports strategy development, historical backtests and reports, with brokerage orders and trading launches unavailable. That restriction has not yet been qualified or released. Use the [destination tracker](docs/distribution-status.md) to check availability; a submitted application is not an installed plugin.

## Connection problems

- **Not signed in:** use the client's normal OAuth sign-in or reconnect control, then repeat the account check.
- **Paid access or data required:** use the returned account/data-access instructions. Do not change providers merely to bypass an entitlement error.
- **Operation not permitted:** inspect the connection's granted permissions. A smaller requested scope or a different display name does not grant extra authority.
- **Backtest still queued:** check the original job's status. Do not start duplicate runs.

Disconnect through your client's connector controls. For a BotSpot API key, revoke the exact key in BotSpot Account Settings. Keep keys in your client/secret manager; never paste them into a prompt or commit them.

Client setup sources: [Claude Code](https://code.claude.com/docs/en/mcp), [Cursor](https://cursor.com/docs/mcp), [Codex](https://developers.openai.com/codex/mcp), and [Cline](https://docs.cline.bot/mcp/mcp-overview). Client menus can change; the endpoint above stays the same.

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
