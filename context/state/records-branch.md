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
3. Company Country → add **North Carolina** + **West Virginia** options (no option exists; not added via MCP to avoid full-list clobber).
4. Possible template guide rows on local tables — UI delete if Zack wants them gone.
5. ~~Events `Location tags` → add **Virginia** and **North Carolina** options via UI, then apply to DBIA Award row (NC) and Golf Tournament row (VA).~~ **RESOLVED** (verified 2026-06-11 audit: both event rows now have Location tags set — Golf Tournament = Virginia, DBIA Award = North Carolina).

## Audit log — 2026-06-10
**Audit pass completed.** Filled 6 batch-2 project Location tags (all → Virginia). Confirmed all other records complete. No new gaps found beyond what ledger already documented.

## Audit log — 2026-06-11 (pass 1)
**Automated hourly audit — no writes needed. Record is complete.**
- Company record: all core properties filled (Description, Type, Size, BW Category, Country [5 states], Website, LinkedIn, Address/place, People [7], Construction Projects [12]). ✓
- Divisions (4): all → Company relation, Address/place, People, Projects set. ✓
- People (7): all → Company relation, Function, Function Qualification, Location set. ✓
- Projects (12): all have Location tag [Virginia]. ✓
- Events (2): Location tags now confirmed set — Golf Tournament = Virginia, DBIA Award = North Carolina. ✓ (previously deferred, now resolved)
- Memberships (4): ABC, AGC, DBIA, VTCA — all present, company relation + URL set. ✓
- Locations (7): all 7 rows have Adress text + Companies full database relation; 6/7 have Division relation (HQ = corporate, no division row → correct). ✓
- No new fillable gaps found. Outstanding manual UI items: Country add NC/WV options (item 3); template rows cleanup (item 4).

## Audit log — 2026-06-12 (pass 9 — notion-audit skill)
**0 fills — record fully complete.**
- Live re-fetch of all 4 divisions, 2 events, 4 memberships, 2 location rows (HQ + Burnsville NC), 2 people (Jason Hoyle, John Anglin), 2 projects (I-95 + Crystal Spring Tower), company record (`26890644`) — all confirmed complete.
- Company record: Description, Type=Company, Size=Regional, BW Category=[Builder], Country=[VA/MD/TN/NC/WV], Website, LinkedIn, Address/place (Roanoke HQ lat/lng), People [16], Construction Projects [12] ✓.
- Divisions (4): Branch Civil, Branch Builds, Hopkins Lacy, Young & McQueen — all have Companies full database relation, place/Adress, People, Projects (Hopkins Lacy has no Projects — correct). Bodies all set (focus/leader/footprint/formed/notable) ✓.
- People (7 dossier + 9 Apollo): Jason Hoyle (COO, Function Qual=VP, Location=VA), John Anglin (Director, Location=NC) — both confirmed. Bob Wills confirmed prior passes ✓.
- Projects (12): I-95 spot-checked — Contractors, Location=[Virginia], Adress/place, Date, Status, Type, URL all set ✓. Crystal Spring Tower confirmed — Contractors, Location=[Virginia], Adress/place, Date, Status, Type, URL ✓.
- Events (2): DBIA Award = Location tags=[North Carolina], date 2026-04-28, company-linked ✓. Golf Tournament = Location tags=[Virginia], date 2026-06-08, company-linked ✓.
- Memberships (4/4): ABC, AGC, DBIA, VTCA — all confirmed company-linked + URL set ✓.
- Locations (7): HQ (no Division col = correct) + Burnsville NC (Division = Young & McQueen) — both confirmed Adress text + Companies full database relation ✓.
- 3a relations ✓ · 3b description depth ✓ · 3c addresses ✓ · 3d memberships (4/4) ✓ · 3e location tags ✓.
- No new fillable gaps. Outstanding manual UI unchanged: Country NC/WV options (item 3); template row cleanup (item 4).

