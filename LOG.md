# LOG — What Happened (index)

> **What this file is:** the index to the append-only action journal. Entries live in monthly files under [context/log/](context/log/) so no single log file gets heavy.
> **Read it:** when you need history — open the relevant month.
> **Write to it:** append one entry to the **current month** ([context/log/2026-06.md](context/log/2026-06.md)) after every create/update/decision. Never edit or delete past entries — append corrections instead. When a month's file passes ~200 lines or the month closes, roll the older entries into `context/log/archive/` and leave a pointer (rollover protocol: [harness-maintenance §11.4](context/playbook/harness-maintenance.md)).
> **Sibling hubs:** [CLAUDE.md](CLAUDE.md) (rules + router) · [PLAYBOOK.md](PLAYBOOK.md) (how-to) · [STATE.md](STATE.md) (current picture) · [USER_PREFS.md](USER_PREFS.md) (how Zack works).

---

## Monthly logs
| Month | File | Status |
|---|---|---|
| June 2026 | [context/log/2026-06.md](context/log/2026-06.md) | current — append here (Clayco load onward) |
| June 2026 · part 1 | [context/log/archive/2026-06-part1.md](context/log/archive/2026-06-part1.md) | archived — Owners/Harvard builds, TEMPLATE work, Consigli saga (06-08 → 06-09) |

_Older entries roll into [context/log/archive/](context/log/archive/) when a month closes or the current file passes ~200 lines._

---

## Entry format
```
### YYYY-MM-DD — <session label>
- HH:MM | <CREATE|UPDATE|DEDUP|DECISION|NOTE> | <entity> | <what + why> | source: <url> | → STATE: <updated?>
```
- **CREATE / UPDATE** — a record written to Notion. Always pair with a STATE index change.
- **DEDUP** — a possible-duplicate found and how it was resolved.
- **DECISION** — a judgment call worth remembering (ambiguous match, schema choice).
- **NOTE** — anything else future-you should know.
