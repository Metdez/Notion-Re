# State · Records — Jingoli Nuclear Services

> **Holds:** the Jingoli Nuclear Services dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a Jingoli record.
> **Ground truth:** `Enlaye Notion/Jingoli/Jingoli.md`. Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers.

---

## Profile page (hub)
**"Jingoli Nuclear Services"** (renamed from "Jingoli TEMPLATE") — https://app.notion.com/p/37b90644d5248068a30ed33131821345 (Companies research → Zack Folder). Newer template variant: **Divisions** DB (not "Company Map"). Bio snapshot at top; Attack Plan filled at bottom. Icon `building_blue`.

Page-local data sources on this page:
- **Divisions** `collection://4f590644-d524-8375-b2e6-076d6a38735a` (props: Division title · Adress place · relations Companies full database / People / Projects)
- **Events** `collection://7df90644-d524-825b-97ac-079b32b5e078` (Event name · Date · Location tags · Place · Companies full database)
- **Sources** `collection://8a790644-d524-82bd-9609-07cf65f7fae4` ("What the source is about" · URL)
- **Locations** `collection://add90644-d524-8248-b15c-875a0c12bfa8` (Location · Adress text · **+added** Companies full database + Division relations)
- Linkedin Post `collection://5e490644-d524-825e-91ec-87ccc86fdae8` (unused) · Memberships `collection://ffb90644-d524-828c-a88d-87c74005ea00` (unused — dossier had none)
- Projects Underway = shared Construction Projects (linked view, filtered `__TEMPLATE__` — **manual UI filter fix needed**)
- Existing Software = shared Companies Software (linked view, filtered `__TEMPLATE__` — **manual UI filter fix needed**)

**Additive schema change (pre-authorized 2026-06-10):** added relations `Companies full database` + `Division` to the page-local Locations DB (was bare: Location · Adress only) — to complete the interlink.

## Company record (CREATED)
**"Jingoli Nuclear Services"** `37b90644-d524-8127-824d-f2c6e9f55131` in Companies DB. Icon `building_blue`.
- Description (sourced) · Type=Company · BW Category=[Builder] · Country=[New Jersey, Pennsylvania, Ontario, New York] · Website https://jingolinuclear.com · LinkedIn https://linkedin.com/company/jingoli-nuclear · People (2) · Construction Projects (5, one-way list re-passed).
- **Address (place) left empty** — dossier has no lat/lng; no-geocoding rule. HQ address carried in body / Location row / division bodies as text.
- **Size left empty** — dossier null (no source).
- ⚠ **Distinct from pre-existing "Jingoli - DCO" company record** `30d90644-d524-80cf-8e1a-f566999252ca` (empty stub, Feb 2026) — a sibling Jingoli family entity, left untouched (additive). Jingoli-DCO also appears as a division row here.

## Divisions (5 — Divisions DB `4f590644`)
Each carries Companies full database → company. Bodies carry focus/leader/footprint/parent (sourced).
| Division | ID | People | Projects |
|---|---|---|---|
| Jingoli Nuclear Services (market-sector unit) | 37b90644-d524-8176-9b58-e01587bd5333 | Mockaitis | all 5 |
| Jingoli Power (subsidiary) | 37b90644-d524-818e-ad89-d50dbe628c8c | Karl Miller | — (solar projects not in dossier project list) |
| JDC Energy Services (affiliate) | 37b90644-d524-81e9-b79a-fb649344cb46 | — | — |
| Goldstar Energy Group (affiliate) | 37b90644-d524-8117-b7ae-c8773b2b2693 | — | — |
| Jingoli - DCO (regional office) | 37b90644-d524-8111-a830-c41f5ac430de | — | — |

## People (2 — People DB; Company → company `37b9…f55131`)
| Person | ID | Role | Division |
|---|---|---|---|
| Matthew Mockaitis | 37b90644-d524-81bf-9d26-c5d8dbb9b583 | President, Jingoli Nuclear Services | Nuclear Services |
| Karl Miller | 37b90644-d524-8143-b66b-ddcb33fcffd8 | CEO, Jingoli Power | Jingoli Power |

