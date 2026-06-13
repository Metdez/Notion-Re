# Parallel Import Harness — Company-Affiliated, US

A markdown environment for importing 44,669 records into Notion with **18 parallel agents**, crash-safe and resumable. Nothing here runs on its own — agents read these files, do Notion work via MCP, and **constantly write progress back**. Pull the plug anytime; the files say exactly what's done.

## Files
```
_import-harness/
├── README.md        ← this — how to dispatch, resume, monitor
├── BOARD.md         ← master status of all 18 batches (the coordinator's view)
├── agent-brief.md   ← the instructions ONE agent follows for ONE batch
├── company-cache.md ← canonical GC string → Notion pageID map (+ machine copy _plan/company_ids.json)
├── excluded-not-in-notion.md  ← track record of contacts skipped (company not in Notion)
└── ledgers/
    ├── batch-01.md  ← per-batch, per-file progress + resume cursor + log
    └── … batch-18.md
```
Data lives next door in `Big Data/batch-01/ … batch-18/` (5 CSVs of 500 each).

> **Registered in working memory:** this whole harness is indexed at [context/state/records-bulk-import.md](../../context/state/records-bulk-import.md) (the dedup ledger for the import), and from STATE/MAP/LOG. Update that spoke when the import's status changes.

## How it stays resumable ("inter-looping")
- **One agent = one batch = one ledger.** No two agents ever write the same file → zero collisions, even all 18 at once.
- **The ledger is the truth, updated per-record.** Each ledger holds a **cursor** (`file X, row R`). An interrupted agent left a cursor; the next one continues at R+1. Files already imported are skipped via the **LinkedIn dedup key** + Notion dedup-first.
- **Two loops:**
  - *Inner* (per agent): record → write to Notion → update cursor/count/heartbeat → repeat.
  - *Outer* (coordinator): read BOARD → relaunch any batch that's `pending` or a stale `in-progress` → repeat until all 18 are `done`.

## Dispatch — three ways

**A. Fan out all 18 at once (Agent tool).** Send 18 Agent calls in a single message, each one:
> "Read `Big Data/_import-harness/agent-brief.md`. You are agent **A07**, you own **batch-07**. Run the loop to completion."

**B. Loop-until-done coordinator (recommended).** One driver that re-reads `BOARD.md`, launches only batches that are `pending` or stale `in-progress`, waits, repeats until 0 incomplete remain. Survives any agent dying mid-run — the relaunch resumes from the cursor.

**C. Resume after a full stop.** Just re-run A or B. Done batches are skipped (`Status: done`), partial batches continue from their cursor. No double-imports because of dedup-first + the cursor.

> Throttle if Notion rate-limits: run 6 at a time, three waves. The harness doesn't care how many run in parallel.

## Monitor
Open `BOARD.md` for the fleet; open any `ledgers/batch-NN.md` for record-level detail and the log. "What's done vs not" = the ticked boxes and the totals line.

## Safety (inherits CLAUDE.md)
Dedup-first · sourced fields · additive only · no new databases · match existing record formatting · agents stay in their own batch.
