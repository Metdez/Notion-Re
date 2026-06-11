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

## Audit — 2026-06-11 (automated hourly cycle)
**Status: ✅ audit complete — 0 fills, 0 writes.** Full re-verification vs Flat.md + Flatiron1.md.

All checks passed clean:
- **3a:** all 6 division→company + People + Projects edges live; company→21 projects; all side-tables→company.
- **3b:** all division + project bodies at full dossier depth.
- **3c:** all 6 division Adress places confirmed; company HQ place confirmed. Project Adress correctly empty (no-geocoding rule — no project coordinates in dossier).
- **3d (memberships):** 7/7 present and company-linked.
- **3e (location tags):** both events fully tagged (Las Vegas / San Diego). Howard Hanson Dam `Location`=`["Washington"]` confirmed set — the deferred 06-10 item was resolved by a subsequent session adding the Washington option to the shared Projects multi-select.

**Deferred items resolved since 06-10:**
- Howard Hanson Dam "Washington" Location tag: ✅ NOW SET.
- DBIA Conference "Las Vegas" location tag: ✅ NOW SET.
- Groundbreaking Women "San Diego" location tag: ✅ NOW SET.

**Manual UI steps (updated — items 4/6 resolved; remaining):**
1. Projects Underway view — set Contractors = FlatironDragados.
2. Existing Software view — remove `__TEMPLATE__` filter.
3. Memberships "View of People" tab — repoint company filter.
4. ~~Projects `Location` — add "Washington" + tag Howard Hanson~~ ✅ DONE.
5. Restore the clobbered Projects `Location` option list (was ~115, reset to FL+SC) — cross-company impact; Zack's call.
6. ~~Events `Location tags` — add "Las Vegas" + "San Diego"~~ ✅ DONE.
7. Section guide italics + template starter rows → delete in UI if unwanted.
8. Size conflict: Regional (existing) vs Multinational (dossier) — pick one.

---

## Audit — 2026-06-11 (automated /notion-audit cycle #2)
**Status: ✅ audit complete — 0 fills, 0 writes.** Full re-verification vs Flat.md + Flatiron1.md + Flat1.md (all three dossiers).

All checks passed clean:
- **3a:** 6 divisions live (+ TEMPLATE stub skipped); all division→company, People, Projects edges confirmed. Company record → 29 Construction Projects + 6 software + 45 people. All 7 memberships, 2 events, 10 location rows → company.
- **3b:** all division and project bodies at full dossier depth (Flat.md + Flatiron1.md + Flat1.md).
- **3c:** company HQ place (Atlanta, 33.8746/-84.3389) confirmed. All 6 division Adress places set (USA/Canada/Pulice/JFWhite/Prince/SPC). All 10 location row Adress text fields populated. Project Adress correctly empty — no geocoords in dossier.
- **3d (memberships):** 7/7 present (AGC, DBIA, IPI, The Beavers, California Alliance for Jobs, Hispanic Contractors of Colorado, NECA Boston) — all company-linked.
- **3e (location tags):** both events fully tagged — DBIA Conference → Las Vegas; Groundbreaking Women → San Diego. Both confirmed live.
- **False positives rejected:** 0 (no sub-agent hallucinations detected).

No fillable gaps found. All sourced data from all three dossiers is reflected in Notion.

---

## Audit — 2026-06-11 (manual /notion-audit from Flat1.md)
**Status: ✅ audit complete — 13 new records created.** Full re-verification of all checks 3a–3e; discovered 8 projects + 4 locations + 1 software row sourced in Flat1.md but not previously loaded.

### Filled in audit
**8 new projects** (Contractors→FD; company Construction Projects relation updated to 29 total):
| Project | ID | $M | Status | Location tag |
|---|---|---|---|---|
| Upper San Leandro Water Treatment Plant | `37c90644-d524-81f6…` | 237 | In progress | California |
| Isabella Lake Dam Safety Modification | `37c90644-d524-814e…` | 204 | Done | California |
| Wellsburg Bridge | `37c90644-d524-810d…` | 131 | Done | USA |
| North Coast Corridor | `37c90644-d524-8185…` | 860 | In progress | California, San Diego |
| US 50 Multimodal Corridor Enhancement | `37c90644-d524-81ae…` | 460 | In progress | California |
| Site C Dam — Generating Station & Spillway Civil Works | `37c90644-d524-819c…` | — | Done | Canada |
| I-10 Broadway Curve Improvement | `37c90644-d524-8122…` | — | Done | Arizona |
| VIA Rapid Green Line | `37c90644-d524-8106…` | 446 | In progress | Texas |

**4 new location rows** (Companies full database→FD; Division linked):
| Location | ID | Address | Division |
|---|---|---|---|
| Prince Contracting — Winter Garden, FL | `37c90644-d524-8134…` | 13640 W Colonial Dr, Suite 130B, Winter Garden FL 34787 | Prince Contracting |
| Pulice — Irving, TX (North Texas Office) | `37c90644-d524-81f2…` | 1320 Greenway Dr, Suite 815, Irving TX 75038 | Pulice |
| Pulice — Houston, TX (South Texas Office) | `37c90644-d524-819c…` | 2050 W. Sam Houston Pkwy S., Suite 825, Houston TX 77042 | Pulice |
| SPC Construction — Secaucus, NJ | `37c90644-d524-8153…` | 150 Meadowlands Pkwy, Floor 2, Secaucus NJ 07094 | SPC Construction |

**1 new software row** (Companies full database→FD):
- HCSS HeavyJob (FlatironDragados) `37c90644-d524-8147…` — field/job-costing; moderate confidence (TrustRadius — FD Corporate Apps Mgr). Source: https://www.trustradius.com/products/hcss/reviews

### Still empty / genuinely sourceless (unchanged from prior audit)
- EMR/TRIR/DART/OSHA · bonding/surety/insurance · per-division revenue & headcount · exact employee count · DUNS · project permit/parcel/APN · most per-project full date sets · People Email/Phone/LinkedIn.
- FlatironDragados Canada division People relation: no named Canada-specific leader in any dossier.
- J.F. White division People relation: no named leader in any dossier.
- Site C Dam: no $ value in sources; Location tag = Canada (British Columbia not in schema — deferred).
- Wellsburg Bridge: WV/OH not in Location schema as state options; "USA" used as fallback.
- I-10 Broadway Curve: no $ value in Flat1.md sources.

### Manual UI steps (updated)
1. Projects Underway view — set Contractors = FlatironDragados.
2. Existing Software view — remove `__TEMPLATE__` filter.
3. Memberships "View of People" tab — repoint company filter.
4. Restore the clobbered Projects `Location` option list (was ~115, reset to FL+SC) — cross-company impact; Zack's call.
5. Size conflict: Regional (existing) vs Multinational (dossier) — pick one.
6. Projects Location schema: add "British Columbia" option for Site C Dam; add "West Virginia"/"Ohio" for Wellsburg Bridge (currently tagged "USA").
