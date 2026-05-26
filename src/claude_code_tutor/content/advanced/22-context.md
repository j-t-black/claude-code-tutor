---
id: advanced-context
title: "Context management"
tier: advanced
order: 22
tags: [advanced, context]
version_added: "0.1"
updated: "2026-05-26"
---

# Context management

The context window is Claude's working memory for a session — every file,
message, tool definition, and memory competes for the same finite space. As it
fills, responses can slow and quality can drift ("context rot"). Managing it well
is one of the biggest levers on getting good results.

The toolkit: `/context` to *see* the breakdown, `/compact` to summarise, `/clear`
to reset, plus habits like referencing only the files you need and keeping tool/MCP
overhead lean. Subagents help too, by keeping bulky exploration out of the main thread.

> **Flagship lesson — coming in M2**, building on the [[slash-context]] basics.
