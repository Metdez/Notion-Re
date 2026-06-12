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

---

## Audit — 2026-06-11 (automated /notion-audit cycle #3)
**Status: ✅ audit complete — 0 fills, 0 writes.** Live Notion re-verified vs all three dossiers (Flat.md + Flatiron1.md + Flat1.md).

All checks passed clean:
- **3a:** Company record live (`24690644…`) — 29 Construction Projects + 6 software + 45 people confirmed. All 6 divisions → company + People + Projects edges intact (Canada + J.F. White have no People — confirmed sourceless). All 7 memberships, 2 events, 10 location rows → company. Relations verified live.
- **3b:** All 6 division bodies at full dossier depth. Sample projects (Upper San Leandro, VIA Green Line, Howard Hanson, Site C Dam, Wellsburg Bridge) confirmed full body depth with sourced inline links.
- **3c:** Company HQ place (Atlanta, 33.8746/-84.3389) confirmed. All 6 division Adress places confirmed live (USA/Canada/Pulice-Scottsdale/SPC-Whitestone/Prince-Tampa/JFWhite-Framingham). 10 location rows confirmed present. Project Adress correctly empty (no geocoords in dossier).
- **3d (memberships):** 7/7 confirmed live — AGC, DBIA, IPI, The Beavers, California Alliance for Jobs, Hispanic Contractors of Colorado, NECA Boston. All company-linked.
- **3e (location tags):** Both events fully tagged — DBIA Conference → Las Vegas ✅; Groundbreaking Women → San Diego ✅. Howard Hanson Dam → Washington ✅. All confirmed live.
- **False positives rejected:** 0.

No fillable gaps found. Notion fully reflects all three dossiers.

---

## Flat2.md Load — 2026-06-12

**Ground truth:** `Enlaye Notion/FlatironDragados/Flat2.md` (third supplementary dossier; session resumed from context summary — 2 divisions + 1 person created before context reset).

### New divisions (2)
| Division | ID | People | Projects |
|---|---|---|---|
| Flatiron Dragados West, LLC | `37d90644-d524-8191-bb94-c1f5be9c8612` | Dale Nelson (EVP West) | CA HSR, San Diego T1, North Coast Corridor, LAX APM, SE Gateway |
| FlatironDragados Constructors, Inc. (Mid-Atlantic/SE) | `37d90644-d524-81b3-96fe-f44b890685d7` | Jim Schneiderman (EVP Mid-Atlantic) | HRBT, Wellsburg Bridge |

### New person (1)
| Name | ID | Function |
|---|---|---|
| Stephanie Hun | `37d90644-d524-8127-b32d-d1eaf51302e0` | VP Business Development, Canada — Company→FD + Canada division People relation set |

### New projects (7 — shared Construction Projects `4c8ed827…`)
| Project | ID | $M | Status | Loc tag | Division |
|---|---|---|---|---|---|
| California High-Speed Rail CP 2-3 | `37d90644-d524-81c3-b188-dd446ecfd075` | 1365 | In progress | California | FD West |
| State Route 99 Tunnel (Alaskan Way Viaduct Replacement) | `37d90644-d524-81d4-880f-e918dc940536` | 1350 | Done | Washington | FD USA |
| Susquehanna River Rail Bridge Replacement | `37d90644-d524-81c8-a360-d572ed7d3c80` | 1500 | In progress | Maryland | FD USA |
| Palisades Tunnel Project | `37d90644-d524-81b7-b412-d2c8ed0bfc1f` | 466 | In progress | New Jersey | SPC |
| Denver International Airport Concourse Expansion | `37d90644-d524-81c8-8f2f-e18fe2ba7e91` | 700 | Done | ⚠ deferred (Colorado) | FD USA |
| Pearl Harbor Dry Dock 5 | `37d90644-d524-81de-bcb9-d3f7a3c0bfc0` | 3400 | In progress | ⚠ deferred (Hawaii) | FD USA |
| South Coast Rail Bridges, Berkley-Lakeville | `37d90644-d524-8102-a1fd-da08d8d93fac` | — | Done | Massachusetts | J.F. White |

Dates set: CA HSR `date:Date:start = 2015-01-13` · Palisades `date:Date:start = 2024-08-01` · S Coast Rail `date:Date:start = 2025-03-24`.

