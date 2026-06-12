# State · Records — Sundt

> **Holds:** the Sundt dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a Sundt record.
> **Ground truth:** `Enlaye Notion/Sundt/Sundt.md` (single-line JSON dossier; run_date 2026-06-10; 8 divisions · 18 projects · 15 locations · 2 events · 1 membership · 3 software · 50 sources · 24 gaps · NO people array). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.

---

## Profile page (hub)
**"Sundt"** (renamed from "Sundt TEMPLATE") — https://app.notion.com/p/37b90644d52480908a3cf33c8e2f63af (Companies research → Zack Folder). Newer template variant (Divisions DB, same as Branch/HITT). Shell was pre-created by a prior session 2026-06-10 12:53.

Page-local data sources on this page:
- **Divisions / Company Map** `collection://f4f90644-d524-82e8-8049-070a21e9e185` (Division title · Adress place · relations Companies full database / People / Projects) — db `ceb90644d52483f2a63a817f13886d6b`
- **Events** `collection://af290644-d524-83f1-b328-07770f7e9c41` (Event name · Date · Location tags · Place · Companies full database)
- **Sources** `collection://fb090644-d524-8285-8bd8-0702b4e3c976` ("What the source is about" · URL)
- **Locations** `collection://abc90644-d524-82dc-8677-879d77176767` (Location · Adress TEXT — **+added** Companies + Division relations)
- **Memberships** `collection://b1c90644-d524-82a0-b1c9-0787b14ccf89` (was Name-only — **+added** Companies relation)
- Linkedin Post `collection://adb90644-d524-832b-9815-079f52cd900c` (unused)
- Projects Underway = shared Construction Projects (linked view, filtered `__TEMPLATE__` — **manual UI fix**)
- Existing Software = shared Companies Software (linked view, filtered `__TEMPLATE__` — **manual UI fix**)

## Company record (UPDATED — existing, NOT created)
**"Sundt"** `22b90644-d524-8027-af9b-e3c3761a7fb7` in Companies full database. Pre-existing (Feb 2026), custom-emoji icon. Already had: BW Category=[Builder] · Country=[USA] · Description (marketing copy) · LinkedIn · Website · Size=Regional · Type=Company · 15 People linked (Feb-2026 import incl. Sassaman/Hageman/Odom/Yang/Brousseau + 10 `2fb90644…` rows).
- Filled this pass: Country +[Arizona, Texas, California, Tennessee, Washington, Florida] · body Company Snapshot + Sources (revenue/employees/ESOP/founded/ENR/HQ/IDIQ, sourced) · Construction Projects = 18 (one-way) · Companies Software = 3. People auto-grew 15→18.
- **Conflicts kept (existing wins):** Size=Regional (dossier=Multinational/"Mutlinational") · Description marketing copy (dossier one-liner added to body snapshot instead).
- ⚠ Address (place) NOT set — workspace `place` rejects address-only and dossier has no lat/lng (no-geocoding rule). HQ address is in the body snapshot + Tempe HQ location row.
- ⚠ Country: dossier footprint also includes **Utah, New Mexico, North Carolina** — no option in Companies Country multi-select; NOT added (avoided 60-option ALTER clobber). Flag for manual UI.

## Divisions (8 — Divisions DB `f4f90644`; each → company `22b9…fb7`)
| Division | ID | Leader | Projects linked |
|---|---|---|---|
| Advanced Facilities | `37b90644-d524-8177-a6b2-d3a4e8264bfe` | Alex Charland | Data Center Campus |
| Building Group | `37b90644-d524-8102-b6ac-e00611442d25` | Chad Buck | UTEP, UA, Cal Poly Humboldt, SD City College, Cal Poly Pomona |
| Mining | `37b90644-d524-81f6-96ca-e4a338fba666` | — | Hermosa |
| PoweR | `37b90644-d524-81a1-b21c-c2ce56b4a098` | — | APS Four Corners |
| Heavy Industrial | `37b90644-d524-81f2-95dc-f8ff3dab5df2` | — | Apache Junction Mfg |
| Renewables and Solar | `37b90644-d524-8139-b542-ca0760d30880` | — (founded 2020; >$700M) | rPlus Appaloosa I PV |
| Transportation and Infrastructure | `37b90644-d524-812c-b46c-c159138e2c32` | — | I-20, I-10, 183 North, Nashville CONRAC |
| Water | `37b90644-d524-819f-b471-c8448cb6155a` | Sam Reidy (founded 1950) | SLC, El Paso, Gilbert, Lake Dams |

