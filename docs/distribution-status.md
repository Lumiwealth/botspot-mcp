# Distribution status — October 11, 2026

[Execution game plan](distribution-game-plan.md): preserve the direct MCP and qualify installation-specific permissions before finishing store reviews.

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

## Financial eligibility — clarified October 12, 2026

The earlier blanket statement that trading is banned in ChatGPT was too broad. OpenAI's current plugin guidelines prohibit execution of money transfers, crypto transfers and investment trades. Alpaca provides a concrete public-directory precedent for simulated trading and live-account reporting:

| Alpaca ChatGPT plugin | Published capabilities |
| --- | --- |
| Paper Trading | Account/market reads and simulated order placement. |
| Live | Live-account reporting and market research; cannot submit, modify or cancel live orders. |

Sources: [Alpaca launch article, October 12](https://alpaca.markets/blog/paper-trading-and-live-portfolio-monitoring-now-available-in-chatgpt-with-alpaca/), [OpenAI's Alpaca listing](https://openai.com/business/plugins/alpaca/) and [OpenAI plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines). The OpenAI listing also includes an ambiguous order-placement example while directing execution to Alpaca's own API/dashboard. Alpaca's explicit published capability limits establish the distinction; that example alone does not establish live-order permission.

**BotSpot submission approach:** pursue a package for strategy development, historical backtesting, paper trading and live-account reporting. Alpaca's approval is a precedent, not a guarantee of BotSpot approval. Verify supported capabilities and enforce real authorization/account-mode boundaries before claiming eligibility. Seek specific clarification before including real-money order submission, modification/cancellation, or deployment that initiates live trading.

Live BotSpot protected-resource discovery advertises `place_trade` and `start_deployment`. Descriptions or narrower requested OAuth scopes alone do not make that full connector eligible. Use dedicated reviewer access, tested denials of prohibited actions and honest paid-access disclosure. Do not hide tools with runtime intent filters or make unsupported compliance attestations. This clarification changes the submission plan, not product behavior or production deployment. Claude and Muse requirements remain separate; Alpaca's ChatGPT listing does not establish their approval.

## Official requirements

- OpenAI: https://developers.openai.com/plugins/deploy/submission and https://developers.openai.com/plugins/plugin-guidelines
- Claude: https://claude.com/docs/directory/publish and https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy
- Cursor: https://cursor.com/docs/reference/plugins and https://cursor.com/marketplace-publisher-terms
- Muse: https://muse.ai/platform/docs
- Grok Build: https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md
- Cline: https://github.com/cline/mcp-marketplace

Public product facts only. Reviewer credentials, mail bodies and customer data stay outside source control. No recurring monitoring schedule attached.


## Continuation: October 12 UTC / October 11 Toronto

- **Official MCP Registry:** public latest-version API re-read; version 1.1.1 is active and latest, with paid access and trading disclosed. No duplicate listing.
- **Cursor curated marketplace:** complete application sent to the documented marketplace-publishing@cursor.com address. Repository, endpoint, privacy, terms, brand asset and paid/trading capabilities were included. The direct/indirect fee restriction was explicitly disclosed and review requested. Gmail Sent independently confirmed delivery into the sender's Sent folder. This is an email application, not a portal submission, terms acceptance or marketplace approval.
- **Anthropic:** complete application and request for written financial-capability permission sent to directory@anthropic.com, the contact published in current directory documentation. Gmail Sent independently confirmed. The repository route validated source 7c6d0e7, with image-file policy holds permitted to proceed to human review. The portal's compliance warranty remains unsigned; no claim that trade-order tools meet policy section 4.A was made. The separate remote-connector route requires a connected account before advancing. Neither route has a completed portal submission.
- **Package metadata:** version 1.0.2 explicitly declares the BotSpot display name, icon, privacy, support, documentation and terms destinations, with paid access and trading in its description. A square icon was regenerated through the approved Image Generator and used without edits. All eight packaging tests pass, including true square dimensions, file-size limits and credential-free public configuration. An earlier metadata commit reached main while its new square-size test failed; the immediate corrective commit fixed the asset and passed that unchanged test.
- **Smithery:** publication restarted with https://mcp.botspot.trade/mcp. The scanner authorization URL was blocked by the connected Chrome client (ERR_BLOCKED_BY_CLIENT). The prior release timed out during authentication. A new attempt is not a successful deployment or discovered capabilities.
- **OpenAI:** the upload gate still says Complete identity verification. Organization settings show Individual Approved under Verified. This inconsistency was reproduced; no new business identity information or credentials were entered. Review eligibility remains separate from this technical gate.
- **Muse:** overview fields completed, including payment/paid access and full trading/deployment disclosure. The API upload requires the Chrome extension's disabled file-URL permission; the native picker left Open disabled. The form additionally requires a 512x512 PNG/SVG no larger than 256 KiB. Existing and generated eligible square PNG files exceed that byte limit; no prohibited manual image repair was used. Not submitted.
- **Grok Build / Cline / MCP Market:** prior submissions retained without duplication. Grok PR 1376 and Cline issue 1352 remain open. MCP Market has its previously recorded free-queue receipt.

Private mail bodies, message identifiers, browser evidence and credentials remain outside this public repository. Received applications, reviewer permission, store approval, publication and actual installation are separate states.


## Additional distribution: October 12, 2026

- **mcpservers.org:** submitted the free application through the public form. The success page identified BotSpot and stated review within two weeks, with email notification after approval. Finance category, OAuth, the exact hosted endpoint, Registry name, paid account requirement and user-approved trading were disclosed. No priority fee purchased. This is a received submission, not a live listing. Official intake: https://mcpservers.org/submit .
- **MCP.Directory:** submitted the maintained public package with an explicit paid-access and trading description. The success page stated Server Submitted and review/publication within 24 hours. Do not treat the provider's estimated timeline as approval or a confirmed live listing. Official intake: https://mcp.directory/submit .
- **Awesome Remote MCP Servers:** submitted https://github.com/jaw9c/awesome-remote-mcp-servers/pull/1260 after reviewing current contribution rules. The older PR 253 was closed by the maintainer on June 23 and contained stale free-tier, fixed tool-count and broker claims. The new one-line entry uses the current URL, OAuth 2.1, category Other and the official maintainer. Its body discloses paid access and user-approved trading; authenticated installation and uptime benchmarks are not invented. Maintainer review is pending.
- **Anthropic:** an automated acknowledgement confirmed the emailed application is queued. This is neither a completed portal submission nor store approval.
- **OpenAI:** a separate publishing-identity support conversation was escalated to a specialist and checked again. It is unrelated to any other support case. The current official requirements distinguish verified individual publishers from business-name publishers; business verification is not shown as completed in the inspected account. No new identity documents were submitted.
- **Smithery:** official publishing documentation describes a static public server card at /.well-known/mcp/server-card.json for cases where authenticated scanning cannot complete. This is a documented engineering route to investigate, not a claim that the card has shipped or that the failed scan succeeded. Source: https://smithery.ai/docs/build/publish .
- **Additional curation rules checked:** punkpeye's standard list directs hosted-only servers to its remote list; that remote list requires a live Glama connector and endpoint checks. modelcontextprotocol/servers no longer accepts third-party listing PRs and directs them to the official Registry. wong2/awesome-mcp-servers directs submissions to mcpservers.org; it does not accept listing PRs. No duplicate or out-of-scope reference-server PR was filed.

Public authentication-discovery preflight on October 12: unauthenticated initialize at https://mcp.botspot.trade/mcp returned HTTP 401 with a Bearer resource_metadata challenge; protected-resource metadata returned HTTP 200 and identified the OAuth authority. This proves public discovery behavior, not authenticated user installation or tool execution. Screenshots and private application/support identifiers remain outside source control.


### Muse icon follow-through

Rob explicitly authorized a format-only exception to the generator-only image rule for this exact Muse logo on October 12. The approved generated brand image was resized to 512x512 and PNG-compressed, without adding creative content; the final file is 136,288 bytes, below 256 KiB. The image was visually inspected. The automated upload still reports that the ChatGPT Chrome extension requires Allow access to file URLs. Native file-picker attempts did not produce a received icon in Muse. No browser permission was changed. The overview remains unsubmitted pending the actual upload and subsequent technical/review stages. The required icon is prepared; resizing is no longer a blocker.