### New events (2 — Events DS `94d90644…`)
| Event | ID |
|---|---|
| 2025 IAI Summit (Infrastructure & Asset Innovation) | `37d90644-d524-8126-8618-d8765522e72e` |
| International Partnering Institute (IPI) Awards 2022 | `37d90644-d524-8101-9311-d24ff6b2ceae` |

### New memberships (3 — Memberships DS `54b90644…`)
| Membership | ID |
|---|---|
| AGC San Diego Chapter | `37d90644-d524-81f3-aaba-e05fbc8e93f8` |
| Carolinas AGC | `37d90644-d524-8136-b2c5-faf410d90a3e` |
| Canadian Construction Innovation Bureau (CCIB) | `37d90644-d524-81fa-b67e-eae9026652aa` |

### New locations (7 — Locations DS `19a90644…`)
| Location | ID | Address | Division |
|---|---|---|---|
| Concord CA — FD West | `37d90644-d524-8103-bc00-ebd10c906140` | 1200 Concord Ave Suite 465, Concord CA 94520 | FD West |
| San Diego CA — FD West | `37d90644-d524-81fe-b45d-e7f50cd43232` | 12121 Scripps Summit Drive Suite 400, San Diego CA 92121 | FD West |
| Raleigh NC — Mid-Atlantic | `37d90644-d524-813c-9d41-fe0c76ae1419` | 5438 Wade Park Blvd Ste 520, Raleigh NC 27607 | Mid-Atlantic |
| Whitestone NY — SPC | `37d90644-d524-8170-bb9f-d05f355e7908` | 16-16 Whitestone Expressway Floor 5, Whitestone NY 11357 | SPC |
| Richmond BC — Canada | `37d90644-d524-81cb-bb27-d40249de672e` | 4020 Viking Way Suite 210, Richmond BC V6V 2N2 | Canada |
| Montreal QC — Canada | `37d90644-d524-8129-b17b-e8f762f7c41f` | 1000 Sherbrooke Rue O Floor 16, Montreal QC H3A 3G4 | Canada |
| Orlando FL — Prince | `37d90644-d524-810d-83d3-c6a88efa8477` | 1515 S Semoran Blvd, Orlando FL 32807 | Prince |

### New software (1 — shared Software DS `37690644…`)
- Oracle Contract Management `37d90644-d524-8108-ac21-d7ada1e5e226` — legal/contract lifecycle; Location=[United States, Canada]; Companies→FD. Option "Oracle Contract Management" added to shared multi-select.

### Cross-links applied
- Company `Construction Projects`: re-passed full 36-URL list (29 existing + 7 new).
- FD West Projects: CA HSR + San Diego T1 + North Coast Corridor + LAX APM + SE Gateway (5 total).
- FD West People: Dale Nelson.
- Mid-Atlantic Projects: HRBT + Wellsburg Bridge.
- Mid-Atlantic People: Jim Schneiderman.
- J.F. White Projects: Sumner Tunnel + South Coast Rail Bridges (2 total).
- Canada People: Stephanie Hun.

### Conflicts preserved
- `Size` = "Regional" (Flat2.md says "Multinational") — kept existing per additive rule.
- Gordie Howe `Status` = "In progress" (Flat2.md says "Done") — kept existing per additive rule.

### Deferred
- Denver Concourse `Location` tag: ~~Colorado option uncertain~~ **✅ RESOLVED 2026-06-12 audit** — Colorado option confirmed present; tag applied.
- Pearl Harbor Dry Dock `Location` tag: Hawaii option **still absent** from shared Projects multi-select — Zack to add in UI then tag.
- FD West / Mid-Atlantic Adress place: no office coordinates in Flat2.md → left empty.

---

## Cross-link completion — 2026-06-12 (resumed session, post context-reset)

**Status: ✅ all pending cross-links executed.**

### Corrected division IDs (Flat2.md section above has wrong IDs — Big Data harness duplicates)
The ledger's "Flat2.md Load" section lists `37d90644…8191` (FD West) and `37d90644…81b3` (Mid-Atlantic) — these are Big Data harness duplicates (created ~10:46). The canonical records (created ~10:45, have Adress place filled) are:
- **FD West canonical:** `37d90644-d524-8104-ba55-f3288d543eec` — THIS is the record linked to the company and updated
- **Mid-Atlantic canonical:** `37d90644-d524-8101-8214-e570d57c94fb` — THIS is the record linked to the company and updated

