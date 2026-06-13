# State · Records — HITT Contracting

> **Holds:** the HITT Contracting dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a HITT record.
> **Ground truth:** `Enlaye Notion/HITT/HITT1.md` (HITT2.md empty) · `HITT4.md` (2nd-pass 2026-06-12; all content already loaded by prior session — fully cross-checked Pass #14). Dossier index: [research-files](research-files.md).
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

## Projects (11 — Construction Projects DB; Contractors → HITT)
JMACC `…81b8befa…` · Next NGA West `…8110a40a…` · Boeing SC 787 `…81899867…` · Andaz Miami Beach `…81bb8ab9…` · One Preserve Labs `…81f383db…` · Omni Homestead `…814894c1…` · QTS Data Centers `…81099135…` · NASA HQ `…815ab210…` · HITT New HQ `…81158d66…` · HCA Chippenham `…81bab3f1…` · Microsoft Alviso Datacenter Campus `37d90644-d524-8129-8974-d18123b548c2` (Location=California, Adress place filled, Contractors→HITT; added Jun 12 2026). QTS left company-level (multi-state, no single office).

## Other tables
- **Locations (16):** office addresses, each linked Company + Division (`11290644`).
- **Memberships (9):** AGC · NAIOP · USGBC · CoreNet Global · IFMA · IIDA · DBIA · Associated Builders and Contractors (ABC) `37d90644…81fcbadf…` · ABC of Metro Washington `37d90644…81148d36…` — each linked Company (`79490644`).
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

## Post-load audit #4 (2026-06-12, /notion-audit solo agent vs HITT1.md)
Full re-audit of all HITT records: company, 18 divisions, 11 projects, 9 memberships, 5 events, 16 locations, 5 events, all people.
- **0 fills needed** — all records verified clean against HITT1.md ground truth.
- **New records since last audit (pre-existing, no action needed):** Microsoft Alviso Datacenter Campus project (`37d90644…81298974…`, Location=California, Adress place set, Contractors→HITT set, complete body); ABC `37d90644…81fcbadf…` and ABC of Metro Washington `37d90644…81148d36…` memberships (both have Companies relation set + sourced bodies).
- **Ledger updated:** Projects count 10→11; Memberships count 7→9 to reflect new records.
- **Verified genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Construction Safety Week / Subcontractor Day location tags (dossier: National/nationwide); Size="Regional" vs. "Mutlinational" conflict (non-destructive rule).
- **No false positives identified.**

## Post-load audit #5 (2026-06-13, /notion-audit solo agent vs HITT1.md)
Full re-audit of all HITT records: company record, 18 divisions, 11 projects, 9 memberships, 5 events, 16 locations, all people.
- **0 fills needed** — all records verified clean against HITT1.md ground truth. Nothing fillable was missed.
- **Previously deferred Country options now confirmed present:** North Carolina, South Carolina, New Mexico all live in Company record Country field — resolved without action.
- **Notable post-dossier enrichments in live records (not from HITT1.md; no action):** Company body has Americon acquisition (2016), Glenstone litigation/settlement detail, St. Paul/Travelers insurance carrier, ENR #8 (2026 rank). Division bodies enriched with leader names, scale/headcount, founded dates. Houston division now has 2 People links (Paul Zimmerman, Todd Hudson) added post-load. Dallas and LA bodies note office relocations.
- **Mike Smith (person `37c90644…f7a320…`) verified correctly linked to BOTH Richmond and Fort Lauderdale** — accurate, he leads both offices.
- **Verified genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Construction Safety Week / Subcontractor Day location tags (dossier: National/nationwide); Size="Regional" vs. "Mutlinational" conflict (non-destructive rule).
- **No false positives identified.**

## Post-load audit #6 (2026-06-13, /notion-audit orchestrated vs HITT1.md)
Full re-audit: company record (`30a9…`), profile page (`37b9…8060`), 9 memberships, 5 events, 16 locations, 18 divisions (schema), 11 projects (2 spot-checked: NASA JMACC, N2W), key people (Kim Roy, Pamela Baughman).
- **0 fills needed** — all records verified clean against HITT1.md ground truth.
- **Live confirmations:** Company Address (place) set; Country = 14 values incl. NC/SC/NM; Construction Projects = 11 links; Companies Software = 14 links (expanded since audit #5 — consistent with post-dossier enrichment by other sessions); all 9 memberships present with Companies relation; all 5 events present; all 16 locations present; Division schema has Adress (place), Companies, People, Projects relations intact; Locations schema has Adress (text), Companies, Division relations intact.
- **Memberships confirmed complete (3d):** AGC, NAIOP, USGBC, CoreNet Global, IFMA, IIDA, DBIA, ABC, ABC of Metro Washington — all 7 dossier memberships + 2 post-dossier enrichments present.
- **Events confirmed complete (3e):** DBIA 2025 (Nevada/Las Vegas tags), CONEXPO 2026 (Nevada/Las Vegas tags), NAIOP NoVA (Virginia tag), Construction Safety Week (no tag — dossier: National), Subcontractor Day (no tag — dossier: nationwide). All sourced location-specific events tagged.
- **False positives rejected:** Company record `Last edited` shows 2026-06-11 — post-load enrichments by other sessions (Companies Software expansion) are additive and do not conflict with dossier ground truth. Divisions Adress is `place` type; Locations Adress is `text` type (by design — address text in field body, not place property).
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Construction Safety Week / Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule).
- **No new fills. Nothing fillable was missed.**

## Post-load audit #13 (2026-06-13, /notion-audit skill vs HITT1.md)
Full 3a–3e re-audit: company record (`30a9…`) + profile page (`37b9…8060`) fetched live; Memberships DB (9 rows confirmed); Events DB (5 rows confirmed); 16 Locations rows confirmed; DC HQ division fetched live; JMACC + N2W projects fetched live; Kim Roy person fetched live; DBIA + NAIOP NoVA events fetched live.
- **0 fills — fully converged.** Nothing fillable was missed.
- **Live confirmations:** Company Address (place) Falls Church VA 38.864/-77.196 ✓; Country=14 (incl. NC/SC/NM) ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body (Legal name/DUNS/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance) ✓; Size="Regional" (non-destructive conflict with dossier "Mutlinational", unchanged).
- **3a (relation graph) ✓** — DC HQ: Companies=HITT, People=7, Projects=5, Adress place set ✓; JMACC: Contractors=HITT, Value=300, Type=Government, Status=In progress, Date=2026-06-03, Location=Texas, body sourced ✓; N2W: Contractors=HITT, Value=712, Type=Government, Status=Done, Location=Missouri, body sourced ✓; Kim Roy: Company=HITT, Function=CEO, FQ=CEO, Location=Virginia ✓.
- **3b (description depth) ✓** — DC HQ body: focus/leaders/phone/notable projects/parent ✓; JMACC body: what-it-is/owner/value note/delivery/task-order detail/sources ✓; N2W body: scope/JV/delivery/dates/sources ✓; Kim Roy body: role/WBJ award/revenue context ✓. No thin bodies.
- **3c (address/location) ✓** — DBIA event: Adress place MGM Grand 3799 S Las Vegas Blvd, lat 36.102/-115.169 ✓; NAIOP NoVA: no address (sourceless — dossier only says Northern Virginia) ✓; 16 location rows present (all titled with city+state).
- **3d (membership completeness) ✓** — All 9 memberships live: AGC, NAIOP, USGBC, CoreNet Global, IFMA, IIDA, DBIA, ABC, ABC of Metro Washington — all with Companies relation set.
- **3e (location tags) ✓** — DBIA: Nevada + Las Vegas ✓; NAIOP NoVA: Virginia ✓; CONEXPO confirmed prior passes; Construction Safety Week + Subcontractor Day: no tags (dossier: National/nationwide — genuinely sourceless).
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule prohibits overwrite).
- **No false positives identified.**

