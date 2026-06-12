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

## Audit pass — 2026-06-11 (post-load verification)

**3 fills:**
1. **Company record** `17b90644-d524-8055-88ec-f7f399f27e9d` — `BW Category` updated from `["Builder"]` → `["Builder", "Design and Architecture", "Developer"]`. Source: https://www.kiewit.com/about-us/
2. **Grain Belt Express** `37b90644-d524-817a-ad8c-d733e8e0bf2b` — `Location` += Kansas (was [Missouri, Illinois, Indiana]; dossier names Kansas first). Source: https://www.power-technology.com/news/quanta-kiewit-grain-belt-express/
3. **Federal Way Link Extension** `37b90644-d524-81b9-bddf-c139e3ac792f` — `Location` = [Washington] (was empty). Source: https://www.kiewit.com/projects/federal-way-link-extension/

**Confirmed schema gap (manual UI):** Oregon and Alaska absent from shared Construction Projects `Location` multi-select → Bull Run and Nome cannot be tagged until Zack adds these options in the UI. Washington and Kansas ARE present (confirmed by successful writes above).

**Stale body artifact:** Grain Belt body contains "(Kansas leg not taggable in Location — see body.)" — now outdated; harmless per additive-only rule.

**Confirmed complete (no further fillable gaps):**
- 3a: all 17 divisions → Companies=Kiewit; all 15 projects → Contractors=Kiewit; both people → Company; 7 memberships/11 locations/2 events/4 software → company
- 3b: all division + project bodies at full dossier depth
- 3c: company Address place + 17 division places filled; 8/15 project places filled; 7 remain genuinely sourceless (no coords, multi-state corridors)
- 3d: all 7 memberships present with company relation
- 3e: all fillable Location tags applied; Alaska/Oregon remain schema-blocked

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

## Audit pass — 2026-06-12 (#3 — post Kiewitt3-thin + Kiewitt4 load)

**27 division rows now live** (17 original + WSCI + KW-FL + InEight + Kiewit Supply Network + Kiewit Foundations + Kiewit Canada Group + Kiewit Water Facilities South + Kiewit Louisiana + Healy Tibbitts + McNally Tunneling). Came from 06-12 sessions loading Kiewitt3-thin.md and Kiewitt4.md.

**3 division Adress places filled:**
- Kiewit Foundations Co. `37d90644-d524-8100` → 1550 Mike Fahey St., Omaha, NE 68102 (41.265948/-95.935909). Source: https://www.kiewit.com/locations/
- Healy Tibbitts Builders, Inc. `37d90644-d524-8176` → 99-994 Iwaena Street, Suite A, Aiea, HI 96701 (21.3831/-157.929). Source: https://www.kiewit.com/locations/
- McNally Tunneling Corp. `37d90644-d524-816a` → 800 Westpoint Parkway, Suite 1130, Westlake, OH 44145 (41.4553/-81.9179). Source: https://www.kiewit.com/locations/

**1 division Projects edge filled:**
- Kiewit Louisiana Co. `37d90644-d524-8167` → Projects: Calcasieu Pass LNG `37d90644-d524-81b3-be19`. Source: https://www.prnewswire.com/news-releases/venture-global-lng-and-kiewit-announce-execution-of-epc-contract-for-calcasieu-pass-lng-export-facility-300761731.html

