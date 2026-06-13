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

## Audit log — 2026-06-12
**Fill:**
- NASDEP Status `In progress` → `Done` — source: [Allston Development Update Oct 2025](https://construction.harvard.edu/2025/11/04/allston-development-update-october-2025/) confirms substantially complete / close-out.

**No fills (genuinely sourceless or already filled):**
- All 15 project `place:Adress` fields already populated (except NASDEP/Steam Tunnel 29/30 which have no street address in dossier — confirmed sourceless).
- All 26+ people `LinkedIn` fields: already set where sourced (Lisa Giovanetti, Sarah Henning, Tory Wolcott Green, Alyssa Hubbard, John Martell, David Armitage, Anne-Sophie Divenyi, Tom O'Connor). Remaining people (HALC leadership, HMS team, CSL team) have no public LinkedIn URLs in either dossier.
- Email fields already complete on CSL team (Edward LeFlore, Ann Davis, Nicole Clement, Holly Sutherland, Shane O'Halloran) and Purnima Kapur. No new emails found in dossier for remaining people.
- Pritzker Hall/Lewis Law Center date fields: start/end not in dossier for Lewis; Pritzker already set.
- 12 Palmer Street / Barker Center status: targeted for completion ~Apr–Jun 2026 per dossier, but actual completion not confirmed in source — Status left as "In progress."
- ART/Goel Center end date: body notes "expected 2027" for ART theater itself but property shows 2026-10-31 (for combined package with 100 SCD housing). Ambiguous; not updated.

**Flags (non-destructive, for Zack):**
- **Duplicate Gund Hall records:** `37c90644-d524-8159-a591-c390f06ce2e3` and `37c90644-d524-813f-98c8-efd5cad0f266` are both "George Gund Hall Renovation — Harvard GSD." First has Owning Department + more data; second is a thinner duplicate. Cannot delete per safety rules — Zack should manually archive/delete the second one.
- Gund Hall `Owning Department` on first record (`37c90644-d524-8159`) points to `37b90644-d524-811c` which is actually the "Shawmut — New England Region" Division record (not a Harvard dept) — this is by design, reflecting the project's origin in the Shawmut dossier.

**3a check:** All owner↔department↔project relation edges intact across all 15 projects and 26 people. No missing edges found.
**3b check:** All project bodies complete; no thin bodies where source has more detail.
**3d memberships:** N/A — no memberships table on Harvard Owner record.
**3e location tags:** All project `Location: ["Massachusetts"]` populated. ✓

## Audit log — 2026-06-13 (second pass)
**Fill:**
- Campus Steam Tunnel 29/30 `userDefined:URL` was blank → filled with `https://construction.harvard.edu/current-projects/allston-development/blackstone-steam-plant-storm-hardening-project/engineering-facilities/29-30-tunnel-project/` (sourced from dossier 1).

**No fills (genuinely sourceless or already filled):**
- All project `place:Adress` fields populated; Steam Tunnel 29/30 and NASDEP have no street address in either dossier (confirmed sourceless across two audit passes).
- Barker Center status: dossier says "scheduled to complete by June 2026" (not confirmed complete) — left as "In progress."
- 12 Palmer Street status: end date Apr 2026 passed but dossier does not confirm actual completion — left as "In progress."
- WJH Plaza status: end date Jun 30, 2026; dossier says "Spring/Summer 2026" — consistent; no confirmed completion.
- ART end date: dossier 2 aligns with 2026-10-31 for housing; ART theater body note says "expected 2027" — ambiguous, not touched (prior audit flag stands).
- Lewis International Law Center: no start/end dates or contract value in any dossier — confirmed sourceless.
- All department LinkedIn/Website fields: no data in either dossier.
- All people LinkedIn fields: no new URLs found beyond what was already filled.
- Pritzker Hall design architect (Grafton Architects) and PM (Amy Finlayson) from dossier 2 are both marked [LOW CONFIDENCE] — not filled per sourced-data-only rule.

**3a check:** All relation edges intact. HBS→Chase/McCulloch/Dillon, FAS→4 projects, HUPAD→2, Harvard Capital Projects→2, HMS→Bertarelli, SEAS→ESL, Harvard Engineering & Utilities→Tunnel 29/30+NASDEP, HALC→ERC+NASDEP. No missing edges.
**3b check:** All project bodies complete and accurate per dossier.
**3d memberships:** N/A.
**3e location tags:** All projects tagged `["Massachusetts"]`. ✓

## Audit log — 2026-06-13 (third pass / notion-audit skill run)
**Fill:**
- Smoot Construction `LinkedIn` was blank → filled with `https://www.linkedin.com/company/smootbuilds` (sourced from dossier 1 sources_consulted list).

**No fills (genuinely sourceless or already complete):**
- All 12 Harvard project records fully populated: properties, addresses, dates, GC relations, department relations, people relations, contract values, URLs, body descriptions — all complete across prior audit passes.
- Smoot `Website` — no URL in dossier.
- Harvard University `LinkedIn` — still no URL in dossier.
- All department LinkedIn/Website fields — not in either dossier.
- ESL/Steam Tunnel start/end dates — source says null/not disclosed.
- ART `Contrat Value in Million` — $122M from dossier 2 is explicitly LOW CONFIDENCE/third-party; not filled per sourced-data rule.

**3a check:** All relation edges intact — all 12 projects linked to Owner (Harvard), Owning Department(s), Contractors, and People where sourced. No missing edges found.
**3b check:** All project and department bodies complete; no thin bodies where source has more detail.
**3d memberships:** N/A — no memberships table on Harvard Owner record.
**3e location tags:** All projects tagged `["Massachusetts"]`. ✓

## Audit log — 2026-06-13 (fourth pass / notion-audit skill run)
**Fill:**
- IC&E `Description` property was "Innovative Contracting & Engineering (IC&E)" (just the name) → updated to "IC&E — heavy-civil/utilities CM-GC; Harvard NASDEP (North Allston Storm Drain Extension, ~$50M) as CM/GC support to Engineering & Utilities." Source: dossier 1 (iceteams.com/harvard-nasdep).

**No fills (genuinely sourceless or already complete):**
- All 15 project records fully verified: all properties, addresses, dates, GC relations, Owning Department relations, People relations, contract values, URLs, body descriptions complete.
- J&J Contractors — LinkedIn/Website/revenue/employees null in both dossiers; confirmed sourceless.
- Smoot `Website` — still no URL in dossier.
- Harvard University `LinkedIn` — no URL in either dossier.
- All department LinkedIn/Website fields — not in either dossier.
- ART `Contrat Value in Million` — $122M LOW CONFIDENCE per dossier 2; not filled.
- Lewis International Law Center — no start/end dates, no street address; confirmed sourceless across all passes.
- Gund Hall duplicate (`37c90644-d524-813f-98c8-efd5cad0f266`) still present; cannot delete per safety rules — flag for Zack UI cleanup.

**3a check:** All owner↔department↔project↔people relation edges intact. No missing edges.
**3b check:** All project and department bodies complete; IC&E description improved.
**3d memberships:** N/A — no memberships table on Harvard Owner record.
**3e location tags:** All 15 projects tagged `["Massachusetts"]`. ✓