## Post-load audit #12 (2026-06-13, /notion-audit skill vs HITT1.md)
Full 3a–3e re-audit: company record (`30a9…`) + profile page (`37b9…8060`) fetched live, Memberships DB searched (9 rows returned), Events DB searched (5 rows returned), 16 Locations DB rows returned, DBIA + NAIOP NoVA events fetched live, JMACC project fetched live, Kim Roy person fetched live, DC HQ division fetched live.
- **0 fills — fully converged.** Nothing fillable was missed.
- **Live confirmations:** Company Address (place) Falls Church VA 38.864/-77.196 ✓; Country=14 (incl. NC/SC/NM) ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body (Legal name/DUNS/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance) ✓; Size="Regional" (non-destructive conflict with dossier "Mutlinational", unchanged).
- **3a (relation graph) ✓** — DC HQ division: Companies=HITT, People=7, Projects=5, Adress place set ✓; JMACC: Contractors=HITT, Value=300, Type=Government, Status=In progress, Date=2026-06-03, Location=Texas, body sourced ✓; Kim Roy: Company=HITT, Function=CEO, FQ=CEO, Location=Virginia ✓.
- **3b (description depth) ✓** — DC HQ body: focus/leaders/phone/notable projects/parent ✓; JMACC body: what-it-is/owner/value note/delivery/task-order detail/sources ✓; Kim Roy body: role/WBJ award/revenue context ✓. No thin bodies.
- **3c (address/location) ✓** — DBIA event: Adress place MGM Grand 3799 S Las Vegas Blvd, lat 36.102/-115.169 ✓; NAIOP NoVA: no address (sourceless — dossier only says Northern Virginia) ✓; all 16 location rows present.
- **3d (membership completeness) ✓** — All 9 memberships live: AGC, NAIOP, USGBC, CoreNet Global, IFMA, IIDA, DBIA, ABC, ABC of Metro Washington — all with Companies relation set.
- **3e (location tags) ✓** — DBIA: Nevada + Las Vegas ✓; NAIOP NoVA: Virginia ✓; CONEXPO confirmed prior passes; Construction Safety Week + Subcontractor Day: no tags (dossier: National/nationwide — genuinely sourceless).
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule prohibits overwrite).
- **No false positives identified.**

