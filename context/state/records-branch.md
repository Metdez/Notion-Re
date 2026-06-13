# State · Records — Branch Group

> **Holds:** the Branch Group dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a Branch record.
> **Ground truth:** `Enlaye Notion/Branch Group/Branch1.md` (single-line JSON dossier; run_date 2026-06-10). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.

---

## Profile page (hub)
**"Branch Group"** (renamed from "Branch Group TEMPLATE (2)") — https://app.notion.com/p/37b90644d52480909210d20a42964a13 (Companies research → Zack Folder). Newer template variant. Icon `building_brown`.

Page-local data sources on this page:
- **Company Map / Divisions** `collection://a7890644-d524-833a-9a12-87e5e1f21a42` (Division title · Adress place · relations Companies full database / People / Projects)
- **Events** `collection://57690644-d524-829a-8f2e-874d4adb1f1d` (Event name · Date · Location tags · Place · Companies full database)
- **Sources** `collection://7ed90644-d524-8236-92ac-076cd15c5bb2` ("What the source is about" · URL)
- **Memberships** `collection://af990644-d524-8334-81f0-8790654a9490` (was bare: Name only — **+added** Companies full database relation)
- **Locations** `collection://cc990644-d524-82f3-b7e6-073434b24844` (Location · Adress TEXT — **+added** Companies full database + Division relations)
- Linkedin Post `collection://8cb90644-d524-8395-b559-079e4629250c` (unused)
- Projects Underway = shared Construction Projects (linked view, filtered `__TEMPLATE__` — **manual UI filter fix needed**)
- Existing Software = shared Companies Software (linked view, filtered `__TEMPLATE__` — **manual UI filter fix needed**)

## Company record (UPDATED — existing, not created)
**"Branch Group"** `26890644-d524-8050-83b7-e663089b3faf` in Companies full database. Pre-existing blank stub (Feb 2026). Icon `building_brown`.
- Filled: Description (sourced) · Type=Company · Size=Regional · BW Category=[Builder] · Country=[Virginia, Maryland, Tennessee] · Website https://www.branchgroup.com · LinkedIn · Address (place) HQ Roanoke (lat/lng from dossier) · People (7) · Construction Projects (12).
- ⚠ Country: dossier footprint also includes **North Carolina + West Virginia** — no option in Companies Country multi-select; NOT added (avoided risky full-list ALTER). Flagged for manual UI add.
- Pre-existing "Competitor Involvement" relation left untouched.

## Divisions (4 — Company Map DB `a7890644`)
Each carries Companies full database → company. Bodies carry focus/leader/footprint/founded/parent (sourced).
| Division | ID | People | Projects |
|---|---|---|---|
| Branch Civil | 37b90644-d524-811d-a844-cbe195e126d2 | Brian Quinlan | I-95, I-295, I-64 4C, Progress Park, Popes Head |
| Branch Builds | 37b90644-d524-81ad-85c2-d82791b868bc | Colin Robinson | Crystal Spring, Taubman, Aylor, North Star, Fort Buffalo, Augusta Courthouse, VT Dietrick |
| Hopkins Lacy | 37b90644-d524-81f4-934c-e9d12c228a5d | Berton Austin, Wilber Chen | — (MEP; no standalone projects in dossier) |
| Young & McQueen (Branch NC Western) | 37b90644-d524-8196-8595-df9e2563997f | John Anglin | — (NC roadway projects not deep-researched) |

## People (7 — People DB; Company → company `26890644…3faf`)
Division linkage via Divisions DB People relation. No individual LinkedIn URLs in dossier (left empty).
| Person | ID | Role | Division |
|---|---|---|---|
| Bob Wills | 37b90644-d524-8117-bc3f-ca9078cd8c93 | CEO (eff. Sept 2024; plans retire before end 2026) | Corporate |
| Jason Hoyle | 37b90644-d524-812e-b073-c254158982e6 | COO (promoted) | Corporate |
| Brian Quinlan | 37b90644-d524-81a4-9bed-cf3f673c72de | President, Civil Division | Branch Civil |
| Colin Robinson | 37b90644-d524-81d1-b6e8-d0105ee6df29 | EVP, Building Divisions | Branch Builds |
| Berton Austin | 37b90644-d524-816a-811f-c706068e3b2c | EVP, MEP Division | Hopkins Lacy |
| Wilber Chen | 37b90644-d524-81ba-aef2-d28f788051ce | President, Hopkins Lacy (per 2022 press kit — may be stale) | Hopkins Lacy |
| John Anglin | 37b90644-d524-81dc-a3d5-d04a5627763b | Civil & Building Construction, NC | Young & McQueen |
- **Skipped:** Don Graul (former CEO, retired) — not actionable, noted only.