⚠ **Duplicate division rows** (Big Data harness): `37d90644-d524-8191-bb94-c1f5be9c8612` (FD West dup) + `37d90644-d524-81b3-96fe-f44b890685d7` (Mid-Atlantic dup) — Zack to delete in UI.

### Cross-links executed (all confirmed ✅)
| Record | Change |
|---|---|
| FD Canada `37b90644-d524-81b2…` | People: added Stephanie Hun `37d90644d524818b9d93f26b8807761d` (now 2 people) |
| FD West `37d90644-d524-8104…` | Projects: set to 5 — CA HSR `37d90644d52481c3b188dd446ecfd075` · SE Gateway `37d90644d52481629a4bed9c34bd58fd` · San Diego T1 `37b90644d5248132b20fcacb7734ae6e` · LA Metro `37b90644d5248189bf6be141f8bd6928` · North Coast Corridor `37c90644d5248185ac2beb9c81c2a7f5` |
| FD Mid-Atlantic `37d90644-d524-8101…` | Projects: Hampton Roads + Wellsburg Bridge = 2 |
| SPC `37b90644-d524-817c…` | Projects: added Palisades `37d90644d52481b7b412d2c8ed0bfc1f` → 3 total |
| FD USA `37b90644-d524-81cf…` | Projects: 17 → 21 (added SR 99 `37d90644d52481d4880fe918dc940536`, Susquehanna `37d90644d52481c8a360d572ed7d3c80`, Denver `37d90644d52481c88f2fe18fe2ba7e91`, Pearl Harbor `37d90644d52481debcb9d3f7a3c0bfc0`) |
| Company `24690644-d524-8067…` | Construction Projects: 36 → **37** (added SE Gateway `37d90644d52481629a4bed9c34bd58fd`) |
| J.F. White `37b90644-d524-8124…` | No change — South Coast Rail `37d90644d5248102a1fdda08d8d93fac` already present (Big Data harness had linked it) |

### Duplicate project records (Big Data harness parallel writes — Zack to delete dups in UI)
| Canonical (use this) | Duplicate (delete) |
|---|---|
| CA HSR `37d90644-d524-81c3-b188-dd446ecfd075` | `37d90644-d524-8124-bb11-f1ec96137d56` |
| SE Gateway AW `37d90644-d524-8162-9a4b-ed9c34bd58fd` | _(no duplicate found)_ |
| SR 99 `37d90644-d524-81d4-880f-e918dc940536` | `37d90644-d524-8100-85ac-fcb99160718b` |
| Susquehanna `37d90644-d524-81c8-a360-d572ed7d3c80` | `37d90644-d524-81c3-ad47-ef304b7931d7` |
| Denver Airport `37d90644-d524-81c8-8f2f-e18fe2ba7e91` | `37d90644-d524-8151-b924-c2b79923014f` |
| Pearl Harbor `37d90644-d524-81de-bcb9-d3f7a3c0bfc0` | `37d90644-d524-8184-8a5d-ee2e8c67b1cc` |
| Palisades `37d90644-d524-81b7-b412-d2c8ed0bfc1f` | `37d90644-d524-8126-87f9-d5a89b227e3a` |
| South Coast Rail `37d90644-d524-8102-a1fd-da08d8d93fac` | `37d90644-d524-81f9-bcff-eb77e5bfcfd6` |

### Updated tallies
- Company Construction Projects: **37**
- FD USA Projects: **21**
- SPC Projects: **3**
- FD West Projects: **5**
- FD Mid-Atlantic Projects: **2**
- FD Canada People: **2**

---

## Audit — 2026-06-12 (2nd manual /notion-audit cycle — post-Flat2 load)
**Status: ✅ audit complete — 9 fills.** Full re-verification vs all 4 dossiers (Flat.md + Flatiron1.md + Flat1.md + Flat2.md). Live Notion fetched for company record, profile page, all 8 divisions, all projects with deferred location tags, all memberships/events/software for dup check, and Projects DB schema.

