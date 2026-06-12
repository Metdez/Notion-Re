# State · Records — O&G Industries Build

> **Holds:** the O&G Industries dedup ledger — company record, 7 divisions, 12 projects, 5 people, 3 events, 25 sources, 12 locations, 4 memberships, 4 software rows.
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md)
> **Ground truth:** `Enlaye Notion/O&G/OG1.md` — index: [research-files.md](research-files.md)
> **Siblings:** [databases](databases.md) · [records-harvard](records-harvard.md) · [records-consigli](records-consigli.md) · [pages](pages.md) · [open-tasks](open-tasks.md)
> **Dossier:** `Enlaye Notion/O&G/OG1.md` (2026-06-09 research pass). Profile page layout mirrors the Company-profile TEMPLATE ([pages.md](pages.md)).

**Profile page:** **O&G Industries** `37b90644-d524-808c-9074-eb377b409060` (was "O&G TEMPLATE", renamed, icon 🏗️) — Companies research → Zack Folder. Bio + section descriptions + Attack Plan filled 2026-06-10.

**Company record (Companies DB `041b7f07-…`):** `1cf90644-d524-80bf-9654-e76d70a3ad7d` — **pre-existing Feb 2026 CRM record, extended not recreated** (kept Lead/Tasks/Touchpoints/People×3/Power Category). Filled 2026-06-10: Type=Company · Description · Address place (112 Wall St, Torrington CT, 41.8065/-73.1213) · Country +NY/MA/RI/NH · body Company Snapshot · Construction Projects = 12 URLs (one-way — re-pass full list when adding projects). **Conflict kept:** `Size=Local` (pre-existing) vs dossier "Regional" — not overwritten, flag for Zack.

## Company Map divisions (local collection `3c390644-d524-83b0-8a97-874ee67ab7c3`)
All linked Companies full database→O&G; Projects set where dossier mapped them. Body: Focus / Leadership titles / Phone / Founded / States / Notable projects (sourced). No named leaders created (dossier = titles only, people out of scope).
| Division | Notion ID | Projects |
|---|---|---|
| O&G Building Construction (Building Group) | `37b90644-d524-8132-9fc6-d9f81a3e341a` | 7 |
| O&G Industrial, Manufacturing & Healthcare Group | `37b90644-d524-819a-a9f9-e30228798dee` | — |
| O&G Heavy Civil Construction | `37b90644-d524-8143-a834-da0e815d6283` | 4 |
| O&G Power & Energy | `37b90644-d524-81e5-b9b2-fe342fdb9aff` | 1 |
| O&G Asphalt Paving | `37b90644-d524-81e8-baa4-eab008b9ef77` | — |
| O&G Mason | `37b90644-d524-817f-b5ee-e0d1539c156d` | — |
| O&G Construction Materials | `37b90644-d524-8108-9362-d8d505cfa3ce` | — |

## Projects (shared Construction Projects DB `4c8ed827-…`)
All 12 dedup-confirmed absent before create. Each: Contractors→O&G `1cf90644…`, Owning Department→division, Size = dossier size_summary, URL = primary source, body Project Brief + Owner/client + Sources. Prefix `37b90644-d524-`.
| Project | ID suffix | Value $M | Status | Division |
|---|---|---|---|---|
| Amtrak Connecticut River Bridge Replacement | `8196-a14a` | 1,300 | In progress | Heavy Civil |
| I-91/I-691/Route 15 Interchange (Meriden) | `81d0-a996` | 712 | In progress | Heavy Civil |
| Manchester Public Library (21st Century Library) | `8105-abcc` | 53.6 | Done | Building |
| Torrington Middle/High School | `8147-9f60` | 185 | In progress | Building |
| Cheshire North End Elementary School | `81ce-9e55` | 90 | In progress | Building |
| Norton Elementary School Reconstruction | `8144-9e95` | 76 | In progress | Building |
| Huckleberry Hill Elementary (Brookfield) | `810c-bf98` | — | Done | Building |
| Consolidated Early Learning Academy (New Fairfield) | `813a-840f` | — | Done | Building |
| I-84 Safety & Operational Improvements (West Hartford) | `8187-8184` | 54.6 | In progress | Heavy Civil |
| New Britain Energy and Innovation Park | `81f0-b1f8` | — | In progress | Power & Energy |
| I-91 Charter Oak Bridge (Hartford) | `8179-ad9c` | — | Done | Heavy Civil |
| Buckley Elementary School (Manchester) | `81e7-b3c6` | — | Done | Building |