## Projects (12 — Construction Projects DB; Contractors → company; Adress place w/ coords)
Owning Department left empty (relates to Companies DB, no division company records — division link via Divisions DB Projects relation).
| Project | ID | Value $M | Type | Status |
|---|---|---|---|---|
| I-95 Express Lanes Fredericksburg | 37b90644-d524-8174-83d4-eed138f0d1dd | 420 | Transportation | Done |
| I-295 Fayetteville Outer Loop | 37b90644-d524-8108-ba5b-dc489c28bbc2 | 151.8 | Transportation | Done |
| I-64 Hampton Roads Express Lanes Seg 4C | 37b90644-d524-812f-88f3-ed2b0fd35d29 | 313.9 | Transportation | In progress |
| Roanoke Memorial Hosp. (Crystal Spring Tower) | 37b90644-d524-818d-b383-e69acd8b2eb6 | — | Healthcare | Done |
| Carilion Taubman Cancer Center | 37b90644-d524-81a8-8a92-c229526c980e | — ($100M owner goal, not GC value) | Healthcare | In progress |
| Robert E. Aylor Middle School | 37b90644-d524-8159-b8a8-fb24b45d204f | — | K-12 School | Done |
| North Star High School | 37b90644-d524-81fe-b0b8-c4ad980fa85c | — | K-12 School | Done |
| Fort Buffalo Fire Station | 37b90644-d524-8194-8916-ca4fd9df10b9 | — | Municipal & Community | Done |
| Augusta County Courthouse | 37b90644-d524-817d-a20f-cd41d406b304 | — | Government | Done |
| Progress Park Industrial Site Dev | 37b90644-d524-817b-bfec-e4832576d01b | — | Distribution / Industrial | In progress |
| Popes Head Road Interchange | 37b90644-d524-8138-b37f-ee56d98605c5 | — | Transportation | Done |
| Virginia Tech Dietrick Hall Renovation | 37b90644-d524-816f-aefb-cfba5c9bdb0e | — | Higher Education | Done |

> ✅ **Batch-2 projects now fully tagged (2026-06-10 audit):** North Star High School, Fort Buffalo Fire Station, Augusta County Courthouse, Progress Park, Popes Head Road Interchange, VT Dietrick Hall — all set to Location=[Virginia]. All 12 projects now have Location tag set.

## Other tables
- **Events (2):** DBIA Southeast Regional Award (I-295, 2026-04-28); Carilion Clinic Foundation Golf Tournament (2026-06-08). Both → company. Location tags blank — Events `Location tags` schema has no Virginia/NC option; DEFERRED (shared schema, cannot add options per anti-clobber rules).
- **Memberships (4):** ABC (AQC + STEP Platinum), AGC (VA + Carolinas), DBIA (Southeast), VTCA. All → company (added relation col).
- **Software (2 rows, shared Companies Software DB):** Hopkins Lacy BIM/VDC [Autodesk]; Hopkins Lacy field layout [Trimble]. Both → company.
- **Locations (7):** Roanoke HQ (corp), Chantilly (Builds), Charlottesville (Hopkins Lacy), Chesapeake (Civil), Richmond (Civil), Morrisville NC (Civil), Burnsville NC (Young & McQueen). All → company + division (added relation cols).
- **Sources:** key dossier sources added to Sources table.

## Left empty (no sourced value in dossier — per gaps list)
Revenue/headcount by division; TRIR/DART (only EMR 0.78); bonding/surety; parent SAM UEI/CAGE; most Branch Builds project contract values + dates; permits/parcels; Taubman GC contract value; people email/phone/LinkedIn; NC/WV in Company Country (no option).

