# State · Records — Harvard Build

> **Holds:** the Harvard dedup ledger — owner, 12 projects, 11 GCs, 27 people, 16 department companies. Checked FIRST in dedup ([playbook/loop-and-dedup.md](../playbook/loop-and-dedup.md) §1) before searching Notion.
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md)
> **Ground truth:** `Enlaye Notion/Harvard Researsch/1Harvard University Construction Intelligence Resea.md` + `2Harvard Researsch.md` — index: [research-files.md](research-files.md)
> **Siblings:** [databases](databases.md) · [records-consigli](records-consigli.md) · [pages](pages.md) · [open-tasks](open-tasks.md)

> Append a row every time a record is created or updated.

## Owners
| Name | Notion ID | Status | Last touched |
|---|---|---|---|
| Harvard | `37990644-d524-80b8-9f63-f25b06e96d20` | enriched — single owner for all Harvard projects | 2026-06-08 |

## Construction Projects — Harvard build (12, all Owner→Harvard)
| Project | Notion ID | GC(s) linked |
|---|---|---|
| Enterprise Research Campus (ERC) Phase A | `37990644-d524-8142-9b0d-c39f4eb862dc` | Turner, Consigli, Smoot, Skanska, Janey, J&J |
| American Repertory Theater (Goel Center) & 100 South Campus Drive | `37990644-d524-81c6-81e5-e7dad395faab` | Shawmut |
| Eliot House Renewal | `37990644-d524-8120-80c8-d33d0231cc0f` | Shawmut |
| Pritzker Hall (Economics) | `37990644-d524-8143-bbc6-ec4a765df64c` | Consigli [med] |
| William James Hall Plaza Renovation | `37990644-d524-81f1-a367-c6f43651fbff` | G. Greene |
| Barker Center Roofing Project | `37990644-d524-81e9-bc61-cd0907ef686d` | — |
| 12 Palmer Street Renovation | `37990644-d524-8128-aea7-ff8451df575d` | Consigli |
| HBS Chase / McCulloch / Dillon Renovation | `37990644-d524-8102-b2bf-eb263b4b06e1` | Suffolk |
| HMS Building C / Bertarelli Renovation | `37990644-d524-812b-9709-fb6e79b94ce4` | Shawmut [med] |
| North Allston Storm Drain Extension (NASDEP) | `37990644-d524-817a-83a3-dc7aec135af6` | IC&E |
| Campus Steam Tunnel Project 29/30 | `37990644-d524-8103-a870-f0946fa2319b` | — (BOND did prior Blackstone) |
| Engineering Sciences Lab (ESL) Renewal (SEAS) | `37990644-d524-813e-9866-c15b6f07a0b8` | — |

## Companies (GCs) — Harvard build (11; all Owners→Harvard + Construction Projects linked + sourced body)
| Name | Notion ID | Action |
|---|---|---|
| Shawmut Design and Construction | `19990644-d524-8021-a4a6-f0a6321589f6` | enriched |
| Turner | `18290644-d524-80f5-aadf-e92fa8d5a93c` | enriched |
| Consigli Building Group | `19990644-d524-801a-a283-e806cb9b69b1` | enriched — profile page `37a90644-d524-806f-a31d-e6ef42083b66` fully filled: Company Map ×20 rows, 7 Existing Software rows, Attack Plan complete |
| Suffolk Construction | `17b90644-d524-8044-9514-eda61dd449ae` | enriched |
| Skanska USA | `2fb90644-d524-8070-a903-fb03fc1d8334` | enriched |
| BOND Civil & Utility | `30a90644-d524-80a2-aa67-f2a11366d4d1` | enriched (Blackstone note; has child Task/Ticket DBs) |
| Janey Construction | `1cf90644-d524-80da-9a63-cf5f9605151a` | enriched |
| G. Greene Construction Co. | `21b90644-d524-801d-bdc2-c579a1b7ca8b` | enriched |
| Smoot Construction Company of Washington DC | `37990644-d524-81f4-a2ea-d6a1a7769db6` | **created** |
| Innovative Contracting & Engineering | `37990644-d524-8120-9793-cd5de157e403` | **created** |
| J&J Contractors | `37990644-d524-814b-b3fe-e1fd45c10ca1` | **created** |

