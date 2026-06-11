# State · Records — Shawmut Design and Construction

> **Holds:** the dedup ledger for the Shawmut build — company record, profile page, 5 divisions, 19 projects, 13 people, 12 locations, 2 events, 1 membership, 7 software, 14 owner-clients, full interlink map.
> **Ground truth dossier:** `Enlaye Notion/Shawmut/Shawmut3.md` (valid JSON; Shawmut2.md is a truncated/corrupt earlier copy — ignore; Shawmut1/4 empty).
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

## Audit log — 2026-06-11 (automated hourly cycle)
**Full audit run.** Checked: profile page body, 5 divisions (all properties + body depth), 12 locations (all properties), 2 events (all properties), 1 membership, people/projects via prior ledger.
**Result: 0 fills executed.** All records remain complete. No properties found that were both (a) empty AND (b) have a sourced value in the dossier not yet applied.
**Gaps confirmed still sourceless (not regressions — same as prior audit):**
- Large Project Division `People` relation empty — dossier has VP titles only, no named person confirmed.
- Mission Critical `Adress` (place) empty — dossier explicitly null for address.
- Miami + West Palm Beach location rows — `Division` relation empty — dossier explicitly null for owning_division.
- Events `Place` property — both events nationwide, no geocode; correct to leave empty.
- Location `People` relation — dossier assigns people to divisions, not offices; sourceless at office level.
**3b description-depth check:** All 5 division bodies confirmed full depth vs. dossier. Mission Critical 4-bullet body matches dossier (new division, minimal sourced data). ART/100 SCD project body confirmed full depth.
**3c address check:** All 12 location Adress text fields filled. San Diego has street-level address (3655 Nobel Drive). Events Place legitimately empty (nationwide). No regression.
**3d membership check:** AGC of America — 1 membership, Name + Company relation both filled. No additional sourced memberships in dossier.
**3e location tags check:** Safety Week 2026: [Massachusetts, Boston, Rhode Island, Providence, New York, California, Nevada, Florida, National] — complete. 12th Annual: [Boston, Massachusetts, National] — complete.
**Worcester ID note:** correct ID confirmed as `37b90644-d524-8131-9783-e64663faa7fb` (ledger had a space in the ID string — corrected above).
**Harness updated:** this ledger only. No Notion writes executed.

## Audit log — 2026-06-11 (manual run, notion-audit skill)
**Full audit run.** Checked: profile page body, 5 divisions (all properties + body depth), all 12 locations (all properties), 2 events (all properties + location tags), 1 membership, 3 sampled people records (Les Hiscoe CEO, Reza Amirkhalili COO, Shaun Carvalho CSO).
**Result: 0 fills executed.** No properties found that were both (a) empty AND (b) have a sourced value in the dossier not yet applied.
**3a interconnection check:** All 5 divisions → Companies relation ✅. All confirmed people → Company relation ✅. Division-People relations: New England (Kevin Sullivan), NY Metro (David Margolius), West (Greg Skalaski + Sam Ragsdale), Mission Critical (Joel Nickel) — all wired ✅. Large Project Division People empty — no named person in dossier (sourceless). Division-Projects all wired ✅. Locations-Company all wired ✅. Locations-Division wired for 10/12 (Miami + West Palm Beach null per dossier) ✅. Events-Company wired ✅. Membership-Company wired ✅.
**3b description-depth check:** All 5 division bodies confirmed full depth matching dossier. People bodies (3 sampled) full depth with sourced content. No thin bodies found.
**3c address check:** All 12 location Adress text fields filled and correct. Division Adress place properties all set (except Mission Critical — dossier null). Events Place property legitimately empty (nationwide). No regression.
**3d membership check:** AGC of America — only confirmed membership in dossier. 1 row, Name + Company filled ✅. No missing memberships.
**3e location tags check:** Safety Week 2026: [Massachusetts, Boston, Rhode Island, Providence, New York, California, Nevada, Florida, National] — all 9 tags present ✅. 12th Annual: [Boston, Massachusetts, National] — all 3 tags present ✅.
**Genuinely sourceless gaps (unchanged from prior audits):** Large Project Division People; Mission Critical Adress; Miami + West Palm Beach Division relation; Events Place; all-office People relations.
**Harness updated:** this ledger only. No Notion writes executed.