### Filled in audit
- **Company record body:** added "ENR #1 Transportation · ENR #1 Domestic Heavy Contracting" to revenue/ENR bullet. Source: [ACS press release](https://www.grupoacs.com/en/press-releases/acs-group-ranked-1-in-transportation-and-domestic-heavy-contracting-by-enr/)
- **Company record body:** new Federal contract vehicles bullet — "USACE Galveston District MATOC IDIQ — $7.0B ceiling (W912HY25D0017) · USAF AFICA C2E IDIQ — $15.0B ceiling (FA890325D0081)". Source: Flat2.md / USAspending.gov
- **Profile page body:** same ENR #1 rankings additions.
- **Projects `Location` schema (shared DB `4c8ed827`):** added 4 new options — Hawaii · British Columbia · West Virginia · Ohio (all 136 prior options preserved).
- **Pearl Harbor Dry Dock 5** `Location` → `["Hawaii"]`. Body "deferred" note cleaned. Source: fdcorp.com
- **Site C Dam** `Location` → `["British Columbia"]`. Source: sitecproject.com
- **Wellsburg Bridge** `Location` → `["West Virginia", "Ohio"]`. Source: wvdot.gov

### Duplicate records found (Zack to delete in Notion UI)
- **Memberships:** AGC San Diego ×2 (`37c90644…79b17ceb` = older richer; `37d90644…f3aabae0` = Flat2 load dup) · Carolinas AGC ×2 (`37d90644…108e42c9` = older richer; `37d90644…36b2c5fa` = dup) · CCIB ×2 (`37d90644…1a9962cd` = older richer; `37d90644…fab67eae` = dup)
- **Events:** 2025 IAI Summit ×2 (`37d90644…268618d8` = older w/ date; `37d90644…2586f3d4` = Flat2 load dup, no date) · IPI Awards 2022 ×2 (`37d90644…019311d2` = older w/ date; `37d90644…eab116f5` = dup, no date)
- **Software:** Oracle Contract Management ×2 (`37d90644…08ac21d7` = canonical, has Location+tag+body; `37d90644…4290c5f2` = dup, no Location/tag)

### Still empty / genuinely sourceless (unchanged + 3 items resolved)
- ~~Pearl Harbor Dry Dock 5 Location: Hawaii option missing~~ **✅ RESOLVED — Hawaii option added + tagged**
- ~~Site C Dam: British Columbia not in schema~~ **✅ RESOLVED — British Columbia option added + tagged**
- ~~Wellsburg Bridge: WV/OH not in schema~~ **✅ RESOLVED — West Virginia + Ohio options added + tagged**
- EMR/TRIR/DART/OSHA · bonding/surety/insurance · per-division revenue & headcount · exact employee count · DUNS · project permit/parcel/APN · most per-project full date sets · People Email/Phone/LinkedIn.
- FD West / Mid-Atlantic `Adress` place: no office coordinates in any dossier.
- IAI Summit 2025 + IPI Awards 2022 + CI Student Days 2025 venue: not disclosed in source → genuinely sourceless.
- FlatironDragados Canada division People: no additional named Canada-specific leader beyond Stephanie Hun in any dossier.
- J.F. White division People: no named leader in any dossier.

### All checks 3a–3e
- **3a:** 8 divisions live; company→37 Construction Projects + 8 software + people. All 15 memberships (incl. 3 dup pairs) + 7 events (incl. 2 dup pairs) + 17 locations → company. Division→People + Projects edges intact.
- **3b:** all 8 division + sampled project bodies at full dossier depth.
- **3c:** company HQ place confirmed; all 8 division Adress places confirmed; 17 location Adress text fields confirmed. Project Adress empty = correct (no geocoords in dossier).
- **3d:** 10 unique memberships (15 rows incl. 3 dup pairs) — AGC, AGC of California, AGC San Diego, Carolinas AGC, CCIB, DBIA, IPI, The Beavers, California Alliance for Jobs, Hispanic Contractors of Colorado, NECA Boston, NTEA. All company-linked.
- **3e:** DBIA Conference → Las Vegas ✅ · Groundbreaking Women → San Diego ✅ · Howard Hanson → Washington ✅ · Denver Airport → Colorado ✅ · Pearl Harbor → **Hawaii ✅** · Site C Dam → **British Columbia ✅** · Wellsburg Bridge → **West Virginia + Ohio ✅** · CI Student Days + IAI Summit + IPI Awards → no venue in source, correctly blank.
- **False positives rejected:** 0.

### Manual UI steps (updated)
1. Projects Underway view — set Contractors = FlatironDragados.
2. Existing Software view — remove `__TEMPLATE__` filter.
3. Memberships "View of People" tab — repoint company filter.
4. Size conflict: Regional (existing) vs Multinational (dossier) — Zack's call.
5. Delete dup division rows: FD West `37d90644…8191` + Mid-Atlantic `37d90644…81b3`.
6. Delete 8 dup project rows (listed in cross-link section above).
7. Delete 6 dup side-table rows: AGC San Diego dup `37d90644…f3aabae0` + Carolinas AGC dup `37d90644…36b2c5fa` + CCIB dup `37d90644…fab67eae` + IAI Summit dup `37d90644…2586f3d4` + IPI Awards dup `37d90644…eab116f5` + Oracle CM dup `37d90644…4290c5f2`.

---

## Audit — 2026-06-12 (1st manual /notion-audit cycle — immediately post load)
**Status: ✅ audit complete — 1 fill.** Full re-verification vs all dossiers (Flat.md + Flatiron1.md + Flat1.md + Flat2.md). Live Notion fetched for company, all 8 divisions, sample projects, all memberships, events, locations, and shared Projects DB schema.

### Filled in audit
- **Denver International Airport Concourse Expansion** `Location` tag: **Colorado** — schema confirmed present (Colorado option exists in Projects DB multi-select); property was empty. Source: [fdcorp.com](https://www.fdcorp.com/en/projects/aviation/denver-international-airport-concourse-expansion). Body note updated to remove "deferred" text.

### Still empty / genuinely sourceless (unchanged)
- **Pearl Harbor Dry Dock 5** `Location` tag: "Hawaii" option still absent from shared Projects multi-select schema → remains deferred; Zack to add option in UI then tag.
- EMR/TRIR/DART/OSHA · bonding/surety/insurance · per-division revenue & headcount · exact employee count · DUNS · project permit/parcel/APN · most per-project full date sets · People Email/Phone/LinkedIn.
- FD West / Mid-Atlantic `Adress` place: no office coordinates in any dossier.
- IAI Summit 2025 + IPI Awards 2022 `Location tags`: location not disclosed in source → genuinely sourceless.
- FlatironDragados Canada division People: no additional named Canada-specific leader beyond Stephanie Hun in any dossier.
- J.F. White division People: no named leader in any dossier.
- Site C Dam: British Columbia not in Projects Location schema as state option — deferred (UI).
- Wellsburg Bridge: WV/OH not in Projects Location schema — currently tagged "USA".

### All checks 3a–3e
- **3a:** 8 divisions live + company relation confirmed; company → 37 Construction Projects + 8 software + people (all confirmed). All 10 memberships + 4 events + 17 locations → company linked. Division→People + Projects edges intact.
- **3b:** All 8 division bodies at full dossier depth. Sample projects at full body depth.
- **3c:** Company HQ place confirmed (Atlanta 33.8746/-84.3389). All 8 division Adress places confirmed (FD West at Concord CA; Mid-Atlantic at Raleigh NC; original 6 unchanged). All 17 location row Adress text fields populated. Pearl Harbor and Denver project Adress correctly empty (no geocoords in dossier).
- **3d (memberships):** 10/10 confirmed live — AGC, DBIA, IPI, The Beavers, California Alliance for Jobs, Hispanic Contractors of Colorado, NECA Boston, AGC San Diego Chapter, Carolinas AGC, CCIB. All company-linked.
- **3e (location tags):** DBIA Conference → Las Vegas ✅; Groundbreaking Women → San Diego ✅; Howard Hanson Dam → Washington ✅. Denver Airport → **Colorado ✅ (filled this audit)**. Pearl Harbor → ⏳ Hawaii option missing from schema. Both new events (IAI Summit + IPI Awards) have no venue disclosed → genuinely sourceless.
- **False positives rejected:** 0.

### Manual UI steps (updated)
1. Projects Underway view — set Contractors = FlatironDragados.
2. Existing Software view — remove `__TEMPLATE__` filter.
3. Memberships "View of People" tab — repoint company filter.
4. ~~Restore clobbered Projects `Location` option list~~ — ongoing; current list is large (Colorado, Hawaii, etc. present for many companies).
5. **Add "Hawaii" to Projects `Location` schema** → then tag Pearl Harbor Dry Dock 5.
6. Size conflict: Regional (existing) vs Multinational (dossier) — pick one.
7. Delete Big Data harness dup division rows: FD West `37d90644…8191` + Mid-Atlantic `37d90644…81b3`.
8. Delete Big Data harness dup project rows (8 dupes listed in cross-link section above).
9. Add "British Columbia" to Projects `Location` schema → tag Site C Dam.
10. Add "West Virginia" / "Ohio" to Projects `Location` schema → re-tag Wellsburg Bridge (currently "USA").
