# Distribution status — October 11, 2026

A compatible MCP connection, a draft, a submitted application, approval and a working public listing are different states. Several older listings advertised retired tools and a free tier, while marketplace applications had not completed the current intake process.

## Verified listings and submissions

| Destination | Current evidence | Remaining work |
| --- | --- | --- |
| [Cursor Directory](https://cursor.directory/plugins/botspot) | Existing community listing corrected and read back publicly. Eight malformed components replaced with one valid HTTP MCP configuration using `https://mcp.botspot.trade/mcp`. Description, paid-plan requirement, source and homepage corrected. | Authenticated Cursor installation still needs qualification. Community listing does not establish acceptance into the curated marketplace. |
| [Grok Build](https://github.com/xai-org/plugin-marketplace/pull/1376) | Catalog PR submitted, source pinned to `a15962339cf94f903c51d9c352c1ed52ebef5915`. Official catalog validator and generated-index check passed. | Maintainer review and merge. Does not prove availability in every Grok product. |
| [MCP Market](https://mcpmarket.com/submit) | Free submission accepted; success message estimates a 4–6 week queue. | Editorial review and live listing. No priority fee purchased. |
| [Cline](https://github.com/cline/mcp-marketplace/issues/1352) | Existing submission corrected; duplicate issue 1316 closed with a pointer to the canonical submission. | Cline-assisted installation qualification and required icon size; maintainer approval. No false installation-test attestation. |
| [Smithery](https://smithery.ai/servers/rob-grzesik/botspot-trading) | Owner updated title, description, homepage and source. New registration uses `/mcp` and discovers OAuth metadata. | Scanner requires authorization to discover tools. Public page still reports no capabilities/deployments. Use dedicated reviewer access, not customer credentials. |
| [Glama](https://glama.ai/mcp/connectors/io.github.grzesir/botspot-trading) | Existing listing observed live as unhealthy, with OAuth not checked. Correction report submitted through listing UI. | Ownership requires domain proof. Metadata and authenticated health remain unresolved; a report is not a repaired listing. |

## Prepared applications with blockers

- **Claude:** current developer portal displayed zero submissions in the inspected account. A July 31 message closed the older queue and requested resubmission. New connector fields prepared, not submitted. Financial-execution restrictions, reviewer access, testing and compliance attestations remain unresolved.
- **ChatGPT / OpenAI / Codex:** inspected BotSpot project displayed no plugin drafts. Upload blocked by a developer-identity gate, even though verification shows an approved individual identity. Resolve this portal inconsistency before assuming new identity submission is necessary. Review also needs domain verification, dedicated reviewer access, demo, five positive and three negative cases, and eligible financial scope. Local package tests do not establish store compliance or approval.
- **Cursor curated marketplace:** publisher application fields prepared, not submitted. Publisher Terms acceptance pending. Section 3.1 prohibits plugin monetization, including indirect fees; applicability to this paid hosted connector needs resolution.
- **Muse:** connector fields prepared, not submitted. Finance policy allows financial reads but excludes initiating money movement/trade orders. Reviewer access, demo, required icon and developer terms pending. Browser file upload also requires the Chrome extension file-access setting, which is currently disabled. Payment answer discloses existing checkout-link capability.

## Other directories

- **Official MCP Registry:** existing version 1.1.0 confirmed in the public browser search. Corrected version 1.1.1 published with the official publisher and read back through the latest-version API as active and latest. Namespace remains `io.github.grzesir/botspot-trading`; source now points to this maintained public package. Paid access, current capabilities and the correct endpoint are stated. `server.json` in this repository is the corrected publisher input; older Node submission notes are historical.
- **PulseMCP:** live search returned no BotSpot result. Site reports new submissions and listing changes paused.
- **mcp.so:** submission page exposes a $39 fee. No purchase made.
- **Appz:** older receipt identifies `https://appz.com/apps/botspot`; current page and ownership could not be verified.
- **Grok Bot:** no verified separate public intake route found. Grok Build tracked separately.

## Financial eligibility

Live protected-resource discovery advertises `place_trade` and `start_deployment`, alongside research, file editing, backtests and monitoring. OpenAI, Anthropic and Muse restrict financial execution in their public directories. Descriptions or narrower requested OAuth scopes alone do not establish eligibility.

A store-specific integration needs real authorization boundaries, tested denial of prohibited actions, dedicated reviewer access and honest paid-access disclosure. Do not hide tools with runtime intent filters, make unsupported compliance attestations, or call the full direct connector read-only. No product behavior or production deployment changed in this audit.

## Official requirements

- OpenAI: https://developers.openai.com/plugins/deploy/submission and https://developers.openai.com/plugins/plugin-guidelines
- Claude: https://claude.com/docs/directory/publish and https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy
- Cursor: https://cursor.com/docs/reference/plugins and https://cursor.com/marketplace-publisher-terms
- Muse: https://muse.ai/platform/docs
- Grok Build: https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md
- Cline: https://github.com/cline/mcp-marketplace

Public product facts only. Reviewer credentials, mail bodies and customer data stay outside source control. No recurring monitoring schedule attached.