## People (3 — People DB; Company → `22b9…fb7`; division via Divisions.People back-link)
Derived from sourced division-leadership announcements (dossier has no people array). Function Qualification=[President]. No email/phone/LinkedIn in dossier.
| Person | ID | Role | Division |
|---|---|---|---|
| Alex Charland | `37b90644-d524-81b8-9568-dadd126ff3a7` | President, Advanced Facilities Group (late 2024) | Advanced Facilities |
| Chad Buck | `37b90644-d524-8160-afae-ddab7ddb12f1` | President, Building Group (2025) | Building Group |
| Sam Reidy | `37b90644-d524-8102-b8df-c812366346f3` | President, Water & Wastewater Group (2024) | Water |
- **Pre-existing 15 Sundt People** (Feb-2026 import) left as-is on company record; not in dossier.

## Projects (18 — Construction Projects DB; Contractors → company; body brief+sources)
Owning Department left empty (relates to Companies DB; division link via Divisions.Projects). Owner/client in body (Owners DB records NOT created). Place left empty (no coords). Location tag where state option exists.
| Project | ID | $M | Type | Status | Division |
|---|---|---|---|---|---|
| Salt Lake City New Water Reclamation Facility | `37b90644-d524-8121-84c2-ee6353aadfd2` | 900 | Infrastructure | In progress | Water |
| El Paso Water Pure Water Center | `37b90644-d524-8142-a4e5-caa81abf2e55` | 295 | Infrastructure | In progress | Water |
| Nashville Airport CONRAC Program (Messer-Sundt JV) | `37b90644-d524-8199-a696-db4980d6b045` | 900 | Transportation | In progress | Transportation |
| Apache Junction Manufacturing Facility | `37b90644-d524-817e-a6cf-ca3842e22076` | — | Distribution / Industrial | In progress | Heavy Industrial |
| UTEP Texas Western Hall | `37b90644-d524-818a-82c5-fc7f1894cf98` | 110 | Higher Education | Done | Building Group |
| I-20 Improvements Odessa | `37b90644-d524-8121-bc01-fc61abb5169e` | 225 | Transportation | In progress | Transportation |
| I-10 Widening West Phase II | `37b90644-d524-8102-85cd-efb13a29614c` | 87 | Transportation | In progress | Transportation |
| 183 North Mobility Project (Archer Western-Sundt JV) | `37b90644-d524-8156-acfb-dea8193576bf` | 612 | Transportation | In progress | Transportation |
| University of Arizona Student Success District | `37b90644-d524-8194-a867-c2ad892f4c8e` | 143 | Higher Education | Done | Building Group |
| Cal Poly Humboldt Healthcare Education Hub | `37b90644-d524-819b-b2eb-c01894b12cbc` | — | Higher Education | In progress | Building Group |
| San Diego City College Performing Arts Center | `37b90644-d524-8182-a5ab-ed8cbe2de394` | 95 | Higher Education | In progress | Building Group |
| rPlus Energies Appaloosa I PV Plant | `37b90644-d524-8111-b70a-f39a54340db7` | — | Energy & Power | Done | Renewables |
| Gilbert North Water Treatment Plant Upgrades | `37b90644-d524-8165-885b-f9a861ff28ac` | 95 | Infrastructure | In progress | Water |
| Lake McQueeney and Lake Placid Dams | `37b90644-d524-8171-8d83-e4700a6e4001` | 746 | Infrastructure | In progress | Water |
| Confidential Client Data Center Campus | `37b90644-d524-8115-b64f-c387c63f7b0b` | — | Data Center / Mission Critical | In progress | Advanced Facilities |
| Cal Poly Pomona Student Housing & Dining Commons Ph 1 | `37b90644-d524-8109-9728-ddf4a9a354cc` | — | Higher Education | Done | Building Group |
| Arizona Minerals South32 Hermosa Mine | `37b90644-d524-8179-a04b-ff196f1976f9` | — | Industrial / Chemicals | In progress | Mining |
| APS Four Corners Generating Station | `37b90644-d524-81d7-95b6-cdca5f77b736` | — | Energy & Power | In progress | PoweR |

