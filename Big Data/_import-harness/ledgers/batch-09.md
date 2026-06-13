# Batch 09 — records 20001–22500 (2500 total)

> **Harness:** [BOARD](../BOARD.md) · [README](../README.md) · [agent-brief](../agent-brief.md) · [company-cache](../company-cache.md) · [excluded](../excluded-not-in-notion.md) · registered in [records-bulk-import](../../../context/state/records-bulk-import.md)

> One agent owns this batch. Update this file **after every record** — cursor, count, heartbeat.
> If you are resuming: read **Resume cursor** below and continue from the next row. Never restart a file from the top.

| Field | Value |
|---|---|
| Agent | A09 |
| Status | `in-progress` |   <!-- pending → in-progress → done -->
| Heartbeat | 2026-06-10 19:32 |   <!-- timestamp of last record imported -->
| Source folder | `batch-09/` |
| Records | 0 / 2500 |

## Files
- [ ] `records-20001-20500.csv` — 0/500 — cursor: row 0 — `pending`
- [ ] `records-20501-21000.csv` — 0/500 — cursor: row 0 — `pending`
- [ ] `records-21001-21500.csv` — 0/500 — cursor: row 0 — `pending`
- [ ] `records-21501-22000.csv` — 0/500 — cursor: row 0 — `pending`
- [ ] `records-22001-22500.csv` — 0/500 — cursor: row 0 — `pending`

## Resume cursor
- Last imported: **none**
- Next up: file `records-20001-20500.csv`, row **1**

## Company cache (resolved Companies-DB pageIDs — reuse, do not re-search)
- Kiewit → `17b90644-d524-8055-88ec-f7f399f27e9d` (covers: Kiewit, Kiewit Building Group, Kiewit Power Delivery)
- Bechtel Group (parent) → `18490644-d524-80ff-8307-e94405919579`
- Bechtel National → `30a90644-d524-8037-8b5f-e3134e999f7d` (covers: Bechtel National Inc)
- Bechtel Power → `2b590644-d524-8039-8fb4-ce11364a6bdc` (covers: Bechtel Power Corporation)
- _Bechtel Corporation / Energy / Oil Gas & Chemicals / Civil Infrastructure / Government Services / "bechtel" / "Bechtel Corp" → map to closest Bechtel sub-record; default Bechtel Group if no closer match (NOT yet confirmed — search pending)_
- _Pending resolution: Gilbane Building Company, Clayco, Sundt Construction, Consigli Construction, Alberici Constructors, Zachry Group, Suffolk Construction, HITT Contracting, FlatironDragados, Cianbro Corporation, Branch (branchgroup), O&G Industries, Dellbrook | JKS, Shawmut Design and Construction, ITSI Gilbane_

## NOTE — environment blocker (2026-06-10 ~19:35)
Notion MCP is returning persistent HTTP 429 (`mcp_tool_rate_limit`, "try again in a few minutes") on nearly every call — only ~1 call succeeds before a multi-minute cooldown. With 18 agents + the hourly cron audit sharing one Notion MCP, per-record dedup-search+create for 2500 rows is not achievable in a single run at this rate. Proceeding by: resolve each distinct company once (cached above), then import people in small resumable chunks, advancing the cursor after each chunk. If 429s persist, set Status `blocked` with this note so a human/coordinator can throttle the fleet.

## Log  (append newest at the bottom; one line per ~25 records or per file)
- 2026-06-10 19:35 · setup · resolved Kiewit + 3 Bechtel records; hit persistent Notion 429 rate limit (see NOTE). No people imported yet; cursor still at file 1 row 1.
