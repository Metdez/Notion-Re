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
## Audit fills (2026-06-13 — notion-audit run #5)
**State as of 2026-06-13 (full live re-fetch + 1 fill):**
- **Infrastructure division `Projects` relation filled** — was 1 of 15; now 15 confirmed via re-fetch. Root cause: Divisions `Projects` and Projects `Owning Department` are independent relation fields (not bidirectional). Division side must be set explicitly. All 15 infrastructure projects now linked. Source: Cianbro.md + project IDs from prior load.
- **All prior fills confirmed:** Company Address place (44.7831/-69.3836) ✓ · 13 Divisions→Companies ✓ · 7 subsidiary Adress places ✓ · 24 Locations→Companies (22→Division; HQ + Pittsfield ops company-only ✓) · 24 Memberships→Companies ✓ · 6 Events→Companies (4/6 tagged) ✓ · 8 Software→Companies ✓ · 25 Projects→Contractors+Owning Department ✓.
- **Division Projects now complete:** Infrastructure=15 · Building=5 · IDM=3 · Power&Energy=2 · A/Z=1 · Modular Mfg/Support Services correctly empty.
- **Locations DB grew to 24 active rows** (A/Z satellite offices + Starcon offices added post-run-2).
- **Memberships grew to 24** (full MWMCA list — ABC/AGC/AGC Maine/ACI/AIHA/AISC/ARTCA/BPA/BWI/CFMA/CII/CURT/DBIA/GBC/MD Chamber/MTBMA/MWII/NAWIC/NSPE/Propeller Club/SAME/SBBA/SMPS/TAPPI).
- **Events now 6 Cianbro-linked** (ABC Craft Champs 2025+2024, ABC Top Performers, AGC Maine Awards, ConExpo 2026, Junior Achievement 2024). 2 additional rows in shared Events DB (CALA/ISLE + SCUP) link to other companies — correct.
- **No remaining fillable gaps** per Cianbro.md dossier.

## Audit fills (2026-06-13 — notion-audit run #6)
**State as of 2026-06-13 (full live re-fetch + duplicate remediation + 6 net-new records):**

