# Playbook · Loop & Dedup (§0–§3)

> **Holds:** the task loop, the dedup procedure, and the create/update procedures — the core of every task.
> **Part of:** [PLAYBOOK.md](../../PLAYBOOK.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [schemas](schemas.md) · [conventions](conventions.md) · [recipes](recipes.md) · [safety](safety.md) · [notion-mcp](notion-mcp.md)

---

## 0. The loop (run this every task)
1. **Read** [STATE.md](../../STATE.md) — know what already exists and what's in flight.
2. **Match** the task to a recipe in [recipes.md](recipes.md).
3. **Dedup** — §1 below, always, before any create.
4. **Pass the [Write Gate](write-gate.md) (§12)** — before the first Notion write, state the 4 gate lines to Zack and get each to ✅. No write tool runs until it passes.
5. **Act** via Notion MCP (`mcp__claude_ai_Notion__*`).
6. **Record** — update the matching [state spoke](../state/) , then append to the current [log](../log/2026-06.md). Non-optional.

---

## 1. Dedup procedure (non-negotiable — run before EVERY create)
1. Check the record index in the relevant [state spoke](../state/) for the name/domain/person.
2. `mcp__claude_ai_Notion__notion-search` the target database for the entity.
3. Match on: company → name **and** domain; person → name **and** company/email.
4. **If found:** update the existing record (§3). Never create a second.
5. **If unsure:** treat as a possible match, update rather than create, and note the ambiguity in the [log](../log/2026-06.md).
6. **Only if truly absent:** create (§2).

---

## 2. Creating a record
- Confirm dedup (§1) returned nothing first, and the [Write Gate §12](write-gate.md) passed.
- Assign a **Notion icon** (not an emoji) — see [conventions](conventions.md) §5.
- Fill fields per the schema in [schemas.md](schemas.md). Every factual field carries an inline source URL ([conventions](conventions.md) §6).
- Keep copy CEO-skimmable: bullets, short labels, no filler.
- After create → add to the index in the matching [state spoke](../state/) + append to the [log](../log/2026-06.md).

---

## 3. Updating / enriching a record
- Pass the [Write Gate §12](write-gate.md) first — esp. line 1 (identity) and line 2 (additive-only).
- Fetch the live record first (`notion-fetch`) — don't overwrite blind.
- Add only new, sourced facts. Don't duplicate a fact already present.
- Preserve existing sources; append new ones inline ([conventions](conventions.md) §6).
- After update → bump the entry in the matching [state spoke](../state/) + append to the [log](../log/2026-06.md).
