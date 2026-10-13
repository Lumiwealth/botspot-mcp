# Install the BotSpot hosted MCP in Cline

Use the maintained [setup guide](README.md#connect). BotSpot is a hosted service;
do not clone or execute a local server, install dependencies or run hooks.

1. Open Cline's MCP Servers → Remote Servers.
2. Set Server Name to BotSpot, Server URL to `https://mcp.botspot.trade/mcp`,
   and Transport Type to Streamable HTTP. Add the server.
3. Use Cline's normal OAuth authorization. The user signs into their own
   BotSpot account. Never ask them to paste passwords or tokens into chat.
4. Confirm tools appear. Ask for an account access check and strategy list
   without changes. If sign-in or paid access fails, report that exact result.
5. Follow the [starter workflow](README.md#your-first-useful-result), keeping
   the newest saved revision and the exact returned historical backtest ID.

A paid BotSpot plan is required. The direct MCP includes broader financial
execution capabilities and normal approvals. Do not represent it as read-only
or as an approved marketplace plugin. Do not auto-approve sensitive actions.
No live brokerage action is needed for installation verification.

Installation through Cline and its marketplace remains unqualified; this
document is an instruction source for that test, not evidence that it passed.

Source: https://docs.cline.bot/mcp/mcp-overview .