## People — Harvard build (27; owner-side all Owner→Harvard unless noted)
- **Created (25):** Purnima Kapur (HUPAD, P0) · Jennifer Cohen (HALC, P0) · Nitin Nohria (HALC/HBS, P1) · Jessica Finch (HUPAD, P2) · Alexandra Toteva (HALC, P1) · Craig McCurley (HALC, P1) · Brenda Messervy (HALC, P2) · Neal Schutt (HALC, P2) · Lisa Giovanetti (FAS House Renewal, P1) · Rich LeBlanc (HMS, P0) · Dave LaPlante (HMS, P1) · Meaghan Doyle Paquette (HMS, P1) · Tarah Hyatt Allen (HMS, P2) · Sarah Henning (Harvard Capital Projects, P1) · Tory Wolcott Green (HCP, P1) · Alyssa Hubbard (HCP, P1) · John Martell (HCP, P1) · David Armitage (HCP, P1) · Anne-Sophie Divenyi (FAS, P1) · Edward LeFlore (CSL, P1) · Ann Davis (CSL, P2) · Nicole Clement (CSL, P2) · Holly Sutherland (CSL, P2) · Shane O'Halloran (CSL, P2) · Anthony Consigli (Consigli CEO, P1 — **Company→Consigli**, not Owner).
- **Updated existing (2):** Tom O'Connor `24890644-d524-80c9-a96a-f4f85471f707` (MD Harvard Capital Projects; +Owner→Harvard, P0) · Shallan Fitzgerald `2c690644-d524-802d-91d7-f5fd84fcaa3d` (HALC Dir. Infrastructure; +Owner→Harvard, +ERC/NASDEP, P1).

## Harvard Departments — Company subsidiary hierarchy (2026-06-08)
Departments are **Companies** (BW Category `Owner`), nested under parent **Harvard University** via `Parent Company`⇄`Subsidiaries`. Each links to the Harvard owner via the new **`Owner Institution`**⇄ Owners **`Departments`** relation, and to its projects via the new **`Owned Projects`**⇄ Projects **`Owning Department`** relation. People link via `Company`. Varied emoji icons. **Two new relations added** to keep departments out of the GC `Contractors`/`General Contractors` fields.

| Emoji | Department (Company) | Notion ID | Parent | Action |
|---|---|---|---|---|
| 🏛️ | Harvard University (parent) | `18390644-d524-80e6-98d9-ef8bafd05ed5` | — | enriched |
| 🏗️ | Harvard Allston Land Company | `2c690644-d524-8084-abe2-d0993c4206fe` | Harvard University | enriched |
| 🗺️ | Harvard University Planning & Design (HUPAD) | `37990644-d524-8138-8c9c-cb771af9ad3d` | Harvard University | created |
| 🏢 | Harvard Capital Projects | `37990644-d524-81e7-93a9-d1983cbed35b` | Harvard University | created |
| ⚡ | Harvard Engineering & Utilities | `37990644-d524-8109-a524-d179812bb783` | Harvard University | created |
| 🏬 | Harvard Real Estate | `37990644-d524-8105-b86f-e5203c4872a4` | Harvard University | created |
| 🏠 | Harvard University Housing | `37990644-d524-812a-b3dd-ea882c35077b` | Harvard University | created |
| 🧭 | Office of the Executive VP (EVP) | `37990644-d524-8159-b043-f9c1ea28270e` | Harvard University | created |
| 🌱 | Harvard Office for Sustainability | `37990644-d524-818b-84d8-d88bb4c63aac` | Harvard University | created |
| 📐 | Harvard Faculty of Arts & Sciences (FAS) | `37990644-d524-81f6-8be1-d2efaee2437a` | Harvard University | created |
| 🛠️ | FAS House Renewal PMO | `37990644-d524-811d-bf3b-df3091837c8e` | **FAS** | created |
| ⚕️ | Harvard Medical School — Campus Planning & Facilities | `37990644-d524-8104-ad19-d590eb28d9d6` | Harvard University | created |
| ⚙️ | Paulson School of Engineering & Applied Sciences (SEAS) | `37990644-d524-81f0-bd41-ec566b7a6817` | Harvard University | created |
| 💼 | Harvard Business School (HBS) | `37990644-d524-8187-b76d-fc24877c9906` | Harvard University | created |
| 🎭 | American Repertory Theater (A.R.T.) | `37990644-d524-81dc-8a07-d2a2ab2e98e1` | Harvard University | created |
| 📣 | CSL Consulting LLC (mitigation vendor) | `1cf90644-d524-80c2-9d8c-e1bbd9cc5c04` | — (not a subsidiary) | enriched |

Harvard owner `Departments` rollup = 16 companies; `General Contractors` unchanged (11 GCs, unpolluted).

## Audit log — 2026-06-10
**Addresses added (place:Adress, 3c):**
- Eliot House Renewal → 101 Dunster Street, Cambridge, MA 02138
- William James Hall Plaza → 33 Kirkland Street, Cambridge, MA 02138
- Barker Center Roofing → 12 Quincy Street, Cambridge, MA 02138
- HBS Chase/McCulloch/Dillon → 34 Harvard Way, Boston, MA 02163
- HMS Building C / Bertarelli → 240 Longwood Avenue, Boston, MA 02115
- ESL Infrastructure Renewal → 58 Oxford Street, Cambridge, MA 02138

**Description fixes (departments):**
- HMS Campus Planning & Facilities — `Description` was empty → filled
- Harvard Office for Sustainability — `Description` was empty → filled
- Harvard Office of the EVP — `Description` was empty → filled
- Harvard FAS — `Description` corrected (removed erroneous "12 Palmer Street" attribution)

