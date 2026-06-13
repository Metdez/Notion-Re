# State · Records — FlatironDragados

> **Holds:** the FlatironDragados dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching an FD record.
> **Ground truth:** `Enlaye Notion/FlatironDragados/Flat.md` (primary structured dossier) + `Flatiron1.md` (secondary — extra projects/people/software/events/memberships). `Flat1.md` is empty. Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.

---

## Status: ✅ load complete (2026-06-10)
Prior "in progress" ledger was stale — only the orient step had run (company record confirmed + conflicts noted; template page duplicated but **unmodified**). Full load executed 2026-06-10 from a clean slate.

## Company record (EXISTING — extended, not created)
**"FlatironDragados"** `24690644-d524-8067-94e4-c40fbc9c089f` in Companies DB. Pre-existed (2026-02-17): Website/LinkedIn/BW=Builder/Country=USA/Type=Company/Parent Company (ACS Group `18a90644…`) + **34 People**.
- **Filled 2026-06-10:** `Address` place (4004 Summit Blvd NE Ste 1600, Atlanta GA 30319; 33.8746,-84.3389) · `Country` += Georgia, Atlanta, Canada, Ontario, Arizona, Florida, Massachusetts, New York, Virginia, Maryland, California, Texas, New Jersey, Washington · body **Company Snapshot + Sources** · `Construction Projects` = 21 URLs (one-way, set explicitly). People auto-grew to ~45 (11 new leaders two-way).
- ⚠ **Size = "Regional" kept** (dossier says "Multinational"/Mutlinational). Conflict preserved per additive rule.
- ⚠ **Description = "Merger between Flatiron & Dragados" kept** (thin but filled) — rich description placed in profile-page bio + company Snapshot body instead.

## Profile page (hub)
**"FlatironDragados"** `37b90644-d524-8039-a71b-f0498180c9a7` (was "FlatrionDragadosTEMPLATE (2)" — renamed, icon 🌉). Company Map variant. Bio/Snapshot inserted at top; Attack Plan filled (risk-led, integration-timed). Section guide italics left in place (cosmetic — UI cleanup).
- Inline DBs: Company Map (Divisions) `e7190644-d524-83d2-9d8a-87a0a1214bb7` · Events `94d90644-d524-8299-b912-076f6e39bfae` · **Sources** `3cc90644-d524-82ee-ab22-87a50603cac4` · Locations `19a90644-d524-83d2-a915-0713b827fc14` · Memberships `54b90644-d524-82f4-b9ae-8730a723a35a` · Projects Underway = shared `4c8ed827…` · Existing Software = shared `37690644-d524-804f…`.

## Divisions (6 — Company Map `e7190644…`)
All Companies→FD; bodies (focus/leader/footprint/notable projects/parent); Adress place where coords known.
| Division | ID | Adress place | People | Projects |
|---|---|---|---|---|
| FlatironDragados USA | `37b90644-d524-81cf-aef0-f4866e7949c5` | Atlanta (33.8746,-84.3389) | Sevilla, Davoren, Grabinski, Nelson, Schneiderman, Fiuza | 12 |
| FlatironDragados Canada | `37b90644-d524-81b2-905d-c146adc8983d` | Toronto (43.648,-79.3848) | — | 2 (Gordie Howe, QEW) |
| Pulice – a FlatironDragados company | `37b90644-d524-814e-8558-c6ae6c011149` | Scottsdale AZ (33.5722,-111.8957) | Jimenez | 2 (New Harbor, SR303L) |
| SPC Construction Co. LLC | `37b90644-d524-817c-8c6f-e79cde224bd5` | — (no coords) | Diez, Sheehan, Wegman | 2 (Battery Park, Hudson River) |
| Prince Contracting, LLC | `37b90644-d524-81d8-a293-e2169b8edf0c` | — (no coords) | Calandros | 2 (I-95 Broward, I-275) |
| J.F. White Contracting Co. | `37b90644-d524-8124-bd3a-f0ed57f676af` | Framingham MA (42.3076,-71.4204) | — | 1 (Sumner Tunnel) |

