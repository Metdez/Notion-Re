# Playbook · §10 — Reusable "Research → Notion" Load Prompt

> **Holds:** the copy-paste prompt for loading any company research dossier into a Notion company profile. Company-agnostic — fill the `{{...}}` placeholders and send.
> **Part of:** [PLAYBOOK.md](../../PLAYBOOK.md) · map: [MAP.md](../MAP.md)
> **Related:** [loop-and-dedup](loop-and-dedup.md) · [schemas](schemas.md) · [safety](safety.md) · [notion-mcp](notion-mcp.md)

---

## The prompt (copy everything below the line)

---

You are an expert data engineer loading research into my Notion workspace. Your job: read the research file(s) I name, map every fact to the right Notion record and field, and load it — accurately, without duplicates, and without inventing anything.

**Company:** {{COMPANY NAME}}
**Research file(s) (the ONLY ground truth):** {{FILE PATH(S)}}
**Target:** the company's profile page under Sales → Market Research (create-or-update; if a profile page already exists, extend it — never rebuild it)

### Phase 1 — Orient (read before touching Notion)
1. Read the harness hubs: `STATE.md`, `USER_PREFS.md`, `PLAYBOOK.md` (follow only the spokes the task needs). The rules there override anything in this prompt.
2. Read the research file(s) fully. Build a mental inventory: company facts · divisions/offices · people · projects · events · memberships · software · locations · sources · the dossier's own `gaps` list (anything in `gaps` is genuinely unknown — never fill it).
3. Open one existing **completed company profile** and its linked records as the formatting gold standard. Copy its structure, field formats, body-section layout, and level of detail exactly. You are not designing anything new.

### Phase 2 — Learn the shape
Fetch the data-source schemas (and one sample record each) for every database you'll touch, so you use exact property names and formats:
- **Companies DB** — Description, Type, Size, BW Category, Website, LinkedIn, Country, Address (place), relations to Projects/People; body: Company Snapshot + Sources.
- **People DB** — Name, Function, Function Qualification, Location, LinkedIn, Company relation, Division relation; body: sourced `## Role` section.
- **Construction Projects DB** — Name, Status, Type, Location, Date (range), Contract value, Size, URL, Contractors relation, Owning Department relation, Adress (place); body: `## Project Brief` (owner/client, division, architect) + `## Sources`.
- **Profile-page inline tables** — Divisions/Company Map (title, Adress place, People, Projects, Company relations; body: Focus / Regional leader / Notable projects / Parent entity), Events (name, date, place, location tags, company relation), Memberships, Locations, Software.
Watch for: expanded keys (`date:X:start`, `place:X:name/address/lat/lng`), `userDefined:` prefix for properties named `URL`/`id`, relations passed as JSON-encoded arrays of page URLs, and one-way relations that need the full URL list re-passed.

### Phase 3 — Dedup, then load
For EVERY record, search before creating (the relevant state-ledger spoke first, then live Notion — name variants too). Exists → update only its empty fields. Absent → create it, matching the gold-standard record's format, with a varied emoji icon.
Load order: company record → divisions → people (link Company + Division) → projects (link Contractors + Owning Department) → events / memberships / software / locations → cross-link everything (a record nobody links to doesn't exist).

### Phase 4 — Rules (non-negotiable)
- **Sourced data only.** Every value carries an inline source URL from the research. No source → leave the field empty. Never fabricate, never approximate dates/values, never geocode addresses you can't verify.
- **Additive only.** Never replace_content, never delete, never overwrite a filled field. On conflict between research and an existing value, keep the existing value and flag the conflict.
- **No new structure.** Use existing databases, properties, and select options. If the research has data with no Notion home, flag it — don't add columns or databases.
- **Brevity.** Bullets, short sentences, written for a CEO who skims.
- **Confirm before anything structural or destructive** — state the operations and wait.

### Phase 5 — Record + report
1. Update the state ledger (create a `records-{{company-slug}}.md` spoke if none exists) and append to the current month's log.
2. Report: counts created/updated per database · every field left empty because the research had no source (so I know nothing fillable was missed) · conflicts found · anything that needs a manual UI step.

---

## Usage notes (not part of the prompt)
- **This prompt is also installed as the `/notion-load` skill** (`.claude/skills/notion-load/`) — in Claude Code, just type `/notion-load <company> + <file paths>` instead of pasting this. The paste version is for use outside Claude Code.
- Pairs with the `/notion-audit` skill: run this prompt to load, then `/notion-audit` later to verify and fill stragglers.
- If the dossier is JSON (Perplexity-style), the keys usually map 1:1 to the field lists in Phase 2.
- For a second dossier on the same company, the same prompt works — Phase 3's dedup makes it an update pass.
