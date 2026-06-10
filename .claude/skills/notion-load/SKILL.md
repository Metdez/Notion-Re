---
name: notion-load
description: Load a company research dossier into Notion — map every sourced fact to the right record and field, dedup-first, additive only. Use when given research file(s) for a company and asked to "add this to Notion," "load this research," or "build/extend the company profile." Works for new companies and second-pass dossiers on existing ones.
argument-hint: <company name> + <research file path(s)> (e.g. "Acme Corp — research/acme-dossier.md")
---

# Notion Load

Read the named research file(s), map every fact to the right Notion record and field, and load it — accurately, without duplicates, and without inventing anything.

**Inputs (from arguments):** the company name + the research file path(s). The files are the ONLY ground truth. If either is missing, ask before doing anything.
**Target:** the company's profile page under Sales → Market Research — create-or-update. If a profile already exists, extend it; never rebuild it.

## Phase 1 — Orient (read before touching Notion)
1. Read the harness hubs: `STATE.md`, `USER_PREFS.md`, `PLAYBOOK.md` (follow only the spokes the task needs). The harness rules override anything in this skill.
2. Read the research file(s) fully. Build an inventory: company facts · divisions/offices · people · projects · events · memberships · software · locations · sources · the dossier's own `gaps` list (anything in `gaps` is genuinely unknown — never fill it).
3. Open one existing **completed company profile** and its linked records as the formatting gold standard. Copy its structure, field formats, body-section layout, and level of detail exactly. Do not design anything new.

## Phase 2 — Learn the shape
Fetch the data-source schemas (and one sample record each) for every database you'll touch, so you use exact property names and formats:
- **Companies DB** — Description, Type, Size, BW Category, Website, LinkedIn, Country, Address (place), relations to Projects/People; body: Company Snapshot + Sources.
- **People DB** — Name, Function, Function Qualification, Location, LinkedIn, Company relation, Division relation; body: sourced `## Role` section.
- **Construction Projects DB** — Name, Status, Type, Location, Date (range), Contract value, Size, URL, Contractors relation, Owning Department relation, Adress (place); body: `## Project Brief` (owner/client, division, architect) + `## Sources`.
- **Profile-page inline tables** — Divisions/Company Map (title, Adress place, People, Projects, Company relations; body: Focus / Regional leader / Notable projects / Parent entity), Events (name, date, place, location tags, company relation), Memberships, Locations, Software.
Watch for: expanded keys (`date:X:start`, `place:X:name/address/lat/lng`), the `userDefined:` prefix for properties named `URL`/`id`, relations passed as JSON-encoded arrays of page URLs, and one-way relations that need the full URL list re-passed (details: [playbook/notion-mcp](../../../context/playbook/notion-mcp.md)).

