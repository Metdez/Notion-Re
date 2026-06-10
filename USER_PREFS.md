# USER_PREFS — Zack's Preferences

> **What this file is:** a living record of Zack's confirmed preferences, corrections, and workflow habits.
> **Read it:** at the start of every chat, right after STATE.md.
> **Write to it:** whenever Zack corrects an approach, confirms something worked well, or states a preference. Append — never overwrite history.
> **Sibling files:** [CLAUDE.md](CLAUDE.md) (rules + router) · [STATE.md](STATE.md) (what exists) · [PLAYBOOK.md](PLAYBOOK.md) (how-to) · [LOG.md](LOG.md) (history) · [context/MAP.md](context/MAP.md) (the whole file map).

---

## Output & formatting
- Write for a CEO who skims — bullets, short sentences, clear labels.
- No trailing summaries or narration. State results directly.
- Use markdown links for file references, not backticks.
- No emojis unless explicitly requested.

## Data hygiene
- Dedup is non-negotiable. Always check STATE.md index and search Notion before creating.
- Every factual field needs an inline source URL — no source means don't add the fact.
- Copy formatting from existing similar records. Never invent new structure.
- Assign Notion icons (not emojis) to every new page or record.

## Notion workspace
- Primary path: Sales → Market Research → Zack Projects.
- Always use the Notion MCP (`mcp__claude_ai_Notion__*`) for all reads and writes.
- Use `data-source ID` (`collection://…`) for schema reads and property writes. Page URLs are for navigation/linking only.

## Workflow habits
- When starting a task: read STATE.md first, then PLAYBOOK.md recipe. Don't skip this.
- When finished: update STATE.md, then append to LOG.md. Both. Every time.
- When unsure if a record exists: treat it as a possible match and update rather than create.

## Interaction style (derived from session analysis, 2026-06-09)
- **Propose, don't just act.** Zack prefers Claude to state a plan first — he'll approve or redirect before execution. Don't execute structural changes without showing the plan.
- **Interrupts quickly.** If Claude is heading the wrong direction, Zack stops it early. Don't treat silence as approval.
- **Doesn't take "done" at face value.** Zack will push for verification. Don't declare something complete unless it actually is — flag any gaps proactively rather than waiting to be asked.
- **Iterates through rounds.** Tasks often go plan → feedback → adjust → re-execute. This is normal and preferred, not a failure.
- **Safety-alert.** Zack catches and redirects destructive operations. Always flag risky Notion operations before running them (see PLAYBOOK.md §8).

---

## Preference log
> Append entries here as new preferences are confirmed or corrections are made. Most recent at top.

| Date | Preference / correction | Source |
|---|---|---|
| 2026-06-09 | Harness restructured into hub-and-spoke (lazy context). CLAUDE.md = pure router → [context/MAP.md](context/MAP.md). PLAYBOOK/STATE/LOG are thin indexes; real content lives in small interlinked spokes under context/, opened only when needed. Files split when they outgrow ~200 lines (protocol in MAP.md). Nothing deleted — content moved. | Zack request |
| 2026-06-09 | Interaction style encoded from Claude Code session analysis (31 sessions) — propose before acting, flag destructive ops, don't declare done early | /insights report |
| 2026-06-08 | Harness created; preferences seeded from CLAUDE.md global + project rules | Initial setup |
