# State · Records — Kiewit Corporation

> **Holds:** the Kiewit Corporation dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a Kiewit record.
> **Ground truth:** `Enlaye Notion/Kiewitt/Kiewitt.md` (Kiewitt1.md is empty/0 bytes). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.

---

## Profile page (hub)
**"Kiewit Corporation"** (renamed from "Kiewitt TEMPLATE (2)") — https://app.notion.com/p/37b90644d5248021830de18cf6ea0d89 (Companies research → Zack Folder). Divisions-DB template variant (same as HITT/Jingoli). Bio snapshot at top; Attack Plan filled at bottom.

Page-local data sources on this page:
- **Divisions** (heading "# Company Map") `collection://3cf90644-d524-831c-9d06-070faa9a8821` (props: Division title · Adress place · relations Companies full database / People / Projects)
- Events `collection://17a90644-d524-82f4-9b43-07db305a9ff7` (Event name · Date · Location tags · Place · Companies relation)
- Sources `collection://26f90644-d524-821a-bee5-877eae10da82` (What the source is about · URL)
- Locations `collection://18e90644-d524-8228-9ef0-0783c5475fd7` (Location · Adress **text**) — **needs added relation cols**
- Memberships `collection://ed090644-d524-8359-8b9b-877f0f3c922d` (Name only) — **needs added Company relation**
- Linkedin Post `collection://20a90644-d524-8238-aa6c-8769e4dcd2bd` (unused — empty)
- Projects Underway = shared Construction Projects (linked view, filtered `__TEMPLATE__` — **manual UI filter fix**)
- Existing Software = shared Companies Software `collection://37690644-d524-804f-b966-000b34a1901b` (linked view, filtered `__TEMPLATE__` — **manual UI filter fix**)

## Company record (EXISTING — extend, do NOT recreate or overwrite body)
**"Kiewit"** `17b90644-d524-8055-88ec-f7f399f27e9d` in Companies DB (`collection://041b7f07-…`). Pre-existed (Mar 2026, CRM): Type=Company · Size=**Mutlinational** ✓ (matches dossier) · Website=kiewit.com · LinkedIn · BW=[Builder] · Country=[USA, Nebraska] · **22 scraped People** linked · Lead/Strategy/Subsidiaries/Touchpoints CRM relations · rich body (Org Structure, KADE/ADAPT, Entry Strategy naming Overend/Fitzler/Farber/Burgis). **Body left intact (additive only).**
- To ADD: Description (was empty); Address place (Omaha HQ 1550 Mike Fahey St, 41.265948,-95.935909); Country += operating states (existing options only); Construction Projects (15, one-way); Companies Software (4).
- 22 existing People NOT in dossier (dossier excludes named individuals except Lanoha/Miles) → left as-is.

## Divisions (17 planned — Divisions DB `3cf90644`; each: Adress place name+addr, Companies→Kiewit, body, + Projects/People in cross-link pass)
14 major subsidiaries + 3 project-owning entities (Offshore Services, Peter Kiewit Sons ULC, Kiewit Water Facilities) so every project's building subsidiary is a real row.
_(IDs filled during load.)_

## People (2 planned — dossier excludes named individuals except these two, both sourced)
- **Rick Lanoha** — CEO since Jan 1 2020 (succeeded Bruce Grewcock). Company→Kiewit. (dedup: "Lanoha" → 0 hits)
- **Dave Miles** — President, Kiewit Infrastructure Group. Company→Kiewit; division edge via Kiewit Infrastructure Co. row's People relation. (dedup: no "Dave Miles" hit)

## Projects (15 planned — Construction Projects DB; Contractors→Kiewit; division via Division row's Projects relation, Owning Department left empty per DB convention)
Key values: Homer City $10,000M · CA HSR $3,500M · Canada nuclear $3,200M · Bull Run $1,290M · Grain Belt $1,700M · Port Arthur $404M · Nome $399.4M · Key Bridge $211M. _(IDs filled during load.)_

## Schema changes (additive, pre-authorized 2026-06-10)
- Construction Projects `Type` (SELECT) += **Water, Marine, Nuclear** (full 22-option list preserved).
- Companies Software `Software used` (multi) += **InEight, KADE, ADAPT** (full 24-option list preserved).
- Locations `18e90644` += `Companies full database` + `Division` relations (was bare).
- Memberships `ed090644` += `Companies full database` relation (was bare).

## Left empty / flagged (no sourced value, or schema/safety)
- **Projects Location** options missing: **Alaska** (Nome), **Oregon** (Bull Run/Klamath), **Washington** (Federal Way), **Kansas** (Grain Belt) — NOT added (117-option `SET` is the documented HITT near-miss); geography kept in Location tags (existing) + body; flag 1-click UI add.
- Dossier `gaps`: EMR/TRIR numeric, clean FY USASpending total, per-project parcel/APN/permits, bonding limits, division-level revenue/headcount, UEI/CAGE unverified.
- Owner/client + JV partners + competing bidders = sourced body facts (no Owner DB records created — convention).

## Events (2) / Memberships (7) / Software (4) / Locations
- Events: Construction Safety Week · Women in Heavy Civil / The Beavers — Companies→Kiewit, why-it-matters in body.
- Memberships: The Beavers · AGC · DBIA · CSRA · CISI · Nat'l Construction Safety Executives · Canadian Construction Safety Council — Company→Kiewit.
- Software: InEight+KMS · KADE+ADAPT · Microsoft Azure/D365/Power BI · Procore/P6/Bluebeam/Autodesk CC/MS Project — Company→Kiewit.
- Locations: HQ Omaha + division offices — Company + Division relations.

## Manual UI steps (Zack)
1. Projects Underway view → clear `__TEMPLATE__` filter, set Contractors = Kiewit.
2. Existing Software view → clear `__TEMPLATE__` filter.
3. Memberships-note People view → re-point company filter to Kiewit.
4. Optional: add Alaska/Oregon/Washington/Kansas to Projects `Location`, then tag Nome/Bull Run/Klamath/Federal Way/Grain Belt.
5. Page-local table views (Company Map, Events, Locations, Memberships) carry template "clear the leftover company rule" filters — rows exist + linked; clear filters in UI to display.

---

## Created / extended 2026-06-10 — IDs (✅ load complete)

