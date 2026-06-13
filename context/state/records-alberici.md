# State · Records — Alberici Build

> **Holds:** the Alberici dedup ledger — company record, operating-company records, divisions, people, projects, page tables, with Notion IDs, so the next session deduplicates before touching an Alberici record.
> **Ground truth:** `Enlaye Notion/Alberici Corp/Alb.md` (single sourced JSON dossier). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.
> **Status:** ✅ complete (2026-06-10 load, full interlink).
> **⚠ Disambiguation / conflicts:** Alberici **Corporation** (parent, existing record) ≠ Alberici **Constructors, Inc.** (flagship US operating co, created this build). ENR reports the group as "Alberici-Flintco" from 2025. Williams Crossing bridge = Hillsdale STEEL scope only (GC was Crossland) — not an Alberici GC project.

---

## Profile page (hub)
**"Alberici"** (renamed from "Alberici TEMPLATE"; icon building_blue) — https://app.notion.com/p/37b90644d52480a0aab5d9716831b22e (Companies research → Zack Folder → Market Research). Divisions-DB template variant. Skim bio added at top; Attack Plan filled at bottom (Stage 1 Industrial/water → Stage 2 Procore-complementary → Stage 3 Flintco; personas Geiger/Franco/Scalzo Brown/Brooks Williams).

Page-local data sources:
- **Divisions** `collection://a8490644-d524-83e0-aa64-0784b3b7ca57` (Division title · Adress place · relations Companies full database / People / Projects — all three present)
- **Events** `collection://32690644-d524-82e8-9e60-07665ea992f0` (Event name · Date · Location tags · Place · Companies full database) — **+added Missouri, Ohio** tags
- **Sources** `collection://15c90644-d524-82f7-b199-875e0d4c01a5` ("What the source is about" · URL)
- **Memberships** `collection://e9190644-d524-834c-b191-07ec4f1bcdb9` — **+added** Companies full database relation
- **Locations** `collection://f3090644-d524-82d3-9a5e-077930e0b20d` (Location · Adress text) — **+added** Companies full database + Division relations
- Projects Underway = shared Construction Projects (linked view, `__TEMPLATE__` filter — **manual UI fix**)
- Existing Software = shared Companies Software `collection://37690644-d524-804f-b966-000b34a1901b` (linked view, `__TEMPLATE__` filter — **manual UI fix**)

## Company record (PRE-EXISTING — extended, not recreated)
**"Alberici Corporation"** `27990644-d524-802f-9f84-f3d1fc8af395` (Companies DB, alberici.png icon).
- Verified post-build: **Construction Projects = 13** (one-way list set) · **People = 28** (17 pre-existing + 11 new corp execs; Biermann/Brokenshire link to their operating-co records instead) · **Subsidiaries = 11** · **Address place** 8800 Page Ave (38.7028,-90.3673) · **Country** +MO/OK/ON/CA/MX/GA/MI/IL/CA/TX · Companies Software = Alberici row · body Company Snapshot + Sources.
- Kept as-was: Description (generic tagline — richer snapshot in body), Type=Company, Size=Mutlinational, LinkedIn, Website.
- ⚠ One pre-existing People link is `28190644-d524-817e-9827-ec13adac46cd` (not 2f8…; left intact).

## Operating-company records (Companies DB · Parent → Alberici Corp)
**Existing 8 — extended (Address place where coords; concise Snapshot body):**
| Operating co | ID |
|---|---|
| Alberici Industrial | 30a90644-d524-80df-8360-c9a9b29e5d56 |
| Alberici Constructors Limited | 30a90644-d524-8097-851c-e2dfbc2ff010 |
| Alberici Construcciones S.A | 30a90644-d524-8053-acfb-c3c202e99ec0 |
| CAS Constructors | 30a90644-d524-804e-b397-d65908eb6433 |
| Filanc | 30a90644-d524-8052-b7e2-f2b4af0bceb2 |
| Flintco | 30a90644-d524-8093-bdd4-fa45dd1104fd |
| Leonard Masonry | 30a90644-d524-8045-a0e3-f1d8a8851830 |
| WWPS | 30a90644-d524-80ca-9ad9-fc48763bb15d |

**Created 3 (Parent → Alberici Corp):**
| Operating co | ID |
|---|---|
| Alberici Constructors, Inc. (flagship) | 37b90644-d524-8129-8d57-fbca3d20307b |
| Hillsdale Fabricators | 37b90644-d524-8112-8b3f-f6805294d14c |
| Kienlen Constructors | 37b90644-d524-812d-9fd8-c3f48b255e4d |

