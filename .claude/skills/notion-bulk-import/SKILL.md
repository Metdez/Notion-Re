---
name: notion-bulk-import
description: Import any bulk record list (CSV, export, scraped list) into the right Notion database(s) — dedup-first, relations linked, existing records enriched, nothing overwritten. Use when given a file of contacts/companies/records and asked to "import this," "add these to Notion," or "link them to <event/company/etc>." Works for any source (Apollo, LinkedIn, conference lists) and any target database.
argument-hint: <file path(s)> + <target/context> (e.g. "Events/export.csv → People DB, linked to <event name>")
---

# Notion Bulk Import

Turn a record list into clean Notion records — zero duplicates, additive only, every relation linked. The process is the product: dedup before writing, write in clobber-safe order, enrich rather than recreate.

**Inputs (from arguments):** the file(s), the target database(s), and any context records the imports should link to (an event, a company, a project…). The file is the ONLY ground truth — no field gets data the file doesn't carry. If the file→target mapping is ambiguous, ask before writing anything.

## Phase 1 — Orient
1. Glance at the harness hubs (`STATE.md`, `USER_PREFS.md`) and any matching ledger under `context/state/` — ledgers are the first dedup index. Harness rules override this skill.
2. **Parse the file with a local script — never raw-Read a large export.** Extract only the fields that map to Notion properties; build a compact per-record list plus a deduplicated list of every referenced entity (companies, orgs, etc.).
3. Note which columns are usable data vs. source-tool plumbing (internal IDs, pipeline stages) — plumbing doesn't get imported.

## Phase 2 — Resolve targets and schemas
- Fetch the schema of every database you'll touch (handles in [state/databases](../../../context/state/databases.md)) — exact property names, select options, relation targets, expanded-key formats.
- Resolve every context record the imports link to: search, then **fetch and confirm** it's the right one (watch for near-twins — annual-event editions, similarly named pages). Capture its current relation arrays for merge-safe updates later.
- A context record genuinely missing → propose creating ONE, confirm with Zack first. Never guess into a duplicate.

## Phase 3 — Dedup everything (before any write)
- For **every** entity in the file — primary records and referenced ones — check the ledger, then search the live database. No exceptions for "obviously new" records.
- **Core-name rule for organizations:** a shortened, extended, or sub-unit variant maps to the existing record (a venture arm, a country subsidiary, a legal-suffix variant). Preserve the file's literal name in a text field when it differs from the linked record.
- **Validate the search channel** with a control search for a record you know exists; if the control misses, stop and rethink.
- Match on name + a second signal (org, email, role). Name-case and accent variants count. **Unsure → treat as existing and enrich; never create a second.**
- Harvest incidental finds from search results; record pre-existing duplicate records you trip over but don't merge them — that's destructive, Zack's call.
- Batch reads conservatively (~5–8 calls per turn); on a rate-limit, shrink the batch and retry the failures — never skip them.

## Phase 4 — Write, in clobber-safe order (the order IS the safety mechanism)
1. **Create missing reference records first** (e.g. companies before the people who link to them) — batched creates, varied Notion icons, only file-sourced fields, a short provenance line in Description.
2. **Merge-update shared relation arrays on context records BEFORE batch creates.** Property updates **replace** arrays — write current + additions, and do it before new records start appending via two-way relations, or you'll clobber them.
3. **Batch-create the new records with relations set at create** — two-way relations propagate to the other side automatically; no second touch needed.
4. **Enrich existing records last: fetch first, fill only empty fields.** Never overwrite a curated value; on conflict keep the existing and flag it (exception: clearly fresher data may replace stale — say so in the report).

## Phase 5 — Rules (non-negotiable)
- **File-sourced only.** No value the file doesn't contain; URLs are their own source. Don't invent, geocode, or "complete" anything.
- **Additive only.** No `replace_content`, no deletes, no merging duplicates, no new databases or columns.
- **No shared-select ALTERs.** Missing select options → nearest existing option or skip, and list the wanted options for Zack's manual UI pass. (Concurrent sessions have clobbered shared selects before.)
- **Encoding fixes are flagged.** Exports mangle accents/characters; restore only unambiguous cases and log every restoration in the ledger; keep the literal when unsure.
- Records with a missing reference (no company, no org) get created without that relation — flagged, not guessed.

## Phase 6 — Record + report
1. Ledger the import under `context/state/` (append to the matching ledger or create one): targets + IDs, matched vs. created per entity type, mappings applied, enrichments, flags. Bump `STATE.md`, register any new file in `MAP.md`, append to the current month's log.
2. Report (CEO-skim): created vs. existing counts per database · relation/link totals · enrichments · flags needing Zack (duplicates spotted, ambiguous matches, encoding fixes) · select options left for manual UI.

## After importing
Spot-check: fetch one context record (relation counts) and one new record (relations present). Suggest `/notion-audit` on any record created bare.
