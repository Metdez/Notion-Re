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

## Audit pass #8 (2026-06-13 — notion-audit skill, KBE.md + KBE2.md re-audit)

**Ground truth:** `KBE.md` (primary) + `KBE2.md` (for federal project Size fields).

### 2 fills (both verified live as empty before writing)
| Project | ID | Field | Value written | Source |
|---|---|---|---|---|
| Naval Submarine Base Commissary (Groton) | 37d90644-d524-81d1-8ff6-cdd252308cfe | `Size` | "56,847 SF new commissary at Naval Submarine Base New London" | kbebuilding.com/portfolio-cat/government/ |
| Armed Forces Reserve Center (Middletown, CT) | 37d90644-d524-81a6-94e7-e8dba20bb68b | `Size` | "164,000 SF training facility + 36,000 SF maintenance facility; classrooms, SIPRNET center, weapons simulator, vault" | kbebuilding.com/portfolio-cat/government/ |

### Full 3a–3e verified clean
- 3a Interconnection ✓: company→45 projects; 3 divisions→company+People+Projects+Adress; 11 memberships→KBE; 9 events→KBE; 4 software→KBE.
- 3b Description depth ✓: all division bodies and project bodies at full sourced depth.
- 3c Addresses ✓: company HQ place, 3 division Adress places, sampled project Adress places all set. Locations DB intentionally empty.
- 3d Memberships ✓ — 11/11: ABC-CT · ABC Metro Washington · ABC Baltimore/Chesapeake · Arizona Builders Alliance · CBC · Stamford Chamber · Greater Norwalk Chamber · WESTMARC · National Builders Alliance · AGC-CT/CCIA · Retail Contractors Association. All company-linked.
- 3e Location tags ✓: 9 events — all have Connecticut tag (or no location tag needed for sourceless venues).

### Confirmed genuinely sourceless (no write)
DUNS/EIN/state entity IDs · EMR/TRIR/DART · surety provider · insurance carriers · division-level revenue/headcount · FPDS PIIDs · Golf Tournament + CBC Awards + Special Olympics venue addresses · DBIA/USGBC/AGC national memberships.

---

## Left empty (no sourced value in dossier — per gaps list)
DUNS · EIN · CT/MD state entity IDs · numeric EMR/TRIR/DART · surety provider · insurance carriers · division-level revenue/headcount · FPDS PIIDs/obligation amounts · MBE/WBE/8(a) certs (none — merit-shop).
Event `place:Place` on Golf Tournament + CBC events — dossier gives only "Connecticut" (no venue address).

---

## Audit pass #6 (2026-06-12 — notion-audit skill, KBE2.md additional_federal_awards)

**Ground truth used:** `KBE2.md` — `additional_federal_awards` section (2 projects absent from all prior dossiers + loads).

### Findings
- **All 36 KBE2.md projects** verified present in Notion EXCEPT the 2 below — systematically searched by name; confirmed absent before creating.
- **11 memberships** in Notion: ABC-CT · ABC Metro Washington · ABC Baltimore/Chesapeake · Arizona Builders Alliance · CBC · Stamford Chamber · ABC-CT EIC Awards (event) · Women in Construction (pre-existing event) — matches all sourced memberships; DBIA/USGBC/AGC national explicitly "not fully confirmed" in KBE2.md → NOT added (genuinely sourceless).
- **4 software rows** confirmed: Procore · Sage 300 CRE · On-Screen Takeoff · iSqFt — all linked to KBE; matches KBE2.md confirmed stack.
- **Company record, 3 divisions, 9+ events, interconnection graph** — verified clean.

### 2 net-new projects created
Both from KBE2.md `additional_federal_awards`; both linked Contractors→KBE, Zack Database→KBE Northeast; Adress place filled with coords; sourced body.

| Project | ID | Location | Value | Source |
|---|---|---|---|---|
| Naval Submarine Base Commissary (Groton) | 37d90644-d524-81d1-8ff6-cdd252308cfe | Groton, CT 06340 (41.3535/-72.0887) | $14.5M | kbebuilding.com/portfolio-cat/government/ |
| Armed Forces Reserve Center (Middletown, CT) | 37d90644-d524-81a6-94e7-e8dba20bb68b | Middletown, CT 06457 (41.5623/-72.6506) | Design-Build | kbebuilding.com/portfolio-cat/government/ + awards-recognition |

### Company record update
- `1cf90644-d524-802a` `Construction Projects` relation updated **43 → 45 URLs** (full list re-passed with both new project URLs appended; additive replace).

### New data-quality issues (not auto-fixed — non-destructive rule)
- **Station House Greenwich duplicate ×3:** `37c90644…` (rich) + `37d90644…81b5` + `37d90644…816b` (2 thin copies from prior sessions). Recommend Zack trash the 2 thin copies.
- **SoNo Collection duplicate ×3:** similar pattern — rich copy + 2 thin copies from prior sessions. Recommend Zack trash 2 thin copies.
- **Choate Rosemary Hall Pedestrian Bridge** `37d90644…` — still DELETED (in trash). Recommend Zack restore if the project should remain.

