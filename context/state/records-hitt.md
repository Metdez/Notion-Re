# State · Records — HITT Contracting

> **Holds:** the HITT Contracting dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a HITT record.
> **Ground truth:** `Enlaye Notion/HITT/HITT1.md` (HITT2.md is empty/0 bytes). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.

---

## Profile page (hub)
**"HITT Contracting"** (renamed from "HITT TEMPLATE (2)") — https://app.notion.com/p/37b90644d5248060a129c5276585311d (Companies research → Zack Folder). Template variant uses a **Divisions** DB (not "Company Map"). Bio snapshot at top; Attack Plan filled at bottom.

Page-local data sources on this page:
- **Divisions** `collection://dad90644-d524-83ae-9461-07a0fe7efb71` (props: Division title · Adress place · relations Companies/People/Projects)
- Events `collection://71890644-d524-83cb-9d95-8710f43267d0` · Sources `collection://0f590644-d524-822c-b011-87293ae564a2` · Locations `collection://11290644-d524-8326-a2f8-87080d4963b2` · Memberships `collection://79490644-d524-8374-a000-072dfd21946e`
- Projects Underway = shared Construction Projects (linked view, filtered `__TEMPLATE__` — **manual UI filter fix needed**)
- Existing Software = shared Companies Software (linked view, filtered `__TEMPLATE__` — **manual UI filter fix needed**)

**Additive schema changes (pre-authorized 2026-06-10):** added relation `Companies full database` to Memberships DB; added `Companies full database` + `Division` relations to Locations DB — to complete the interlink.

## Company record (EXISTING — updated, not created)
**"HITT"** `30a90644-d524-80ef-a7d5-f533e2296b88` in Companies DB. Pre-existed (Feb 2026) with Website/LinkedIn/Description/BW=Builder/Country=USA/Type=Company + 6 people.
- Added: Address (place) 2900 Fairview Park Dr, Falls Church VA (38.864,-77.196); Country += Virginia/Texas/California/Florida/Georgia/Arizona/New York/Washington; Construction Projects (10); Companies Software (6). People auto-grew to **20** via dual relation.
- ⚠ **Size = "Regional" kept** — dossier says "Mutlinational". Conflict preserved per additive rule.
- Title left as "HITT" (not renamed to "HITT Contracting") — additive/non-destructive.

## Divisions (18 — Divisions DB `dad90644`)
Each carries Adress (place) + Companies(HITT) + People + Projects.
| Division | ID | People | Projects |
|---|---|---|---|
| Washington, DC (HQ) | 37b90644-d524-813f-bc72-c0cdf3e31fed | Roy, Antonides, Mucci, Ross, Landefeld, Sorensen, Arias | NASA HQ, One Preserve, Omni, HITT HQ, N2W |
| Phoenix | 37b90644-d524-81a1-a901-d9dfffb5bdab | Kindle | — |
| Los Angeles | 37b90644-d524-8119-8463-d36103934558 | — | — |
| San Francisco | 37b90644-d524-81b5-a1c9-f7d83726055c | — | — |
| Santa Clara | 37b90644-d524-81b7-b6db-d354d64c4325 | — | — |
| Fort Lauderdale | 37b90644-d524-8151-a042-e53025a665cb | — | Andaz Miami Beach |
| Atlanta | 37b90644-d524-81d4-aacf-c3b65fecab69 | — | — |
| Albuquerque | 37b90644-d524-81f7-b574-dadd63604e5c | Kindle | — |
| New York | 37b90644-d524-8185-b569-ee1824e261b2 | Grebenstein, Simone | — |
| Raleigh | 37b90644-d524-81c3-bec2-d6534fca6ad3 | — | — |
| Charleston | 37b90644-d524-815c-b012-f0b9a06e7dda | — | Boeing SC 787 |
| Austin | 37b90644-d524-810f-87d1-cdbe43fa06bb | Macks | — |
| Dallas | 37b90644-d524-81eb-86b8-fe4aee0366d3 | Baughman | — |
| Houston | 37b90644-d524-8105-8f3d-e893dca323ee | — | NASA JSC MACC |
| Richmond | 37b90644-d524-8135-b4e7-ce6083208dba | — | HCA Chippenham |
| Seattle | 37b90644-d524-8144-a065-d552a0216f4a | Wagner | — |
| Brycon Corp. (subsidiary) | 37b90644-d524-81bf-b20f-d03320a3d477 | — | — |
| Central Consulting (sub → NY) | 37b90644-d524-81c6-8cf4-c75d6def9ab3 | Simone | — |