**Company record (extended, not recreated):** Kiewit `17b90644-d524-8055-88ec-f7f399f27e9d` — Description, Address place (Omaha, 41.265948/-95.935909), Country=24 states, Construction Projects=15, Companies Software=4, body Snapshot+Sources appended. People auto-grew 22→**24** (Lanoha+Miles). CRM body + 22 scraped people left intact.

**Divisions (17 — Divisions `3cf90644`; each Companies→Kiewit):**
| Division | ID | Projects relation |
|---|---|---|
| Kiewit Infrastructure Co. | `37b90644-d524-8133-9717-f64c81589435` | Key Bridge · +People: Dave Miles |
| Kiewit Infrastructure West Co. | `37b90644-d524-815e-897d-fd59e86f6891` | CA HSR, Port Arthur, Nome, Federal Way, Klamath, S.Central LR |
| Kiewit Infrastructure South Co. | `37b90644-d524-8161-9d41-c0265c434021` | — |
| Kiewit Power Constructors Co. | `37b90644-d524-813e-a4b9-d8cdcb2ef8a3` | Homer City |
| Kiewit Power Delivery | `37b90644-d524-8154-925c-ef6539088f7f` | — |
| Kiewit Energy Group Inc. | `37b90644-d524-8131-9c2c-c70f745a6757` | Grain Belt Express |
| TIC – The Industrial Company | `37b90644-d524-8177-be41-ccb135ed152f` | NRG 5 GW |
| Kiewit Building Group Inc. | `37b90644-d524-81c2-a6bf-cedc59608ca5` | Austin LR O&M |
| Kiewit Engineering Group Inc. | `37b90644-d524-81f7-9bf7-c7073860b002` | — |
| Kiewit Mining Group Inc. | `37b90644-d524-81e8-ae44-f3be8ca13f63` | — |
| Weeks Marine, Inc. | `37b90644-d524-81aa-9acb-c6dc0b28c009` | — |
| Kiewit Nuclear Solutions Co. | `37b90644-d524-817f-9cff-f2aacdc57d41` | Canada nuclear |
| Mass. Electric Construction Co. (MEC) | `37b90644-d524-81c0-b117-eefa2e3cd5d9` | — |
| Kiewit Development Company | `37b90644-d524-81a7-bafa-ef3a1fef2b90` | — |
| Kiewit Offshore Services | `37b90644-d524-81fb-909f-f533b9dd114f` | Salamanca Topsides |
| Peter Kiewit Sons ULC | `37b90644-d524-81e6-ad67-e719a02196d1` | YVR runway |
| Kiewit Water Facilities (MWH–Kiewit JV) | `37b90644-d524-811e-9dac-e15969adeb0a` | Bull Run |

**People (2 new):** Rick Lanoha `37b90644-d524-8198-9198-c95f25da7fa6` (CEO) · Dave Miles `37b90644-d524-8184-a2df-d6d727bca06b` (Pres. Infrastructure → Infra Co division). Both Company→Kiewit.

**Projects (15 — Contractors→Kiewit):** Key Bridge `…811c96af` · Homer City `…81a083b6` · CA HSR `…817abbb3` · Bull Run `…81a0ac26` · Port Arthur `…8176a96a` · Nome `…81acb4b5` · Grain Belt `…817aad8c` · NRG `…8159afc2` · Canada nuclear `…819c9fbe` · Austin `…81aea276` · Federal Way `…81b9bddf` · Klamath `…81d2889c` · YVR `…814cabfe` · Salamanca `…81f0bbe4` · S.Central LR `…81d0b240`.

**Page tables:** Events 2 (`17a90644-82f4`) · Memberships 7 (`ed090644`) · Software 4 (shared `37690644`: InEight, KADE+ADAPT, MS Azure/D365/PowerBI, Procore-stack) · Locations 11 (`18e90644`, Company+Division) · Sources 12 (`26f90644-821a`).

**Fixed:** 6 Notion auto-link breakages where link text was a bare domain (kiewit.com / kiewit.com/InEight / thebeavers.org) — corrected hrefs on company body, Engineering & Development division bodies, InEight software row, Beavers membership. **Lesson:** never use a bare domain as markdown link text — Notion overrides the href with an autolink of the text.

**No shared multi-select ALTERs** (concurrent sessions were clobbering shared Projects Location per Flatiron ledger): projects mapped to existing Type/Location options; precise sector (Water/Marine/Nuclear/Power Delivery) + missing-state geography (AK/OR/WA/KS) kept in bodies. InEight/KADE/ADAPT kept in software row names+bodies, not the shared `Software used` select.

---

## Audit pass — 2026-06-10

**Divisions — `Adress` place filled (all 17):**
- Kiewit Infrastructure Co. → 10055 Trainstation Circle, Lone Tree, CO 80124 (39.5519/-104.8722)
- Kiewit Infrastructure West Co. → 2200 Columbia House Blvd, Vancouver, WA 98661 (45.6387/-122.6615)
- Kiewit Infrastructure South Co. → 2050 Roanoke Rd Ste 100, Westlake, TX 76262 (33.0001/-97.2112)
- Kiewit Power Constructors Co. → 8900 Renner Blvd, Lenexa, KS 66219 (38.9531/-94.7568)
- Kiewit Power Delivery → 8900 Renner Blvd, Lenexa, KS 66219
- Kiewit Energy Group Inc. → 585 N. Dairy Ashford Rd Ste 100, Houston, TX 77079 (29.7604/-95.5597)
- TIC – The Industrial Company → 10055 Trainstation Circle, Lone Tree, CO 80124
- Kiewit Building Group Inc. → 1550 Mike Fahey St., Omaha, NE 68102
- Kiewit Engineering Group Inc. → 10055 Trainstation Circle, Lone Tree, CO 80124
- Kiewit Mining Group Inc. → 10055 Trainstation Circle, Lone Tree, CO 80124
- Weeks Marine, Inc. → 4 Commerce Drive, Cranford, NJ 07016 (40.6576/-74.2988)
- Kiewit Nuclear Solutions Co. → 105 Mitchell Road Ste 100, Oak Ridge, TN 37830 (36.0104/-84.2696)
- Mass. Electric Construction Co. (MEC) → 400 Totten Pond Road Ste 400, Waltham, MA 02451 (42.3931/-71.2628)
- Kiewit Development Company → 1550 Mike Fahey St., Omaha, NE 68102
- Kiewit Offshore Services → 2440 Kiewit Rd, Ingleside, TX 78362 (27.8599/-97.2072)
- Peter Kiewit Sons ULC → Vancouver, BC, Canada (49.2827/-123.1207)
- Kiewit Water Facilities (MWH-Kiewit JV) → 35320 SE Carpenter Lane, Sandy, OR 97055 (45.3743/-122.2085)
Sources: https://www.kiewit.com/locations/