## Other tables
- **Events (2 — `af290644`, → company):** AGC Construction Safety Excellence Award Grand Prize (nation's safest 2025; 2026-04-16; tag Arizona) `37b90644-d524-81df-b355-d224cf3b91c6` · DBIA 30-Year Membership Milestone `37b90644-d524-81ef-985a-fd19bca1a6fb`.
- **Memberships (1 — `b1c90644`, → company):** Design-Build Institute of America (DBIA) `37b90644-d524-81c6-a123-f8aa51f2e00b`.
- **Software (3 — shared Companies Software DB `37690644`, → company):** PSIcapture + Microsoft SharePoint `37b90644-d524-81ed-955c-f8fa8eef9d68` (neither in option set — title/body) · Autodesk (BIM, Transportation) `37b90644-d524-8142-ad48-c62a6478d034` [Autodesk] · DESTINI Estimator `37b90644-d524-81d8-a82e-c6c01ff05ff7` [DESTINI Estimator].
- **Locations (15 — `abc90644`, → company + owning division):** Tempe HQ `…81e6-85cf-e4bb503a84a2` (corp) · Phoenix Ops `…81f2-ad5d…` · Phoenix Training `…81fb-9510…` · Tucson River Rd `…8143-aec0…` (Building) · Tucson Old Vail `…8109-b9e1…` (Building) · San Diego `…8186-b874…` (Building) · Irvine `…814a-9e53…` (Building) · Sacramento `…8111-bbb7…` (Building) · San Antonio `…8124-8777…` (Transportation) · El Paso `…81a1-8dbc…` (Water) · Dallas `…813a-8a50…` (Transportation) · Salt Lake City `…8134-a905…` (Renewables) · Charlotte `…81ef-b3a3…` (Transportation) · Vancouver WA `…81ac-a26d…` (Transportation) · Tampa `…8132-9ef9…` (Transportation). All Adress text filled.
- **Sources (16 — `fb090644`):** firmographics (What We Build, Contact, About, 2025 Fact Sheet), ENR 2026/2024, Bizjournals, AGC safety, DBIA, 3 leadership announcements, Renewables, ENR El Paso reuse, InStream software, SAM.gov.

## Left empty (no sourced value in dossier — per 24-item gaps list)
Most project contract values (Cal Poly Pomona, rPlus, Data Center, APS Four Corners, Hermosa, Apache Junction); architect-of-record on several; division revenue/headcount; TRIR/EMR/DART; bonding/surety; permits/parcels/flood-zone; competing bidders; open-req counts; all place fields (no coords); people Email/Phone/LinkedIn. Referenced-but-not-researched projects (NOT created): Pepperdine Seaside, ODOT I-5 Rose Quarter, SE Water Pollution Control HW, San Pedro Creek, Valley Metro NW Extension, AZ Biltmore Golf.

## Interlink graph (verified by re-fetch 2026-06-10)
Company ↔ People (3 new + 15 existing = 18) ✓ · Company ↔ Construction Projects (18) ✓ · Company ↔ Software (3) ✓ · Division→Company (8) ✓ · Division→People (3: Charland/Buck/Reidy) ✓ · Division→Projects (18 mapped) ✓ · Project→Contractors (18) ✓ · Location→Company + Division (15) ✓ · Event→Company (2) ✓ · Membership→Company (1) ✓ · Software→Company (3) ✓. Project `Owning Department` deliberately empty (wrong-mechanism for page-local divisions); Person→Division N/A (People.Division targets a fixed other collection).

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = Sundt.
2. **Existing Software** view → clear `__TEMPLATE__` filter.
3. Company Country → add **Utah, New Mexico, North Carolina** options (none exist; not added via MCP to avoid full-list clobber).
4. Construction Projects Location multi-select → add **Utah, New Mexico** if precise project-location tags wanted (used body instead; SLC/rPlus/Data Center/APS untagged).
5. Companies Software `Software used` → add **PSIcapture, Microsoft SharePoint** if tag wanted (in row Name/body for now).
6. Possible template guide rows on local tables — UI delete if Zack wants them gone.

## Audit — 2026-06-10 (second pass)
Full re-fetch of all records: company record, 8 divisions, 3 people, 18 projects, 2 events, 1 membership, 15 locations, data-source schemas. **No new fillable gaps found.**
- Division `place:Adress` still empty — write attempted, rejected (Notion place type requires lat/lng; dossier has none; no-geocoding rule confirmed).
- All relations, body content, properties confirmed intact from load session.
- Profile page (`37b90644…3af`) body retains template instruction text — non-destructive rule; no `replace_content` permitted without explicit confirmation.
- Genuinely sourceless blanks unchanged: place fields (no coords), division revenue/headcount, people email/phone/LinkedIn, DBIA event date, AGC event venue address, 5 project contract values.
- **Result: 0 writes, 0 new gaps filled, 0 data corrupted. Record is complete per available dossier data.**

## Audit — 2026-06-12 (third pass — /notion-audit Sundt)
Full re-fetch: company record, all linked tables (Divisions, Events, Memberships, Locations, Software, Projects). Workspace was substantially enriched by a subsequent session between 06-10 and 06-12.

### What has grown since the 06-10 audit
- **Company body** — significantly expanded: CEO (Cade Rowley, Oct 2024), M&A (electrical contractor acquisition May 2026), ENR trajectory (#62→#42), legal name/UEI/CAGE/NAICS, state licenses, 2025 Fact Sheet data, water milestone (60 plants/15 years/$9B+).
- **Construction Projects** — 18 → 53+ linked. New projects include (partial list): State Route 347 ($396M, Arizona/Transportation), Boeckman Road Corridor Improvement (Sundt-Tapani JV, $27M, WA/Transportation), US-30 Rocky Point Wildlife Crossing ($11.9M, Idaho/Transportation), TxDOT I-10 Widening Phase II ($120M, Texas/Transportation), Windhaven Parkway ($16.57M, Texas/Transportation), Valley Metro NW Extension Light Rail (Phoenix/Transportation), City of Phoenix Scenario 3B Water Pipeline Rehab (Phoenix/Water), SF SE Water Pollution Control Headworks ($540M, CA/Water), and many more.
- **Divisions** — 8 → 9 (new: Concrete division `37d90644-d524-8155-b8ec-ea2507ae6474` — Leader: Danny Gumm; 400+ concrete craft workers; linked to company ✓ / People ✓; Projects not linked).
- **People (Divisions)** — multiple new leaders added to division People relations: Renewables has Tom Dodson + Chris Steves; Transportation has Jeff Williamson + Ken Kubacki + Jasen Bennie + Jeffrey Hamilton; Water has Omar Chavez + Matt Bothun + Paul Laufer; Advanced Facilities has +Josh Anderson; Building Group has +Ryan Nessen, Sarah Owen, Shawn Blubaum (+ Chad Buck).
- **Memberships** — 1 → 4+: DBIA (original), AGC (`37d90644-d524-811e-b8fc-fa65bc716c58`), APWA (`37d90644-d524-81f2-902d-c7ddbe28f8e6`), Arizona Builders Alliance (`37d90644-d524-8146-abe0-d82ef36fe939`). All linked to company ✓.
- **Events** — 2 → 3+: AGC Safety Award (original), DBIA Milestone (original), Sundt Renewables Launch (`37d90644-d524-812a-b79f-dbc5cb84f476`, Dec 2020, linked to company ✓).
- **Software** — 3 → 5: original 3 + Bluebeam Revu `37d90644-d524-81d1-b9a4-f706d6b2a573` + Bluebeam Revu/Studio `37d90644-d524-8156-a8c7-f53ec8c5253e`. Both linked to company ✓.
- **Country** — Utah, New Mexico, North Carolina now present in company record (previously flagged as "manual UI only" — resolved by another session).

### ⚠ Duplicate records flagged (non-destructive — cannot delete; Zack should clean via UI)
| Table | Dup records | Note |
|---|---|---|
| Locations | "Tempe Headquarters" `37b90644-d524-81e6-85cf-e4bb503a84a2` (original, has body) vs "Tempe HQ" `37d90644-d524-81f8-816c-efbc1f976755` (blank body, same address) | Retain original; delete new via UI |
| Locations | "Phoenix Operations Support Services" `37b90644-d524-81f2-ad5d-fcaa77e88c99` (original, has body) vs `37d90644-d524-8114-8c2c-e8dbd32e549b` AND `37d90644-d524-810a-b472-d132ceb0ee9d` (both blank bodies, same address) | Retain original; delete two new via UI |
| Memberships | "Associated General Contractors of America (AGC)" — 3 records: `37d90644-d524-811e-b8fc-fa65bc716c58` (has body) + `37d90644-d524-81e5-8e61-d9c95e3f1cdc` + `37d90644-d524-814c-8ff7-fda3024fb70a` (blank) | Retain first; delete two via UI |
| Memberships | "Arizona Builders Alliance" — 2 records: `37d90644-d524-8146-abe0-d82ef36fe939` (has body) + `37d90644-d524-819e-a255-d55764fbe062` | Retain first; delete second via UI |
| Memberships | "American Public Works Association (APWA)" — 2 records: `37d90644-d524-81f2-902d-c7ddbe28f8e6` (has body) + `37d90644-d524-817b-a5dd-ce8a49b5bb0c` | Retain first; delete second via UI |
| Projects | "I-10 Widening West Phase II" `37b90644-d524-8102-85cd-efb13a29614c` ($87M) vs "TxDOT I-10 Widening Phase II" `37d90644-d524-81a5-af38-c58e478f03a3` ($120M) — same source URL, different scope/name → possible same project re-created with different value; review before deleting |

### Orphan standalone page
- `37d90644-d524-810e-9a9c-fc8149ba1b6e` — blank-titled standalone Notion page (not in any DB) containing Concrete Division content identical to the DB row `37d90644-d524-8155-b8ec-ea2507ae6474`. The DB row is correct; this orphan should be deleted via UI.

### No new fillable gaps found from dossier
- Division `Adress` (place) still requires lat/lng → dossier has none → unchanged.
- All new records have company relation set ✓.
- DBIA event date still null (sourceless).
- place fields on all records remain empty (no coords; no-geocoding rule).
- **Result: 0 writes this pass. No dossier-sourceable gaps remain. Duplicate/orphan cleanup requires manual UI action.**

### Manual UI steps outstanding (cumulative)
1. **Dup cleanup** (see table above) — delete 2 Tempe HQ, 2 Phoenix Ops, 2 AGC, 1 AzBA, 1 APWA membership dups; orphan Concrete page.
2. **I-10 duplicate review** — determine if $87M vs $120M are the same project or different phases; merge or archive accordingly.
3. Projects Underway view → clear `__TEMPLATE__` filter, set Contractors = Sundt.
4. Existing Software view → clear `__TEMPLATE__` filter.
5. Country → Utah, New Mexico, North Carolina now present ✓ (resolved).
6. Construction Projects Location multi-select → add Idaho, Oregon options for new Northwest projects.
