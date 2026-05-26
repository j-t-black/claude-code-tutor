---
id: advanced-mcp
title: "MCP servers"
tier: advanced
order: 25
tags: [advanced, mcp, integrations]
version_added: "0.1"
updated: "2026-05-26"
---

# MCP (Model Context Protocol) servers

MCP is how Claude Code talks to **external systems** — GitHub, Slack, databases,
your cloud provider — by connecting to *servers* that expose **tools**,
**resources**, and **prompts**. Add one with `claude mcp add --transport
[stdio|sse|http] <name> <endpoint>` (local stdio scripts or remote HTTP services),
or manage and authenticate connections with **`/mcp`**.

Two things worth knowing early: tool schemas are **deferred by default** (only
names load up front, full definitions on demand) so a big server doesn't bloat
your context; and you can pull a server's resource into a prompt with
`@server:protocol://path`. MCP is the main way you extend what Claude can *reach*.
