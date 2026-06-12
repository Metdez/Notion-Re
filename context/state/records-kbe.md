# State · Records — KBE Building Corporation

> **Holds:** the KBE dedup ledger — every record created/updated loading the KBE dossier onto the pre-existing (06-05→06-09) build, with Notion IDs, so the next session deduplicates before touching a KBE record.
> **Ground truth:** `Enlaye Notion/KBE Building/KBE.md` (KBE1.md is empty/0 bytes). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.

---

## Situation (2026-06-10)
KBE was **NOT a blank slate.** An earlier pass (06-05→06-09, LinkedIn-scraped + template) already built most of the structure. The 06-10 dossier load is an **additive gap-fill**: fill empty company fields, add ~9 net-new sourced projects, add leadership people (dedup vs ~180 existing), enrich divisions, add events/memberships/software/sources, complete interlink.

## Profile hub page
**"KBE"** `37690644-d524-809e-801e-ff5cfed1cb11` (Market Research → Zack Folder → Companies research). Inline page-local DBs:
- **Company Map** (divisions) = `collection://37690644-d524-8088-abd7-000b818a9b6b` (aka the "Zack Database" relation on Companies; props: Division title · Companies full database rel · People rel · Projects rel · Adress place). Body per row: Bio/Comments/Tasks/Tickets.
- **Linkedin Post** `collection://37890644-d524-80ba-90ea-000b9966d7b5`
- **Events** `collection://37690644-d524-80cb-82b1-000b78799305` (= "Untitled Database" rel on Companies)
- unlabeled DB `collection://37690644-d524-805b-bdeb-000b6591168e`
- **Locations** `collection://37690644-d524-803c-b832-000b0ca49c9e`
- **Projects Underway** = linked view of shared Construction Projects
- **Memberships** `collection://37690644-d524-80b0-b5eb-000b53bf2cd2`
- **Existing Software** = linked view of shared Companies Software `collection://37690644-d524-804f-b966-000b34a1901b`