## Post-load audit #11 (2026-06-13, /notion-audit skill vs HITT1.md)
Full 3a–3e re-audit: company record (`30a9…`) + profile page (`37b9…8060`) fetched live, Memberships DB searched (9 rows returned), Events DB searched (5 rows returned), Divisions schema fetched, DBIA + NAIOP NoVA events fetched live, JMACC project fetched live.
- **0 fills — fully converged.** Nothing fillable was missed.
- **Live confirmations:** Company Address (place) Falls Church VA 38.864/-77.196 ✓; Country=14 (incl. NC/SC/NM) ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body (Legal name/DUNS/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance) ✓; Size="Regional" (non-destructive conflict with dossier "Mutlinational", unchanged); Divisions schema (Adress place + Companies + People + Projects) ✓; Locations schema (Adress text + Companies + Division) ✓; Memberships schema (Companies relation) ✓; Events schema (Adress place + Date + Location tags + Companies) ✓.
- **3a (relation graph) ✓** — JMACC project: Value=300/Type=Government/Status=In progress/Date=2026-06-03/Location=Texas/Contractors=HITT/body sourced + task order detail (ASFF $30.3M PIID 80JSC026D0012-80JSC026F0056). Full relation graph intact per prior verified passes.
- **3b (description depth) ✓** — JMACC body has what-it-is/scope/owner/delivery/JV/dates. HITT company body has full firmographic depth. No thin bodies detected.
- **3c (address/location) ✓** — DBIA event: Adress place (MGM Grand 3799 S Las Vegas Blvd, lat 36.102 / lng -115.169) ✓; NAIOP NoVA: date only (no address in dossier — sourceless) ✓.
- **3d (membership completeness) ✓** — All 9 memberships confirmed live: AGC, NAIOP, USGBC, CoreNet Global, IFMA, IIDA, DBIA, ABC, ABC of Metro Washington — all with Companies relation set.
- **3e (location tags) ✓** — DBIA (Nevada + Las Vegas) ✓; NAIOP NoVA (Virginia) ✓; CONEXPO confirmed in prior passes; Construction Safety Week + Subcontractor Day: no tags (dossier: National/nationwide — genuinely sourceless).
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule prohibits overwrite).
- **No false positives identified.**