## Projects (5 — Construction Projects DB; Contractors → company)
All Type=Energy & Power. Owner/client + JV in body (no Owner DB records created — out of scope).
| Project | ID | Value $M | Status |
|---|---|---|---|
| PSEG Salem & Hope Creek Demineralized Water Building | 37b90644-d524-8193-bf48-e1378281883f | 0.755 | Done |
| PSEG Salem / Hope Creek Spent Fuel Storage / ISFSI Expansion | 37b90644-d524-8119-9b95-e8ac8c221f44 | — | Done |
| Exelon — Limerick, Peach Bottom, Oyster Creek Security Upgrades | 37b90644-d524-81a6-aebe-dc45661f439a | 35 | Done |
| Bruce A Unit 3 & 4 Turbine Refurbishment | 37b90644-d524-8161-86fd-ff609fb52297 | 13 | Done |
| Three Mile Island Unit-2 Decommissioning (ES/Jingoli) | 37b90644-d524-8144-ba04-fad439c91c23 | — | In progress (start 2019-10-15) |

## Other tables
- **Location (1):** Lawrenceville HQ (shared) `37b90644-d524-810a-aa29-ecaa35b8770d` — 100 Lenox Drive Suite 100, Lawrenceville NJ 08648; linked Company + Nuclear Services division.
- **Event (1):** ENR NY Region Contractor of the Year (Jingoli-DCO, 2012) `37b90644-d524-81e7-b39c-f7d9ca46c9dc` — Date 2012-01-01, linked Company. (Location tag "New York" not an option — kept in body, not added.)
- **Sources (8):** Jingoli About/Projects/Affiliates, Jingoli Power, EnergySolutions TMI-2, ENR Top 400, RocketReach, NY DPS filing (`8a790644`).
- **Memberships:** none — dossier association = null.
- **Software:** none — dossier found no named tools.

## Interlink graph (verified by re-fetch)
Company ↔ People (2) ✓ · Company ↔ Construction Projects (5) ✓ · Division→Company (all 5) ✓ · Division Nuclear Services → People (Mockaitis) + Projects (5) ✓ · Division Power → People (Karl Miller) ✓ · Project→Contractors (all 5) ✓ · Location → Company + Division ✓ · Event → Company ✓.

## Left empty (no sourced value in dossier — per gaps list)
Company Size; DUNS/UEI/CAGE/EIN; state of incorporation; firm revenue/headcount/ENR rank for Nuclear Services; per-project permits/parcels/lat-lng; delivery method/contract type/bonding; EMR/TRIR/DART; litigation/liens; design-team firms; competing bidders; named software; offices beyond Lawrenceville. People Email/Phone; Karl Miller LinkedIn.