**20 project Adress places filled:**
| Project | ID | Place |
|---|---|---|
| I-55 Bridge (Memphis) | `37d90644-d524-81fc` | Memphis, TN 38103 (35.1495/-90.0489) |
| Midtown Tunnel | `37d90644-d524-81c7` | Portsmouth, VA 23704 (36.8354/-76.2983) |
| Alaskan Way Viaduct | `37d90644-d524-811b` | Alaskan Way, Seattle, WA 98101 (47.6062/-122.3432) |
| BART SV Phase II CP2 | `37d90644-d524-81dc` | San Jose, CA 95110 (37.3382/-121.8863) |
| DART Irving Orange Line | `37d90644-d524-81e9` | Irving, TX 75038 (32.814/-96.9489) |
| Monroe County CCGT | `37d90644-d524-81bc` | Monroe County, GA 31029 (33.0209/-83.9196) |
| Birdsboro Power Plant | `37d90644-d524-81b8` | Birdsboro, PA 19508 (40.2662/-75.8138) |
| AES Southland | `37d90644-d524-814b` | 21730 Newland St., Huntington Beach, CA (33.7092/-118.0001) |
| Henry Ford Health CEH | `37d90644-d524-81ca` | Detroit, MI 48202 (42.3674/-83.0552) |
| South Fork Wind | `37d90644-d524-8152` | Narragansett, RI 02882 (41.3802/-71.4773) |
| Prospect Lake CWC | `37d90644-d524-817c` | Fort Lauderdale, FL 33301 (26.1224/-80.1373) |
| Elliott West | `37d90644-d524-8114` | Seattle, WA 98119 (47.6272/-122.3745) |
| Savannah River HFTOC | `37d90644-d524-81ac` | Aiken, SC 29802 (33.5604/-81.7198) |
| CT State Pier | `37d90644-d524-8172` | New London, CT 06320 (41.3557/-72.0995) |
| Miramar WTP | `37d90644-d524-813f` | San Diego, CA 92131 (32.9157/-117.1325) |
| TECO CHP | `37d90644-d524-81d4` | Tampa, FL 33601 (27.9506/-82.4572) |
| Texas LNG | `37d90644-d524-8199` | Brownsville, TX 78520 (25.9017/-97.4975) |
| Beaver Lake FEED | `37d90644-d524-816d` | Rapides Parish, LA 71301 (31.3065/-92.4454) |
| ECA LNG | `37d90644-d524-81cf` | Ensenada, Baja California, Mexico (31.8676/-116.5956) |
| Canada Nuclear Waste | `37b90644-d524-819c` | Ignace, Ontario, Canada (49.4166/-91.6667) |

**Genuinely sourceless / left empty:**
- Kiewit Louisiana Co. Adress — no street address in source
- Kiewit Supply Network Adress — corporate unit, no distinct office address
- NRG Gas Plants + Front Range Pipeline Adress — multi-site/multi-state, no single address
- KETS 2026 + AGC Convention 2026 dates — year-only in source
- Rick Lanoha + Dave Miles LinkedIn URLs — not in dossier
- Kiewit Infrastructure West address — dossier null (multi-district)

**Confirmed intact:** 39 Construction Projects · 8 software rows · 8 memberships · 6 events · 12 locations · 615+ people

---

## Second-pass load — 2026-06-12 (Kiewitt4.md)

Ground truth: `Enlaye Notion/Kiewitt/Kiewitt4.md` (4016 lines, run date 2026-06-12). Additive-only on top of 06-10 build. Schema note: Type options "Water/Marine/Nuclear" were never in the live DB; mapped water→Municipal & Community/Infrastructure, nuclear→Government, LNG→Industrial/Chemicals.

**New divisions (2):**
| Division | ID |
|---|---|
| Western Summit Constructors Inc. (WSCI) | `37d90644-d524-8142-b339-d1e6533f785a` |
| Kiewit Water Facilities Florida Co. | `37d90644-d524-8174-b919-f5bf50335298` |

**New projects (23 — Contractors→Kiewit, Type/Location mapped to existing schema):**
| Project | ID | Type | Status |
|---|---|---|---|
| I-55 Bridge Replacement (Memphis) | `37d90644-d524-81fc-82db-e3dd82d983e9` | Transportation | In progress |
| Midtown Tunnel (Elizabeth River Crossing) | `37d90644-d524-81c7-9635-cea0aaeaa51f` | Transportation | Done |
| Central 70 (I-70 East Reconstruction) | `37d90644-d524-818c-8437-e69f8265e58c` | Transportation | Done |
| Alaskan Way Viaduct Demolition (SR 99) | `37d90644-d524-811b-8fef-ea12f0622458` | Transportation | Done |
| BART Silicon Valley Phase II - CP2 | `37d90644-d524-81dc-bac3-ed7f35375f46` | Transportation | In progress |
| DART Irving Orange Line Expansion | `37d90644-d524-81e9-ac93-e603624ef660` | Transportation | Done |
| Monroe County Combined-Cycle Power Plant | `37d90644-d524-81bc-93f6-e35bdf9e2668` | Energy & Power | Not started |
| Birdsboro Power Plant (485 MW CCGT) | `37d90644-d524-81b8-b1bd-e281f39791b6` | Energy & Power | Done |
| AES Southland Projects | `37d90644-d524-814b-b7e6-f3cc5e67a892` | Energy & Power | Done |
| Henry Ford Health Central Energy Hub | `37d90644-d524-81ca-9a03-f4d81951f6f5` | Energy & Power | In progress |
| South Fork Wind - Offshore Substation | `37d90644-d524-8152-bbd7-cbdcf5dd994a` | Energy & Power | Done |
| Prospect Lake Clean Water Center | `37d90644-d524-817c-8303-d83b6f08b39f` | Municipal & Community | In progress |
| Elliott West Wet Weather Treatment Station | `37d90644-d524-8114-aab5-fc6ae9602909` | Municipal & Community | In progress |
| Oroville Dam Spillways Emergency Recovery | `37d90644-d524-81b3-94b5-e4b0e030bcfe` | Infrastructure | Done |
| Calcasieu Pass LNG Export Facility | `37d90644-d524-81b3-be19-db579d54acb7` | Industrial / Chemicals | Done |
| Texas LNG Export Terminal (Brownsville) | `37d90644-d524-8199-a0a8-d17e8c3dda9b` | Industrial / Chemicals | Not started |
| Energia Costa Azul (ECA) LNG | `37d90644-d524-81cf-98f0-eb0d6a646979` | Industrial / Chemicals | Done |
| Front Range Pipeline Facilities (NGL) | `37d90644-d524-8188-a76f-fc8107a3ba32` | Industrial / Chemicals | Done |
| Savannah River HFTOC | `37d90644-d524-81ac-9f13-f229e4dded51` | Government | In progress |
| Connecticut State Pier Redevelopment | `37d90644-d524-8172-8104-f8571458bce1` | Infrastructure | Done |
| Miramar Water Treatment Plant Expansion | `37d90644-d524-813f-b8b4-f45bd26a3900` | Municipal & Community | Done |
| Beaver Lake Renewable Energy (FEED) | `37d90644-d524-816d-94cb-d965a738ba5f` | Industrial / Chemicals | Not started |
| TECO Combined Heat and Power Plant | `37d90644-d524-81d4-b9f3-c0aca7c475c9` | Energy & Power | Done |

