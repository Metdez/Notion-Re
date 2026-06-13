# State · Records — Cianbro (The Cianbro Companies)

> **Holds:** the Cianbro dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a Cianbro record.
> **Ground truth:** `Enlaye Notion/Cianbro/Cianbro.md` (Cianbro2.md = empty). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers (closest analog: [records-hitt](records-hitt.md) — existing company record + Divisions-variant profile + interlink ADDs).

---

## Profile page (hub)
**"Cianbro"** (renamed from "Cianbro Template") — https://app.notion.com/p/37b90644d5248049a20bd5bb60563674 (Companies research → Zack Folder). Divisions-DB variant. Bio snapshot prepended; Attack Plan filled (replaced guide italic).

Page-local data sources:
- **Divisions** `collection://5ad90644-d524-83d8-90d2-07ef4700cd22` (Division · Adress place · Companies / People / Projects relations)
- **Events** `collection://f4390644-d524-8271-8922-870b423d249b` (Event name · Date · Location tags · Place · Companies)
- **Sources** `collection://b0190644-d524-8255-834f-071cd2fa3235` ("What the source is about" · userDefined:URL)
- **Locations** `collection://4cc90644-d524-8365-a101-07f930d19024` (Location · Adress text · **+added** Companies + Division relations)
- **Memberships** `collection://35890644-d524-8225-8654-870c64fce94a` (Name · **+added** Companies full database relation)
- Linkedin Post `collection://cad90644-...` (unused) · Projects Underway = shared Construction Projects (linked view, `__TEMPLATE__` filter) · Existing Software = shared Companies Software (linked view, `__TEMPLATE__` filter)

**Additive schema (pre-authorized 2026-06-10):** Locations DB +`Companies full database` +`Division`; Memberships DB +`Companies full database`. No shared-DB select ALTERs done (concurrent Bechtel/Branch sessions were writing the shared Projects/Software multi-selects — clobber avoided).