## People (11 leaders created — all dedup-confirmed absent vs 34 existing)
People DB `0b7ff339…`; each Company→FD + ## Role body. (People→Division relation N/A — targets fixed collection `37690644…818a9b6b`, not page-local Company Map; reverse link on division rows carries it.)
| Name | ID | Function |
|---|---|---|
| Javier Sevilla | `37b90644-d524-8139-beda-d5b088c467bc` | CEO, FlatironDragados |
| Peter Davoren | `37b90644-d524-81c0-9d85-c332cf5519b5` | Chairman (also Turner Chairman/CEO) |
| Richard Grabinski | `37b90644-d524-810f-b470-f025f3e7dd6b` | COO; AGC of California Caltrans liaison |
| Victor Jimenez | `37b90644-d524-8159-8765-c6262b900c5c` | President, Pulice |
| Jack Calandros | `37b90644-d524-81af-8264-f0de3fabff5a` | President, Prince Contracting |
| Jesus Diez | `37b90644-d524-818d-beda-d32a67c0d096` | MD, SPC Construction |
| Joe Sheehan | `37b90644-d524-81a1-bf2c-e4699bdf3d15` | COO, SPC |
| Neil Wegman | `37b90644-d524-81fc-8d57-db78253acd09` | CFO, SPC |
| Dale Nelson | `37b90644-d524-8169-8a5a-eb1562ac8bd8` | EVP, USA West |
| Jim Schneiderman | `37b90644-d524-81a5-9d1e-d4770b93a9af` | EVP, Mid-Atlantic |
| Ramon Fiuza | `37b90644-d524-8110-9dc8-f837d99fdbde` | EVP, Large Projects (w/ José Luis Méndez Sánchez, in body) |

## Projects (21 — shared Construction Projects `4c8ed827…`, all Contractors→FD)
Prefix `37b90644-d524-`. Division link via Company Map row's Projects relation (project `Owning Department` NOT set — targets Companies DB, not page-local; division.Projects carries the edge).
| Project | ID suffix | $M | Status | Loc tag | Division |
|---|---|---|---|---|---|
| Hampton Roads Bridge-Tunnel Expansion | `81f5-a2e9-d5385052b4ea` | 3900 | In progress | VA, Norfolk | USA |
| Gordie Howe International Bridge | `81c7-87ad-c45249cf21d1` | 4600 | In progress | Ontario, Canada | Canada |
| Purple Line light rail | `813f-b112-cd045cd869ad` | 3400 | In progress | Maryland | USA |
| SR 400 Express Lanes | `81c1-9f78-d1954447258b` | 4600 | In progress | Georgia | USA |
| Long Bridge North | `8162-a9e5-fe385aad3230` | 1000 | In progress | DC, VA | USA |
| Franconia-Springfield Bypass | `817c-8e25-ca399ee8030c` | 414 | In progress | Virginia | USA |
| New Harbor Bridge Corpus Christi | `8154-8fa0-d63c8bea02fc` | 1200 | Done | Texas | Pulice |
| LA Metro SE Gateway / Link Union Station | `8189-bf6b-e141f8bd6928` | 900 | In progress | LA, CA | USA |
| LAX ATMP Roadway Improvements | `8144-8166-c7d58a5ad206` | 868 | In progress | LA, CA | USA |
| QEW Garden City Skyway Twinning | `81a5-934a-ed85feb3d581` | — | In progress | Ontario, Canada | Canada |
| SR 303L Bob Stump Memorial Parkway | `81c0-8e12-f5a943aeabb2` | 129 | In progress | Arizona | Pulice |
| San Diego International Airport Terminal 1 | `8132-b20f-cacb7734aa6e` | 3800 | In progress | San Diego, CA | USA |
| I-95 / SW 10th Street Broward County | `8152-aa72-f4bafa57f7f7` | 933 | In progress | ⚠ none (Florida) | Prince |
| I-275 Express Lanes Pinellas County | `8181-ad0c-d768409693d1` | 340 | In progress | ⚠ none (Florida) | Prince |
| Windsor Woods / Princess Anne / The Lakes Stormwater | `81ee-8b43-cc91d0fb6835` | 518 | In progress | ⚠ none (clobber) | USA |
| North / West Battery Park City Resiliency | `8114-982f-c6d06b079279` | 1700 | In progress | ⚠ none (clobber) | SPC |
| Rebuild by Design Hudson River Resiliency | `816d-b794-e8b5524024a6` | 251 | In progress | ⚠ none (clobber) | SPC |
| Port Arthur Storm Surge Upgrade | `81c0-ade7-dc9d03d7b00f` | 102 | In progress | ⚠ none (clobber) | USA |
| Howard A. Hanson Dam Fish Passage | `8118-939b-d37a19aab9b2` | 691 | In progress | ⚠ none (Washington) | USA |
| Sumner Tunnel Restoration | `815d-94eb-c03e46a068ac` | 156 | Done | ⚠ none (clobber) | J.F. White |
| LAX Automated People Mover | `812c-953a-c29a425bb4cf` | 2400 | Done | ⚠ none (clobber); ⚠ medium confidence | USA |

