# Context budget checklist

When a session feels heavy or slow, run `/context` and work down this list:

- [ ] `/compact` to summarise — add `focus: <what to keep>` to steer it
- [ ] `/clear` if the earlier conversation is now irrelevant
- [ ] Drop large `@file` references you no longer need
- [ ] Move standing rules into CLAUDE.md instead of repeating them in chat
- [ ] Delegate bulky exploration to a subagent (its output stays out of your thread)
- [ ] Keep MCP tool search on so schemas load on demand, not all up front
- [ ] Set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` to compact earlier if you prefer

Biggest consumers, roughly in order:
conversation history → MCP tool definitions → large file contents → CLAUDE.md → preloaded skills.
