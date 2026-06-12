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
EMR/TRIR/DART numerics · bonding capacity/surety · insurance carriers · division-level revenue/headcount splits · Maine SOS charter # · per-project parcel/APN/FEMA/seismic · exact NTP/substantial-completion dates (year/month-only kept in body) · per-state license numbers · Cianbro revenue share of JV/program totals (WALK/PNSY/Western Maine are program totals) · company Address place (no lat/lng) · project Adress places (no lat/lng) · most new people Email/Phone (Vigue/Lorenz/Henshaw/Walsh also no LinkedIn) · SBBA long-form name (row exists, name expansion "Specialty Balance Beam Association" is fabricated — MWMCA source only lists the abbreviation).

**Note on memberships:** as of 2026-06-11 audit, Notion Memberships DB contains ~25 rows covering all named associations from the dossier. The prior "~18 missing" gap was filled in a session after the initial 06-10 load (timestamps 23:18 UTC). All are linked to company.

## Audit fills (2026-06-10 — notion-audit run)
- **Events DB `Location tags`:** 3 new options added (Las Vegas, Kissimmee, Maine) — all 9 original options preserved. Applied: ABC Craft Champs 2025 → Las Vegas · ConExpo 2026 → Las Vegas · ABC Craft Champs 2024 → Kissimmee · AGC Maine Build Maine Awards → Maine. ABC Top Performers left untagged (no location in source). Source: `Enlaye Notion/Cianbro/Cianbro.md`.
- **Divisions DB `Adress` place:** A/Z Corporation filled → 40 East Dudley Town Road, Bloomfield CT 06002 (lat 41.8265, lng -72.7376). Source: `Enlaye Notion/Cianbro/Cianbro2.md`.
- Starcon `Adress` not filled — Gonzales LA address in Cianbro2.md is an office, not HQ; primary HQ La Porte TX has no sourced lat/lng → left empty.
- All other Divisions `Adress` (place): market-sector units have no physical address; R.C. Stevens/CFCC/Cianbro Equipment/Cianbro Constructors have no lat/lng in source → left empty.
- Events `Date` not filled — no exact dates sourced in dossier for any events.
- Events `Place` not filled — no lat/lng for event venues sourced.
- Locations `Adress` (text): all 14 rows already populated from prior load session.

## Audit fills (2026-06-11 — hourly /notion-audit cycle)
- **0 new writes.** All sourced fields verified populated. Membership gap (~18 missing noted at load) was closed by a subsequent session; all ~25 MWMCA-named associations now present in Memberships DB.
- **1 data quality flag (no destructive action taken):** SBBA row title reads "SBBA (Specialty Balance Beam Association)" — the full-name expansion is not found in any source; dossier and MWMCA profile only list the abbreviation "SBBA". Row and Company relation are correct; only the parenthetical expansion is unverified. Recommend Zack confirm the correct SBBA full name or rename to "SBBA" only.
- **Verified complete:** company record · 13 divisions (all → Company + People + Projects) · 12 people (all → Company + Division) · 24 projects (all → Contractors + Owning Department) · 14 locations (all → Company + Division) · 5 events (4 location-tagged; ABC Top Performers untagged = no location in source ✓) · ~25 memberships (all → Company) · 7 software (all → Company) · 13 sources · full interlink graph intact.
- **Genuinely sourceless (no data available, confirmed):** EMR/TRIR/DART · bonding/surety · insurance carriers · division revenue/headcount splits · charter # · APN/FEMA/seismic · exact NTP/completion dates · license #s · company/project Address place coords · people Email/Phone/LinkedIn (most).

## Audit fills (2026-06-11 — notion-audit skill run)
- **0 new writes.** Full re-verify: all 5 events live-fetched (tags confirmed — ABC Craft 2025 → Las Vegas ✓, ABC Craft 2024 → Kissimmee ✓, ConExpo 2026 → Las Vegas ✓, AGC Maine → Maine ✓, ABC Top Performers → untagged/no location in source ✓). All 25 membership rows present + Company relation confirmed on ABC spot-check. Infrastructure division body verified. WALK Bridge project body verified (complete depth). Andi Vigue people record verified (Company + Function + body ✓).
- **1 address judgment confirmed:** Starcon `Adress` place property empty — Cianbro2.md gives Gonzales LA office address (lat 30.2241/lng -90.9201) but HQ is La Porte TX (no lat/lng); filling place with a secondary office address would be misleading. Left empty correctly. Body already lists both addresses.
- **1 SBBA flag carried forward:** "SBBA (Specialty Balance Beam Association)" — expansion unverified. Recommend Zack confirm or rename to "SBBA".
- **Sourceless gaps confirmed unchanged:** same list as prior audit run.