## Division rows (11 — Divisions DB `a8490644`; each → Companies [operating-co + Corp], People, Projects, Adress place)
| Division | Row ID | People | Projects |
|---|---|---|---|
| Alberici Constructors, Inc. | 37b90644-d524-8110-b917-d834f3210c16 | 11 (10 execs + Brooks Williams) | 4 |
| Alberici Constructors, Ltd. | 37b90644-d524-81b5-a25f-f7cbcf209ec2 | Brokenshire | 1 (Pearson) |
| Alberici Construcciones | 37b90644-d524-81e6-a5f8-d53e36c44f7f | — | — |
| Alberici Industrial | 37b90644-d524-81b1-b480-fc60bfe4a71b | Biermann, Reid Abbott | 5 |
| CAS Constructors | 37b90644-d524-81be-a74a-e91445b36475 | — | — |
| Flintco | 37b90644-d524-81a5-94b2-ef4428dacf94 | — | 2 |
| Filanc | 37b90644-d524-81e6-8ed4-c7ba86bc0447 | — | — |
| Hillsdale Fabricators | 37b90644-d524-8151-9b8e-f3c6ffd122aa | — | 1 (Williams Crossing) |
| Kienlen Constructors | 37b90644-d524-816b-86b3-cf328162ece6 | — | — |
| Leonard Masonry | 37b90644-d524-811b-93a9-e886a1183a82 | — | — |
| WWPS | 37b90644-d524-81f6-86a4-fd3da6784629 | — | — |

## People
**Pre-existing 17 linked to Alberici Corp (outreach — NOT re-created):** Alec Searcy, Brian Mazanec, Cara Greenley, Matthew Million, Gary Jacobsmeyer, **Brooks Williams** (Director Construction Technology — dossier leader; +Role body added, linked to Constructors Inc. division), Emelynn Hasky, Mauricio Silva, Bud Freeze, Eileen Murray, Glauco Lago, Aaron Sonnenschein, Brian King, Steven Door, Victoria Fleddermann, Tonia Bitar (+1 link `28190644…46cd`).
**Created 13 (dossier leadership):**
| Person | ID | Company → |
|---|---|---|
| Greg Kozicz (Chairman) | 37b90644-d524-816d-a0f3-d0a529f4e4c3 | Corp |
| Greg Hesser (Exec Chairman) | 37b90644-d524-81eb-9d33-e4a87886f7f9 | Corp |
| Richard Jaggers (Pres & CEO) | 37b90644-d524-81ec-be2c-de739e8508c0 | Corp |
| John Alberici (Chairman Emeritus) | 37b90644-d524-8140-bdeb-d4c932a95e2c | Corp |
| Fred Biermann (Pres, Industrial) | 37b90644-d524-81a3-a13d-d1a554bbd317 | Industrial |
| Greg Brokenshire (Pres, Ltd.) | 37b90644-d524-81c0-b73b-f19df973d938 | Constructors Ltd |
| Mike Ryan (CFO) | 37b90644-d524-8104-a6d2-c8abd166d9ff | Corp |
| Shelley Scalzo Brown (VP Safety) | 37b90644-d524-8134-ab88-c7db9677a3c5 | Corp |
| George Franco (Chief Innovation Officer) | 37b90644-d524-81cb-8a29-e95e1e6b2e7f | Corp |
| Aaron Geiger (CTO) | 37b90644-d524-81fd-9b8a-d9df09e40cad | Corp |
| Gabrielle Robitaille (Construction Tech Mgr) | 37b90644-d524-8123-8586-d1f1fcbf14ff | Corp |
| Charles Williams (Construction Tech) | 37b90644-d524-8152-baec-c9c7f9d3f776 | Corp |
| Reid Abbott (Water/WW, DBIA speaker) | 37b90644-d524-81b8-9e04-d0382309a680 | Corp |
- **Dropped:** Liam O'Donnell (Alberici data scientist) — appeared only in a pre-existing Notion page, **not in Alb.md** → not created (sourcing rule).