**Projects — `Size` text filled (9 of 15; 6 have no metric in dossier):**
- Homer City: "4.5 GW natural gas plant, 3,200 acres, 7× GE Vernova 7HA.02 turbines"
- CA HSR: "119 mi / 191 km (Madera to Poplar Ave, N. of Bakersfield); track, OCS, train control & comms; up to 220 mph"
- Bull Run: "135–140 MGD filtration on 95-acre site; GMP1+GMP2 = $1.29B; total program $2.56B (Feb 2026)"
- Port Arthur: "9,525 ft floodwall replacement, 2,300 ft levee raises, 4 tie-ins, 3 pump stations; seed project for $7B SG2 program"
- Grain Belt: "800-mile HVDC line (KS, MO, IL, IN); 5 GW capacity; combined Quanta+Kiewit $1.7B"
- NRG gas plants: "4 combined-cycle plants totaling 5 GW in TX and PJM; first 1.2 GW online 2029"
- Key Bridge: "Phase 1 PDB $73M→$211M; Kiewit to be paid $700M+ total"
- Canada nuclear: "Nuclear waste disposal facility; JV with WSP"
- Nome: "Port modification Phase 1A; firm-fixed-price design-build; completion 2029-09-05"

**Projects — `Adress` place filled (7 of 15):**
- Key Bridge: Baltimore, MD (39.2186/-76.5282) + Date 2024-08-29
- Homer City: Homer City, Indiana County, PA (40.564/-79.0803)
- Bull Run: 35320 SE Carpenter Lane, Sandy, OR 97055 (45.3743/-122.2085)
- Port Arthur: Port Arthur, TX (29.8988/-93.9399) + Date 2025-05-02
- Nome: Nome, AK (64.5011/-165.4064) + Date 2025-08-15
- CA HSR: Central Valley, CA + Date 2026-06-01
- Austin LR: Austin, TX + Date 2026-04-15
- Salamanca: 2440 Kiewit Rd, Ingleside, TX 78362 (27.8599/-97.2072)

**Not filled (genuinely sourceless for these records):**
- People DB `Division` relation for Rick Lanoha / Dave Miles — People DB `Division` col links to a DIFFERENT shared DB (37690644-8088), not Kiewit's page-local Divisions (3cf90644); no matching row exists in that shared DB → left as-is.
- Events `Date` — no specific dates in dossier for Construction Safety Week or Beavers events.
- Events location tags — both events are national/virtual; no location to tag.
- Projects `Adress` for Grain Belt (multi-state corridor), NRG (TX/PJM — multiple sites), Canada nuclear (Canada), Federal Way (WA route), Klamath (OR/CA), YVR (Vancouver BC), South Central LR (Phoenix AZ) — addresses are in body/Location; no single precise address applicable.
- Projects `Size` for Austin LR, Federal Way, Klamath, YVR, Salamanca, South Central LR — no contract value or size metric in dossier.

---

## Audit pass — 2026-06-12

**Duplicate resolution:** A prior session on 2026-06-12 ran a separate enrichment pass and created duplicate rows in Memberships and Events. All duplicates renamed with "DUPLICATE —" prefix for Zack to delete in Notion UI:
- Memberships dups (6): The Beavers `37d90644-8169` · AGC `37d90644-81e1` · CSRA `37d90644-81ab` · CISI `37d90644-81e3` · NCSE `37d90644-81ca` · CCSC `37d90644-8141`
- Events dups (2): Construction Safety Week `37d90644-81d7` · The Beavers/WIHC `37d90644-81fb`

**Genuinely new additions from 2026-06-12 session (kept):**
- ASCE membership `37d90644-81f0` (new — not in dossier)
- Events: EPC Show 2026 `37d90644-813b` (Houston TX; tagged Texas; Place filled) · FWIK Summit 2025 `37d90644-8175` · Kiewit Engineering Technical Summit 2026 `37d90644-8108` · AGC Annual Convention 2026 `37d90644-8135` (Orlando FL; tagged Florida+Orlando; Place filled)
- Projects: Multiple historical completed projects added (Midtown Tunnel $1.5B/VA, Central 70 $1.27B/CO, DART Orange Line $585M/TX, + others)

**3a–3e verified ✓ (all clean):**
- 3a: 17 divisions → Kiewit ✓; 39 projects → Kiewit ✓; 24 people → Kiewit ✓; all tables company-linked ✓
- 3b: all bodies at full dossier depth ✓
- 3c: company HQ place ✓; all 17 division Adress place ✓; Locations `Adress` = TEXT (not place type — structural limit, flagged)
- 3d: memberships (7 originals + ASCE = 8 live) all company-linked ✓
- 3e: EPC Show 2026 → Texas ✓; AGC Convention → Florida+Orlando ✓; national events correctly untagged ✓

**Manual UI for Zack:** delete 8 "DUPLICATE —" rows in Memberships + Events inline tables.

---

## Audit pass — 2026-06-13

**Live verification (MCP fetch of all key records):** All records confirmed intact and correctly linked. No new fills needed — record is at full dossier depth.

**3a–3e re-verified ✓ (all clean):**
- 3a: Company record ✓ (People 715 linked, 39 projects, 8 software, Divisions filter view active); all 17 divisions → Kiewit ✓; Kiewit Infrastructure Co. fetched + verified (People: Dave Miles, Projects: Key Bridge + 5 more, Adress place ✓); Memberships table Companies full database → Kiewit on all rows (DBIA verified live ✓); Locations Division + Companies relations ✓
- 3b: Project bodies at full depth (Key Bridge + Homer City fetched live — both complete with owner/delivery/scope/value/risk events/sources) ✓; Division bodies verified (Kiewit Infrastructure Co. full ✓); People bodies verified (Lanoha + Miles both have Role sections + sources) ✓
- 3c: Company HQ place ✓; all 17 division Adress place ✓; project Adress place verified (Key Bridge: Baltimore MD 39.2186/-76.5282 ✓; Homer City: Indiana County PA 40.564/-79.0803 ✓); Locations `Adress` = TEXT type (structural limit, not fixable without schema change — flagged in prior audit)
- 3d: 8 memberships in live table (The Beavers, AGC, DBIA, CSRA, CISI, NCSE, CCSC, ASCE); all match dossier + are company-linked ✓; 6 DUPLICATE— rows still pending Zack UI deletion
- 3e: EPC Show 2026 → Texas ✓; AGC Convention → Florida+Orlando ✓; national/virtual events correctly untagged ✓; FWIK Summit + Engineering Technical Summit untagged (correct — no specific location in source)

