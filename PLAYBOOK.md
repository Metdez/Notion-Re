# PLAYBOOK — How To Do The Work (index)

> **What this file is:** the index to the operating manual. *How* every task gets done. The procedures themselves live in small spokes under [context/playbook/](context/playbook/) — open the one your task needs, don't read them all.
> **Read it:** when starting a task, to find the matching procedure.
> **Write to it:** when a procedure changes, edit the spoke; add a new spoke (and a row here) when a topic outgrows its file — see the splitting protocol in [context/MAP.md](context/MAP.md).
> **Sibling hubs:** [CLAUDE.md](CLAUDE.md) (rules + router) · [STATE.md](STATE.md) (what exists now) · [LOG.md](LOG.md) (what happened) · [USER_PREFS.md](USER_PREFS.md) (how Zack works).

---

## Procedure spokes
| § | Spoke | Open when |
|---|---|---|
| §0–§3 | [loop-and-dedup](context/playbook/loop-and-dedup.md) | every task — the loop, dedup, create, update |
| §4 | [schemas](context/playbook/schemas.md) | filling fields — Owners / Companies / People schemas |
| §5–§6 | [conventions](context/playbook/conventions.md) | choosing an icon or sourcing a fact |
| §7 | [recipes](context/playbook/recipes.md) | a recurring task (R1–R6: owners, projects, GCs, departments, hub pages) |
| §8 | [safety](context/playbook/safety.md) | **before any structural Notion change** |
| §9 | [notion-mcp](context/playbook/notion-mcp.md) | **before writing to Notion** — relations, icons, newlines, view DSL, nested DBs |
| §10 | [research-load-prompt](context/playbook/research-load-prompt.md) | loading a new company's research dossier — reusable copy-paste prompt (skill version: `/notion-load`) |
| §11 | [harness-maintenance](context/playbook/harness-maintenance.md) | **the self-healing protocol** — session health check, where new content goes, when to create/split files, log rollover, drift repair, file templates |

## The loop, in one line
Read [STATE.md](STATE.md) → match a [recipe](context/playbook/recipes.md) → [dedup](context/playbook/loop-and-dedup.md) → act via Notion MCP → record in the matching [state spoke](context/state/) + the current [log](context/log/2026-06.md). Full version: [loop-and-dedup §0](context/playbook/loop-and-dedup.md). Writing files? Route content per [harness-maintenance §11.2](context/playbook/harness-maintenance.md).
