# Import Board — Company-Affiliated, US

Master status for the parallel Notion import. **The fleet coordinator reads this file to decide what to (re)launch**, and is the ONLY writer here — it rolls each row up from that batch's ledger. **Agents never edit this file** (they'd clobber each other); they write only their own `ledgers/batch-NN.md`. A batch is only `done` when its ledger shows every file ticked.

- **Source:** `Big Data/Company-Affiliated,-US-Default-view-export-1781143506146.csv`
- **Split:** 44,669 records → 90 files (500 each) → 18 batches (5 files each)
- **Scope (2026-06-10):** import **44,639** contacts whose employer already exists in Notion; **skip 30** (company not in Notion) → tracked in [excluded-not-in-notion.md](excluded-not-in-notion.md). **Create zero new companies.**
- **Targets:** People DB (one record per contact) + Company DB (relation, **link existing only**, dedup-first)
- **Rule of the board:** a row here must match its ledger. If they disagree, the **ledger wins** (it's the per-record source of truth).
- **Company resolution:** [company-cache.md](company-cache.md) (canonical) · registered in working memory at [records-bulk-import](../../context/state/records-bulk-import.md).
- **⛔ 2026-06-12 — BLOCKED, resume point in [_plan/CONTINUATION.md](_plan/CONTINUATION.md):** the dedup-first pre-phase (`read_existing`, 93/3,122 existing people fetched) stalled because the session had **no Notion access** (connector not attached; cloud routines have no connectors/GitHub either). Candidates verified clean: 44,613 rows, all unique LinkedIn keys, zero internal dupes. Nothing imported yet — the table below is accurate.

## Status

| Batch | Records | Status | Done | Agent | Heartbeat | Ledger |
|---|---|---|---|---|---|---|
| 01 | 2500 | `pending` | 0/2500 | — | — | [batch-01](ledgers/batch-01.md) |
| 02 | 2500 | `pending` | 0/2500 | — | — | [batch-02](ledgers/batch-02.md) |
| 03 | 2500 | `pending` | 0/2500 | — | — | [batch-03](ledgers/batch-03.md) |
| 04 | 2500 | `pending` | 0/2500 | — | — | [batch-04](ledgers/batch-04.md) |
| 05 | 2500 | `pending` | 0/2500 | — | — | [batch-05](ledgers/batch-05.md) |
| 06 | 2500 | `pending` | 0/2500 | — | — | [batch-06](ledgers/batch-06.md) |
| 07 | 2500 | `pending` | 0/2500 | — | — | [batch-07](ledgers/batch-07.md) |
| 08 | 2500 | `pending` | 0/2500 | — | — | [batch-08](ledgers/batch-08.md) |
| 09 | 2500 | `pending` | 0/2500 | — | — | [batch-09](ledgers/batch-09.md) |
| 10 | 2500 | `pending` | 0/2500 | — | — | [batch-10](ledgers/batch-10.md) |
| 11 | 2500 | `pending` | 0/2500 | — | — | [batch-11](ledgers/batch-11.md) |
| 12 | 2500 | `pending` | 0/2500 | — | — | [batch-12](ledgers/batch-12.md) |
| 13 | 2500 | `pending` | 0/2500 | — | — | [batch-13](ledgers/batch-13.md) |
| 14 | 2500 | `pending` | 0/2500 | — | — | [batch-14](ledgers/batch-14.md) |
| 15 | 2500 | `pending` | 0/2500 | — | — | [batch-15](ledgers/batch-15.md) |
| 16 | 2500 | `pending` | 0/2500 | — | — | [batch-16](ledgers/batch-16.md) |
| 17 | 2500 | `pending` | 0/2500 | — | — | [batch-17](ledgers/batch-17.md) |
| 18 | 2169 | `pending` | 0/2169 | — | — | [batch-18](ledgers/batch-18.md) |

**Totals:** 0 / 44,669 imported · 0/18 batches done

## Legend
- `pending` — nobody has claimed it. Free to launch.
- `in-progress` — an agent owns it; check **Heartbeat**. Stale (>15 min, no change) = treat as dead, safe to relaunch (it resumes from its cursor).
- `done` — ledger fully ticked. Skip.
- `blocked` — agent hit something it can't resolve; see the ledger Log. Needs a human.
