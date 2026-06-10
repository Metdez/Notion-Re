# Playbook · Harness Maintenance (§11) — the self-healing protocol

> **Holds:** how the harness keeps itself healthy — the health check, the growth protocol (when to create a new file), the splitting protocol (when a file gets too big), log rollover, and drift repair. This is what makes the system self-expanding instead of self-clogging.
> **Part of:** [PLAYBOOK.md](../../PLAYBOOK.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [loop-and-dedup](loop-and-dedup.md) · [schemas](schemas.md) · [conventions](conventions.md) · [recipes](recipes.md) · [safety](safety.md) · [notion-mcp](notion-mcp.md)
> **Read it:** at the start of any session that will write files, and any time you're about to add content and aren't sure *where* it goes.

---

## 11.0 The principle
The harness only works if every file stays **small, single-topic, and findable from [MAP.md](../MAP.md)**. Content always has exactly one home; everything else points to it. When new information arrives, the question is never "should I record this?" (always yes) — it's "**which file owns this, and does that file still have room?**"

---

## 11.1 Session-start health check (cheap — ~30 seconds)
Run when a session begins real work. Three checks:
1. **Log size:** `wc -l context/log/<current-month>.md` — over ~200 lines → roll it (§11.4) *before* appending today's entries.
2. **Map freshness:** does every file in `context/` appear in [MAP.md](../MAP.md)'s tree, and vice versa? (`ls context/state context/playbook context/log`) — a file the map doesn't list is invisible to future sessions. Fix immediately.
3. **State snapshot:** does the [STATE.md](../../STATE.md) snapshot table have a row for every `records-*.md` ledger? Missing row → add it.
If any check fails, fix it first and log a one-line `MAINT` entry. Drift compounds; a 2-minute fix now saves a confused session later.

## 11.2 Where does new content go? (routing decision)
When you have something to record, route it top-down:
| It is… | It goes in… |
|---|---|
| A fact about what now exists in Notion (record IDs, schema changes, page layouts) | the matching `state/records-<company>.md` ledger, or [state/databases.md](../state/databases.md) / [state/pages.md](../state/pages.md) |
| A new company's first records | a **new** `state/records-<company-slug>.md` ledger (§11.3) |
| What you did and why (actions, decisions, dedups) | the current month's log — entries reference state, never replace it |
| A reusable procedure / a task that recurred | [recipes.md](recipes.md) (new numbered recipe) — or a new playbook spoke if it's a whole new topic (§11.3) |
| An MCP gotcha / mechanic learned the hard way | [notion-mcp.md](notion-mcp.md) |
| A schema fact (property name, type, quirk) | [schemas.md](schemas.md) |
| A Zack preference or correction | [USER_PREFS.md](../../USER_PREFS.md) preference log |
| A pending manual step or known gap | [state/open-tasks.md](../state/open-tasks.md) |
| A new research dossier file arrived on disk | register it in [state/research-files.md](../state/research-files.md) |
**Never** put live data in a hub (CLAUDE/STATE/PLAYBOOK/LOG are indexes) and never record the same fact in two homes — record once, link from elsewhere.

## 11.3 Growth protocol — when to CREATE a new file
Create a new spoke the moment content has **no existing single-topic home**. Don't wedge a new topic into a nearby file "for now" — that's how files bloat and topics get lost. Triggers:
- **New company enters the pipeline** → create `context/state/records-<company-slug>.md` from the ledger template (§11.6) **before** the first Notion write. Register it in three places: MAP tree · STATE spoke table + snapshot row · this month's log.
- **New recurring topic in procedures** (e.g. a future "outreach sequencing" or "Instantly campaign" workflow) → new `context/playbook/<topic>.md`, one row in PLAYBOOK.md, one row in MAP.
- **New category of state** (e.g. campaigns, meeting notes) → new `context/state/<topic>.md`, registered the same way.
- **A spoke is straining** — you keep scrolling past unrelated sections to find things → split (§11.5) even if under 200 lines. Two topics in one file is the trigger; the line count is just the backstop.
Every new file starts with the standard header (§11.6) and gets registered in **MAP + its hub + the log** in the same session it's created. An unregistered file doesn't exist.

## 11.4 Log rollover
- **Monthly:** when the month closes, move `context/log/YYYY-MM.md` → `context/log/archive/` and start the new month's file.
- **Mid-month overflow:** past ~200 lines, move the **older** entries (whole dated sections, top of file) to `context/log/archive/YYYY-MM-partN.md`; leave a one-line pointer under the current file's header saying what moved and where. Newest entries always stay in the current file. (Done 2026-06-09: [archive/2026-06-part1.md](../log/archive/2026-06-part1.md).)
- Update LOG.md's monthly table with each archive file.

## 11.5 Splitting protocol — when a file gets too big
**Trigger:** a spoke crosses **~200 lines**, or covers two clearly separate topics — whichever comes first.
1. Pick the natural seam (a heading, an entity, a date range).
2. Create the new sibling spoke with a predictable kebab-case name (e.g. `records-consigli.md` → `records-consigli-projects.md`).
3. **Move** the content — cut and paste, never retype, never drop a line.
4. Replace the moved block with a one-line markdown-link pointer (what moved + where).
5. Register the new file: MAP tree + hub link table + a log line.
6. Cross-link: new file's header points back to its hub and the siblings it references.
**Splitting moves; it never prunes.** Truly obsolete content goes to an archive file with a log entry explaining why — never silently deleted.

## 11.6 Templates for new files

**Standard spoke header** (every file in `context/`):
```markdown
# <Area> · <Topic>

> **Holds:** <one line — what single topic this file owns>
> **Part of:** [<HUB>.md](../../<HUB>.md) · map: [MAP.md](../MAP.md)
> **Siblings:** <links to the spokes it most often pairs with>
> **Read it:** <when a future session should open this file>
```

**New company ledger** (`context/state/records-<slug>.md`):
```markdown
# State · Records — <Company> Build

> **Holds:** the <Company> dedup ledger — company record, divisions, people, projects, page tables.
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md)
> **Ground truth:** `Enlaye Notion/<folder>/<dossier file(s)>` (also indexed in [research-files.md](research-files.md))
> **⚠ Disambiguation / conflicts:** <name collisions, kept conflicts — or "none">

**Profile page:** <name + page ID + icon + local collection IDs>
**Company record:** <Companies DB row ID + which properties were filled>
**Schema ALTERs:** <non-destructive option additions made for this build>
**Divisions / People / Projects:** <tables with Notion IDs — every created record gets its ID here>
**Left empty (no source):** <the dossier-gaps list — so audits don't re-chase them>
**Still manual in Notion UI:** <view filters etc. MCP can't set>
```

## 11.7 Drift repair
- **STATE vs Notion:** Notion wins. Re-fetch, reconcile the ledger, log a `MAINT` correction.
- **MAP vs tree:** the tree wins (files are reality); update the map, then check the hub tables too.
- **Two files claiming the same topic:** merge into the older home, leave a pointer in the other, log it.
- **Concurrent-session collisions** (it has happened 3+ times — see log): before writing a file another session may touch, re-read it right before the edit; on conflict, union the content, never clobber.
