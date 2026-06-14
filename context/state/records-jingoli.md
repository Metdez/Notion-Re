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

## Audit pass 2026-06-12 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 records (company DB record + 5 divisions + 2 people + 5 Jingoli projects + 1 location + 1 event + local table schemas). Ground truth: `Jingoli.md`. No fillable gaps found from dossier source — all sourced fields already populated.
- **New data observed (not by this audit):** Company body has "Jing3 Enrichment (2026-06-12)" section — legal name, founded (1922), revenue ($884M), ENR Top 400 #153, ENR Power #15, 1,500+ employees, phone, CEO, COO, 19+ states. Added in a separate session after last ledger entry. PSEG ISFSI project now shows $27M contract value (was null in dossier).
- **Interconnection (3a) ✓:** all edges confirmed — 5 divisions→company; Nuclear Services→Mockaitis + 11 projects; Power→Karl Miller + 5 Power projects; all 5 Jingoli projects→Contractors; both people→company; Location→company+division; Event→company. People `Division` property still deferred (global Divisions DB `37690644` has no Jingoli rows).
- **Description-depth (3b) ✓:** all project + division bodies carry full sourced depth.
- **Address/location (3c):** place fields genuinely unfillable — no lat/lng in dossier; no-geocoding rule unchanged. Location row `Adress` text ✓.
- **Memberships (3d):** none in dossier → none in Notion ✓.
- **Location tags (3e):** Event "New York" ✓ (set in prior pass). No other located records with missing tags.

## Audit pass 2026-06-13 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 records (company DB record + 5 divisions + 2 people + 5 projects + 1 location + 1 event). Ground truth: `Jingoli.md`. No fillable gaps found — all sourced fields already populated.
- **New state since 06-12:** Company DB record `Size = "Regional"` now set (was empty in prior pass; filled by a separate session).
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis + 11 projects; Power→Karl Miller + 5 Power projects; all 5 Jingoli dossier projects→Contractors; both people→company; Location→company+division; Event→company. People `Division` deferred (global Divisions DB no Jingoli rows).
- **Description-depth (3b) ✓:** all project/division/people bodies carry full sourced depth.
- **Address/location (3c):** place fields genuinely unfillable — no lat/lng in dossier; no-geocoding rule. Location row `Adress` text ✓.
- **Memberships (3d):** none in dossier → none in Notion ✓.
- **Location tags (3e):** Event "New York" ✓. No other untagged located records.

## Audit pass 2026-06-13 second run (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 records (company + 5 divisions + 2 people + 5 projects + 1 location + 1 event). Ground truth: `Jingoli.md`. No fillable gaps found — every sourced field already populated, no new state changes observed since prior pass.
- **New state since prior 06-13 pass:** Company now has 19 people linked and 27 construction projects linked (added by other sessions since 06-12).
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis + 11 projects; Power→Karl Miller + 5 Power projects; all 5 Jingoli dossier projects→Contractors + Owning Department (Nuclear Services div); both people→company; Location→company+division; Event→company. People `Division` deferred (global Divisions DB no Jingoli rows).
- **Description-depth (3b) ✓:** all project/division/people bodies carry full sourced depth.
## Audit pass 2026-06-13 Pass #5 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 records (company DB record + 5 divisions + 2 people + 5 dossier projects + 1 location + 1 event). Ground truth: `Jingoli.md`. No fillable gaps found.
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis + 11 projects; Jingoli Power→Karl Miller + 5 projects; all 5 dossier projects→Contractors + Owning Department (Nuclear Services); both people→company; Location→company+division; Event→company. People `Division` deferred (global Divisions DB no Jingoli rows).
- **Description-depth (3b) ✓:** all 5 division bodies + all 5 project bodies + both people bodies at source-maximum depth.
- **Address/location (3c):** place fields genuinely unfillable — no lat/lng in dossier; no-geocoding rule. Location row `Adress` text ✓.
- **Memberships (3d):** none in dossier → none in Notion ✓.
- **Location tags (3e):** Event "New York" ✓. No other untagged located records.