## People (14 created; Fernando Arias pre-existed)
All linked Company → HITT (`30a9…`). Pre-existing & kept: Fernando Arias `31190644…c3d7`, Reilly John, Allan Chan, Alex Seleznyov, Jack Craig, Brendan Hynes.
| Person | ID | Role | Division |
|---|---|---|---|
| Kim Roy | 37b90644-d524-814a-824f-fdf96bea7a22 | CEO | DC HQ |
| Evan Antonides | 37b90644-d524-8136-be34-e3b3b2cdc96b | Co-President | DC HQ |
| Drew Mucci | 37b90644-d524-81e8-99f5-ff7ad66514b4 | Co-President | DC HQ |
| P.J. Ross | 37b90644-d524-819f-bb89-ffdc154e7471 | CFO | DC HQ |
| Pamela Baughman | 37b90644-d524-8183-a76c-ce3f65c1ee0d | VP Health & Safety | Dallas |
| Andre Grebenstein | 37b90644-d524-81c4-9919-f500f3b22983 | VP & NY Office Leader | New York |
| Thomas Kindle | 37b90644-d524-81dd-8bc8-db25500bd3ef | VP (ABQ + Phoenix) | Phoenix, Albuquerque |
| Jennifer Macks | 37b90644-d524-8144-b686-e5fe66a3f268 | VP Austin (DBIA award) | Austin |
| Ryan Wagner | 37b90644-d524-8123-adf2-fc1f501d752b | VP Pacific Northwest | Seattle |
| Aaron Martens | 37b90644-d524-815d-81df-db378315f074 | VP Mission Critical | (company-level) |
| Peter Lanfranchi | 37b90644-d524-81f8-8d9f-ceeb55cd7b3e | SVP Hospitality | (company-level) |
| Richard Simone | 37b90644-d524-81ca-86d3-dd54909d903a | VP (Central founder) | New York, Central |
| Jim Landefeld | 37b90644-d524-810c-afe6-f50553cb7731 | SVP Operations Technology | DC HQ |
| Karl Sorensen | 37b90644-d524-81fe-abd4-dc63926452bb | Director, Project Solutions | DC HQ |

## Projects (10 — Construction Projects DB; Contractors → HITT)
JMACC `…81b8befa…` · Next NGA West `…8110a40a…` · Boeing SC 787 `…81899867…` · Andaz Miami Beach `…81bb8ab9…` · One Preserve Labs `…81f383db…` · Omni Homestead `…814894c1…` · QTS Data Centers `…81099135…` · NASA HQ `…815ab210…` · HITT New HQ `…81158d66…` · HCA Chippenham `…81bab3f1…`. QTS left company-level (multi-state, no single office).

## Other tables
- **Locations (16):** office addresses, each linked Company + Division (`11290644`).
- **Memberships (7):** AGC · NAIOP · USGBC · CoreNet Global · IFMA · IIDA · DBIA — each linked Company (`79490644`).
- **Software (6):** Procore · Bluebeam · Autodesk/BIM · OpenSpace · Hilti Jaibot · Microsoft 365 — each linked Company (`37690644` shared).
- **Events (5):** DBIA 2025 · CONEXPO 2026 · NAIOP NoVA Awards · Construction Safety Week · Subcontractor Appreciation Day — each linked Company (`71890644`).
- **Sources (10):** firmographics, ENR, NASA JSC, N2W, Boeing, Brycon, Central, Procore, Federal IDs, new HQ (`0f590644`).

