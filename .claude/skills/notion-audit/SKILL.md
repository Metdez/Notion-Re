---
name: notion-audit
description: Audit a Notion company/page and every record linked to it, then fill ONLY the fields that have real sourced data. Read-only parallel audit → verify against live Notion → additive fills. Use when asked to "make sure every field is filled," "find what's missing," or "complete the data" on a Notion record. Works on any company or page.
argument-hint: <company or page name> (e.g. "Consigli Building Group")
---

# Notion Audit

Fill every field that has sourced data on a target Notion page and all records linked to it — without fabricating, duplicating, or deleting anything.

**Core principle:** a blank is only worth filling if the source data actually exists. Distinguish *fillable gaps* (data exists, field empty) from *genuinely sourceless blanks* (no data anywhere — leave empty, never invent). Report both.

## Non-negotiables
- **Non-destructive.** Additive only. Never `replace_content`, never create databases, never delete rows. Update only empty fields.
- **Sourced data only.** Every value written carries an inline source URL. No source → no write.
- **Verify before writing.** Treat every audit finding as a *hypothesis*, not a fact (sub-agents produce false positives). Re-fetch the live record and confirm the field is actually empty before touching it.
- **No duplicates.** Confirm a value isn't already present (in a property *or* the page body) before adding it.

## Process

### 1. Ground truth
Identify the source of truth for the data (research dossier, ledger, prior notes — usually a file the user names). Read it fully. This is the *only* thing you may fill from. If no source is named, ask where the data lives.

### 2. Learn the shape
- Search/fetch the target page and its linked databases.
- Fetch each relevant **data-source schema** + **one sample record** to learn the exact property names, types, expanded-key formats (dates, place), and which facts live in the page **body** vs. in **properties**.
- Enumerate every record to audit: the company/page itself + all linked records (projects, people, divisions, events, etc.). Capture their IDs.

### 3. Parallel READ-ONLY audit
Dispatch parallel sub-agents (Sonnet is fine), split by record type/batch. Each agent **fetches and reports only** — no writes. Each returns, per record, a compact list of which fields are **empty** (properties *and* expected body elements).

Two checks are ALWAYS part of the audit, on every run (per Zack, 2026-06-10):

**3a. Interconnection check.** Verify the full relation graph, not just field values:
- every person → `Company` AND `Division` relations set
- every division row → company relation + `People` + `Projects` set (where the source names any)
- every project → `Contractors` (company) + `Owning Department` (division) set
- every location row → division + company relations set
- every event/membership/software row → company relation set
- one-way forward relations (e.g. Companies DB `Construction Projects`) hold the complete URL list
A missing edge whose endpoints both exist is a fillable gap — fix it additively. **If the relation property itself doesn't exist** (common on page-local Locations tables), `ADD COLUMN "<name>" RELATION('<target ds id>')` is pre-authorized (additive only; report it).

**3b. Description-depth check.** Project, division, and people bodies must carry the full sourced depth (projects: what-it-is/why-it-matters, scope + metrics, owner, delivery, JV partners, dates, incidents; divisions: focus, leader, footprint, founded, notable projects; people: role, dates, division context, flagship projects). A thin body where the ground truth has more detail = fillable gap.

**3c. Address/location check (per Zack, 2026-06-10).** Every record that has a location must carry its address in the **actual data field** (the `place` property — `place:X:name/address/lat/lng`), not just mentioned in the body description. Audit the address property on, at minimum:
- **Company locations** — the company record's `Address` (place) property AND every row in the page-local Locations / Company Map table.
- **Project locations** — each Construction Project's `Adress` (place) property (and `Location`).
- **Event locations** — each Events-table row's `place` property (and any location tags).
An address that exists in the ground truth but sits only in the body (or is missing from the place field) = fillable gap — write it into the place property. If a company **location row** doesn't exist at all and the source gives its address, creating that one location record (with the address filled) is pre-authorized. Every location across every record must end the audit with its address in the data field, not blank.

**3d. Membership completeness check (per Zack, 2026-06-10).** The company's **Memberships** table must list *every* association, alliance, certification body, trade group, consortium, or program the source says the company belongs to — not a partial set. Audit the live Memberships table against the ground truth and enumerate which memberships are present vs. missing. Each membership row must carry its company relation (3a) and its source URL. Any membership named in the source but absent from Notion is a fillable gap — add the row. Audit ends only when every sourced membership is listed.

**3e. Location tags check (per Zack, 2026-06-10).** Every record that has a location must carry its **location tag** (the location-tag select/multi-select — e.g. on Events, Locations, and any tagged record), for *every* location variable present. Audit each such record: is the tag set, and does the tag *option* exist in the schema?
- Tag option exists but isn't applied → fillable gap, set it.
- **Tag option doesn't exist yet** → creating the new select option is pre-authorized (additive; extend the multi-select, preserving every existing option + color — never replace). Then apply it.
Audit ends only when every location on every record is tagged, and no location variable is left untagged for want of an option.

### 4. Cross-reference: fillable vs. sourceless
For every empty field the audit surfaced, check the ground-truth source:
- **Source has a value** → fillable gap. Queue it.
- **Source has nothing** (or explicitly lists it as undisclosed/`null`) → genuinely sourceless. Leave blank, note it.

### 5. Verify, then fill
Before writing, **re-fetch each target record** to confirm the field is still empty (catches sub-agent false positives + concurrent-session edits). Then:
- Properties: `update_properties` — only the empty keys, with sourced values. **Addresses go into the `place` property** (`place:X:name/address/...`) on every company, project, location-row, and event — never leave an address only in the body.
- **Memberships:** add a row for every sourced membership the live table is missing (3d), with company relation + source URL.
- **Location tags:** set the location tag on every record that has a location (3e); if the tag option doesn't exist, add it to the select (additive, preserving existing options) then apply it.
- Body facts: insert/update the missing line in place, with inline source link. Match the formatting of records that are already complete.
- Make **zero** unnecessary writes.

### 6. Record + report
- If the project has a harness (STATE/LOG or similar), update the relevant state spoke and append a log entry — what was filled, what was left blank and why.
- Report to the user (CEO-skim): what was filled, and an explicit list of what's *genuinely unfillable* (so they know nothing fillable was missed). Explicitly state the full membership list now in Notion (3d) and confirm every located record is tagged (3e). Flag any false positives you rejected.

## Watch for
- **Concurrent sessions** editing the same records — re-fetch right before writing; converge, don't clobber.
- **Body vs. property** — a fact may already exist in the page body even when the property is empty (or vice versa). Check both before declaring a gap.
- **Misspelled / special property names** — use exact schema names verbatim; properties named `url`/`id` need a `userDefined:` prefix.
- **"Looks empty" ≠ "is empty"** — a filtered/template view can hide populated data. The records can be complete while the page *displays* nothing.
