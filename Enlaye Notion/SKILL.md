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

### 4. Cross-reference: fillable vs. sourceless
For every empty field the audit surfaced, check the ground-truth source:
- **Source has a value** → fillable gap. Queue it.
- **Source has nothing** (or explicitly lists it as undisclosed/`null`) → genuinely sourceless. Leave blank, note it.

### 5. Verify, then fill
Before writing, **re-fetch each target record** to confirm the field is still empty (catches sub-agent false positives + concurrent-session edits). Then:
- Properties: `update_properties` — only the empty keys, with sourced values.
- Body facts: insert/update the missing line in place, with inline source link. Match the formatting of records that are already complete.
- Make **zero** unnecessary writes.

### 6. Record + report
- If the project has a harness (STATE/LOG or similar), update the relevant state spoke and append a log entry — what was filled, what was left blank and why.
- Report to the user (CEO-skim): what was filled, and an explicit list of what's *genuinely unfillable* (so they know nothing fillable was missed). Flag any false positives you rejected.

## Watch for
- **Concurrent sessions** editing the same records — re-fetch right before writing; converge, don't clobber.
- **Body vs. property** — a fact may already exist in the page body even when the property is empty (or vice versa). Check both before declaring a gap.
- **Misspelled / special property names** — use exact schema names verbatim; properties named `url`/`id` need a `userDefined:` prefix.
- **"Looks empty" ≠ "is empty"** — a filtered/template view can hide populated data. The records can be complete while the page *displays* nothing.