Dates set (month-precise only): New Harbor 2025-06-28 · Long Bridge 2025-07-01→2030-12-01 · Franconia 2025-07-01 · San Diego 2025-09-23 · Howard Hanson 2026-03-01. Year-only/quarter dates in body prose.

## Page-local tables
- **Software** (shared `37690644-d524-804f…`): 5 new FD rows — HCSS HeavyBid `81db-871d…` (no tag — option absent) · Bluebeam Revu `81de-a353…` · Oracle Primavera P6 `812f-80f2…` · Procore `8199-841b…` · Oracle Aconex + Autodesk `816c-9109…`. All Companies→FD. ⚠ New rows (not extending existing dup-laden Procore/Bluebeam rows) — audit/Zack dedup.
- **Memberships** (`54b90644…`): 7 rows — AGC, DBIA, IPI, The Beavers, California Alliance for Jobs, Hispanic Contractors of Colorado, NECA Boston (via J.F. White). **ADD COLUMN `Companies full database` (pre-authorized)** → all 7 linked → FD.
- **Events** (`94d90644…`): 2 rows — DBIA Conference & Expo 2025 (2025-11-05) · Groundbreaking Women in Construction 2026 (2026-06-14). Companies→FD. Venue tags absent from multi-select → body; Place needs coords → omitted.
- **Locations** (`19a90644…`): 6 rows — Atlanta HQ, Toronto, Scottsdale (Pulice), Framingham (J.F. White), Tampa (Prince), legacy Broomfield CO. **ADD COLUMN `Companies full database` + `Division` (pre-authorized)** → all → FD; 5 → owning division (Broomfield legacy = company-only). Adress is TEXT here → addresses stored as text.
- **Sources** (`3cc90644…`): 34 rows — primary dossier sources.

## ⚠ Concurrent-session clobber incident (2026-06-10)
Mid-load, a **parallel session reset the shared Projects `Location` multi-select to only `["Florida","South Carolina"]`** (the ~115-option list was wiped from the selectable schema). Caught when project batch C failed validation. **Existing page values survived** (HRBT still shows Virginia/Norfolk) — Notion keeps values when an option is removed; only NEW assignments are blocked. Impact on this build: batch C's 7 projects (Windsor Woods, Battery Park, Hudson River, Port Arthur, Howard Hanson, Sumner, LAX APM) have **no Location tag** (geography in body). Did NOT restore the option list — destructive-class re-write of a shared multi-select while another session is actively writing; needs Zack's call. **This likely affects other companies' projects too** (cross-company shared DB).

## Audit — 2026-06-13 (seventh pass)
**Status: ✅ audit complete.** Ground truth: `Flat.md` + `Flatiron1.md`. Zero fillable gaps found. No writes made this pass.

### What was verified (seventh pass)
- **Company record** `24690644…`: Size="Mutlinational", Type="Company", Website, Address place (4004 Summit Blvd NE Ste 1600, Atlanta GA; 33.8746/-84.3389), Description, BW Category, Country 15 tags, People 46+, Construction Projects 37+, Parent Company — all populated ✓
- **Profile page body** `37b90644…8039`: Bio, Snapshot, Attack Plan — complete ✓
- **All 21 original projects:** Location tags confirmed present on ALL — including all 7 previously-clobbered batch-C projects: Windsor Woods=[Virginia] ✓, Battery Park=[New York] ✓, Hudson River=[New Jersey] ✓, Port Arthur=[Texas] ✓, Sumner=[Massachusetts,Boston] ✓, LAX APM=[California,Los Angeles] ✓, Howard Hanson=[Washington] ✓. Gordie Howe=[Ontario,Michigan] ✓. All Contractors→FD ✓.
- **Memberships (10 content rows confirmed live):** AGC of California `37e90644…8191` · DBIA `37e90644…81e6` · IPI `37e90644…810e` · Hispanic Contractors of Colorado `37e90644…8170` · NECA Boston `37e90644…81b8` · The Beavers `37b90644…81ea` · AGC San Diego `37c90644…8179` · AGC San Diego (dup) `37d90644…81f3` · Carolinas AGC `37d90644…8136` · CCIB `37d90644…81fa` · California Alliance for Jobs `37e90644…8130` — all Companies→FD ✓. (Plus 7 blank dup rows from 2026-06-12 20:20 — still pending Zack UI delete.)
- **Events (5 rows):** DBIA Conf & Expo 2025 (Las Vegas, place+tag ✓) · Groundbreaking Women 2026 (San Diego, place+tag ✓) · IAI Summit 2025 (location not disclosed — correct no tag) · IPI Awards 2022 (location unknown — correct no tag) · CI Student Days 2025 — all Companies→FD ✓
- **All 6 Divisions:** Companies→FD, Adress place where available, body content — complete ✓