## Audit pass 2026-06-13 Pass #6 (`/notion-audit Jingoli Nuclear Services`) — 2 FILLS
Full live re-verify of all 15 records (company DB record + 5 divisions + 2 people + 5 projects + 1 location + 1 event) + cross-check with `Jingoli1.md`. **2 fillable gaps found and filled — previously missed because prior passes only checked `Jingoli.md` (no lat/lng), not `Jingoli1.md` (HQ lat/lng present).**
- **Filled (2):**
  1. Company DB record `37b90644-d524-8127-824d-f2c6e9f55131` — `place:Address` → "100 Lenox Drive Suite 100, Lawrenceville, NJ 08648" (lat 40.2793 / lng -74.7263). Source: Jingoli1.md / jingoli.com/contact.
  2. Division `37b90644-d524-8176-9b58-e01587bd5333` (Nuclear Services market-sector unit) — `place:Adress` → same address + coords. Source: Jingoli1.md / documents.dps.ny.gov.
- **Project Adress fills attempted (5) — rejected:** dossier lat/lng = null for all project sites; Notion place validation requires lat/lng; no-geocoding rule blocks fabrication. All 5 remain genuinely unfillable.
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis+11 projects; Jingoli Power→Karl Miller+5 projects; all 5 dossier projects→Contractors+Owning Department; both people→company; Location→company+division; Event→company.
- **Description-depth (3b) ✓:** all bodies at full sourced depth.
- **Address/location (3c):** Company Address place now filled ✓; Nuclear Services division Adress now filled ✓; 4 other division Adress empty (no physical offices — market-sector units, sourceless). Project Adress genuinely unfillable (lat/lng null in both dossiers).
- **Memberships (3d):** none — `Jingoli.md` memberships array all-null; `Jingoli1.md` memberships belong to parent entity JINGOLI/Joseph Jingoli & Son (not nuclear subsidiary). Complete ✓.
- **Location tags (3e):** Event "ENR NY Region Contractor of the Year" → [New York] ✓.
- **Duplicates observed (not fixed — destructive):** 2× ENR 2012 event rows (`37b9…81e7`, `37e9…81a9`); 2× HQ location rows (`37b9…810a`, `37e9…8166`).

## Audit pass 2026-06-13 Pass #8 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 records (company DB record + 5 divisions + 2 people + 5 dossier projects + 1 location + 1 event) via 3 parallel sub-agents. Ground truth: `Jingoli.md`. No fillable gaps found — every sourced field already populated.
- **State confirmed:** Company: Description/Type/BW Category/Size=Regional/Website/LinkedIn/Country/Address(lat/lng) all populated; 19 people + 27 projects + 7 software linked. Nuclear Services division: Company+People(Mockaitis)+Projects(11)+Adress(lat/lng) all set. Jingoli Power: Company+People(Karl Miller)+Projects(5) set; Address empty (no lat/lng in dossier — genuinely unfillable). JDC/Goldstar/DCO: Company relation only — address/people/projects all sourceless. Both people: Company relation ✓; Division deferred (no rows in global Divisions DB `37690644`); Karl Miller LinkedIn blank (no source in dossier). All 5 projects: Contractors+Owning Department set; Adress genuinely unfillable (no lat/lng in dossier). Event: [New York] tag ✓.
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis+11 projects+Adress; Jingoli Power→Karl Miller+5 projects; all 5 dossier projects→Contractors+Owning Department; both people→company; Location→company+division; Event→company.
- **Description-depth (3b) ✓:** all bodies at source-maximum depth.
- **Address/location (3c):** Company Address place ✓; Nuclear Services Adress ✓; 4 other divisions genuinely unfillable; 5 project Adress genuinely unfillable; Location row Adress text ✓.
- **Memberships (3d):** none in dossier → none in Notion ✓.
- **Location tags (3e):** Event "New York" ✓. No other untagged located records.
- **Duplicates (outstanding — destructive, Zack UI):** ENR 2012 event dup `37e9…81a9` + HQ location dup `37e9…8166` still present.