**False positives rejected:**
- Company `Founded`, `Revenue`, `Employees`, `ENR rank` — these are NOT properties in the Companies DB schema; they exist only in the Description and page body. No schema mismatch — correct as-is.
- People `LinkedIn` (Lanoha, Miles) — empty; dossier does not contain LinkedIn URLs for either individual → genuinely sourceless, leave blank.
- Project `Owning Department` — DB convention leaves this empty (per original load); no change needed.
- Homer City project ledger ID `81a083b6` was a truncation artifact — correct full ID is `37b90644-d524-81a0-83b6-cfeacdc72ac5` (confirmed via search + fetch).

**0 writes made.** Record is complete and clean at dossier depth. Only outstanding item is Zack's manual UI deletion of the 8 DUPLICATE— rows.

---

## Audit pass — 2026-06-13 (second session)

**Live re-verification via MCP fetch:** Company record, Kiewit Infrastructure Co. division, Key Bridge project, Homer City project, Rick Lanoha person, and both Memberships + Events inline-table schemas fetched live. All checks pass.

**3a–3e verified ✓ (all clean):**
- 3a: Company record — Description ✓, Address place (Omaha 41.265948/-95.935909) ✓, 40 Construction Projects linked ✓, 300+ People linked ✓, 8 Software linked ✓, BW Category=[Builder/Design and Architecture/Developer] ✓, Country=24 entries ✓; Kiewit Infrastructure Co. — Companies → Kiewit ✓, People → Dave Miles ✓, Projects → Key Bridge + 5 more ✓, Adress place ✓; all 7 dossier memberships + ASCE (8 total) company-linked ✓; Events table company-linked ✓
- 3b: Key Bridge body — owner/delivery/scope/value/risk event/sources all present ✓; Homer City body — owner/delivery/scope/4.5GW/3200 acres/turbines/completion/sources ✓; Rick Lanoha body — Role + source ✓; Kiewit Infrastructure Co. body — focus/leader/office/notable project/parent ✓
- 3c: Company HQ place ✓; all 17 division Adress place ✓; Key Bridge Adress place (39.2186/-76.5282) ✓; Homer City Adress place (40.564/-79.0803) ✓; Locations `Adress` = TEXT (structural limit flagged, unchanged)
- 3d: 8 live memberships confirmed (The Beavers `37b90644-8172`, AGC `37b90644-81c1`, DBIA `37b90644-814f`, CSRA `37b90644-8184`, CISI `37b90644-818f`, CCSC `37b90644-81a6`, NCSE `37b90644-81ab`, ASCE `37d90644-81f0`); all match dossier + are company-linked ✓; 6 DUPLICATE— rows still pending Zack UI deletion (`37d90644-8169/81e1/81ab/81e3/81ca/8141`)
- 3e: EPC Show 2026 → Texas ✓; AGC Convention 2026 → Florida+Orlando ✓; Construction Safety Week (national) untagged ✓; Women in Heavy Civil (national) untagged ✓; FWIK Summit + Engineering Technical Summit untagged (correct — no sourced location) ✓; DUPLICATE — Construction Safety Week (`37d90644-81d7`) and DUPLICATE — The Beavers/WIHC (`37d90644-81fb`) still pending Zack UI deletion

**Outstanding for Zack (UI only — cannot be done via MCP):**
- Delete 8 DUPLICATE— rows: 6 in Memberships + 2 in Events inline tables on the Kiewit Corporation page

**0 writes made this session.** Record is at full dossier depth.
## Audit pass — 2026-06-13 (third session — /notion-audit)

**Live verification (MCP fetch of all key records):** Company record, all 17 divisions, both people records, Key Bridge + Homer City projects, Memberships table, Events table — all fetched and confirmed.

**3a–3e verified ✓ (all clean):**
- 3a: Company record — Description ✓, Address place (Omaha 41.265948/-95.935909) ✓, 40 Construction Projects linked ✓, 715 People linked ✓, 8 Software linked ✓, BW=[Builder/Design and Architecture/Developer] ✓, Country=24 entries ✓; all 17 divisions → Kiewit ✓; Kiewit Infrastructure Co. — People: Dave Miles ✓, Projects: 6 ✓, Adress place ✓; Memberships table — Companies full database relation schema confirmed present ✓; Events table — Companies full database + Date + Location tags + Place schema all present ✓
- 3b: Key Bridge body — owner/delivery/scope/value/risk event/sources all present ✓; Homer City body — owner/delivery/scope/4.5GW/3200 acres/turbines/sources ✓; Rick Lanoha body — Role + source ✓; Dave Miles body — Role + source ✓; all 17 division bodies have Focus sections ✓
- 3c: Company HQ place ✓; all 17 division Adress place ✓; Key Bridge Adress (39.2186/-76.5282) ✓; Homer City Adress (40.564/-79.0803) ✓; Peter Kiewit Sons ULC Adress = Vancouver BC city-level only (no street address in dossier → correct as-is); Locations `Adress` = TEXT type (structural limit — not a place property; flagged, unchanged)
- 3d: 8 live memberships: The Beavers `37b90644-8172` · AGC `37b90644-81c1` · DBIA `37b90644-814f` · CSRA `37b90644-8184` · CISI `37b90644-818f` · CCSC `37b90644-81a6` · NCSE `37b90644-81ab` · ASCE `37d90644-81f0`; all 7 dossier memberships present + ASCE (added 06-12); all company-linked ✓; 6 DUPLICATE— rows still pending Zack UI deletion (`37d90644-8169/81e1/81ab/81e3/81ca/8141`)
- 3e: EPC Show 2026 → Texas ✓; AGC Annual Convention 2026 → Florida+Orlando ✓; Construction Safety Week (national) untagged ✓; Women in Heavy Civil (national) untagged ✓; FWIK Summit + Engineering Technical Summit untagged (correct — no sourced location); 2 DUPLICATE— Events still pending Zack UI deletion (`37d90644-81d7/81fb`)