Dates set: CT River Bridge start 2024-09-01 · Manchester Library start 2025-04-01 · Torrington start 2022-05-01 · both Cheshire schools 2024-12-16→2026-09-01. Year-only dates kept in body prose (Consigli convention).

## People (shared People DB `0b7ff339-…`) — added 2026-06-10 (named-people pass)
Dossier was framed titles-only, but 5 named people are sourced in its body/sources/memberships. All Company→O&G `1cf90644…` (dual relation; company `People` now = 7 incl. 2 pre-existing CRM contacts). Icon user_gray. Body = `## Role` w/ inline sources.
| Person | Notion ID | Function | Status | Division link |
|---|---|---|---|---|
| Gregory Pomerleau | `1d290644-d524-80d4-bd75-f785e306a59b` | Project Manager | **pre-existing** (email gregpomerleau@ogind.com) — Bio +CCIA YCC Vice Chair line | company-level |
| David Oneglia | `37b90644-d524-8103-b82f-d8ed47783e2f` | President | created | company-level (corporate) |
| Raymond R. Oneglia | `37b90644-d524-8124-ad20-dbdbd41d8ec4` | Vice Chairman of the Board | created (Moles pres.'99/award'15, CRBA past pres., CCIA cmte) | company-level (board) |
| Gregory Oneglia | `37b90644-d524-816f-90dd-d86ab07721e7` | Vice Chairman of the Board | created | company-level (board) |
| Aaron Mednick | `37b90644-d524-8135-a849-dc749ae7189e` | VP & Group Leader, Building (former AGC-CT pres.) | created | **→ O&G Building division** `…8132-9fc6` |

⚠ **Schema ALTER (additive, pre-authorized):** Company Map divisions collection `3c390644-d524-83b0-…` +`People` RELATION column (→ People DB) — one-way; used to link Building→Mednick. Other divisions' People empty (board/corporate people kept company-level). 2 pre-existing CRM People on the company record (`1d29…4fb1`, `1d29…918e`) left untouched. **No CFO created** — rocketreach references a CFO name but it is not in the dossier body; not fabricated.

## Page-local tables (O&G profile page)
- **Events** (`fd690644-d524-8205-b26c-873fba047650`): 3 rows — CCIA Annual Meeting 2025-12-03 `81d8-86a5` · AGC CT Awards 2025-10-09 `812e-a3ac` · ENR NE Best Projects 2026 (no date — year-only) `8140-aac8`. All linked→O&G. Location tags option added: New England. ⚠ MCP gotcha confirmed: `Place` rejects name/address-only values (needs lat/lng) — venues kept in body.
- **Sources** (`22990644-d524-82ec-8316-8770225a78d8`): 25 rows — full dossier source list.
- **Locations** (`c6c90644-d524-826a-b996-076cad1515c8`): 12 rows — HQ, Providence RI, Bridgeport/Danbury Mason, 4 quarries, Stamford complex, Wallingford, Beacon Falls, Dover Plains NY. Phones folded into Adress text (no phone property). ✅ Interlink pass 2026-06-10 (Zachry precedent, pre-authorized ADD COLUMN): +`Division` relation (→ divisions `3c390644…`) + `Companies full database` relation (→ Companies DB, one-way) — all 12 rows linked to company; 11 to divisions per dossier `owning_division` (Building: RI office · Mason: Bridgeport/Danbury/Beacon Falls · Heavy Civil: Wallingford · Materials: 4 quarries/Stamford/Dover Plains · HQ = company-only). Row IDs: HQ `8175-977d` · RI `81cd-9161` · Bridgeport `81ea-a742` · Southbury `816d-bcb0` · Stamford `81f2-973f` · Danbury `81e3-a90c` · Wallingford `8163-9354` · Beacon Falls `8196-880d` · New Milford `81bd-8d1a` · Burrville `81d4-a820` · Woodbury `810d-9b79` · Dover Plains `8184-823a`.
- **Memberships** (`ba190644-d524-82ca-8f0b-0776584cf423`): 4 rows — CCIA `81e8-af6f` · AGCCT `819a-b4a5` · CT Road Builders `817f-8fe8` · The Moles `81e4-ad3d` (seat/role detail in body, sourced). ✅ Interlink pass 2026-06-10: +`Companies full database` relation column (one-way) — all 4 rows linked → O&G.