## Phase 3 — Dedup, then load
For EVERY record, search before creating — the relevant state-ledger spoke first, then live Notion, including name variants. Exists → update only its empty fields. Absent → create it, matching the gold-standard format, with a varied emoji icon.
Load order: company record → divisions → people (link Company + Division) → projects (link Contractors + Owning Department) → events / memberships / software / locations → cross-link everything (a record nobody links to doesn't exist).
Parallel sub-agents are fine for research/read work, but serialize creates per record type — concurrent creates are how past sessions made 18 duplicates.

### Interlink checklist (mandatory — per Zack, 2026-06-10)
The build is not done until this relation graph is complete. Verify each edge after loading:
- **Person → Division** (People DB `Division` relation) and **Person → Company** (`Company` relation) — both, on every person.
- **Division → Company** (Divisions table company relation) + **Division → People** + **Division → Projects** — every division row carries all three.
- **Project → Contractors** (company) + **Project → Owning Department** (division) on every project.
- **Location → Division** (its `owning_division`) and **Location → Company** — every location row.
- **Events / Memberships / Software → Company** relation on every row.
- One-way forward relations (e.g. Companies DB `Construction Projects`) need the FULL URL list re-passed — see [playbook/notion-mcp](../../../context/playbook/notion-mcp.md).
**If a table lacks the relation property an edge needs** (page-local Locations tables usually have no relations): `ADD COLUMN "<name>" RELATION('<target ds id>')` via `notion-update-data-source` — this additive schema change is pre-authorized by Zack (2026-06-10); state it in the report. Never drop/alter existing columns for this.

### Addresses → data fields (mandatory — per Zack, 2026-06-10)
Every location's address must land in the **actual `place` data field** (`place:X:name/address/lat/lng`), not just in the body description. The build is not done until each of these carries its sourced address in the place property:
- **Company locations** — the Companies DB `Address` (place) property AND every page-local Locations / Company Map row.
- **Project locations** — each Construction Projects `Adress` (place) property (plus `Location`).
- **Event locations** — each Events-table row's `place` property (plus location tags).
Fill the address in the place field for every such record. If a company **location** doesn't already exist and the research gives its address, creating that one location record (address filled) is pre-authorized — dedup first, additive only. No location row should end the load with a blank address field when the source has the address.

### Memberships — load all (mandatory — per Zack, 2026-06-10)
Load **every** membership the research lists — every association, alliance, certification body, trade group, consortium, or program the company belongs to. The Memberships table is not done until each sourced membership has a row, with its company relation and inline source URL. Dedup first (a membership may already exist under a name variant); additive only. A partial membership list is a failed load.

### Location tags — tag every location (mandatory — per Zack, 2026-06-10)
Every record with a location must carry its **location tag** (the location-tag select/multi-select on Events, Locations, and any tagged record), for *every* location variable present. For each such record:
- If the tag option exists → apply it.
- **If the tag option doesn't exist yet → create it** (additive: extend the select, preserving every existing option + color — never replace), then apply it. This is pre-authorized.
No located record ends the load untagged, and no location variable is skipped for want of an option.

### Description depth (mandatory — per Zack, 2026-06-10)
Bodies stay CEO-skim (bullets, short sentences) but must carry the full sourced depth, not one-liners:
- **Projects:** what it is + why it matters (scope, technology, configuration, key metrics like MW/MTPA/SF), owner/client, delivery method + contract type, JV partners & competing bidders, award/announced dates and timeline, incidents/litigation — everything the dossier has, each with its source.
- **Divisions:** focus, leader (+ appointment date), footprint (states/metros/sectors served), founded/acquired date, office phone, notable projects, parent entity.
- **People:** role + appointment/hire date, division context, flagship projects/wins they're tied to, awards/events — everything the dossier sources about the person.

## Phase 4 — Rules (non-negotiable)
- **Sourced data only.** Every value carries an inline source URL from the research. No source → leave the field empty. Never fabricate, never approximate dates/values, never geocode addresses you can't verify.
- **Additive only.** Never `replace_content`, never delete, never overwrite a filled field. On conflict between research and an existing value, keep the existing value and flag the conflict.
- **No new structure** — with ONE exception: relation properties needed to complete the Interlink checklist may be ADDed (additive `ADD COLUMN … RELATION(…)`, pre-authorized by Zack 2026-06-10; report it). Otherwise use existing databases, properties, and select options (when extending a multi-select, preserve every existing option + color). If research data has no Notion home, flag it — don't add columns or databases.
- **Brevity.** Bullets, short sentences, written for a CEO who skims.
- **Confirm before anything structural or destructive** — state the operations, bold the risky ones, wait.

## Phase 5 — Record + report
1. Update the state ledger (create a `records-<company-slug>.md` spoke under `context/state/` if none exists, and add its row to `STATE.md`) and append to the current month's log.
2. Report (CEO-skim): counts created/updated per database · the full membership list now in Notion (confirm none missed) · confirmation every located record is tagged (and any tag options created) · every field left empty because the research had no source (so nothing fillable was silently missed) · conflicts found · anything needing a manual UI step.

## After loading
Suggest running `/notion-audit <company>` as the verification pass — it re-audits the build against the same research and fills stragglers.