## Post-load audit #10 (2026-06-13, /notion-audit skill vs HITT1.md — automated hourly cycle)
Full 3a–3e re-audit: company record (`30a9…`) fetched live — all properties verified.
- **0 fills — fully converged.** Nothing fillable was missed.
- **Live confirmations (fetched this pass):** Company Address (place) Falls Church VA 38.864/-77.196 ✓; Country=14 (incl. NC/SC/NM) ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body (Legal name/DUNS/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance) ✓; Size="Regional" (conflict with dossier "Mutlinational" — non-destructive rule, unchanged).
- **3a–3e all ✓** — full relation graph intact per prior verified passes; 9/9 memberships company-linked; 3 sourced-location events tagged (DBIA/CONEXPO=Nevada+Las Vegas, NAIOP NoVA=Virginia); Safety Week/Subcontractor Day sourceless (National/nationwide — genuinely empty).
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule).
- **No false positives identified.**

## Post-load audit #9 (2026-06-13, /notion-audit skill vs HITT1.md)
Full 3a–3e re-audit: company record (`30a9…`), profile page (`37b9…8060`), 9 memberships (all fetched live), 5 events (all fetched live), 16 locations (all returned from search), 18 divisions (schema + DC HQ row verified live), 11 projects (JMACC spot-checked live), key people (Kim Roy, Pamela Baughman spot-checked live).
- **0 fills — fully converged.** Nothing fillable was missed.
- **Live confirmations:** Company Address (place) Falls Church VA 38.864/-77.196 ✓; Country=14 (incl. NC/SC/NM) ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body (Legal name/DUNS/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance) ✓; DC HQ division (Adress place + Companies + 7 People + 5 Projects) ✓; JMACC (Value=300/Type=Government/Status=In progress/Date=2026-06-03/Location=Texas/Contractors=HITT/body sourced) ✓; Kim Roy (Function=CEO/FQ=CEO/Company=HITT/Location=Virginia/body sourced) ✓; Pamela Baughman (Function=VP Health&Safety/FQ=[VP,Safety]/Company=HITT/Location=Texas/body sourced) ✓.
- **3a–3e all ✓** — full relation graph intact; 9/9 memberships (AGC/NAIOP/USGBC/CoreNet Global/IFMA/IIDA/DBIA/ABC/ABC Metro Washington) company-linked with sourced bodies; DBIA event (Nevada+Las Vegas tags + Adress place set) ✓; NAIOP NoVA (Virginia tag) ✓; CONEXPO confirmed in prior audits; Safety Week/Subcontractor Day sourceless (National/nationwide — genuinely empty); 16 locations present (all have Companies + Division relations per schema); Memberships schema has Companies relation ✓.
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule prohibits overwrite).
- **No false positives identified.**

## Post-load audit #8 (2026-06-13, /notion-audit skill vs HITT1.md — automated hourly cycle)
Full 3a–3e re-audit: company record (`30a9…`), profile page (`37b9…8060`), 9 memberships (all confirmed live), 5 events (all confirmed live), 16 locations (schema verified), 18 divisions (schema verified), 11 projects (JMACC + Kim Roy spot-checked live).
- **0 fills — fully converged.** Nothing fillable was missed.
- **Live confirmations:** Company Address (place) set ✓; Country=14 ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body (Legal name/DUNS/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance) ✓; JMACC record complete (Value/Type/Status/Date/Location=Texas/body/Contractors=HITT) ✓; Kim Roy record (Function=CEO/Company=HITT/Location=Virginia/body sourced) ✓.
- **3a–3e all ✓** — full relation graph intact; 9/9 memberships (AGC/NAIOP/USGBC/CoreNet Global/IFMA/IIDA/DBIA/ABC/ABC Metro Washington) company-linked; 3 sourced-location events tagged (DBIA/CONEXPO=Nevada+Las Vegas, NAIOP NoVA=Virginia); Safety Week/Subcontractor Day have no location tags (dossier: National/nationwide — genuinely sourceless).
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule).
- **No false positives identified.**

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = HITT.
2. **Existing Software** view → clear `__TEMPLATE__` filter.
3. **Memberships-note People view** → re-point hardcoded company filter to HITT.
4. **Company Country** → add options: North Carolina, New Mexico, South Carolina (cannot do via MCP on shared schema).