### Persisting data-quality issues (unchanged)
- Mozaic duplicate: `37790644-d524-814b` + `37790644-d524-81d1` — same Stamford project.
- "Bridgeport" stray division row `37690644-d524-8010` — satellite stub; pre-existing.
- 3 trashed/mislabeled Mid-Atlantic rows under TEMPLATE — left as-is.

### Genuinely sourceless (confirmed, no write)
EMR/TRIR/DART · surety provider · insurance carriers · DUNS/EIN/state IDs · FPDS PIIDs · Golf Tournament + CBC Project Team Awards venue addresses · DBIA/USGBC/AGC national memberships (unconfirmed in KBE2.md).

---

## Audit pass #7 (2026-06-12 — notion-audit skill, KBE.md full re-audit)

**Ground truth used:** `Enlaye Notion/KBE Building/KBE.md` (primary dossier).

### Audit scope
Full read-only scan across: company record · 3 divisions (NE/MA/West) · all events (9 in DB) · all memberships (11 in DB) · sampled projects (15+ fetched) · Locations DB · Company Map (Zack Database) structure.

### Findings — all clean, no writes needed

**Company record `1cf90644-d524-802a`:** All key properties filled (Description, Type, Address place, Countries, Construction Projects=45 URLs, LinkedIn, Website, BW Category). Body complete (Snapshot/Leadership/Safety/Risk/Sources + Boston BD context). No gaps.

**Divisions (3 rows in Zack Database):**
- KBE Northeast `37690644-d524-8037`: Companies rel ✓ · People (63 linked) ✓ · Projects (44 linked) ✓ · Adress place (Farmington) ✓ · bio body ✓
- KBE Mid-Atlantic `37690644-d524-807c`: Companies rel ✓ · People (6) ✓ · Projects (9) ✓ · Adress place (Laurel, MD) ✓ · bio body ✓
- KBE West `37690644-d524-80e6`: Companies rel ✓ · People (4) ✓ · Projects (2) ✓ · Adress place (Scottsdale, AZ) ✓ · bio body ✓

**Events (9 rows in Events DB):** All linked to KBE via Companies full database ✓. Place/Location tags check:
- ABC EIC Awards (2026): Place = Aqua Turf Club, Plantsville CT ✓; tags = Connecticut + Southington + Plantsville ✓
- ABC WIC Breakfast (2026): Place = Bristol Event Center CT ✓; tag = Connecticut ✓
- KBE Foundation Scholarship Night: Place = Farmington Gardens CT ✓; tag = Connecticut ✓
- InterFace Active Adult: Place = Plano TX ✓; tags = Texas + Plano ✓
- KBE Annual Golf Tournament: Place EMPTY — no venue address in any source → genuinely sourceless (confirmed)
- CBC Project Team Awards: Place EMPTY — dossier says "Connecticut" only → genuinely sourceless (confirmed)
- Special Olympics Fishing Tournament: Place EMPTY — no venue in dossier → genuinely sourceless (confirmed)
- ABC-CT Membership Meeting (2026) + CALA/ISLE 2026: pre-existing events, not KBE-specific; linked to KBE.

**Memberships (11 rows confirmed in Memberships DB):** ABC-CT · ABC Metro Washington · ABC Baltimore/Chesapeake · Arizona Builders Alliance (ABC) · CBC · Stamford Chamber · Greater Norwalk Chamber · WESTMARC · National Builders Alliance · AGC-CT/CCIA · Retail Contractors Association. All linked to KBE ✓. Matches full sourced list from KBE.md + KBE2.md. No missing memberships from KBE.md dossier.

**Projects sampled (15+ checked):** All have Contractors→KBE ✓, Zack Database→division ✓, Adress place filled ✓, sourced body ✓. Includes: The August, Stonington Village, Mozaic, Wampanoag CC, SUNY Grace Hall, Sunrise Tarrytown, Residence Inn, UConn Health ED, Annapolis Commissary, NASCAR Clash, Naval Sub Base Commissary, Armed Forces Reserve Center, Choate Rosemary Hall Pedestrian Bridge.

**Locations DB `37690644-d524-803c`:** Empty (zero rows). Intentionally left unpopulated — addresses live on division Adress place fields and company Address place. No change.

### No writes executed
All sourced data already present in Notion. Zero fillable gaps found from KBE.md ground truth.

### Data-quality issues updated
- **Mozaic duplicate RESOLVED:** `37790644-d524-814b` now shows as `deleted` (in trash) — live record is `37790644-d524-81d1` only. Duplicate effectively resolved.
- **Choate Rosemary Hall Welcome Center `37d90644-d524-813e`**: shows as `deleted` but still in KBE NE Projects list and Companies Construction Projects relation. Flag for Zack to restore or remove from relations.
- **Station House Greenwich ×3 + SoNo Collection ×3 duplicates**: still present from prior sessions. Recommend Zack trash thin copies.
- **"Bridgeport" stray division row `37690644-d524-8010`**: still present; pre-existing; safe to ignore.

### Genuinely sourceless (confirmed for KBE.md dossier)
DUNS/EIN/state entity IDs · EMR/TRIR/DART numerics · surety provider · insurance carriers · division-level revenue/headcount · FPDS PIIDs · Golf Tournament, CBC Awards, Special Olympics Fishing Tournament venue addresses · DBIA/USGBC/AGC national memberships.
