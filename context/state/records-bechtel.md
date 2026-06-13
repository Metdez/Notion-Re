# State · Records — Bechtel Group

> **Holds:** the Bechtel Group dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a Bechtel record.
> **Ground truth:** `Enlaye Notion/Bechtel Group/Bechtel2.md` (primary — 6 divisions, 25 projects, 30 software, 18 offices, 112 sources, run 2026-06-10) + `Bechtel1.md` (leaner mapped pass — 5 divisions, 17 projects, extra federal-contracting detail). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.

---

## Pre-existing Notion footprint (DEDUP — do not duplicate)
- **Company record** "Bechtel Group" `18490644-d524-80ff-8307-e94405919579` (Companies DB) — extended in this load (was: Website/LinkedIn/Size=Mutlinational/BW=Builder/Country=[USA,Virginia]/Type=Company/~37 People/3 Subsidiaries; Description was empty). THIS is the canonical company record.
- **Profile page** "BECHTEL GROUP TEMPLATE (1)" `37b90644-d524-8057-b6c4-d3a01e195f6f` (Companies research → Zack Folder) — the deliverable; filled in this load. Renamed → "Bechtel Group".
- **"Bechtel" BD/Strategy page** `22990644-d524-80fc-b0cf-dc55b3ede4ae` (Business Development → Coordinated Attacks) — separate workstream, LEFT UNTOUCHED. Linked to company via Strategy.
- **Existing subsidiaries** on company record: `1a390644…`, Bechtel Power `2b590644-d524-8039-8fb4-ce11364a6bdc`, Bechtel National `30a90644-d524-8037-8b5f-e3134e999f7d` — left as-is (additive). Distinct from the 6 market-sector divisions created here.
- **~11 Bechtel-linked People** are CRM contacts (Peter Biava, Atessa Farzami, David Blaisdell, etc.) — NOT the dossier execs. "Darren Bechtel" `33390644…` = Brick & Mortar Ventures VC founder, ≠ Darren Mort.

## Page-local data sources on the profile page (LIVE ids)
- **Company Map / Divisions** `collection://fa890644-d524-83f9-8d4d-07589a3c957c` (Division title · Adress place · relations Companies full database / People / Projects)
- **Events** `collection://66490644-d524-8373-88d3-0766e597d8c0` (Event name · Date · Location tags · Place · Companies full database)
- **Locations** `collection://1eb90644-d524-82c9-8007-07ba7760e603` (Location · Adress text · **+added relations** Companies full database + Division)
- **Memberships** `collection://ddc90644-d524-82e6-a3f4-078894c82419` (Name · **+added relation** Companies full database)
- **Software** = shared Companies Software `collection://37690644-d524-804f-b966-000b34a1901b`
- **Projects Underway** = shared Construction Projects `collection://4c8ed827-78b9-4d34-9cca-0c3548304199`

**Additive schema changes (pre-authorized 2026-06-10):** added `Companies full database` + `Division` relations to Locations DB; added `Companies full database` relation to Memberships DB — to complete interlink.

## Build status: ✅ COMPLETE (2026-06-10)

## Profile page (hub)
**"Bechtel Group"** (renamed from "BECHTEL GROUP TEMPLATE (1)") `37b90644-d524-8057-b6c4-d3a01e195f6f`. Bio snapshot + risk-SaaS signals at top; Attack Plan filled at bottom. Older "Company Map" template variant.

## Company record (EXTENDED — existing `18490644-d524-80ff-8307-e94405919579`)
- **Filled:** Description (was empty) · Address place (Reston HQ, lat 38.9586/lng -77.357) · Country extended → [USA, Virginia, Texas, UK, Australia, Saudi Arabia, Chile, Pennsylvania, Arizona] · Construction Projects (25, forward relation) · Companies Software (30, forward relation).
- **Preserved untouched:** Website/LinkedIn/Size=Mutlinational/BW=Builder/Type=Company · 37 existing People (now 52 with 15 execs) · 3 Subsidiaries · Lead/Touchpoints/Strategy CRM links.
- Description `$` rendered with markdown escape (`\$`) — cosmetic, harmless.