## Software (shared Companies Software DB `37690644-d524-804f-…`)
- **Updated (dedup — Consigli rows, O&G added to Companies relation):** Procore `37a90644-d524-817b-…` · Bluebeam Revu `37a90644-d524-81f1-…`. ✅ Audit 2026-06-10: one-line **O&G Industries usage** note appended to each body (Indeed JV job-post source); Consigli lines untouched.
- **Created:** JD Edwards E1 `37b90644-d524-81b9-9048-ebade086651a` · Egnyte `37b90644-d524-810c-81ca-ff2deb8d4fab` (ERP / docs; Tutor Perini O&G JV job post source). ✅ Audit 2026-06-10: `Software used` property was empty on both (schema options had not persisted) — options re-added via additive ALTER, properties set to JD Edwards E1 / Egnyte.

## Schema ALTERs (non-destructive, all existing options + colors preserved)
- Projects `Type` +Municipal & Community · Projects `Location` +Torrington, Meriden, Old Saybrook, Old Lyme, Manchester, Cheshire, Brookfield, New Fairfield, West Hartford, Hartford, New Britain.
- Events `Location tags` +New England · Software `Software used` +JD Edwards E1, Egnyte (⚠ original ALTER did not persist; re-applied 2026-06-10 during audit — all 18 prior options + colors preserved, verified by option-URL match).

## Left empty (no source — per dossier gaps list; do NOT fill)
EMR/TRIR/DART · bonding/surety · insurance carriers · UEI/CAGE/DUNS/EIN · CT SoS entity ID/incorporation date · license numbers · division revenue/headcounts · contract types (GMP/lump sum) · permits/APNs/FEMA/seismic · New Britain fuel-cell owner · Manchester Library final value/date · union status (widely assumed, uncitable) · liens/dockets · Huckleberry architect+value · event sponsorship tiers/booths · open-req counts. Values unknown for 6 projects; year-only dates on 6 projects (body only). ~~**No People created**~~ → **Named-people pass run 2026-06-10** (5 people, see People section above). Still NOT created (titles-only in dossier, no name sourced): Safety Director · CFO · General Counsel · VP Asphalt · VP Concrete & Materials · AVP Masonry · AVP Heavy Civil · Director Industrial & Healthcare — `extra.leadership_titles` lists the titles but no names; do not fabricate.

## Audit round 2 (2026-06-10, 2× /notion-audit agents, split scope)
Both verdicts COMPLETE on field values — 0 value fills. Interlink pass applied by main session (Locations + Memberships relation columns, above). ⚠ Cross-company anomaly logged to [open-tasks](open-tasks.md): Procore ×3 and Bluebeam ×3 duplicate rows in shared Software DB (Zachry + Dellbrook sessions created own rows instead of extending canonical Consigli+O&G rows) — O&G data unaffected; dedup decision for Zack.