## Audit fills (2026-06-11 — notion-audit pass 4, autonomous)
- **0 new writes.** All sourced fields verified populated across full record set.
- **Company Address place confirmed filled:** `place:Address` = Cianbro Corporation HQ / 101 Cianbro Square Pittsfield ME (lat 44.7831 / lng -69.3836) — ledger previously noted as empty; live fetch confirms it is populated. No gap.
- **Events (5):** all tags and company relations confirmed live. ABC Craft 2025 → Las Vegas ✓ · ABC Craft 2024 → Kissimmee ✓ · ConExpo 2026 → Las Vegas ✓ · AGC Maine → Maine ✓ · ABC Top Performers → no location in source (untagged = correct) ✓.
- **Memberships (24 rows):** all 24 MWMCA-sourced associations present and linked to company. Full list: ABC, AGC, AGC Maine, AIHA, AISC, ARTCA, BPA, BWI Business Partnership, CII, CFMA, CURT, DBIA, GBC, MD Chamber, MWII, MTBMA, NAWIC, NSPE, Propeller Club, SAME, SBBA, SMPS, TAPPI, ACI ✓.
- **SBBA flag still open:** "SBBA (Specialty Balance Beam Association)" — full-name expansion unverified in source. Recommend Zack confirm or rename to plain "SBBA".
- **Genuinely sourceless (confirmed):** same list as prior runs — EMR/TRIR/DART · bonding/surety · insurance carriers · division revenue/headcount · charter # · APN/FEMA/seismic · exact NTP/completion dates · license #s · project Adress place coords · most people Email/Phone/LinkedIn · Starcon Adress place.

## Additive pass (2026-06-12 — Cianbro3.md, /notion-load)
Ground truth: `Enlaye Notion/Cianbro/Cianbro3.md`. Additive-only on top of 06-10/06-11 build.

**Profile page body updated:**
- ENR Top 400 #96 → **#94**, ~$1.3B → **$1,342M** (2024 revenue; Chubb ENR list). Source: Chubb ENR top-400.pdf.
- Added **ABC 2026 Top General Contractors #21**. Source: cianbro.com/news/abc-top-performers-2026.

**3 new people created (People DB):**
- Charlie Cianchette `37d90644-d524-813d-a8bd-cdfac41ba8f4` — President, A/Z Corporation · A/Z Corp division → A/Z div People relation updated (now: Lorenz + C.Cianchette)
- Gary Smith `37d90644-d524-81f8-a6ab-ea1675506a8a` — Regional Manager, IDM (Baltimore MD) · IDM division → IDM div People relation updated (now: P.Malikowski + Smith)
- Aric Dreher `37d90644-d524-8137-bd4d-f26b6ae59856` — Asst GM Infrastructure · Infrastructure division → Infra div People relation updated (now: Henshaw + Dreher)

**3 division bodies updated (additive — no replace_content):**
- A/Z Corp: added C.Cianchette as current president + 2024 Building group merger note (a-zcorp.com/announcements/…)
- IDM: added Gary Smith as Regional Manager (cianbro.com/news/project-aims-to-provide-cleaner-air-in-baltimore)
- Infrastructure: added Aric Dreher as Asst GM (cianbro.com/news/cianbros-andrew-hallett…)

**1 new Construction Project created:**
- WIN Waste Wheelabrator Baltimore WTE Overhaul `37d90644-d524-81ce-b559-fcb457fff5e4` — Type=Energy & Power · Status=In progress · Location=[Baltimore, Maryland] · Size=64.5 MW WTE facility · Contractors→Cianbro · Owning Department→IDM
  - IDM div Projects relation updated: now [Lockhart Power, Puritan P4, **WIN Waste**]
  - Company Construction Projects relation updated: 25→**26** projects

**Conflict (additive-only — held):** company Description field still reads "~$1.3B … ENR #96" (filled field; not overwritten). Body on profile page updated; company record Description left as-is.

**Interlink additions (2026-06-12):**
Company ↔ 26 Construction Projects ✓ · Company ↔ 15 People ✓ (3 new) · A/Z→Lorenz+C.Cianchette ✓ · IDM→P.Malikowski+G.Smith ✓ · Infrastructure→Henshaw+Dreher ✓ · WIN Waste→Contractors+Owning Department ✓.

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = Cianbro.
2. **Existing Software** view → clear `__TEMPLATE__` filter (Cianbro's 7 rows are in the shared DB).
3. **Company Map / Memberships** People-tab views may carry leftover template filters.
4. Possible template guide rows on local tables + remaining section guide italics (Company Map/Events/Locations/Memberships) — UI cleanup if wanted.
5. **Software dedup (Zack's call, destructive):** Cianbro's Procore row adds to the existing Procore×3 pile — merge later if consolidating.
6. Optional: add Maine/Vermont/SC + towns to Projects `Location` select (deferred — concurrent-session clobber risk at load time).
7. Optional: event icons used `trophy_*`/`medal_*` (may be non-standard built-in names → verify render).