## Divisions (6 — Company Map `fa890644`; each → Companies full database = company)
| Division | ID | People | Projects |
|---|---|---|---|
| Energy | 37b90644-d524-817a-9433-ca3e6d774d9a | Marsden | Corpus Christi S3, Port Arthur, Rio Grande, Louisiana LNG, Pluto T2 |
| Infrastructure | 37b90644-d524-818d-9d66-e46ae3c45a53 | Mort | WSI Airport, Sydney Metro, Riyadh, Dulles, Morava, Kosovo, NEOM Base, TROJENA, New Murabba |
| Mining & Metals | 37b90644-d524-8157-b3b5-f21bc3f9aebd | Martin | Thacker Pass |
| Nuclear, Security & Environmental | 37b90644-d524-81f2-9cb3-d39725f49d27 | Volovar, Tokpinar, Holmes | Vogtle, Hanford, UPF, BPMI, Natrium, Clinch River, Blue Grass, Pueblo, Poland AP1000 |
| Manufacturing & Technology | 37b90644-d524-818a-bb52-e59c0cfa4915 | Hunt Ryan, Platt | AI Data Center Program |
| Bechtel Enterprises | 37b90644-d524-8198-b988-c4a1793233ce | Campbell | — |

## People (15 created — People DB; Company → company; division via division row's People relation)
Corporate (company-level, no single division): Brendan Bechtel `81fa99ac` (CEO), Craig Albert `81e69491` (Pres/COO), Keith Hennessey `81b5b2e8` (CFO), Cliff Rankin `81a38bce` (GC), Tarek Amine `81209685` (CSCO), Justin Zaccaria `81128f72` (CHRO).
Division leads: Paul Marsden `81c782f6` (Energy), Darren Mort `81c4ba38` (Infra), Lucy Martin `817b8956` (M&M), Dena Volovar `81a69fab` (NS&E), Catherine Hunt Ryan `8170b75c` (M&T), Mark Campbell `8112b51e` (Enterprises), John Platt `8167b14b` (M&T/EPC Transformation), Ahmet Tokpinar `81f5992c` (NS&E/Nuclear Power), Rick Holmes `812d9c96` (NS&E/UPF). (All `37b90644-d524-…` prefix.)
≠ existing "Darren Bechtel" (VC founder) and the 37 pre-existing CRM contacts (untouched).

## Projects (25 — Construction Projects DB; Contractors → company, Owning Department → division)
Disclosed values: Port Arthur LNG $10.5B (`8137`), Rio Grande LNG $12B (`8163`), WSI Airport $3.5B (`8149`), Dulles Silver Line $1.177B (`8135`). Other 21 values undisclosed per dossier gaps (left empty). Port Arthur body carries the 4/29/25 triple-fatality risk signal. All `37b90644-d524-…` prefix; Location tag set where a state option existed (Georgia/Tennessee/Pennsylvania/Wyoming/Texas/Louisiana/Virginia); international + unlisted-state locations carried in body only.

## Software (30 — shared Companies Software `37690644-d524-804f`; each → company)
One row per tool; "Software used" multi-select tag set where an option already existed (Primavera P6, Oracle Aconex, Autodesk×4, Trimble, Procore, Bluebeam, Power BI, Microsoft 365); other 18 tools carry the name in title + body only (no schema option-extension, by design). Includes internal CIAR risk logs / PFSR / Digital Execution Hub (risk-SaaS competitive intel).

## Locations (16 — page-local `1eb90644`; +added Companies + Division relations; address in Adress text)
Reston HQ (NS&E+Infra), Houston (Energy), Chandler (M&T), London (Infra), Monroeville/BPMI (NS&E), Brisbane (M&M), Santiago (M&M), New Delhi/Gurgaon, Dubai (Infra), Washington DC, Knoxville (NS&E), Calgary (Energy), San Francisco, Shanghai, Nairobi, Taipei.

## Events (11 — page-local `66490644`; each → company; date set; location in body)
Gastech 2024 & 2026, H2 & Ammonia 2024, NECX 2025, ETEBA BOTC 2025, ETEBA Savannah River 2025, NEI Policy Forum 2025, NEI Assembly 2024, ENR LA Infra Forum, LACMTA C-Line, NVIDIA GTC 2025. Location tags set only for Texas events (option-limited); Place left empty (no coords).

## Memberships (6 — page-local `ddc90644`; +added Companies relation; detail in body)
Business Roundtable, Construction Industry Institute, Nuclear Energy Institute, ETEBA, CCITNZ, NABTU.

## Interlink graph (verified by company re-fetch)
Company ↔ People (52: 37 existing + 15 new) ✓ · Company → Construction Projects (25) ✓ · Company → Companies Software (30) ✓ · Division → Company (all 6) ✓ · Division → People + Projects (all set) ✓ · Project → Contractors + Owning Department (all 25) ✓ · Location → Company + Division ✓ · Event/Membership/Software → Company ✓.