**No fills (genuinely sourceless):**
- Harvard owner `LinkedIn` — no URL in dossier
- NASDEP / Steam Tunnel 29/30 `place:Adress` — no single precise street address in source
- Lewis International Law Center address — dossier gives campus area only, no street number
- All `LinkedIn` fields on departments — not in source
- All `Website` fields on departments — not in source

**3a check:** all owner↔department↔project edges intact. No missing relation edges.
**3b check:** all project bodies complete; department bodies adequate.
**3d memberships:** N/A (Owner entity, no memberships table).
**3e location tags:** all project Location fields populated; no missing tags.

**13th project found:** Lewis International Law Center Renovation `37b90644-d524-8198-a97e-fefc1444e834` (Shawmut GC, added after initial build from Shawmut dossier — not in original ledger). Owning dept: `37b90644-d524-811c-9937-c91b1e37bf88` (Harvard Law School, separate company — not in this ledger).

## Audit log — 2026-06-11 (second pass — completion dates)
**Filled — `date:Date:end` (estimated completion) added to 11 of 13 projects:**
- ERC Phase A `37990644-d524-8142-9b0d-c39f4eb862dc` → end = 2026-12-31 (source: dossier 1, WCN)
- ART / 100 South Campus Drive `37990644-d524-81c6-81e5-e7dad395faab` → end = 2026-10-31 (source: dossier 2)
- Eliot House Renewal `37990644-d524-8120-80c8-d33d0231cc0f` → end = 2027-09-01 (source: dossier 2, Crimson)
- Pritzker Hall `37990644-d524-8143-bbc6-ec4a765df64c` → end = 2027-12-01 (source: dossier 2, Crimson)
- William James Hall Plaza `37990644-d524-81f1-a367-c6f43651fbff` → end = 2026-06-30 (source: dossier 2)
- Barker Center Roofing `37990644-d524-81e9-bc61-cd0907ef686d` → end = 2026-06-30 (source: dossier 1 + 2)
- 12 Palmer Street `37990644-d524-8128-aea7-ff8451df575d` → end = 2026-04-30 (source: dossier 2)
- HBS Chase/McCulloch/Dillon `37990644-d524-8102-b2bf-eb263b4b06e1` → end = 2026-08-31 (source: dossier 2)
- HMS Building C / Bertarelli `37990644-d524-812b-9709-fb6e79b94ce4` → end = 2026-10-01 (source: dossier 2)
- NASDEP `37990644-d524-817a-83a3-dc7aec135af6` → end = 2025-12-31 (source: dossier 1)
- Steam Tunnel 29/30 `37990644-d524-8103-a870-f0946fa2319b` → end = 2027-11-01 (source: dossier 1)

**Filled — body depth (3b):**
- Tom O'Connor `24890644-d524-80c9-a96a-f4f85471f707` — Bio section filled (was empty; dossier has role, scope, reporting chain)

**No fills (genuinely sourceless — confirmed this pass):**
- ESL SEAS `date:Date:end` — completion not disclosed in source
- Lewis International Law Center `date:Date:end` — not disclosed in source
- Lewis International Law Center `date:Date:start` — not disclosed in source
- All `Contrat Value in Million` fields not already filled — not publicly disclosed

**3a check:** all owner↔department↔project↔people↔GC edges intact — no missing relation edges.
**3b check:** project bodies complete; department bodies adequate; people bodies adequate for priority level.
**3d memberships:** N/A (owner entity, no memberships table).
**3e location tags:** all 13 project Location fields populated; no missing tags.

## Audit log — 2026-06-11
**Filled:**
- HMS Building C / Bertarelli Renovation `37990644-d524-812b-9709-fb6e79b94ce4` → `Contrat Value in Million` = 75 (sourced: Bertarelli $75M gift — https://hms.harvard.edu/about-hms/office-dean/messages/big-news-about-building-c)

**Already complete (no gaps found):**
- Harvard owner record — all key fields populated
- 12 of 13 projects: all had Owner, Location, Owning Department, Contractors (where known), Status, Type, Date, Adress, Size, URL, and sourced body
- All relation edges (owner↔department↔project↔people↔GC) intact
- All project Location tags set

**No fills (genuinely sourceless — confirmed):**
- NASDEP `place:Adress` — corridor description only, no single street address in source
- Steam Tunnel 29/30 `place:Adress` — no single street address in source
- Lewis International Law Center `place:Adress` precise street — dossier gives campus area only
- Lewis International Law Center `date:Date:start` — not disclosed in source
- Barker Center `Contractors` — GC not publicly disclosed
- Steam Tunnel 29/30 `Contractors` — GC not publicly disclosed
- ESL SEAS `Contractors` — GC not publicly disclosed
- All `LinkedIn` / `Website` fields on departments — not in source