## Company record (EXISTING — extend, do not recreate)
**"KBE Building Corporation"** `1cf90644-d524-802a-ac06-ea175f0df1fe` in Companies DB (`041b7f07`). Pre-existing: BW=Builder · Country=[Connecticut, USA] · LinkedIn + Website filled · Size=**Local** · icon set · ~180 People + ~93 Linkedin relations · 3 divisions in Zack Database.
- ⚠ **Size = "Local" kept** — dossier says "Regional" (ENR Top 400 #340 2025). Conflict preserved per additive rule.
- Empty at start: Description · Address (place) · Type · Construction Projects relation · body (blank).

## Divisions (Company Map `37690644-d524-8088`)
| Division | ID | Notes |
|---|---|---|
| KBE Northeast | 37690644-d524-8037-9e13-d6cb17496a29 | addr=76 Batterson Park Rd Farmington; 63 people; 7 projects |
| KBE Mid-Atlantic | 37690644-d524-807c-b12d-c54c53169266 | real row (Zack Database rel on company) |
| KBE West | 37690644-d524-80e6-ab40-c28652977ea5 | real row (Zack Database rel on company) |

**Stray/ignore:** "KBE Northeast" `72d90644-d524-8227` and "KBE Mid-Atlantic" `13090644-d524-8352` live under page **"TEMPLATE — old data (safe to delete)"** `37a90644-d524-818c` — do not touch/link.

## Existing projects (Construction Projects `4c8ed827`; Contractors→KBE `1cf9…`; Zack Database→NE)
| Project | ID | Matches dossier? |
|---|---|---|
| Bradley Airport GTC ($210M, Transportation, Done) | 37790644-d524-81c1-a96d-c220e974a666 | NE bonus (not detailed in dossier) |
| UConn Connecticut Hall | 37790644-d524-8177-abec-e8782c06a3c8 | ✓ dossier |
| Bard College Passive House Dorms | 37790644-d524-8164-b13c-f15d2d8d1d6f | ✓ dossier (Annandale) |
| Stonington Village ($41M) | 37790644-d524-81c1-a60a-ca329edc8c06 | ✓ dossier |
| Jefferson's Ferry Expansion | 37790644-d524-81f6-8bf4-eb2a72f60841 | ✓ dossier |
| UConn Jones Lab Reno | 37790644-d524-81d2-b166-e2b57eb62019 | ✓ dossier |
| SUNY Binghamton Grace Hall | 37790644-d524-81d6-b83f-da137b7d94af | ✓ dossier |
Mid-Atlantic projects also already exist: Harbor Place Baltimore `37790644-d524-8176-981c-d7384d3db224`, Catholic Univ Athletic Fields `37790644-d524-812c-8886-fb2147a87024` (more likely — search before creating any Mid-Atlantic project).

## NET-NEW dossier projects to create (dedup by name first!)
The August at Steelpointe Harbor ($190M) · Mozaic Concierge Living · Sunrise Senior Living Tarrytown · Wampanoag Country Club Clubhouse · Residence Inn by Marriott (Steelpointe) · UConn Health ED Expansion · Waterside District (Norfolk) · Annapolis Joint Commissary & Navy Exchange ($27M) · NASCAR Clash at LA Coliseum.

## People (dedup vs ~180 existing!)
Michael Kolakowski (CEO) EXISTS `37790644-d524-8101-914b-f2dafad69d75`. Leadership to dedup/add: James Culkin (COO/EVP) · Timothy O'Brien (CFO/EVP) · Robert Dunn (VP/GC) · Adam Peters (Safety Dir) · division leaders (Maselli, Mancini, Haught, Boscardin, Darling, Nydahl).

## Created / updated this load (2026-06-10)
**Company record updated** (`1cf90644`): filled Description · Type=Company · Country +Maryland/Arizona/Virginia/New York/Tennessee · Address place (Farmington HQ) · Company Snapshot+Leadership+Safety+Risk+Sources body · **Construction Projects relation set to 19 URLs** (one-way). Size=Local kept (conflict w/ dossier Regional).

**7 net-new projects created** (Contractors→KBE, Zack Database→division, sourced briefs, varied building_* icons):
| Project | ID | Division |
|---|---|---|
| The August at Steelpointe Harbor ($190M) | 37b90644-d524-814c-8f8c-eef22ede8819 | NE |
| Sunrise Senior Living (Tarrytown) | 37b90644-d524-81db-990d-dfaa03247034 | NE |
| Wampanoag Country Club Clubhouse | 37b90644-d524-815b-bcce-ddfb2dd02e3f | NE |
| Residence Inn by Marriott (Steelpointe) | 37b90644-d524-81e4-b0d9-df4a188c2d47 | NE |
| UConn Health Emergency Department Expansion | 37b90644-d524-8120-abf5-fb5d0ce9e16e | NE |
| Annapolis Joint Commissary & Navy Exchange ($27M) | 37b90644-d524-8190-ba8a-cccafb900166 | Mid-Atlantic |
| NASCAR Clash at LA Memorial Coliseum | 37b90644-d524-816a-be11-d76de2698637 | West |

**6 memberships created** (Memberships DB `37690644-d524-80b0` — **added `Companies full database` relation column**, pre-authorized; each linked KBE, sourced body): ABC-CT `37b90644-d524-815f` · ABC Metro Washington `…8180` · ABC Baltimore/Chesapeake `…8152` · Arizona Builders Alliance `…81d0` · CBC `…81a2` · Stamford Chamber `…81c9`.

**2 events created** (Events DB `37690644-d524-80cb`, linked KBE): KBE Annual Golf Tournament `37b90644-d524-81ef-9445-ec9c7a745596` · CBC Project Team Awards `37b90644-d524-8153-836e-d8185e86f991`. (ABC-CT EIC Awards + Women in Construction already existed → not duplicated.)

**3 division Bios added** (NE/MA/West Company Map rows): focus, offices, leaders, notable projects.

**Mozaic linked to NE** (`…81d1` Zack Database += NE division).

## ⚠ Data-quality issues found in pre-existing build (NOT auto-fixed — flag for Zack)
- **Mozaic duplicate:** two live project records — `37790644-d524-81d1` ("Mozaic Concierge Living — Stamford") + `37790644-d524-814b` ("Mozaic Concierge Living"). Same Stamford project. Did not delete (no safe per-row delete). **Recommend merge/trash one.**
- **3 mislabeled + trashed Mid-Atlantic rows** all titled "Catholic Univ Athletic Fields" but actually UVA Bond House (`…06987be`), Hood College Coblentz Hall (`…09b97c`), Catholic Univ Athletic Fields (`…06827b`) — already in trash; titles wrong. Left as-is.
- **Stray Company Map rows** under "TEMPLATE — old data (safe to delete)" `37a90644-d524-818c`: "KBE Northeast" `72d90644-d524-8227`, "KBE Mid-Atlantic" `13090644-d524-8352`. Unlinked stubs; left untouched.
- **Unidentified division row** `37690644-d524-8010a019…` in company Zack Database (Mozaic `…81d1` was linked to it) — not NE/MA/West; possibly KBE-NY or a stray. Left as-is.

## Not loaded (intentional)
- **Software:** skipped — dossier gaps list confirms NO specific PM/ERP/estimating tool sourced (only generic in-house BIM/VDC). Nothing concrete to add.
- **Page-local Locations DB** (`37690644-d524-803c`, title+Adress text, no relations): not populated — addresses already live on the 3 division rows + company Address place. Low value / would duplicate divisions.
- **Sources page-local DB:** not populated — sources are inline in company/project/membership/event bodies.
- **People:** all dossier leadership already existed (Kolakowski `…8101`, Jim Culkin `1e090644-…8028`, Tim O'Brien `…81d0`, Robert Dunn `…8157` [VP & GC], Adam Peters `…81d8`, Tony Mancini `…81ad`) and linked to company + NE division. No duplicates created; Function fields not deep-enriched (leave for /notion-audit).

## Audit fills (2026-06-10 — notion-audit pass)
**9 project `Adress` (place) properties filled** (city-level from dossier):
| Project | ID | Address filled |
|---|---|---|
| The August at Steelpointe Harbor | 37b90644-d524-814c | Bridgeport, CT 06608 |
| Sunrise Senior Living (Tarrytown) | 37b90644-d524-81db | Tarrytown, NY 10591 |
| Wampanoag Country Club Clubhouse | 37b90644-d524-815b | West Hartford, CT 06107 |
| Residence Inn by Marriott (Steelpointe) | 37b90644-d524-81e4 | Bridgeport, CT 06608 |
| UConn Health Emergency Department Expansion | 37b90644-d524-8120 | Farmington, CT 06032 |
| Annapolis Joint Commissary & Navy Exchange | 37b90644-d524-8190 | Annapolis, MD 21402 |
| NASCAR Clash at LA Memorial Coliseum | 37b90644-d524-816a | Los Angeles, CA 90037 |
| Stonington Village | 37790644-d524-81c1-a60a | Stonington, CT 06378 |
| SUNY Binghamton Grace Hall | 37790644-d524-81d6 | Binghamton, NY 13902 |

**1 edge fix:** Mozaic Concierge Living (`37790644-d524-814b`) — `Zack Database` → NE division (`37690644-d524-8037`) added (was missing division link on the duplicate row).

## Data-quality issues (persisting — for Zack)
- **Mozaic duplicate:** `37790644-d524-814b` + `37790644-d524-81d1` — same Stamford project. NE division now linked to both. Recommend Zack manually merge/trash one.
- **"Bridgeport" stray division row** `37690644-d524-8010` — satellite office stub, not a real division; linked to company and holds Mozaic-Stamford project. Pre-existing; left as-is.
- **3 trashed/mislabeled Mid-Atlantic rows** under "TEMPLATE — old data (safe to delete)" `37a90644-d524-818c` — left as-is per non-destructive rules.

## Left empty (no sourced value in dossier — per gaps list)
DUNS · EIN · CT/MD state entity IDs · numeric EMR/TRIR/DART · surety provider · insurance carriers · division-level revenue/headcount · FPDS PIIDs/obligation amounts · MBE/WBE/8(a) certs (none — merit-shop).
Event `place:Place` on Golf Tournament + CBC events — dossier gives only "Connecticut" (no venue address).

## Audit (2026-06-11 — hourly cycle)
**Result: No fills needed. Record fully up to date.**
Verified live: company record, 3 divisions, 14+ projects, 6 memberships, 4 events. All fields that have sourced data are already populated. No new gaps found vs. 2026-06-10 state. Genuinely sourceless fields remain empty (see above).

## Audit (2026-06-11 — notion-audit skill pass)
**3 location tag fills applied (3e — city-level tags missing):**
| Project | ID | Tag added |
|---|---|---|
| The August at Steelpointe Harbor | 37b90644-d524-814c | + Bridgeport |
| Residence Inn by Marriott (Steelpointe Harbor) | 37b90644-d524-81e4 | + Bridgeport |
| UConn Health Emergency Department Expansion | 37b90644-d524-8120 | + Farmington |

**Schema change:** Added "Bridgeport" and "Farmington" as new options to Construction Projects `Location` multi-select (additive, all existing options preserved). Source: dossier city-level project locations.

All other records verified: company, 3 divisions, 6 memberships, 7 events, all remaining projects — no further gaps found. Genuinely sourceless fields remain empty (see above).

## KBEboston.md load (2026-06-12)
**Ground truth:** `Enlaye Notion/KBE Building/KBEboston.md`. 0 confirmed MA projects. 21 CT nearest-New-England context projects → 14 net-new loaded.

**14 new projects created** (all KBE Northeast; CT-based; Adress place set on all 14):
| Project | ID | City |
|---|---|---|
| Choate Rosemary Hall – Pedestrian Bridge | 37d90644-d524-8191-9cac-d4b7ef0253e8 | Wallingford |
| Choate Rosemary Hall – Welcome Center & Parking Garage | 37d90644-d524-81fe-889d-d88eee1c3ce2 | Wallingford |
| Sacred Heart University Community Theatre | 37d90644-d524-8146-ac85-d335ddfb4d70 | Fairfield |
| Seabury Active Life Community – The Collamore Wing | 37d90644-d524-8163-a00f-ea6a4c566b1b | Bloomfield |
| Seabury Active Life Community – Earlier Phase | 37d90644-d524-81b6-9a18-d38c10092de1 | Bloomfield |
| The Linden at Brookfield | 37d90644-d524-8149-9537-e0d621396dc4 | Brookfield |
| The Vero at Orange | 37d90644-d524-8114-94b8-f292a92b3fff | Orange |
| Piper (TB Norwalk Apartments) | 37d90644-d524-810c-95d0-cc806a683289 | Norwalk |
| The Station House Greenwich | 37d90644-d524-816b-93f9-cba1a8d511b4 | Old Greenwich |
| SoNo Collection | 37d90644-d524-8113-ad0c-f0604a784eed | South Norwalk |
| 1928 Farmington Town Hall | 37d90644-d524-813c-a10d-e18f6c72b6cb | Farmington |
| City of Waterbury ARPA/ESSER School Renovation Program | 37d90644-d524-8139-8bea-e23bd02bf774 | Waterbury |
| 200 Connecticut Avenue | 37d90644-d524-818a-8924-fe066720cdd2 | Norwalk |
| OneBeacon Insurance Group | 37d90644-d524-8105-9271-c7d196ad5154 | Farmington |

**Company CP relation:** updated from 19 → **33 URLs** (one-way, full list re-passed).
**Schema:** Projects Location +Wallingford/Fairfield/Bloomfield/Orange/Old Greenwich/Waterbury (additive, 129→135 options).
**Not loaded:** no MA projects (0 confirmed MA sites in dossier). KBE West "assisted-living multiple states incl. MA" = low-confidence aggregate, no name/city/date.

## Audit (2026-06-11 — notion-audit skill pass #2)
**Result: No fills needed. Record fully up to date.**
Verified live (parallel fetches): company record (`1cf90644`) — all properties populated (Description, Type, Country ×7, Address place, BW Category, LinkedIn, Website, 19 Construction Projects linked, body complete). 3 divisions (NE/MA/West) — all linked to company, People, Projects; Adress place filled on all 3; bodies complete. 7 net-new projects + 12 pre-existing — Adress place filled on all checked; Location multi-select tags applied (Bridgeport+Farmington confirmed from prior pass); bodies sourced and complete. 6 memberships confirmed in live Memberships DB (ABC-CT, ABC Metro Washington, ABC Baltimore/Chesapeake, Arizona Builders Alliance, CBC, Stamford Chamber). 4 events confirmed (KBE Annual Golf Tournament + CBC Project Team Awards + 2 pre-existing). Locations table schema is text-only (no place/relation fields; accepted per prior notes). No fillable gaps identified. Genuinely sourceless fields remain empty (see §Left empty above).

## Audit (2026-06-11 — notion-audit skill pass #3)
**Result: No fills needed. Record fully up to date.**
Full parallel re-audit against live Notion and dossier KBE.md.
- **Company record** (`1cf90644`): all properties populated ✓ (Description, Type, Country ×7, Address place, BW Category, LinkedIn, Website, 19 CP links, body complete).
- **3 divisions** (NE/MA/West): Companies + People + Projects relations ✓; Adress place ✓; bodies complete ✓.
- **19 projects**: Contractors (KBE) ✓, Zack Database (division) ✓, Adress place ✓, Location tags ✓, sourced bodies ✓. Mozaic duplicate (`…81d1` + `…814b`) still live — manual merge required (Zack).
- **6 memberships** (3d — completeness check ✓): ABC-CT, ABC Metro Washington, ABC Baltimore/Chesapeake, Arizona Builders Alliance, CBC, Stamford Chamber — all present with Companies relation ✓ and sourced bodies ✓. Ledger IDs had minor UUID variants; all records confirmed live via search.
- **7 events** (all linked to KBE): InterFace Active Adult, CALA/ISLE, CT ABC EIC Awards, CT ABC Women in Construction, CT ABC Membership Meeting, KBE Golf Tournament, CBC Project Team Awards. Company relation ✓ on all. Place filled on 5; Golf Tournament + CBC = genuinely sourceless (no venue address in dossier).
- **Location tags** (3e): all projects and events with location data tagged ✓.
- **Interconnection** (3a): verified — all division → company ✓, all projects → division + company ✓, all memberships/events → company ✓.
- **No new fillable gaps found.** Genuinely sourceless fields remain empty (see §Left empty).