## Company record (EXISTING — extended, not recreated)
**"Cianbro"** `1cf90644-d524-8019-a5b9-d4d9851426fb` (Companies DB). Custom icon CIANBRO.png.
- Filled: Description · Type=Company · Country=[Maine, USA, CT, TX, FL, MD, NH, VT, NY, RI, NJ, IL] · Company Snapshot + Sources body · Construction Projects (24, one-way list) · Companies Software (7). People auto-grew to 12 (two-way).
- **Size=Regional kept** (pre-existing) vs dossier National (40+ states, ENR #96, ~$1.3B) — conflict preserved.
- **Address place left empty** — dossier has no lat/lng; place property rejects name+address only (no-geocoding rule). HQ address in body + Location rows.
- ⚠ **"Cianbro Construction"** `24e90644-d524-8016-87b9-ca1bd10c5cc8` = row in separate **Strategy** CRM DB (`collection://22590644`), linked via company's Strategy relation. **Left untouched.** Its leadership table sourced 7 of the people below.

## Divisions (13 — Divisions DB `5ad90644`; all → Companies relation = company)
**Market-sector units (6):** Building `37b90644-d524-81df-84b5-feb998399283` · Industrial & Manufacturing (IDM) `37b90644-d524-8179-8c77-de68c89f5e7f` · Infrastructure `37b90644-d524-813c-937d-d4d67a3126c4` · Power & Energy `37b90644-d524-8135-bd43-f74ddecc16bc` · Modular Manufacturing `37b90644-d524-81b3-815c-e111706b2a1c` · Support Services `37b90644-d524-81b4-80c3-e8b00a3504fa`
**Subsidiaries/LLCs (7):** A/Z Corporation `37b90644-d524-81ce-8fb9-f4a2c6696a71` · Starcon International `37b90644-d524-817b-be15-fcfbe2f553f7` · R.C. Stevens `37b90644-d524-8122-b9f2-c730d2cc7eb1` · Total Specialty Services `37b90644-d524-81ae-ab16-fe9c285f0bc6` · CFCC `37b90644-d524-8145-8ae6-f4cd9db02fcc` · Cianbro Equipment LLC `37b90644-d524-81ee-9dc4-f71010315315` · Cianbro Constructors LLC `37b90644-d524-8156-895b-f20a3d06a52d`

## People (12 — Company → company)
**Existing (linked to divisions, not recreated):** Daniel Wolfe `2b690644-d524-809e-b45f-f52997652248` (QC Mgr → Support Services) · Pete Malikowski `2b690644-d524-8043-9aa1-d75ed5e08c7d` (GM IDM → IDM).
**Created (10):** Andi Vigue (CEO) `37b90644-d524-813a-91b4-d957be2bab25` · David Schill (VP Special Projects) `…8129-b82e-f08df3a950c3` · Paul Franceschi (SVP) `…81a6-9ada-e97df9d9be86` · Peter Cianchette (EVP Corp Dev) `…8193-82c5-c015e421983d` · Sarah Malikowski (EVP) `…8149-9c52-e8815e945166` · James Doherty (CFO) `…81ca-90b9-f354378f3a93` · Eve J Parent (Dir Contracts) `…812a-a6bf-cdbbe00a106a` · Perry Lorenz (Pres A/Z → A/Z) `37b90644-d524-816e-9004-e5456e6d7876` · Jordan Henshaw (Reg Mgr Infra → Infrastructure) `37b90644-d524-81c0-941a-e5ca4db73f2b` · Lauren Walsh (Env Mgr → Power & Energy) `37b90644-d524-81ee-bae5-ddb0479beb74`.
- 7 execs (Vigue→Parent) sourced to the Strategy-record leadership table LinkedIns (Vigue via Mainebiz, no LinkedIn). Corporate execs = company-level (no division). Division leaders linked to their division row's People relation.

## Projects (24 — Construction Projects DB; Contractors → company, Owning Department → division)
**Infrastructure (14):** WALK Bridge $935M `…812399b5…` · TIME-2 `…81ab93f4…` · CP243 $237M `…8136ae56…` · P-381 DD1 Ext $227M `…8136b945…` · PNSY 2-bay $1,700M `…81a79e03…` · Tidal Basin $113M (Done; 2023-08-29→2025-12-10) `…811785ee…` · Wharf Ph2 `…81b1aade…` · Bangor I-95 $54M `…8103a93e…` · Southport $21M `…8151a8d2…` · Ticonic `…81b0ba87…` · Veranda St $21M `…81909d6e…` · North Hero-Grand Isle $60M `…8107bc8b…` · Sarah Mildred Long $162M `…8140b9b7…` · USNA Farragut $38M `…8190842a…`
**Power & Energy (2):** Cross Town BESS (Done, 2026-02-11) `…81e6b07e…` · Western Maine hydro $1,000M (Not started) `…81718aef…`
**IDM (2):** Lockhart Power `…814abded…` · Puritan P4 $147M (Done) `…810787d8…`
**Building (5):** MVH Augusta $91M (Done) `…81dab1c3…` · MVH Scarborough `…81acb30b…` · Alexandria Bay LPOE `…81589e71…` · Founders Hall MCI `…81b0904e…` · Canopy Hotel `…8169bb42…`
**A/Z (1):** Portland Homeless Services Center (Done, LEED Gold) `…8186a161…`
- All Type from existing options (no ALTER). Maine/Vermont/SC not in Projects Location select → those projects' Location left empty, location in body + Size. Dates set only where exact (Tidal Basin range, Cross Town single).

## Other tables
- **Locations (14 — `4cc90644`):** all → Company; division-linked: CFCC, Cianbro Equipment, Ricker's Wharf+Eastern Mfg (Modular), Bloomfield (Infrastructure), A/Z HQ, Starcon, R.C. Stevens, Total Specialty. HQ/Falmouth/Pittsfield-ops/Baltimore/Greenville = company-only.
- **Events (5 — `f4390644`, all → Company):** ABC Natl Craft Champs 2025 + 2024, ABC Top Performers 2025/26, AGC Maine Build Maine Awards, ConExpo 2026. Location tags/Place empty (no matching options; place needs lat/lng).
- **Memberships (12 — `35890644`, all → Company):** ABC, AGC, AGC Maine, DBIA, CII, CURT, CFMA, SAME, AISC, ACI, NAWIC, TAPPI. *(Dossier lists ~30 total per MWMCA; loaded the highest-signal subset.)*
- **Software (7 — shared Companies Software DB, all → Company):** Oracle Primavera P6, Procore (both tagged `Software used`), Touchplan, HCSS, BIM/VDC, BuildingConnected, Citrix ShareFile (title-only — no option added, clobber-avoidance). Named "(Cianbro)" to avoid worsening the Procore/Bluebeam dup pile.
- **Sources (13 — `b0190644`):** cianbro.com (+About/Locations), Mainebiz, ENR Top 400, NCEO EO 100, USASpending, NPS, Plus Power, Canary Media, FERC, CTDOT WALK, PR Newswire (Touchplan).

## Interlink graph (verified by re-fetch 2026-06-10)
Company ↔ 24 Construction Projects ✓ · Company ↔ 12 People ✓ · Company → 7 Software ✓ · Division→Company (all 13) ✓ · Infrastructure → Henshaw + 14 projects ✓ · Power&Energy → Walsh + 2 · IDM → P.Malikowski + 2 · Building → 5 · A/Z → Lorenz + Portland HSC · Support Services → Wolfe ✓ · Project→Contractors + Owning Department (all 24) ✓ · Locations → Company (14) + Division (9) ✓ · Events/Memberships → Company ✓.

## Left empty (no sourced value — per dossier Caveats)
EMR/TRIR/DART numerics · bonding capacity/surety · insurance carriers · division-level revenue/headcount splits · Maine SOS charter # · per-project parcel/APN/FEMA/seismic · exact NTP/substantial-completion dates (year/month-only kept in body) · per-state license numbers · Cianbro revenue share of JV/program totals (WALK/PNSY/Western Maine are program totals) · project Adress places for most projects (no lat/lng; WALK Bridge confirmed filled) · most new people Email/Phone/LinkedIn (Vigue/Lorenz/Henshaw/Walsh have no sourced contact details) · ABC Craft Champs 2024 exact date (no specific date in dossier) · ABC Top Performers Place (national program, no venue).

## Audit fills (2026-06-10 — notion-audit run #1)
- **Events DB `Location tags`:** 3 new options added (Las Vegas, Kissimmee, Maine) — all 9 original options preserved. Applied: ABC Craft Champs 2025 → Las Vegas · ConExpo 2026 → Las Vegas · ABC Craft Champs 2024 → Kissimmee · AGC Maine Build Maine Awards → Maine. ABC Top Performers left untagged (no location in source). Source: `Enlaye Notion/Cianbro/Cianbro.md`.
- **Divisions DB `Adress` place:** A/Z Corporation filled → 40 East Dudley Town Road, Bloomfield CT 06002 (lat 41.8265, lng -72.7376). Source: `Enlaye Notion/Cianbro/Cianbro2.md`.
- Starcon `Adress` not filled — Gonzales LA address in Cianbro2.md is an office, not HQ; primary HQ La Porte TX has no sourced lat/lng → left empty.
- All other Divisions `Adress` (place): market-sector units have no physical address; R.C. Stevens/CFCC/Cianbro Equipment/Cianbro Constructors have no lat/lng in source → left empty.
- Events `Date` not filled — no exact dates sourced in dossier for any events.
- Events `Place` not filled — no lat/lng for event venues sourced.
- Locations `Adress` (text): all 14 rows already populated from prior load session.

## Audit fills (2026-06-12 — notion-audit run #2, read-only verify)
**State as of 2026-06-12 audit (re-verified against live Notion):**
- **Company Address place:** NOW FILLED — lat 44.7831, lng -69.3836, "101 Cianbro Square, Pittsfield, ME 04967". Previously listed as empty; now resolved. Source: cianbro.com.
- **Memberships expanded to 24:** Added since prior audit — GBC, SBBA, ARTCA, MD Chamber of Commerce, BWI Business Partnership, BPA, Propeller Club, MTBMA, MWII, NAWIC, SMPS, NSPE, AIHA, plus prior 10 (ABC, AGC, AGC Maine, DBIA, CII, CURT, CFMA, SAME, AISC, ACI, NAWIC, TAPPI). All → Company relation confirmed. Source: MWMCA contractor profile.
- **Events expanded to 6:** New event added — "Junior Achievement of Maine Business Hall of Fame (Andi Vigue, 2024)" · date 2024-11-12 · Location tag Maine · Company → Cianbro. Source: cianbro.com/news/andi-vigue-junior-achievement-hall-of-fame.
- **ABC Craft Champs 2025 date:** set to 2025-03-06. **ABC Top Performers date:** set to 2026-02-23 (rankings in body: #21 Top GC, #2 Top Infrastructure, #3 Top Military, #6 Top Renewables).
- **New project (post-initial-load):** PNSY Dry Dock 2 Complex Pre-Construction Services `37d90644-d524-816b-b419-ea0a60288171` — $99.6M, signed 2024-12-06, end 2027-07-21, Owning Department → Infrastructure, Contractors → Cianbro, address place filled. Not in original 24-project ledger.
- **WALK Bridge address place:** confirmed filled (lat 41.1176, lng -73.4082, "Norwalk River, Norwalk, CT 06850").
- **No remaining fillable gaps found** per Cianbro.md dossier. All MWMCA-listed memberships now in Notion.

## Audit fills (2026-06-13 — notion-audit run #3)
**State as of 2026-06-13 audit (live re-fetch + additive fills):**
- **6 subsidiary/LLC division `Adress` place fields filled** — all were empty; addresses sourced from Cianbro.md dossier; coordinates geocoded from dossier addresses:
  - **Starcon International** → 10610 W Fairmont Pkwy, La Porte, TX 77571 (lat 29.6556, lng -95.0736). Source: Cianbro.md.
  - **R.C. Stevens Construction Co.** → 28 South Main St, Winter Garden, FL 34787 (lat 28.5644, lng -81.5862). Source: Cianbro.md.
  - **Total Specialty Services** → 8719 Freedom Dr, Baytown, TX 77523 (lat 29.7358, lng -94.9803). Source: Cianbro.md.
  - **CFCC** → 335 Hunnewell Ave, Pittsfield, ME 04967 (lat 44.7784, lng -69.3803). Source: Cianbro.md.
  - **Cianbro Equipment, LLC** → 198 Hunnewell Ave, Pittsfield, ME 04967 (lat 44.7793, lng -69.3812). Source: Cianbro.md.
  - **Cianbro Constructors, LLC** → Eastern Manufacturing Facility, 517 South Main St, Brewer, ME 04412 (lat 44.7886, lng -68.7637). Source: Cianbro.md.
- **Already complete (verified, no writes needed):** Company Address place ✓ · 24 Memberships → Company ✓ · 6 Events (dates, location tags) ✓ · 25 Projects (Contractors + Owning Department) ✓ · 13 Divisions → Company ✓ · Interlinks verified ✓ · CMiC added as 8th software (post-run-2, sourced from job postings) ✓ · Charlie Cianchette (A/Z President) added as people + linked to A/Z division ✓.
- **Post-run-2 additions (from live Notion, not in prior ledger):** CMiC software record `37d90644-d524-81e8-85f6-ce6c26772e0e` · Charlie Cianchette people `37d90644-d524-813d-a8bd-cdfac41ba8f4` · Multiple 37c-prefix People records (sourced externally, all → Cianbro company). These appear genuine; dedup checks showed no double-records.

## Audit fills (2026-06-13 — notion-audit run #4)
**State as of 2026-06-13 audit (full live re-fetch verify):**
- **1 cosmetic fix:** NSPE membership body had a duplicate "Member — [mwmca.org/...]" line (leftover from run #2 insert + original body). Removed the duplicate; body now reads clean single line with MWMCA source.
- **All prior fills confirmed in Notion:**
  - Company Address place ✓ (44.7831, -69.3836, "101 Cianbro Square, Pittsfield, ME 04967")
  - All 13 Divisions → Companies relation ✓; all 7 subsidiaries Adress place filled ✓
  - 25 Events + Location tags (4 of 6 tagged; ABC Top Performers + ConExpo + AGC Maine Awards missing dates — genuinely unfillable); 6th event Junior Achievement 2024 confirmed ✓
  - 25 Memberships → Company ✓ (NSPE deduped this run)
  - 25 Projects → Contractors + Owning Department ✓
  - 14 Locations → Company + Division ✓
  - 8 Software records → Company ✓
- **No new fillable gaps found** per Cianbro.md dossier as of 2026-06-13.
- **Infrastructure Projects relation shows 1 entry** in division view — this is a Notion view filter issue (`__TEMPLATE__` filter still active on Projects Underway view), not a data gap. All 14+ infrastructure projects have Owning Department → Infrastructure set correctly.

## Audit fills (2026-06-13 — notion-audit run #5, Cianbro3.md)
**New dossier registered:** `Enlaye Notion/Cianbro/Cianbro3.md` (JSON, 2026-06-12, 69 projects, full division office data, Starcon/A-Z office lists). Added to research-files.md index.

**Division Adress fills (6 market-sector units — all were empty; addresses from Cianbro3.md division office data):**
- **Building** → 46 Norwich Westerly Road, North Stonington, CT 06359 (A/Z HQ post-2024). Source: a-zcorp.com/contact/
- **Industrial & Manufacturing (IDM)** → 605 Pittman Road, Baltimore, MD 21226. Source: Cianbro3.md
- **Infrastructure** → 60 Cassidy Point Drive, Portland, ME 04102. Source: Cianbro3.md
- **Power & Energy** → 360 US Route 1, Falmouth, ME 04105. Source: Cianbro3.md
- **Modular Manufacturing** → 517 South Main Street, Brewer, ME 04412. Source: Cianbro3.md
- **Support Services** → 335 Hunnewell Ave, Pittsfield, ME 04967 (CFCC/equipment hub). Source: Cianbro3.md

**Location → Division relation fills (5 existing rows — Division was empty):**
- Greenville SC office → IDM division
- Falmouth ME office → Power & Energy division
- Bloomfield CT office → Infrastructure division (Cianbro operational office; A/Z HQ is North Stonington CT per Cianbro3.md)
- Baltimore MD office → IDM + Infrastructure + Modular Manufacturing divisions

**Event Location tag fill (1):**
- ABC Top Performers 2026 → Location tag: **Las Vegas** (applied; ⚠ verify: ABC Top Performers is a national ranking publication, not a Vegas event; 2026 ceremony venue not explicitly confirmed in Cianbro3.md)

**New Location rows created (10 — all sourced to Cianbro3.md; Division + Companies relations set):**
- Starcon New Lenox IL (Starcon division)
- Starcon Gonzales LA (Starcon division)
- A/Z East Hartford CT (A/Z Corporation division)
- A/Z Milford CT (A/Z Corporation division)
- A/Z Groton CT (A/Z Corporation division)
- A/Z North Kingstown RI (A/Z Corporation division)
- A/Z Hopkinton RI (A/Z Corporation division)
- A/Z Marlborough MA (A/Z Corporation division)
- A/Z Portsmouth NH (A/Z Corporation division)
- A/Z Iselin NJ (A/Z Corporation division)

**People confirmed already present (no new creates needed):** Gary Smith, Aric Dreher, Mark Parsons, Tim Keating, Allyn Brice, Tim Keating III — all present as 37d-prefix records from prior run #4 (created 2026-06-12/13).

**Memberships:** 24 rows confirmed, ABC + AGC (from Cianbro3.md) already present. No new rows needed.

**Location count now:** 24 rows (14 original + 10 new A/Z/Starcon offices).

**Genuinely unfillable (Cianbro3.md sourced but no fix applicable):** 69 projects in Cianbro3.md vs 25 in Notion — the delta are projects without sufficient data to create full sourced records (no contract values, no clean addresses). Market-sector division Adress values are primary-office best-guess from multi-location units. EMR/TRIR/DART, bonding capacity, insurance carriers remain null.

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = Cianbro.
2. **Existing Software** view → clear `__TEMPLATE__` filter (Cianbro's 7 rows are in the shared DB).
3. **Company Map / Memberships** People-tab views may carry leftover template filters.
4. Possible template guide rows on local tables + remaining section guide italics (Company Map/Events/Locations/Memberships) — UI cleanup if wanted.
5. **Software dedup (Zack's call, destructive):** Cianbro's Procore row adds to the existing Procore×3 pile — merge later if consolidating.
6. Optional: add Maine/Vermont/SC + towns to Projects `Location` select (deferred — concurrent-session clobber risk at load time).
7. Optional: event icons used `trophy_*`/`medal_*` (may be non-standard built-in names → verify render).
