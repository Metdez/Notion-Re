# Playbook · Task Recipes (§7)

> **Holds:** repeatable recipes, one per recurring task. Add a numbered recipe the first time a task recurs; keep each a tight checklist.
> **Part of:** [PLAYBOOK.md](../../PLAYBOOK.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [loop-and-dedup](loop-and-dedup.md) · [schemas](schemas.md) · [conventions](conventions.md) · [safety](safety.md) · [notion-mcp](notion-mcp.md)

> Every recipe assumes the loop ([loop-and-dedup](loop-and-dedup.md) §0) and dedup (§1). "Record in STATE + LOG" means the matching [state spoke](../state/) + the current [log](../log/2026-06.md).

### R1 — Move an Enlaye entity into Notion
1. Loop §0 → dedup §1 → create §2 or update §3.
2. Source every field §6, assign icon §5 ([conventions](conventions.md)).
3. Record in STATE + LOG.

### R2 — Add an owner (Owners DB)
1. Dedup §1 against the Owners DB (name) before creating.
2. Create from the "⟨Owner Name⟩ — TEMPLATE" page (duplicate it) so the body sections are pre-built.
3. Set fields per [schemas](schemas.md); set Priority + Status for the outreach pipeline.
4. Link **Projects**, **Key Contacts**, **General Contractors** relations (search those DBs; reuse existing records, don't create dupes).
5. Source every fact inline §6; assign a Notion icon §5.
6. Record in STATE + LOG.

### R3 — Add a construction project (Construction Projects DB)
1. Dedup §1 (search the Projects data source by name).
2. Create via `notion-create-pages` (parent = `data_source_id` `4c8ed827-…`). Notion icon `/icons/building_<color>.svg`.
3. Fields: `Name` · `Type` (select) · `Status` (status) · `Location` (multi-select, JSON-array string) · `Contrat Value in Million` (number, only if disclosed) · `date:Date:start` (start date) · `Size` (text scope summary) · `userDefined:URL` (primary source) · `Owner` (relation, page URL) · `Contractors` (relation, JSON-array of GC page URLs).
4. Body (copy the "Bard College Passive House Dorms" record): `**Project Brief**` (scope, owning Harvard dept, GC, architects as text, confidence flags) then `**Sources**` (bulleted markdown links, first tagged `*(Primary — …)*`).
5. Record in STATE + LOG.

### R4 — Enrich / add a GC (Companies DB)
1. Dedup §1 (search the Companies data source — many GCs already exist; enrich, never duplicate).
2. If new: `notion-create-pages` (parent `041b7f07-…`), icon `/icons/building_blue.svg`, `Type`=`Company` (JV partner contractor still `Company`), `BW Category`=`Builder`, `Country` (JSON array), `Size`, `Description`, `Website ` (⚠ trailing space), `LinkedIn`.
3. Link `Construction Projects` (JSON-array of project URLs) + `Owners` (owner page URL). NOTE: project-side `Contractors` and company-side `Construction Projects` are **separate** relations — set both.
4. Body: `**Company Snapshot**` (HQ/founded/revenue/employees/specializations w/ inline source) + `**Harvard projects:**` (incl. confidence) + `**Sources**`. Fill empty scalar fields only; don't overwrite populated ones unless clearly wrong + sourced.
5. Record in STATE + LOG.

### R5 — Add a Harvard department company (subsidiary)
1. Dedup §1 (search Companies DS). Parent **Harvard University** = `18390644-d524-80e6-98d9-ef8bafd05ed5`; Harvard **owner** = `37990644-d524-80b8-9f63-f25b06e96d20`.
2. Create via `notion-create-pages` (parent `041b7f07-…`), **varied emoji icon** (depts are the emoji exception). Fields: `Type`=`Company` · `BW Category`=`Owner` · `Country`=`["USA","Massachusetts"]` · `Parent Company`→Harvard University (or a parent dept, e.g. House Renewal→FAS) · `Owner Institution`→Harvard owner · `Owned Projects`→its project URL(s).
3. **Use the dedicated relations, not the GC ones:** `Owned Projects` (⇄ Projects `Owning Department`) for projects; `Owner Institution` (⇄ Owners `Departments`) for the owner. Do NOT use `Construction Projects`/`Owners` (those drive `Contractors`/`General Contractors`).
4. Link people: set each person's People `Company` → the dept company (multi, additive). Back-fills the dept's `People`.
5. Body: `**About**` one-liner + `**Owns / oversees**` + `**Sources**` (inline links). Record in STATE + LOG.

### R6 — Build a filtered hub page (linked DB views, no new DBs)
1. Goal: surface EXISTING records on a hub page as **linked database table-views** — no new databases, no records created/edited. One section per view of a source data source, filtered to the subject.
2. `notion-create-view` with `parent_page_id` + `data_source_id` (type `table`) **appends a linked view to the END of the page** (no positional insert). Build sections in order; add a `## Heading` (insert at end) then create the view under it, or rely on the view `name`.
3. **Filter by relation:** the view DSL does NOT support relation `CONTAINS "<page>"` (silently dropped — title/URL/UUID all fail). Use `FILTER "<relation>" IS NOT EMPTY` when the subject is the ONLY value populating that relation (Harvard is the sole Owner → `Owner`/`Owners`/`Owner Institution` IS NOT EMPTY isolate Harvard). Title filter uses `=` (`"Owner" = "Harvard"`). Group with `GROUP BY "<prop>"` (select/status/relation OK). A column removed from a view can't be re-added/sorted via DSL — fix in UI.
4. **Never `replace_content` a page that physically hosts a real database** (check `notion-fetch` ancestry) — it can delete the DB. Use `update_content` surgical removals; `allow_deleting_content:true` only drops *linked-view* blocks (references), not source data sources.
5. Verify each view's count against the owner/parent record's rollups; confirm zero records created/edited. Record in STATE + LOG.

_(more recipes added as patterns emerge)_