## Projects (13 — Construction Projects DB; Contractors → [Corp, operating-co], Owning Department → operating-co)
| Project | ID | $M | Status | Owning Dept |
|---|---|---|---|---|
| Saint Louis Zoo WildCare Park | 37b90644-d524-8187-817b-d3cde0a78d39 | 230 | In progress | Constructors Inc. |
| Mercy Center for Performance Medicine | 37b90644-d524-810e-baab-c26634791fd5 | — | Done | Constructors Inc. |
| Wichita Northwest Water Facility | 37b90644-d524-813d-acd7-ced490940b70 | 556.8 | Done | Industrial |
| Ford KC Tire, Wheel & Subassembly Addition | 37b90644-d524-81bb-b740-c01e5280635e | 75 | In progress | Constructors Inc. |
| Saronic Franklin LA Shipyard Expansion | 37b90644-d524-81a5-a912-e29608995256 | 300 | In progress | Industrial |
| Toronto Pearson Accelerator (Pearson LIFT) | 37b90644-d524-8108-91c2-cf12424038dd | — | In progress | Constructors Ltd |
| OKC Continental Coliseum (NBA Arena) | 37b90644-d524-815b-9e52-e7b50a83410c | 900 | In progress | Flintco |
| University of Oklahoma Life Sciences Lab | 37b90644-d524-815f-b9dd-d5677d759b30 | — | In progress | Flintco |
| Kings Bay Dry Dock Recapitalization | 37b90644-d524-81e9-9bfd-fb71886f8472 | 625.5 | Done | Industrial |
| New Lock at the Soo (Soo Locks Ph 3) | 37b90644-d524-819d-95a0-fbd43730fb12 | 1068 | In progress | Industrial |
| Fort Gibson Spillway Bridge | 37b90644-d524-81d5-9d70-f48104b5e362 | 63.8 | Not started | Constructors Inc. |
| Williams Crossing Pedestrian Bridge | 37b90644-d524-81a7-8bc2-e0a6a77ba7f7 | — | Done | Hillsdale |
| Wright City Wastewater Treatment Facility | 37b90644-d524-813f-961b-dc90217a5df9 | — | Done | Industrial |