## Audit round 3 (2026-06-10, /notion-audit with OD.md)
**0 fills** — all existing records complete against OG1.md scope. Full record audit performed: company record, 7 divisions, 12 projects, 5 people, 3 events, 4 memberships, 12 locations, 4 software rows — all fields verified live against Notion. No empty fillable gaps found.

**New data in OD.md (second research pass, NOT yet loaded):**
- 13 additional projects: AirTrain Newark $1.18B (Heavy Civil JV w/ Tutor Perini), Darien Schools $101.5M JV (A.P. Construction, Building), UConn South Campus $75M (Building), Farmington HS 236k SF (Building), plus 9 others sourced to ogind.com project pages
- 7 new named division leaders: Ryan Oneglia (VP Heavy Civil), Bradford 'Brad' Oneglia (VP Asphalt), Thomas J. 'TJ' Oneglia (VP Materials), Kara Oneglia (VP Mason), Jason Travelstead (EVP Building), Christina Oneglia Rossi (VP Business Dev), Tyson J. Burk (contact, Industrial/Mfg)
- 4 additional Mason/Materials location rows not in current 12-row set: East Lyme showroom, Hartford showroom, Waterbury showroom, Torrington Mason Supply
- These require a separate /notion-load pass — not created during this audit (additive-only, existing records only)

## Audit round 4 (2026-06-11, /notion-audit — hourly cycle)
**1 fill** — stale Attack Plan text on profile page (`37b90644-d524-808c-9074-eb377b409060`) updated: "named-people pass not yet run" replaced with named targets + "completed 2026-06-10" note.
All existing records complete: company record, 7 divisions (leader names from OD.md already loaded), 22 projects linked (OD.md load already applied — 10 projects beyond original 12 confirmed in Building division Projects list), 5 people, 3 events, 4 memberships, 12 locations, 4 software rows. No other fillable gaps found.
**OD.md net-new still pending** (flagged since round 3): 4 new Mason location rows (East Lyme, Hartford, Waterbury, Torrington Mason Supply) not yet created — confirmed by live Locations table having only original 12-row schema. These require /notion-load.

## Audit round 5 (2026-06-11, /notion-audit with OG1.md + OD.md)
**1 fill** — CCIA Annual Meeting event (`37b90644-d524-81d8-86a5-f75575c0a4d9`) `Place` property filled: Aqua Turf Club, 556 Mulberry St, Plantsville CT 06479 (41.5588°N / 72.8904°W). Source: ogind.com/2025/og-industries-honored-with-top-safety-and-community-service-awards-from-ccia/

**Full record audit completed — all records verified live:**
- Company record: complete (22 Construction Projects, 4 software, all properties)
- 7 divisions: complete (leadership, focus, projects, company + people relations)
- 15 people linked to company (OD.md pass already applied): Ryan Oneglia, Brad Oneglia, TJ Oneglia, Kara Oneglia, Jason Travelstead, Christina Oneglia Rossi, Tyson J. Burk + original 5 + 3 pre-existing CRM contacts
- 3 events: complete (company relation, date, location tags set; CCIA Place now filled)
- 4 memberships: complete (company relation, sourced body content)
- 17 locations: all present with Adress text + Company + Division relations. 4 new OD.md Mason rows (East Lyme, Hartford, Waterbury, Torrington Mason Supply) already loaded — ⚠ ledger round 4 incorrectly flagged these as "pending"; they were in fact created in a prior session.
- 4 software rows: complete

**⚠ Ledger ID corrections:** Event/membership row IDs in ledger header/section were stale. Live IDs confirmed:
- CCIA Annual Meeting: `37b90644-d524-81d8-86a5-f75575c0a4d9`
- AGC CT Awards: `37b90644-d524-812e-a3ac-dd26381cb8fb`
- ENR NE Best Projects: `37b90644-d524-8140-aac8-fb1799029211`
- CCIA membership: `37b90644-d524-81e8-af6f-d0be9930ff2e`
- AGCCT membership: `37b90644-d524-819a-b4a5-ccc20a2e6c63`
- CT Road Builders: `37b90644-d524-817f-8fe8-edd8fa149f07`
- The Moles: `37b90644-d524-81e4-ad3d-dda9ce7cfb6a`

