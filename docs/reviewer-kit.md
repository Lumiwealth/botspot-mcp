# BotSpot restricted connection review kit

Prepared October 13, 2026. **Not a compliance attestation or a completed store installation.** The direct Dev workflow has been exercised; the store client ceiling, production reviewer identity and destination installations remain unqualified.

## Shared listing facts

- Product: BotSpot; publisher: Lumiwealth, subject to destination verification.
- Endpoint: `https://mcp.botspot.trade/mcp` (Streamable HTTP, OAuth).
- Setup/source: https://github.com/Lumiwealth/botspot-mcp .
- Pricing: https://botspot.trade/pricing ; a paid account is required.
- Privacy: https://botspot.trade/privacy ; terms: https://botspot.trade/terms .
- Support: contact@botspot.trade .
- Initial requested capability: create/edit strategy files, run historical backtests, read results/charts and account reports. Strategy creation and backtest jobs are writes; they must not be labeled read-only.
- Exclusions: brokerage order placement/modification/cancellation, liquidation/exercise, trading deployment starts/restarts/updates, trading schedules and indirect execution through generated jobs or broker credentials. Paper brokerage orders are excluded initially too.
- Direct MCP capabilities remain broader. The submitted connection's actual signed grant and tool scan must match its description. No client name, User-Agent or requested-scope string is a trusted permission boundary.

## Reviewer account prerequisites

Provision a dedicated synthetic production reviewer identity through the supported account/administrative path; do not reuse an owner/customer login or disclose the shared Dev test credentials. It must have review-duration paid/data access without requiring a real purchase, representative saved strategy/backtest data, and no live broker credentials or funds. If a destination requires password sign-in without MFA/email challenges, qualify that exact isolated identity; do not weaken authentication on another account.

Each destination receives its own trusted OAuth client registration and exact callback configuration. Signed client provenance and the server-owned ceiling must survive token refresh, reconnect and background work. Never put passwords, client secrets or reviewer tokens in this repository. Deliver them only through the destination's private review channel after testing.

## Five positive cases

| Case | Reviewer prompt | Required evidence |
| --- | --- | --- |
| P1 | Check my BotSpot account access and list my strategies. Do not change anything. | Authenticated account/strategy result, with no unrelated private data. |
| P2 | Create SPY Hold Example: buy SPY once with 50% of starting cash, hold, and add a daily price chart. Do not deploy or place brokerage orders. | Neutral workspace, complete saved files, new immutable revision and readback. |
| P3 | Backtest the newest saved revision for October 5–11, 2026 with $10,000. | Exact revision/run linkage; queued/running states distinguished from terminal completion. |
| P4 | For that exact run, report filled trades, return and drawdown, and show its equity chart. | Terminal status, bounded filled-trade query and matching chart; unavailable fields explicitly reported. |
| P5 | Reconnect and read the same saved strategy revision and backtest result. | Same user ownership and store ceiling after reauthentication; no duplicate strategy or run. |

## Three negative cases

Run these only in the synthetic qualification environment. Use a broker/service spy or approved test broker and verify denial **before** the external call. An assistant refusing a prompt is not backend enforcement evidence.

| Case | Request | Required evidence |
| --- | --- | --- |
| N1 | Submit, modify or cancel a brokerage order, including an initially requested paper order. | Visible authorization denial; zero broker writes. |
| N2 | Start/restart/update a trading deployment, or schedule/background a trading launch. | Visible denial; zero trading jobs created or altered. |
| N3 | Obtain broader authority by refresh, reconnect, a spoofed client name/User-Agent, requested full scopes, key issuance or an indirect generated job. | Verified originating client ceiling remains enforced; no credential or authority escape. |

Direct-client comparison tests must separately prove that ordinary approved trading/deployment scopes and their normal approval flow remain intact. Do not execute real-money trades to prove this.

## Test and demo record

October 13 Dev check: authenticated account access; neutral strategy creation; complete SPY hold strategy saved as a second revision and read back; seven-day historical backtest completed; Parquet queries verified one filled buy; equity series returned; bounded runtime diagnostics found no error/traceback/exception matches. The installed runtime identified itself as LumiBot 4.6.19. This was a direct headless MCP workflow, not a real-model prompt eval, fresh client installation, restricted grant test or production/store qualification.

Demo sequence after the restricted integration is released: fresh client install → reviewer OAuth → account check → save strategy → start exact-revision historical run → wait → inspect filled trades and chart → demonstrate forbidden launch denial → disconnect/reconnect. Record the actual destination, served source tuple, client registration identity, grant and outcomes privately. Do not substitute screenshots of another environment or decorate performance evidence.

Before submitting, replace every pending item with actual evidence: production endpoint/served tuple, trusted destination client identity, reviewer sign-in, each tool's title/schema/annotations and side effects, private credentials, required brand/screenshot formats, actual demo and destination-specific test receipts. OpenAI's current review requirements require a testable demo account and successful workflows on every selected ChatGPT/Codex surface. Claude asks for testing every submitted tool and, for MCP Apps, 3–5 response-only PNG screenshots at least 1000px wide. Muse requires the final payment classification and data-handling answers to match the submitted grant.

Sources: [OpenAI review](https://developers.openai.com/plugins/deploy/app-review), [Claude submission](https://claude.com/docs/connectors/building/submission), [Muse guidelines](https://muse.ai/platform/docs).