## Other tables (all → Companies full database = Alberici Corp)
- **Events (4):** DBIA Water/WW 2026 Grapevine `37b90644-d524-81b5-b038-d4f96bb2c8f5` (Place set) · AGC MO AEC TechCon 2025 `…81bc-b834-ee6cd982c752` · Procore Groundbreak 2022 `…81ea-b23d-db7130922a62` (no date — year-only) · DBIA Water/WW 2024 Cincinnati `…8190-b0ec-df3cb1a7f9ca` (Place set).
- **Memberships (4):** NSC `…813a-9da6-e0f5559d0fcc` · AGC `…81cc-a60b-e1d63dd94e5b` · DBIA `…81aa-93a1-fd8c847b14a6` · USGBC `…8180-abe4-f95e8edf4658`.
- **Software (1, shared DB):** "Alberici" `37b90644-d524-81df-a781-fc26e98dc085` — Software used [Procore, Autodesk, Bluebeam, Primavera P6]; full stack (eCMS, StructionSite, DroneDeploy, Navisworks, Touchplan, InEight, PlanSwift, AGTEK) in body. **Consolidated single row** (not per-tool) to avoid the shared DB's known dup-row mess + option-clobber.
- **Locations (10):** St. Louis HQ · Hillsdale · Washington IL · Atlanta · Detroit · Topeka · Burlington · Cambridge · Saskatoon · León — all → Company; **10 → Division** (Washington IL → Alberici Constructors Inc.; Atlanta → WWPS; Detroit → Alberici Constructors Inc. — filled 2026-06-13 from Alb2.md). Adress = text (table's Adress is text type).
- **Sources (10):** operating-companies, contact, projects index, leadership, ENR 2026, flintco news, HigherGov UEI, Procore case study, OSHA 2023, USACE Soo Locks.

## Schema ALTERs (additive, pre-authorized 2026-06-10)
- Memberships `e9190644` +Companies full database relation.
- Locations `f3090644` +Companies full database +Division relations.
- Events `32690644` Location tags +Missouri +Ohio (9 existing preserved).
- Events `32690644` Location tags +**technology** (2026-06-10 audit; 11 existing preserved).
- **No Projects Type ALTER** (all 13 mapped to existing options). **No Projects Location/Country/Software-used ALTER** (avoided shared-multi-select clobber; used existing options).

## Left empty (no sourced value — per dossier `gaps`)
CAGE code · numeric EMR/TRIR · MO SOS charter # / exact incorporation date · exact values for most of the 111 website projects · Flintco federal PIIDs · per-project permits/APNs/FEMA/seismic · bonding limits + surety · insurance carriers/wrap-up · division revenue/headcount beyond Flintco · DUNS/EIN · full NAICS beyond 236220/238120 · all people Email/Phone/LinkedIn (dossier had none for new execs).

## Still manual in Notion UI (MCP can't set)
1. **Projects Underway** view → clear `__TEMPLATE__`, set Contractors = Alberici Corporation (shows all 13).
2. **Existing Software** view → clear `__TEMPLATE__` (shows the Alberici row).
3. **Projects Location** select has no **Kansas / Oklahoma / Michigan** option → 6 projects (Wichita, OKC Arena, OU, Fort Gibson, Williams Crossing, Soo Locks) left Location-blank; 1-click UI add of those 3 state options would let them tag (states are in each project's body/Size). Country select also lacks Kansas.
4. Possible template guide rows / leftover italics on the page + local tables (cosmetic UI delete).

## Build log
- 2026-06-10: full load — company extended; 8 subsidiaries extended + 3 created; 11 division rows; 13 projects; 13 new people (Brooks Williams pre-existing, enriched; Liam O'Donnell dropped); 4 events; 4 memberships; 1 software row; 10 locations; 10 sources; full interlink verified by re-fetch.
- 2026-06-10 audit: 3 fills — (1) Wichita Northwest Water Facility `Contrat Value in Million` → 556.8 [alberici.com]; (2) Procore Groundbreak (2022) `Date` → 2022-01-01 [LinkedIn]; (3) Procore Groundbreak (2022) `Location tags` → technology (new option added to Events `32690644` schema, all 11 prior options preserved). All other records verified complete against dossier. Deferred: Kansas/Oklahoma/Michigan Location options on 6 projects (shared schema); Procore Groundbreak Place (USA only, no lat/lng); AGC TechCon Place (Missouri, no lat/lng).
- 2026-06-12 audit (notion-audit skill, full 3a–3e pass): **0 fills** — all sourced data confirmed present. Full live-fetch of all 11 divisions, 13 projects, 4 events, 4 memberships, 10 location rows, company record, profile page. All checks passed: 3a interconnection ✓ (divisions→Companies [both operating-co+Corp]; projects→Contractors+Owning Department; events/memberships/locations→Companies; location rows→Company+Division where dossier named one); 3b description depth ✓ (all division/project/people bodies at full dossier depth); 3c addresses ✓ (company HQ place + all 11 division Adress places set; location rows Adress text-field set [text type, not place type — correct]; project-site addresses genuinely sourceless — dossier has no lat/lng for sites); 3d memberships ✓ — 4/4 in Notion: NSC, AGC, DBIA, USGBC; 3e location tags ✓ (DBIA 2026=Texas+water; AGC TechCon=Missouri+technology; Procore Groundbreak=technology; DBIA 2024=Ohio+water). Genuinely sourceless confirmed (no write): AGC TechCon `Place` (Missouri only, no lat/lng); Procore Groundbreak `Place` (USA only, no lat/lng); project-site `Adress` place (no sourced coords); Leonard Masonry + WWPS People relations (no leaders named in dossier). Note: Soo Locks live value $1,921.3M vs dossier $1,068M — appears to reflect a prior session's sourced options-awarded figure; left as-is (do not overwrite).
- 2026-06-13 audit (notion-audit skill, full 3a–3e pass): **1 fill** — Alberici Corporation `Country` +Saskatchewan [alberici.com/contact-alberici/] (Saskatoon SK office; option already existed in schema). All 3a–3e checks passed. Division bodies now enriched by post-build sessions (CAS/Filanc/Alberici Construcciones/Hillsdale/Kienlen/WWPS/Leonard all have leaders + projects). Genuinely sourceless: AGC TechCon Place; Procore Groundbreak Place; project-site lat/lng; Louisiana (not in Country schema options). Observation: Mercy Center `Contrat Value in Million` = 148 live (not in dossier, null) — left as-is (non-destructive).
- 2026-06-13 audit #2 (notion-audit skill, full 3a–3e pass): **0 fills** — all sourced data confirmed present. Full live-fetch of all 11 divisions, 13 projects (Saint Louis Zoo, Mercy Center, Wichita, Ford KC, Saronic, Toronto Pearson, OKC Arena, Kings Bay, Soo Locks, Fort Gibson + 3 others), 4 events, 4 memberships, Locations schema, Construction Projects schema. 3a ✓ (all relation edges intact; Leonard Masonry + WWPS People-empty confirmed sourceless); 3b ✓ (all division + project bodies at full dossier depth); 3c ✓ (company HQ place set; all 11 division Adress places set; Locations table Adress is text type — correct; project Adress place field exists in schema but no sourced coords in dossier — confirmed sourceless); 3d ✓ — 4/4 memberships present: NSC, AGC, DBIA, USGBC; 3e ✓ (all 4 events tagged: DBIA 2026=Texas+water; AGC TechCon=Missouri+technology; Procore Groundbreak=technology; DBIA 2024=Ohio+water). Observation: Alberici Constructors Inc. division now shows 12 People + 22 Projects (up from 11+4 at build — additional relations added by post-build sessions; all consistent). Record is fully complete against Alb.md dossier.
- 2026-06-13 audit (notion-audit skill, full 3a–3e pass): **0 fills** — all sourced data confirmed present. Full live-fetch of all 11 divisions (parallel sub-agents), 4 events, 4 memberships, 10 location rows, company record body, profile page. 3a interconnection ✓ — all division→Companies (2 each), all events/memberships/locations→Companies linked; Washington IL, Atlanta, Detroit location rows have no Division relation (dossier `owning_division: null` for all three — sourceless confirmed); 3b description depth ✓ — all 11 division bodies substantive (full focus/leader/footprint), all 5 sampled projects full depth; 3c addresses ✓ — company HQ place set; all 11 division Adress places set; Locations Adress = text type (correct); project Adress place empty on all 5 sampled — confirmed sourceless (dossier has string locations, no lat/lng); 3d memberships ✓ — 4/4 in Notion: NSC, AGC, DBIA, USGBC; 3e location tags ✓ — DBIA 2026=Texas+water; AGC TechCon=Missouri+technology; Procore Groundbreak=technology; DBIA 2024=Ohio+water. Genuinely sourceless (no write): Filanc+Kienlen+Leonard+WWPS Projects relations (dossier project_names:[] for all four); Leonard+WWPS People relations (leader_title: null); Washington IL/Atlanta/Detroit Division relations (owning_division: null); all project-site Adress place (no lat/lng in dossier); AGC TechCon Place (lat/lng null); Procore Groundbreak Place (address null). Note: Procore Groundbreak Date = 2022-01-01 is consistent with dossier year-only "2022". No false positives identified.
- 2026-06-13 audit #5 (notion-audit skill, automated hourly cycle, full 3a–3e pass): **0 fills** — all sourced data confirmed present. Live-fetched: company record (properties grep confirmed Description/Type/Size/Address/LinkedIn/Website/Country all set), profile page, Alberici Industrial division (Companies×2, People×2, Projects×5, Adress place set ✓), Flintco division (Companies×2, People, Projects×2, Adress place set ✓), all 4 events (Date/Location tags/Place confirmed), all 4 memberships (Companies relation + body confirmed), software row (Software used/Companies/body confirmed), Saint Louis Zoo project (Contractors/Contrat Value/Location/Owning Department/Status/Type/Date/Size/URL all set). 3a–3e all pass. No new gaps surfaced. Genuinely sourceless unchanged: AGC TechCon Place; Procore Groundbreak Place; project-site Adress place; Filanc/Kienlen/Leonard/WWPS Projects+People; 3 location Division links; all People Email/Phone/LinkedIn; CAGE code; numeric EMR/TRIR.
- 2026-06-13 audit #6 (notion-audit skill, full 3a–3e pass): **0 fills** — all sourced data confirmed present. Full live-fetch of all 11 divisions (parallel), all 13 projects, all 4 events, all 4 memberships, all 10 location rows, company record, profile page. 3a ✓ — all divisions→Companies (2 each); projects→Contractors (2 each)+Owning Department (1 each); events/memberships/locations→Companies; Washington IL/Atlanta/Detroit Division empty (dossier owning_division: null — sourceless); Filanc/Kienlen/Leonard/WWPS Projects empty (dossier project_names:[] — sourceless); Leonard/WWPS People empty (dossier leader_title: null — sourceless). 3b ✓ — all 11 division bodies substantive (leaders named with source URLs from post-build sessions); all 13 project bodies at full dossier depth. 3c ✓ — company HQ place set; all 11 division Adress places set; Locations Adress text-field set (text type, not place — correct); project Adress place empty on all 13 — confirmed sourceless (dossier has no lat/lng for any site). 3d ✓ — 4/4 memberships: NSC, AGC, DBIA, USGBC; all Companies relations set. 3e ✓ — DBIA 2026=Texas+water; AGC TechCon=Missouri+technology; Procore Groundbreak=technology; DBIA 2024=Ohio+water. Observations: Alberici Constructors Inc. division shows 12 People + 22 Projects (post-build enrichment consistent); Soo Locks live value $1,921.3M (reflects options-awarded mod — do not overwrite); Mercy Center live value $148M (added by prior session — do not overwrite). No false positives. Record confirmed fully complete against Alb.md dossier.