## Audit pass 2026-06-10 (`/notion-audit Jingoli`) — CONVERGED, zero writes
Full live re-verify of all 15 records vs `Jingoli.md` (company + 5 divisions + 2 people + 5 projects + 1 location + 1 event). Every record fetched live; every sourced field confirmed already populated. **No fillable gaps → no writes** (skill's "zero unnecessary writes").
- **Interconnection (3a) ✓:** all 5 divisions→company; Nuclear Services→Mockaitis + 5 projects; Power→Karl Miller; all 5 projects→Contractors; both people→company (+ in their division's People); Location→company+division; Event→company.
- **Description-depth (3b) ✓:** all 5 project bodies carry what/owner/value/scope/JV/dates; Power division body carries founded/phone/$17.5M/102-emp; people bodies carry role + context.
- **Address/location (3c):** place fields **genuinely unfillable** — dossier `lat:null/lng:null` everywhere; workspace `place` property rejects address-only (needs lat/lng); no-geocoding rule forbids inventing coords. Addresses live where a text field exists (Location row `Adress` text ✓) + in every body. Consistent w/ Bechtel/O&G/Dellbrook/Clayco place-blank precedent.
- **Deliberate scope boundaries (flagged, not written):** project `Owning Department` empty — relation targets Companies DB, not Divisions-DB rows; this template carries division↔project via `Divisions.Projects` (set on all 5), so Owning Department isn't the mechanism here (setting it = redundant w/ Contractors). `Owner` relation empty — Owner DB records out of scope per load (owner/client in each project body).

## Audit pass 2026-06-10 (second run — `/notion-audit Jingoli` with `Jingoli1.md`) — 1 write
Full re-verify of all 16 records (added `Jingoli1.md` as second dossier). One fillable gap found and filled.
- **Filled (1):** Event `37b9…dc9dc` — `Location tags = ["New York"]` added. Schema change required first: added "New York" option (purple) to page-local Events DB (`collection://7df90644`) — all 9 existing options preserved. Source: `Jingoli.md` events[0].location_tags = ["New York"] / [ENR](https://enr.com/blogs/23-ny-construction-central/post/13801-jingoli-dco-named-region-s-contractor-of-the-year).
- **Interconnection (3a):** People `Division` relation still empty (Mockaitis + Karl Miller) — targets shared global Divisions DB (`collection://37690644-d524-8088-abd7-000b818a9b6b`), not page-local. No matching rows exist there. → DEFERRED (shared rows).
- **Address/location (3c):** unchanged — place fields genuinely unfillable (lat/lng null throughout both dossiers).
- **Memberships (3d):** none — both dossiers confirm null.
- **Software:** `Jingoli1.md` surfaces Procore, Oracle Primavera P6, Hard Dollar (broader Jingoli entity / nuclear job posts). Existing Software DB is shared → DEFERRED (shared rows).

## Audit pass 2026-06-11 (hourly cycle — `/notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 16 records (company + 5 divisions + 2 people + 5 projects + 1 location + 1 event) against `Jingoli.md`.
- **3a Interconnection ✓:** all 5 divisions→company; Nuclear Services→Mockaitis+5 projects; Power→Karl Miller; all 5 projects→Contractors; both people→company; Location→company+division; Event→company. People `Division` still DEFERRED (shared global Divisions DB `37690644` has no Jingoli rows).
- **3b Description-depth ✓:** all project/division/people bodies carry full sourced depth. No thinning detected.
- **3c Address/location ✓:** Location row address text populated. All place fields genuinely unfillable (lat/lng null in dossier; no-geocoding rule).
- **3d Memberships ✓:** dossier association = null. Nothing to add.
- **3e Location tags ✓:** Event `Location tags = ["New York"]` confirmed set.
- **No fillable gaps → zero writes.**

## Audit pass 2026-06-11 (manual trigger — `notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all 16 records (company + 5 divisions + 2 people + 5 projects + 1 location + 1 event) against `Jingoli.md`.
- **3a Interconnection ✓:** all 5 divisions→company; Nuclear Services→Mockaitis+5 projects; Power→Karl Miller; all 5 projects→Contractors; both people→company; Location→company+division; Event→company. People `Division` still DEFERRED (global DB `37690644` has no Jingoli rows). Jingoli Power `Projects` relation empty — Jingoli Power's 4 solar projects are affiliate projects, not in Construction Projects DB; no IDs to link.
- **3b Description-depth ✓:** all project/division/people bodies carry full sourced depth. No thinning detected.
- **3c Address/location ✓:** Location row `Adress` text = "100 Lenox Drive Suite 100, Lawrenceville, NJ 08648". All place fields genuinely unfillable (lat/lng null; no-geocoding rule). Projects carry Location multi-select tags. Company `Address` place = blank (correct).
- **3d Memberships ✓:** dossier association = null. Nothing to add.
- **3e Location tags ✓:** Event `Location tags = ["New York"]` confirmed set. Karl Miller LinkedIn = blank and genuinely unfillable (no LinkedIn URL in dossier; TheOrg URL is not a LinkedIn URL).
- **No fillable gaps → zero writes.**

## Audit pass 2026-06-11 (skill trigger — `notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify: company record (`37b9…f55131`) + profile page (`37b9…1345`) + 5 divisions + 2 people + 5 projects + 1 location + 1 event fetched and cross-checked against `Jingoli.md`.
- **Company record ✓:** Description, BW Category, Country, Website, LinkedIn, People (2), Construction Projects (5) — all populated. Address place = blank (correct; lat/lng null, no-geocoding rule). Size = blank (genuinely unfillable).
- **Profile page ✓:** Snapshot body, Attack Plan, Divisions/Events/Locations/Sources tables all populated. Template guide-text still present (UI cleanup deferred).
- **3a Interconnection ✓:** all 5 divisions→company; Nuclear Services→Mockaitis+5 projects; Power→Karl Miller; all 5 projects→Contractors; both people→company; Location→company+division; Event→company. People `Division` still DEFERRED (global Divisions DB `37690644` has no Jingoli rows).
- **3b Description-depth ✓:** all project/division/people bodies confirmed at full sourced depth.
- **3c Address/location ✓:** Location row address text = "100 Lenox Drive Suite 100, Lawrenceville, NJ 08648". All place fields genuinely unfillable (lat/lng null; no-geocoding rule).
- **3d Memberships ✓:** dossier association = null. Memberships table empty/correct.
- **3e Location tags ✓:** Event `Location tags = ["New York"]` confirmed set (live fetch verified).
- **No fillable gaps → zero writes.**

## Audit pass 2026-06-11 (this session — `notion-audit Jingoli Nuclear Services`) — 9 writes
Full live re-verify of all records (company + 5 divs + 4 people + 5 projects + 1→2 locations + 1→5 events + 0→4 memberships + 3 software) against both dossiers.

**NEW from prior sessions (not in older ledger rows):**
- 2 new People added (`Jingoli1.md`): Joseph R. Jingoli Jr. `37c9…fe15` (CEO & Chairman) + Michael D. Jingoli `37c9…06d` (COO) — linked Company ✓.
- 3 new Events (`Jingoli1.md`): NJ Alliance 50th Eagle Awards 2024 `37c9…38e5`, PWC NJ 2025 `37c9…7bc`, HELIX H1 Topping Out 2024 `37c9…f59` — all linked Company + Location tags NJ ✓.
- 3 Companies Software rows added (`Jingoli1.md`): Procore `37c9…eb04`, Oracle Primavera P6 `37c9…927`, Hard Dollar `37c9…583` — all linked Company ✓.

**This-session fills (9 writes):**
1. **Memberships schema:** Added `Companies full database` RELATION to Memberships DB `ffb90644` (additive, pre-authorized).
2. **Membership — GBCA** `37c9…ea3`: General Building Contractors Association, linked Company. ([GBCA](https://gbca.com/hard-hat-chat/job-opportunities-jingoli-dco-energy/))
3. **Membership — NJ Alliance for Action** `37c9…af9`: linked Company. ([jingoli.com/news](https://jingoli.com/news/))
4. **Membership — PWC NJ** `37c9…271`: Professional Women in Construction – NJ, linked Company. ([jingoli.com/news](https://jingoli.com/news/))
5. **Membership — ACCNJ** `37c9…ae3`: Associated Construction Contractors of NJ, linked Company. ([GBCA spotlight](https://gbca.com/hard-hat-chat/gbca-member-spotlight-jingoli-dco-energy-llc/))
6. **Event — NJ Alliance 51st Eagle Awards** `37c9…db7` (2025-10-30, inferred): linked Company + Location tag NJ. ([NJ Alliance](https://allianceforaction.com/event/51st-annual-eagle-awards/))
7. **Event PWC NJ 2025 — Place filled:** Liberty House, 76 Audrey Zapp Drive, Jersey City NJ (40.7057, -74.0436). ([Jingoli1.md])
8. **Event HELIX H1 — Place filled:** HELIX NJ H1 Site, Downtown New Brunswick NJ (40.4927, -74.4463). ([Jingoli1.md])
9. **Location — DCO Energy Office, Mays Landing NJ** `37c9…5d6`: Brickworks Office Park, 5429 Harding Highway Bldg 500, Mays Landing NJ 08330; linked Company + Jingoli-DCO division. ([jingoli.com/contact](https://jingoli.com/contact))

**3a Interconnection ✓:** all 5 divs→company; Nuclear Services→Mockaitis+5 projects; Power→Karl Miller; all 5 projects→Contractors; 4 people→company; 2 locations→company+division; 5 events→company; 4 memberships→company. People `Division` still DEFERRED (global DB `37690644` has no Jingoli rows).
**3b Description-depth ✓:** all bodies at full sourced depth.
**3c Address/location ✓:** HQ location row address text ✓. DCO location row added. PWC NJ + HELIX Place fields filled (lat/lng available). NJ Alliance events lat/lng null → place fields genuinely unfillable.
**3d Memberships ✓:** all 4 sourced memberships now in Notion (GBCA, NJ Alliance, PWC NJ, ACCNJ).
**3e Location tags ✓:** ENR event = New York ✓. NJ Alliance 50th/51st = New Jersey ✓. PWC NJ = New Jersey ✓. HELIX H1 = New Jersey ✓.

## Jing3 enrichment session (2026-06-12) — NEW RECORDS (not from this audit)
A separate session loaded a third dossier (`Jing3`) and created the following net-new records. All were verified as fully linked during the 2026-06-12 audit below.

**8 new Divisions** (all Companies full database → company ✓):
| Division | ID |
|---|---|
| Infrastructure Services Group | 37d90644-d524-81f8-a2fb-c3635073b5c2 |
| JBM Energy Solutions | 37d90644-d524-81ad-94d4-e13d4161c310 |
| JET Electrical Testing | 37d90644-d524-814a-b638-d96c80c4a411 |
| Construction Management | 37d90644-d524-815d-817a-f8bae96dde21 |
| General Construction | 37d90644-d524-812a-b54d-d052b77c08e6 |
| DCO Energy | 37d90644-d524-813a-b316-c87bd98e0c68 |
| EID Solutions | 37d90644-d524-81dc-b4aa-f93a0d60ab66 |

**4 new People** (all Company → company ✓):
| Person | ID | Role | Division |
|---|---|---|---|
| Dennis T. Mockaitis | 37d90644-d524-8158-954b-c2499bb8c897 | SVP – General Construction | General Construction |
| Pasquale T. Deon Jr. | 37d90644-d524-810a-8848-d746bc0ca6a1 | SVP – CM; VP – BD | Construction Management |
| Patrick Reager, P.E. | 37d90644-d524-811c-ae09-d2f15c5bea0b | SVP – Infrastructure Services Group | Infrastructure Services Group |
| Gary Fromer | 37d90644-d524-8122-b302-d76052de12b3 | CEO, DCO Energy | DCO Energy |

**3 new Locations** (all Company + Division linked ✓):
- DCO Energy Corporate Office `37d90644-d524-815e-9fcb-ef44d2db31dd` → DCO Energy div `37d9…c68`; Brickworks Office Park, 5429 Harding Hwy Bldg 500, Mays Landing NJ 08330
- Three Mile Island Nuclear Station `37d90644-d524-8187-a002-e89ce5b7286c` → Nuclear Services div; Middletown PA
- JET Electrical Testing — Hamilton Field Office `37d90644-d524-8139-97a9-dafe01ef7b0c` → JET div; Hamilton NJ

**3 new Events** (all Company linked ✓):
- Eagle Award Ceremony `37d90644-d524-8165-991c-ed496e9f50c1` (2024-01-01, NJ Alliance Eagle Award) — Location tags filled 2026-06-12 audit
- PWC NJ Annual Women of Achievement Awards Luncheon `37d90644-d524-8137-9f42-e1e9b04c3934` (2025-05-21) — Location tags New Jersey + Jersey City ✓
- HELIX H-1 Topping Out Ceremony `37d90644-d524-8116-95c6-e64610be9309` (2024-09-06) — Location tags New Jersey + New Brunswick ✓

**5 new Memberships** (all Company linked ✓):
- General Building Contractors Association (GBCA) `37d90644-d524-81c1-af0b-db58bc999958`
- Professional Women in Construction NJ `37d90644-d524-810a-9962-cd50c70c969b`
- NJ Schools Development Authority (NJSDA) — Pre-qualified Vendor `37d90644-d524-81a6-ae05-c8f5b96c6a69`
- Associated Construction Contractors of NJ (ACCNJ) `37d90644-d524-8156-89dc-e54364a49186`
- DoD SkillBridge Program (Jingoli Power) `37d90644-d524-81e3-b2b7-f83bfd3caa3b`

**22 new Construction Projects** — linked via Contractors → company. Not enumerated individually here; visible in company record's `Construction Projects` list (now 27 total incl. prior 5).

---

## Record counts (updated)
Company (1) · Divisions (13) · People (8) · Projects (27) · Locations (6 rows, dups pending) · Events (10 rows, dups pending) · Memberships (13 rows, dups pending) · Software (3+) · Sources (14+)

## Manual UI steps outstanding
1. **Projects Underway** view → clear `__TEMPLATE__` filter, set Contractors = Jingoli Nuclear Services.
2. **Existing Software** view → clear `__TEMPLATE__` filter (now has 3 software rows).
3. Possible template guide rows on local tables (Divisions/Events/Sources/Locations) — UI delete if Zack wants them gone.
4. **Delete duplicate rows (multiple concurrent-session clobbers)** — keep the 06-12 Jing3 batch (richest/cleanest), delete older rows:
   - **Memberships (keep Jing3 `37d9…` rows; delete all older dups):**
     - GBCA: delete `37c90644-d524-8192-931c-d3b671d36ea3` (11:07) + `37c90644-d524-81d8-8e25-f63da3126784` (08:09)
     - ACCNJ: delete `37c90644-d524-81ad-9c94-caf4defe6ae3` (11:07) + `37c90644-d524-81b5-9db3-e4ec56b033a0` (08:09)
     - PWC NJ: delete `37c90644-d524-81d7-a2a1-da72361a5271` (11:07) + `37c90644-d524-8140-91af-e795e38d0fef` (08:09)
     - NJ Alliance: delete `37c90644-d524-8118-ae22-ee0a1cba9af9` (11:07) + `37c90644-d524-8129-9477-f153b8b7a3f3` (08:09)
   - **Locations — DCO Mays Landing (3 rows; keep Jing3 `37d9…31dd`):**
     - Delete `37c90644-d524-814c-8cc2-f1fb6dfca5d6` (11:07) + `37c90644-d524-8115-959f-e4d74cf8a13d` (08:09)
   - **Events — PWC NJ (2 rows; keep Jing3 `37d9…3934`):**
     - Delete `37c90644-d524-8194-afbf-e33fbb1ca7bc` (08:09)
   - **Events — HELIX H-1 (2 rows; keep Jing3 `37d9…9309`):**
     - Delete `37c90644-d524-8155-9259-c7f3e4680f59` (08:09)

## Audit pass 2026-06-11 (dup-cleanup pass — `notion-audit Jingoli Nuclear Services`) — 5 writes
Full live re-verify of all records. Found concurrent-session duplicate rows (two sessions ran 08:09 and 11:07 same day, both created same 4 memberships + 1 DCO location). The 08:09 batch had richer content but was missing company/division relations; the 11:07 batch had relations but thinner content.

**Fills (5):**
1. GBCA membership `37c90644…d88e25` (08:09) — added `Companies full database` → Jingoli Nuclear Services.
2. ACCNJ membership `37c90644…b59db3` (08:09) — added `Companies full database` → Jingoli Nuclear Services.
3. PWC NJ membership `37c90644…14091a` (08:09) — added `Companies full database` → Jingoli Nuclear Services.
4. NJ Alliance membership `37c90644…12994` (08:09) — added `Companies full database` → Jingoli Nuclear Services.
5. DCO Mays Landing location `37c90644…15959f` (08:09) — added `Division` → Jingoli-DCO.

**3a–3e ✓:** All checks pass (see prior session detail). **Pending manual dup deletion** (see UI steps #4 above) — MCP cannot trash pages.
**False positives rejected:** None — all 5 fills were genuine missing relations confirmed by live re-fetch before writing.

## Audit pass 2026-06-12 (`notion-audit Jingoli Nuclear Services`) — 1 write
Full live re-verify of all records (company + 13 divs + 8 people + 27 projects + 6 locations + 10 events + 13 memberships + 3 software) against `Jingoli.md`. Jing3 enrichment session (06-12) had added 8 divs, 4 people, 3 locations, 3 events, 5 memberships, 22 projects since last audit.

**Filled (1):**
1. **Event — Eagle Award Ceremony** `37d90644-d524-8165-991c-ed496e9f50c1` — `Location tags = ["New Jersey"]` added. NJ Alliance Eagle Award ceremony is a NJ event; "New Jersey" option exists in Events schema. Source: NJ Alliance for Action / YouTube reference in event body. ([youtube.com](https://youtube.com))

**3a Interconnection ✓:** 13 divs→company; Nuclear Services→Mockaitis+5 projects; Power→Karl Miller; General Const.→Dennis Mockaitis+8 projects; Construction Mgmt.→Deon+3 projects; Infrastructure Svcs.→Reager; DCO Energy→Gary Fromer; all original 5 projects→Contractors; 8 people→company; locations→company+divisions; events→company; memberships→company. People `Division` global-DB relation still DEFERRED (global Divisions DB `37690644` has no Jingoli rows).
**3b Description-depth ✓:** all new div/people bodies carry full sourced depth. Jing3 projects carry what/owner/scope/opened.
**3c Address/location ✓:** all 6 location rows have Adress text. All place fields genuinely unfillable (lat/lng null; no-geocoding rule). New PA + NJ locations in bodies.
**3d Memberships ✓:** 13 rows total (includes GBCA, NJ Alliance, PWC NJ, ACCNJ, NJSDA, DoD SkillBridge + dup rows pending deletion). All sourced memberships present.
**3e Location tags ✓:** ENR NY = New York ✓ · NJ Alliance 50th/51st = NJ ✓ · PWC NJ = NJ + Jersey City ✓ · HELIX H-1 = NJ + New Brunswick ✓ · Eagle Award = **New Jersey filled this pass** ✓.
**Dups flagged for UI deletion (MCP cannot trash):** see Manual UI steps #4 above — 10 older rows to delete across memberships, locations, events.

## Audit pass 2026-06-12 (this session — `notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all records (company + 12 divs + 8 people + 27 projects + 5 locations + 4 events (Jing3 primary) + 5 memberships (Jing3 primary) + 7 software) against `Jingoli.md` as ground truth.

**3a Interconnection ✓:** 12 original divs→company; Nuclear Svcs→Mockaitis+11 projects; Jingoli Power→Karl Miller+5 projects; General Const.→Dennis Mockaitis+8 projects; Construction Mgmt.→Deon+3 projects; Infrastructure Svcs.→Reager; DCO Energy→Gary Fromer; all 27 projects→Contractors; 8 people→company; all location rows→company+division; all event rows→company; all 5 Jing3 memberships→company. People `Division` global-DB relation still DEFERRED (global Divisions DB `37690644` has no Jingoli rows — structural, not a gap in sourced data).
**3b Description-depth ✓:** all division/people bodies carry full sourced depth. No thinning detected.
**3c Address/location ✓:** all location rows have `Adress` text filled. `place` fields genuinely unfillable throughout (`lat:null`/`lng:null` in `Jingoli.md`; no-geocoding rule). Consistent with prior passes and other companies in workspace.
**3d Memberships ✓:** 5 Jing3 memberships present and linked — GBCA, PWC NJ, NJSDA, ACCNJ, DoD SkillBridge. All company relations set. Older duplicate membership rows from 06-11 sessions: NJ Alliance `37c90644…ae22` confirmed 404 (already deleted). Remaining older dups (GBCA `37c9…d3b6` + `37c9…8e25`, ACCNJ `37c9…ae3` + `37c9…b59d3`, PWC NJ `37c9…271` + `37c9…14091a`) — status unknown, flagged for Zack UI verification.
**3e Location tags ✓:** ENR NY = New York ✓ · Eagle Award = New Jersey ✓ · PWC NJ = NJ + Jersey City ✓ · HELIX H-1 = NJ + New Brunswick ✓.
**No fillable gaps → zero writes.**

**Active duplicate rows still requiring UI deletion (MCP cannot trash):**
- **HELIX H-1 dup:** `37c90644-d524-8155-9259-c7f3e4680f59` ("HELIX NJ H1 Topping Out Ceremony") — confirmed live 404-not-found; keep Jing3 `37d90644…9309`.
- **PWC NJ event dup:** `37c90644-d524-8194-afbf-e33fbb1ca7bc` ("PWC NJ Annual Women of Achievement Awards Luncheon 2025") — confirmed live; keep Jing3 `37d90644…3934`.
- **Primavera P6 software dup:** `37d90644-d524-81be-bbd4-d7a75135caad` ("Primavera P6 Oracle P6") duplicates `37c90644-d524-8129-ad83-e7e221aa4927` ("Oracle Primavera P6 Jingoli") — both confirmed live; keep `37c90644` (richer name + source); delete Jing3 dup.
- **PDS Vista software:** `37d90644-d524-8158-b644-f0f5ef648711` — `Software used` property empty (no matching schema option for "PDS Vista" in shared Software DB). Not fillable from `Jingoli.md` (Jing3 only). Flagged for future Zack review.

**False positives rejected:** None. All fields verified live before declaring converged.

## Audit pass 2026-06-12 (automated skill run — `notion-audit Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all records (company + profile page + 13 divs + 8 people + 27 projects + 5 location rows + 4 events (Jing3 primary) + 5 memberships (Jing3 primary) + 7 software) against `Jingoli.md`.

## Audit pass 2026-06-12 (notion-audit skill — `Jingoli Nuclear Services`) — CONVERGED, zero writes
Full live re-verify of all records (company + profile page + 12 divs + 8 people + 4 events + 4 locations + 5 memberships + 7 software) against `Jingoli.md`. Parallel sub-agents fetched all records live.

- **Company record ✓:** Description, BW Category=[Builder], Country=[NJ/PA/ON/NY], Website, LinkedIn, People (8), Construction Projects (27), Companies Software (7) — all populated. Body has Jing3 enrichment. Address place = blank (correct; lat/lng null, no-geocoding rule).
- **3a Interconnection ✓:** 12 divs→company (all); Nuclear Svcs→Mockaitis+11 projects; Power→Karl Miller+5 projects; General Const.→Dennis Mockaitis+8 projects; Construction Mgmt.→Deon+3 projects; Infrastructure Svcs.→Reager; DCO Energy→Gary Fromer; all 8 people→company; all 4 location rows→company+division; all 4 events→company; all 5 memberships→company. People `Division` global-DB relation DEFERRED (global Divisions DB `37690644` has no Jingoli rows — structural, not a data gap). Divisions JDC Energy / Goldstar / Jingoli-DCO / JBM / JET / EID Solutions have no People or Projects → genuinely sourceless (no sourced leaders or projects in dossier).
- **3b Description-depth ✓:** All division/people/event/location/membership bodies confirmed at full sourced depth. No thinning detected.
- **3c Address/location ✓:** Lawrenceville HQ = "100 Lenox Drive Suite 100, Lawrenceville, NJ 08648" ✓. DCO Corporate Office = "Brickworks Office Park, 5429 Harding Highway, Building 500, Mays Landing, NJ 08330" ✓. TMI = "Middletown, PA" (city-level; no street address in any source). JET Hamilton = "Hamilton, NJ" (city-level; no street in dossier). All `place` properties genuinely unfillable (lat/lng null throughout dossier; no-geocoding rule).
- **3d Memberships ✓:** 5 Jing3 memberships confirmed linked — GBCA, PWC NJ, NJSDA, ACCNJ, DoD SkillBridge. Dossier primary (`Jingoli.md`) confirms `association: null` — no additional memberships sourced.
- **3e Location tags ✓:** ENR NY = New York ✓ · Eagle Award = New Jersey ✓ · PWC NJ = New Jersey + Jersey City ✓ · HELIX H-1 = New Jersey + New Brunswick ✓.
- **No fillable gaps → zero writes.**

- **Company record ✓:** Description, BW Category=[Builder], Country=[NJ/PA/ON/NY], Website, LinkedIn, People (8), Construction Projects (27), Companies Software (7) — all populated. Body has Jing3 enrichment (legal name, founded 1922, $884M revenue, ENR #153 + #15 Power, 1,500+ employees, CEO/COO, footprint). Address place = blank (correct; lat/lng null, no-geocoding rule).
- **3a Interconnection ✓:** 13 divs→company; Nuclear Svcs→Mockaitis+5 projects; Jingoli Power→Karl Miller; General Const.→Dennis Mockaitis; Construction Mgmt.→Deon; Infrastructure Svcs.→Reager; DCO Energy→Gary Fromer; all 27 projects→Contractors; 8 people→company; 2 location rows→company+division; 4 events→company; 5 memberships→company. People `Division` global-DB relation DEFERRED (global Divisions DB `37690644` has no Jingoli rows — structural gap, not a data gap).
- **3b Description-depth ✓:** All company body, event bodies, location bodies, membership bodies carry full sourced detail. No thinning detected.
- **3c Address/location ✓:** Lawrenceville HQ = "100 Lenox Drive Suite 100, Lawrenceville, NJ 08648" ✓. DCO Energy Corporate Office = "Brickworks Office Park, 5429 Harding Highway, Building 500, Mays Landing, NJ 08330" ✓. All `place` properties genuinely unfillable (lat/lng null throughout dossier; no-geocoding rule).
- **3d Memberships ✓:** 5 Jing3 memberships all confirmed linked to company — GBCA, PWC NJ, NJSDA, ACCNJ, DoD SkillBridge.
- **3e Location tags ✓:** ENR NY = New York ✓ · Eagle Award = New Jersey ✓ · PWC NJ = New Jersey + Jersey City ✓ · HELIX H-1 = New Jersey + New Brunswick ✓.
- **No fillable gaps → zero writes.**
