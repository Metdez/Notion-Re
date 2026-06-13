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

## Audit — 2026-06-13 (fourth pass — /notion-audit Sundt)
Full re-fetch: company record (schema + body), all 9 divisions, 4 memberships, 3 events, 15 locations schema, sample projects (SLC Water, APS Four Corners, Hermosa Mine). Companies DB schema confirmed (no Ownership/Founded/Revenue/Employees/ENR Rank properties — those fields don't exist in the schema; correctly in body only).

### New since 06-12
- **Company record Address (place)** — now filled: `place:Address:name=Sundt Construction HQ`, address=2620 S 55th St Tempe AZ 85282, lat=33.3979, lng=-111.9662. Previously flagged as outstanding; resolved by an intervening session. ✓
- **People count** — 835 people relations on company record (was ~18 dossier-sourced + 15 pre-existing; bulk growth reflects ongoing workspace enrichment from Apollo/LinkedIn imports).

### Checks performed (3a–3e)
- **3a Interconnection:** Company ↔ Divisions (9) ✓ · Divisions → Company (9) ✓ · Divisions → People ✓ · Divisions → Projects ✓ (where linked) · Events → Company (3) ✓ · Memberships → Company (4) ✓ · Locations → Company ✓. PoweR division has no People — dossier names no PoweR leader; genuinely sourceless.
- **3b Description depth:** All 9 division bodies confirmed rich with focus/leader/footprint/portfolio. Events have sourced bodies. Memberships have sourced bodies.
- **3c Address/location:** Company Address place = filled ✓. Division `Adress` (place type) = still empty; requires lat/lng; dossier has none; no-geocoding rule applies → genuinely sourceless. Location rows have Address text filled ✓.
- **3d Membership completeness:** 4 memberships present: DBIA ✓ · AGC ✓ · APWA ✓ · Arizona Builders Alliance ✓. Dossier names no additional memberships beyond these 4. Complete.
- **3e Location tags:** AGC Safety Award has Location tag "Arizona" ✓. DBIA Milestone has no date and no location tag — dossier gives no event date or location for the milestone; genuinely sourceless. Sundt Renewables Launch has no Location tag — event occurred Dec 2020, no specific venue in dossier; genuinely sourceless.

### No new fillable gaps found
- Companies DB schema has no Ownership/Founded/Revenue/Employees/ENR Rank properties — these don't exist; body-only is correct.
- DBIA event date null — sourceless (no date in dossier).
- Renewables Launch location tag — sourceless (no venue in dossier).
- Division place (Adress) — no coords, no-geocoding rule.
- PoweR division People — no leader named in dossier.
- Concrete division Projects — cross-company support group; no specific projects attributed in dossier.
- **Result: 0 writes this pass. Record complete per dossier. Dup/orphan cleanup (~8 records) still requires manual UI action.**

### Manual UI steps outstanding (cumulative — unchanged from 06-12)
1. **Dup cleanup** — delete 2 Tempe HQ, 2 Phoenix Ops, 2 AGC, 1 AzBA, 1 APWA membership dups; orphan Concrete page (`37d90644-d524-810e-9a9c-fc8149ba1b6e`).
2. **I-10 dup review** — $87M vs $120M same or different project.
3. Projects Underway view → clear `__TEMPLATE__` filter.
4. Existing Software view → clear `__TEMPLATE__` filter.
5. Construction Projects Location → add Idaho, Oregon options for Northwest projects.

## Audit — 2026-06-13 (fifth pass — /notion-audit Sundt)
Full re-fetch: company record, Memberships table (all rows), Events table (all rows), Locations table (schema + sample rows), Divisions (Advanced Facilities, Building Group, Mining + schema), sample projects (SLC Water, Building Group).

### Workspace growth since 06-13 (fourth pass)
- **Memberships** — now 5 rows: DBIA · AGC · APWA · Arizona Builders Alliance · **The Beavers** (`37d90644-d524-8118-9bc4-f7a3e08a57b9`, added ~06-12 19:07). All linked to company ✓.
- **Locations** — now 3 "Tempe Headquarters" rows: original `37b90644…81e6…` (with body) + `37d90644…81a6…` (blank body, same address, added ~06-12 20:06) + `37d90644…81f8…` ("Tempe HQ", added ~06-12 20:18). Two new dups beyond what 06-12 audit flagged.
- **Company record** confirmed healthy; all relations, properties as recorded.

### Checks performed (3a–3e)
- **3a Interconnection:** All 9 divisions → company ✓ · Events → company (3) ✓ · Memberships → company (5) ✓ · Locations → company ✓. No new gaps.
- **3b Description depth:** Divisions confirm rich bodies ✓. All sampled projects have sourced body content ✓.
- **3c Address/location:** Company Address place still filled ✓. Location `Adress` text field populated on original rows ✓. Division `Adress` (place type) still empty — no coords in dossier, no-geocoding rule → genuinely sourceless.
- **3d Membership completeness:** Dossier `memberships` array = 1 entry (DBIA only). The 4 additional memberships (AGC, APWA, Arizona Builders Alliance, The Beavers) were added by post-dossier enrichment sessions using sources outside the original dossier — valid enrichment, not dossier-sourced. Dossier is fully covered (DBIA ✓). No new dossier-sourced memberships to add.
- **3e Location tags:** AGC Safety Award tag "Arizona" ✓. DBIA Milestone — no date/location in dossier; sourceless ✓. Renewables Launch — no venue in dossier; sourceless ✓.

### No new fillable gaps found from dossier
All dossier-sourced data remains correctly recorded. No empty fields with sourced values were identified.
- **Result: 0 writes this pass. Record complete per dossier.**

### New duplicates to flag (UI cleanup required)
- Locations: **"Tempe Headquarters"** — `37d90644-d524-81a6-9e90-d5ef10d12c7e` (blank body, added 06-12 20:06) is a new dup beyond those flagged 06-12. Delete via UI; retain original `37b90644…81e6…`.

### Manual UI steps outstanding (updated 06-13 fifth pass)
1. **Dup cleanup** — Locations: delete `37d90644-d524-81a6-9e90-d5ef10d12c7e` (new Tempe HQ dup) + previously flagged: `37d90644-d524-81f8-816c-efbc1f976755` (Tempe HQ), 2 Phoenix Ops dups, 2 AGC dups, 1 AzBA dup, 1 APWA dup; orphan Concrete page (`37d90644-d524-810e-9a9c-fc8149ba1b6e`).
2. **I-10 dup review** — $87M vs $120M same or different project.
3. Projects Underway view → clear `__TEMPLATE__` filter.
4. Existing Software view → clear `__TEMPLATE__` filter.
5. Construction Projects Location → add Idaho, Oregon options for Northwest projects.

## Audit — 2026-06-13 (sixth pass — /notion-audit Sundt)
Full parallel re-fetch: company record (full body + properties), all 9 divisions (individual page fetches), all 3 event pages, all Locations rows, all 5+ Membership rows, sample project pages (SLC Water, Nashville, I-10 $87M, 183 North, rPlus, Gilbert, TxDOT $120M dup), hub page full scan.

### Workspace growth since 06-13 (fifth pass)
- **Memberships** — grew from 5 to 8 unique + 6 dup rows: added **ESOP Association** (`37d90644-d524-81XX`), **U.S. Green Building Council (USGBC)** (`37d90644-d524-81XX`), **ENR Top 400 Contractors (2026, #42)** (`37d90644-d524-81XX`) — all from post-dossier enrichment ~06-12 20:18. Also **6 additional duplicate rows** (Beavers ×3 total, AGC ×3 total, APWA ×2 total, AzBA ×2 total).
- **Locations** — **Austin TX** is a new unique location (`37d90644-d524-81fb-bebb-e76c42c97838`, 1701 Directors Blvd Suite 730, Austin TX 78744, Division SET, body present) — net-new, not a duplicate. Also Vancouver WA now has 2 extra dups beyond the 1 flagged in pass 5. Phoenix Training Center now has 2 dups. Total dup count in Locations escalated.
- **Company record** — Size property confirmed `"Mutlinational"` (typo for "Multinational" — pre-existing schema option, not correctable without full-list clobber risk).

### Full dup inventory (updated 06-13 sixth pass)
**Locations dupes (delete via UI — keep 37b90644-... originals):**
| Dup ID | Name | Keep? |
|---|---|---|
| `37d90644-d524-81f8-816c-efbc1f976755` | Tempe HQ | Delete — keep `37b90644…81e6…` |
| `37d90644-d524-81a6-9e90-d5ef10d12c7e` | Tempe Headquarters | Delete — keep `37b90644…81e6…` |
| `37d90644-d524-810a-b472-d132ceb0ee9d` | Phoenix Operations Support Services | Delete — keep `37b90644…81f2…` |
| `37d90644-d524-8114-8c2c-e8dbd32e549b` | Phoenix Operations Support Services | Delete — keep `37b90644…81f2…` |
| `37d90644-d524-8173-bd01-f579963d0509` | Phoenix Training Center | Delete — keep `37b90644…81fb…` |
| `37d90644-d524-....` (second Phoenix TC dup) | Phoenix Training Center | Delete |
| `37d90644-d524-81ac-...` (Vancouver WA dup 1) | Vancouver, WA | Delete — keep `37b90644…81ac…` |
| `37d90644-d524-....` (Vancouver WA dup 2) | Vancouver, WA | Delete |
| `37d90644-d524-81d0-985a-c73bc8339449` | Tucson Old Vail Road | Delete — keep `37b90644…8109…` |
| `37d90644-d524-8134-9783-eca223dba0cb` | Irvine | Delete — keep `37b90644…814a…` |
| `37d90644-d524-81f8-8dbe-e3e07785560f` | Sacramento | Delete — keep `37b90644…8111…` |

**Memberships dupes (delete via UI — keep the one with fullest content):**
| Dup ID(s) | Name | Keep |
|---|---|---|
| 2 extra rows | The Beavers (×3 total) | Keep `37d90644-d524-8118-9bc4-f7a3e08a57b9` |
| 2 extra rows | AGC (×3 total) | Keep `37d90644-d524-811e-b8fc-fa65bc716c58` |
| 1 extra row | APWA (×2 total) | Keep `37d90644-d524-81f2-902d-c7ddbe28f8e6` |
| 1 extra row | Arizona Builders Alliance (×2 total) | Keep `37d90644-d524-8146-abe0-d82ef36fe939` |

**Projects dup:**
- I-10 $87M (`37b90644-d524-8102-85cd-efb13a29614c`) vs TxDOT I-10 $120M (`37d90644-d524-81a5-af38-c58e478f03a3`) — same source URL, same award, different values. $87M record richer; $120M record very thin. Review and merge/delete via UI.

**Orphan page:** `37d90644-d524-810e-9a9c-fc8149ba1b6e` (blank-titled Concrete Division standalone, not in DB)

### Checks performed (3a–3e)
- **3a Interconnection:** Company ↔ Divisions (9) ✓ · Divisions → Company (9) ✓ · Divisions → People (7 of 9 — PoweR has 0, Concrete has 1; both sourceless) ✓ · Divisions → Projects (7 of 9 linked; Concrete has 0 projects — sourceless per dossier) ✓ · Events → Company (3, all Sundt-linked) ✓ · Memberships → Company (8 unique, all SET) ✓ · Locations → Company (all originals SET) ✓ · Location originals → Division: 12/15 SET; Tempe HQ, Phoenix Ops, Phoenix Training = corporate, no division → genuinely sourceless ✓.
- **3b Description depth:** All 9 division bodies rich (Advanced Facilities, Building Group, Mining, PoweR, Heavy Industrial, Renewables, Transportation, Water, Concrete) ✓. Events have sourced bodies ✓. Memberships have sourced bodies ✓. Sample projects have sourced body content ✓ (Nashville body noted thin — scope/metrics missing — but dossier has no more detail; genuinely sourceless).
- **3c Address/location:** Company Address place filled (`place:Address`, lat/lng set) ✓. All 15 original Location rows have Adress text filled ✓. Austin TX new location has body + Division + Companies SET ✓. Division `Adress` (place type) empty on all 9 — requires lat/lng; dossier has none; no-geocoding rule → genuinely sourceless. Project `Adress` (place type) empty on all sampled projects — same rule.
- **3d Membership completeness:** 8 unique memberships present (DBIA, AGC, APWA, AzBA, The Beavers, ESOP Association, USGBC, ENR Top 400). Dossier names only DBIA. All others are post-dossier enrichment — valid. Dossier fully covered ✓.
- **3e Location tags:** AGC Safety Award = "Arizona" ✓. DBIA Milestone — no date/venue in dossier; sourceless ✓. Renewables Launch — date SET (2020-12-07) ✓; location tag empty — no specific venue in dossier; sourceless ✓.

### No new fillable gaps found from dossier
- All dossier-sourced data correctly recorded across company, divisions, projects, events, memberships, locations.
- Nashville CONRAC body thin (scope/metrics) — dossier has no additional detail; genuinely sourceless.
- PoweR division People — no leader named in dossier; genuinely sourceless.
- Concrete division Projects — no specific projects in dossier; genuinely sourceless.
- DBIA event date — no date in dossier; genuinely sourceless.
- Division/project place fields — no lat/lng in dossier; no-geocoding rule.
- **Result: 0 writes this pass. Record complete per dossier. Dup/orphan cleanup escalated (see below).**

### Manual UI steps outstanding (updated 06-13 sixth pass)
1. **Locations dup cleanup** — delete 11+ dup rows (see table above); Austin TX is net-new unique, keep it.
2. **Memberships dup cleanup** — delete 6 dup rows (see table above); 8 unique memberships correct.
3. **Orphan Concrete page** — delete `37d90644-d524-810e-9a9c-fc8149ba1b6e` via UI.
4. **I-10 dup review** — $87M vs $120M: same press release, same award; recommend keeping $87M record (richer) and deleting $120M record, or merging the $120M figure into the $87M body.
5. Projects Underway view → clear `__TEMPLATE__` filter, set Contractors = Sundt.
6. Existing Software view → clear `__TEMPLATE__` filter.
7. Construction Projects Location → add Idaho, Oregon options for Northwest projects.
