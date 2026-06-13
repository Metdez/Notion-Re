# CONTINUATION — resume the bulk import here

> **Written 2026-06-12 by the coordinator session.** This file is the exact resume point for the dedup-first import of 44,613 contacts. Read it before touching anything else in `_plan/`.

## ⛔ Why the 2026-06-12 session stopped
The session had **no Notion access of any kind**:
- No `mcp__claude_ai_Notion__*` tools attached (ToolSearch finds none; the claude.ai Notion connector was not on the session).
- No local Notion API token, no `ntn` CLI on disk.
- Cloud-routine path also blocked: the claude.ai account shows **zero MCP connectors** and **GitHub not connected** for `Metdez/Notion-Re` — a routine would launch with neither Notion nor the repo.

**To unblock (either works):**
1. Run the next session somewhere the **claude.ai Notion connector is attached** (it was attached in every prior import/audit session of this project), **or**
2. For cloud routines: connect Notion at https://claude.ai/customize/connectors **and** GitHub via `/web-setup` or https://claude.ai/code/onboarding?magic=github-app-setup — then a routine can clone this repo and run the loop below.

## Where the import stands
| Item | State |
|---|---|
| Phase | `read_existing` (build dedup set from existing People DB) |
| Existing people fetched | **93 / 3,122** (slice_00: 42/150 · slice_01: 24/150 · slice_02: 27/150 · slices 03–20: untouched) |
| Merged partial | `existing_linkedin_partial.json` (93 entries, 83 with a LinkedIn URL) |
| Candidates | `candidates.json` = 44,613 parsed rows; **all have a unique normalized `li_key`** — zero internal dupes (`internal_dupes.json` is empty; `candidates_deduped.json` ≡ candidates.json) |
| Net-new created in Notion | **0** |
| Company map | `company_ids.json` (22 slugs → Notion pageIDs; canonical prose copy `../company-cache.md`) |

## The loop to run (per worker, throttled)
1. **Finish `read_existing`:** for each `slices/slice_NN.json` (150 Notion people-page URLs each), fetch every page via Notion MCP, extract the person's LinkedIn URL, append `{url, linkedin, name}` to `linkedin/slice_NN.json` **after every page**. Resume partial slices at their current length (the files are ordered the same as the slice). Slices 00–02 are partial; 03–20 untouched.
2. **Build the dedup set:** union of all `linkedin/*.json` LinkedIn URLs, normalized (trim, lowercase, strip trailing `/`). For existing people with no LinkedIn, also key by lowercased name for a soft-match warning list.
3. **Filter:** `candidates.json` minus dedup set (match on `li_key`) → `netnew.json`. Expect ≈41–44k net-new (3,122 existing, overlap unknown until step 2).
4. **Phase `create`:** batch-create People records (Notion MCP `notion-create-pages`, multi-page batches) — fields per [agent-brief.md](../agent-brief.md) column map, Company relation from `company_ids.json`, icon varied per CLAUDE.md, LinkedIn URL as the inline source. **Update `run_state.json` + the owning `ledgers/batch-NN.md` cursor after every batch.** Never create a company; unknown company → [excluded-not-in-notion.md](../excluded-not-in-notion.md) §C.
5. On completion roll ledgers up to [BOARD.md](../BOARD.md), update [records-bulk-import](../../../context/state/records-bulk-import.md), append to the monthly log.

## Invariants (unchanged)
Dedup-first on normalized LinkedIn URL · additive only · link existing companies only · sourced fields · ledgers are the truth, updated per record/batch.
