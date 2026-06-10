# MAP — The Context System

> **What this file is:** the index of the whole harness. Every other file is reachable from here.
> **Read it:** when you need to find *where* something lives but don't already know the file.
> **Write to it:** whenever a file is added, split, renamed, or moved. The map must always match the tree.

This project spreads its working memory across many small, single-topic files so the agent loads **only what a task needs** — not everything at once. [CLAUDE.md](../CLAUDE.md) is the root router; it points here and nowhere else loads automatically.

---

## How loading works
1. [CLAUDE.md](../CLAUDE.md) is always in context. It carries the rules and points to this map.
2. At chat start, glance at the four **hub** files — they are thin indexes, cheap to read:
   [STATE.md](../STATE.md) · [USER_PREFS.md](../USER_PREFS.md) · [PLAYBOOK.md](../PLAYBOOK.md) · [LOG.md](../LOG.md).
3. **Open a spoke only when the task touches it.** Don't pre-read spokes. Follow the link when you hit the need.
4. After acting, update the spoke(s) you changed, then append to the current log file. See [§ Update protocol](#update-protocol).

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
| [playbook/schemas.md](playbook/schemas.md) | Field schemas (§4): Owners, Companies, People |
| [playbook/conventions.md](playbook/conventions.md) | Icon convention (§5), sourcing format (§6) |
| [playbook/recipes.md](playbook/recipes.md) | Task recipes R1–R6 (§7) |
| [playbook/safety.md](playbook/safety.md) | Pre-write safety protocol (§8) |
| [playbook/notion-mcp.md](playbook/notion-mcp.md) | Notion MCP mechanics & gotchas (§9) |

### State spokes — *what exists* now
| File | Holds |
|---|---|
| [state/databases.md](state/databases.md) | The 4 databases (IDs, URLs), Owners schema, template page |
| [state/records-harvard.md](state/records-harvard.md) | Harvard owner, 12 projects, 11 GCs, 27 people, 16 departments |
| [state/records-consigli.md](state/records-consigli.md) | Consigli profile build: 19 projects, 21 people, cross-linking |
| [state/pages.md](state/pages.md) | Built pages: Harvard Projects, Company-profile TEMPLATE, Consigli profile |
| [state/open-tasks.md](state/open-tasks.md) | Open tasks / in-flight + notes & known gaps |

### Log spokes — *what happened* (append-only)
| File | Holds |
|---|---|
| [log/2026-06.md](log/2026-06.md) | June 2026 action journal (current) |
| `log/archive/` | Past months, rolled here once a month closes |

---

## Update protocol — run after every action
A change that isn't recorded didn't happen.
1. **State:** update the matching `state/` spoke (record index, page layout, open tasks).
2. **Log:** append one entry to the current month's file in `log/` (format in [LOG.md](../LOG.md)).
3. **Procedure changed?** edit the matching `playbook/` spoke.
4. **New preference/correction?** append to [USER_PREFS.md](../USER_PREFS.md).
5. **Added/split/moved a file?** update this map and the relevant hub's link list.

---

## Splitting protocol — keep every file short
The point of this system is that no single file is heavy to load. When a file grows past a comfortable read, split it.

**Trigger:** a spoke crosses **~200 lines** (or covers two clearly separate topics, whichever comes first).

**How to split:**
1. Pick the natural seam (a heading, an entity, a date range).
2. Create a new sibling spoke with a clear kebab-case name (e.g. `state/records-consigli.md` → split off `state/records-consigli-projects.md`).
3. **Move** the content — never retype, never drop a line. Cut from the old file, paste into the new.
4. Replace the moved block in the old file with a one-line pointer — a real markdown link to the new file plus a note of what it holds (e.g. `→ moved to context/state/records-consigli-projects.md — the 19 projects`).
5. Add the new file to this map's tree and to its hub's link list.
6. Cross-link: the new file links back to its hub and to siblings it references.

**Naming:** `area/topic.md`, lowercase, hyphens. Logs are `YYYY-MM.md`. Keep names predictable so links are guessable.

**Never delete content when splitting.** Splitting moves; it does not prune. If something is truly obsolete, move it to an archive note and log why — don't silently remove it.

---

## Conventions for all files
- Every file opens with a `> What this is / Read it / Write to it` header and a sibling-links line.
- Use markdown links for every file/record reference (not backticks) — they're clickable.
- Keep entries CEO-skimmable: bullets, short labels, no filler.