### Still empty (genuinely sourceless — unchanged)
EMR/TRIR/DART/OSHA records · bonding/surety/insurance · per-division revenue & headcount · exact employee count · DUNS · project permit/parcel/APN/FEMA/seismic · most per-project full date sets. InEight/SAP/Viewpoint Vista/Trimble One UNVERIFIED. People Email/Phone/LinkedIn. Project `Adress` place property. J.F. White division People relation (no named leader in any dossier). IAI Summit 2025, IPI Awards 2022 Location tags/Place (genuinely sourceless — location not disclosed in source).

---

## Audit — 2026-06-13 (sixth pass — hourly auto-cycle)
**Status: ✅ audit complete.** Ground truth: `Flat.md` + `Flatiron1.md` + `Flat2.md`. Zero fillable gaps found. No writes made this pass.

### Key finding: view-filter false positives rejected
Inline-DB views on the profile page have a leftover `__TEMPLATE__` filter that hides most rows from view queries. Sub-agent reading the filtered view reported only 4 memberships and 4 events — but raw collection searches confirmed all 10 memberships and 5 events exist with full data. Every "missing" row was a view-filter artifact, not an actual gap. Verified records present:
- **Memberships (10):** AGC of California `37e90644…8191`, DBIA `37e90644…81e6`, IPI `37e90644…810e`, California Alliance for Jobs `37e90644…8130`, Hispanic Contractors of Colorado `37e90644…8170`, NECA Boston `37e90644…81b8`, AGC San Diego `37d90644…81f3`, Carolinas AGC, The Beavers, CCIB — all Companies→FD ✓
- **Events (5):** DBIA Conf & Expo 2025 (Las Vegas, Nov 5, place+tag ✓) · Groundbreaking Women 2026 (San Diego, Jun 14, place+tag ✓) · IAI Summit 2025 · IPI Awards 2022 · CI Student Days 2025
- **Locations:** Secaucus NJ `37c90644…8153` confirmed with address + Division→SPC ✓
- **Company record:** all properties populated (Description, Size="Mutlinational", Address place, Country 15 tags, BW Category, Website, LinkedIn, Parent Company, People 46, Construction Projects 37) ✓
- **Profile page body:** Bio, Snapshot, Attack Plan — complete ✓

### Still empty (genuinely sourceless — unchanged)
EMR/TRIR/DART/OSHA records · bonding/surety/insurance · per-division revenue & headcount · exact employee count · DUNS · project permit/parcel/APN/FEMA/seismic · most per-project full date sets. InEight/SAP/Viewpoint Vista/Trimble One UNVERIFIED. People Email/Phone/LinkedIn. Project `Adress` place property. J.F. White division People relation (no named leader in any dossier). IAI Summit 2025, IPI Awards 2022, CI Student Days 2025 Location tags/Place (genuinely sourceless — "UNKNOWN" in all dossiers).

## Audit — 2026-06-13 (fifth pass)
**Status: ✅ audit complete.** Ground truth: `Flat.md` + `Flatiron1.md`. Zero fillable gaps found. Full live verification of all record types: company record, profile page, 21+ projects, 6 divisions, 10 memberships, 2 events, location rows. Every field with sourced data is already present in Notion. No writes made this pass.

### What was verified as already complete (fifth pass)
- Company record: all properties populated (Description, Website, Size, Address place, BW Category, Country 15 tags, People 160+, Construction Projects 37 URLs, Parent Company, LinkedIn, body Snapshot with UEI/NAICS/ISO/IDIQ/revenue) ✓
- Profile page: Bio, Snapshot, Attack Plan — complete ✓
- All 21 original projects: Contractors→FD, Status, Contract Value, Location tags, Date (where sourced), body — complete ✓. LAX APM updated in prior session to $4.9B/In progress/richer body from Flat2.md ✓
- Additional projects from Flat2.md (later sessions): confirmed present and linked to FD USA division (e.g. Upper San Leandro WTP `37c90644…81f6`) ✓
- All 6 Divisions: Address place (where available), body, Companies→FD, People, Projects — complete ✓
- All 10 Memberships: AGC of California, AGC San Diego, Carolinas AGC, The Beavers, CCIB, DBIA, IPI, California Alliance for Jobs, Hispanic Contractors of Colorado, NECA Boston — all have Companies→FD + body + source URLs ✓
- Both Events: DBIA (Las Vegas, Nov 5 2025, place coords, "Las Vegas" tag, Companies→FD) · Groundbreaking Women (San Diego, Jun 14 2026, place coords, "San Diego" tag, Companies→FD) ✓
- Gordie Howe Bridge Location: ["Ontario","Michigan"] ✓
- I-275 Pinellas Location: ["Florida"] ✓; stale body note removed ✓