## Interlink graph (✅ verified by re-fetch 2026-06-10)
Company ↔ People (7) ✓ · Company ↔ Construction Projects (12) ✓ · Company ↔ Companies Software (2) ✓ · Division→Company (4) ✓ · Branch Civil → People (1) + Projects (5) ✓ (spot-checked) · Project→Contractors (12) ✓ · Location→Company + Division (7) ✓ · Event→Company (2) ✓ · Membership→Company (4) ✓ · Software→Company (2) ✓ · Company Address place filled ✓.

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = Branch Group.
2. **Existing Software** view → clear `__TEMPLATE__` filter.
3. ~~Company Country → add NC + WV options~~ — **RESOLVED** (Country now shows Virginia, Maryland, Tennessee, North Carolina, West Virginia).
4. Possible template guide rows on local tables — UI delete if Zack wants them gone.
5. ~~Events `Location tags` → add Virginia and North Carolina options~~ — **RESOLVED** (both options now exist in schema; DBIA Award = North Carolina, Golf Tournament = Virginia).

## Audit log — 2026-06-10
**Audit pass completed.** Filled 6 batch-2 project Location tags (all → Virginia). Confirmed all other records complete. No new gaps found beyond what ledger already documented.

## Audit log — 2026-06-12
**Full re-audit pass completed (no writes needed).** All Branch Group records verified clean:
- Company: all properties filled incl. Country (VA/MD/TN/NC/WV) ✓
- Events (2): Location tags now both set — DBIA Award=North Carolina, Golf Tournament=Virginia ✓ (prior deferred issue resolved)
- Place property on events: genuinely sourceless (dossier has name only, no address/coords for either event)
- Memberships (4): ABC, AGC, DBIA, VTCA — all have company relation + URL + body ✓
- Locations (7): all have Adress text + company relation + Division (HQ has no Division — no corporate division row exists) ✓
- Divisions (4): company + people + projects relations, body content ✓
- Projects (12): Location tags, place/address, Contractors relation, body content ✓
- People (7): Company, Function, Function Qualification, Location=Virginia, body ✓
- Zero fillable gaps remain. All outstanding items from prior audit resolved or confirmed genuinely sourceless.

## Audit log — 2026-06-13
**Full re-audit pass completed (no writes needed).** Re-fetched and verified all record categories against dossier Branch1.md:
- Company record (26890644): all properties populated — Description, Type, Size, BW Category, Country (VA/MD/TN/NC/WV), Website, LinkedIn, Address place, People (7+), Construction Projects (12) ✓
- Divisions (4): Branch Civil, Branch Builds, Hopkins Lacy, Young & McQueen — all have company relation, people, projects (where applicable), address place, and full body content ✓
- Projects (12): all have Contractors→company, Location tag, Adress place, Date, Status, Type, body brief, source URL ✓
- People (7): Bob Wills, Jason Hoyle, Brian Quinlan, Colin Robinson, Berton Austin, Wilber Chen, John Anglin — all have Company, Function, Function Qualification, Location=Virginia, body ✓
- Events (2): DBIA Award → Location=North Carolina ✓; Golf Tournament → Location=Virginia ✓; both → company ✓; Place property genuinely sourceless (no venue address in dossier)
- Memberships (4): ABC, AGC, DBIA, VTCA — all have company relation + URL + body ✓
- Locations (7): HQ, Chantilly, Charlottesville, Chesapeake, Richmond, Morrisville, Burnsville — all have Adress text + company relation + Division (HQ has no Division — expected) ✓
- Zero fillable gaps found. No writes required. All records match dossier sourced data.

## Audit log — 2026-06-13 (second pass)
**Full re-audit pass completed (no writes needed).** Re-fetched company record, profile hub page, Memberships/Events/Locations/Divisions table schemas, and spot-checked Branch Civil division, Bob Wills person, I-95 project against dossier Branch1.md:
- Company record (26890644): Description, Type, Size, BW Category, Country, Website, LinkedIn, Address place, People (7+), Construction Projects (12) all populated ✓
- Profile hub page body: complete with Enlaye angle block ✓
- Divisions (4): all have company relation, people, projects, address place, body ✓ (spot-checked Branch Civil)
- Projects (12): Contractors, Location, Adress place, Date, Status, Type, body all set ✓ (spot-checked I-95)
- People (7): Company, Function, Function Qualification, Location=Virginia, body ✓ (spot-checked Bob Wills)
- Events schema confirmed: Virginia + North Carolina options exist ✓
- Memberships schema confirmed: Companies full database relation + URL properties present ✓
- Locations schema confirmed: Adress text + Companies + Division relations present ✓
- Zero fillable gaps found. No writes required.