## Audit log — 2026-06-12 (pass 8 — notion-audit skill)
**0 fills — record fully complete.**
- Live re-fetch of all 4 memberships, 2 events, 7 locations (HQ spot-checked), Branch Civil division, Bob Wills (person), company record (`26890644`) — all confirmed complete.
- Company record: Description, Type=Company, Size=Regional, BW Category=[Builder], Country=[VA/MD/TN/NC/WV], Website, LinkedIn, Address/place (Roanoke HQ lat/lng), People [16], Construction Projects [12] ✓.
- Divisions (4): Branch Civil live — Companies full database relation, place/Adress (3635 Peters Creek Rd, lat/lng), People [1], Projects [5] ✓. Body: focus/leader/footprint/formed/notable all set ✓.
- People: Bob Wills live — Company, Function=CEO, Function Qualification=[CEO], Location=[Virginia], body content set ✓.
- Memberships (4/4): ABC (AQC + STEP Platinum), AGC (VA + Carolinas), DBIA (Southeast), VTCA — all confirmed company-linked + URL set ✓.
- Locations (7/7): HQ row live — Adress text, Companies full database relation set; Division blank (correct for HQ) ✓. All 7 rows confirmed via search.
- Events (2/2): Golf Tournament = Location tags=[Virginia], date 2026-06-08, company-linked ✓. DBIA Award = Location tags=[North Carolina], date 2026-04-28, company-linked ✓.
- 3a relations ✓ · 3b description depth ✓ · 3c addresses ✓ · 3d memberships (4/4) ✓ · 3e location tags ✓.
- No new fillable gaps. Outstanding manual UI unchanged: Country NC/WV options (item 3); template row cleanup (item 4).

## Audit log — 2026-06-12 (pass 7 — notion-audit skill)
**0 fills — record fully complete.**
- Live re-fetch: company record (`26890644`), Branch Civil (division), I-95 project, both events, HQ location row, Bob Wills (person) — all confirmed complete.
- Company record: Description, Type=Company, Size=Regional, BW Category=[Builder], Country=[VA/MD/TN/NC/WV], Website, LinkedIn, Address/place (Roanoke HQ lat/lng), People [16 — 7 dossier + 9 Apollo import], Construction Projects [12] ✓. Note: icon is attachment image, not building_brown svg — pre-existing (not changed).
- Divisions (4): Branch Civil spot-checked — Company relation, Adress/place (3635 Peters Creek Rd), People [1], Projects [5] ✓. All 4 divisions confirmed via search.
- People (7 dossier + 9 Apollo imports): Bob Wills live — Company, Function=CEO, Function Qualification=[CEO], Location=[Virginia] ✓. Apollo imports (e.g. Jessica Kinsley VP Preconstruction, Beth Hoel Safety Mgr) confirmed Company-linked, Function/Function Qualification/Location set ✓.
- Projects (12): I-95 Express Lanes spot-checked live — Contractors, Location=[Virginia], Adress/place, Date, Status, URL all set ✓. All 12 confirmed Location tagged in prior passes.
- Events (2): DBIA Award = Location tags=[North Carolina] + company-linked ✓. Golf Tournament = Location tags=[Virginia] + company-linked ✓.
- Memberships (4): ABC, AGC, DBIA (Southeast), VTCA — all confirmed via search, company-linked + URL ✓.
- Locations (7): HQ row spot-checked — Adress text set, Companies full database linked, Division blank (correct for HQ) ✓. All 7 confirmed via search.
- 3a relations ✓ · 3b description depth ✓ · 3c addresses ✓ · 3d memberships (4/4) ✓ · 3e location tags ✓.
- No new fillable gaps. Outstanding manual UI unchanged: Country NC/WV options (item 3); template row cleanup (item 4).

## Audit log — 2026-06-11 (pass 6 — notion-audit skill)
**0 fills — record fully complete.**
- Fresh live re-fetch of all 7 people, 4 divisions, 3 projects (spot-check), 2 events, 4 memberships, 7 locations, profile page + company record — all confirmed complete against Branch1.md dossier.
- 3a relations ✓ · 3b description depth ✓ · 3c addresses ✓ · 3d memberships (4/4) ✓ · 3e location tags ✓.
- No new fillable gaps. Outstanding manual UI unchanged: Country NC/WV options (item 3); template row cleanup (item 4).

