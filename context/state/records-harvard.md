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

## Audit log — 2026-06-11 (pass 1)
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

## Audit log — 2026-06-11 (pass 2 — full re-audit)
**0 fills — already complete.**

All 13 projects fetched live. Full pass:
- **3a (relations):** All owner↔department↔project↔people↔GC edges intact. All 13 projects have Owner=Harvard, Owning Department(s), and Contractors where the source names one. No missing edges.
- **3b (body depth):** All project bodies carry full sourced brief (scope, GC, owner, dates, sources). Department bodies adequate. People bodies adequate for priority level.
- **3c (addresses):** All projects with a confirmed street address have it set in `place:Adress`. Genuinely sourceless cases (NASDEP, Steam Tunnel 29/30, Lewis Law Center precise street) remain blank — correct.
- **3d (memberships):** N/A — Owner entity has no memberships table.
- **3e (location tags):** All 13 projects have `Location` property populated. No missing tags.

**Genuinely sourceless — confirmed again (no change):**
- Pritzker Hall `place:Adress` precise street — dossier marks "Approx. 1805 Cambridge Street [ESTIMATED]" (not confirmed)
- NASDEP / Steam Tunnel 29/30 / Lewis Law Center street addresses — sourced as corridor/campus area only
- Barker Center / Steam Tunnel 29/30 / ESL SEAS `Contractors` — GC not publicly disclosed
- All department `LinkedIn` / `Website` — not in source

## Audit log — 2026-06-12 (pass 4 — notion-audit skill)
**2 fills — department Website fields.**

Live-fetched: all 13 projects (full audit agent), 8 department companies (parallel agent). Cross-checked against dossiers `1Harvard University Construction Intelligence Resea.md` + `2Harvard Researsch.md`.