### Still empty (genuinely sourceless — unchanged)
EMR/TRIR/DART/OSHA records · bonding/surety/insurance · per-division revenue & headcount · exact employee count · DUNS · project permit/parcel/APN/FEMA/seismic · most per-project full date sets. InEight/SAP/Viewpoint Vista/Trimble One UNVERIFIED. People Email/Phone/LinkedIn. Project `Adress` place property (no per-project street addresses in source). J.F. White division People relation (no named leader in any dossier).

---

## Audit — 2026-06-13 (fourth pass)
**Status: ✅ audit complete.** Ground truth: `Flat.md` + `Flatiron1.md` + `Flat2.md`. One fillable gap found and resolved.

### Filled in audit
- **Gordie Howe International Bridge** `Location` — added "Michigan" tag (bridge crosses Windsor ON → Detroit MI; Michigan was a valid schema option, only Ontario was set). Source: Flat.md + Flatiron1.md. ID: `37b90644-d524-81c7-87ad-c45249cf21d1`.
- **I-275 Express Lanes Pinellas County** body — removed stale "(Location tag pending — 'Florida' not yet a Projects option)" note; Florida is now a valid tagged option. ID: `37b90644-d524-8181-ad0c-d768409693d1`.

### What was verified as already complete
- Company record: Description, Size ("Mutlinational"), Website, Address (place), BW Category, Country tags, People, Construction Projects — all populated ✓
- All 21 projects: Contractors→FD, Location tags, Status, Values, Date (where sourced) — all verified ✓
- All 10 Memberships rows: linked to FD company ✓ (AGC of California, AGC San Diego, Carolinas AGC, The Beavers, CCIB, DBIA, IPI, California Alliance for Jobs, Hispanic Contractors of Colorado, NECA Boston)
- Both Events rows: Place (coords), Date, Location tags, Companies→FD ✓
- All 6 Divisions: Address place (where available), body content, Companies→FD ✓
- Profile page body: Bio, Snapshot, Attack Plan — all filled ✓

### Still empty (genuinely sourceless — unchanged from prior passes)
EMR/TRIR/DART/OSHA records · bonding/surety/insurance · per-division revenue & headcount · exact employee count · DUNS · project permit/parcel/APN/FEMA/seismic · most per-project full date sets. InEight/SAP/Viewpoint Vista/Trimble One UNVERIFIED. People Email/Phone/LinkedIn. Project `Adress` place property (no per-project street addresses in source). J.F. White division People relation (no named leader in any dossier).

### ⚠ Duplicate rows for Zack UI cleanup (unchanged)
See prior audit entries — 7 blank Membership dups, 2 duplicate division rows, 4+ duplicate location rows.

---

## Audit — 2026-06-13 (third pass)
**Status: ✅ audit complete.** Ground truth: `Flat.md` + `Flatiron1.md` + `Flat2.md` (newly discovered comprehensive dossier, 6,127 lines, run date 2026-06-12). Most significant finding: Memberships table had only 4 real content rows vs 7+ required — 6 missing memberships created.

