# BotSpot app-store distribution game plan

Date: October 12, 2026. This is an execution plan, not a claim that restricted grants or new store approvals have shipped. [Current receipts](distribution-status.md) distinguish drafts, submitted applications, approval and live installation.

## The Alpaca precedent

Alpaca's [October 12 ChatGPT announcement](https://alpaca.markets/blog/paper-trading-and-live-portfolio-monitoring-now-available-in-chatgpt-with-alpaca/) separates simulated order placement from live-account reporting. Its ChatGPT Live plugin cannot submit, modify or cancel live orders. Its [direct Trading MCP documentation](https://docs.alpaca.markets/us/docs/trading-api-mcp) separately supports live execution with live credentials and an explicit live-mode setting. The [official agentic repository](https://github.com/alpacahq/agentic) distributes hosted live and paper endpoint configurations for supported clients. The hosted implementation and private review agreements were not inspected, so do not claim to know Alpaca's internal enforcement mechanism or approval rationale.

## Product contract

Keep the canonical authenticated endpoint `https://mcp.botspot.trade/mcp`, existing handler/service owners and normal direct-client capabilities. The removed `/mcp/public` route and old exposure filter stay removed. A marketplace installation receives explicit permissions under the same authentication system; direct installations retain the user's approved capabilities and normal ownership, entitlement and trading approvals.

| Connection | Target capability contract |
| --- | --- |
| Direct MCP | Current authorized functionality, including permitted real-money execution. |
| ChatGPT directory | Strategy files, historical backtests, simulated trading and live-account reporting, subject to review of each capability. |
| Claude directory | Strategy files, backtests and reporting; verify simulated trading with Anthropic before attesting compliance. Financial-execution exceptions require written permission. |
| Muse directory | Begin with financial reads, account reports and backtest-result analysis. Verify strategy/backtest writes and simulation separately; do not assume ChatGPT's paper-trading precedent applies. |
| Other stores | Preserve supported direct functionality unless that destination requires a narrower grant. Disclose paid access and trading accurately. |

A direct install is not an exemption from the host's own policies. Document compatible clients where execution is permitted. Store copy must not instruct the host or model to evade its rules.

## Track 1 — qualify one authorization design

1. Audit current OAuth issuance, registration, signed claims, refresh/revocation and every money-affecting handler. Verify deployed settings independently of GitHub source. Current Node main source can expand external scopes to the complete advertised set by default; a restricted manifest request alone does not enforce least privilege. The current request context also needs a verified installation/client identity for a permission ceiling. Do not flip a global scope-mode switch and assume legacy clients remain functional.
2. Register dedicated store OAuth clients using supported provided-client flows where possible. Resolve the installation from verified token claims plus a trusted server-owned grant record. Client display names, User-Agent, URL query flags and caller-provided profile fields cannot establish authority. Shared static-client fallback must not erase the distinction for store connections.
3. Apply an immutable permission ceiling for the installation, intersected with the user's permissions and subscription entitlements. Refresh, incremental scope requests and reconnects must not elevate a store connection to a full direct grant. Direct connections keep their own explicit grant and existing approvals.
4. Enforce authorization inside the real tool/service execution path. Reads of live accounts may succeed; prohibited writes return a clear visible permission error. Validate the resolved broker/account mode, not only a caller's `paper` flag. Missing or unknown account mode denies execution. Scope checks remain real product/security controls; do not add hidden tool filters, regex intent routing or prompt-based safety as substitutes.
5. Audit bypass paths: order placement/replacement/cancellation, liquidation, options exercise, account/broker configuration, deployment start/restart/update, schedules and background wakes, generated-code jobs, saved-secret access and credential export. A store caller must not obtain live credentials or launch work that later trades live. Carry the same authority into queued work and background execution. Raw broker credentials must stay out of model-visible responses.
6. Inspect each reviewer's authenticated tool inventory and obtain clarification if the store requires prohibited tools to be absent rather than returning authorization errors. Do not invent an acceptable catalog contract, hide tools to pass a scan, or submit a full server as read-only. Resolve this external review boundary before broad endpoint or catalog changes.

Acceptance evidence uses synthetic users and confirmed test accounts: store reads succeed; allowed simulations succeed; live writes and indirect bypasses fail without a broker call; direct-client behavior and existing approvals are preserved; token renewal, client spoofing, connection switching, revocation and cross-user ownership tests pass. Establish red regressions before implementation. Run required Node type/unit/owning-folder contracts and exact-source cloud OAuth/browser qualification. Production deployment receives separate approval and served-source readback through the normal release playbook. No live customer trades are needed for validation.

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

Proposed ChatGPT copy, to use only after the stated capability checks pass:

> Build and backtest strategies, practice with simulated trading, and review your live portfolio in ChatGPT. This connection cannot place or change real-money orders. BotSpot's direct MCP connection supports permitted live trading in compatible clients, subject to your account permissions and approvals. A paid BotSpot account is required.

The direct-install guide can explain setup and supported clients. Have each store review any proposed direct-connection link/copy; it must not promise that installing directly bypasses that host's policies. Muse and any read-only grant receive copy matching their own actual capabilities.

## Order and completion

Start the scoped authorization contract and reviewer kit first. Publisher identity, upload permission and existing review replies can be resolved independently. After the security tests and normal release qualification, finish ChatGPT, Claude and Muse submissions; finish Cursor once its terms are resolved. Continue already-submitted directories using their existing application IDs.

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
