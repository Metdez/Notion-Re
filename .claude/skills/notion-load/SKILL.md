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

## Phase 4 — Rules (non-negotiable)
- **Sourced data only.** Every value carries an inline source URL from the research. No source → leave the field empty. Never fabricate, never approximate dates/values, never geocode addresses you can't verify.
- **Additive only.** Never `replace_content`, never delete, never overwrite a filled field. On conflict between research and an existing value, keep the existing value and flag the conflict.
- **No new structure.** Use existing databases, properties, and select options (when extending a multi-select, preserve every existing option + color). If research data has no Notion home, flag it — don't add columns or databases.
- **Brevity.** Bullets, short sentences, written for a CEO who skims.
- **Confirm before anything structural or destructive** — state the operations, bold the risky ones, wait.

## Phase 5 — Record + report
1. Update the state ledger (create a `records-<company-slug>.md` spoke under `context/state/` if none exists, and add its row to `STATE.md`) and append to the current month's log.
2. Report (CEO-skim): counts created/updated per database · every field left empty because the research had no source (so nothing fillable was silently missed) · conflicts found · anything needing a manual UI step.

## After loading
Suggest running `/notion-audit <company>` as the verification pass — it re-audits the build against the same research and fills stragglers.