**Filled — Website property on 2 departments:**
- FAS House Renewal PMO `37990644-d524-811d-bf3b-df3091837c8e` → `https://oprp.fas.harvard.edu/capital-project-management` (source: dossier 1, seed URL list)
- Harvard Office of the EVP `37990644-d524-8159-b043-f9c1ea28270e` → `https://evp.harvard.edu` (source: dossier 1, `evp.harvard.edu/people` used as stakeholder source → root URL is the department's public site)

- **3a (relations):** All owner↔department↔project↔people↔GC edges intact. No missing edges found.
- **3b (body depth):** All 13 project bodies complete. 4 thin records (Barker, Steam Tunnel, ESL, Lewis) confirmed genuinely sourceless — no additional detail available in dossier. Department bodies adequate.
- **3c (addresses):** NASDEP, Steam Tunnel 29/30, Lewis Law Center street addresses remain blank — confirmed corridor/campus-area only in source. All other projects have `place:Adress` set. No change.
- **3d (memberships):** N/A — Owner entity, no memberships table.
- **3e (location tags):** All 13 projects have Location populated. No missing tags.

**Genuinely sourceless — confirmed (no change from prior passes):**
- All 13 projects: `Contrat Value in Million` blank on 10 of 13 (ERC $1,500M, NASDEP $50M, HMS Bertarelli $75M already set; rest NOT DISCLOSED in dossier)
- Barker Center / Steam Tunnel 29/30 / ESL SEAS Contractors — GC not publicly disclosed
- ESL SEAS Date start/end — not disclosed in source
- Lewis Law Center Date start/end — not disclosed in source
- NASDEP / Steam Tunnel 29/30 / Lewis Law Center / Pritzker Hall precise street addresses — sourced as corridor/campus area or estimated only
- Harvard Capital Projects `Website` — only source is an intranet URL (not public-facing)
- Harvard Real Estate `Website` — no public website URL in dossier
- All department `LinkedIn` — not in source

**False positives rejected:** None.

## Audit log — 2026-06-11 (pass 3 — notion-audit skill)
**0 fills — all records complete.**

Live-fetched: all 13 projects, 4 department companies, Harvard owner record, Harvard University Companies DB record, Tom O'Connor (P0) + Shallan Fitzgerald (P1). Cross-checked against dossier `2Harvard Researsch.md` (project JSON + GC JSON).

- **3a (relations):** All owner↔department↔project↔people↔GC edges intact. Harvard owner has 13 Projects, 16 Departments, 11 General Contractors, 26 Key Contacts — all verified.
- **3b (body depth):** All 13 project bodies complete with scope, GC, owner, dates, sourced URLs. Department About/Owns/Sources sections present. Tom O'Connor bio fully filled.
- **3c (addresses):** All projects with confirmed street addresses have `place:Adress` set. Genuinely sourceless cases (NASDEP no street, Steam Tunnel 29/30 no street, Lewis Law Center no precise street, Pritzker Hall address estimated not confirmed) remain blank — correct.
- **3d (memberships):** N/A — owner entity has no memberships table.
- **3e (location tags):** All 13 projects have `Location` populated. No missing tags.
- **Amy Finlayson (Pritzker PM, LOW CONFIDENCE):** dossier flags as possible Pritzker day-to-day PM but explicitly marks LOW CONFIDENCE. Not added to Notion — no reliable source URL.

**False positives rejected:** None. All prior fills verified correct in live records.

**Genuinely sourceless — confirmed (no change from prior passes):**
- Pritzker Hall precise street address
- NASDEP / Steam Tunnel 29/30 / Lewis Law Center street addresses
- Barker Center / Steam Tunnel 29/30 / ESL SEAS Contractors
- All department LinkedIn / Website fields

## Audit log — 2026-06-12 (pass 8 — notion-audit skill)
**0 fills — all records complete.**

Live-fetched: Harvard owner (Owners DB), all 14 project records, all 13 department company records (full set). Cross-checked against both Harvard dossiers (`1Harvard University Construction Intelligence Resea.md` + `2Harvard Researsch.md`).

- **3a (relations):** Harvard owner → 15 entries in Projects (14 unique + 1 duplicate `813f`), 16 depts, 11 GCs, 26 contacts. All intact. All project→Owner/Owning Department/Contractors edges correct for the 12 projects with known GCs.
- **3b (body depth):** All 14 project bodies complete with full sourced depth. All department bodies adequate. No thin bodies with more dossier detail available.
- **3c (addresses):** NASDEP/Steam Tunnel/Lewis Law Center/Pritzker Hall estimated-only remain blank — correct (genuinely sourceless). All other 10 projects have `place:Adress` set.
- **3d (memberships):** N/A — Owner entity, no memberships table.
- **3e (location tags):** All 14 projects have `Location` populated. No missing tags.

**No fills made — nothing fillable found after full dossier cross-check.**

**Open structural issues (require Zack action — no change):**
- Gund Hall `8159` + Lewis Law Center `8198` `Owning Department` wrongly point to Shawmut NE Region div
- Duplicate Gund Hall `813f` still present — Zack to delete in UI

**Genuinely sourceless — confirmed (no change from prior passes):**
- NASDEP/Steam Tunnel 29/30/Lewis Law Center/Pritzker Hall precise street addresses
- Barker Center/Steam Tunnel 29/30/ESL SEAS Contractors
- ESL SEAS/Lewis Law Center dates (start/end)
- 10 of 14 project contract values
- Harvard Capital Projects/Harvard Real Estate/HBS/SEAS/A.R.T. Website (no public URL in dossier)
- All department LinkedIn

---

## Audit log — 2026-06-12 (pass 7 — notion-audit skill)
**2 fills — department Website fields.**

Live-fetched: Harvard owner Owners DB record, all 16 department company records. Cross-checked against both Harvard dossiers.

**Filled — Website property on 2 departments:**
- Harvard Office for Sustainability `37990644-d524-818b-84d8-d88bb4c63aac` → `https://sustainable.harvard.edu` (source: dossier 1 + dossier 2 — `sustainable.harvard.edu/our-plan/how-we-build/` used as primary source URL throughout both dossiers)
- Harvard University Housing `37990644-d524-812a-b3dd-ea882c35077b` → `https://huhousing.harvard.edu` (source: dossier 1 — `huhousing.harvard.edu/our-properties/100-south-campus-drive` + `huhousing.harvard.edu/introducing-100-south-campus-drive`)

- **3a (relations):** Harvard owner → 15 entries in Projects (14 unique + 1 dup `813f`), 16 depts, 11 GCs, 26 contacts. All intact.
- **3b (body depth):** All 14 project bodies complete. Department bodies adequate.
- **3c (addresses):** NASDEP/Steam Tunnel/Lewis Law Center/Pritzker Hall estimated-only remain blank — correct.
- **3d (memberships):** N/A — Owner entity.
- **3e (location tags):** All 14 projects have Location populated. No missing tags.

**Genuinely sourceless — confirmed (no change):**
- Harvard Capital Projects Website — intranet URL only, not public-facing
- Harvard Real Estate Website — no public URL in dossier
- Harvard Business School Website — `hbs.edu` not in dossier source URLs
- Harvard SEAS Website — `seas.harvard.edu` not in dossier source URLs
- A.R.T. Website — no ART website URL in dossier sources
- All department LinkedIn
- NASDEP/Steam Tunnel 29/30/Lewis Law Center/Pritzker Hall precise street addresses
- Barker Center/Steam Tunnel 29/30/ESL SEAS Contractors
- ESL SEAS/Lewis Law Center dates (start/end)
- 10 of 14 project contract values

**Open structural issues (require Zack action — no change):**
- Gund Hall `8159` + Lewis Law Center `8198` `Owning Department` wrongly point to Shawmut NE Region div
- Duplicate Gund Hall `813f` still present — Zack to delete in UI

---

## Audit log — 2026-06-12 (pass 6 — notion-audit skill)
**0 fills — all records complete.**

Live-fetched: all 14 projects, Harvard owner Owners DB record, 5 department companies (FAS House Renewal PMO, EVP, Harvard Capital Projects, Harvard Real Estate, Harvard Engineering & Utilities). Cross-checked against both Harvard dossiers.

- **3a (relations):** Harvard owner → 15 entries in Projects (14 unique + 1 duplicate `813f` still present), 16 depts, 11 GCs, 26 contacts. All project→Owner/Owning Department/Contractors edges intact and correct for all 12 projects with known GCs.
- **3b (body depth):** All 14 project bodies complete. Department bodies adequate. No thin bodies with more dossier detail available.
- **3c (addresses):** NASDEP/Steam Tunnel/Lewis Law Center/Pritzker Hall estimated-only remain blank — correct.
- **3d (memberships):** N/A — Owner entity.
- **3e (location tags):** All 14 projects have Location populated. No missing tags.

**Open structural issues (require Zack action):**
- Gund Hall `8159` + Lewis Law Center `8198` `Owning Department` → both wrongly point to `37b90644-d524-811c` = "Shawmut — New England Region" (contractor division). No Harvard GSD or Harvard Law School company dept records exist in Notion. Fix: create those dept records → repoint Owning Department on both projects.
- Duplicate Gund Hall `37c90644-d524-813f` — still in Harvard owner's Projects list. Zack should delete in Notion UI.

**Genuinely sourceless — confirmed (no change):**
- NASDEP/Steam Tunnel 29/30/Lewis Law Center/Pritzker Hall precise street addresses
- Barker Center/Steam Tunnel 29/30/ESL SEAS Contractors
- ESL SEAS/Lewis Law Center dates (start/end)
- 10 of 14 project contract values
- Harvard Capital Projects/Harvard Real Estate Website (no public URL)
- All department LinkedIn

## Audit log — 2026-06-12 (pass 5 — notion-audit skill)
**2 fills — Gund Hall dates+address + duplicate record Owner link.**

Live-fetched: all 14 projects (Harvard owner shows 14 in Projects relation). Ground truth: both Harvard dossiers + `Shaw5.md` for Gund Hall.

**Filled:**
- Gund Hall `37c90644-d524-8159-a591-c390f06ce2e3` → `date:Date:start`=2024-05-01, `date:Date:end`=2025-01-31, `place:Adress`="48 Quincy Street, Cambridge, MA 02138" (42.3748, -71.1151). Source: https://www.gsd.harvard.edu/2025/02/five-lessons-from-the-gund-hall-renovation/
- Gund Hall duplicate `37c90644-d524-813f-98c8-efd5cad0f266` → `Owner`→Harvard + `Location`+=[Cambridge]. Source: same.

**14th project (new, from Shawmut dossier, not in original ledger):**
- Harvard GSD — George Gund Hall Renovation (Phase 1) `37c90644-d524-8159-a591-c390f06ce2e3` — Status=Done · Type=Historic Preservation · Contractor=Shawmut · GC=Shawmut NE Region

**⚠ Structural flags (require Zack action — cannot fix additively):**
- **Gund Hall `8159` + Lewis Law Center `37b90644-d524-8198` `Owning Department`** both wrongly point to `37b90644-d524-811c` = Shawmut — New England Region division (a Shawmut DIVISION, not a Harvard dept). No Harvard GSD or Harvard Law School company dept records exist in Notion. Fix: create those Harvard dept Company records, then repoint Owning Department on both projects.
- **Duplicate Gund Hall record `37c90644-d524-813f-98c8-efd5cad0f266`** — sparser copy (no Owner until this pass, no Owning Dept, Location=Massachusetts only). Canonical = `8159` which has full data. Zack should delete `813f` in Notion UI.

- **3a (relations):** Harvard owner→14 projects/16 depts/11 GCs/26 contacts. All intact. Gund Hall `813f` now Owner+Cambridge linked.
- **3b (body depth):** Gund Hall `8159` body carries full scope, GC, owner, award, sources.
- **3c (addresses):** Gund Hall `8159` `place:Adress` now filled. NASDEP, Steam Tunnel, Lewis Law Center, Pritzker Hall estimated-only remain blank.
- **3d (memberships):** N/A — Owner entity.
- **3e (location tags):** all 14 projects have Location populated. No missing tags.

**Genuinely sourceless — confirmed (no change):**
- NASDEP / Steam Tunnel 29/30 / Lewis Law Center / Pritzker Hall precise street addresses
- Barker Center / Steam Tunnel 29/30 / ESL SEAS Contractors
- ESL SEAS / Lewis Law Center dates
- 10 of 14 project contract values
- Harvard Capital Projects / Harvard Real Estate Website (no public URL)
- All dept LinkedIn
