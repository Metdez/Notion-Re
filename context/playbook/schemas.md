# Playbook · Field Schemas (§4)

> **Holds:** the field schema for each database. Mirror exact property names — several are misspelled or carry trailing spaces; match verbatim (full gotcha list: [notion-mcp](notion-mcp.md)).
> **Part of:** [PLAYBOOK.md](../../PLAYBOOK.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [loop-and-dedup](loop-and-dedup.md) · [conventions](conventions.md) · [recipes](recipes.md) · [safety](safety.md) · [notion-mcp](notion-mcp.md)
> **Related:** live DB IDs/URLs in [state/databases.md](../state/databases.md). Before a big write-pass, still fetch the live schema + one sample record — Zack adds properties in the UI (e.g. Projects `Adress`, added 2026-06-09).

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
| Departments | Relation → Companies | two-way w/ Companies "Owner Institution" (dept hierarchy — NOT the GC relation) |
| Project Count | Rollup | count of Projects |
| Total Project Value | Rollup | sum of Projects' "Contrat Value in Million" |

**Page template body** (mirrors the Companies DB template): `Description` · `Comments` · `Where we loose / Where we win` · `Needs / Opportunities`. Template page: https://app.notion.com/p/37990644d5248109a665dc6b1da594d3

## Companies DB (GCs + owner-departments)  (`collection://041b7f07-9564-4696-ae78-1b61b34df758`)
| Field | Type | Notes |
|---|---|---|
| Name | Title | Canonical company name. Dedup key with Website/domain |
| Description | Text | Informative one-liner (revenue, rank, role) — not a tagline |
| Type | Select | `Company` for GCs (JV partners too) · `Consultant` etc. |
| Size | Select | ⚠ option misspelled `Mutlinational` — match verbatim |
| BW Category | Select/multi | `Builder` (GCs) · `Owner` (departments) · `Advisor` · `Developer` · `Design and Architecture` |
| Country | Multi-select | JSON-array string, e.g. `["USA","Massachusetts"]` — states live here too |
| Website␣ | URL | ⚠ **trailing space** in property name |
| LinkedIn | URL | |
| Address | Place | expanded keys `place:Address:name/address/latitude/longitude` |
| Competitor Involvement␣ | — | ⚠ trailing space |
| Parent Company / Subsidiaries | Relation (self) | dept hierarchy (e.g. Harvard University → departments) |
| Construction Projects | Relation → Projects | **one-way** — re-pass the FULL URL list on every update |
| People | Relation → People | two-way with People `Company` |
| Owners | Relation → Owners | GC-side ("General Contractors") — GCs only |
| Owned Projects | Relation → Projects | two-way w/ Projects `Owning Department` — departments only |
| Owner Institution | Relation → Owners | two-way w/ Owners `Departments` — departments only |

**Body:** `**Company Snapshot**` (HQ / founded / revenue / employees / specializations, inline sources) + project-history lines + `**Sources**`. Some records also carry CRM blocks (Lead/Tasks/Touchpoints) — never overwrite.

## People Database  (`collection://0b7ff339-0887-4bbf-a218-7f8d4ede89ef`)
| Field | Type | Notes |
|---|---|---|
| Name | Title | Full name. Dedup key with Company/Email |
| Function | Text/select | Role title |
| Function Qualification | Select/multi | e.g. Director / Project / Business Development |
| Location | Select | state-level OK |
| Email / Phone | — | only if publicly sourced |
| LinkedIn | URL | |
| Lead Priority | Select | P0… |
| Company | Relation → Companies | two-way; multi OK (additive) |
| Division | Relation → profile-page Divisions table | set alongside Company — both, on every person |
| Owner | Relation → Owners | owner-side stakeholders |

**Body:** sourced `## Role` section (+ `## Why This Matters` bullets on key contacts). Icon: `/icons/user_gray.svg`.

## Construction Projects DB  (`collection://4c8ed827-78b9-4d34-9cca-0c3548304199`)
| Field | Type | Notes |
|---|---|---|
| Name | Title | |
| Type | Select | options grow per build (Infrastructure, Life Sciences, Energy & Power, K-12 School…) — ALTER additively first |
| Status | Status | |
| Location | Multi-select | JSON-array string; options grow per build |
| Contrat Value in Million | Number | ⚠ **misspelled** — match verbatim. Only if publicly disclosed; total-project basis |
| Date | Date range | `date:Date:start` / `:end`. Precise dates only — year-only stays in body prose |
| Size | Text | scope summary (SF, MW, beds…) |
| URL | URL | ⚠ write as `userDefined:URL` |
| Adress | Place | ⚠ misspelled; added by Zack 2026-06-09. Legacy empty `Place` property also exists — ignore it |
| Contractors | Relation → Companies | GC(s). NOT a synced pair with Companies `Construction Projects` — set both sides |
| Owner | Relation → Owners | |
| Owning Department | Relation → division rows / dept companies | two-way w/ `Owned Projects` |

**Body:** `## Project Brief` (what & why, scope + metrics, owner/client, delivery method, JV partners, architect, dates, division) + `## Sources` (first tagged `*(Primary — …)*`). Icon: varied emoji per Zack.

## Profile-page local tables (one set per company profile page — collections differ per page; IDs in each [records ledger](../state/))
| Table | Title prop | Other props | Notes |
|---|---|---|---|
| Company Map / Divisions | Division | `Adress` (place, misspelled) · relations `Companies full database` / People / Projects | body: Focus / Leader / Footprint / Founded / Phone / Notable projects / Parent |
| Events | Event name | Date · Location tags (multi) · Place · relation Companies | ⚠ `Place` rejects name-only values (needs lat/lng) — venue goes in body |
| Sources | What the source is about | URL (`userDefined:URL`) | one row per dossier source |
| Locations | Location | `Adress` (TEXT here, unlike Company Map) | add Division/Company relations if missing (pre-authorized ADD COLUMN) |
| Memberships | Name | (+ a People linked-view tab — company filter is manual UI) | |
| Linkedin Post | Name | 19 props incl. Post Type / Media Type / Topics selects | usually empty for new companies |
| Projects Underway | — | **SHARED view of Construction Projects** | never create/delete rows here; clear `__TEMPLATE__` filter manually |
| Existing Software | Name | Location (multi) · `Software used` (multi) | **SHARED Companies-Software DB** `collection://37690644-d524-804f-b966-000b34a1901b` — dedup across companies; extend a row's company relation rather than duplicating |
