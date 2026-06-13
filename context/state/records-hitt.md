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

## Post-load audit #7 (2026-06-13, /notion-audit vs HITT4.md — new dossier registered)
New dossier `HITT4.md` (133KB, run_date 2026-06-12, 7 projects, 38 sources) appeared on disk. Full comparison of HITT4 vs. all live records.
- **3 fills (all verified live):**
  1. Boeing SC 787 body → +LEED Silver, +395 acres, +6.2M construction hours. Source: HITT LinkedIn post.
  2. HITT New HQ body → +LEED Platinum + WELL targets, +100k sf solar canopy, +40k sf VT lab, +55k sf urban parks. Source: New England Construction News.
  3. Andaz Miami Beach body → +groundbreaking Mar 25 2024, +18-month schedule, +ABC Florida East Coast Excellence Eagle Award (2025). Source: HITT project page.
- **Duplicate flagged (UI):** Megan Lantz — 2 People records: `37d90644…8116acdc` (06-12, richer body, no LinkedIn) and `37c90644…81f4988e` (06-11, LinkedIn present, from Apollo CSV). Non-destructive rule → not deleted. Zack to merge/delete in UI.
- **Verified clean:** 14 software rows (incl. FARO Scene, Synchro, EC3, TradeTapp, Pype, e4Clicks — all present); 5 events; 9 memberships; 18 divisions; 16 locations; John Kane + Brett Hitt + Megan Lantz (dup noted) all in People.
- **HITT4 not loaded:** DBIA webinar (Feb 2026 virtual — low-confidence Facebook source); revenue trend table (body already has figures); safety programs, federal contracts (JMACC project covers it); divisional structure (0 divisions in HITT4; Notion's 18 are correct from HITT1).

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = HITT.
2. **Existing Software** view → clear `__TEMPLATE__` filter.
3. **Memberships-note People view** → re-point hardcoded company filter to HITT.
4. **Megan Lantz dup** → merge `37c90644…81f4988e` LinkedIn into `37d90644…8116acdc`, then delete the 06-11 record (Apollo CSV origin).