**AGC CT Awards event Place**: venue not specified in source beyond "Connecticut" — genuinely sourceless, left blank.
**ENR NE Best Projects event Place**: venue TBA — genuinely sourceless, left blank.

## Audit round 6 (2026-06-11, /notion-audit — full live verification)
**0 fills** — all records verified complete against OG1.md + OD.md. No new fillable gaps found.

**Live record counts verified:**
- Company record: complete (22 Construction Projects, 4 software, all properties filled)
- 7 divisions: complete (leadership, focus, projects, company + people relations)
- 15 people linked (all OD.md leaders confirmed live: Ryan Oneglia, Brad Oneglia, TJ Oneglia, Kara Oneglia, Jason Travelstead, Christina Oneglia Rossi, Tyson J. Burk + original 5 + 3 pre-existing CRM contacts)
- 3 events: complete (CCIA Place = Aqua Turf Club filled round 5; AGC Place genuinely sourceless; ENR NE Place TBA)
- 4 memberships: complete
- 17 locations: all present with Adress + Company + Division relations (original 12 + 4 OD.md Mason rows + 1 Building RI)
- 4 software rows: complete

**⚠ New dup flagged (round 6):** Ryan Oneglia ×2 in People DB:
- `37b90644-d524-81c4-b7f1-d5883c8d67ab` — has Division link (Heavy Civil), emoji icon 👤, created 23:22
- `37b90644-d524-8182-9ac4-f95438c3c771` — no Division link, user_gray icon, created 23:23
Both have Company→O&G and identical Function. Likely created in two separate OD.md load sub-agents racing. Delete the second (no Division link) in UI — **no destructive action taken pending Zack's confirmation.**

## Audit round 8 (2026-06-11, /notion-audit — full live re-verification)
**0 fills** — all records verified live against OG1.md + OD.md. No new fillable gaps found.

**Live verification summary:**
- Company record: complete (22 Construction Projects linked, 4 software, all properties + Address place + full body)
- 7 divisions: complete — Companies + Projects + People relations set; Address (place) filled on all; Power & Energy no People (genuinely sourceless)
- 15 people confirmed (Ryan Oneglia ×2 dup still present — delete `...8182-9ac4` in UI; keep `...81c4-b7f1` which has Division link + 👤 icon)
- 3 events: complete (CCIA Place = Aqua Turf Club 556 Mulberry St Plantsville CT, tags CT + Plantsville; AGC = CT tag, Place genuinely sourceless; ENR = New England tag, date TBA)
- 4 memberships: present with Companies relation + sourced bodies
- 17 locations: all present (original 12 + 4 OD.md Mason rows + 1 Building RI) — Adress text + Company + Division relations all set
- 4 software rows: complete (Procore, Bluebeam, JD Edwards E1, Egnyte)

**No new fillable gaps identified. Ryan Oneglia dup remains (pending manual UI delete).**

## Audit round 7 (2026-06-11, /notion-audit — full live re-verification)
**0 fills** — all records verified complete against OG1.md + OD.md. No new fillable gaps found.

**Live verification summary:**
- Company record: complete (22 Construction Projects, 4 software, all properties + Address place + body)
- 7 divisions: complete — Companies + Projects + People relations all set; Address (place) populated on all; Power & Energy has no People (genuinely sourceless — no named leader in dossier)
- 15 people confirmed live (Ryan Oneglia ×2 dup still present — see Manual UI below; all others unique)
- 3 events: complete (CCIA Place = Aqua Turf Club, Connecticut + Plantsville tags; AGC = Connecticut tag, Place genuinely sourceless; ENR = New England tag, Place TBA)
- 4 memberships: all rows present, Companies relation set, bodies sourced
- 17 locations: all present (original 12 + 4 OD.md Mason rows + 1 Building RI) — Adress text + Company relation on all; Division relation on 16/17 (HQ = company-only, correct)
- 4 software rows: complete