## Left empty (no sourced value in dossier — per gaps list)
DUNS, VA SCC entity ID, state of incorporation; numeric EMR/TRIR; OSHA citation/penalty $; bonding/surety; division-level revenue/headcount; acquisition prices; most LinkedIn URLs for new leaders; per-project parcel/permit data.

## Post-load audit (2026-06-10, 2 parallel /notion-audit agents)
- **Fills (2):** Software "Hilti Jaibot" row → `Software used` option added + set; Fernando Arias (`31190644…c3d7`) → Function Qualification [Sustainability, Director] + sourced `## Role` body.
- **Schema-option gaps (left as-is, optional UI add):** Projects `Location` has no "Florida" → Andaz Location blank (city in body); People `Location` has no "New Mexico" → Thomas Kindle = Arizona only.
- Everything else verified correct; full interlink graph intact.

## Post-load audit #2 (2026-06-10, user-invoked orchestration prompt → /notion-audit)
4 parallel read-only agents (divisions / people / projects / side-tables) vs HITT1.md. HITT2.md + HITT3.md confirmed 0 bytes — nothing new to load → pure Audit Mode.
- **Verified clean (0 gaps):** 18 divisions (Adress place + Companies + People/Projects all set), 16 locations, 7 memberships, 6 software, 14 people (Company + sourced bios; "Division MISSING" is a People-DB schema fact, not a gap — people→division lives on division rows' People relation).
- **4 fills (all verified live):** Andaz Miami Beach `…81bb8ab9` Location=**Florida**; Boeing SC 787 `…81899867` Location=**South Carolina**; CONEXPO 2026 event `…81b7a53c` Location tags=**Nevada, Las Vegas**; NAIOP NoVA Awards event `…815db36f` Location tags=**Virginia**. (Resolves the prior audit's "Florida option" gap.)
- **Schema (additive):** Projects `Location` +Florida +South Carolina; Events `Location tags` +Virginia.
- ⚠ **Incident + recovery (no data lost):** first `ALTER COLUMN … SET` used only the *new* options → it **REPLACED** the shared option lists (Projects Location ~115 opts, Events tags 11 opts dropped). Immediately restored the full original lists by exact name; Notion re-bound all page values by name → spot-checked NASA JSC MACC=Texas, Omni=Virginia, DBIA=Nevada/Las Vegas, CONEXPO intact. **Lesson:** [notion-mcp.md §9](../playbook/notion-mcp.md) line 10 already warns to pass the FULL existing option list — read it before any `ALTER … SET` on a shared multi-select.
- **Left empty-for-cause (schema/sourceless):** project `Owning Department` + `Adress` place unused by DB convention (division in body + division-row Projects relation); project values rounded (N2W 712 vs 711.7, NASA HQ 68 vs 67.7 — not empty, additive rule); HCA Chippenham body thin (dossier itself thin); NAIOP/Subcontractor-Day event dates null in dossier.

## Post-load audit #3 (2026-06-10, /notion-audit solo agent vs HITT1 + HITT2 + HITT3)
HITT2.md (JSON) and HITT3.md (JSON) now contain content (not 0 bytes as previously reported — prior agents had truncation).
- **Fills (2):**
  1. Company record `30a90644` → `Country` += **Missouri** (N2W/St. Louis) + **Maryland** (One Preserve Rockville). Sources: [HITT](https://www.hitt.com/news-hub/mccarthy-hitt-celebrate-next-nga-west-completion/) / [HITT](https://www.hitt.com/projects/one-preserve-labs-spec-suites/)
  2. Company record `30a90644` body `# Description` section → filled with firmographic facts: Legal name, DUNS 003258746, State of Incorporation VA, UEI/CAGE, NAICS, Founded 1937/family-owned, Revenue history. Sources: [cage.report](https://cage.report/SAM/0TDS4) / [HigherGov](https://www.highergov.com/awardee/hitt-contracting-inc-10006941/)
- **Verified correct (no change needed):** 5 events (DBIA Nevada/Las Vegas ✓, CONEXPO Nevada/Las Vegas ✓, NAIOP Virginia ✓, Safety Week no location tag needed, Subcontractor Day no location tag needed); 18 divisions (all Adress + Companies + People/Projects set); 7 memberships; 6 software; 20 people (Company + bios); 10 projects (Location/Type/Status/Value/Date set).
- **Left empty-for-cause (sourceless or blocked):** Construction Safety Week / Subcontractor Appreciation Day — no specific location tags (dossier says "National" / "offices nationwide"); Size "Regional" remains (conflict with dossier "Mutlinational" — non-destructive rule prohibits overwrite of set value).
- **DEFERRED (shared schema):** Country options `North Carolina`, `New Mexico`, `South Carolina` not in Companies DB Country schema — cannot add options without risk to shared data. UI add needed.
- **False positives rejected:** Addresses on divisions already populated from HITT1 load — HITT3 has some updated addresses (e.g., Dallas = Frisco TX, Houston = 9300 Bamboo Rd, LA = Culver City) but fields already filled → additive rule prevents overwrite. Verified Adress (place) values set on all 18 divisions.

## Post-load audit #4 (2026-06-11, automated hourly cycle → /notion-audit)
Parallel read-only audit: events, memberships, divisions (sample), locations, people (Aaron Martens, Peter Lanfranchi), projects (NASA JSC MACC).
- **Fills (4):**
  1. DBIA 2025 event `37b90644…81a2aeed` → `Adress` (place) = MGM Grand Las Vegas, 3799 S Las Vegas Blvd, NV 89109 (36.102, -115.169). Source: [HITT](https://www.hitt.com/leadership/jennifer-macks/)
  2. DBIA 2025 event → `Date` end = **2025-11-07** (was start-only). Source: [HITT](https://www.hitt.com/leadership/jennifer-macks/)
  3. CONEXPO 2026 event `37b90644…81b7a53c` → `Adress` (place) = Las Vegas Convention Center, 3150 Paradise Rd, NV 89109 (36.13, -115.152). Source: [ZoomInfo](https://www.zoominfo.com/c/hitt-contracting-inc/17842496)
  4. CONEXPO 2026 event → `Date` end = **2026-03-07** (was start-only). Source: [ZoomInfo](https://www.zoominfo.com/c/hitt-contracting-inc/17842496)
- **Verified correct (no change needed):** 7 memberships (all linked to HITT); 16 locations (all addresses + company + division linked); 18 divisions (Adress place + Companies + People/Projects set); all sampled projects filled; Aaron Martens + Peter Lanfranchi company-level people records intact.
- **Left empty-for-cause (sourceless):** Construction Safety Week + Subcontractor Appreciation Day — no Adress, no Location tags, no end date (dossier: "National"/"offices nationwide"); NAIOP NoVA Awards — no date (dossier null).
- **False positives rejected:** Division People/Projects empty for LA/SF/Santa Clara/Raleigh/Brycon = correct (no named contacts or projects in dossier for those offices).

## Post-load audit #5 (2026-06-11, /notion-audit HITT Contracting)
Full read-only pass vs HITT1.md on profile hub, company record, 18 divisions, 16 locations, 7 memberships, 5 events, 10 projects, 14 named people.
- **Fills (2):**
  1. HITT New Headquarters project `37b90644-d524-8115-8d66-c69befca1c22` → `Adress` (place) = 7125 West Falls Station Blvd, Falls Church, VA 22043 (38.864, -77.196). Source: [HITT](https://www.hitt.com/news-hub/hitt-contracting-unveils-new-hq/)
  2. Andaz Miami Beach project `37b90644-d524-81bb-8ab9-fd6332569690` → `Date` start = 2025-01-01 (year of completion; no specific date in dossier). Source: [HITT](https://www.hitt.com/projects/andaz-miami-beach/)
- **Verified clean (no write needed):** 5 events (DBIA/CONEXPO: Adress+Date+Location tags ✓; NAIOP: Location tags ✓; Safety Week/SubDay: sourceless OK); 7 memberships all Company-linked ✓; 18 divisions all Adress+Companies+People/Projects ✓; 16 locations all Adress(text)+Company+Division ✓; 10 projects all Contractors+Location+Type+Status ✓; 14 people all Company+Function+bio ✓.
- **Left empty-for-cause:** 9 project `Adress` place fields (dossier city/state only, no street; place requires lat/lng, no-geocoding rule); Locations DB `Adress` = text type not place (schema — converting = destructive); Size=Regional conflict preserved; people LinkedIn/Email/Phone (none in dossier); NAIOP Adress (source: "Northern Virginia"); Safety Week/SubDay Adress/date (National = sourceless).

## Post-load audit #6 (2026-06-11, /notion-audit HITT Contracting — description-depth 3b)
Full pass vs HITT1.md + HITT2.md + HITT3.md. HITT3.md contains richer per-division data (office leaders, founding dates, headcounts, revenue) that had not been loaded in prior passes (Audit #3 only used HITT3 for company-level Country + Description fields, not individual division bodies).
- **Fills (5) — division body enrichments:**
  1. **Atlanta** `37b90644-d524-81d4-aacf-c3b65fecab69` body → added Ryan Bixler (EVP), Erik Kandler (SVP Interiors), Edward Miko (VP Mission Critical); founded 1998; ~180 staff; ~$900M delivered in 5 yrs; 30+ active projects. Source: [hitt.com/locations/atlanta-ga/](https://www.hitt.com/locations/atlanta-ga/)
  2. **Houston** `37b90644-d524-8105-8f3d-e893dca323ee` body → added Paul Zimmerman (VP), Todd Hudson (VP); founded 2016 (Trademark Construction acquisition); ~200 staff. Source: [hitt.com/locations/houston-tx/](https://www.hitt.com/locations/houston-tx/)
  3. **Dallas** `37b90644-d524-81eb-86b4-fe4aee0366d3` body → added Chris Jewell (VP Office Leader), Jon Duffey (SVP); founded 2008; ~200 staff; 75 active projects; noted address relocation to Frisco TX. Source: [hitt.com/locations/dallas-tx/](https://www.hitt.com/locations/dallas-tx/)
  4. **Los Angeles** `37b90644-d524-8119-8463-d36103934558` body → added Trevor Coffey (EVP), Kavan Ranasinghe (VP Office Leader); ~75 staff; noted address relocation to Culver City CA. Source: [hitt.com/locations/los-angeles-ca/](https://www.hitt.com/locations/los-angeles-ca/)
  5. **Raleigh** `37b90644-d524-81c3-bec2-d6534fca6ad3` body → added Sam Holbrook (VP & Office Leader); refined focus description. Source: [hitt.com/leadership/sam-holbrook/](https://www.hitt.com/leadership/sam-holbrook/)
- **Deferred (not audit scope — needs /notion-load):** 10 net-new projects from HITT3.md (JCC Advanced Manufacturing $35M, Leidos HQ Reston VA, MedImmune $40M Gaithersburg MD, Inova Women's/Children's, Inova Fairfax PSB 5th Floor, Inova Perioperative, + others). Additional division leaders not yet in People DB: Brad Hunley (Government EVP), Josh VanScoy (Charleston VP), Rav Dhaliwal (Bay Area VP), Ryan Bixler, Erik Kandler, Edward Miko, Paul Zimmerman, Todd Hudson, Chris Jewell, Jon Duffey, Trevor Coffey, Kavan Ranasinghe, Sam Holbrook.
- **False positives / non-fills:** division address fields already populated → HITT3 updated addresses (Dallas=Frisco TX, LA=Culver City) noted in bodies only, not overwritten (additive rule). 13 other divisions had sufficient bodies already.
- **Verified clean:** 7 memberships ✓, 16 locations ✓, 5 events ✓, 10 projects ✓, 6 software ✓, all 20 people ✓.

## Post-load audit #7 (2026-06-11, /notion-audit HITT Contracting — full verification pass)
Full read-only pass vs HITT1.md + HITT2.md + HITT3.md, covering: company record, 18 divisions, 16 locations, 7 memberships, 5 events, 10 projects, 20 people, 6 software.
- **Fills (0):** Record is fully built after 6 prior audit passes. No empty fields with available sourced data were found.
- **Verified correct (no change needed):**
  - Company record `30a90644`: Description/DUNS 003258746/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance all filled ✓; Country = 14 values including NC/SC/NM ✓; Address place ✓; 10 Construction Projects linked ✓; 6 Software linked ✓; 20 People linked ✓
  - All 5 events: DBIA (Date 2025-11-05→07, Adress MGM Grand, Location=Nevada/Las Vegas ✓), CONEXPO (Date 2026-03-03→07, Adress LVCC, Location=Nevada/Las Vegas ✓), NAIOP (Location=Virginia ✓), Safety Week (Date start only = correct/national), SubDay (no data = correct/nationwide)
  - All 18 divisions: Adress place ✓, Companies relation ✓, body content with leaders/focus/projects ✓ (enriched via Audits #2/#6)
  - All 7 memberships: AGC, NAIOP, USGBC, CoreNet Global, IFMA, IIDA, DBIA — all Company-linked ✓ (3d complete)
  - All 6 software: Procore, Bluebeam, Autodesk/BIM, OpenSpace, Hilti Jaibot, Microsoft 365 ✓
  - All 20 people: Company linked ✓, Function Qualification set ✓, sourced body content ✓
  - Interconnection (3a): All 18 divisions → Companies(HITT) ✓; all people → Company(HITT) ✓; all events/memberships → Companies(HITT) ✓
  - Location tags (3e): DBIA=Nevada/Las Vegas ✓, CONEXPO=Nevada/Las Vegas ✓, NAIOP=Virginia ✓, Safety Week/SubDay = no tag (national/sourceless ✓)
- **Left empty-for-cause (genuinely sourceless):** Safety Week / SubDay — no Adress, no Location tags, no end date (dossier: "National"/"offices nationwide"); NAIOP — no date, no Adress (source: "Northern Virginia" only); Size=Regional conflict preserved (non-destructive rule); people LinkedIn/Email/Phone (none in dossiers).
- **DEFERRED (requires /notion-load, not /notion-audit):**
  - 5-6 net-new projects confirmed absent: JCC Advanced Manufacturing Training Facility ($35M, Four Oaks NC), MedImmune R&D ($40M, Gaithersburg MD), Inova Women's/Children's (Falls Church VA), Inova Fairfax PSB 5th Floor (Falls Church VA), Inova Fairfax Perioperative (Falls Church VA), Leidos HQ (Reston VA, Boston Properties client)
  - Net-new people not yet in People DB: Triloka Shanbhag (Mission Critical co-leader), Jason Hair (NY VP), Brad Hunley (Government EVP), Sven Sahkul/Luke Marshall/J. Fontaine (Government VPs), Kyle Sugrowe (Advanced Manufacturing VP), Scott Decker/Gary Stewart (Life Sciences), Kevin Daniels/Chris Lukawski/JoAnna Heath (Healthcare BU), Brian Kilpatrick (Fort Lauderdale VP), Ryan Bixler/Erik Kandler/Edward Miko (Atlanta), Paul Zimmerman/Todd Hudson (Houston), Chris Jewell/Jon Duffey (Dallas), Trevor Coffey/Kavan Ranasinghe (LA), Sam Holbrook (Raleigh)

## Post-load audit #8 (2026-06-12, /notion-audit HITT Contracting — HITT4.md)
New dossier `HITT4.md` (2026-06-12 run, 38 sources, region_hint=Boston/New England) discovered. Compared against all prior audits and live Notion state.
- **1 new project created:** Microsoft Alviso Datacenter Campus `37d90644-d524-8129-8974-d18123b548c2` (Data Center / Mission Critical, San Jose CA, groundbreaking 2026-06-10, est. completion 2028, 397,205 sf / 48 MW, Microsoft owner, Santa Clara BU). [ConnectCRE](https://www.connectcre.com/stories/microsoft-breaks-ground-on-long-planned-north-san-jose-data-center-site/)
- **1 new membership created:** Associated Builders and Contractors (ABC) `37d90644-d524-81fc-badf-f9207d030b02` → linked to HITT. [HITT](https://www.hitt.com/news-hub/hitt-earns-abc-eagle-award/)
- **3 new people created:** Brett Hitt (Co-Chairman) `37d90644-d524-8142-afe6-f4f32c89044c`; John Kane (SVP Santa Clara/Mission Critical) `37d90644-d524-8168-a299-f6dacd6f2e39`; Megan Lantz (VP R&D) `37d90644-d524-8116-acdc-c23227c4831f`. All linked Company→HITT.
- **5 new software rows created:** Autodesk Navisworks `37d90644-…818f97d8`, Autodesk Revit `37d90644-…815a8c90`, FARO Scene `37d90644-…81eea866`, Synchro (Bentley) `37d90644-…811092e6`, Building Transparency EC3 `37d90644-…81be9531`. Schema extended with 5 new `Software used` options (additive; 34 total options, all prior preserved).
- **Interlinks set:** company `Construction Projects` updated (+Microsoft Alviso); company `Companies Software ` updated (+5 new rows); Santa Clara division `Projects` += Microsoft Alviso; Santa Clara division `People` += John Kane; John Kane `Division` = Santa Clara.
- **Verified no change needed:** Boeing SC body already rich (JV/BRPH/dates/delivery ✓); all prior 7 audits' fills still intact; 7 memberships (now 8 with ABC) ✓; 18 divisions ✓; 20 original people ✓.
- **False positives rejected:** HITT4 division_count=0/divisions=[] (no division detail); locations array populated but addresses already set in Notion (additive rule); hq_address updated to new HQ — current operational address already in place field (additive rule prevents overwrite); employees/revenue: HITT4 shows $8.7B 2024 and 3,300 staff — body already has richer $13.1B 2025 figures.
- **DEFERRED from HITT4 (virtual event, low signal):** DBIA 2025/2026 Webinar — virtual event, optional add.
- **Left empty-for-cause:** all prior sourceless items unchanged (Safety Week/SubDay, NAIOP date/address, Size=Regional conflict, LinkedIn/Email/Phone for people).

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = HITT.
2. **Existing Software** view → clear `__TEMPLATE__` filter.
3. **Memberships-note People view** → re-point hardcoded company filter to HITT.
4. **Company Country** → add options: North Carolina, New Mexico, South Carolina (cannot do via MCP on shared schema).

## Post-load audit #9 (2026-06-12, /notion-audit HITT Contracting — HITT4.md post-#8 gap fill)
Full verification pass vs HITT1.md + HITT2.md + HITT3.md + HITT4.md. Scope: all records created or modified in Audit #8 (Microsoft Alviso project, ABC membership, 3 people, 5 software) + full 3c/3d/3e sweep.
- **Fills (2 — both on Microsoft Alviso Datacenter Campus `37d90644-d524-8129-8974-d18123b548c2`):**
  1. `Adress` (place) set → "Microsoft Alviso Datacenter Campus", 1657 Alviso-Milpitas Road, San Jose, CA 95002 (37.432, -121.967). Source: ConnectCRE.
  2. `Size` set → "397,205 sf / 2-building campus / 48 MW / 65 acres". Source: HITT4.md.
- **Verified clean (0 additional writes needed):** all 3 new people (Brett Hitt/John Kane/Megan Lantz) Company+FQ+Location ✓ · ABC membership Companies→HITT ✓ · Santa Clara division Adress+People=Kane+Projects=Alviso ✓ · all 5 new software Company→HITT ✓ · 5 events ✓ · 18 divisions ✓ · 8 memberships ✓ · 16 locations ✓.
- **Left empty-for-cause (unchanged from prior passes):** Construction Safety Week/SubDay (national/sourceless) · NAIOP date/Adress ("Northern Virginia" only) · Size=Regional conflict · people LinkedIn/Email/Phone (none in any dossier).
