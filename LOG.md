# LOG — What Happened (index)

> **What this file is:** the index to the append-only action journal. Entries live in monthly files under [context/log/](context/log/) so no single log file gets heavy.
> **Read it:** when you need history — open the relevant month.
> **Write to it:** append one entry to the **current month** ([context/log/2026-06.md](context/log/2026-06.md)) after every create/update/decision. Never edit or delete past entries — append corrections instead. When a month's file passes ~200 lines or the month closes, roll it into `context/log/archive/` and start the next month (see [context/MAP.md](context/MAP.md)).
> **Sibling hubs:** [CLAUDE.md](CLAUDE.md) (rules + router) · [PLAYBOOK.md](PLAYBOOK.md) (how-to) · [STATE.md](STATE.md) (current picture) · [USER_PREFS.md](USER_PREFS.md) (how Zack works).

---

## Monthly logs
| Month | File | Status |
|---|---|---|
| June 2026 | [context/log/2026-06.md](context/log/2026-06.md) | current — append here |

_Past months roll into [context/log/archive/](context/log/archive/) as they close._

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
