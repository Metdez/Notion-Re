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

**New data in OD.md (second research pass, NOT yet loaded at time of round 3):**
- 13 additional projects, 7 new named leaders, 4 new Mason location rows — flagged for /notion-load pass.

## Audit round 6 (2026-06-13, /notion-audit — OG1.md + OD.md full re-verify)
**0 fills** — all records verified live against Notion; no fillable gaps against either dossier.

Live verification confirmed: company record (all properties populated), profile page body complete, 7 divisions complete, 22 projects present and linked (Contractors + Owning Department set), 12+ named People linked (Company + Division relations), 4 OG1.md memberships + 3 OD.md memberships present (6 dedup-needed rows outstanding), 16 location rows confirmed (OD.md Mason locations loaded), 4 software rows complete.

**Correction still pending (not changed — requires Zack decision):** Bridgeport Mason Showroom address "240 Bostwick Ave" (OG1.md/BBB source) vs "325 Hancock Ave" (OD.md / mason.ogind.com — more authoritative). This is a correction, not an additive fill.

**Outstanding for Zack (unchanged from rounds 4-5):**
- Size=Local vs Regional conflict on company CRM record
- 3 duplicate membership pairs (37d-prefix rows): AGC National, NAPA, CMAA CT Chapter
- LinkedIn/Apollo bulk import People dupes (37d-prefix, 100+ thin rows linked to O&G)
- 3 view TEMPLATE filters still showing in profile page (Projects Underway, Existing Software, Memberships "View of People")

---

## Audit round 5 (2026-06-13, /notion-audit — OG1.md + OD.md full re-verify)
**0 fills** — all records verified live against Notion; no fillable gaps against either dossier.

**New flag:** OD.md gives Bridgeport Mason address as "325 Hancock Ave" (mason.ogind.com — more authoritative); existing row uses "240 Bostwick Ave" (OG1.md/BBB). This is a **correction** not an additive fill — flagged for Zack. Not changed this pass.

**Outstanding (same as round 4):** Size=Local vs Regional conflict · 3 dup membership pairs (37d-prefix) · LinkedIn import People dupes · 3 view TEMPLATE filters.

---

## Audit round 4 (2026-06-12, /notion-audit — OD.md data check)
**0 fills** — OD.md data was fully loaded by an intervening session (between round 3 and round 4). All records verified live.

**What was loaded (by a post-round-3 session, not recorded):**
- 22 Construction Projects now linked on company record (was 12 after round 3) — OD.md projects confirmed present: AirTrain Newark ($1.18B), Darien Schools ($101.5M JV w/ A.P. Construction), UConn South Campus ($75M), Farmington HS, Winsted Health Center ($30M), USJ Pope Pious XII Library ($10M), Middlefield Memorial School ($63M), Cricket Valley Energy Center, SMART Technology Solution, and others.
- 7 OD.md division leaders created in People DB: Ryan Oneglia (VP Heavy Civil) `37b90644-d524-81c4`, Bradford 'Brad' Oneglia (VP Asphalt) `37b90644-d524-8179`, Thomas J. 'TJ' Oneglia (VP Materials) `37b90644-d524-81ac`, Kara Oneglia (VP Mason) `37b90644-d524-819c`, Jason Travelstead (EVP Building) `37b90644-d524-8162`, Christina Oneglia Rossi (VP Business Dev) `37b90644-d524-81d1`, Tyson J. Burk (contact, Industrial/Mfg) `37b90644-d524-81f6`. All linked to O&G company record + respective divisions.
- 4 new Mason location rows: East Lyme `37b90644-d524-8192` · Hartford `37b90644-d524-81fd` · Waterbury `37b90644-d524-814a` · Torrington Mason Supply `37b90644-d524-813c`. All linked to company + Mason division. Addresses filled (text field).
- 3 additional Memberships: AGC National `37c90644-d524-81e8` · NAPA `37c90644-d524-81da` · CMAA CT Chapter `37c90644-d524-8140`. All linked → O&G.

⚠ **DUPLICATES detected — flag for Zack (dedup decisions needed):**

**Memberships (3 duplicate pairs, all linked to O&G):**
- AGC National: `37c90644-d524-81e8` (2026-06-11) AND `37d90644-d524-8158` (2026-06-12) — identical content
- NAPA: `37c90644-d524-81da` (2026-06-11) AND `37d90644-d524-81ec` (2026-06-12) — identical content
- CMAA CT Chapter: `37c90644-d524-8140` (2026-06-11) AND `37d90644-d524-8135` (2026-06-12) — identical content
→ Delete the 37d-prefix rows in each pair (they are the later duplicates). Decision for Zack.