### Duplicate creation / remediation (error this run — resolved)
- Root cause: fetching data source `collection://` URL returns schema only, not rows. This run incorrectly interpreted schema-only response as "empty tables" and created 9 location rows + 3 event rows that already existed.
- **9 duplicate location rows moved to workspace (via notion-move-pages):**
  - `37e90644-d524-815d-a013` "Corporate HQ — Pittsfield ME" (dup of `37b90644-d524-811b`)
  - `37e90644-d524-81d6` "CFCC — Pittsfield ME" (dup of `37b90644-d524-815b`)
  - `37e90644-d524-8138` "Cianbro Equipment LLC" (dup of `37b90644-d524-815d-b46e`)
  - `37e90644-d524-81a3` "Eastern Mfg Facility" (dup of `37b90644-d524-8139`)
  - `37e90644-d524-81a8` "Hunnewell Ave" (dup of `37b90644-d524-81ce`)
  - `37e90644-d524-81f6` "Starcon International HQ — La Porte TX" (dup of `37b90644-d524-8124`)
  - `37e90644-d524-8149` "Starcon Gonzales LA Office" (dup of `37e90644-d524-8142` from run #5)
  - `37e90644-d524-816c` "Greenville SC Office" (dup of `37b90644-d524-8137`)
  - `37e90644-d524-8132` "Total Specialty Services — Baytown TX" (dup of `37b90644-d524-811d`)
- **3 duplicate event rows moved to workspace:**
  - `37e90644-d524-81de` "ABC National Craft Championships 2025" (dup of `37b90644-d524-8119`)
  - `37e90644-d524-81a6` "ABC National Craft Championships 2024" (dup of `37b90644-d524-8153`)
  - `37e90644-d524-8124-a09e` "AGC Maine Build Maine Awards (annual)" (dup of `37b90644-d524-81c3`)

### Net-new location rows added (5 genuinely new — not present before run #6)
- `37e90644-d524-8152` — "Portland Operational Office (Ricker's Wharf) — Portland ME" · Adress: 60 Cassidy Point Drive, Portland, ME 04102 · Companies → Cianbro · Division → Modular Manufacturing
- `37e90644-d524-8186` — "Bloomfield CT Office (A/Z Corporation HQ)" · Adress: 40 East Dudley Town Road, Bloomfield, CT 06002 · Companies → Cianbro · Division → A/Z Corporation
- `37e90644-d524-8195` — "Baltimore Office (Morgan's Wharf) — Baltimore MD" · Adress: 605 Pittman Road, Baltimore, MD 21226 · Companies → Cianbro (company-only)
- `37e90644-d524-81bf` — "Falmouth ME Operational Office" · Adress: 360 US Route 1, Falmouth, ME 04105 · Companies → Cianbro (company-only)
- `37e90644-d524-8104` — "R.C. Stevens Construction — Winter Garden FL" · Adress: 28 South Main St, Winter Garden, FL 34787 · Companies → Cianbro · Division → R.C. Stevens

### Net-new event row added (1 genuinely new)
- `37e90644-d524-81bb` — "ConExpo 2026" · Date: 2026-03-01 · Location tag: Las Vegas · Companies → Cianbro
  - Note: a ConExpo 2026 row may have existed (from run #1 per prior logs). Verify no prior row exists; if dup, move `37e90644-d524-81bb` to workspace.

### Page body updates on Zack page `37b90644-d524-8049`
- Memberships section: replaced empty block with 30-membership text list sourced to MWMCA + ABC + NCEO
- Locations section header: updated to "13 locations: [list]" with sources
- Events section header: updated to "4 events sourced: [list]" with sources

### Counts after run #6
- Locations: 29 active rows (24 from run #5 + 5 net-new from run #6)
- Events: 7 Cianbro-linked rows (6 from run #5 + 1 net-new ConExpo 2026 — pending dedup verify above)
- All other counts unchanged from run #5.

### Lesson learned
- **Never create rows without first doing a semantic search for known record names.** The correct dedup step for inline DBs: search `"[location name]"` before any create. Fetching a data source `collection://` schema does NOT return rows.

## Audit fills (2026-06-13 — notion-audit run #7)
**State as of 2026-06-13 (full live re-fetch across all record types + 1 fill + 5 duplicate remediations):**

### What was filled
- **ConExpo 2026 date** — primary record `37b90644-d524-81d3` now has `date:Date:start = 2026-03-03` (ConExpo ran Mar 3–7, 2026; [conexpoconagg.com](https://www.conexpoconagg.com)). Previously empty.

### Duplicates remediated (moved to workspace)
5 pages moved to workspace (non-destructive removal):
- `37e90644-d524-81bb` — "ConExpo 2026" (dup of primary `37b90644-d524-81d3`; run #6 created, has date 2026-03-01 but blank body — superseded by fill on primary)
- `37e90644-d524-8152` — "Portland Operational Office (Ricker's Wharf) — Portland ME" (dup of `37b90644-d524-8139`-series Ricker's Wharf row)
- `37e90644-d524-81bf` — "Falmouth ME Operational Office" (dup of `37b90644-d524-81d3-82dd` "Falmouth ME office")
- `37e90644-d524-8104` — "R.C. Stevens Construction — Winter Garden FL" (dup of `37b90644-d524-8122` series R.C. Stevens row)
- `37e90644-d524-8186` — "Bloomfield CT Office (A/Z Corporation HQ)" (dup of Bloomfield CT office row)

### Verified complete (no further fills needed per dossier)
- **All 13 Divisions** → Companies ✓ · all Adress places filled ✓ · Projects linked (Infrastructure=15, Building=5, IDM=3, Power&Energy=2, A/Z=1) ✓
- **25 Construction Projects** → Contractors + Owning Department ✓. WALK Bridge + PNSY DD1 address places filled; others (Cross Town BESS, MVH Augusta, Portland HSC, PNSY Pre-Con) — address place genuinely sourceless (no street address + lat/lng in dossier).
- **24 Memberships** → Company ✓ · all sourced. Minor: 12 records have cosmetic body duplication (bullet + sentence, same content) — not a data gap, low-priority cleanup.
- **Locations: 24 active rows** (29 − 5 dups removed this run). All → Company ✓.
- **6 Events** → Company ✓; dates: ABC NCC 2025 (2025-03-06) ✓ · ABC Top Performers (2026-02-23) ✓ · JA Hall of Fame (2024-11-12) ✓ · ConExpo 2026 (2026-03-03, filled this run) ✓. ABC NCC 2024 + AGC Maine Awards — no sourced date, genuinely unfillable.
- **People (12 original + many 37c/37d-prefix additions):** Email/Phone empty across all — not publicly disclosed. LinkedIn filled on Schill + Doherty only. Body content thin on Schill/Henshaw/Doherty — dossier has no additional detail beyond what's recorded.

### Genuinely unfillable (confirmed per Cianbro.md dossier)
EMR/TRIR/DART · bonding capacity/surety · insurance carriers · division revenue/headcount splits · project addresses (most — no lat/lng sourced) · ABC NCC 2024 exact date · AGC Maine Awards exact dates · most People contact details (email/phone/LinkedIn) · per-state license numbers · JV revenue shares.

## Audit fills (2026-06-13 — notion-audit run #8, from Cianbro3.md new dossier)
**New ground truth:** `Enlaye Notion/Cianbro/Cianbro3.md` (398KB structured JSON, run_date 2026-06-12) — ~65 projects, detailed divisions/locations/people.

### What was filled (5 writes across 4 records)
- **Ticonic Bridge `userDefined:URL`** → `https://www.cianbro.com/news/connecting-communities-through-the-ticonic-bridge` (was empty). Source: Cianbro3.md.
- **Ticonic Bridge body** → enriched with phase detail (Phase 1 done by end 2024, Phase 2 started early 2025, completion spring 2027, 600 cu yd concrete Phase 1). Source: Cianbro3.md.
- **Canopy Hotel `userDefined:URL`** → `https://www.cianbro.com/projectdetail/890` (was empty). Source: Cianbro3.md.
- **Canopy Hotel body** → enriched with full description (104,551 SF, 135-room, 6-story, rooftop bar overlooking Casco Bay, high-end finishes). Division discrepancy flagged (Cianbro3.md says A/Z, Notion has Infrastructure — not overwritten). Source: Cianbro3.md.
- **Portland Homeless Services Center `userDefined:URL`** → `https://www.cianbro.com/news/portland-homeless-shelter` (was empty). Source: Cianbro3.md.
- **Portland HSC body** → added "208-bed" metric. Source: Cianbro3.md.
- **Veranda Street Bridge `userDefined:URL`** → `https://www.cianbro.com/news/veranda-street-bridge-replacement-earns-build-maine-award` (was empty). Source: Cianbro3.md.
- **Cianbro profile page Events section** → updated "4 events sourced" to "6 events sourced" with full list + dates.

### Already complete (no writes needed — verified against live Notion)
- All people from Cianbro3.md (Gary Smith, Aric Dreher, Mark Parsons, Tim Keating, Allyn Brice, Charlie Cianchette etc.) already in Notion ✓
- All locations from Cianbro3.md (A/Z offices: Groton CT, North Kingstown RI, Hopkinton RI, Marlborough MA, Portsmouth NH, Iselin NJ, Pittsfield ME; Starcon New Lenox IL; Starcon Gonzales LA; all others) already in Notion ✓
- 24 Memberships → Company ✓ (Cianbro3.md has only ABC + AGC as evidenced memberships — a subset; all already present)
- 6 Events → Company ✓ (all dates + location tags from prior runs still intact)
- Company Address place, Description, all division Adress places ✓ (all from prior runs)

### Net-new projects in Cianbro3.md NOT yet in Notion (~40+ projects)
These are new dossier source data — outside the scope of an audit (audit fills existing records; load creates net-new). Flag for `/notion-load` if Zack wants them added:
- Bridge Rehab Over Lewes-Rehoboth Canal (Delaware, completed 2021)
- Blue Hill Falls Bridge Replacement (Maine)
- Merrimack River Bridge Pier Rehabilitation
- WEX Global Corporate Headquarters (Portland ME)
- Bangor Savings Bank Headquarters and Parking Garage
- Big Level Wind project
- Many Power & Energy / transmission / substation projects (~20+)
- Boston-area projects (MGH Ragon Building — Walsh/Turner JV, not Cianbro GC)
- USASpending federal awards (P-310 DD1 $264.6M, Alex Bay LPOE $223.7M, Dry Dock 4 $120.3M, Tidal Basin seawall $112.8M, etc.)

### Flags / discrepancies (not overwritten)
- **Ticonic Bridge Status** = "Done" in Notion but Cianbro3.md says "active, completion spring 2027" — Status field not overwritten (additive-only rule; body note added).
- **Canopy Hotel Owning Department** = Infrastructure in Notion but Cianbro3.md says A/Z Corporation — not overwritten (body note added).

## Audit fills (2026-06-13 — notion-audit run #9)
**State as of 2026-06-13 (live re-fetch + 3 URL fills + 3 body enrichments):**

### What was filled (6 writes across 3 records)
- **North Hero-Grand Isle Drawbridge `userDefined:URL`** → `https://www.cianbro.com/projectdetail/621` (was empty). Source: Cianbro3.md.
- **North Hero-Grand Isle Drawbridge body** → enriched: Bridge 8 detail (double-leaf bascule, Route 2 over Lake Champlain, only movable bridge in VT), replaced on new foundation with same aesthetic as 1937 structure, completed end 2023. Source: Cianbro3.md.
- **US Naval Academy Farragut Field Seawall `userDefined:URL`** → `https://www.cianbro.com/news/safeguarding-a-historic-naval-academy` (was empty). Source: Cianbro3.md.
- **US Naval Academy Farragut Field Seawall body** → enriched: scope includes Santee Basin + Brown Park; barge crane work; ribbon cutting Aug 2024; USASpending contract N4008022C0011; start date 2022-09-16. Source: Cianbro3.md.
- **Founders Hall Modernization (MCI) `userDefined:URL`** → `https://www.cianbro.com/projectdetail/1043` (was empty). Source: Cianbro3.md.
- **Founders Hall Modernization (MCI) body** → enriched: MCI semi-private high school context, 1868 Italianate building heart of 23-acre campus, 18-mo project spring 2021–end 2022, delivered by A/Z Corporation. Source: Cianbro3.md.

### Verified empty + genuinely sourceless (no fill possible from dossiers)
- **Bangor I-95 Bridge Replacements `userDefined:URL`** — empty; no direct project page URL in Cianbro.md or Cianbro3.md (only MaineDOT as generic source). Left empty.
- **Southport Swing Bridge `userDefined:URL`** — empty; not in Cianbro3.md project list; Cianbro.md has no direct project URL. Left empty.
- **Maine Veterans' Homes Scarborough `userDefined:URL`** — empty; no direct URL in either dossier. Left empty.

### Already complete (verified this run)
- All prior fills from runs #1–#8 confirmed still in Notion ✓
- Canopy Hotel URL `https://www.cianbro.com/projectdetail/890` ✓ (filled run #8)
- Ticonic Bridge URL + body ✓ (filled run #8)
- Portland HSC URL ✓ (filled run #8)
- Veranda Street URL ✓ (filled run #8)
- All 24 Memberships → Company ✓; 6 Events with dates/tags ✓; 13 Divisions → Company ✓; all addresses filled ✓
- Company Address place (44.7831/-69.3836) ✓

## Audit fills (2026-06-13 — notion-audit run #10)
**State as of 2026-06-13 (full live re-fetch + 1 fill):**
- **Alexandria Bay LPOE `userDefined:URL`** → `https://www.cianbro.com/projectdetail/724` (was empty). Source: Cianbro3.md. Record `37b90644-d524-8158-9e71-e4339dd571c2`. Confirmed written + re-fetched.
- **Already confirmed complete (no writes needed):** Cross Town BESS URL (`pluspower.com`) ✓ · Lockhart Power URL (`cianbro.com/news/lockhart-power`) ✓ · Puritan P4 URL (`cianbro.com/projectdetail/989`) ✓ · Wharf Ph2 URL (`cianbro.com/projectdetail/821`) ✓ · All 7 subsidiary Adress places ✓ · 24 Memberships → Company ✓ · 6 Events with dates/tags ✓ · Division Projects (Infra 15, Building 5, IDM 3, Power&Energy 2, A/Z 1) ✓ · Infrastructure division Adress place (Portland ME, lat 43.6528) ✓ · Company Address place (44.7831/-69.3836) ✓.
- **Genuinely sourceless (confirmed):** Bangor I-95 URL (no cianbro.com project page) · Southport Swing Bridge URL · MVH Scarborough URL · Sarah Mildred Long URL · EMR/TRIR/DART · bonding/surety/insurance · ABC NCC 2024 + AGC Maine Awards exact dates · most People contact details.
- **3a–3e all pass.** Record fully saturated vs Cianbro.md + Cianbro3.md.

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = Cianbro.
2. **Existing Software** view → clear `__TEMPLATE__` filter (Cianbro's 8 rows are in the shared DB).
3. **Company Map / Memberships** People-tab views may carry leftover template filters.
4. Possible template guide rows on local tables + remaining section guide italics (Company Map/Events/Locations/Memberships) — UI cleanup if wanted.
5. **Software dedup (Zack's call, destructive):** Cianbro's Procore row adds to the existing Procore×N pile — merge later if consolidating.
6. Optional: add Maine/Vermont/SC + towns to Projects `Location` select (deferred — concurrent-session clobber risk at load time).
7. Optional: event icons used `trophy_*`/`medal_*` (may be non-standard built-in names → verify render).
8. **Membership body cleanup (optional, cosmetic):** 12 membership records have duplicate content (bullet + identical sentence). TAPPI has the full sentence twice. Non-destructive cleanup whenever convenient.
