# Enlaye to Notion

Enlaye is an AI B2B SaaS. they sell construction tech software for risk magenment. Their target audeince is huge GC's.

## Notion Workspace
- **Path:** Sales → Market Research → Zack Projects
- **Company Database** — company records
- **People Database** — contact/relationship records

## Rules
- **No duplicates.** When adding data Search before creating. If a record exists, update it.
- **Sourced data only.** Every field added must include an inline URL to the source.
- **Brevity.** Bullet points, short sentences. Written for a CEO who skims.
- **Emojis.** Always assign a Notion icon  to new pages/records, make sure they vary and there is some varients to them.
- **Data.** When it comes to adding data. Look at otehr records similar to see how they are formatted and copy the formating, you should not be creating the structure of data.

## Notion Safety
- **Non-destructive by default.** Prefer additive operations (new views, tables, fields). Never use `replace_content` or create new databases without explicit confirmation from Zack.
- **Plan before acting.** Before any structural Notion change, state the full list of operations and flag anything destructive in bold. Wait for confirmation before executing.
- **Notion-first.** Content lives in the connected Notion workspace. Always check Notion via MCP before searching the local filesystem or Desktop files.
- **Schema matching.** When building or extending databases, match the field detail of an existing comparable database (e.g. Companies DB). Do not over-build or strip fields — mirror what's already there.

## MCP
Notion is connected via MCP (`mcp__claude_ai_Notion__*`). Use it for all reads and writes.

---

## The Harness — your working memory
This file holds the rules and routes you to everything else. It does **not** hold live data, and it does **not** ask you to read every file up front. The working memory is spread across many small, interlinked files so you load only what a task needs. The full map is **[context/MAP.md](context/MAP.md)** — go there to find where anything lives.

The map's top level is four thin **hub** files (cheap to glance at; each links down to small spokes you open only when needed):

| Hub | Routes you to | Glance when |
|---|---|---|
| [STATE.md](STATE.md) | what exists now — databases, record ledgers, pages, open tasks | chat start; before creating anything |
| [USER_PREFS.md](USER_PREFS.md) | how Zack works — confirmed preferences & corrections | chat start |
| [PLAYBOOK.md](PLAYBOOK.md) | how to do the work — procedures, schemas, recipes, safety, MCP gotchas | when a task arrives |
| [LOG.md](LOG.md) | what happened — append-only journal, by month | when you need history |

**How to work:** glance at the four hubs, then follow links into [context/](context/) **only as the task requires** — don't pre-read spokes. Before any create, dedup ([context/playbook/loop-and-dedup.md](context/playbook/loop-and-dedup.md) §1). After any write, update the matching state spoke and append to the current log. A change that isn't recorded didn't happen; this is how the rules above (no duplicates, sourced data, brevity, icons) get enforced.

**The harness maintains itself** — full protocol in [context/playbook/harness-maintenance.md](context/playbook/harness-maintenance.md):
- **Session start:** 30-second health check — current log under ~200 lines, [context/MAP.md](context/MAP.md) matches the file tree, STATE snapshot has a row per ledger. Fix drift before working.
- **New topic → new file.** New company → create its `context/state/records-<slug>.md` ledger *before* the first Notion write; new procedure area → new playbook spoke. Register every new file in MAP + its hub + the log in the same session — an unregistered file doesn't exist.
- **Full file → split it.** Past ~200 lines (or two topics in one file), move the older/secondary content to a new spoke, leave a pointer, update the map. Move — never retype, never prune.
- **Finding more context:** the company → research-dossier index is [context/state/research-files.md](context/state/research-files.md); each ledger names its ground-truth files in its header.

### Bulk parallel import — the fan-out environment
For large list imports (thousands of records), there's a self-contained, resumable harness at **[Big Data/_import-harness/](Big%20Data/_import-harness/)** that lets up to **18 agents import in parallel**, each owning one batch and writing progress constantly so any interruption is recoverable.
- **Start here:** [Big Data/_import-harness/README.md](Big%20Data/_import-harness/README.md) — how to dispatch, resume, and loop-until-done.
- **Coordinator view:** [BOARD.md](Big%20Data/_import-harness/BOARD.md) — status of all 18 batches; relaunch anything `pending` or stale.
- **Per-agent instructions:** [agent-brief.md](Big%20Data/_import-harness/agent-brief.md) — one agent = one batch = one ledger; dedup-first, additive, sourced.
- **Per-batch ledgers:** `Big Data/_import-harness/ledgers/batch-NN.md` — per-file checkboxes + a resume cursor (`file X, row R`) updated after every record. **The ledger is the source of truth**, not the agent's memory.
- **How it's crash-safe:** one agent per batch = zero write-collisions; the cursor + LinkedIn dedup key make every record idempotent, so a re-run skips done work and resumes mid-file. Throttle the parallel count if Notion rate-limits — the harness is agnostic to how many run at once.
