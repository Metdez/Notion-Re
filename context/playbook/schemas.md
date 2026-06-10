# Playbook · Field Schemas (§4)

> **Holds:** the field schema for each database. Mirror exact property names (watch the typos — see [notion-mcp](notion-mcp.md)).
> **Part of:** [PLAYBOOK.md](../../PLAYBOOK.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [loop-and-dedup](loop-and-dedup.md) · [conventions](conventions.md) · [recipes](recipes.md) · [safety](safety.md) · [notion-mcp](notion-mcp.md)
> **Related:** live DB IDs/URLs in [state/databases.md](../state/databases.md).

> Fill these in as the real Notion databases are inspected. Mirror exact property names.

## Owners Database  (`collection://37990644-d524-80da-92f8-000b22169334`)
> Modeled on the Companies DB field set, plus owner-specific outreach fields.

| Field | Type | Notes |
|---|---|---|
| Owner | Title | Owner organization name |
| Description | Text | One-liner |
| Type | Select | Higher Education / Healthcare / Government-Public / Developer-REIT / Corporate / Senior Living / K-12 / Other |
| Size | Select | National / Regional / Local / Single-campus |
| Location | Multi-select | MA / CT / NY / RI / NH / ME / VT / USA / Other |
| Website | URL | |
| LinkedIn | URL | |
| Priority | Select | P0 / P1 / P2 / P3 (outreach) |
| Status | Select | Not started / Researching / Contacted / In conversation / Qualified / Not now |
| Capital Program | Text | Annual construction/capital spend — carry inline source |
| Source | URL | Primary citation |
| Last edited | Last edited time | auto |
| Projects | Relation → Construction Projects | two-way, back-prop "Owner" |
| Key Contacts | Relation → People | two-way, back-prop "Owner" |
| General Contractors | Relation → Companies full database | two-way, back-prop "Owners" |
| Project Count | Rollup | count of Projects |
| Total Project Value | Rollup | sum of Projects' "Contrat Value in Million" |

**Page template body** (mirrors the Companies DB template): `Description` · `Comments` · `Where we loose / Where we win` · `Needs / Opportunities`. Template page: https://app.notion.com/p/37990644d5248109a665dc6b1da594d3

## Company Database
| Field | Type | Notes |
|---|---|---|
| Name | Title | Canonical company name |
| Domain | URL/Text | Primary dedup key alongside Name |
| _…_ | _…_ | _Inspect DB and complete_ |

## People Database
| Field | Type | Notes |
|---|---|---|
| Name | Title | Full name |
| Company | Relation | Link to Company Database |
| _…_ | _…_ | _Inspect DB and complete_ |
