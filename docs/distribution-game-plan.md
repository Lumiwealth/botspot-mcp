# BotSpot app-store distribution game plan

Date: October 12, 2026. This is an execution plan, not a claim that restricted grants or new store approvals have shipped. [Current receipts](distribution-status.md) distinguish drafts, submitted applications, approval and live installation.

## The Alpaca precedent

Alpaca's [October 12 ChatGPT announcement](https://alpaca.markets/blog/paper-trading-and-live-portfolio-monitoring-now-available-in-chatgpt-with-alpaca/) separates simulated order placement from live-account reporting. Its ChatGPT Live plugin cannot submit, modify or cancel live orders. Its [direct Trading MCP documentation](https://docs.alpaca.markets/us/docs/trading-api-mcp) separately supports live execution with live credentials and an explicit live-mode setting. The [official agentic repository](https://github.com/alpacahq/agentic) distributes hosted live and paper endpoint configurations for supported clients. The hosted implementation and private review agreements were not inspected, so do not claim to know Alpaca's internal enforcement mechanism or approval rationale.

## Product contract — simplify the first store release

Keep the canonical authenticated endpoint `https://mcp.botspot.trade/mcp`, existing handler/service owners and current direct-client behavior. Do not revive `/mcp/public`, introduce a separate product backend or build a general permissions UI/engine for this distribution task.

Use two initial connection profiles:

| Connection profile | First-release contract |
| --- | --- |
| Direct MCP | Existing authorized functionality, including permitted real-money execution and normal approvals. |
| Restricted store installation | Strategy development, historical backtesting and account/result reporting. Broker writes and deployment/schedule actions that initiate trading are unavailable. |

Register each restricted store's OAuth connection separately and map its verified client/installation identity to the restricted profile in server-owned configuration. Stores that accept the normal connector keep direct functionality. Do not blanket-restrict every external client, and do not infer the profile from User-Agent, app display name, a URL flag or model instructions.

Start with the shared research/backtesting profile to reduce review and engineering complexity. Broker paper orders are optional follow-through after a destination confirms they are acceptable and they materially improve activation. ChatGPT has Alpaca's published paper-order precedent; Claude and Muse require their own review. Initial store descriptions must not promise paper-order execution that has not shipped.

A direct install is not an exemption from the host's policies. Document compatible direct clients honestly; no instructions to evade platform rules or hidden route from a restricted store connection to live execution.

## Track 1 — qualify the smallest real compatibility change

1. Confirm each store accepts the proposed authenticated capability contract and tool inventory before broad implementation. A trade tool returning a visible permission error may not satisfy every store's inventory requirements. Do not fake the scan result, hide tools to pass review or call the full connector read-only.
2. Audit existing issuance, client identity, refresh and shared static-client fallback. Node main currently has a default that can expand external scopes to the full advertised set; requesting fewer manifest scopes alone is insufficient. Verify deployed configuration separately. Keep ordinary direct clients unchanged rather than globally switching scope modes.
3. Resolve the profile from a verified signed OAuth identity plus trusted registration/configuration. Apply the small store restriction inside existing authorization and execution owners. Refresh, reconnect and incremental scope requests cannot remove it. No new scheduler, database owner, regex intent router or parallel MCP implementation.
4. Check all execution paths: broker order writes, liquidation/exercise, mode/configuration changes, deployment starts/restarts/updates, trading schedules/background wakes, generated jobs and access to live broker secrets. Validate actual account mode; carry the originating restriction into work that runs later. Visible authorization errors are required; prompts and tool descriptions alone are insufficient.
5. Prove restricted strategy/backtest/report workflows succeed; prohibited actions fail before a broker call; direct behavior and normal approvals remain intact; refresh, spoofed metadata, connection switching, revocation and ownership tests pass. Use synthetic users/test accounts, establish red regressions, run required Node owning-folder/type/contracts and exact-source cloud OAuth/browser checks. Production deployment remains a separate normal approval/release step.

The goal is real store-compatible functionality with the smallest maintenance surface. A review-only restriction that is advertised but does not work is not a completed integration. The current task has produced a plan; these product changes have not been implemented.

## Track 2 — complete a reusable reviewer kit

Prepare a dedicated reviewer identity, supported sign-in path and synthetic seeded account with representative strategies, historical backtest artifacts, clearly labeled account observations and permitted simulation access. No customer login, owner account credentials or live funds. Set scoped usage limits for review without changing customer/provider-wide limits.

Keep one versioned kit with the package/source SHA, tested endpoint and grant, paid-plan disclosure, tool permissions/side effects, privacy/terms/support/security contacts, correctly sized original/approved brand assets, a short demo and setup/revocation instructions. Credentials are delivered only through the destination's approved private review channel. OpenAI needs five positive and three negative test cases; Anthropic needs at least three working examples; include platform-specific requirements without inventing completed tests.

Run an actual install-to-success workflow in each target client with the reviewer identity. Then attempt prohibited operations and verify the denial. Record screenshots, source-bound test receipts and the exact received application ID. Heavy browser/build work stays in the established cloud runner. Requested deliverables stay outside disposable output; temporary captures use task-owned artifact runs, with QA evidence retained under the 14-day policy.

## Track 3 — finish the major-store submissions