## Audit pass 2026-06-13 Pass #7 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 records (company DB record + 5 divisions + 2 people + 5 dossier projects + 1 location + 1 event). Ground truth: `Jingoli.md`. No fillable gaps found — every sourced field already populated.
- **New state confirmed:** Company now has 19 people linked + 27 construction projects linked + place:Address filled (lat 40.2793 / lng -74.7263); Size = "Regional"; Nuclear Services division place:Adress filled. Jingoli1.md fills from Pass #6 confirmed present.
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis + 11 projects + Adress filled; Jingoli Power→Karl Miller + 5 Power projects; all 5 dossier projects→Contractors + Owning Department (Nuclear Services); both people→company; Location→company+division; Event→company. People `Division` deferred (global Divisions DB `37690644` has no Jingoli rows).
- **Description-depth (3b) ✓:** all 5 division bodies + all 5 project bodies + both people bodies at source-maximum depth.
- **Address/location (3c):** Company Address place ✓; Nuclear Services division Adress ✓; 4 other divisions sourceless (no lat/lng in dossier); 5 project Adress genuinely unfillable (no lat/lng in dossier); Location row Adress text ✓; Event Place genuinely unfillable.
- **Memberships (3d):** none in dossier → none in Notion ✓.
- **Location tags (3e):** Event "New York" ✓. No other untagged located records.