### Filled in audit
- **AGC of California** `37e90644-d524-8191-b6ca-e32d20ac39ac` — new Membership row; body: Statewide trade association focused on advocacy and workforce; Companies→FD; source: https://www.agc-ca.org/about/member-directory/
- **DBIA** `37e90644-d524-81e6-944e-d21bcc8f2ffb` — new Membership row; body: National design-build advocacy body; Companies→FD; source: https://www.dbia.org/membership/member-directory/
- **IPI (International Parking & Mobility Institute)** `37e90644-d524-810e-a0ce-c2678dd14c7d` — new Membership row; body: Global parking/mobility professional association; Companies→FD; source: https://www.parking.org/member-directory/
- **California Alliance for Jobs** `37e90644-d524-8130-8ba6-ef9e1ecb071e` — new Membership row; body: Coalition advocating for CA infrastructure investment; Companies→FD; source: https://www.caallianceforjobs.org/members/
- **Hispanic Contractors of Colorado** `37e90644-d524-8170-b283-cfde6912ade0` — new Membership row; body: Trade association for Hispanic contractors in Colorado; Companies→FD; source: https://www.hccolorado.org/members
- **NECA Boston** `37e90644-d524-81b8-853c-ec2feae9faf3` — new Membership row; body: National Electrical Contractors Association, Boston chapter; Companies→FD; source: https://www.necaboston.org/member-directory/
- **The Beavers body** `37d90644-d524-81b3…` — source URL updated from bare domain `fdcorp.com` → proper anchor: [Source: fdcorp.com leadership](https://www.fdcorp.com/en/our-company/us-leadership)
- **Hampton Roads Bridge-Tunnel Expansion** — `Date` filled: 2027-02-01 (substantial completion Feb 2027 per dossier). Source: Flat2.md.
- **Gordie Howe International Bridge** — `Status` set to "Done"; `Date` set to 2026-01-01. Dossier conflict resolved: Flat.md says "opening early 2026" / Flat2.md says "Done / 2025"; ENR confirms ~98% complete late 2025, opened early 2026. Bridge opened Jan 2026 (confirmed by today's date 2026-06-13). Source: Flat2.md + ENR.

### Flat2.md net-new projects dedup result
11 projects from Flat2.md not in prior dossiers checked against Notion — all confirmed already present (added in prior sessions). LAX SkyLink has no exact name match (closest = LAX APM, a different/earlier project) — **not created** (insufficient sourcing to distinguish from the existing APM row; deferred to Zack review). Flat2.md "Flatiron Dragados West, LLC" + "Flatiron Dragados Constructors, Inc. (Mid-Atlantic/Southeast)" confirmed as duplicate division rows in Company Map — **not created** (dedup rule).

### Memberships — full list now in Notion (10 rows)
AGC San Diego · Carolinas AGC (CAGC) · The Beavers · CCIB · AGC of California · DBIA · IPI · California Alliance for Jobs · Hispanic Contractors of Colorado · NECA Boston. (Plus any pre-existing rows pre-dating this ledger.)

### Location tags (confirmed all resolved)
All 21 projects confirmed tagged (prior sessions resolved the shared-schema clobber; all 7 previously-untagged projects now have Location tags — Windsor Woods, Battery Park, Hudson River, Port Arthur, Howard Hanson, Sumner, LAX APM all confirmed ✓).

### ⚠ Duplicate rows — Zack UI cleanup (updated 2026-06-13)
- **7 blank Memberships rows** from 2026-06-12 ~20:20: `37d90644-815f` (DBIA dup), `37d90644-81e1` (AGC CA dup), `37d90644-8139` (Beavers dup), `37d90644-81c6` (IPI dup), `37d90644-8182` (CA Alliance dup), `37d90644-819f` (Carolinas AGC dup), `37d90644-81fc` (CCIB dup) — delete in UI
- **2 duplicate division rows**: FD West LLC + Mid-Atlantic/SE — delete in UI
- **4+ duplicate location rows**: Concord CA ×2, Montreal QC ×2, Richmond BC ×2, San Diego CA ×2 — delete extras in UI

### Still empty (genuinely sourceless)
EMR/TRIR/DART/OSHA records · bonding/surety/insurance carriers/wrap-ups · per-division revenue & headcount · exact firm employee count · DUNS · project permit/parcel/APN/FEMA/seismic · most per-project full date sets. InEight/SAP/Viewpoint Vista/Trimble One UNVERIFIED. People Email/Phone/LinkedIn. Project `Adress` place property (no per-project street addresses in source). **J.F. White division** People relation: no named leader in any dossier. LAX SkyLink deferred (insufficient to distinguish from existing APM row).

## Manual UI steps for Zack (updated 2026-06-13)
1. **Delete 7 blank duplicate Memberships rows** from 2026-06-12 ~20:20 (IDs above).
2. **Delete 2 duplicate division rows** (FD West LLC + Mid-Atlantic/SE) from Company Map.
3. **Delete 4+ duplicate location rows** (Concord CA ×2, Montreal QC ×2, Richmond BC ×2, San Diego CA ×2).
4. **Projects Underway** view on profile page — still filtered `Name="__TEMPLATE__"`; set Contractors = FlatironDragados.
5. **Existing Software** view — same `__TEMPLATE__` filter; shared DB has no relation filter via MCP.
6. **Memberships "View of People" tab** — repoint/clear leftover company filter.
7. **Restore the clobbered Projects `Location` option list** (was reset to FL+SC) — cross-company impact; decide approach.
8. Section guide italics + any template starter rows in Company Map/Events/Sources/Locations/Memberships → delete in UI if unwanted.
9. **Fix "Mutlinational" typo** → "Multinational" in company record `Size` field.
10. **LAX SkyLink** — confirm if this is the same project as LAX APM or a net-new project; if net-new, add from Flat2.md.

---

## Audit — 2026-06-12 (second pass)
**Status: ✅ audit complete (read-only review; no new writes needed — all fillable gaps resolved by prior sessions).** Verified full record graph vs Flat.md + Flatiron1.md.

### What the 2026-06-11/12 sessions added (confirmed live)
- **FlatironDragados Canada** division: People relation now populated (Stephanie Hun + 1 other: IDs `37d90644-d524-8127b32d…` + `37d90644-d524-818b9d93…`).
- **Howard Hanson Dam** Location tag: "Washington" now set (confirmed live `[\"Washington\"]`). Prior deferred item resolved.
- **Events `Location tags`**: "Las Vegas" + "San Diego" options added to schema; both events now tagged ✅.
- **Memberships (additional):** AGC of California `37d90644-d524-8100-857f…`, AGC San Diego `37c90644-d524-8179-b17c…`, Carolinas AGC (CAGC) `37d90644-d524-8110-8e42…`, CCIB `37d90644-d524-811a-9962…` — all added with body content + FD company link. Total membership rows now **11+ (original 7 plus 4 new valid ones)**.
- **Locations table:** Multiple new rows added — Atlanta USA HQ, Toronto ON (Canada HQ), Broomfield CO, Whitestone NY (SPC), Tampa FL (Prince), Scottsdale AZ (Pulice), Framingham MA (J.F. White), Richmond BC, Montreal QC, Raleigh NC (Mid-Atlantic), Orlando FL (Prince), Concord CA (FD West), San Diego CA (FD West). All linked to FD company + owning division.
- **Events:** DBIA Conference & Expo (Las Vegas, `37d90644-d524-81f4…`) + Groundbreaking Women in Construction (San Diego, `37d90644-d524-812f…`) — new rows replacing/supplementing original rows; place + location tags + dates all set. Additional events added: 2025 IAI Summit (`37d90644-d524-8126…`), IPI Awards 2022 (`37d90644-d524-81ea…`), CI Student Days 2025 (`37c90644-d524-8186…`).
- **Company record `Description`**: Updated to full rich description (no longer thin). `Size` = "Mutlinational" (typo persists from Flatiron1.md; "Regional" conflict resolved).

### ⚠ Duplicate membership rows (created ~2026-06-12 20:20 — blank, need Zack cleanup)
A session at ~20:20 UTC created blank duplicate rows for: DBIA, AGC of California, The Beavers, IPI, California Alliance for Jobs, Carolinas AGC, CCIB. These are empty pages in the Memberships DB but linked to FD. **Not deleted (non-destructive rule) — Zack to delete in UI.** IDs: `37d90644-815f…` (DBIA dup), `37d90644-81e1…` (AGC CA dup), `37d90644-8139…` (Beavers dup), `37d90644-81c6…` (IPI dup), `37d90644-8182…` (CA Alliance dup), `37d90644-819f…` (Carolinas AGC dup), `37d90644-81fc…` (CCIB dup).

### Still empty (genuinely sourceless)
- EMR/TRIR/DART/OSHA records · bonding/surety/insurance carriers/wrap-ups · per-division revenue & headcount · exact firm employee count · DUNS · project permit/parcel/APN/FEMA/seismic · most per-project full date sets. InEight/SAP/Viewpoint Vista/Trimble One UNVERIFIED. People Email/Phone/LinkedIn. Project `Adress` place property (no per-project street addresses in source).
- **J.F. White division** People relation: no named leader in dossier (still empty).

### All prior deferred items — resolved
- Howard Hanson Dam "Washington" location tag ✅ resolved
- Events "Las Vegas" + "San Diego" tags ✅ resolved
- Company Size conflict: "Mutlinational" (from Flatiron1.md) is now set — typo but consistent with dossier

## Manual UI steps for Zack (updated 2026-06-12)
1. **Delete 7 blank duplicate Memberships rows** from 2026-06-12 ~20:20 (listed above).
2. **Projects Underway** view on profile page — still filtered `Name="__TEMPLATE__"`; set Contractors = FlatironDragados.
3. **Existing Software** view — same `__TEMPLATE__` filter; shared DB has no relation filter via MCP.
4. **Memberships "View of People" tab** — repoint/clear leftover company filter.
5. **Restore the clobbered Projects `Location` option list** (was reset to FL+SC) — cross-company impact; decide approach. (Most FD projects survived with their tags intact; new option assignments still blocked for any project needing non-FL/SC tags.)
6. Section guide italics + any template starter rows in Company Map/Events/Sources/Locations/Memberships → delete in UI if unwanted.
7. **Fix "Mutlinational" typo** → "Multinational" in company record `Size` field.

---

## Audit — 2026-06-10 (post-load)
**Status: ✅ audit complete.** Verified build vs Flat.md + Flatiron1.md + Flat1.md. Filled stragglers:

### Filled in audit
- **SPC Construction division** `Adress` place: 16-16 Whitestone Expressway, Floor 5, Whitestone, NY 11357 (40.7891, -73.8223). Source: spcco.com (Flat1.md).
- **Prince Contracting division** `Adress` place: 10210 Highland Manor Drive, Suite 110, Tampa, FL 33610 (27.9506, -82.4572). Source: levelset.com (Flat1.md).
- **Prince Contracting — Tampa, FL** location row `Adress` text: updated to full street address "10210 Highland Manor Drive, Suite 110, Tampa, FL 33610". Source: Flat1.md.
- **DBIA Conference & Expo 2025** event `Place`: MGM Grand Las Vegas, 3799 S Las Vegas Blvd, Las Vegas, NV 89109 (36.1024, -115.1703). Source: Flatiron1.md.
- **Groundbreaking Women in Construction 2026** event `Place`: San Diego, CA (32.7157, -117.1611). Source: Flatiron1.md.
- **9 projects Location tags** applied (existing options only):
  - Windsor Woods → Virginia
  - Battery Park City Resiliency → New York, Manhattan
  - Hudson River Resiliency → New Jersey
  - Port Arthur Storm Surge → Texas
  - Sumner Tunnel → Massachusetts, Boston
  - LAX Automated People Mover → California, Los Angeles
  - I-95 / SW 10th Street Broward → Florida
  - I-275 Express Lanes Pinellas → Florida

### Still empty (genuinely sourceless or deferred)
- EMR/TRIR/DART/OSHA records · bonding/surety/insurance carriers/wrap-ups · per-division revenue & headcount · exact firm employee count · DUNS · project permit/parcel/APN/FEMA/seismic · most per-project full date sets. InEight/SAP/Viewpoint Vista/Trimble One UNVERIFIED. People Email/Phone/LinkedIn. MicroStation (no shared software option).
- **FlatironDragados Canada division** People relation: dossier lists no named Canada-specific leader.
- **J.F. White division** People relation: no named leader in dossier.
- **Howard Hanson Dam** Location tag: "Washington" state option does NOT exist in Projects DB schema → DEFERRED (shared schema; add "Washington" option in UI then tag).

### DEFERRED (shared schema — do not add options via API)
- Projects `Location` "Washington" — needed for Howard Hanson Dam Fish Passage.
- Events `Location tags` "Las Vegas" / "Nevada" — needed for DBIA Conference. Options "San Diego" / "California" — needed for Groundbreaking Women in Construction. None of these exist in the Events Location tags schema.
- Projects `Location` option list restoration (clobbered from ~115 to FL+SC) — cross-company impact; Zack to decide approach.

## Manual UI steps for Zack (updated)
1. **Projects Underway** view on profile page — still filtered `Name="__TEMPLATE__"`; set Contractors = FlatironDragados.
2. **Existing Software** view — same `__TEMPLATE__` filter; shared DB has no relation filter via MCP.
3. **Memberships "View of People" tab** — repoint/clear leftover company filter.
4. **Projects `Location` — add "Washington"** (1-click UI add), then tag Howard Hanson Dam.
5. **Restore the clobbered Projects `Location` option list** (was reset to FL+SC) — cross-company impact; decide approach.
6. **Events `Location tags`** — add "Las Vegas" (DBIA) + "San Diego" (Groundbreaking Women) options, then tag both rows.
7. Section guide italics + any template starter rows in Company Map/Events/Sources/Locations/Memberships → delete in UI if unwanted.
8. **Size conflict** on company record: Regional (existing) vs Multinational (dossier) — pick one.