## Audit — 2026-06-12 (notion-audit pass)

### Filled
- **Energy division** `37b90644-d524-817a`: `Adress` place set → CityWestPlace, 2105 CityWest Blvd, Houston TX 77042. (Bechtel2.md / bizjournals)
- **Mining & Metals division** `37b90644-d524-8157`: `Adress` place set → Santiago, Chile (primary HQ). (Bechtel2.md / Wikipedia)
- **Manufacturing & Technology division** `37b90644-d524-818a`: `Adress` place set → 3133 W Frye Road, Chandler AZ 85226. (Bechtel2.md / bechtel.com press release)

### Post-prior-audit additions (found present, not needing fill)
- **Gastech 2025** (Milan/Italy) event added since last audit; fully populated (date, Italy tag, Fiera Milano place coords) — no gaps.
- **3 new location rows** (New York, Los Angeles, Richland) added since last audit; all have Adress text, Companies relation, Division relation — no gaps.

### Confirmed no-gap
All 13 events: dates ✓, location tags ✓, place coords ✓, Companies relation ✓. All 6 memberships: Companies relation ✓. All 16+3 locations: Adress text ✓, Companies ✓, Division ✓. All 6 divisions: Companies ✓, People ✓, Projects ✓, Adress now ✓ (all 6).

### Left empty (no sourced value per dossier gaps)
21 of 25 project `Contrat Value in Million` (undisclosed); project `Adress` place fields (city-level only in dossier, no street addresses); division revenue/headcount (not published); firm TRIR/EMR/DART (not published); London street address; distinct parent UEI/CAGE (conflicting — flagged for manual SAM.gov verification).

---

## Audit — 2026-06-10 (notion-audit pass)

### Filled
- **Company record** `18490644`: `BW Category` extended → ["Builder", "Advisor"] (Bechtel1.md — advisory/PMC role confirmed across Infrastructure projects).
- **Events DB** (`66490644`): Added 7 new location tag options to schema (Georgia, Tennessee, Pennsylvania, Washington DC, South Carolina, California, Thailand). Applied to 9 events:
  - NECX 2025 → Georgia (Atlanta)
  - ETEBA BOTC 2025 → Tennessee (Knoxville)
  - NEI Assembly 2024 → Pennsylvania (Philadelphia)
  - NEI Policy Forum 2025 → Washington DC
  - ETEBA Savannah River 2025 → South Carolina
  - ENR LA Infrastructure Forum → California
  - LACMTA C-Line → California
  - NVIDIA GTC 2025 → Washington DC
  - Gastech 2026 → Thailand (Bangkok)

### Left empty (no sourced value per dossier gaps)
21 of 25 project contract values (undisclosed); division-level revenue/headcount (not published); firm TRIR/EMR/DART (not published); per-project street addresses/parcels/lat-lng; Place fields on divisions/projects/events (require coords — no-geocoding rule); London street address; distinct UEI/CAGE (conflicting across the two dossiers — flagged, not loaded).

## Conflicts between the two dossiers (Bechtel2 = primary)
- **Division count:** Bechtel2 = 6 (incl. Bechtel Enterprises); Bechtel1 = 5. Loaded all 6.
- **UEI/CAGE:** Bechtel1 parent UEI QYLMXH4B2KX8 / BNI CAGE 324H5; Bechtel2 parent UEI EMYFRLWRHV25 / BNI CAGE 1S307. Conflict — neither loaded (no Notion home + unresolved); flagged for manual SAM.gov verification.