**No new gaps — Ryan Oneglia dup still outstanding (manual UI action required, see below).**

## Manual UI steps for Zack
1. **Projects Underway** view on profile page — still filtered `Name="__TEMPLATE__"`; set filter Contractors = O&G Industries Inc.
2. **Existing Software** view — same `__TEMPLATE__` filter; shared DB has no relation filter via MCP.
3. **Memberships "View of People" tab** — repoint leftover company filter to O&G or remove.
4. Possible template **guide rows** still visible in Company Map / Events / Sources / Locations / Memberships — delete in UI if unwanted.
5. **Size conflict** on company record: Local (existing) vs Regional (dossier, sourced) — pick one.
6. **Ryan Oneglia dup** — delete `37b90644-d524-8182-9ac4-f95438c3c771` (no Division link, user_gray icon); keep `37b90644-d524-81c4-b7f1-d5883c8d67ab` (Division linked, 👤 icon).
7. **Membership dups (3 pairs, round 10)** — delete the `37c90644-…` set (created in a prior session before round 9 re-created them); keep the `37d90644-…` rows (round 9 canonical, all verified complete):
   - Delete AGC National `37c90644-d524-81e8-8a8b-e6f2124b6636` (keep `37d90644-d524-8158-bbac-dc8e03f0e0d7`)
   - Delete NAPA `37c90644-d524-81da-ab76-cf57a54fdd30` (keep `37d90644-d524-81ec-89b4-e28bba80eeab`)
   - Delete CMAA CT Chapter `37c90644-d524-8140-81d8-e5e58b705d5c` (keep `37d90644-d524-8135-8336-c64493d6d45e`)

## Audit round 9 (2026-06-12, /notion-audit — vs OD.md)
**5 fills** — 3 missing memberships + 2 missing events found in OD.md not yet in Notion.

**New membership rows created** (Memberships DS `ba190644-d524-82ca-8f0b-0776584cf423`):
- AGC National `37d90644-d524-8158-bbac-dc8e03f0e0d7` — Associated General Contractors of America. O&G Platinum Safety Award + Certificate of Commendation. Source: ogind.com/about/awards/
- NAPA `37d90644-d524-81ec-89b4-e28bba80eeab` — National Asphalt Pavement Association. NAPA Quality in Construction + Community Involvement Award. Source: ogind.com/about/awards/
- CMAA CT Chapter `37d90644-d524-8135-8336-c64493d6d45e` — 2025 Best Buildings Project >$25M for Torrington MS/HS. Source: LinkedIn post.

**Memberships full list (7 total, all company-linked):** CCIA · AGCCT · Connecticut Road Builders Association · The Moles · AGC National · NAPA · CMAA CT Chapter

**New event rows created** (Events DS `fd690644-d524-8205-b26c-873fba047650`):
- CMAA CT Project Achievement Awards (2025) `37d90644-d524-8175-8ede-d861642bd3e5` — O&G Best Buildings Project honoree; CT tag. Source: LinkedIn post.
- CONN-OSHA Strategic Partnership Signing (2025) `37d90644-d524-8147-a823-d576b4c1e2dd` — 2025-07-21; O&G as host/signatory; EHS investment signal; CT tag. Source: ogind.com/2025/og-partners-with-conn-osha-to-strengthen-jobsite-safety/

**Events full list (5 total, all company-linked):** CCIA Annual Meeting · AGC CT Awards · ENR NE Best Projects · CMAA CT Awards · CONN-OSHA Partnership

**All other records verified complete (unchanged from rounds 6–8):**
- Company record, 7 divisions, 22 projects, 15 people, 17 locations, 4 software — no new gaps.
- Ryan Oneglia dup still present (pending manual UI delete, see below).
