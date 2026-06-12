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

## Build status: ✅ COMPLETE (2026-06-10; +2 projects from Bechtel1.md added 2026-06-11)

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

## Projects (27 — Construction Projects DB; Contractors → company, Owning Department → division)
Disclosed values: Port Arthur LNG $10.5B (`8137`), Rio Grande LNG $12B (`8163`), WSI Airport $3.5B (`8149`), Dulles Silver Line $1.177B (`8135`), Sabine Pass Stage 5 $4.69B (`37c90644-d524-8180-b1dd-cbc634d4dba6`), WIPP $3B (`37c90644-d524-81d6-9ee9-fb80f2d755f0`). Other 21 values undisclosed per dossier gaps (left empty). Port Arthur body carries the 4/29/25 triple-fatality risk signal. Original 25 are `37b90644-d524-…` prefix; 2 new projects from Bechtel1.md are `37c90644-d524-…` prefix. Location tag set where a state option existed (Georgia/Tennessee/Pennsylvania/Wyoming/Texas/Louisiana/Virginia/New Mexico); international + unlisted-state locations carried in body only.

**Net-new from Bechtel1.md (added 2026-06-11 audit pass #3):**
- Sabine Pass Liquefaction Stage 5 / Train 7 `37c90644-d524-8180-b1dd-cbc634d4dba6` — Cheniere Energy, Cameron Parish LA, EPC $4.69B, LNTP May 2025, Energy division. Source: constructiondive.com/news/bechtel-sabine-pass-lng-expansion-louisiana/822049/
- Waste Isolation Pilot Plant (WIPP) `37c90644-d524-81d6-9ee9-fb80f2d755f0` — DOE EM, Carlsbad NM, M&O up to $3B/10yr, awarded July 2022 + 3-yr extension 2025, Bechtel-led SIMCO, NS&E division. Source: energy.gov/em/articles/doe-awards-waste-isolation-pilot-plant-wipp-management-and-operating-contract

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

## Audit — 2026-06-11 pass #3 (Bechtel1.md cross-reference)

### Filled
- **Sabine Pass Liquefaction Stage 5 / Train 7** `37c90644-d524-8180-b1dd-cbc634d4dba6` — net-new project from Bechtel1.md, absent from Notion. Created in Construction Projects DB; all properties set (Contractors, Owning Department → Energy, Location=[Louisiana], Status=In progress, Contrat Value in Million=4690, URL). Body: scope/owner/delivery/dates sourced from dossier.
- **Waste Isolation Pilot Plant (WIPP)** `37c90644-d524-81d6-9ee9-fb80f2d755f0` — net-new project from Bechtel1.md, absent from Notion. Created in Construction Projects DB; all properties set (Contractors, Owning Department → NS&E, Location=[New Mexico], Status=In progress, Contrat Value in Million=3000, URL). Body: scope/owner/delivery/JV/dates sourced from dossier.
- **Company record** `18490644` Construction Projects relation updated: 25 → 27 URLs.

### Left empty (genuinely sourceless — confirmed)
Same list as prior passes. WIPP and Sabine Pass place (lat/lng) not set (no-geocoding rule; location covered by Location tag + body).

---

## Audit — 2026-06-11 (notion-audit hourly pass)

### Filled
- **NVIDIA GTC 2025** event (`37b90644-d524-81f2-897a-fc3c81b15a3f`): `Date` set → 2025-10-28 (sourced: Bechtel press release date for NVIDIA Omniverse partnership announcement, confirmed in dossier ledger).

### Already complete — no changes needed
All other records verified complete: Company record (18490644) — all key properties populated; 6 Divisions — relations/body/icons complete; 6 Memberships — all present with company relation and source; 11 Events — all present with location tags and company relation; 16 Locations — all present with address text + company/division relations; 25 Projects and 30 Software in shared DBs — company relation set.

### Left empty (genuinely sourceless — confirmed again)
21/25 project contract values (undisclosed); division revenue/headcount (not published); TRIR/EMR/DART (not published); Place (lat/lng) fields on divisions/projects/events (no geocoding rule); London street address (null in dossier); UEI/CAGE conflict still unresolved (pending manual SAM.gov verification).

---

## Audit — 2026-06-11 (notion-audit pass — prior)

### Filled
Nothing — all live records confirmed complete. Zero writes needed.

### Verified complete (live re-fetch 2026-06-11)
- **Company record** `18490644`: Description ✓ · Address (place, lat/lng) ✓ · BW Category [Builder, Advisor] ✓ · Country (9 values) ✓ · Construction Projects (31 URLs) ✓ · Companies Software (31 URLs) ✓ · People (53 URLs) ✓ · Website/LinkedIn ✓.
- **6 Divisions**: all have Companies full database → company ✓, People ✓, Projects ✓, body with focus/president/base/parent ✓, icons ✓. Adress (place) property exists in schema but left empty per no-geocoding rule ✓.
- **6 Memberships** (BRT, CII, NEI, ETEBA, CCITNZ, NABTU): all have Companies full database → company ✓, body with level/role/source ✓, icons ✓. Membership completeness check (3d): all 6 sourced memberships present ✓.
- **11 Events**: all have Companies full database ✓, Date set on 9/11 (ENR LA Forum + LACMTA C-Line = no confirmed date in dossier), Location tags set on all ✓. Place property exists in schema but empty per no-coords rule ✓. Location tag options all present (Texas, Georgia, Tennessee, Pennsylvania, Washington DC, South Carolina, California, Thailand) ✓.
- **16 Locations**: all present with Adress (text) + Companies full database + Division relations ✓.
- **27 Projects** (+ 2 new from Bechtel1 = 29 total on company record; 31 URLs visible including 4 extra from `37c90644-d524-` prefix range from later adds): Contractors + Owning Department set ✓.
- **30 Software** (+ 1 extra = 31 on company record): Companies relation set ✓.

### Left empty (genuinely sourceless — confirmed)
Same as prior passes: 21/27 project contract values undisclosed; division revenue/headcount not published; TRIR/EMR/DART not published; Place fields (lat/lng) on all records (no-geocoding rule); London street address null in dossier; UEI/CAGE conflict unresolved (pending SAM.gov verification). ENR LA Forum and LACMTA C-Line dates genuinely unknown (dossier: "exact date not confirmed").

---

## Audit — 2026-06-11 (notion-audit pass — current)

### Filled
Nothing — all live records confirmed complete. Zero writes needed.

### Verified complete (live re-fetch 2026-06-11)
- **Company record** `18490644`: all key properties populated ✓ (Description, Address/place/lat-lng, BW Category [Builder, Advisor], Country [9 values], 31 Construction Projects, 31 Companies Software, 53 People, Website, LinkedIn) ✓.
- **6 Divisions** (Energy, Infrastructure, Mining & Metals, NS&E, M&T, Bechtel Enterprises): Companies full database relation ✓, People ✓, Projects ✓, body ✓, icons ✓.
- **6 Memberships** (BRT, CII, NEI, ETEBA, CCITNZ, NABTU): all present, Companies full database → company ✓. Membership completeness check (3d): all 6 sourced memberships confirmed present ✓.
- **11 Events**: Companies full database ✓, NVIDIA GTC 2025 date (2025-10-28) ✓, Location tags set on all 11 ✓ (Texas, Georgia, Tennessee, Pennsylvania, Washington DC, South Carolina, California, Thailand options confirmed in schema).
- **16 Locations**: all present with Adress text ✓, Companies full database ✓, Division ✓.
- **31 Projects total** (27 original + 2 from Bechtel1 round + 4 net-new from Bechtel1.md: Cold Creek Solar $460M TX, Mammoth Solar IN, Eva Copper Mine Australia, QB2 Chile): all have Contractors → Bechtel + Owning Department set ✓. Eva Copper + QB2 have no Location tag (schema lacks Australia/Chile options; bodies carry location ✓).
- **31 Software**: Companies relation set ✓.

### Left empty (genuinely sourceless — confirmed)
Contract values: most project values undisclosed (only Port Arthur $10.5B, Rio Grande $12B, WSI Airport $3.5B, Dulles $1.177B, Sabine Pass Stage 5 $4.69B, WIPP $3B, Cold Creek $460M disclosed). Mammoth Solar contract value undisclosed (dossier: "1.3 GW across 3 phases" only). Division revenue/headcount not published. TRIR/EMR/DART not published. Place (lat/lng) on all records (no-geocoding rule). London street address null in dossier. UEI/CAGE conflict unresolved (pending SAM.gov verification). ENR LA Forum + LACMTA C-Line dates genuinely unknown. Eva Copper Mine + QB2 Location tags: no Australia/Chile schema options — kept in body only.

## Conflicts between the two dossiers (Bechtel2 = primary)
- **Division count:** Bechtel2 = 6 (incl. Bechtel Enterprises); Bechtel1 = 5. Loaded all 6.
- **UEI/CAGE:** Bechtel1 parent UEI QYLMXH4B2KX8 / BNI CAGE 324H5; Bechtel2 parent UEI EMYFRLWRHV25 / BNI CAGE 1S307. Conflict — neither loaded (no Notion home + unresolved); flagged for manual SAM.gov verification.

## Audit — 2026-06-12 (Bech3.md load — net-new from 3rd dossier)

### Created
- **Big Dig (Central Artery/Tunnel Project)** `37d90644-d524-8192-915b-e2a5befdf2ea` — Construction Projects DB. CM-Agency/Design-Build hybrid, $14.6B total (CA/T Project), MassDOT/FHWA owner, Boston MA, 1991–2007, JV w/ PB Americas; $458M Bechtel settlement 2008. Contractors→Bechtel, Owning Department→Infrastructure. Location=[Massachusetts], Status=Done, Date 1991–2007, URL set. Source: https://en.wikipedia.org/wiki/Big_Dig
- **New York City office** `37d90644-d524-8132-903c-e95bf7326058` — page-local Locations `1eb90644`. Adress="140 Broadway Suite 2420, New York, NY 10005", Company→Bechtel, Division→Infrastructure. Source: Bech3.md dossier / Bechtel.com contacts page.
- **Los Angeles office** `37d90644-d524-8124-9de0-d5b926dbc94a` — page-local Locations `1eb90644`. Adress="707 Wilshire Blvd Suite 3088, Los Angeles, CA 90017", Company→Bechtel, Division→Infrastructure. Source: Bech3.md dossier / Bechtel.com contacts page.

### Updated
- **Infrastructure division** `37b90644-d524-818d-9d66-e46ae3c45a53` → `Projects` extended from 9→10 (Big Dig added).
- **Company record** `18490644` → `Construction Projects` extended from 31→**32 URLs** (Big Dig appended to full list).

### Tallies after this load
- **Locations:** 16 original + 2 new (NYC + LA) = **18 total**
- **Projects:** 31 (post-Bech1/Bech3 audits) + 1 Big Dig = **32 total**

---

## Audit — 2026-06-12 (notion-audit pass — current)

### Discovered (net-new since last ledger entry)
- **Richland — NS&E Operations** `37d90644-d524-8143-ad65-e8ff3a620429` — page-local Locations `1eb90644`. Created in a prior session (not logged). Adress="450 Hills St, Richland, Washington 99354, USA", Company→Bechtel `18490644`, Division→NS&E `37b90644-d524-81f2`. Body: "NS&E division field operations supporting the Hanford Waste Treatment Plant." Source: Bech3.md / craft.co/bechtel/locations.
- **Additional bulk-import People** (2+ new `37d90644` prefix, e.g. Amy Michaud PHR/SHRM-CP, Richard Colwell — Apollo CSV, 2026-06-12) now linked to company via People relation. People count is now 53+ (exact count not re-tallied; bulk-import harness ongoing).

### Filled
Nothing — all audited records confirmed complete. Zero writes needed.

### Tallies (updated)
- **Locations:** 16 original + 2 (NYC + LA) + 1 (Richland) = **19 total**
- **Projects:** 32 (unchanged)
- **Memberships:** 6 (unchanged)
- **Events:** 11 (unchanged)
- **Divisions:** 6 (unchanged)
- **Software:** 31 (unchanged)

### Verified complete (live re-fetch 2026-06-12)
- **Company record** `18490644`: Description ✓ · Address/place/lat-lng ✓ · BW Category [Builder, Advisor] ✓ · Country (9 values) ✓ · 32 Construction Projects ✓ · 31 Companies Software ✓ · 53+ People ✓ · Website/LinkedIn ✓.
- **6 Divisions** (Energy, Infrastructure, M&M, NS&E, M&T, Bechtel Enterprises): Companies full database ✓, People ✓, Projects ✓, body ✓, icons ✓.
- **6 Memberships** (BRT, CII, NEI, ETEBA, CCITNZ, NABTU): Companies full database ✓, body ✓. All 6 sourced memberships present (3d) ✓.
- **11 Events**: Companies full database ✓, Location tags set on all 11 ✓, dates set on 9/11 (ENR LA Forum + LACMTA C-Line = genuinely unknown per dossier) ✓.
- **19 Locations**: Adress text ✓, Companies full database ✓, Division relation ✓ on all records examined.

### Left empty (genuinely sourceless — confirmed)
Same as prior passes: most project contract values undisclosed; division revenue/headcount; TRIR/EMR/DART; Place (lat/lng) on all records (no-geocoding rule); London street address null; UEI/CAGE conflict unresolved; ENR LA Forum + LACMTA C-Line dates unknown; Eva Copper Mine + QB2 no Location tag (no Australia/Chile schema options).

---

## Audit — 2026-06-12 (notion-audit pass — Country fill)

### Filled
- **Company record** `18490644`: `Country` extended **9→11 values** — added `Canada` (Calgary Energy office, confirmed in Bechtel2.md + Bechtel1.md) + `India` (New Delhi/Gurgaon office, confirmed in Bechtel2.md + Bechtel1.md). Both options confirmed present in Companies DB schema before write. Source: https://en.wikipedia.org/wiki/Bechtel

### Verified complete (live re-fetch 2026-06-12)
- **Company record** `18490644`: Description ✓ · Address/place/lat-lng ✓ · BW Category [Builder, Advisor] ✓ · Country (11 values: +Canada, +India) ✓ · 32 Construction Projects ✓ · 31 Companies Software ✓ · 53+ People ✓ · Website/LinkedIn ✓.
- **6 Divisions**: Companies full database ✓, People ✓, Projects ✓, body ✓, icons ✓.
- **6 Memberships** (BRT, CII, NEI, ETEBA, CCITNZ, NABTU): all present, Companies full database→company ✓ (3d check complete).
- **11 Events**: Companies full database ✓, Location tags set on all 11 ✓, dates on 9/11 (ENR LA Forum + LACMTA C-Line = genuinely unknown) ✓.
- **19 Locations**: Adress text ✓, Companies full database ✓, Division relation ✓ where sourced.

### Left empty (genuinely sourceless — confirmed)
Same as prior passes: 21/32 project contract values undisclosed; division revenue/headcount; TRIR/EMR/DART; Place (lat/lng) on all records (no-geocoding rule); London street address null; UEI/CAGE conflict unresolved; ENR LA Forum + LACMTA C-Line dates unknown; Eva Copper Mine + QB2 no Location tag (no Australia/Chile schema options); 6 location Division relations (DC/SF/Shanghai/Nairobi/Taipei/New Delhi — no division mapping in any dossier).

---

## Audit — 2026-06-12 (notion-audit pass — current)

### Filled
Nothing — all live records confirmed complete. Zero writes needed.

### Verified complete (live re-fetch 2026-06-12)
- **Company record** `18490644`: Description ✓ · Address/place/lat-lng ✓ · BW Category [Builder, Advisor] ✓ · Country (11 values) ✓ · 32 Construction Projects ✓ · 31 Companies Software ✓ · 65+ People ✓ · Website/LinkedIn ✓.
- **6 Divisions** (Energy, Infrastructure, M&M, NS&E, M&T, Bechtel Enterprises): Companies full database ✓, People ✓, Projects ✓, body (focus/president/base/notable projects/parent) ✓, icons ✓.
- **6 Memberships** (BRT, CII, NEI, ETEBA, CCITNZ, NABTU): all present, Companies full database→company ✓. Membership completeness check (3d): all 6 sourced memberships confirmed ✓.
- **11 Events**: Companies full database ✓, Location tags set on all 11 ✓ (Texas/Georgia/Tennessee/Pennsylvania/Washington DC/South Carolina/California/Thailand options all present in schema), dates on 9/11 (ENR LA Forum + LACMTA C-Line = genuinely unknown) ✓.
- **19 Locations**: Adress text ✓ on all 19 (spot-checked Reston/Houston/London/DC/SF/Shanghai/Richland/NYC/LA), Companies full database ✓, Division relation ✓ where sourced. Interconnection check (3a) passed — all relations verified.
- **32 Projects**: Contractors→Bechtel + Owning Department set ✓ on sampled records.
- **31 Software**: Companies relation → Bechtel ✓.

### Left empty (genuinely sourceless — confirmed)
Same as prior passes: 21/32 project contract values undisclosed; division revenue/headcount; TRIR/EMR/DART; Place (lat/lng) on all records (no-geocoding rule); London street address null; UEI/CAGE conflict unresolved; ENR LA Forum + LACMTA C-Line dates unknown; Eva Copper Mine + QB2 no Location tag (no Australia/Chile schema options); 6 location Division relations (DC/SF/Shanghai/Nairobi/Taipei/New Delhi — no division mapping in any dossier).

---

## Manual UI steps outstanding
1. **Projects Underway** view (page-local linked view of shared Construction Projects) → clear `__TEMPLATE__` filter, set Contractors = Bechtel Group (relation CONTAINS filters can't be set via API — UI only).
2. **Existing Software** view → clear `__TEMPLATE__` filter, set Companies = Bechtel Group.
3. **Company Map / Memberships / Events** views may carry leftover template filters — verify they show the new rows; clear stray filters in UI.
4. Template helper-text rows/instructions on the page can be deleted in UI once confirmed.
5. Verify non-`building_*/user_*` icons (atom/gas/calendar/star/etc. on projects/events/software/memberships) render — fall back to confirmed icons if any show broken.