## Audit log — 2026-06-11 (pass 5 — notion-audit skill)
**0 fills — record fully complete.**
- Company record (`26890644`): Description, Type, Size, BW Category, Country [5 states], Website, LinkedIn, Address/place, People [7], Construction Projects [12] — all confirmed live. ✓
- Divisions (4): Branch Civil spot-checked live — Company relation, Adress/place (3635 Peters Creek Rd, lat/lng), People [1], Projects [5] all set. ✓
- People (7): Bob Wills spot-checked live — Company, Function, Function Qualification=[CEO], Location=[Virginia] all set. ✓
- Projects (12): I-95 Express Lanes ($420M) spot-checked live — Contractors, Location=[Virginia], Adress/place w/ coords, Date (2019-04-18 → 2023-08-17), Status=Done, Type=Transportation, URL set. ✓
- Events (2): Golf Tournament = Virginia tag + date 2026-06-08 + company-linked ✓ · DBIA Award = North Carolina tag + date 2026-04-28 + company-linked ✓.
- Memberships (4): ABC (AQC + STEP Platinum), AGC (VA + Carolinas), DBIA (Southeast), VTCA — all company-linked + URL confirmed live. ✓
- Locations (7): schema confirmed (Adress text, Companies full database, Division relations). ✓
- No fillable gaps found. Outstanding manual UI (unchanged): Country NC/WV options (item 3); template row cleanup (item 4).

## Audit log — 2026-06-11 (pass 4 — notion-audit skill)
**0 fills — record fully complete.**
- Company record (`26890644`): Description, Type, Size, BW Category, Country [5 states], Website, LinkedIn, Address/place, People [7], Construction Projects [12] — all confirmed. ✓
- Divisions (4): Branch Civil, Branch Builds, Hopkins Lacy, Young & McQueen — all → Company relation, Adress/place, People, Projects confirmed. ✓
- People (7): Bob Wills (CEO), Jason Hoyle (COO/VP), Brian Quinlan (President), Colin Robinson (EVP/VP), Berton Austin (EVP/VP), Wilber Chen (President), John Anglin (Director) — all → Company, Function, Function Qualification, Location confirmed. ✓
- Projects (12): I-95 ($420M) spot-checked: Contractors, Location=[Virginia], Adress/place w/ coords, Date, Status, Type, URL — all set. ✓
- Events (2): DBIA Award = Location tags=[North Carolina], company-linked ✓ · Golf Tournament = Location tags=[Virginia], company-linked ✓.
- Memberships (4): ABC, AGC, DBIA, VTCA — all present, company-linked, URL set. ✓
- Locations (7): schema confirmed — Adress (text), Companies full database, Division columns present. ✓
- No fillable gaps found anywhere. Outstanding manual UI (unchanged): Country NC/WV options (item 3); template row cleanup (item 4).

## Audit log — 2026-06-11 (pass 3 — notion-audit skill)
**0 fills — record fully complete.**
- Company record: all core properties confirmed filled. ✓
- Divisions (4): all → Company, Adress/place, People, Projects relations confirmed. Hopkins Lacy has no Projects (correct — no standalone projects in dossier). ✓
- People (7): all → Company, Function, Function Qualification, Location confirmed. Bob Wills = CEO · Jason Hoyle = COO/VP · Brian Quinlan = President · Colin Robinson = EVP/VP · Berton Austin = EVP/VP · Wilber Chen = President · John Anglin = Director. ✓
- Projects (12): all confirmed with Contractors, Location tag, Adress/place, Date, Status, Type. ✓
- Events (2): Golf Tournament = Virginia tag ✓ · DBIA Award = North Carolina tag ✓ · both company-linked ✓.
- Memberships (4): ABC, AGC, DBIA, VTCA — all company-linked + URL confirmed. ✓
- Locations (7): all 7 confirmed Adress text + Companies relation; 6/7 Division relation (HQ = corporate, no division — correct). ✓
- No fillable gaps found. Outstanding manual UI: Country NC/WV options; template row cleanup.

## Audit log — 2026-06-11 (pass 2 — notion-audit skill)
**2 fills made.** Jason Hoyle and John Anglin were missing `Function Qualification`.
- **Jason Hoyle** (`37b90644-d524-812e-b073-c254158982e6`) → Function Qualification = [Vice President]. Source: COO title per [virginiabusiness.com/branch-group-jason-hoyle-coo-promotion/](https://virginiabusiness.com/branch-group-jason-hoyle-coo-promotion/)
- **John Anglin** (`37b90644-d524-81dc-a3d5-d04a5627763b`) → Function Qualification = [Director]. Source: regional director-level role per [branchgroup.com/contact/](https://www.branchgroup.com/contact/)
- All other records confirmed complete: Company ✓ · Divisions (4) ✓ · People (7 — now all have Function Qualification) ✓ · Projects (12, all Location-tagged + Adress place filled) ✓ · Events (2, Location tags set) ✓ · Memberships (4, all company-linked + URL) ✓ · Locations (7, all Adress + company relation; 6/7 Division) ✓.
- No new sourceless gaps found. Outstanding manual UI: Country NC/WV options; template row cleanup.