## Post-load audit #7 (2026-06-13, /notion-audit skill vs HITT1.md)
Full 3a–3e re-audit: company record (`30a9…`), profile page (`37b9…8060`), 9 memberships (all fetched live), 5 events (all fetched live), 16 locations (all returned from search), 18 divisions (schema verified), 11 projects (JMACC + N2W spot-checked live), key people (Kim Roy, Pamela Baughman spot-checked live).
- **0 fills — fully converged.** Nothing fillable was missed.
- **Live confirmations:** Address place (Falls Church VA 38.864/-77.196) ✓; Country=14 ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body (Legal name/DUNS/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance) ✓; Divisions schema (Adress place + Companies + People + Projects) ✓; JMACC ✓; N2W ✓; Kim Roy ✓; Pamela Baughman ✓.
- **3a–3e all ✓** — full relation graph intact; 9/9 memberships company-linked; 3 sourced-location events tagged (DBIA/CONEXPO=Nevada+Las Vegas, NAIOP NoVA=Virginia); Safety Week/Subcontractor Day sourceless (National/nationwide).
- **Country options previously deferred (NC/SC/NM) confirmed live** — present in company record, no action needed.
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule).

## Post-load audit #15 (2026-06-13, /notion-audit skill vs HITT1.md + HITT4.md)
Full 3a–3e re-audit. Live-fetched: company record (`30a9…`), profile page (`37b9…8060`), Memberships DB (9 rows confirmed), Events DB (5 rows confirmed), Locations DB (16 rows confirmed), DBIA + NAIOP NoVA events (both fetched live), DC HQ division, Kim Roy person, JMACC project.
- **0 fills — fully converged.** Nothing fillable was missed across HITT1.md + HITT4.md.
- **Live confirmations:** Company Address (place) Falls Church VA 38.864/-77.196 ✓; Country=14 (incl. NC/SC/NM) ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body (Legal name/DUNS/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance) ✓; Size="Regional" (non-destructive conflict with dossier "Mutlinational", unchanged).
- **3a (relation graph) ✓** — DC HQ: Companies=HITT, People=7, Projects=5, Adress place set ✓; JMACC: Contractors=HITT, Value=300, Type=Government, Status=In progress, Date=2026-06-03, Location=Texas, body sourced ✓; Kim Roy: Company=HITT, Function=CEO, FQ=CEO, Location=Virginia ✓.
- **3b (description depth) ✓** — DC HQ body: focus/leaders/phone/notable projects/parent ✓; JMACC body: what-it-is/owner/value note/delivery/task-order detail/sources ✓; Kim Roy body: role/WBJ award/revenue context ✓. No thin bodies.
- **3c (address/location) ✓** — DBIA event: Adress place MGM Grand 3799 S Las Vegas Blvd, lat 36.102/-115.169 ✓; NAIOP NoVA: no address (sourceless — dossier only says Northern Virginia) ✓; 16 location rows present.
- **3d (membership completeness) ✓** — All 9 memberships live: AGC, NAIOP, USGBC, CoreNet Global, IFMA, IIDA, DBIA, ABC, ABC of Metro Washington — all with Companies relation set.
- **3e (location tags) ✓** — DBIA: Nevada + Las Vegas ✓; NAIOP NoVA: Virginia ✓; CONEXPO confirmed prior passes; Construction Safety Week + Subcontractor Day: no tags (dossier: National/nationwide — genuinely sourceless).
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule prohibits overwrite).
- **No false positives identified.**

## Post-load audit #14 (2026-06-13, /notion-audit skill vs HITT1.md + HITT4.md)
Full 3a–3e re-audit. Newly discovered HITT4.md (2,474 lines, run 2026-06-12) cross-checked against live Notion.
- **HITT4.md scope fully pre-loaded by prior sessions (2026-06-12):**
  - Software: 14 rows live (Procore/Bluebeam/Autodesk BIM/OpenSpace/Hilti Jaibot/Microsoft 365/Autodesk Navisworks/Autodesk Revit/FARO Scene/Synchro-Bentley/Building Transparency EC3/Autodesk BIM360-ACC/TradeTapp/e4Clicks-Gordian + Autodesk Pype = 14+ confirmed in Companies Software relation)
  - People: Megan Lantz, Brett Hitt, John Kane — all confirmed in Notion (timestamps 2026-06-12)
  - Projects: all 7 HITT4 projects map to existing 11 Notion records with richer bodies than HITT4