**People (duplicates from LinkedIn/Apollo bulk import ~2026-06-12):**
- Ryan Oneglia: `37b90644-d524-81c4` (OD.md load, has Division) AND `37b90644-d524-8182` (second OD.md load) — identical content; keep `81c4`, delete `8182`
- Raymond R. Oneglia: `37b90644-d524-8124` (original, full bio) AND `37d90644-d524-81cc` "Raymond Oneglia" (LinkedIn import, thin) — keep `8124`, delete `81cc`
- Gregory Oneglia (Vice Chairman): `37b90644-d524-816f` AND `37d90644-d524-8133` "Greg Oneglia" (LinkedIn) — keep `816f`, delete `8133`
- T.J. Oneglia: `37b90644-d524-81ac` "Thomas J. 'TJ' Oneglia" (OD.md, full) AND `37d90644-d524-8156` "T.J. Oneglia" (LinkedIn) — keep `81ac`, delete `8156`
- Many more 37d-prefix LinkedIn imports may be present on the company People relation (company has 100+ People linked as of 2026-06-12 — bulk import). These are NOT O&G-specific audit scope — flag to Zack as a broader dedup/data-quality issue.
→ **Dedup of 37d-prefix LinkedIn People is an open task for Zack (UI or bulk operation).**

**Left empty (unchanged from OG1.md gaps — no source):** EMR/TRIR/DART · bonding/surety · insurance carriers · UEI/CAGE/DUNS/EIN · CT SoS entity ID · license numbers · division revenue/headcounts · contract types for most projects · permits/APNs/FEMA/seismic · New Britain fuel-cell owner · union status.

## Manual UI steps for Zack (updated 2026-06-12)
1. **Projects Underway** view on profile page — still filtered `Name="__TEMPLATE__"`; set filter Contractors = O&G Industries Inc.
2. **Existing Software** view — same `__TEMPLATE__` filter; shared DB has no relation filter via MCP.
3. **Memberships "View of People" tab** — repoint leftover company filter to O&G or remove.
4. **Duplicate Memberships** — delete 3 duplicate 37d-prefix rows: AGC National `37d90644-d524-8158`, NAPA `37d90644-d524-81ec`, CMAA CT Chapter `37d90644-d524-8135`.
5. **Duplicate People** — delete: Ryan Oneglia `37b90644-d524-8182`; LinkedIn-import dupes `37d90644-d524-81cc` (Raymond), `37d90644-d524-8133` (Greg), `37d90644-d524-8156` (T.J.). Broader 37d-prefix LinkedIn import may have 100+ thin People rows linked to O&G — review and dedup in bulk.
6. **Size conflict** on company record: Local (existing) vs Regional (dossier, sourced) — pick one.
7. Possible template **guide rows** still visible in Company Map / Events / Sources / Locations / Memberships — delete in UI if unwanted.
## Audit round 7 (2026-06-13, /notion-audit — OG1.md re-verify)
**0 fills** — all records verified live against Notion; no fillable gaps against OG1.md.

Live verification: company record (all properties populated), profile page body complete, 7 divisions (Companies + Projects + People relations set; address/place on each; bodies sourced), 22 projects (Contractors + Owning Department set; spot-checked Amtrak CT River Bridge — complete), 12+ named People (Company + Division relations set; role bodies sourced), 7 memberships (CCIA, AGCCT, CT Road Builders, The Moles, AGC National, NAPA, CMAA CT Chapter — all linked → O&G; bodies sourced), 16 location rows (Adress text set; Division linked where applicable; Companies → O&G on all rows), 3 events (Date, Location tags, Place all set; Companies → O&G), 4 software rows complete.

**Outstanding (all for Zack — unchanged):** Size=Local vs Regional conflict · 3 dup membership pairs (37d-prefix): AGC National `37d90644-d524-8158-bbac-dc8e03f0e0d7` / NAPA `37d90644-d524-81ec-89b4-e28bba80eeab` / CMAA CT `37d90644-d524-8135-8336-c64493d6d45e` · LinkedIn/Apollo People dupes (37d-prefix bulk import) · Bridgeport Mason address conflict (OG1.md: 240 Bostwick Ave vs OD.md: 325 Hancock Ave — correction needed, not additive fill).

## Manual UI steps for Zack
1. **Projects Underway** view on profile page — still filtered `Name="__TEMPLATE__"`; set filter Contractors = O&G Industries Inc.
2. **Existing Software** view — same `__TEMPLATE__` filter; shared DB has no relation filter via MCP.
3. **Memberships "View of People" tab** — repoint leftover company filter to O&G or remove.
4. Possible template **guide rows** still visible in Company Map / Events / Sources / Locations / Memberships — delete in UI if unwanted.
5. **Size conflict** on company record: Local (existing) vs Regional (dossier, sourced) — pick one.
6. **Duplicate memberships** — delete 3 duplicate 37d-prefix rows: AGC National `37d90644-d524-8158`, NAPA `37d90644-d524-81ec`, CMAA CT `37d90644-d524-8135`.
7. **Duplicate People** — LinkedIn/Apollo bulk import created 37d-prefix thin rows; review and dedup in bulk.
8. **Bridgeport Mason address** — 240 Bostwick Ave (OG1.md/BBB) vs 325 Hancock Ave (OD.md/mason.ogind.com — more authoritative); correct in UI.