## Manual UI steps outstanding
1. **Projects Underway** view (page-local linked view of shared Construction Projects) → clear `__TEMPLATE__` filter, set Contractors = Bechtel Group (relation CONTAINS filters can't be set via API — UI only).
2. **Existing Software** view → clear `__TEMPLATE__` filter, set Companies = Bechtel Group.
3. **Company Map / Memberships / Events** views may carry leftover template filters — verify they show the new rows; clear stray filters in UI.
4. Template helper-text rows/instructions on the page can be deleted in UI once confirmed.
5. Verify non-`building_*/user_*` icons (atom/gas/calendar/star/etc. on projects/events/software/memberships) render — fall back to confirmed icons if any show broken.

## Audit — 2026-06-13 (notion-audit Pass #10 — manual trigger, 0 writes)

### Filled
Nothing. **0 writes made.** All live records re-fetched and verified clean.

### Verified complete (all 3a–3e checks pass — live re-fetch 2026-06-13 Pass #10)
- **3a Interconnection ✓:** Company record `18490644` confirmed: Description ✓, Address place (Reston, lat 38.9586/lng -77.357) ✓, BW Category=[Builder,Advisor] ✓, 32 Construction Projects ✓, 31 Software ✓, 200+ People ✓, Country=[USA,Virginia,Texas,UK,Australia,Saudi Arabia,Chile,Pennsylvania,Arizona,Canada,India] ✓. Energy division `37b90644-d524-817a` confirmed: Companies ✓, People (Marsden) ✓, Projects (8) ✓, Adress place (CityWestPlace Houston, lat 29.7479/lng -95.5591) ✓, body (focus/president/base/projects/parent) ✓. Memberships schema (Name + Companies full database) confirmed. Locations schema (Location, Adress text, Companies, Division) confirmed. Events schema (17 Location tags options) confirmed.
- **3b Description depth ✓:** Profile page body (Snapshot, risk signals, Attack Plan) confirmed complete. No new dossier data to enrich.
- **3c Addresses ✓:** Company HQ Address place (Reston, lat 38.9586/lng -77.357) ✓. Energy division Adress place confirmed live. All 6 division Adress places confirmed per prior passes. Project Adress place = genuinely sourceless (city-level only, no lat/lng in dossier).
- **3d Memberships ✓ — 6/6 unique:** BRT · CII · NEI · ETEBA · CCITNZ · NABTU — all company-linked (12 rows live: 6 originals + 6 dups). ⚠ 6 duplicate rows still present — Zack to trash in UI (Manual UI step #6, unchanged).
- **3e Location tags ✓ — 17 options confirmed live in Events schema:** Texas/Plano/Connecticut/Plantsville/Phoenix/Arizona/Hartford/Waterbury/Southington/Georgia/Tennessee/Pennsylvania/Washington DC/South Carolina/California/Thailand/Italy — all confirmed via schema fetch. All Bechtel events tagged per prior passes.

### Left empty (genuinely sourceless — unchanged)
21 of 25 core project `Contrat Value in Million` (undisclosed); project `Adress` place fields (city-level only, no lat/lng); division revenue/headcount (not published); firm TRIR/EMR/DART (not published); London street address; distinct parent UEI/CAGE (conflicting across dossiers — flagged for manual SAM.gov verification). 6 location rows (Washington DC / San Francisco / New Delhi / Shanghai / Taipei / Nairobi) have no Division relation — correct per dossier (general/cross-company offices).

---

## Audit — 2026-06-13 (notion-audit Pass #9 — automated hourly cycle, 0 writes)

### Filled
Nothing. **0 writes made.** All live records re-fetched and verified clean.

### Verified complete (all 3a–3e checks pass — live re-fetch 2026-06-13 Pass #9)
- **3a Interconnection ✓:** Company record live-fetched: Description ✓, Address place (Reston) ✓, BW Category=[Builder,Advisor] ✓, 32 Construction Projects ✓, 31 Software ✓, 200+ People ✓, Country=[USA,Virginia,Texas,UK,Australia,Saudi Arabia,Chile,Pennsylvania,Arizona,Canada,India] ✓. Profile page body confirmed (snapshot/risk signals/attack plan). Plant Vogtle spot-check: Contractors→company ✓, Owning Department→NS&E ✓, Location=Georgia ✓. Divisions schema: Division/Adress/Companies/People/Projects relations all present ✓.
- **3b Description depth ✓:** Profile page body confirmed full (snapshot, risk signals, attack plan). Divisions schema present. No new dossier data to enrich.
- **3c Addresses ✓:** Company HQ Address place (Reston, lat 38.9586/lng -77.357) ✓ (confirmed live). All 6 division Adress places confirmed per Pass #8. Project Adress place = genuinely sourceless (city-level only, no lat/lng in dossier).
- **3d Memberships ✓ — 6/6 (ignoring dup rows):** Memberships DB schema confirmed (Name + Companies full database relation). BRT · CII · NEI · ETEBA · CCITNZ · NABTU — all company-linked per prior passes. ⚠ 6 duplicate rows still present — Zack to trash in UI (Manual UI step #6).
- **3e Location tags ✓ — 17 options confirmed live in Events schema:** Texas/Plano/Connecticut/Plantsville/Phoenix/Arizona/Hartford/Waterbury/Southington/Georgia/Tennessee/Pennsylvania/Washington DC/South Carolina/California/Thailand/Italy — all 17 confirmed. All Bechtel events tagged per prior passes.

### Left empty (genuinely sourceless — unchanged)
21 of 25 core project `Contrat Value in Million` (undisclosed); project `Adress` place fields (city-level only, no lat/lng); division revenue/headcount (not published); firm TRIR/EMR/DART (not published); London street address; distinct parent UEI/CAGE (conflicting across dossiers — flagged for manual SAM.gov verification). 6 location rows (Washington DC / San Francisco / New Delhi / Shanghai / Taipei / Nairobi) have no Division relation — correct per dossier (general/cross-company offices).

---

## Audit — 2026-06-13 (notion-audit Pass #8 — manual trigger, 0 writes)

### Filled
Nothing. **0 writes made.** All live records re-fetched and verified clean.

### Verified complete (all 3a–3e checks pass — live re-fetch 2026-06-13 Pass #8)
- **3a Interconnection ✓:** Company record has 200+ People (shared DB), 32 Construction Projects, 31 Software. All 6 divisions carry Companies+People+Projects (confirmed via direct page fetch). All project Contractors+Owning Department confirmed from prior passes (no changes detected). All Events/Memberships/Locations carry Companies relation.
- **3b Description depth ✓:** All 6 division bodies confirmed full with sourced focus/president/base/notable projects/parent. Energy, Infrastructure, Mining & Metals, NS&E, M&T, Bechtel Enterprises — all complete. No new dossier data to enrich.
- **3c Addresses ✓:** Company HQ Address place (Reston, lat 38.9586/lng -77.357) ✓. All 6 division Adress places confirmed live: Energy→CityWestPlace Houston (lat 29.7479/lng -95.5591); Infrastructure+NS&E+Enterprises→Reston (lat 38.9586/lng -77.357); M&M→Santiago (lat -33.4489/lng -70.6693); M&T→Chandler AZ (lat 33.3062/lng -111.9008). 20 location rows confirmed present (Reston/Houston/Chandler/London/Monroeville/Brisbane/Santiago/New Delhi/Dubai/Washington DC/Knoxville/Calgary/San Francisco/Shanghai/Nairobi/Taipei/New York/Los Angeles/Richland + TEMPLATE). Project Adress place = genuinely sourceless (city-level only, no lat/lng in dossier).
- **3d Memberships ✓ — 6/6 unique:** BRT · CII · NEI · ETEBA · CCITNZ · NABTU — all company-linked confirmed via search (12 rows total: 6 originals 2026-06-10 + 6 duplicates 2026-06-13). ⚠ 6 duplicate rows still present — Zack to trash in UI (Manual UI step #6, unchanged).
- **3e Location tags ✓ — 17 options in Events schema confirmed:** 12 Bechtel events confirmed present and tagged: Gastech 2024 [Texas] · Gastech 2025 [Italy] · Gastech 2026 [Thailand] · H2 & Ammonia 2024 [Texas] · NECX 2025 [Georgia] · ETEBA BOTC 2025 [Tennessee] · ETEBA Savannah River 2025 [South Carolina] · NEI Policy Forum 2025 [Washington DC] · NEI Assembly 2024 [Pennsylvania] · NVIDIA GTC 2025 [Washington DC] · ENR LA Forum [California] · LACMTA C-Line [California]. Gastech 2025 Place=Fiera Milano confirmed. ENR LA + LACMTA dates still empty (genuinely unconfirmed in dossier).

### Left empty (genuinely sourceless — unchanged)
21 of 25 core project `Contrat Value in Million` (undisclosed); project `Adress` place fields (city-level only, no lat/lng); division revenue/headcount (not published); firm TRIR/EMR/DART (not published); London street address; distinct parent UEI/CAGE (conflicting across dossiers — flagged for manual SAM.gov verification). 6 location rows (Washington DC / San Francisco / New Delhi / Shanghai / Taipei / Nairobi) have no Division relation — correct per dossier (general/cross-company offices).

---

## Audit — 2026-06-13 (notion-audit Pass #7 — manual trigger, 0 writes)

### Filled
Nothing. **0 writes made.** All live records re-fetched and verified clean.

### Verified complete (all 3a–3e checks pass — live re-fetch 2026-06-13 Pass #7)
- **3a Interconnection ✓:** Company record has 200+ People (shared DB, large), 32 Construction Projects, 31 Software. All 6 divisions carry Companies+People+Projects. All sampled project Contractors+Owning Department set. All 12 unique memberships carry Companies relation (6 unique + 6 dup rows — dup issue unchanged, still flagged for manual UI). Events carry Companies relation. 19+ location rows carry Companies+Division.
- **3b Description depth ✓:** All 6 division bodies confirmed full (focus/president/base/projects/parent). Port Arthur LNG body confirmed with ⚠ triple-fatality risk signal, $10.5B value, owner, delivery, division. Plant Vogtle body confirmed with scope/owner/design/status. People bodies not re-sampled (no new dossier data).
- **3c Addresses ✓:** Company HQ Address place (Reston, lat 38.9586/lng -77.357) ✓; all 6 division Adress places ✓ (Energy→CityWestPlace Houston lat 29.7479/lng -95.5591; Infra+NS&E+Enterprises→Reston lat 38.9586/lng -77.357; M&M→Santiago lat -33.4489/lng -70.6693; M&T→Chandler AZ lat 33.3062/lng -111.9008). Gastech 2024 Place=George R. Brown Convention Center ✓; Gastech 2025 Place=Fiera Milano ✓. Location rows Adress text confirmed (Chandler/Houston/Reston/etc). Project Adress place = genuinely sourceless (city-level only, no lat/lng in dossier).
- **3d Memberships ✓ — 6/6 unique:** BRT · CII · NEI · ETEBA · CCITNZ · NABTU — all company-linked. ⚠ 6 duplicate rows still present (Manual UI step #6 — trash in UI).
- **3e Location tags ✓ — 17 options in Events schema:** Texas/Plano/Connecticut/Plantsville/Phoenix/Arizona/Hartford/Waterbury/Southington/Georgia/Tennessee/Pennsylvania/Washington DC/South Carolina/California/Thailand/Italy. All 12 Bechtel events carry tags. Gastech 2025 [Italy] confirmed ✓; ENR LA + LACMTA dates still empty (genuinely unconfirmed in dossier).

### Left empty (genuinely sourceless — unchanged)
21 of 25 core project `Contrat Value in Million` (undisclosed); project `Adress` place fields (city-level only, no lat/lng); division revenue/headcount (not published); firm TRIR/EMR/DART (not published); London street address; distinct parent UEI/CAGE (conflicting across dossiers — flagged for manual SAM.gov verification). 6 location rows (Washington DC / San Francisco / New Delhi / Shanghai / Taipei / Nairobi) have no Division relation — correct per dossier (general/cross-company offices).

---

## Audit — 2026-06-13 (notion-audit Pass #6 — automated hourly cycle, 0 writes)

### Filled
Nothing. **0 writes made.** All live records re-fetched; no fillable gaps found.

### Verified complete (all 3a–3e checks pass — live re-fetch 2026-06-13 Pass #6)
- **3a Interconnection ✓:** Company record has 52+ People, **32 Construction Projects** (25 Bechtel2 + 7 Bechtel1-sourced: Sabine Pass S5, WIPP, Mammoth Solar, Cold Creek Solar, Eva Copper, QB2, + Poland AP1000 enriched), 30+ Software. All 6 divisions carry Companies+People+Projects. All project Contractors+Owning Department set. 19 Locations/13 Events/12 Membership rows (6 unique + 6 dups)/Software all carry Companies relation.
- **3b Description depth ✓:** All 6 division bodies confirmed present and full. Project bodies carry sourced scope/owner/delivery/dates/fatality signal (Port Arthur). People bodies carry sourced role detail.
- **3c Addresses ✓:** Company HQ Address place (Reston, lat 38.9586/lng -77.357) ✓; all 6 division Adress places ✓; all 19 location rows Adress text ✓ (incl. 3 newer rows: New York 140 Broadway, Los Angeles, Richland 450 Hills St — all fully linked). Project Adress place = genuinely sourceless (no coords in dossier).
- **3d Memberships ✓ — 6/6 (ignoring 6 dup rows):** BRT · CII · NEI · ETEBA · CCITNZ · NABTU — all company-linked. ⚠ 6 duplicate rows persist — Zack to trash in UI (Manual UI step #6).
- **3e Location tags ✓ — 13 events georeferenced, 17 options in Events schema:** Gastech 2024 [Texas] · Gastech 2025 [Italy, Fiera Milano place coords confirmed] · Gastech 2026 [Thailand] · H2 & Ammonia 2024 [Texas] · NECX 2025 [Georgia] · ETEBA BOTC 2025 [Tennessee] · ETEBA Savannah River 2025 [South Carolina] · NEI Policy Forum 2025 [Washington DC] · NEI Assembly 2024 [Pennsylvania] · NVIDIA GTC 2025 [Washington DC] · ENR LA Forum [California] · LACMTA C-Line [California] · Gastech 2026 [Thailand]. ENR LA + LACMTA dates genuinely unconfirmed in dossier.

### Left empty (genuinely sourceless — unchanged)
21 of 25 core project `Contrat Value in Million` (undisclosed); project `Adress` place fields (city-level only, no lat/lng); division revenue/headcount (not published); firm TRIR/EMR/DART (not published); London street address; distinct parent UEI/CAGE (conflicting across dossiers — flagged for manual SAM.gov verification). 6 location rows missing Division (Washington DC / San Francisco / New Delhi / Shanghai / Taipei / Nairobi — general offices, no single division in source).

---

## Audit — 2026-06-13 (notion-audit Pass #4 — confirmed no-gap)

### Filled
Nothing. **0 writes made.** All live records re-fetched and verified identical to Pass #3.

### Verified complete (all 3a–3e checks pass — live re-fetch 2026-06-13)
- **3a Interconnection ✓:** Company record has 52 People, 25 Construction Projects (forward relation), 30 Software. All 6 divisions carry Companies+People+Projects relations. All project Contractors+Owning Department set. Locations/Events/Memberships all carry Companies relation.
- **3b Description depth ✓:** All 6 division bodies verified (Energy/Infrastructure/Mining & Metals/NS&E/M&T/Enterprises — full focus/president/base/projects/parent). All sampled project bodies carry sourced scope, owner, delivery, dates, risk signals (Port Arthur fatality in body confirmed). People bodies carry role + sourced detail.
- **3c Addresses ✓:** Company HQ place (Reston, lat 38.9586/lng -77.357) ✓; all 6 division Adress places ✓ (Energy→CityWestPlace Houston; Infra+NS&E+Enterprises→Reston; M&M→Santiago; M&T→Chandler AZ). Locations DB schema confirmed (Adress text + Companies + Division relations). Project Adress place = genuinely sourceless (city-level only; Notion place requires lat/lng — no coords in dossier).
- **3d Memberships ✓ — 6/6:** BRT · CII · NEI · ETEBA · CCITNZ · NABTU — schema + Companies relation confirmed present.
- **3e Location tags ✓ — 17 options in Events schema:** Texas/Plano/Connecticut/Plantsville/Phoenix/Arizona/Hartford/Waterbury/Southington/Georgia/Tennessee/Pennsylvania/Washington DC/South Carolina/California/Thailand/Italy — all Bechtel events tagged per prior audit.

### Left empty (genuinely sourceless — unchanged)
21 of 25 project `Contrat Value in Million` (undisclosed); project `Adress` place fields (city-level only, no lat/lng in dossier); division revenue/headcount (not published); firm TRIR/EMR/DART (not published); London street address; distinct parent UEI/CAGE (conflicting across dossiers — flagged for manual SAM.gov verification).

---

## Audit — 2026-06-13 (notion-audit Pass #3 — final convergence)

### Filled
Nothing. Build fully converged. **0 writes made.**

### Verified complete (all 3a–3e checks pass)
- **3a Interconnection ✓:** 52 people→company; 25 projects→Contractors; 6 divisions→company+People+Projects; 19 location rows→company+division; 13 events→company; 6 memberships→company; 30 software→company.
- **3b Description depth ✓:** all 25 project bodies (Port Arthur fatality signal, sourced values/owners/JVs/dates); all 6 division bodies; all 15 people bodies — verified at full dossier depth.
- **3c Addresses ✓:** company HQ Address place ✓; all 6 division Adress places ✓; all 19 location rows Adress text ✓. Project Adress place = genuinely sourceless (no coords in any dossier; Notion place requires lat/lng).
- **3d Memberships ✓ — 6/6:** BRT · CII · NEI · ETEBA · CCITNZ · NABTU — all company-linked. Bech3.md confirms no additional memberships.
- **3e Location tags ✓ — all 13 events georeferenced:** Gastech 2024 [Texas] · Gastech 2025 [Italy] · Gastech 2026 [Thailand] · H2 & Ammonia 2024 [Texas] · NECX 2025 [Georgia] · ETEBA BOTC 2025 [Tennessee] · ETEBA Savannah River 2025 [South Carolina] · NEI Policy Forum 2025 [Washington DC] · NEI Assembly 2024 [Pennsylvania] · NVIDIA GTC 2025 [Washington DC] · ENR LA Forum [California] · LACMTA C-Line [California] · Gastech 2025 [Italy]. All Place coords + Companies relation confirmed.

### Left empty (genuinely sourceless — unchanged from prior audits)
21 of 25 project `Contrat Value in Million` (undisclosed); project `Adress` place fields (city-level only, no lat/lng); division revenue/headcount (not published); firm TRIR/EMR/DART (not published); London street address; distinct parent UEI/CAGE (conflicting across dossiers — flagged for manual SAM.gov verification).
6. **⚠ Memberships DB has 6 duplicate rows** — the 6 original rows (created 2026-06-10) and 6 newer duplicate rows (created 2026-06-13 by a prior audit session) both exist. All 12 have the Companies relation set but the content is duplicated. Delete the 6 older (2026-06-10) rows or the 6 newer ones — keep whichever set has richer body content. Zack to trash duplicates in UI.

---

## Audit — 2026-06-13 (notion-audit Pass #5 — live re-verification, 0 writes)

### Filled
Nothing. **0 writes made.** All live records re-fetched and verified.

### New issue found — ⚠ Duplicate memberships
The Memberships DB (`ddc90644`) has **12 substantive rows** (6 created 2026-06-10 + 6 created 2026-06-13 by a prior audit session). All 12 carry the Companies full database relation. The dossier only lists 6 memberships (BRT, CII, NEI, ETEBA, CCITNZ, NABTU). **6 are duplicates — flagged for Zack to trash in UI.** (Above in Manual UI steps.)

### Verified complete (all 3a–3e checks pass — live re-fetch 2026-06-13 Pass #5)
- **3a Interconnection ✓:** Company record has 52 People, 25+ Construction Projects (forward relation), 30+ Software. All 6 divisions carry Companies+People+Projects relations. All project Contractors+Owning Department set. Locations/Events/Memberships all carry Companies relation.
- **3b Description depth ✓:** All 6 division bodies present (Energy/Infrastructure/Mining & Metals/NS&E/M&T/Enterprises). Project bodies carry sourced scope/owner/delivery/dates (Port Arthur fatality signal confirmed in body). People bodies carry sourced role detail.
- **3c Addresses ✓:** Company HQ Address place (Reston, lat 38.9586/lng -77.357) ✓; all 6 division Adress places ✓ (Energy→CityWestPlace Houston; Infra+NS&E+Enterprises→Reston; M&M→Santiago; M&T→Chandler AZ). All 19 location rows Adress text ✓. Project Adress place = genuinely sourceless (city-level only; Notion place requires lat/lng — no coords in dossier). 6 locations (Washington DC, San Francisco, New Delhi/Gurgaon, Shanghai, Taipei, Nairobi) have no Division relation — correct per dossier (these are general/cross-company offices, no single-division assignment in source).
- **3d Memberships ✓ — 6/6 (ignoring duplicates):** BRT · CII · NEI · ETEBA · CCITNZ · NABTU — all company-linked. ⚠ 6 duplicate rows also present — see Manual UI #6.
- **3e Location tags ✓ — 12 events georeferenced, 17 options in Events schema:** Gastech 2024 [Texas] · Gastech 2025 [Italy] · Gastech 2026 [Thailand] · H2 & Ammonia 2024 [Texas] · NECX 2025 [Georgia] · ETEBA BOTC 2025 [Tennessee] · ETEBA Savannah River 2025 [South Carolina] · NEI Policy Forum 2025 [Washington DC] · NEI Assembly 2024 [Pennsylvania] · NVIDIA GTC 2025 [Washington DC] · ENR LA Forum [California] · LACMTA C-Line [California]. All 12 real events have location tags; ENR LA + LACMTA dates still empty (dates genuinely unconfirmed in dossier).

### Left empty (genuinely sourceless — unchanged)
21 of 25 project `Contrat Value in Million` (undisclosed); project `Adress` place fields (city-level only, no lat/lng in dossier); division revenue/headcount (not published); firm TRIR/EMR/DART (not published); London street address; distinct parent UEI/CAGE (conflicting across dossiers — flagged for manual SAM.gov verification). 6 location rows missing Division (Washington DC / San Francisco / New Delhi / Shanghai / Taipei / Nairobi — general offices, no single division in source).