| Destination | Remaining steps | Submitted means |
| --- | --- | --- |
| ChatGPT / OpenAI / Codex | Resolve the publisher identity path with the existing support specialist: individual approval and business-name publishing are separate facts. Complete required business verification if the intended publisher requires it, without fabricating identity evidence. Then upload the qualified package, verify the domain, configure the restricted OAuth client, connect the reviewer identity, pass scans and supply cases/demo. | Portal confirms submitted for review with a durable receipt. |
| Claude | Reuse the existing application and queued email. Connect the reviewer account, complete the applicable connector/plugin route, settle capability questions and make only tested compliance attestations. | Completed portal submission and receipt; email acknowledgement alone is insufficient. |
| Muse | Use the prepared 512x512, 136,288-byte logo after the Chrome extension file-upload permission is enabled. Complete business/data-handling questionnaires, restricted financial scope, reviewer access and demo. Verify any checkout/payment answer against the actual submitted grant. | Form confirms received submission. |
| Cursor curated marketplace | Reuse the prepared application and emailed review request. Resolve how section 3.1 applies to a free connector for a paid hosted service. Complete the normal portal flow with current source and install proof. | Portal receipt; email application and community listing are separate. |

Final publisher agreements/warranties need specific approval when presented for acceptance. Prepare a complete, reviewable application first. Review decisions belong to the store and have no guaranteed completion date. Nothing in this plan authorizes paid listings or changes to production authentication/configuration.

## Track 4 — finish directory distribution

- **Smithery:** qualify OAuth tool discovery with the dedicated reviewer grant. Investigate its documented static server-card route for metadata discovery if scanning remains blocked; a card does not prove authenticated installation works. Verify the public page shows accurate capabilities and a usable install path.
- **Glama:** complete exact domain-ownership proof through the approved deployment path, update metadata and verify its authenticated health/install process. Existing unhealthy status or a correction report is not completion. Once Glama works, use eligible remote-server list intake without duplicate submissions.
- **Cline:** finish Cline-assisted installation qualification and exact icon requirements on canonical issue 1352; add truthful evidence to that issue and await review.
- **Grok Build:** track existing PR 1376, address review requests and verify the installed plugin after merge. It was still open when this plan was prepared. No separate Grok Bot store route is verified.
- **MCP Market, mcpservers.org, MCP.Directory and Awesome Remote MCP Servers:** reuse submitted applications/PRs; respond to actual review requests, then verify the live listing and installation. An estimated queue time is not approval.
- **Official Registry and Cursor community directory:** preserve current corrected listings; qualify authenticated installation and reconcile any changed package metadata without duplicating entries.
- **PulseMCP:** intake was paused at the latest audit; revisit when available, with no recurring schedule created.
- **mcp.so:** the current $39 intake is optional and requires an approved spend decision.
- **Appz and additional agent stores:** verify the existing Appz listing and its ownership before changes. For Gemini, VS Code/Copilot, Windsurf and additional agents, identify the official supported distribution/intake route first. MCP compatibility is not a curated-store listing; do not invent an app store or count the same registry twice.

## Listing explanation

Proposed first-release copy, to use only after the stated checks pass:

> Build and backtest strategies and review your account in ChatGPT. This connection cannot place or change brokerage orders. BotSpot's direct MCP supports permitted live trading in compatible clients, subject to your account permissions and approvals. A paid BotSpot account is required.

Each store receives wording matching its actual grant. The direct-install guide explains supported clients, account setup and normal approvals. Have each store review proposed direct-connection links/copy; never promise a bypass of that host's policies.

## Acquisition after installation works

1. Use one canonical setup destination: supported clients, clear install/connect steps, paid-plan requirement, store limitations and direct-MCP capabilities. Provide a small set of runnable first-use prompts for strategy creation, a historical backtest and inspection of recorded results.
2. Test the path from directory click through sign-in to the first successful useful result. Remove demonstrated onboarding failures before expanding promotion. A live listing with broken OAuth is a poor acquisition channel.
3. Put accurate setup references in relevant LumiBot documentation and the maintained public connector repository. Reuse existing eligible directory submissions; prioritize verified discoverability over duplicate listings or paid badges.
4. Share a tested use case through existing, appropriate developer/customer channels after release and store approval. Prepare source-backed teaching material and outreach for review; send or publish only through the separately authorized channel. New video-topic decisions use vidIQ first. No unsolicited campaigns, paid upgrades, cross-chat work or recurring schedules.
5. Measure acquisition and retention: source-tagged visits and successful connections, first completed useful backtest/report, returning users, paid activation and retained collected contribution cash. Reconcile payment outcomes; validate identity joins and staff/synthetic exclusions before claiming conversion. Use connected first-party GSC for organic queries/pages and production-filtered analytics where coverage is verified. Installs, impressions and directory counts alone do not establish customer growth.

## Order and completion

Start the small restricted-store compatibility contract and reviewer kit first. Publisher identity, upload permission and existing review replies can be resolved independently. After the security tests and normal release qualification, finish ChatGPT, Claude and Muse submissions; finish Cursor once its terms are resolved. Continue already-submitted directories using their existing application IDs.

Maintain states separately: prepared → submitted → approved → published → installed successfully. The requested submission milestone is a verified receipt for every available, eligible free intake, plus an exact blocker for closed, paid or unsupported destinations. Distribution completion additionally requires a live listing and successful authenticated installation. Save small code/source/run/application receipts in the maintained tracker; keep private credentials and customer data out of source control. No new recurring monitoring or outreach schedule is created.

## Sources

- [Alpaca ChatGPT launch](https://alpaca.markets/blog/paper-trading-and-live-portfolio-monitoring-now-available-in-chatgpt-with-alpaca/)
- [Alpaca direct Trading MCP](https://docs.alpaca.markets/us/docs/trading-api-mcp)
- [Alpaca agentic package](https://github.com/alpacahq/agentic)
- [OpenAI OAuth contract](https://developers.openai.com/plugins/build/auth)
- [OpenAI submission requirements](https://developers.openai.com/plugins/deploy/submission)
- [Anthropic directory policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)
- [Muse guidelines](https://muse.ai/platform/docs)
- [Cursor publisher terms](https://cursor.com/marketplace-publisher-terms)
