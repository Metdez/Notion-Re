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
- **Locations (10):** St. Louis HQ · Hillsdale · Washington IL · Atlanta · Detroit · Topeka · Burlington · Cambridge · Saskatoon · León — all → Company; 7 → Division (Washington/Atlanta/Detroit have no dossier owning_division → Company only). Adress = text (table's Adress is text type).
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
3. ~~**Projects Location** select has no **Kansas / Oklahoma / Michigan** option~~ — **RESOLVED (2026-06-11 audit):** Kansas, Oklahoma, Michigan options are now present in the Construction Projects Location schema; all 6 projects are correctly tagged. Stale "(Location tag omitted)" body notes cleaned up.
4. Possible template guide rows / leftover italics on the page + local tables (cosmetic UI delete).
5. **⚠ Duplicate membership rows to delete in UI (6 rows — Alb2 load created dups; keep the richer row in each pair):**
   - USGBC dup `37d90644-d524-8175-a9b1-f4436f8588e1` → keep original `37b90644-d524-8180-abe4-f95e8edf4658`
   - DBIA dup `37d90644-d524-81ef-85eb-c33d9d7c3280` → keep original `37b90644-d524-81aa-93a1-fd8c847b14a6`
   - AGC of America dup `37d90644-d524-8171-bb61-e67895741afc` → keep original `37b90644-d524-81cc-a60b-e1d63dd94e5b`
   - LCI dup `37d90644-d524-8136-99a2-f64665a84a64` → keep `37d90644-d524-810e-9e33-d144c723c39d` (richer body)
   - WCDA dup `37d90644-d524-813f-b2b1-e8476cbd7592` → keep `37d90644-d524-8157-aa36-d582a9f26308` (richer body)
   - CIRT dup `37d90644-d524-8127-94c1-f3ea21a77986` → keep `37d90644-d524-8195-9b4b-fc9ed85db08b` (has "Member since 2016" in name)

## Build log
- 2026-06-10: full load — company extended; 8 subsidiaries extended + 3 created; 11 division rows; 13 projects; 13 new people (Brooks Williams pre-existing, enriched; Liam O'Donnell dropped); 4 events; 4 memberships; 1 software row; 10 locations; 10 sources; full interlink verified by re-fetch.
- 2026-06-10 audit: 3 fills — (1) Wichita Northwest Water Facility `Contrat Value in Million` → 556.8 [alberici.com]; (2) Procore Groundbreak (2022) `Date` → 2022-01-01 [LinkedIn]; (3) Procore Groundbreak (2022) `Location tags` → technology (new option added to Events `32690644` schema, all 11 prior options preserved). All other records verified complete against dossier. Deferred: Kansas/Oklahoma/Michigan Location options on 6 projects (shared schema); Procore Groundbreak Place (USA only, no lat/lng); AGC TechCon Place (Missouri, no lat/lng).
- 2026-06-11 audit: 6 stale body-note cleanups — removed "(Location tag omitted — X not yet an option)" notes from Fort Gibson, Williams Crossing, OU Life Sciences, Wichita NW Water, Soo Locks, and OKC Coliseum bodies (tags ARE set; notes were from prior build pass). Schema confirmed: Kansas/Oklahoma/Michigan now exist as Location select options. All 13 projects, 4 events, 4 memberships, 11 division rows, company record verified complete vs dossier. Zero fillable gaps found. Persistent genuinely sourceless blanks unchanged (CAGE code, EMR/TRIR, etc.). AGC TechCon + Procore Groundbreak Place remain deferred (no lat/lng in dossier).
- 2026-06-11 audit (2nd pass): 1 fill — Kienlen Constructors division row `37b90644-d524-816b-86b3-cf328162ece6` `Adress` place → St. Louis, MO / 8800 Page Ave (38.7028,-90.3673) [alberici.com/contact-alberici/]. Full graph re-verified: 13 projects (all Contractors+Owning Dept+Location+body ✅), 11 division rows (all Companies+People+Projects+Adress place where sourced ✅), 4 events (all Date+Location tags+Place where lat/lng known ✅), 4 memberships (all Company-linked ✅), 10 locations (all Adress text ✅), company record (Address place+Country+People+Projects+body ✅). Genuinely sourceless with no lat/lng: Filanc/Leonard Masonry/WWPS division Adress (no coords in dossier); Procore Groundbreak + AGC TechCon Place (US/MO, no lat/lng). Zero other fillable gaps.
- 2026-06-11 audit (3rd pass): 0 fills. Full re-fetch of all 11 division rows, 13 projects, 4 events, 4 memberships, company record — every record verified against dossier. No new fillable gaps discovered. Confirmed still genuinely sourceless: Filanc/Leonard Masonry/WWPS Adress (no lat/lng in dossier); Procore Groundbreak + AGC TechCon Place (no lat/lng); Flintco/CAS/Alberici Construcciones People relations (no named division leaders in dossier). Workspace fully complete against Alb.md.
- 2026-06-11 audit (4th pass): 0 fills. Complete re-fetch of all 11 division rows, 13 projects, 4 events, 4 memberships, company record, and profile page. All checks 3a–3e passed: relations intact, body depth confirmed, addresses in place fields, 4/4 memberships present, all event location tags set. Zero fillable gaps. Genuinely sourceless fields unchanged (CAGE code, EMR/TRIR, Filanc/Leonard/WWPS Adress, AGC TechCon + Procore Groundbreak Place). Workspace fully complete against Alb.md.
- 2026-06-11 audit (5th pass): 0 fills. Full re-fetch of all 11 division rows (including Filanc, WWPS, Leonard Masonry, Kienlen, Hillsdale, Alberici Construcciones, CAS, Flintco, Alberici Industrial, Alberici Constructors Ltd., Alberici Constructors Inc.), 13 projects (all Contractors+Owning Dept+Location+body ✅), 4 events (all Date+Location tags+Place ✅; "water" tag option confirmed present in Events schema and applied to both DBIA events), 4 memberships (all Company-linked+body sourced ✅), company record (Address+Country+People+Projects+body ✅). All checks 3a–3e passed. Zero fillable gaps. Genuinely sourceless unchanged: Filanc/Leonard Masonry/WWPS division Adress (null lat/lng in Alb.md); Procore Groundbreak + AGC TechCon Place (no lat/lng in dossier); per-project contract values for 0 of 13 sourced projects missing. Workspace fully complete against Alb.md.
- 2026-06-12: **Alb2.md registered as 2nd dossier** (612KB, run_date 2026-06-12; 49 projects, 13 divisions, 22 locations, 94 sources). Alb2.md load appears to have already been run in a prior (same-session) operation — company record now shows 51 projects + 36 people; 2 new subsidiaries (AWCL `37d90644…8298`, LCG Capital `37d90644…8197`); Jose Garcia-Aranda (President ACI) + 8 more people added. **Membership dup alert:** Alb2.md load created duplicate rows for USGBC, DBIA, AGC, LCI (×2), WCDA (×2), CIRT (×2) — all linked to Alberici Corp. ⚠ Zack to delete the following dups in UI: USGBC `37d90644…8175` (keep original `37b90644…8180`), DBIA `37d90644…81ef` (keep original `37b90644…81aa`), AGC of America `37d90644…8171` (consolidate into original `37b90644…81cc`), LCI `37d90644…8136` (keep `37d90644…810e`), WCDA `37d90644…813f` (keep `37d90644…8157`), CIRT `37d90644…8127` (keep `37d90644…8195`).
- 2026-06-12 audit: 1 fill — **ABC membership row** `37d90644-d524-81b8-b8cd-c7bdad664e22` created in Memberships table [Flintco 3× ABC Safety Pinnacle 2023/2024/2025; flintco.com/history-timeline/]. Memberships now: NSC · AGC · DBIA · USGBC · LCI · WCDA · CIRT · AGCMO · ABC + 6 dup rows flagged for UI deletion. Events expanded to 13 (4 original + 9 net-new from Alb2.md: LCI Congress 2025, DBIA Design-Build 2026, AGC Annual Convention 2026, DBIA WW 2027, AGCMO Keystone 2023/2024/2025, WCDA 20th). No other fillable gaps vs Alb2.md. Genuinely sourceless: CAGE/UEI, EMR/TRIR, Filanc/Leonard/WWPS Adress (no lat/lng), Procore Groundbreak + AGC TechCon Place (no lat/lng).
- 2026-06-12 audit (2nd pass — full re-audit vs Alb.md + Alb2.md): **3 fills** — (1) Hillsdale Fabricators division body `37b90644-d524-8151-9b8e-f3c6ffd122aa` → added Leader: Jeanine Engle, SVP & Market Leader [hillsdalefabricators.com/about-us/] + Founded: 1958; (2) Alberici Construcciones S.A. de C.V. division body `37b90644-d524-81e6-a5f8-d53e36c44f7f` → added Leader: Oscar Moctezuma, VP & Market Leader – Mexico [alberici.com/es/…]; (3) Flintco division `Adress` place property `37b90644-d524-81a5-94b2-ef4428dacf94` → corrected from OKC address to Tulsa HQ: 320 South Boston Ave, Suite 300, Tulsa, OK 74103 (36.154, -95.993) [flintco.com/about/]. Full graph verified: 11 division rows, 51+ projects, 13 events, 15 membership rows (9 unique + 6 dup rows pending UI deletion), company record — all complete vs both dossiers. Genuinely sourceless unchanged: CAGE code, EMR/TRIR, Filanc/Leonard Masonry/WWPS Adress (null lat/lng in both dossiers), Procore Groundbreak + AGC TechCon Place (no lat/lng).
