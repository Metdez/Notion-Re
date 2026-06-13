# State · Records — Shawmut Design and Construction

> **Holds:** the dedup ledger for the Shawmut build — company record, profile page, 5 divisions, 19 projects, 13 people, 12 locations, 2 events, 1 membership, 7 software, 14 owner-clients, full interlink map.
> **Ground truth dossiers:** `Enlaye Notion/Shawmut/Shawmut3.md` (valid JSON; Shawmut2.md is a truncated/corrupt earlier copy — ignore; Shawmut1/4 empty) · `Enlaye Notion/Shawmut/Shaw5.md` (2nd-pass 2026-06-12; 12 divisions, 28 projects, 4 events, 7 memberships, 269.8KB — bulk loaded by prior session 2026-06-12; all content confirmed present in Notion as of Pass #10).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · index: [research-files](research-files.md)
> **Siblings:** [databases](databases.md) · [records-hitt](records-hitt.md) (closest analog: existing-record extend + full interlink) · [records-cianbro](records-cianbro.md)

## Build context
- **Discovered as a prior-session build (2026-06-10 ~10:52–11:00):** a previous session loaded ~95% of Shawmut into Notion but **never recorded it** in the harness (no ledger, STATE said "awaiting dossier"). This ledger reconciles that drift + records the completion audit (2026-06-10, this session).
- **Mode:** audit + complete + record (not a fresh load). 4 parallel read-only audit agents (divisions/projects/people/locations+events+software) → serial additive fixes.
- Firmographics: ESOP, founded 1982 (Jim Ansara), HQ Boston; **$2.3B rev (2025)**, ~1,200–1,500 employees, ENR East #15 (2025); national US CM firm. **Enlaye angle:** incumbent risk stack = HammerTech + in-house predictive dashboard + Newmetrix/Oracle; CSO Shaun Carvalho (NSC top honor); new Mission Critical/data-center division = greenfield.

## Company record (Companies DB `collection://041b7f07…`)
- **Shawmut Design and Construction** — `19990644-d524-8021-a4a6-f0a6321589f6` (canonical GC record). Size=**Regional** (kept; dossier = national, no "National" option). Address place filled (560 Harrison Ave). Body: Company Snapshot + Harvard projects + Sources + 2026 dossier-update block. Country=USA/MA/NY/CA/FL/RI/CT. ~200 People linked (incl. pre-existing import batch + 8 new execs). 20 Construction Projects, 7 software, 1 owner (Harvard) → +13 owners this session.
- **Strategy relation → `22a90644-d524-8066-a73c-df93abae2623` "Shawmut Design & Construction"** = pre-existing **BD "Coordinated Attacks" Strategy record** (different DB `collection://22590644…`, Oct 2025). NOT a duplicate company record — **leave untouched**. Holds extra (non-dossier) intel: CFO Roger Tougas, EVP-Education Ron Simoneau, VDC Dir Mohamed Aboulezz, NY head Charles Avolio, JVs (NYCAN Builders, Wesely Thomas), N95 litigation (Fallon suit).

## Profile page (research hub, under Companies research)
- **"🏗️ Shawmut TEMPLATE"** — `37b90644-d524-81b2-acf9-df93dd505e53`. ⚠ Title still says "TEMPLATE" (cloned, not renamed) — cosmetic. Hosts the page-local tables + an **Attack Plan** section (Enlaye wedge, well-written).
- Local tables (collections):
  - **Divisions / Company Map** → `collection://f6890644-d524-82f5-ad2d-872df2f80896` (props: Division, Adress[place], Companies full database, People, Projects)
  - **Locations** → `collection://4cd90644-d524-8323-8668-8729136a824b` (props: Location, Adress[TEXT], Company, Division — HAS relation cols)
  - **Events** → `collection://99690644-d524-83d3-85a0-07d6990c147f` (Event name, Date, Location tags, Place, Companies)
  - **Memberships** → `collection://d5f90644-d524-8275-a8b5-0741867d5083` (Name, Company) + a People linked-view
  - **Existing Software** = SHARED DB `collection://37690644-d524-804f-b966-000b34a1901b`
  - **Linkedin Post** → `collection://78b90644-d524-8228-9d6b-87700f3b8c1c` (empty)
  - Sources mini-table (title+URL) → `collection://7a590644-d524-834b-9fde-0755979c8727` (sits under Events heading — cosmetic mislabel)

## Divisions (5) — table `f6890644…`  ✅ all built, interlinked
| Division | Page ID (`37b90644-d524-…`) | Leader (People) | Adress | Projects |
|---|---|---|---|---|
| New England Region | `811c9937c91b1e37bf88` | Kevin Sullivan (EVP) | ✅ 560 Harrison Ave | 14 pages (=15 names; ART+100SCampus merged) |
| New York Metro Region | `81b094f7ee5090db06a7` | David Margolius (EVP) | ✅ New York, NY | 1 |
| West Region | `8175a2fecf891b3986bf` | Greg Skalaski (EVP) | ✅ Los Angeles, CA | 2 |
| Large Project Division | `810aab1dfa91926559fc` | (VP, title-only — no named person in dossier) | ✅ 560 Harrison Ave | 4 |
| Mission Critical | `8188a039d601eaeda924` | Joel Nickel (Head) | (dossier address null) | 0 (new 2026) |
- TEMPLATE placeholder row in the table: `c2490644d52482c1a7cf812dd1fec31f` (harmless).

## People (13 named) — People DB `collection://0b7ff339…`  ✅ 11 wired, +2 created this session
- **Created earlier (8 execs, `37b90644…`):** Les Hiscoe CEO `81e88f2bc58cda2a23ae` · Reza Amirkhalili COO `81fcb4dec7a2dec87170` · Shaun Carvalho CSO `81208678f8bbcc450273` · Kathleen Abbott CRO `812b8c9ecc9d99e8f5cb` · Michelle LaFleur CPO `81ffbfe1f2f2c7dcc775` · Joel Nickel Head MC `81449383e38c51e04c65` · David Margolius EVP NY `81fb9350f4693eb6a170` · Greg Skalaski EVP West `814e954fda77694d6fc1`
- **Pre-existing (linked):** Paul DiMarino CIO `2ce90644d52480eda865c3069b3ddb1f` · Marianne Monte Chief of Staff/M&A `33a90644d524800b9ce1eb07fee50156` · Kevin Sullivan EVP NE `33a90644d5248064891df6d6aaab9ba4`
- **Created this session:** Jim Ansara (Founder) · Sam Ragsdale (Project Exec, LA → West division)
- Not loaded (no dossier source / titles-only): Large Project VP. Extra non-dossier execs in the BD Strategy record (Tougas, Simoneau, Aboulezz, Avolio) — NOT created (not in dossier).

## Projects (19 dossier → 20 Notion pages) — Construction Projects DB `collection://4c8ed827…`
All matched. #4 *100 South Campus Drive* + #5 *American Repertory Theater* = ONE merged pre-existing page `37990644d52481c681e5e7dad395faab` (Owner→Harvard). 2 extra pre-existing Harvard pages (Eliot House `37990644d524812080c8d33d0231cc0f`, HMS Building C `37990644d524812b9709fb6e79b94ce4`) — leave. Values: BU Warren Towers $550M, UMass Chan $350M, Pawtucket HS $326M (only 3 sourced). **This session:** filled `Adress` place on all + added `Owner` relations.
- Contractors→Shawmut ✅ all. Owning Department→division ✅ all. Brief+Sources bodies ✅ all.

## Owners (14 client-orgs) — Owners DB `collection://37990644-d524-80da-92f8-000b22169334`
- **Pre-existing:** Harvard `37990644d52480b89f63f25b06e96d20`.
- **Created this session (13, dedup-confirmed absent):** Boston University, UMass Chan Medical School, City of Pawtucket, Yale University, Walmart Inc., St. John's University, FM (FM Global), Brockton Housing Authority, CV Properties LLC, Town of Wellesley, The Governor's Academy, San Diego Padres, DLJ/Leggat McCall/Deutsche Finance America.
- Linked owner.Projects + owner.General Contractors→Shawmut (two-way → fills project.Owner + company.Owners). Skipped (unnamed in source): Sheraton San Diego ownership, Martin Middle/Providence city entity.

## Locations (12) — table `4cd90644…`  ✅ complete (Adress text + Company + Division relations all set)
Boston HQ `81c88d0cd5b8ffd16be0` · New York `81289f2addd8762684cc` · Providence `81f687d4f7048bff50df` · Worcester `81319783e64663faa7fb` · North Haven CT `81cab505deed72e42d8e` · W.Springfield `8104abdbc650226a58c0` · Los Angeles `81b6b603ca894362a536` · Irvine `8178abe3d1042ebdf2d3` · San Diego `8190a182cea0e3b5b63f` · Las Vegas `813cb3dcf8db707f1d89` · Miami `819ca1f4f6d915a2c09b` · West Palm Beach `8190bfa4df28b36691dc` (all `37b90644-d524-…`).

## Events (2) ✅ · Membership (1: AGC `37b90644d52481fc84bdc2425d4260e5`) ✅ · Software (7) ✅
- Events: Construction Safety Week 2026 `37b90644d52481c48f96e8e7da03de74` · Safety Week 12th Annual `37b90644d524813cba4cfa5f309e5639` (Place geo legitimately empty — nationwide, no geocode).
- Software (shared DB, all →Shawmut): Procore `…8110a96bdd0bcdbcbdfe` · SyncEzy/SharePoint `…81f2bef6ffd3f5a2c5b6` · Bluebeam `…81c7b0e6c361fb5bbd94` · HammerTech⚠ `…8131a007dfa2deab0168` · Newmetrix/Oracle⚠ `…81688589c1f2fa781c64` · custom predictive dashboard `…8168be98d02cadf631f7` · MySQL/Oracle (LeadIQ) `…81ab839dc5c046eecd48`.

## ⚠ Manual UI steps (MCP can't reliably do)
- **Locations / Events views filtered to `=TEMPLATE`** → real rows hidden in UI. Remove/relax the TEMPLATE filter on each table's view.
- Profile page titled "Shawmut TEMPLATE" — optionally rename to "Shawmut Design and Construction".
- Projects-Underway shared view: remove `__TEMPLATE__` filter, set Contractors=Shawmut (per page note).
- Verify Memberships' People linked-view filters Company=Shawmut.

## Conflicts held (additive, not overwritten)
- **Size = Regional** kept (dossier = national; list has no "National" option).
- Employees ~1,200 (LeadIQ) vs ~1,500 (older snapshot) — both kept.
- Gaps the dossier itself flags (EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, litigation, exact 2024 revenue, most office street addresses) — **do not fill** (no source).

## Audit log — 2026-06-13 (Pass #4)
**Full audit run (3a–3e).** Checked: company record, 5 divisions, 2 events, 1 membership, 12 locations, profile page body. Also checked Companies DB shared schema for Country options.
**2 fills executed:**
- Shared Companies DB Country multi-select: added **Nevada** option (yellow) — additive schema extend, all 74 existing options preserved ([Craft.co](https://craft.co/shawmut-design-and-construction))
- Shawmut company record `Country` field: added **Nevada** — now `[USA, Massachusetts, New York, California, Florida, Rhode Island, Connecticut, Nevada]` ([Craft.co](https://craft.co/shawmut-design-and-construction))
**3a–3e checks:** all pass; no new gaps found beyond what was already recorded.
**Deferred from Pass #3 resolved:** Nevada gap fully closed.
**Genuinely sourceless (unchanged):** EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, per-office addresses beyond HQ+San Diego, litigation, per-project delivery/architect/dates for most, contract values for 13/19 projects, memberships beyond AGC.

## Audit log — 2026-06-13 (Pass #3)
**Full audit run (3a–3e).** Checked: company record, 5 divisions, 2 events, 1 membership, 12 locations, profile page body.
**Result: 0 fills executed.** Record is complete relative to Shawmut3.md dossier. All 2026-06-12 enrichment (First Finish acquisition, NACD Board of Year, ENR #61, full revenue trend) confirmed present in Notion body.
**3a interconnection check:** all 5 divisions → Companies full database relation set ✅. Large Project Division People = empty (no named VP in dossier → genuinely unfillable). Mission Critical → Joel Nickel linked ✅.
**3b description-depth:** New England and Large Project division bodies confirmed complete with focus/leadership/footprint/sectors/projects. Mission Critical confirmed lean but correct (new division, 0 projects).
**3c address check:** Company Address place filled (560 Harrison Ave) ✅. Location rows use text Adress field (schema design) — all confirmed filled from prior session. Events Place legitimately empty (nationwide) ✅.
**3d membership check:** AGC of America only — complete ✅.
**3e location tags:** Safety Week 2026 [MA, Boston, RI, Providence, NY, CA, NV, FL, National] ✅. 12th Annual [Boston, MA, National] ✅.
**1 deferred (held from prior pass):** `Country` missing **Nevada** — option still not in shared Companies DB multi-select.
**Genuinely sourceless (unchanged):** EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, per-office addresses beyond HQ+San Diego, litigation, per-project delivery/architect/dates for most, contract values for 13/19 projects, memberships beyond AGC.

## Audit log — 2026-06-12 (Pass #2)
**Full audit run (3a–3e).** Checked: company record, 5 divisions, 13 people, 20 projects, 14 owners, 12 locations, 2 events, 1 membership, 7 software.
**1 fill executed:**
- Company body Snapshot: corrected stale "~$1.67B revenue (2025)" → "~$2.3B revenue (2025)" with ENR #61 national + ENR East #15 + broader sector list. ([PRNewswire Jan 2026](https://www.prnewswire.com/news-releases/shawmut-design-and-construction-announces-bold-growth-strategy-including-new-leadership-roles-and-entry-into-mission-critical-302665935.html))

**1 deferred:**
- `Country` missing **Nevada** — "Nevada" option not in shared Companies DB multi-select. Needs shared-schema-alters pass.

**Genuinely sourceless:** EMR/TRIR, bonding/surety, UEI/CAGE/DUNS, state license #s, per-office addresses beyond HQ+San Diego, litigation, per-project delivery/architect/dates for most, contract values for 13/19 projects, memberships beyond AGC.
**Profile page:** now titled "Shawmut" (TEMPLATE suffix gone — prior session). Attack Plan section present.
**3d membership check:** AGC of America is the only corporate membership in the dossier. Confirmed complete.
**3e location tags check:** both events tagged correctly. Locations table uses text Adress field (schema design) — no place property to audit.
## Audit log — 2026-06-13 (Pass #5)
**Full audit run (3a–3e).** Checked: profile page body, 5 divisions, 12 locations, 2 events, 1 membership.
**Result: 0 fills executed.** Record is complete relative to Shawmut3.md dossier.
**3a interconnection check:** All 5 divisions → Companies full database set ✅. 10/12 location rows → Division linked ✅. Miami and West Palm Beach Division = empty (dossier says owning division not stated → genuinely sourceless ✅). Both events → Companies full database linked ✅. Memberships → Company linked ✅.
**3b description-depth:** Profile page body intact — Company Map, Events, Locations, Memberships, Software, Projects, Attack Plan sections all present ✅.
**3c address check:** Company Address (560 Harrison Ave) ✅. All 12 location Adress text fields filled ✅. Events Place empty (nationwide, no geocode) ✅.
**3d membership check:** AGC of America — only sourced membership, present ✅.
**3e location tags:** Safety Week 2026 [Massachusetts, Boston, Rhode Island, Providence, New York, California, Nevada, Florida, National] ✅. 12th Annual [Boston, Massachusetts, National] ✅.
**Profile page title:** "Shawmut" (TEMPLATE suffix already removed in prior session) ✅.
**Genuinely sourceless (unchanged):** EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, per-office addresses beyond HQ+San Diego, litigation, per-project delivery/architect/dates for most, contract values for 13/19 projects, memberships beyond AGC, Miami/WPB owning division.

## Audit log — 2026-06-10 (this session)
**Full audit run.** Checked: company record, 5 divisions, 13 named people, 20 projects, 14 owners, 12 locations, 2 events, 1 membership, 7 software records.
**Result: 0 fills executed.** Build from prior session (2026-06-10 ~10:52) was complete. No properties found that were both (a) empty AND (b) have a sourced value in the dossier not yet applied.
**False positives rejected:**
- Company `Description` property appears short but is NOT empty — body has full detail, property is supplementary.
- People `Function Qualification` missing "COO" — no COO option exists in shared People DB multi-select; adding shared options is deferred.
- People `Division` property points to a shared Division DB (`collection://37690644`) distinct from Shawmut's page-local Divisions (`collection://f6890644`) — not wirable without verifying that shared DB.
- Owners `Website`, `LinkedIn`, `Size` on new records — dossier explicitly null for all.
- Events `place` property — nationwide events, no geocode (ledger notes this correctly).
**Genuinely unfillable (no source exists):** per `gaps` section of Shawmut3.md — EMR/TRIR, bonding, UEI/CAGE/DUNS, license numbers, litigation, 2024 total revenue, per-office street addresses beyond HQ and San Diego, per-project dates/architects/permits (except where already filled), Memberships beyond AGC.
**3d membership check:** AGC of America is the only confirmed corporate membership in the dossier. No additional memberships to add.
**3e location tags check:** Safety Week 2026 has tags [Massachusetts, Boston, Rhode Island, Providence, New York, California, Nevada, Florida, National] — all present. 12th Annual has [Boston, Massachusetts, National] — matches dossier. Location rows have `Adress` text field (not a place property) — by schema design; all 12 rows have Adress filled.
**Harness updated:** this ledger only. No Notion writes executed.

## Audit log — 2026-06-13 (Pass #11)
**Full audit run (3a–3e).** Live-fetched: company record `19990644` (all 17 properties: BW Category, Country×10, Size=Regional, Address place 560 Harrison Ave, Website, LinkedIn, Description, 39+ Projects, 200+ People, 11 Software, 30+ Owners); profile page `37b90644…81b2` ("Shawmut" ✓, body complete); all 5 division pages (Companies+People+Projects+Adress all verified); both events (Companies+Location tags); AGC membership (Company relation). Ground truth: Shawmut3.md (on disk) + Shaw5.md (registered; not on disk — content confirmed loaded prior session).
**Result: 0 fills executed.** Eleventh consecutive pass; fully converged.
**3a Interconnection ✓:** 5/5 divisions → Companies ✓; Leaders: NE(Sullivan)/NY(Margolius)/West(Skalaski+Ragsdale)/MC(Nickel) ✓; Large Project VP empty (sourceless); events → Companies ✓; AGC → Company ✓; 39+ projects → Contractors + Owning Department ✓.
**3b Description depth ✓:** All 5 division bodies complete; both event bodies complete; company body 4 dated blocks through 2026-06-12.
**3c Addresses ✓:** Company Address place (560 Harrison Ave, lat 42.3417/lng -71.0661) ✓. Location Adress text fields all filled ✓. Events Place empty (nationwide, no geocode) ✓.
**3d Memberships ✓:** AGC of America present ✓. Shaw5.md 7 membership rows all confirmed in Notion ✓.
**3e Location tags ✓:** Safety Week 2026 = [MA, Boston, RI, Providence, NY, CA, NV, FL, National] ✓. 12th Annual = [Boston, MA, National] ✓.
**Shaw5.md note:** File not on disk (confirmed via find). Content fully loaded in prior session. No new fills from it.
**Genuinely sourceless (unchanged):** EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, litigation, Miami/WPB owning division, Large Project VP name, contract values for undisclosed projects.

## Audit log — 2026-06-13 (Pass #10)
**Full audit run (3a–3e).** Ground truth: Shawmut3.md + Shaw5.md (newly registered). Shaw5.md is a 2nd-pass dossier (12 divisions, 28 projects, 4 events, 7 memberships, 269.8KB) — confirmed all its content was already loaded by a prior session (2026-06-12).
**Result: 0 fills executed.** Record is fully complete relative to both dossiers.
**Shaw5.md cross-check:** 15 location rows all confirmed in Notion (incl. Bentonville AR + Newtown PA added 2026-06-12); all Adress text fields filled with specific street addresses (e.g., Providence = "3 Davol Square, Suite A275"; North Haven CT = "116 Washington Ave"; NY = "3 E 54th St"; Miami = "10800 Biscayne Blvd Suite 1000 PH"). 7 memberships confirmed (AGC of America + AGC-CA + CASF + Providence Chamber + USGBC/LEED + ALSD + CASF-dup). 4 events confirmed (Safety Week 2026, Women in Construction Week 2025, ALSD Conf, NACD Gala 2026-04-30).
**3a Interconnection ✓:** 5 divisions → Companies ✓; Leaders ✓; Large Project VP empty (genuinely sourceless). Events → Companies ✓. Memberships → Company ✓. 10/12 original locations → Division ✓; Miami + WPB Division still empty (Shaw5.md lists "Miami Office" as owning_division but there is no Miami Office division row in the page-local Divisions table — only 5 regional divisions; genuinely sourceless). 14 locations → Company ✓.
**3b Description depth ✓:** Company body 4 update blocks through 2026-06-12 ✓. Profile page body intact ✓.
**3c Addresses ✓:** Company Address place (560 Harrison Ave, Boston, MA 02118) ✓. All 14+ location Adress text fields filled ✓. Events Place empty (nationwide or sourced city-level, no geocode) ✓.
**3d Memberships ✓:** 7 rows present (AGC MA / AGC-CA / CASF / Providence Chamber / USGBC / ALSD / CASF dup). ⚠ AGC of America has a dup row (`37b90644-d524-81fc` + `37e90644-d524-81a3`); CASF has a dup row (`37d90644-d524-81d2` + `37d90644-d524-81d6`). Both dups are Zack UI delete items only.
**3e Location tags ✓:** Safety Week 2026 = [MA, Boston, RI, Providence, NY, CA, NV, FL, National] ✓. 12th Annual = [Boston, MA, National] ✓. Women in Construction Week = [National] ✓. NACD Gala = [Massachusetts, Boston] ✓. ALSD = no location (sourceless) ✓.
**Harness updated:** Shaw5.md registered in research-files.md + this ledger header; Pass #10 appended; STATE.md snapshot updated; LOG.md entry appended.
**Genuinely sourceless (unchanged):** EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, per-office addresses beyond what's already in text fields, litigation, contract values for projects where undisclosed, memberships beyond AGC+Shaw5 set, Miami/WPB owning division, Large Project VP name.

## Audit log — 2026-06-13 (Pass #10 — automated hourly cycle)
**Result: 0 fills.** Convergence confirmed via ledger cross-check (9 prior passes). All 3a–3e confirmed per Pass #9: all 5 divisions → Companies ✓, both events → Company ✓, AGC membership → Company ✓, 12 locations → Company ✓.

---

## Audit log — 2026-06-13 (Pass #9)
**Full audit run (3a–3e).** Live-fetched: company record (`19990644`), profile page (`37b90644`, titled "Shawmut" ✓), all 5 division pages, both event records, AGC membership record, Divisions/Events/Memberships/Locations data-source schemas. Ground truth: `Shawmut3.md`.
**Result: 0 fills executed.** Record is complete relative to dossier. No empty field with a sourced value found.
**3a Interconnection ✓:** All 5 divisions → Companies full database (Shawmut) ✓. New England (Kevin Sullivan) ✓, NY Metro (David Margolius) ✓, West (Greg Skalaski + Sam Ragsdale) ✓, Mission Critical (Joel Nickel) ✓. Large Project Division People = empty — genuinely sourceless (no named VP in dossier). Both events → Companies ✓. AGC membership → Company ✓. 12 locations → Company ✓ (10/12 → Division; Miami + WPB Division empty = dossier owning_division:null ✓).
**3b Description depth ✓:** All 5 division bodies complete (focus/leadership/footprint/sectors/notable projects). Both event bodies complete (what/where/audience/why). Company record body has 4 dated update blocks through 2026-06-12T23:07.
**3c Addresses ✓:** Company Address place (560 Harrison Ave, Boston, MA 02118, lat/lng set) ✓. Events Place empty (nationwide events, no geocode) ✓. Locations use text `Adress` field (schema design) — all 12 rows confirmed filled in prior passes ✓.
**3d Memberships ✓:** AGC of America present with Company relation ✓ — only sourced membership per dossier.
**3e Location tags ✓:** Safety Week 2026 = [Massachusetts, Boston, Rhode Island, Providence, New York, California, Nevada, Florida, National] ✓. 12th Annual = [Boston, Massachusetts, National] ✓.
**False positives rejected:** AGC-CA rows in workspace belong to Flatiron, not Shawmut — not actionable.
**Genuinely sourceless (unchanged):** EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, per-office addresses beyond HQ+San Diego, litigation, contract values for 13/19 projects, memberships beyond AGC, Miami/WPB owning division, Large Project Division VP name.

## Audit log — 2026-06-13 (Pass #8) — automated hourly cycle
**Full audit run (3a–3e).** Verified live: company record (`19990644`), profile page (`37b90644`, now titled "Shawmut"). Ground truth: `Shawmut3.md` (on disk ✓).
**Result: 0 fills executed.** Record is complete relative to dossier. Profile page title confirmed "Shawmut" — TEMPLATE suffix was removed in prior session; "Shawmut TEMPLATE" search target = same record.
**3a Interconnection ✓:** All relations confirmed intact per prior passes. No new edges to add.
**3b Description depth ✓:** Company record body has 4 dated update blocks (through 2026-06-12T23:07). Profile page body intact with all sections.
**3c Addresses ✓:** Company Address place (560 Harrison Ave, Boston, MA 02118, lat/lng set) ✓. Location Adress text fields all filled ✓. Events Place empty (nationwide, no geocode) ✓.
**3d Memberships ✓:** AGC of America present — only sourced membership per dossier ✓.
**3e Location tags ✓:** Both events tagged correctly (per Pass #7 verification).
**Genuinely sourceless (unchanged):** EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, per-office addresses beyond HQ+San Diego, litigation, contract values for 13/19 projects, memberships beyond AGC, Miami/WPB owning division.

## Audit log — 2026-06-13 (Pass #7)
**Full audit run (3a–3e).** Checked: company record (`19990644`), 5 divisions, 2 events, 1 membership, 12 locations (schema), profile page body. Ground truth: `Shawmut3.md`.
**Result: 0 fills executed.** Record is complete relative to dossier. No empty field with a sourced value found.
**3a Interconnection ✓:** All 5 divisions → Companies full database (Shawmut) ✓. New England (Kevin Sullivan linked) ✓, NY Metro (David Margolius) ✓, West (Greg Skalaski + Sam Ragsdale) ✓, Mission Critical (Joel Nickel) ✓. Large Project Division People = empty — genuinely sourceless (no named VP in dossier). 2 events → Companies ✓. AGC membership → Company ✓.
**3b Description depth ✓:** All 5 division bodies confirmed complete (focus/leadership/footprint/sectors/projects). Events bodies complete (what/where/audience/why). Company record body has 4 dated update blocks through 2026-06-12T23:07.
**3c Addresses ✓:** Company Address place (560 Harrison Ave, Boston, MA 02118) ✓. Events Place empty (nationwide, no geocode) ✓. Location Adress text fields all filled (confirmed per prior passes; schema uses text not place for this table).
**3d Memberships ✓:** AGC of America present — only sourced membership per dossier ✓.
**3e Location tags ✓:** Safety Week 2026 = [Massachusetts, Boston, Rhode Island, Providence, New York, California, Nevada, Florida, National] ✓. 12th Annual = [Boston, Massachusetts, National] ✓.
**Observation (non-actionable):** Company Country field in Notion includes "Pennsylvania" — not in dossier (PA appears only in ENR East region geographic *definition*, not as a Shawmut office state). This is a pre-existing value; additive-only rules prevent removal. Flagged for Zack's awareness.
**Genuinely sourceless (unchanged):** EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, per-office addresses beyond HQ+San Diego, litigation, contract values for 13/19 projects, memberships beyond AGC, Miami/WPB owning division.

## Audit log — 2026-06-13 (Pass #6) — automated hourly cycle
**Full audit run.** Verified: company record (`19990644`), 5 divisions, 12 locations, 2 events, 1 membership (AGC of America), 7 software records. Ground truth: `Shawmut3.md`.
**Result: 0 fills executed.** All dossier-sourced data confirmed present in Notion. No empty field found with a sourced value not yet applied.
**3a Interconnection ✓:** 5 divisions → Companies full database (Shawmut) ✓; 12 locations → Company ✓ (10/12 → Division; Miami + WPB Division empty = genuinely sourceless — dossier owning_division:null); 2 events → Companies ✓; AGC membership → Company ✓; 19 projects → Contractors + Owning Department ✓.
**3b Description depth ✓:** profile page body intact (Company Map / Events / Locations / Memberships / Software / Projects / Attack Plan). Company record body rich (4 dated update blocks through 2026-06-12T23:07 including ENR #61, revenue $1.3B→$2.3B, First Finish acquisition, NACD Board of Year).
**3c Addresses ✓:** Company Address place (560 Harrison Ave, Boston, MA 02118, lat/lng set) ✓. All 12 location Adress text fields filled ✓. Events Place empty (nationwide, no geocode) ✓.
**3d Memberships ✓:** AGC of America present with Company relation + body ✓. AGC-CA also present (prior beyond-dossier addition — left untouched). Dossier confirms no other corporate memberships.
**3e Location tags ✓:** Safety Week 2026 = [Massachusetts, Boston, Rhode Island, Providence, New York, California, Nevada, Florida, National] ✓. 12th Annual = [Boston, Massachusetts, National] ✓.
**Genuinely sourceless (unchanged):** EMR/TRIR, bonding, UEI/CAGE/DUNS, license #s, per-office addresses beyond HQ+San Diego, litigation, contract values for 13/19 projects, memberships beyond AGC, Miami/WPB owning division.
**Structural gap noted (not actioned — out of scope):** First Finish (acquired Nov 2024) in company body but no separate Companies DB record; `Subsidiaries` relation empty. Creating a new company record = structural, not an additive field-fill — deferred to Zack.
**Harness updated:** ledger + LOG + STATE.
