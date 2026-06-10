# MAP — The Context System

> **What this file is:** the index of the whole harness. Every other file is reachable from here.
> **Read it:** when you need to find *where* something lives but don't already know the file.
> **Write to it:** whenever a file is added, split, renamed, or moved. **The map must always match the tree** — verify at session start ([harness-maintenance §11.1](playbook/harness-maintenance.md)).

This project spreads its working memory across many small, single-topic files so the agent loads **only what a task needs** — not everything at once. [CLAUDE.md](../CLAUDE.md) is the root router; it points here and nowhere else loads automatically.

---

## How loading works
1. [CLAUDE.md](../CLAUDE.md) is always in context. It carries the rules and points to this map.
2. At chat start, glance at the four **hub** files — they are thin indexes, cheap to read:
   [STATE.md](../STATE.md) · [USER_PREFS.md](../USER_PREFS.md) · [PLAYBOOK.md](../PLAYBOOK.md) · [LOG.md](../LOG.md).
3. **Open a spoke only when the task touches it.** Don't pre-read spokes. Follow the link when you hit the need.
4. After acting, update the spoke(s) you changed, then append to the current log file. See [§ Update protocol](#update-protocol--run-after-every-action).
5. The harness maintains itself: health check, growth, splitting, and drift-repair protocols live in **[playbook/harness-maintenance.md](playbook/harness-maintenance.md)** — open it before creating/splitting any file.

---

## The tree

### Root (rules + thin hubs)
| File | Role | Open when |
|---|---|---|
| [CLAUDE.md](../CLAUDE.md) | Rules + router. Always loaded. | always (automatic) |
| [STATE.md](../STATE.md) | Hub → what exists now | chat start; before any create |
| [USER_PREFS.md](../USER_PREFS.md) | Zack's confirmed preferences | chat start |
| [PLAYBOOK.md](../PLAYBOOK.md) | Hub → how to do the work | when starting a task |
| [LOG.md](../LOG.md) | Hub → history | when you need history |

### Playbook spokes — *how* to do the work
| File | Holds |
|---|---|
| [playbook/loop-and-dedup.md](playbook/loop-and-dedup.md) | The task loop (§0), dedup (§1), create (§2), update (§3) |
| [playbook/schemas.md](playbook/schemas.md) | Field schemas (§4): Owners, Companies, People, Projects, profile-page tables |
| [playbook/conventions.md](playbook/conventions.md) | Icon convention (§5), sourcing format (§6) |
| [playbook/recipes.md](playbook/recipes.md) | Task recipes R1–R6 (§7) |
| [playbook/safety.md](playbook/safety.md) | Pre-write safety protocol (§8) |
| [playbook/notion-mcp.md](playbook/notion-mcp.md) | Notion MCP mechanics & gotchas (§9) |
| [playbook/research-load-prompt.md](playbook/research-load-prompt.md) | Reusable "research → Notion" load prompt (§10) — paste version of `/notion-load` |
| [playbook/harness-maintenance.md](playbook/harness-maintenance.md) | Self-healing protocol (§11): health check, content routing, growth, log rollover, splitting, drift repair, file templates |

### State spokes — *what exists* now
| File | Holds |
|---|---|
| [state/databases.md](state/databases.md) | The 4 databases (IDs, URLs), Owners schema, template page |
| [state/research-files.md](state/research-files.md) | **Ground-truth index:** company → dossier file(s) on disk, loaded-status, ledger links |
| [state/records-harvard.md](state/records-harvard.md) | Harvard ledger: owner, 12 projects, 11 GCs, 27 people, 16 departments |
| [state/records-consigli.md](state/records-consigli.md) | Consigli ledger: 34 projects, 41 people, 21 divisions, cross-linking |
| [state/records-clayco.md](state/records-clayco.md) | Clayco ledger: company, CCDI, 19 divisions, 17 projects, page tables |
| [state/records-zachry.md](state/records-zachry.md) | Zachry Group ledger: company, 7 divisions, 8 people, 12 projects (≠ Zachry Construction Corp) |
| [state/records-dellbrook.md](state/records-dellbrook.md) | Dellbrook \| JKS ledger: company, 3 divisions, 28 projects, 25 people, page tables |
| [state/records-og.md](state/records-og.md) | O&G Industries ledger: company, 7 divisions, 12 projects, page tables |
| [state/records-fontaine.md](state/records-fontaine.md) | Fontaine Bros. ledger: company, 2 divisions, 13 projects, 8 people, page tables |
| [state/pages.md](state/pages.md) | Built pages + view IDs: Harvard Projects, Company-profile TEMPLATE, Consigli profile |
| [state/open-tasks.md](state/open-tasks.md) | Open tasks / in-flight + notes & known gaps |

### Log spokes — *what happened* (append-only)
| File | Holds |
|---|---|
| [log/2026-06.md](log/2026-06.md) | June 2026 journal (current — company loads & audits from 06-09 Clayco onward) |
| [log/archive/2026-06-part1.md](log/archive/2026-06-part1.md) | June 2026 part 1: Owners/Harvard builds, TEMPLATE work, full Consigli saga (06-08 → 06-09) |

### Skills (Claude Code — `.claude/skills/`)
| Skill | Does |
|---|---|
| `/notion-load` | Load a research dossier into Notion (dedup-first, additive, interlink checklist) |
| `/notion-audit` | Read-only parallel audit of a company → verified additive fills only |
⚠ Stray copies of the notion-audit SKILL.md exist at the repo root and in `Enlaye Notion/` — canonical lives in `.claude/skills/`; cleanup flagged in [state/open-tasks.md](state/open-tasks.md).

---

## Update protocol — run after every action
A change that isn't recorded didn't happen.
1. **State:** update the matching `state/` spoke (record index, page layout, open tasks).
2. **Log:** append one entry to the current month's file in `log/` (format in [LOG.md](../LOG.md)).
3. **Procedure changed?** edit the matching `playbook/` spoke.
4. **New preference/correction?** append to [USER_PREFS.md](../USER_PREFS.md).
5. **Added/split/moved a file?** update this map and the relevant hub's link list.
6. **New dossier on disk?** add its row to [state/research-files.md](state/research-files.md).

## Growth & splitting
The harness grows itself — new company → new ledger; new topic → new spoke; file past ~200 lines (or two topics) → split; log past ~200 lines → roll to archive. Full protocols + the file/ledger templates: **[playbook/harness-maintenance.md](playbook/harness-maintenance.md)**.

---

## Conventions for all files
- Every file opens with a `> What this is / Read it / Write to it` header and a sibling-links line ([template](playbook/harness-maintenance.md)).
- Use markdown links for every file/record reference (not backticks) — they're clickable.
- Keep entries CEO-skimmable: bullets, short labels, no filler.
- Names: `area/topic.md`, lowercase kebab-case; ledgers `records-<company-slug>.md`; logs `YYYY-MM.md`. Predictable names make links guessable.