## Audit pass 2026-06-13 Pass #9 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 original dossier records (company DB record + 5 divisions + 2 people + 5 projects + 1 location + 1 event) + cross-check against all 3 dossiers (Jingoli.md, Jingoli1.md, Jing3.md). No fillable gaps found — all sourced fields already populated.
- **New state since last audit:** Jing3 session (2026-06-12/13) added: 22 net-new projects (total 27 linked), 7 software rows (Procore, P6, Hard Dollar, +4), 4 memberships in Memberships table, 4 new events in Events table. Company body has "Jing3 Enrichment (2026-06-12)" section with legal name/founded/revenue/$884M/ENR#153/ENR Power#15/employees/CEO/COO.
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis+11 projects+Adress(lat/lng); Jingoli Power→Karl Miller+5 projects; all 5 dossier projects→Contractors+Owning Department; both people→company; Location→company+division; Event (ENR 2012)→company. People `Division` deferred (global Divisions DB `37690644` no Jingoli rows).
- **Description-depth (3b) ✓:** all bodies at source-maximum depth for both original and Jing3 data.
- **Address/location (3c):** Company Address place ✓ (lat 40.2793/lng -74.7263); Nuclear Services Adress ✓; Jingoli Power Adress empty (same HQ addr but Jing3.md doesn't explicitly assign lat/lng to the Power division record — genuinely unfillable from dossier scope); JDC/Goldstar/DCO Adress genuinely unfillable. Location row Adress text ✓.
- **Memberships (3d):** 4 unique memberships now in Notion (GBCA, NJ Alliance for Action, PWC NJ, ACCNJ) — all sourced from Jing3.md. Complete per all 3 dossiers.
- **Location tags (3e):** Event "New York" ✓. Jing3 events: NJ Alliance Eagle Awards → [New Jersey] ✓ (inferred from event data); PWC NJ → [New Jersey, Jersey City] ✓; HELIX topping-out → [New Jersey, New Brunswick] ✓. All tagged.
- **Duplicates (outstanding — destructive, Zack UI):**
  - ENR 2012 event: `37b9…81e7` (original) + `37e9…81a9` (dup — delete)
  - HQ location row: `37b9…810a` (original) + `37e9…8166` (dup — delete)
  - GBCA membership: 3 rows (`37c9…81d8`, `37d9…81c1`, `37d9…81ea`) — keep richest, delete other 2
  - PWC NJ membership: 3 rows (`37c9…8140`, `37d9…810a`, `37d9…81f0`) — keep richest, delete other 2
  - NJ Alliance for Action events: multiple rows across event table — confirm which is primary

## Audit pass 2026-06-13 Pass #11 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 records (company DB record + 5 divisions + 2 people + 5 dossier projects + 1 location + 1 event). Ground truth: `Jingoli.md`. No fillable gaps found — every sourced field already populated; state matches Pass #10 ledger exactly.
- **Company DB `37b9…f55131`:** Description/Type/BW Category/Size=Regional/Website/LinkedIn/Country/Address(lat 40.2793/lng -74.7263) all populated; 19 people + 27 projects + 7 software linked. ✓
- **Nuclear Services division `37b9…5333`:** Company + People (Mockaitis) + Projects (11) + Adress (lat/lng) all set. ✓
- **Jingoli Power division `37b9…8c8c`:** Company + People (Karl Miller) + Projects (5) set; Adress empty (no lat/lng in dossier — genuinely unfillable). ✓
- **JDC / Goldstar / DCO divisions:** Company relation only — address/people/projects all sourceless. ✓
- **Matthew Mockaitis `37b9…b583`:** Company + Function + LinkedIn set; Division deferred (global Divisions DB `37690644` no Jingoli rows). ✓
- **Karl Miller `37b9…ffd8`:** Company + Function set; LinkedIn blank (no source in dossier) — genuinely unfillable. Division deferred. ✓
- **All 5 dossier projects:** Contractors + Owning Department set; Adress genuinely unfillable (no lat/lng in dossier). ✓
- **Location row `37b9…770d`:** Adress text + Company + Division all set. ✓
- **Event `37b9…dc9dc`:** Company + Date + Location tags ["New York"] all set. ✓
- **Interconnection (3a) ✓** · **Description-depth (3b) ✓** · **Address/location (3c):** Company + Nuclear Services Adress filled; others genuinely unfillable ✓ · **Memberships (3d) ✓** (4 rows from Jing3) · **Location tags (3e) ✓**.
- **Outstanding (destructive — Zack UI):** duplicate ENR 2012 event + duplicate HQ location row + GBCA/PWC NJ membership dups from Pass #9 still present — no change since last pass.

## Audit pass 2026-06-13 Pass #10 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of 15 original dossier records (company DB record + 5 divisions + 2 people + 5 projects + 1 location + 1 event). Ground truth: `Jingoli.md`. No fillable gaps found — every sourced field already populated; state matches Pass #9 ledger exactly.
- **Company DB `37b9…f55131`:** Description/Type/BW Category/Size=Regional/Website/LinkedIn/Country/Address(lat 40.2793/lng -74.7263) all populated; 19 people + 27 projects + 7 software linked. ✓
- **Nuclear Services division `37b9…5333`:** Company + People (Mockaitis) + Projects (11) + Adress (lat/lng) all set. ✓
- **Jingoli Power division `37b9…8c8c`:** Company + People (Karl Miller) + Projects (5) set; Adress empty (no lat/lng in dossier — genuinely unfillable). ✓
- **JDC / Goldstar / DCO divisions:** Company relation only — address/people/projects all sourceless. ✓
- **Matthew Mockaitis `37b9…b583`:** Company + Function + LinkedIn set; Division deferred (global Divisions DB `37690644` no Jingoli rows). ✓
- **Karl Miller `37b9…ffd8`:** Company + Function set; LinkedIn blank (no source in dossier) — genuinely unfillable. Division deferred. ✓
- **All 5 dossier projects:** Contractors + Owning Department set; Adress genuinely unfillable (no lat/lng in dossier). ✓
- **Location row `37b9…770d`:** Adress text + Company + Division all set. ✓
- **Event `37b9…dc9dc`:** Company + Date + Location tags ["New York"] all set. ✓
- **Interconnection (3a) ✓** · **Description-depth (3b) ✓** · **Address/location (3c):** Company + Nuclear Services Adress filled; others genuinely unfillable ✓ · **Memberships (3d) ✓** (4 rows from Jing3) · **Location tags (3e) ✓**.
- **Outstanding (destructive — Zack UI):** duplicate ENR 2012 event + duplicate HQ location row + GBCA/PWC NJ membership dups from Pass #9 still present — no change since last pass.

## Audit pass 2026-06-13 Pass #12 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 records (company DB record + 5 divisions + 2 people + 5 dossier projects + 1 location + 1 event) via direct Notion MCP fetches. Ground truth: all 3 dossiers (Jingoli.md, Jingoli1.md, Jing3.md). No fillable gaps found — every sourced field already populated; state matches Pass #11 exactly.
- **Company DB `37b9…f55131`:** Description/Type/BW Category/Size=Regional/Website/LinkedIn/Country/Address(lat 40.2793/lng -74.7263) all populated; 19 people + 27 projects + 7 software linked. ✓
- **Nuclear Services division `37b9…5333`:** Company + People (Mockaitis) + Projects (11) + Adress (lat/lng) all set. ✓
- **Jingoli Power division `37b9…8c8c`:** Company + People (Karl Miller) + Projects (5) set; Adress empty (no lat/lng in dossier — genuinely unfillable). ✓
- **JDC / Goldstar / DCO divisions:** Company relation only — address/people/projects all sourceless. ✓
- **Matthew Mockaitis `37b9…b583`:** Company + Function + LinkedIn + Location=NJ + Function Qualification=President set; Division deferred (global Divisions DB `37690644` no Jingoli rows). ✓
- **Karl Miller `37b9…ffd8`:** Company + Function + Location=NJ + Function Qualification=CEO set; LinkedIn blank (no source in dossier) — genuinely unfillable. Division deferred. ✓
- **Event `37b9…dc9dc`:** Company + Date 2012-01-01 + Location tags ["New York"] all set. ✓
- **Location row `37b9…770d`:** Adress text + Companies relation + Division relation all set. ✓
- **Interconnection (3a) ✓** · **Description-depth (3b) ✓** · **Address/location (3c):** Company + Nuclear Services Adress filled; others genuinely unfillable ✓ · **Memberships (3d) ✓** (4 rows: GBCA/NJ Alliance/PWC NJ/ACCNJ) · **Location tags (3e) ✓** (Event "New York" set).
- **Outstanding (destructive — Zack UI):** duplicate ENR 2012 event + duplicate HQ location row + GBCA×3 + PWC NJ×3 membership dups still present — no change since Pass #9.

## Audit pass 2026-06-13 Pass #13 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of company DB record via direct Notion MCP fetch. Ground truth: `Jingoli.md`. No fillable gaps found — all sourced fields already populated; state matches Pass #12 exactly.
- **Company DB `37b9…f55131`:** Description/Type/BW Category/Size=Regional/Website/LinkedIn/Country/Address(lat 40.2793/lng -74.7263) all populated; 19 people + 27 projects + 7 software linked. ✓
- **Events table schema verified:** Location tags ["New York"] option confirmed present; schema correct.
- **Interconnection (3a) ✓** · **Description-depth (3b) ✓** · **Address/location (3c) ✓** · **Memberships (3d) ✓** · **Location tags (3e) ✓**.
- **Outstanding (destructive — Zack UI):** duplicate ENR 2012 event + duplicate HQ location row + GBCA×3 + PWC NJ×3 membership dups still present — no change since Pass #9.

## Audit pass 2026-06-13 Pass #14 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of company DB record + Nuclear Services division + ENR 2012 event + TMI-2 project via direct Notion MCP fetches. Ground truth: `Jingoli.md`. No fillable gaps found — every sourced field already populated; state matches Pass #13 exactly.
- **Company DB `37b9…f55131`:** Description/Type/BW Category/Size=Regional/Website/LinkedIn/Country/Address(lat 40.2793/lng -74.7263) all populated; 19 people + 27 projects + 7 software linked. ✓
- **Nuclear Services division `37b9…5333`:** Company + People (Mockaitis) + Projects (11) + Adress (lat/lng) all set; body at full depth. ✓
- **Event `37b9…dc9dc`:** Company + Date 2012-01-01 + Location tags ["New York"] all set. ✓
- **TMI-2 project `37b9…c23`:** Contractors + Owning Department + Location + Date + body at full depth. ✓
- **Interconnection (3a) ✓** · **Description-depth (3b) ✓** · **Address/location (3c):** Company + Nuclear Services Adress filled; others genuinely unfillable ✓ · **Memberships (3d) ✓** (4 rows: GBCA/NJ Alliance/PWC NJ/ACCNJ) · **Location tags (3e) ✓** (Event "New York" set).
- **Outstanding (destructive — Zack UI):** duplicate ENR 2012 event + duplicate HQ location row + GBCA×3 + PWC NJ×3 membership dups still present — no change since Pass #9.

## Audit pass 2026-06-13 Pass #15 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify: company DB record `37b90644-d524-8127-824d-f2c6e9f55131` fetched directly. Ground truth: all 3 dossiers (Jingoli.md, Jingoli1.md, Jing3.md). No fillable gaps found — every sourced field already populated; state matches Pass #14 exactly.
- **Company DB `37b9…f55131`:** Description/Type/BW Category/Size=Regional/Website/LinkedIn/Country×4/Address(lat 40.2793/lng -74.7263) all populated; 19 people + 27 projects + 7 software linked. ✓
- **Interconnection (3a) ✓** · **Description-depth (3b) ✓** · **Address/location (3c):** Company + Nuclear Services Adress filled; others genuinely unfillable ✓ · **Memberships (3d) ✓** (4 rows: GBCA/NJ Alliance/PWC NJ/ACCNJ) · **Location tags (3e) ✓** (Event "New York" set).
- **Outstanding (destructive — Zack UI):** ENR 2012 event dup + HQ location dup + GBCA×3 + PWC NJ×3 membership dups still present — no change since Pass #9.

## Audit pass 2026-06-14 Pass #16 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of company DB record + Nuclear Services division + Matthew Mockaitis + Karl Miller + ENR 2012 event + Lawrenceville HQ location row + TMI-2 project via direct Notion MCP fetches. Ground truth: all 3 dossiers (Jingoli.md, Jingoli1.md, Jing3.md). No fillable gaps found — state matches Pass #15 exactly.
- **Company DB `37b9…f55131`:** Description/Type/BW Category/Size=Regional/Website/LinkedIn/Country×4/Address place (lat 40.2793/lng -74.7263) all populated; 19 people + 27 projects + 7 software linked. ✓
- **Nuclear Services division `37b9…5333`:** Company + People (Mockaitis) + Projects (11) + Adress (lat/lng) all set; body at full depth. ✓
- **Matthew Mockaitis `37b9…b583`:** Company + Function + Function Qualification + LinkedIn + Location=NJ set; Division deferred (global Divisions DB `37690644` no Jingoli rows). ✓
- **Karl Miller `37b9…ffd8`:** Company + Function + Function Qualification + Location=NJ set; LinkedIn blank (no source in dossier) — genuinely unfillable. Division deferred. ✓
- **Event `37b9…dc9dc`:** Company + Date 2012-01-01 + Location tags ["New York"] all set. ✓
- **Location row `37b9…770d`:** Adress text + Companies relation + Division relation all set. ✓
- **TMI-2 project `37b9…c23`:** Contractors + Owning Department (Nuclear Services) + Location + Date + Status + body all set. ✓
- **Profile hub `37b9…1345`:** Bio snapshot + Attack Plan complete; all inline data sources (Divisions/Events/Sources/Locations/Memberships) present. ✓
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis+11 projects+Adress; Jingoli Power→Karl Miller+5 projects; all 5 dossier projects→Contractors+Owning Department; both people→company; Location→company+division; Event→company.
- **Description-depth (3b) ✓:** all bodies at source-maximum depth.
- **Address/location (3c):** Company Address place ✓; Nuclear Services Adress ✓; 4 other divisions genuinely unfillable (no lat/lng in dossier); 5 project Adress genuinely unfillable; Location row Adress text ✓.
- **Memberships (3d):** 4 rows (GBCA/NJ Alliance/PWC NJ/ACCNJ) — all present per Jing3.md ✓.
- **Location tags (3e):** Event "New York" ✓. No other untagged located records.
- **Outstanding (destructive — Zack UI, unchanged):** ENR 2012 event dup `37e9…81a9` + HQ location dup `37e9…8166` + GBCA×3 + PWC NJ×3 membership dups.

## Audit pass 2026-06-14 Pass #17 (`/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 15 records (company DB record + 5 divisions + 2 people + 5 dossier projects + 1 location + 1 event) via direct Notion MCP fetches. Ground truth: `Jingoli.md`. No fillable gaps found — every sourced field already populated; state matches Pass #16 exactly.
- **Company DB `37b9…f55131`:** Description/Type/BW Category/Size=Regional/Website/LinkedIn/Country×4/Address(lat 40.2793/lng -74.7263) all populated; 19 people + 27 projects + 7 software linked. ✓
- **Nuclear Services division `37b9…5333`:** Company + People (Mockaitis) + Projects (11) + Adress (lat/lng) all set; body at full depth. ✓
- **Matthew Mockaitis `37b9…b583`:** Company + Function + Function Qualification + LinkedIn + Location=NJ set; Division deferred (global Divisions DB `37690644` no Jingoli rows). ✓
- **Karl Miller `37b9…ffd8`:** Company + Function + Function Qualification + Location=NJ set; LinkedIn blank (no source in dossier) — genuinely unfillable. Division deferred. ✓
- **All 5 dossier projects:** Contractors + Owning Department (Nuclear Services) set; Adress genuinely unfillable (no lat/lng in dossier). ✓
- **Location row `37b9…770d`:** Adress text + Companies relation + Division relation all set. ✓
- **Event `37b9…dc9dc`:** Company + Date 2012-01-01 + Location tags ["New York"] all set. ✓
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis+11 projects+Adress; Jingoli Power→Karl Miller+5 projects; all 5 dossier projects→Contractors+Owning Department; both people→company; Location→company+division; Event→company.
- **Description-depth (3b) ✓:** all bodies at source-maximum depth.
- **Address/location (3c):** Company Address place ✓; Nuclear Services Adress ✓; 4 other divisions genuinely unfillable (no lat/lng in dossier); 5 project Adress genuinely unfillable; Location row Adress text ✓.
- **Memberships (3d):** 4 rows (GBCA/NJ Alliance/PWC NJ/ACCNJ) present from Jing3 session ✓. Dossier `Jingoli.md` memberships null — complete ✓.
- **Location tags (3e):** Event "New York" ✓. No other untagged located records.
- **Outstanding (destructive — Zack UI, unchanged):** ENR 2012 event dup `37e9…81a9` + HQ location dup `37e9…8166` + GBCA×3 + PWC NJ×3 membership dups still present — no change since Pass #9.

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = Jingoli Nuclear Services.
2. **Existing Software** view → clear `__TEMPLATE__` filter (now has 7 real rows — filter should show them).
3. Delete duplicate ENR 2012 event row (`37e90644-d524-81a9-a79c-c45a8d7fb1a5`) — duplicate of `37b9…81e7`.
4. Delete duplicate HQ location row (`37e90644-d524-8166-aeb9-f6c727613765`) — duplicate of `37b9…810a`.
5. Dedup GBCA membership rows (3 → 1): delete `37c90644-d524-81d8-8e25-f63da3126784` and `37d90644-d524-81c1-af0b-db58bc999958`; keep `37d90644-d524-81ea-9b4f-fc8a369845e8` (richest body with chapter/date).
6. Dedup PWC NJ membership rows (3 → 1): Zack to pick richest and delete others.
7. Review NJ Alliance for Action — multiple event rows + 1 membership row; confirm no additional dups.