**Division Projects relations updated (full URL list re-passed):**
- Kiewit Infrastructure Co. → Key Bridge + Midtown Tunnel + Central 70 + DART + Savannah River + CT State Pier
- Kiewit Infrastructure West Co. → CA HSR + Port Arthur + Nome + Federal Way + Klamath + S.Central LR + Alaskan Way + BART + Elliott West + Oroville Dam
- Kiewit Infrastructure South Co. → I-55 Bridge
- Kiewit Power Constructors Co. → Homer City + AES Southland + Henry Ford CEH
- Kiewit Energy Group Inc. → Grain Belt + Calcasieu Pass + Texas LNG + ECA LNG
- TIC – The Industrial Company → NRG + Monroe County + Birdsboro + Calcasieu Pass + Front Range + TECO CHP
- Kiewit Engineering Group Inc. → Texas LNG + Beaver Lake
- Kiewit Offshore Services → Salamanca + South Fork Wind
- Kiewit Development Company → Central 70 + Henry Ford CEH
- Western Summit Constructors Inc. → Miramar WTP
- Kiewit Water Facilities Florida Co. → Prospect Lake

**New events (3):**
| Event | ID |
|---|---|
| Kiewit Engineering Technical Summit 2026 | `37d90644-d524-8108-ad8f-ca4695ea9fae` |
| Future Women in Kiewit (FWIK) Summit 2025 | `37d90644-d524-8175-a559-cbafefc92f73` |
| EPC Show 2026 (Houston TX, George R. Brown) | `37d90644-d524-813b-8e20-f34b1ab21c42` |

**New membership (1):** ASCE `37d90644-d524-81f0-bec0-fdcc32b47137`

**New software (4):**
| Row | ID |
|---|---|
| SAP ERP ECC 6.0 + SAP HCM | `37d90644-d524-81c5-ad69-c15448674a9b` |
| Autodesk Revit / Navisworks / BIM360 | `37d90644-d524-8196-813f-fcf0f6300ce8` |
| Bentley OpenRoads Designer (ORD) | `37d90644-d524-817c-91fa-ceac9b74ac4d` |
| Tekla Structures | `37d90644-d524-81b7-aaf2-f88cc39bc0f1` |

**Companies DB updated:** Construction Projects = 39 URLs (16 existing + 23 new). Companies Software = 8 URLs (4 existing + 4 new).

**Company body enriched (insert_content):** ENR 2025/2026 ranks · net income $1.315B · 4K+ engineering / 16K+ craft staff · NAVFAC SIOP $8B / Medical $1B / Key Bridge est $1.7B / VA Denver $570.75M / JBER $310M · UEI J9FBNDSUJCW3 / CAGE 6EVG6 · 1,000+ reqs / 24 EHS openings / tool stack.

**Not filled (no sourced value):** ECA LNG Location tag (Mexico not in DB options — noted in body). Project `Adress` place for projects with no single precise address (multi-state, corridor, or Mexico).
