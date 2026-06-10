# State · Records — Jingoli Nuclear Services

> **Holds:** the Jingoli Nuclear Services dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a Jingoli record.
> **Ground truth:** `Enlaye Notion/Jingoli/Jingoli.md`. Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.

---

## Profile page (hub)
**"Jingoli Nuclear Services"** (renamed from "Jingoli TEMPLATE") — https://app.notion.com/p/37b90644d5248068a30ed33131821345 (Companies research → Zack Folder). Newer template variant: **Divisions** DB (not "Company Map"). Bio snapshot at top; Attack Plan filled at bottom. Icon `building_blue`.

Page-local data sources on this page:
- **Divisions** `collection://4f590644-d524-8375-b2e6-076d6a38735a` (props: Division title · Adress place · relations Companies full database / People / Projects)
- **Events** `collection://7df90644-d524-825b-97ac-079b32b5e078` (Event name · Date · Location tags · Place · Companies full database)
- **Sources** `collection://8a790644-d524-82bd-9609-07cf65f7fae4` ("What the source is about" · URL)
- **Locations** `collection://add90644-d524-8248-b15c-875a0c12bfa8` (Location · Adress text · **+added** Companies full database + Division relations)
- Linkedin Post `collection://5e490644-d524-825e-91ec-87ccc86fdae8` (unused) · Memberships `collection://ffb90644-d524-828c-a88d-87c74005ea00` (unused — dossier had none)
- Projects Underway = shared Construction Projects (linked view, filtered `__TEMPLATE__` — **manual UI filter fix needed**)
- Existing Software = shared Companies Software (linked view, filtered `__TEMPLATE__` — **manual UI filter fix needed**)

**Additive schema change (pre-authorized 2026-06-10):** added relations `Companies full database` + `Division` to the page-local Locations DB (was bare: Location · Adress only) — to complete the interlink.

## Company record (CREATED)
**"Jingoli Nuclear Services"** `37b90644-d524-8127-824d-f2c6e9f55131` in Companies DB. Icon `building_blue`.
- Description (sourced) · Type=Company · BW Category=[Builder] · Country=[New Jersey, Pennsylvania, Ontario, New York] · Website https://jingolinuclear.com · LinkedIn https://linkedin.com/company/jingoli-nuclear · People (2) · Construction Projects (5, one-way list re-passed).
- **Address (place) left empty** — dossier has no lat/lng; no-geocoding rule. HQ address carried in body / Location row / division bodies as text.
- **Size left empty** — dossier null (no source).
- ⚠ **Distinct from pre-existing "Jingoli - DCO" company record** `30d90644-d524-80cf-8e1a-f566999252ca` (empty stub, Feb 2026) — a sibling Jingoli family entity, left untouched (additive). Jingoli-DCO also appears as a division row here.

## Divisions (5 — Divisions DB `4f590644`)
Each carries Companies full database → company. Bodies carry focus/leader/footprint/parent (sourced).
| Division | ID | People | Projects |
|---|---|---|---|
| Jingoli Nuclear Services (market-sector unit) | 37b90644-d524-8176-9b58-e01587bd5333 | Mockaitis | all 5 |
| Jingoli Power (subsidiary) | 37b90644-d524-818e-ad89-d50dbe628c8c | Karl Miller | — (solar projects not in dossier project list) |
| JDC Energy Services (affiliate) | 37b90644-d524-81e9-b79a-fb649344cb46 | — | — |
| Goldstar Energy Group (affiliate) | 37b90644-d524-8117-b7ae-c8773b2b2693 | — | — |
| Jingoli - DCO (regional office) | 37b90644-d524-8111-a830-c41f5ac430de | — | — |

## People (2 — People DB; Company → company `37b9…f55131`)
| Person | ID | Role | Division |
|---|---|---|---|
| Matthew Mockaitis | 37b90644-d524-81bf-9d26-c5d8dbb9b583 | President, Jingoli Nuclear Services | Nuclear Services |
| Karl Miller | 37b90644-d524-8143-b66b-ddcb33fcffd8 | CEO, Jingoli Power | Jingoli Power |

## Projects (5 — Construction Projects DB; Contractors → company)
All Type=Energy & Power. Owner/client + JV in body (no Owner DB records created — out of scope).
| Project | ID | Value $M | Status |
|---|---|---|---|
| PSEG Salem & Hope Creek Demineralized Water Building | 37b90644-d524-8193-bf48-e1378281883f | 0.755 | Done |
| PSEG Salem / Hope Creek Spent Fuel Storage / ISFSI Expansion | 37b90644-d524-8119-9b95-e8ac8c221f44 | — | Done |
| Exelon — Limerick, Peach Bottom, Oyster Creek Security Upgrades | 37b90644-d524-81a6-aebe-dc45661f439a | 35 | Done |
| Bruce A Unit 3 & 4 Turbine Refurbishment | 37b90644-d524-8161-86fd-ff609fb52297 | 13 | Done |
| Three Mile Island Unit-2 Decommissioning (ES/Jingoli) | 37b90644-d524-8144-ba04-fad439c91c23 | — | In progress (start 2019-10-15) |

