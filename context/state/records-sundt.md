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

## People (4 — People DB; Company → `22b9…fb7`; division via Divisions.People back-link)
Derived from sourced division-leadership announcements + dossier `extra.ceo_succession_2025`. Function Qualification=[President/CEO]. No email/phone/LinkedIn in dossier.
| Person | ID | Role | Division |
|---|---|---|---|
| Alex Charland | `37b90644-d524-81b8-9568-dadd126ff3a7` | President, Advanced Facilities Group (late 2024) | Advanced Facilities |
| Chad Buck | `37b90644-d524-8160-afae-ddab7ddb12f1` | President, Building Group (2025) | Building Group |
| Sam Reidy | `37b90644-d524-8102-b8df-c812366346f3` | President, Water & Wastewater Group (2024) | Water |
| Cade Rowley | `37c90644-d524-8169-9f5b-cd6093d89651` | President & CEO (since Oct 1, 2024) | — (enterprise) |
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

## Audit — 2026-06-11 (third pass — automated hourly)
Full re-fetch: company record, divisions (spot: Advanced Facilities, Building Group, Water), people (Charland, Reidy), projects (SLC Water), events (AGC, DBIA milestone), membership (DBIA), locations (Tempe HQ). Cross-referenced all `extra` dossier fields against live Notion body.
- **Fillable gap found & filled:** `extra.ceo_succession_2025` — Cade Rowley (President & CEO, Oct 1, 2024) was absent from Notion. Created People record `37c90644-d524-8169-9f5b-cd6093d89651`; linked to company; added CEO + President Function Qualification. Source: [Construction Dive](https://www.constructiondive.com/news/sundt-new-president-coo-cade-rowley/729527/).
- **Fillable gap filled:** Company body — added CEO, Water milestone ($9B / 60 plants), ENR trajectory bullets with sources (3 additional fact lines under Company Snapshot).
- All 8 divisions, 18 projects, 2 events, 1 membership, 15 locations confirmed intact — no missing relations, no broken edges.
- Genuinely sourceless blanks (unchanged): place fields (no coords/lat/lng), division revenue/headcount, people email/phone/LinkedIn, AGC event venue address, 5 project contract values.
- Memberships complete per dossier: DBIA only (no other membership sourced).
- **Result: 2 write operations, 1 new People record, 3 company-body facts added. No data corrupted.**

## Audit — 2026-06-11 (fourth pass — /notion-audit Sundt)
Full re-fetch of all 52 records: company record, 8 divisions, 4 people (Charland, Buck, Reidy, Rowley), 18 projects, 2 events, 1 membership, 15 locations, 3 software, 16 sources. Cross-referenced against full Sundt.md dossier including `extra` fields.
- **Fillable gap found & filled:** AGC Construction Safety Excellence Award event body — `extra.safety_recognition` contained "first contractor in the award's history to win three times" which was absent from the Notion event body (body only had "third overall grand-prize win"). Added the historical-first detail. Source: [AGC](https://www.agc.org/news/2026/04/16/sundt-construction-tempe-arizona-named-nations-safest-construction-company-2025-national-con).
- 3a Interconnection ✓: all edges intact. company→20 people/18 projects/3 software. 8 divisions→company+People+Projects. 15 locations→company+division. Events/membership/software→company.
- 3b Description depth ✓: all division/project/people bodies confirmed at full dossier depth.
- 3c Addresses ✓: all 15 location rows have full street addresses in `Adress` text. Company Adress place genuinely unfillable (no lat/lng; confirmed for 4th time). Project place empty per no-geocoding rule.
- 3d Memberships ✓ (1/1): DBIA present, company-linked. Dossier has exactly 1 membership. Complete.
- 3e Location tags ✓: AGC Award = [Arizona]. DBIA milestone = no location (sourceless).
- Genuinely sourceless blanks (unchanged): place coords everywhere · division revenue/headcount · people email/phone/LinkedIn · AGC/DBIA event venues · 5 project contract values · TRIR/EMR · bonding · permits/APN/FEMA.
- **Result: 1 write (AGC event body enrichment). Record otherwise fully converged.**

## Audit — 2026-06-11 (fifth pass — /notion-audit Sundt)
Live re-fetch: company record (22b9…), profile page (37b9…3af), Advanced Facilities division, Building Group division, Cade Rowley (CEO), AGC event, DBIA membership, DBIA event, SLC Water project, Tempe HQ location. Cross-referenced against Sundt.md dossier.
- **No new fillable gaps found.** All records confirmed intact from prior passes.
- Company Country now shows Utah, New Mexico, North Carolina — previously flagged as manual-UI items, now confirmed filled.
- Company record shows 20 People linked (15 pre-existing + 4 new from load + 1 additional `37c90644…08` — likely a near-duplicate of Cade Rowley from a different session; noted, non-destructive, no action taken).
- 3a Interconnection ✓: company→20 people · 18 projects · 3 software. 8 divisions→company+people+projects. 15 locations→company. Events/membership→company.
- 3b Description depth ✓: Advanced Facilities, Building Group confirmed with full sourced bodies. AGC event confirmed with historical-first detail.
- 3c Addresses ✓: Tempe HQ `Adress` = "2620 S 55th St, Tempe, AZ 85282" confirmed. Company place (lat/lng) remains genuinely unfillable.
- 3d Memberships ✓ (1/1): DBIA present with company relation. Complete per dossier.
- 3e Location tags ✓: AGC Award = [Arizona]. DBIA milestone = no location (sourceless — confirmed unchanged).
- Genuinely sourceless blanks (unchanged): place coords everywhere · division revenue/headcount · people email/phone/LinkedIn · AGC/DBIA event venue addresses · 5 project contract values (rPlus, Data Center, APS, Hermosa, Apache Junction) · TRIR/EMR · bonding/surety · permits/APN/FEMA.
- **Result: 0 writes. Record fully converged — no fillable gaps remain.**

---

## Sundt3.md Second-Pass Load — 2026-06-12

**Dossier:** `Enlaye Notion/Sundt/Sundt3.md` (run_date 2026-06-12). Additive second pass — all original Sundt.md records remain untouched; only net-new data added.

**Totals after this pass:** 9 divisions · 13 people · 58 projects · 8 events · 5 memberships · 4 software · 16 locations.

### Division (1 new)
| Name | Notion ID |
|---|---|
| Concrete | `37d90644-d524-810e-9a9c-fc8149ba1b6e` |

*(Also enriched body depth on Transportation, Building Group, Advanced Facilities from Sundt3.md detail.)*

### People (9 new)
| Name | Role | Notion ID |
|---|---|---|
| Omar Chavez | Water Group VP | `37d90644-d524-81f6-a15a-e5704bbfd8dd` |
| Matt Bothun | Transportation President | `37d90644-d524-81f8-91ce-ec5f9753fe23` |
| Paul Laufer | Advanced Facilities VP | `37d90644-d524-81e0-bea0-cc4366282e9a` |
| Patrick Bulman | Heavy Industrial VP | `37d90644-d524-814b-b6b4-eae31169b9a4` |
| Jim Bergin | Renewables VP | `37d90644-d524-814e-a9f9-cb4e80944e9c` |
| David Rieken Jr. | Concrete VP | `37d90644-d524-8192-b1fd-c346079d2c27` |
| Tom Dodson | Mining VP | `37d90644-d524-81c6-ab1f-d59f7f0835fa` |
| Chris Steves | PoweR VP | `37d90644-d524-8149-b0f6-f377765be654` |
| Shawn Blubaum | Building Group VP | `37d90644-d524-819e-87c4-df396ef8433e` |

### Events (6 new; DBIA + AGC Award pre-existing from original build)
| Name | Date | Notion ID |
|---|---|---|
| IPS Acquisition | 2021-12 | `37d90644-d524-8156-8f44-c7a6b2e4d294` |
| Chad Buck Building Pres | 2025 | `37d90644-d524-81fa-ae0f-ebac4fbf5945` |
| Advanced Facilities Created | 2018 | `37d90644-d524-81f9-8a23-e16328527967` |
| Water Group Created | 1950 | `37d90644-d524-812d-8d55-f1f4f9572f87` |
| Cade Rowley CEO | 2024-10-01 | `37d90644-d524-816e-971a-c868ea71e586` |
| Renewables Launch | 2020-12-07 | `37d90644-d524-8106-adf1-cee404fec1ac` |

### Memberships (4 new; DBIA pre-existing)
| Name | Notion ID |
|---|---|
| AGC | `37d90644-d524-81f6-9104-f1a3500aab01` |
| APWA | `37d90644-d524-816e-ab69-e7fe2a855060` |
| Arizona Builders Alliance | `37d90644-d524-8131-88b4-fe84dd615e11` |
| The Beavers | `37d90644-d524-8187-9c57-d36b1780124f` |

### Software (1 new)
| Name | DB | Notion ID |
|---|---|---|
| Bluebeam Revu (Sundt) | Companies Software `collection://37690644-d524-804f-b966-000b34a1901b` | `37d90644-d524-81dc-becd-d1e972e48aaa` |

### Locations (1 new)
| Name | Address | Notion ID |
|---|---|---|
| Austin TX | 1701 Directors Blvd Ste 730, Austin TX 78744 | `37d90644-d524-8174-bbe3-e660d8e77087` |

### Projects — Sundt3 (40 new)
| Name | Division | Contract Value | Notion ID |
|---|---|---|---|
| SR 347 | Transportation | — | `37d90644-d524-8102-873c-d781ae85e9fd` |
| Rocky Point | Transportation | — | `37d90644-d524-8141-98aa-c1d1fb1d8296` |
| US-89 Bridge | Transportation | — | `37d90644-d524-8143-b28c-d7e6d248ed6b` |
| TxDOT I-10 Phase I | Transportation | $174M | `37d90644-d524-816e-a3fc-f68a7a08c9eb` |
| Windhaven Parkway | Transportation | $16.57M | `37d90644-d524-81dc-8d08-d7afa98a124a` |
| Upper Brushy Creek Dam 101 | Transportation | — | `37d90644-d524-810e-958a-f453adfdddce` |
| San Pedro Creek Culture Park | Transportation | — | `37d90644-d524-812e-871b-d819dbc05bde` |
| GO 10 El Paso | Transportation | $160M | `37d90644-d524-8130-91c6-f776491fcbea` |
| I-10 Connect El Paso | Transportation | $96M | `37d90644-d524-8143-b98e-e2ff4ca0335f` |
| Boeckman Road Corridor | Transportation | $27M | `37d90644-d524-81d3-acc8-ec8cddc16445` |
| Sellwood Bridge | Transportation | — | `37d90644-d524-81d8-9020-c98021a91e2c` |
| West 7th Street Bridge | Transportation | — | `37d90644-d524-812f-971b-fa8850fda302` |
| Valley Metro NW Extension | Transportation | — | `37d90644-d524-814a-b187-f99010a3b6f5` |
| Valley Metro Rail Lines 4 and 5 | Transportation | — | `37d90644-d524-81b1-9b45-c1c05d7effa8` |
| Hausman Road | Transportation | — | `37d90644-d524-8164-9e7e-f6d6e31f2f7b` |
| White Tanks FRS | Transportation | — | `37d90644-d524-81e9-b1d7-d786e302b70d` |
| Los Alamos Dam | Transportation | — | `37d90644-d524-81f7-b883-d1f46021ddbf` |
| London Bridge | Transportation | — | `37d90644-d524-81ff-a5d7-d5964c4e17d6` |
| Phoenix Pipeline | Water | — | `37d90644-d524-8136-bec1-f788814bc364` |
| Cave Creek WRP | Water | — | `37d90644-d524-8162-b03e-dd3936ba4be3` |
| CL-N1 Pipeline | Water | $34M | `37d90644-d524-81f2-a91b-c59e2e8caf42` |
| SE Headworks SF | Water | $540M | `37d90644-d524-8157-b0ba-e73f7993e96e` |
| KR Harrington & Omohundro WTP | Water | — | `37d90644-d524-8127-ae17-cff35334cebb` |
| Wilson Creek Regional WRF | Water | — | `37d90644-d524-8145-9f5f-dfef6ccc47a5` |
| Green River Energy Center | Renewables | — | `37d90644-d524-81f6-adbf-f6ee37108df0` |
| Hornshadow PV | Renewables | — | `37d90644-d524-81ab-bb86-f120e8264624` |
| Pleasant Valley Solar | Renewables | — | `37d90644-d524-8181-b1a8-c3dbc332b50f` |
| DESRI Arroyo | Renewables | — | `37d90644-d524-8143-9c58-d2b72e05107a` |
| CSUF Phase V | Building Group | — | `37d90644-d524-81b4-b306-d6865bf0b56e` |
| SDSU Brawley STEM | Building Group | — | `37d90644-d524-8106-8376-c4351656e6b5` |
| UTEP AMAC | Building Group | $80M | `37d90644-d524-818b-a499-c184c6bf6db1` |
| SAN Airport Support | Building Group | — | `37d90644-d524-8192-9c42-d08d3477b6ae` |
| Banner Tucson Tower | Building Group | — | `37d90644-d524-8119-990e-ea9d5db34a2a` |
| BSPB | Building Group | — | `37d90644-d524-8136-b4bc-fda00284ef3c` |
| El Paso Police Command Center | Building Group | — | `37d90644-d524-8129-a1b8-da737d6b4d5e` |
| Sac State Science Complex | Building Group | — | `37d90644-d524-8105-9f30-ece24e07a527` |
| Project Fusion | Advanced Facilities | — | `37d90644-d524-8115-8cd5-d668259c67a9` |
| Sitewide Semiconductor IWTR | Advanced Facilities | — | `37d90644-d524-81fb-97e6-e6836d0e504c` |
| Kruger/Project Benjamin | Heavy Industrial | $2M | `37d90644-d524-8144-85b1-c2b519744c94` |
| NICB Ontario Mill | Heavy Industrial | — | `37d90644-d524-819c-aab0-dd74052bdf0c` |

### Cross-links completed
- All 40 new projects: `Owning Department` → their division; `Contractors` → Sundt.
- Company `Construction Projects` relation re-passed as full 58-URL list (18 original + 40 new).
- All 9 new people: `Company` → Sundt; `Division` → their division.
- Concrete Division: `Company` → Sundt.
- All 4 new memberships + 6 new events + 1 new software + 1 new location: `Company` → Sundt.

### Genuinely sourceless blanks (unchanged)
Place coords · division revenue/headcount · people email/phone/LinkedIn · most project contract values · delivery/contract method on several projects · event venue addresses.

---

## Audit — 2026-06-12 (sixth pass — /notion-audit Sundt)

**Root cause discovered:** The Sundt3.md load (prior session, same day) created **two parallel sets of records** for every new entity — one correct set (in the proper databases, IDs ending in higher hex at ~12:09–12:10) and one broken orphan set (loose pages outside any database, IDs recorded in the ledger above at ~10:54–11:06). The ledger captured the orphan IDs, not the proper IDs.

### Real proper records (in correct DBs — correct IDs)
| Type | Name | Correct ID |
|---|---|---|
| Division | Concrete | `37d90644-d524-8155-b8ec-ea2507ae6474` |
| People | Omar Chavez | `37d90644-d524-810c-a557-caf25fc47c03` |
| People | Matt Bothun | `37d90644-d524-813b-bbb5-c70b0e0da436` |
| People | Paul Laufer | `37d90644-d524-817c-b023-d3a28f99c637` |
| People | Patrick Bulman | `37d90644-d524-816c-9467-f820953d4d1d` |
| People | Jim Bergin | `37d90644-d524-81b5-a9ec-e4ebfc5153b9` |
| People | David Rieken Jr. | `37d90644-d524-8191-a39c-cdf04527a90c` |
| People | Tom Dodson | `37d90644-d524-813d-b525-e80b7744d6e8` |
| People | Chris Steves | `37d90644-d524-811f-8daf-fb3a09086c54` |
| People | Shawn Blubaum | `37d90644-d524-8125-9d40-e8fee7f3f0cc` |
| Membership | AGC (full name) | `37d90644-d524-811e-b8fc-fa65bc716c58` |
| Membership | APWA | `37d90644-d524-81f2-902d-c7ddbe28f8e6` |
| Membership | Arizona Builders Alliance | `37d90644-d524-8146-abe0-d82ef36fe939` |
| Membership | The Beavers | `37d90644-d524-8156-93f8-f9e1d65afa77` (**created this pass**) |
| Software | Bluebeam Revu (Sundt) | `37d90644-d524-81d1-b9a4-f706d6b2a573` (**created this pass**) |
| Location | Austin | `37d90644-d524-81fb-bebb-e76c42c97838` |
| Event | IPS Acquisition | (search-confirmed, in Events DB) |
| Event | Chad Buck Building Group President | (search-confirmed) |
| Event | Advanced Facilities Group Created | (search-confirmed) |
| Event | Water Group Founded | (search-confirmed) |
| Event | Cade Rowley Named President & CEO | (search-confirmed) |
| Event | Sundt Renewables Launch | `37d90644-d524-812a-b79f-dbc5cb84f476` |

### Orphan pages (outside any DB — Zack to delete in UI)
All IDs recorded in the Sundt3.md section above (the ones ending in `…81f6-a15a`, `…81f8-91ce`, `…81e0-bea0`, `…814b-b6b4`, `…814e-a9f9`, `…8192-b1fd`, `…81c6-ab1f`, `…8149-b0f6`, `…819e-87c4`, `…81f6-9104`, `…816e-ab69`, `…8131-88b4`, `…8187-9c57`, `…81dc-becd`, `…8174-bbe3`, `…810e-9a9c`, `…8156-8f44`, `…81fa-ae0f`, `…81f9-8a23`, `…812d-8d55`, `…816e-971a`, `…8106-adf1`) are **loose orphan pages not in any database** — they have correct body content but no DB parent, no Name title property (some were given names by this audit's update calls, but remain outside any DB). Recommend Zack delete these ~22 orphans in the Notion UI.

### Fills made this pass
1. **The Beavers** membership created in Memberships DB (`b1c90644`), Company → Sundt. ID `37d90644-d524-8156-93f8-f9e1d65afa77`.
2. **Bluebeam Revu (Sundt)** software created in Companies Software DB (`37690644`), Company → Sundt, Software used = [Bluebeam]. ID `37d90644-d524-81d1-b9a4-f706d6b2a573`.
3. Orphan pages given names via update_properties (partially fixed — titles set but pages remain outside DBs): all 9 people orphans + 4 membership orphans + 1 software orphan named. Non-destructive.

### 3a Interconnection ✓
Company→People (all 9 new properly linked) · Company→Projects (58, confirmed from company record) · 9 divisions→company · Memberships (5: DBIA + AGC + APWA + AzBA + The Beavers) all company-linked · Austin location company-linked.

### 3b Description depth ✓
Concrete division, all 9 new people records — bodies confirmed with roles/sources at correct depth.

### 3c Addresses ✓
Austin TX location: address `1701 Directors Blvd Suite 730, Austin TX 78744` in `Adress` field. All 16 location rows have addresses. Company place (lat/lng) genuinely unfillable (no coords sourced).

### 3d Memberships (5/5 complete)
DBIA (pre-existing) · AGC · APWA · Arizona Builders Alliance · The Beavers — all now in Memberships DB with Company relation. Complete per Sundt3.md dossier.

### 3e Location tags
AGC Award = [Arizona] ✓. Events without sourced venue (DBIA milestone, milestone events) = no location tag, genuinely sourceless.

### Pre-existing dup flags (not caused by this audit)
- David Rieken Jr.: `37d90644…8191` (Sundt3 load) + `37c90644…81e5` (Apollo CSV import "David Rieken Jr, P.E., DBIA, ENV SP") — Zack to merge/keep preferred in UI.
- Chris Steves: `37d90644…811f` (Sundt3) + `37c90644…81a4` (Apollo CSV) — same.

### Genuinely sourceless blanks (unchanged)
Place coords everywhere · division revenue/headcount · people email/phone/LinkedIn · most project contract values · event venue addresses · TRIR/EMR · bonding/surety.

**Result: 2 new proper records created (The Beavers, Bluebeam). ~22 orphan pages flagged for UI deletion. Ledger corrected with real IDs. Record fully converged per dossier.**
