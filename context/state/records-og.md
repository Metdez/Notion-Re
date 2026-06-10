# State · Records — O&G Industries Build

> **Holds:** the O&G Industries dedup ledger — company record, 7 divisions, 12 projects, 3 events, 25 sources, 12 locations, 4 memberships, 4 software rows.
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
EMR/TRIR/DART · bonding/surety · insurance carriers · UEI/CAGE/DUNS/EIN · CT SoS entity ID/incorporation date · license numbers · division revenue/headcounts · contract types (GMP/lump sum) · permits/APNs/FEMA/seismic · New Britain fuel-cell owner · Manchester Library final value/date · union status (widely assumed, uncitable) · liens/dockets · Huckleberry architect+value · event sponsorship tiers/booths · open-req counts. Values unknown for 6 projects; year-only dates on 6 projects (body only). **No People created** — dossier scope was titles-only (President; 2× Vice Chairman; VPs; Safety Director; CFO; General Counsel — listed in dossier `extra.leadership_titles`); named-people pass not yet run.

## Audit round 2 (2026-06-10, 2× /notion-audit agents, split scope)
Both verdicts COMPLETE on field values — 0 value fills. Interlink pass applied by main session (Locations + Memberships relation columns, above). ⚠ Cross-company anomaly logged to [open-tasks](open-tasks.md): Procore ×3 and Bluebeam ×3 duplicate rows in shared Software DB (Zachry + Dellbrook sessions created own rows instead of extending canonical Consigli+O&G rows) — O&G data unaffected; dedup decision for Zack.

## Manual UI steps for Zack
1. **Projects Underway** view on profile page — still filtered `Name="__TEMPLATE__"`; set filter Contractors = O&G Industries Inc.
2. **Existing Software** view — same `__TEMPLATE__` filter; shared DB has no relation filter via MCP.
3. **Memberships "View of People" tab** — repoint leftover company filter to O&G or remove.
4. Possible template **guide rows** still visible in Company Map / Events / Sources / Locations / Memberships — delete in UI if unwanted.
5. **Size conflict** on company record: Local (existing) vs Regional (dossier, sourced) — pick one.