## Other tables
- **Location (1):** Lawrenceville HQ (shared) `37b90644-d524-810a-aa29-ecaa35b8770d` — 100 Lenox Drive Suite 100, Lawrenceville NJ 08648; linked Company + Nuclear Services division.
- **Event (1):** ENR NY Region Contractor of the Year (Jingoli-DCO, 2012) `37b90644-d524-81e7-b39c-f7d9ca46c9dc` — Date 2012-01-01, linked Company. (Location tag "New York" not an option — kept in body, not added.)
- **Sources (8):** Jingoli About/Projects/Affiliates, Jingoli Power, EnergySolutions TMI-2, ENR Top 400, RocketReach, NY DPS filing (`8a790644`).
- **Memberships:** none — dossier association = null.
- **Software:** none — dossier found no named tools.

## Interlink graph (verified by re-fetch)
Company ↔ People (2) ✓ · Company ↔ Construction Projects (5) ✓ · Division→Company (all 5) ✓ · Division Nuclear Services → People (Mockaitis) + Projects (5) ✓ · Division Power → People (Karl Miller) ✓ · Project→Contractors (all 5) ✓ · Location → Company + Division ✓ · Event → Company ✓.

## Left empty (no sourced value in dossier — per gaps list)
Company Size; DUNS/UEI/CAGE/EIN; state of incorporation; firm revenue/headcount/ENR rank for Nuclear Services; per-project permits/parcels/lat-lng; delivery method/contract type/bonding; EMR/TRIR/DART; litigation/liens; design-team firms; competing bidders; named software; offices beyond Lawrenceville. People Email/Phone; Karl Miller LinkedIn.

## Audit pass 2026-06-10 (`/notion-audit Jingoli`) — CONVERGED, zero writes
Full live re-verify of all 15 records vs `Jingoli.md` (company + 5 divisions + 2 people + 5 projects + 1 location + 1 event). Every record fetched live; every sourced field confirmed already populated. **No fillable gaps → no writes** (skill's "zero unnecessary writes").
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis + 5 projects; Power→Karl Miller; all 5 projects→Contractors; both people→company (+ in their division's People); Location→company+division; Event→company.
- **Description-depth (3b) ✓:** all 5 project bodies carry what/owner/value/scope/JV/dates; Power division body carries founded/phone/$17.5M/102-emp; people bodies carry role + context.
- **Address/location (3c):** place fields **genuinely unfillable** — dossier `lat:null/lng:null` everywhere; workspace `place` property rejects address-only (needs lat/lng); no-geocoding rule forbids inventing coords. Addresses live where a text field exists (Location row `Adress` text ✓) + in every body. Consistent w/ Bechtel/O&G/Dellbrook/Clayco place-blank precedent.
- **Deliberate scope boundaries (flagged, not written):** project `Owning Department` empty — relation targets Companies DB, not Divisions-DB rows; this template carries division↔project via `Divisions.Projects` (set on all 5), so Owning Department isn't the mechanism here (setting it = redundant w/ Contractors). `Owner` relation empty — Owner DB records out of scope per load (owner/client in each project body).

## Audit pass 2026-06-10 (second run — `/notion-audit Jingoli` with `Jingoli1.md`) — 1 write
Full re-verify of all 16 records (added `Jingoli1.md` as second dossier). One fillable gap found and filled.
- **Filled (1):** Event `37b9…dc9dc` — `Location tags = ["New York"]` added. Schema change required first: added "New York" option (purple) to page-local Events DB (`collection://7df90644`) — all 9 existing options preserved. Source: `Jingoli.md` events[0].location_tags = ["New York"] / [ENR](https://enr.com/blogs/23-ny-construction-central/post/13801-jingoli-dco-named-region-s-contractor-of-the-year).
- **Interconnection (3a):** People `Division` relation still empty (Mockaitis + Karl Miller) — targets shared global Divisions DB (`collection://37690644-d524-8088-abd7-000b818a9b6b`), not page-local. No matching rows exist there. → DEFERRED (shared rows).
- **Address/location (3c):** unchanged — place fields genuinely unfillable (lat/lng null throughout both dossiers).
- **Memberships (3d):** none — both dossiers confirm null.
- **Software:** `Jingoli1.md` surfaces Procore, Oracle Primavera P6, Hard Dollar (broader Jingoli entity / nuclear job posts). Existing Software DB is shared → DEFERRED (shared rows).

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = Jingoli Nuclear Services.
2. **Existing Software** view → clear `__TEMPLATE__` filter (table is empty — no software to show).
3. Possible template guide rows on local tables (Divisions/Events/Sources/Locations) — UI delete if Zack wants them gone.