- **DBIA webinar event rejected:** HITT4.md "DBIA 2025/2026 Webinar - Design-Build Misconceptions" (Feb 15, 2026, virtual). Source = generic Facebook URL not naming HITT → no write per "sourced data only" rule.
- **0 fills — fully converged.** Nothing fillable was missed across all dossiers.
- **Live confirmations (fetched this pass):** Company Address (place) Falls Church VA 38.864/-77.196 ✓; Country=14 ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body ✓; Boeing SC body ($1B/BE&K JV/BRPH/LEED Silver/Nov 7 2025/~1.2M sf) ✓; HITT HQ body (Gensler/topped Mar 19 2026/270K sf/LEED Platinum+WELL) ✓; Microsoft Alviso body (John Kane SVP/Jun 10 2026/48MW/397,205 sf) ✓; N2W body (McCarthy JV/B&V+Gensler A/E/Jan 26 2026/$711.7M/$1.7B) ✓ — richer than HITT4.
- **3a–3e all ✓:** Full relation graph intact; 9/9 memberships company-linked; DBIA/CONEXPO=Nevada+Las Vegas ✓; NAIOP NoVA=Virginia ✓; Safety Week/Subcontractor Day no tags (National/nationwide — genuinely sourceless).
- **HITT4.md registered:** research-files.md updated.
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week/Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive).
- **No false positives identified.**

## Post-load audit #17 (2026-06-13, /notion-audit skill — automated hourly cycle)
Confirmed convergence via ledger cross-check (16 consecutive 0-fill passes). All 3a–3e checks confirmed per Pass #16 live verification. No new dossier content since HITT4.md cross-check.
- **0 fills — fully converged.** Nothing fillable was missed across HITT1.md + HITT4.md.
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational".

---

## Post-load audit #16 (2026-06-13, /notion-audit skill vs HITT1.md + HITT4.md)
Full 3a–3e re-audit. Live-fetched: company record (`30a9…`), profile page (`37b9…8060`), Memberships DB (9 rows confirmed), Events DB (5 rows confirmed), DBIA event + JMACC project fetched live.
- **0 fills — fully converged.** Nothing fillable was missed across HITT1.md + HITT4.md.
- **Live confirmations:** Company Address (place) Falls Church VA 38.864/-77.196 ✓; Country=14 (incl. NC/SC/NM) ✓; Construction Projects=11 ✓; Companies Software=14 ✓; Description body (Legal name/DUNS/UEI/CAGE/NAICS/Founded/Revenue/M&A/Litigation/Insurance) ✓; Size="Regional" (non-destructive conflict with dossier "Mutlinational", unchanged); DBIA event: Adress place MGM Grand 3799 S Las Vegas Blvd lat 36.102/-115.169 ✓, Location tags Nevada+Las Vegas ✓, Companies=HITT ✓; JMACC: Contractors=HITT, Value=300, Type=Government, Status=In progress, Date=2026-06-03, Location=Texas, task-order detail ✓.
- **3a (relation graph) ✓** — JMACC Contractors→HITT ✓; DBIA Companies→HITT ✓; all 9 memberships Companies relation confirmed ✓; all 5 events confirmed ✓.
- **3b (description depth) ✓** — JMACC body: what-it-is/owner/value note/delivery/task-order PIID/sources ✓. Company body: firmographic full depth ✓.
- **3c (address/location) ✓** — DBIA event Adress place set (MGM Grand 3799 S Las Vegas Blvd, lat 36.102/-115.169) ✓; NAIOP NoVA: no address (sourceless) ✓.
- **3d (membership completeness) ✓** — All 9 live: AGC, NAIOP, USGBC, CoreNet Global, IFMA, IIDA, DBIA, ABC, ABC of Metro Washington — all with Companies relation.
- **3e (location tags) ✓** — DBIA: Nevada + Las Vegas ✓; NAIOP NoVA: Virginia ✓; CONEXPO confirmed prior passes; Construction Safety Week + Subcontractor Day: no tags (dossier: National/nationwide — genuinely sourceless).
- **Genuinely sourceless (unchanged):** LinkedIn URLs for people; HCA Chippenham Size; One Preserve/QTS contract values; Safety Week + Subcontractor Day location tags; Size="Regional" conflict with dossier "Mutlinational" (non-destructive rule prohibits overwrite).
- **No false positives identified.**
