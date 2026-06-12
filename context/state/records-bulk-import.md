# State · Records — Bulk Import (Company-Affiliated, US)

> **What this is:** the working-memory registration + dedup ledger for the large LinkedIn/Apollo bulk import staged in [`Big Data/`](../../Big%20Data/). 44,669 US construction contacts → People DB, linked to existing Companies-DB records only. The **live, per-record truth is the import harness's own ledgers** ([BOARD](../../Big%20Data/_import-harness/BOARD.md) + 18 batch ledgers); this spoke is the index into it.
> **Read it:** before importing any People-DB contact from this dataset; before re-running or resuming the import; to find where the harness lives.
> **Write it:** when the import's status changes (a batch completes, a blocker appears, scope changes).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: [records-event-imports](records-event-imports.md) · [databases](databases.md)
> **Ground truth:** [`Big Data/Company-Affiliated,-US-Default-view-export-1781143506146.csv`](../../Big%20Data/Company-Affiliated,-US-Default-view-export-1781143506146.csv) (44,669 rows) → split into 90 CSVs (500 each) across 18 batches.

---

## The harness (lives next door, self-contained & resumable)
| File | Role |
|---|---|
| [README](../../Big%20Data/_import-harness/README.md) | how to dispatch / resume / monitor the 18-agent parallel import |
| [BOARD](../../Big%20Data/_import-harness/BOARD.md) | master status of all 18 batches (coordinator's view) |
| [agent-brief](../../Big%20Data/_import-harness/agent-brief.md) | the loop ONE agent runs for ONE batch |
| [company-cache](../../Big%20Data/_import-harness/company-cache.md) | canonical GC string → Notion pageID (24 records); machine copy `_plan/company_ids.json` |
| [excluded-not-in-notion](../../Big%20Data/_import-harness/excluded-not-in-notion.md) | 30 pre-flight skips + append-only discovered skips |
| `ledgers/batch-01…18.md` | per-batch, per-file progress + resume cursor + log (the per-record truth) |

## Scope (set 2026-06-10)
- **Import 44,639** contacts whose employer is an **existing** Companies-DB record (487 of 517 distinct company strings → 99.93%).
- **Skip 30** (company not in Notion) — 12 real third-party employers + 18 junk cells — tracked in [excluded §A/§B](../../Big%20Data/_import-harness/excluded-not-in-notion.md). Plus append-only §C for any discovered during import.
- **Create zero new companies.** Dedup key = normalized `LinkedIn Profile` URL → Work Email → `Full Name | Company`.
- **Targets:** People DB (one record per contact, sourced) + Company relation (link existing only). Matches existing People/Company field formatting per [CLAUDE.md](../../CLAUDE.md).

## Status — **dedup pre-phase started, then BLOCKED (no Notion access)**
| Item | State |
|---|---|
| Data split (90 CSVs / 18 batches) | ✅ complete · contiguous 00001–44669 · no gaps |
| Ledgers (18) + BOARD + brief + excluded | ✅ in place |
| Company cache | ✅ canonical ([company-cache.md](../../Big%20Data/_import-harness/company-cache.md)) — replaced 4 divergent scratch copies; Alberici parent vs. sub disambiguated |
| Candidate parse + internal dedup | ✅ `_plan/candidates.json` = 44,613 rows, **all unique normalized LinkedIn keys, 0 internal dupes** (verified 2026-06-12) |
| Dedup set (existing People LinkedIn) | ⏳ **93 / 3,122** fetched (`_plan/linkedin/`, merged partial `_plan/existing_linkedin_partial.json`) |
| Records imported to Notion | ⏳ **0 / 44,613** — every batch at row 0 |

## Outstanding / decisions
- ✅ **Zack gave the go 2026-06-12** ("continue … just go"). Strategy: dedup-first single/few throttled workers per `_plan/run_state.json`, not the original 18-agent blind fan-out.
- ⛔ **BLOCKED 2026-06-12 — no Notion access in session**: claude.ai Notion connector not attached, no local token, cloud routines have zero connectors + no GitHub. **Resume point: [`_plan/CONTINUATION.md`](../../Big%20Data/_import-harness/_plan/CONTINUATION.md)** — unblock by running in a connector-attached session, or connecting Notion + GitHub at claude.ai for a cloud routine.
- ⚠ **Alberici** has two valid records (parent `27990644` vs. `Alberici Constructors, Inc.` `37b90644-…8129`); cache disambiguates by string. Bechtel has 3 (Group/National/Power).
- 🧹 Cleaned 2026-06-11: removed 7 empty macOS sync-dup folders; flagged `_a05_tmp/company-cache.md` + `ledgers/batch-12-company-cache.md` as superseded scratch.

## Related working-memory ledgers
The 24 cached GCs each have a full company ledger — e.g. [records-bechtel](records-bechtel.md) · [records-kiewit](records-kiewit.md) · [records-alberici](records-alberici.md) · [records-zachry](records-zachry.md) · [records-shawmut](records-shawmut.md). The bulk import only **links** to those existing company records; it never alters them.