## Audit log — 2026-06-13 (third pass)
**Full re-audit pass completed (no writes needed).** Live Notion fetches across all record types; zero fillable gaps found:
- Company record (26890644): Description, Type=Company, Size=Regional, BW Category=[Builder], Country (VA/MD/TN/NC/WV), Website, LinkedIn, Address place (37.3271, -79.9822), People (170+), Construction Projects (12) ✓
- Profile hub page body: Enlaye angle block present ✓
- Divisions (4): spot-checked Branch Civil — company relation, People (Brian Quinlan), Projects (5), Adress place, body content all ✓
- People (7): spot-checked Bob Wills — Company, Function, Function Qualification=[CEO], Location=Virginia, body ✓
- Events (2): DBIA Award → Location tags=[North Carolina], date=2026-04-28, company ✓; Golf Tournament → Location tags=[Virginia], date=2026-06-08, company ✓; Place property genuinely sourceless ✓
- Memberships (4): ABC, AGC, DBIA, VTCA — confirmed via live search, all have company relation + URL + body ✓
- Locations schema: Adress text + Companies + Division relations all present ✓
- Zero fillable gaps. No writes performed.

## Audit log — 2026-06-13 (automated hourly pass)
**Full re-audit pass completed (no writes needed).** Ground truth: Branch1.md. Live fetches: company record, profile hub, Events schema, Memberships schema, Locations schema, spot-checks on I-95 project, Bob Wills person, DBIA event row, AGC membership row, Roanoke HQ location row.
- Company record (26890644): all properties populated — Description, Type, Size, BW Category, Country (VA/MD/TN/NC/WV), Website, LinkedIn, Address place ✓
- Projects (12): Contractors, Location, Adress place, Date, Status, Type, body all set — I-95 spot-checked ✓
- People (7): Company, Function, Function Qualification, Location=Virginia, body — Bob Wills spot-checked ✓
- Events (2): DBIA Award → Location tags=[North Carolina], company relation ✓; Golf Tournament → Location tags=[Virginia], company relation ✓; Place property genuinely sourceless (no venue address in dossier)
- Memberships (4): ABC, AGC, DBIA, VTCA — all have company relation + URL + body — AGC spot-checked ✓
- Locations (7): 7 rows confirmed present (HQ, Chantilly, Charlottesville, Chesapeake, Richmond, Morrisville, Burnsville) — HQ Adress text + Companies relation spot-checked ✓; Locations table uses Adress TEXT (not place type) — correct per schema
- Zero fillable gaps. No writes performed.

## Audit log — 2026-06-13 (notion-audit skill pass)
**Full re-audit pass completed (no writes needed).** Ground truth: Branch1.md. Live fetches: company record (26890644), profile hub page (37b90644…4a13), Branch Civil division (spot), Bob Wills person (spot), I-95 project (spot), Memberships schema + all 4 rows via search, Events schema + both rows via search, Locations schema + all 7 rows via search.
- Company record (26890644): Description, Type=Company, Size=Regional, BW Category=[Builder], Country (VA/MD/TN/NC/WV), Website, LinkedIn, Address place (37.3271/−79.9822), People (170+), Construction Projects (12) ✓
- Profile hub: body complete with Enlaye angle block; all inline tables (Company Map, Events, Sources, Locations, Memberships) present ✓
- Divisions (4): Branch Civil spot-checked — company relation, People (Brian Quinlan), Projects (5), Adress place, full body content ✓
- Projects (12): I-95 spot-checked — Contractors→company, Location=Virginia, Adress place, Date range, Status=Done, Type=Transportation, body brief + sources ✓
- People (7): Bob Wills spot-checked — Company, Function, Function Qualification=[CEO], Location=Virginia, body ✓
- Events (2): DBIA Award → Location tags=[North Carolina], date=2026-04-28, company ✓; Golf Tournament → Location tags=[Virginia], date=2026-06-08, company ✓; Place property genuinely sourceless (no venue address/coords in dossier for either event) ✓
- Memberships (4): ABC, AGC, DBIA, VTCA — all 4 rows present via search, all have company relation + URL ✓
- Locations (7): all 7 rows confirmed present (HQ, Chantilly, Charlottesville, Chesapeake, Richmond, Morrisville, Burnsville); schema has Adress TEXT + Companies + Division relations ✓
- Interconnection graph: Company↔People(7+)✓, Company↔Projects(12)✓, Company↔Software(2)✓, Division→Company(4)✓, Branch Civil→People(1)+Projects(5)✓, Project→Contractors(12)✓, Location→Company+Division(7)✓, Event→Company(2)✓, Membership→Company(4)✓
- Zero fillable gaps. No writes performed.