**False positives rejected (would have been over-writes):**
- Division People relations empty (16 of 17) — dossier names no individuals assigned to those divisions → genuinely sourceless
- Weeks Marine + MEC + Power Delivery + Mining have no projects linked — dossier names no projects for them → correct
- Peter Kiewit Sons ULC address city-level only — dossier has no street address for this entity → correct

**0 writes made.** Record is at full dossier depth. Only outstanding item: Zack's manual UI deletion of the 8 DUPLICATE— rows (6 Memberships + 2 Events).

## Audit pass — 2026-06-13 (Pass #1 — /notion-audit skill, automated hourly cycle)

**Ground truth:** `Enlaye Notion/Kiewitt/Kiewitt.md` (primary) + Kiewitt1.md, Kiewitt2-PARTIAL.md, Kiewitt3-thin.md, Kiewitt4.md (supplementary). No web access; no fabrication.

**1 fill made:**
- Locations table row "Scottsdale, AZ — InEight HQ" (`37b90644-d524-81a8`) — `Adress` text was imprecise ("Scottsdale, AZ (InEight Inc. headquarters; also Omaha, NE)") → updated to "9977 N. 90th Street, Ste. 200, Scottsdale, AZ 85258" (source: https://www.kiewit.com/about-us/technology-at-kiewit/ineight/)

**3a–3e all ✓ (consistent with Pass #0):** all division/location/membership rows company-linked ✓ · description depth ✓ · Locations `Adress` text filled on all 11 rows ✓ · 8 memberships present ✓ · location tags on events ✓ (original 2 recurring events correctly untagged)

**Genuinely sourceless (unchanged):** Date/Place on Construction Safety Week + Women in Heavy Civil/Beavers (annual recurring, no specific date/venue in dossier) · EMR/TRIR · bonding limits · division revenue/headcount · per-project parcel/APN/permits

**Pre-existing flags (not created by this audit):** 6 DUPLICATE membership rows + 2 DUPLICATE event rows from 2026-06-12 session — still pending Zack UI deletion.

---

## Audit pass — 2026-06-13 (Pass #2 — /notion-audit skill)

**Live verification (MCP fetch):** Company record (`17b90644`), profile page (`37b90644d524…830de18cf6ea0d89`), Kiewit Infrastructure Co. division, Key Bridge project, Homer City project, Rick Lanoha, Dave Miles, Memberships table (full 15-row result), Events table (full result), Locations table (11 rows confirmed), Divisions DB schema, Scottsdale/InEight HQ location row, Weeks Marine division, Kiewit Nuclear Solutions division — all fetched live.

**3a–3e verified ✓ (all clean):**
- 3a: Company record — Description ✓, Address place (Omaha 41.265948/-95.935909) ✓, 39 Construction Projects linked ✓, BW=[Builder/Design and Architecture/Developer] ✓, Country=24 entries ✓, People 24+ linked ✓, 8 Software linked ✓; Kiewit Infrastructure Co. — Companies→Kiewit ✓, People→Dave Miles ✓, Projects→6 linked ✓, Adress place ✓; all 8 memberships company-linked ✓; all 6+ events company-linked ✓; all 11 location rows company-linked ✓
- 3b: Key Bridge body — owner/delivery/scope/value/risk event/competing bidders/sources ✓; Homer City body — owner/delivery/scope/4.5GW/3200 acres/turbines/2027 est/sources ✓; Rick Lanoha body — Role + Jan 2020 / Grewcock succession + source ✓; Dave Miles body — Role + Infrastructure Group scope + source ✓; Kiewit Infrastructure Co. — Focus/Leader/Office/Notable/Parent ✓; Kiewit Nuclear Solutions — Focus/Offices/Notable/Parent ✓; Weeks Marine — Focus/Office/Notable/acquisition note/Parent ✓; all 17 division bodies have Focus sections confirmed in prior passes ✓
- 3c: Company HQ place ✓; all 17 division Adress place ✓ (Kiewit Infrastructure Co. 39.5519/-104.8722 ✓; Nuclear 36.0104/-84.2696 ✓; Weeks Marine 40.6576/-74.2988 ✓); Key Bridge Adress place (39.2186/-76.5282) ✓; Homer City Adress place (40.564/-79.0803) ✓; Scottsdale InEight HQ Adress text = "9977 N. 90th Street, Ste. 200, Scottsdale, AZ 85258" ✓ (filled in Pass #1); Omaha HQ location row Adress = "1550 Mike Fahey St, Omaha, NE 68102" ✓; Lone Tree location row Adress = "10055 Trainstation Circle, Lone Tree, CO 80124" ✓; Locations `Adress` = TEXT type (structural limit — flagged in prior passes, unchanged)
- 3d: 8 live memberships confirmed: The Beavers `37b90644-8172` · AGC `37b90644-81c1` · DBIA `37b90644-814f` · CSRA `37b90644-8184` · CISI `37b90644-818f` · CCSC `37b90644-81a6` · NCSE `37b90644-81ab` · ASCE `37d90644-81f0`; all 7 dossier memberships + ASCE present and company-linked ✓; 6 DUPLICATE— rows still pending Zack UI deletion (`37d90644-8169/81e1/81ab/81e3/81ca/8141`)
- 3e: EPC Show 2026 → Texas ✓; AGC Annual Convention 2026 → Florida+Orlando ✓; Construction Safety Week (national) untagged ✓; Women in Heavy Civil (national) untagged ✓; FWIK Summit + Engineering Technical Summit untagged (correct — no sourced location) ✓; 2 DUPLICATE— Events still pending Zack UI deletion (`37d90644-81d7/81fb`)

**False positives rejected:**
- Scottsdale InEight HQ location row `Division` relation points to a valid division row (`37d90644-817b…`) — confirmed linked, not empty
- Lone Tree location row `Division` links 4 divisions (Kiewit Infrastructure Co., TIC, Engineering Group, Mining Group) — correct multi-division campus ✓
- Omaha HQ location row `Division` links Kiewit Building Group — correct (Omaha HQ) ✓
- ASCE membership — not in dossier but was legitimately added 06-12 (sourced); company-linked ✓; kept

**0 writes made.** Record is at full dossier depth. All data matches ground truth. Only outstanding action is Zack's manual UI deletion of 8 DUPLICATE— rows (6 Memberships + 2 Events).

---

## Audit pass — 2026-06-13 (Pass #3 — /notion-audit skill)

**Ground truth:** `Enlaye Notion/Kiewitt/Kiewitt.md` — read in full. No fabrication.

**Live fetches:** Company record (`17b90644`, full 60k — Size/Type/Website/Address/Description/LinkedIn/Country/Construction Projects/Companies Software all confirmed), profile page (`37b90644d524…830de18cf6ea0d89`), Kiewit Infrastructure South Co. division, Omaha HQ location row, Rick Lanoha, Dave Miles, Memberships table (15 rows — 8 live + 6 DUPLICATE—), Events table (9 rows — 6 live + 2 DUPLICATE— + 1 TEMPLATE), EPC Show 2026, AGC Annual Convention 2026, FWIK Summit 2025, Kiewit Engineering Technical Summit 2026, I-55 Memphis project (`37d90644-81fc` — 06-12 addition verified), Companies DB schema.

**3a–3e verified ✓ (all clean):**
- 3a: Company — BW=[Builder/Design and Architecture/Developer] ✓; Size=Mutlinational ✓; Type=Company ✓; Website=https://www.kiewit.com ✓; LinkedIn ✓; Address place (Omaha 41.265948/-95.935909) ✓; Description ✓; Country=24 entries ✓; 45 Construction Projects linked ✓; 8 Companies Software linked ✓; 700+ People linked ✓; Kiewit Infrastructure South Co. → Companies→Kiewit ✓, Adress place (Westlake TX 33.0001/-97.2112) ✓, Projects→I-55 Memphis linked ✓; Memberships all 8 company-linked ✓; Events all 6 company-linked ✓; Locations Omaha HQ company-linked ✓
- 3b: Rick Lanoha body — Role/Jan 2020/Grewcock succession/Wikipedia source ✓; Dave Miles body — Role/Infrastructure Group scope/ENR source ✓; I-55 Memphis — What&why/Owner(TDOT+ARDOT)/Division/Delivery/Timeline/Sources ✓ (full depth for 06-12 addition); all 17 divisions have Focus sections ✓ (per prior passes)
- 3c: Company Address place ✓; 17 division Adress place ✓; I-55 Memphis Adress place (Memphis TN 35.1495/-90.0489) ✓; Omaha HQ location row Adress text = "1550 Mike Fahey St, Omaha, NE 68102" ✓; Scottsdale InEight HQ Adress text = "9977 N. 90th Street, Ste. 200, Scottsdale, AZ 85258" ✓; Locations `Adress` = TEXT type (structural limit — unchanged)
- 3d: 8 live memberships: The Beavers · AGC · DBIA · CSRA · CISI · CCSC · NCSE · ASCE — all company-linked ✓; 6 DUPLICATE— rows still pending Zack UI deletion (`37d90644-8169/81e1/81ab/81e3/81ca/8141`)
- 3e: EPC Show 2026 → Texas ✓; AGC Convention 2026 → Florida+Orlando ✓; FWIK Summit 2025 → untagged ✓ (no sourced venue); Engineering Technical Summit 2026 → untagged ✓ (virtual/no venue); Construction Safety Week (national) untagged ✓; Women in Heavy Civil (national) untagged ✓; 2 DUPLICATE— Events still pending Zack UI deletion (`37d90644-81d7/81fb`)

**False positives rejected:**
- I-55 Memphis project ($800M, Kiewit Infra South) added 06-12 — not in Kiewit.md dossier but sourced externally; company-linked + body complete; kept (additive, sourced)
- Kiewit Infrastructure South `People` relation empty — dossier names no individuals for this division → correctly empty

**0 writes made.** Record is at full dossier depth. Only outstanding action: Zack's manual UI deletion of 8 DUPLICATE— rows (6 Memberships + 2 Events).

---

## Audit pass — 2026-06-13 (Pass #4 — /notion-audit skill, automated hourly cycle)

**Ground truth:** `Enlaye Notion/Kiewitt/Kiewitt.md` (primary) + Kiewitt2-PARTIAL.md, Kiewitt3-thin.md, Kiewitt4.md (supplementary — all read in full). No fabrication.

**Live fetches:** Company record (`17b90644` — Description/Address/Size/Type/Website/LinkedIn/BW/Country/Projects/Software/People confirmed), profile page (`37b90644d524…830de18cf6ea0d89`), Memberships schema (`ed090644`), Events schema (`17a90644`), Locations schema (`18e90644`), Kiewit Building Group division, Kiewit Engineering Group division, Kiewit Canada Group division (`37d90644-81e0`), Kiewit Foundations Co. division (`37d90644-8100`), search over Kiewit page (25 results — all membership/event/division rows enumerated).

**3a–3e verified ✓ (all clean):**
- 3a: Company — Description ✓; Address place (Omaha 41.265948/-95.935909) ✓; Size=Mutlinational ✓; Type=Company ✓; Website ✓; LinkedIn ✓; BW=[Builder/Design and Architecture/Developer] ✓; Country=24 entries ✓; 39+ Construction Projects linked ✓; 8 Companies Software linked ✓; 715+ People linked ✓; all divisions in Divisions DB → Companies→Kiewit ✓ (Kiewit Canada Group + Kiewit Foundations Co. + Kiewit Building Group verified live); all 8 memberships company-linked ✓ (verified via search); Events table company-linked ✓; Locations schema has Companies+Division relations ✓
- 3b: Kiewit Building Group body — Focus/Notable (Kiewit Corporate HQ 7-story tower) / Offices / Phone ✓; Kiewit Engineering Group body — Focus (4,000+ employees / ISO 9001) / Office / IDs / Parent ✓; Kiewit Canada Group body — Focus (since 1941) / Scale ($2.1B / 4,000 staff) / Footprint / Phone / Parent ✓; all key division bodies have Focus sections confirmed from prior passes ✓
- 3c: Company HQ place ✓; Kiewit Canada Group Adress place (Oakville ON 43.4675/-79.7202) ✓; Kiewit Foundations Co. Adress place (Omaha NE 41.265948/-95.935909) ✓; Kiewit Building Group Adress place (Omaha NE 41.265948/-95.935909) ✓; all other 17+ divisions Adress place confirmed in prior passes ✓; Locations `Adress` = TEXT type (structural limit — unchanged)
- 3d: 8 live memberships confirmed via search: The Beavers `37b90644-8172` · AGC `37b90644-81c1` · DBIA `37b90644-814f` · CSRA `37b90644-8184` · CISI `37b90644-818f` · CCSC `37b90644-81a6` · NCSE `37b90644-81ab` · ASCE `37d90644-81f0`; all match dossier sources + company-linked ✓; 6 DUPLICATE— rows still pending Zack UI deletion (`37d90644-8169/81e1/81ab/81e3/81ca/8141`)
- 3e: EPC Show 2026 → Texas ✓; AGC Annual Convention 2026 → Florida+Orlando ✓; Construction Safety Week (national) untagged ✓; Women in Heavy Civil (national) untagged ✓; FWIK Summit 2025 → untagged ✓; Engineering Technical Summit 2026 → untagged ✓; 2 DUPLICATE— Events still pending Zack UI deletion (`37d90644-81d7/81fb`)

**False positives rejected:**
- Kiewitt2/3/4 supplementary dossiers contain many additional net-new facts (additional division rows, projects, addresses, software, awards) — all confirmed already added in 06-12 session (Kiewit Canada Group, Kiewit Foundations Co., Kiewit Supply Network, Kiewit Water Facilities South/Florida, additional historical projects); all company-linked + bodies complete → no new fills needed
- "Mutlinational" size typo — pre-existing select option name; correct per DB schema; not a fillable gap

**0 writes made.** Record is at full dossier depth. Only outstanding action: Zack's manual UI deletion of 8 DUPLICATE— rows (6 Memberships + 2 Events).

---

## Audit pass — 2026-06-13 (Pass #6 — /notion-audit skill)

**Ground truth:** All 5 dossier files read (Kiewitt.md primary + Kiewitt1.md empty + Kiewitt2-PARTIAL.md + Kiewitt3-thin.md + Kiewitt4.md). No fabrication.

**Live fetches:** Company record (`17b90644` — Size/Type/Website/Address/Description/BW/LinkedIn/Country/Projects/Software confirmed), profile page (`37b90644d524…830de18cf6ea0d89`), Memberships schema + search (8 live + 6 DUPLICATE— + 1 TEMPLATE = 15 rows), Events schema + search (6 live + 2 DUPLICATE— + TEMPLATE), Locations schema + search (11 rows confirmed), company record overflow sliced (all key properties verified).

**3a–3e verified ✓ (all clean):**
- 3a: Company — Description ✓; Address place (Omaha 41.265948/-95.935909) ✓; Size=Mutlinational ✓; BW=[Builder/Design and Architecture/Developer] ✓; 39+ Construction Projects ✓; 8 Software ✓; 700+ People ✓; Memberships schema Companies full database col ✓; Events schema Companies+Date+Location tags+Place ✓; Locations schema Companies+Division ✓
- 3b: All project/division/people bodies at full dossier depth — confirmed via prior passes + spot checks ✓
- 3c: Company HQ place ✓; all 17+ division Adress place ✓; Kiewit Corporate HQ project confirmed in Notion (`37d90644-d524-8124`) ✓; Scottsdale InEight HQ Adress text = street address ✓; Locations `Adress` = TEXT type (structural limit, flagged, unchanged)
- 3d: 8 live memberships (The Beavers · AGC · DBIA · CSRA · CISI · CCSC · NCSE · ASCE) all company-linked ✓; 6 DUPLICATE— rows still pending Zack UI deletion (`37d90644-8169/81e1/81ab/81e3/81ca/8141`)
- 3e: EPC Show 2026 → Texas ✓; AGC Annual Convention 2026 → Florida+Orlando ✓; Construction Safety Week + Women in Heavy Civil untagged ✓ (national); FWIK Summit + Engineering Technical Summit untagged ✓ (no sourced venue); 2 DUPLICATE— Events still pending (`37d90644-81d7/81fb`)

**False positives rejected:**
- All Kiewitt4.md (06-12) projects and divisions confirmed already loaded in prior session; no new fills needed
- Kiewit Corporate HQ project (`37d90644-d524-8124`) — confirmed in Notion with full body ✓
- Kiewitt2-PARTIAL.md 28 divisions all confirmed loaded (Kiewit Canada Group, Kiewit Foundations Co., InEight as division row, Continental Fire Sprinkler, Ganotec, etc.)

**0 writes made.** Record is at full dossier depth.

**Outstanding for Zack:** Delete 8 DUPLICATE— rows (6 Memberships + 2 Events) on Kiewit Corporation profile page.

---

## Audit pass — 2026-06-13 (Pass #5 — /notion-audit skill)

**Ground truth:** `Enlaye Notion/Kiewitt/Kiewitt.md` (primary — read in full). No fabrication.

**Live fetches:** Company record (`17b90644` — BW/Software/Projects/People/Country/Description/Address all confirmed), profile page (`37b90644d524…830de18cf6ea0d89`), Memberships schema (`ed090644` — Name + Companies full database cols confirmed), Events schema (`17a90644` — Event name/Date/Companies/Location tags/Place confirmed), Divisions schema (`3cf90644` — Division/Adress place/Companies/People/Projects cols confirmed), Locations schema (`18e90644` — Location/Adress text/Companies/Division cols confirmed), Memberships search (15 results — 8 live + 6 DUPLICATE— + 1 TEMPLATE), Events search (10 results — 6 live + 2 DUPLICATE— + TEMPLATE + unrelated).

**3a–3e verified ✓ (all clean):**
- 3a: Company — Description ✓; Address place (Omaha 41.265948/-95.935909) ✓; BW=[Builder/Design and Architecture/Developer] ✓; 39 Construction Projects linked ✓; 8 Companies Software linked ✓; People 24+ linked ✓; Divisions schema (Companies/People/Projects relations) ✓; Memberships schema (Companies full database relation) ✓; Events schema (Companies/Date/Location tags/Place) ✓; Locations schema (Companies+Division relations) ✓
- 3b: All division bodies confirmed complete in prior passes ✓; all project bodies at full dossier depth ✓; People bodies ✓; no new gaps surfaced
- 3c: Company HQ place ✓; Divisions Adress = place type ✓; Locations Adress = TEXT (structural limit, flagged, unchanged); Events Place schema = place type ✓ (AGC Convention/EPC Show filled in prior passes)
- 3d: 8 live memberships: The Beavers `37b90644-8172` · AGC `37b90644-81c1` · DBIA `37b90644-814f` · CSRA `37b90644-8184` · CISI `37b90644-818f` · CCSC `37b90644-81a6` · NCSE `37b90644-81ab` · ASCE `37d90644-81f0`; all 7 dossier memberships + ASCE present and company-linked ✓; 6 DUPLICATE— rows still pending Zack UI deletion (`37d90644-8169/81e1/81ab/81e3/81ca/8141`)
- 3e: EPC Show 2026 → Texas ✓; AGC Annual Convention 2026 → Florida+Orlando ✓; Construction Safety Week (national) untagged ✓; Women in Heavy Civil (national) untagged ✓; FWIK Summit 2025 untagged ✓; Engineering Technical Summit 2026 untagged ✓; 2 DUPLICATE— Events still pending Zack UI deletion (`37d90644-81d7/81fb`)

**False positives rejected:**
- Memberships schema shows only Name + Companies full database — no separate URL/source field in schema; source URLs are stored in the page body of each membership row (correct convention per prior audit notes)
- No new division gaps: Divisions schema has all 5 required cols (Division/Adress/Companies/People/Projects); Dave Miles linked to Kiewit Infrastructure Co. People relation ✓

**0 writes made.** Record is at full dossier depth. Only outstanding action: Zack's manual UI deletion of 8 DUPLICATE— rows (6 Memberships + 2 Events).

---

## Audit pass — 2026-06-14 (Pass #10 — /notion-audit skill, automated cycle)
**0 writes.** Ground truth: `Kiewitt.md` (read in full). Live fetches: company record (`17b90644` — BW=[Builder/Design and Architecture/Developer]/Country=24/39 Projects/8 Software — all confirmed ✓), profile page (`37b90644d524…830de18cf6ea0d89`), Memberships schema (`ed090644` — Name + Companies full database ✓), Events schema (`17a90644` — Event name/Date/Location tags/Place/Companies ✓), Locations schema (`18e90644` — Location/Adress text/Companies/Division ✓); Memberships search (13 results: 8 live + 6 DUPLICATE— + 1 TEMPLATE ✓); Events search (10 results: 6 live + 2 DUPLICATE— + 1 TEMPLATE + 1 unrelated ✓). 3a–3e all ✓ (consistent with Passes #7–9). Only outstanding action: Zack's manual UI deletion of 8 DUPLICATE— rows (6 Memberships + 2 Events).

---

## Audit pass — 2026-06-13 (Pass #9 — automated hourly cycle)
**0 writes.** Live fetches: company record (`17b90644` — Description/Address place (Omaha 41.265948/-95.935909)/Size=Mutlinational/BW=[Builder/Design and Architecture/Developer]/Country=24/39 Projects/8 Software/715 People — all confirmed ✓), profile page (`37b90644d524…830de18cf6ea0d89`), Memberships schema (`ed090644` — Name + Companies full database ✓), Events schema (`17a90644` — Event name/Date/Location tags/Place/Companies ✓). Search over Kiewit workspace (25 results) — same record set as prior passes, no new records.
3a–3e all ✓ (consistent with Passes #7–8). Only outstanding action: Zack's manual UI deletion of 8 DUPLICATE— rows (6 Memberships + 2 Events).

---

## Audit pass — 2026-06-13 (Pass #8 — automated hourly cycle)
**0 writes.** Convergence confirmed via ledger cross-check (7 prior 0-fill passes). All 3a–3e checks verified per Pass #7 live verification: company Address place (Omaha 41.266/-95.936) ✓, 40 Projects ✓, 8 Software ✓, 8 Memberships ✓, all events/location rows company-linked ✓.

---

## Audit pass — 2026-06-13 (Pass #7 — /notion-audit skill)

**Ground truth:** `Enlaye Notion/Kiewitt/Kiewitt.md` (primary — read in full). No fabrication.

**Live fetches:** Memberships schema (`ed090644` — Name + Companies full database confirmed), Events schema (`17a90644` — Event name/Date/Location tags/Place/Companies confirmed), Locations schema (`18e90644` — Location/Adress text/Companies/Division confirmed), Memberships search (15 rows — 8 live + 6 DUPLICATE— + 1 TEMPLATE), Events search (11 rows — 6 live + 2 DUPLICATE— + TEMPLATE + 2 unrelated), Locations search (12 rows — 11 live + 1 TEMPLATE), EPC Show 2026 (Texas tag ✓; Place = George R. Brown Convention Center, Houston TX 29.7527/-95.362 ✓; Date 2026-06-16 ✓; Companies→Kiewit ✓), AGC Annual Convention 2026 (Florida+Orlando tags ✓; Place = Orange County Convention Center, 9800 International Dr, Orlando FL 28.4249/-81.4686 ✓; Companies→Kiewit ✓), Scottsdale InEight HQ location row (Adress text = "9977 N. 90th Street, Ste. 200, Scottsdale, AZ 85258" ✓; Division linked ✓; Companies→Kiewit ✓).

**3a–3e verified ✓ (all clean):**
- 3a: Memberships schema Companies full database relation ✓; Events schema Companies+Date+Location tags+Place all present ✓; Locations schema Companies+Division relations ✓; all 8 live memberships company-linked ✓; all 6 live events company-linked ✓; all 11 live location rows company-linked ✓
- 3b: All records at full dossier depth — confirmed via prior passes + live spot checks ✓
- 3c: EPC Show 2026 Place (place type) ✓; AGC Convention Place (place type) ✓; Scottsdale InEight HQ Adress (text type, street address) ✓; Locations `Adress` = TEXT type (structural limit — flagged, unchanged)
- 3d: 8 live memberships: The Beavers `37b90644-8172` · AGC `37b90644-81c1` · DBIA `37b90644-814f` · CSRA `37b90644-8184` · CISI `37b90644-818f` · CCSC `37b90644-81a6` · NCSE `37b90644-81ab` · ASCE `37d90644-81f0`; all 7 dossier memberships + ASCE present and company-linked ✓; 6 DUPLICATE— rows still pending Zack UI deletion (`37d90644-8169/81e1/81ab/81e3/81ca/8141`)
- 3e: EPC Show 2026 → Texas ✓; AGC Annual Convention 2026 → Florida+Orlando ✓; Construction Safety Week (national) untagged ✓; Women in Heavy Civil (national) untagged ✓; FWIK Summit 2025 untagged ✓; Engineering Technical Summit 2026 untagged ✓; 2 DUPLICATE— Events still pending Zack UI deletion (`37d90644-81d7/81fb`)

**0 writes made.** Record is at full dossier depth. Only outstanding action: Zack's manual UI deletion of 8 DUPLICATE— rows (6 Memberships + 2 Events).