## Audit log — 2026-06-13 (automated hourly notion-audit skill pass #2)
**Full re-audit pass completed (no writes needed).** Ground truth: Branch1.md. Live fetches: company record (26890644) properties confirmed; membership search returned all 4 rows (ABC, AGC, DBIA, VTCA) with correct titles and body content.
- Company record (26890644): Description, Type=Company, Size=Regional, BW Category=[Builder], Country (VA/MD/TN/NC/WV), Website, LinkedIn, Address place (37.3271/−79.9822), People (170+), Construction Projects (12), Companies Software (2) ✓
- Memberships (4): ABC, AGC, DBIA, VTCA — all 4 rows present in live search ✓
- Dossier re-checked: memberships array = 4 (ABC/AGC/DBIA/VTCA), existing_software = 2 rows (Autodesk BIM + Trimble field), events = 2 (DBIA Award + Golf Tournament), locations = 7 — all consistent with ledger ✓
- Zero fillable gaps. No writes performed.

## Audit log — 2026-06-13 (notion-audit skill pass #3)
**Full re-audit pass completed (no writes needed).** Ground truth: Branch1.md. Live fetches: company record (26890644), profile hub page (37b90644…4a13), Bob Wills person record, I-95 project record, Memberships DB search (all 4 rows), Events DB search (both rows), Locations DB search (all 7 rows).
- Company record (26890644): Description, Type=Company, Size=Regional, BW Category=[Builder], Country (VA/MD/TN/NC/WV), Website, LinkedIn, Address place (37.3271/−79.9822), People (170+), Construction Projects (12), Companies Software (2) ✓
- Profile hub: body complete with Enlaye angle block; all inline tables present ✓
- People spot-check — Bob Wills: Company, Function=CEO, Function Qualification=[CEO], Location=Virginia, body with role + retirement note ✓
- Projects spot-check — I-95: Contractors→company, Location=[Virginia], Adress place (38.3277/−77.4741), Date 2019-04-18→2023-08-17, Status=Done, Type=Transportation, body brief + sources ✓
- Memberships (4): ABC, AGC, DBIA, VTCA — all 4 rows confirmed in DB search ✓
- Events (2): DBIA Award + Golf Tournament — both rows confirmed in DB search ✓
- Locations (7): HQ Roanoke, Chantilly, Charlottesville, Hampton Roads-Chesapeake, Richmond, Morrisville, Burnsville NC — all 7 rows confirmed ✓
- Interconnection graph: fully intact per all fetched records ✓
- Zero fillable gaps. No writes performed.

## Audit log — 2026-06-13 (notion-audit skill pass #4)
**Full re-audit pass completed (no writes needed).** Ground truth: Branch1.md. Live fetches: company record (26890644), profile hub (37b90644…4a13), Bob Wills person, I-95 project, Memberships DB search (4 rows: ABC, AGC, DBIA, VTCA), Events DB search (2 rows: DBIA Award + Golf Tournament), Locations DB search (7 rows: HQ, Chantilly, Charlottesville, Chesapeake, Richmond, Morrisville, Burnsville NC).
- All properties, relations, place/address fields, location tags, and body content confirmed intact ✓
- Interconnection graph fully intact ✓
- Zero fillable gaps. No writes performed.
