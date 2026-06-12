# State · Records — The Middlesex Corporation

> **Holds:** the Middlesex dedup ledger — every record created/updated in the 2026-06-10 load, with Notion IDs, so the next session deduplicates before touching a Middlesex record.
> **Ground truth:** `Enlaye Notion/The Middlesex Corp/Middlesex.md` (single-line JSON dossier, run_date 2026-06-10; **truncated mid-`sources` array** but all company/divisions/locations/projects/events/memberships/software/owners present). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers (closest analog: [records-branch](records-branch.md) — Company-Map profile variant + existing company stub + interlink ADDs).

---

## Profile page (hub)
**"The Middlesex Corp"** — https://app.notion.com/p/37b90644d5248003baf7e3d038b7c037 (Companies research → Zack Folder). Older **Company Map** variant (like Branch). Template copy, name already trimmed. ⚠ separate **"Middlesex TEMPLATE"** `37b90644-d524-80b2-b047-ef5e4b3a576a` left untouched.

Page-local data sources on this page:
- **Divisions / Company Map** `collection://0ec90644-d524-8259-a809-07180185bf7c` (Division title · Adress **place** · relations Companies full database / People / Projects — full interlink native)
- **Events** `collection://3f590644-d524-8236-8e6d-07e7d65cb2d4` (Event name · Date · Location tags [only TX/CT/AZ-area options — no FL/MA] · Place · Companies full database rel)
- **Locations** `collection://eb190644-d524-8319-a007-87d439438dcf` (Location · Adress **TEXT** — bare, **+added** Companies + Division relations)
- **Memberships** `collection://83490644-d524-8240-bd91-87c2344a19d1` (Name only — bare, **+added** Companies relation)
- **Sources** `collection://0b590644-d524-8238-a139-07f124fc04b1` ("What the source is about" · userDefined:URL)
- Linkedin Post `collection://f3790644-d524-82fd-9aa9-87ca3b43eeb6` (unused)
- Projects Underway = shared Construction Projects (linked view `10e90644…`, `__TEMPLATE__` filter — manual UI fix)
- Existing Software = shared Companies Software (linked view `e6490644…`, `__TEMPLATE__` filter — manual UI fix)

## Company record (EXISTING — extend, do not recreate)
**"The Middlesex Corporation"** `1ce90644-d524-809e-ab40-e6e6c0a21c76` in Companies full database. Pre-load: BW Category=[Builder] · Country=[Massachusetts, USA] · Size=**Local** · LinkedIn + Website set · People(4 existing) · Strategy→`24e90644…b598` · Description + body **empty**. Placeholder grey icon.
- ⚠ **Distinct from "The Middlesex Corporation"** `24e90644-d524-8090-b154-d6aa6301b598` — a row in the **Strategy** CRM DB (`collection://22590644-…`) under Business Development → Coordinated Attacks. NOT a Companies-DB duplicate. Left untouched. Holds a leadership table (Robert W. Pereira founder/CEO; Robert Pereira II Pres/COO; Dave Socci SVP; Joshua Wernig SVP/CLO; Tom Donaruma HR Dir — all w/ LinkedIns) — useful people source but NOT in dossier, so not loaded as People records.
- **Size=Local kept** vs dossier (Regional, $566.7M, ENR #222, ~850 emp). Conflict flagged, not overwritten.

## Existing people (link only — do NOT recreate; already Company→`1ce9…21c76`)
| Person | ID | Function | Notes |
|---|---|---|---|
| Michael Shea | 1d390644-d524-809d-9f47-e6a6aa9aaea0 | Project Manager (mshea@) | CT — not in dossier |
| Patrick Kennally | 1d390644-d524-8047-b55a-c90aa13498ad | Senior Project Manager - Rail (pkennally@) | MA — not in dossier |
| Tim Toth | 2b690644-d524-80c7-b2a9-dfb15a7cc6f7 | Risk Manager (ttoth@) | not in dossier |
| Assem Sherif | 2b690644-d524-801b-b776-c75ddb13ec06 | VP Construction Innovation / Project Controls (asherif@) | not in dossier |

## Existing JV projects (LINK Middlesex as Contractor — do NOT duplicate; created by Cianbro/A-Z load)
| Dossier project | Existing page | ID | Note |
|---|---|---|---|
| P-381 Multi-Mission Dry Dock #1 | PNSY Dry Dock 1 Two-Bay Addition | 37b90644-d524-81a7-9e03-dbe1919cbb9b | $1.7B; 381 Constructors JV (TIC/Kiewit+Cianbro+Middlesex) |
| Walk Bridge Replacement | Norwalk River "WALK" Bridge Replacement | 37b90644-d524-8123-99b5-ffedb5fb4c91 | $935M (Cianbro framing) vs dossier $1.5B program; CMJV |
| Walk Bridge Phase 2 (TIME-2) | WALK Bridge TIME-2 (4 Bridges, East Norwalk) | 37b90644-d524-81ab-93f4-fbb706eaee3a | CMJV |

## Divisions (4 — Company Map DB `0ec90644`) ✅ created
| Division | ID | Leader | People | Projects |
|---|---|---|---|---|
| Northeast Region | 37b90644-d524-8173-ae73-f68910372448 | Seth Whiteman | Whiteman, Hebert | 14 |
| Southeast Region | 37b90644-d524-81ee-b0fd-c00c8620111a | Kevin Bennett | Bennett | 7 |
| Middlesex Paving LLC | 37b90644-d524-81c5-943f-c2268974bc10 | Michael Iapaluccio | Iapaluccio | — |
| Mass Ready Mix | 37b90644-d524-8120-8d99-c72b002711ab | — (no addr/coords; no place set) | — | — |
All carry Companies relation → company. NE/SE/Paving carry Adress place; Mass Ready Mix addr in body only.

## People (4 sourced leaders — People DB) ✅ created (all Company→`1ce9…`)
| Person | ID | Role | Division |
|---|---|---|---|
| Seth Whiteman | 37b90644-d524-8178-8d1f-c39bcef67bca | VP Operations, Northeast Region | NE Region |
| Kevin Bennett | 37b90644-d524-81de-9574-f7d3fbb585b7 | VP Operations, Southeast Region | SE Region |
| Michael Iapaluccio | 37b90644-d524-8105-a633-c6f38feb6fb5 | SVP of Paving (LinkedIn set) | Paving |
| Jonathan Hebert | 37b90644-d524-818e-9800-c12330d16973 | Director, Survey & Construction Technology | NE Region |

## Projects (18 new + 3 existing-linked = 21 — Construction Projects DB) ✅ all carry Contractors→Middlesex
**Existing JV (Middlesex added as 2nd contractor alongside Cianbro):** PNSY Dry Dock `…1919cbb9b` · WALK `…ffedb5fb4c91` · TIME-2 `…b706eaee3a`.
**New NE (created):** South Coast Rail `…d83de1d6a0d3` · Green Line Ext (GLX) `…8862f91751d4d7b7` · I-495/Rte28 Andover `…a923f2618a3c2d2f` · West Haven I-95 `…bb0ef10e780927aa` · Rte17/Rte9 Middletown `…8a90eea9981557e7` · Brightman St Bridge `…b630de37484f725b` · Burns Bridge `…9755e13145e7315a` · I-495 Lowell Bundle `…bc89e4c52ebd9589` · MBTA On-Call Track `…942fd47e0469509d` · Niantic River Bridge `…a11ccc90a6707d11` · Needham Ductbank `…b336d1391a568094`.
**New SE (created):** Brightline Zone 2 `…9459ccb56dfba037` · Tampa Air Cargo `…ab89f8f83d4362db` · I-75 Overpass Rd `…9608fd018735037f` · Brightline Aventura Ped Bridge `…b7dccfb82dbf1a98` · GOAA Terminal B `…b1e3dd110354b968` · SunRail Ph2 South `…818fd406e4dd02c3` · East Selmon Slip Ramps `…9c11e902af9263f1`.
*Owning Department left empty (relates to Companies DB, not page-local divisions); division↔project via Company Map Projects relation. Each project Adress place + lat/lng set; Location multi-select state-level (cities Andover/Lowell/West Haven/Orlando/Tampa/Kittery absent from options → state used; Tampa Air Cargo & East Selmon owners = Hillsborough authorities, NOT created — captured in body).*

## Owners/clients (9 — Owners DB `37990644`) ✅ created (each → General Contractors=Middlesex + Projects; Owners DB was near-empty pre-load)
MassDOT `…f73614c715fe` (4 proj) · CTDOT `…bcc2d2b3501af02a` (4) · MBTA `…824df51af204d89c` (3) · NAVFAC `…8696ce3142972bdd` (1) · FDOT `…89bef0d9bb0ca265` (2) · Brightline Trains LLC `…aafed346b43e6d95` (2) · GOAA `…8ed4de343553e28b` (2) · Eversource `…9355efe10408e0d4` (1) · Amtrak `…bd74c37f098fd206` (1). FL owners Location=[Other,USA] (no FL option in Owners DB).

## Other tables ✅ created
- **Events (4):** FTBA Annual Conference · DBIA-FL Design-Build Awards · CCIA Safety Recognition Awards (Location tags=[Connecticut]) · Middlesex Annual Charity Golf. All → company. No Place set (dossier gave no venue coords; Events Location tags lack FL/MA options).
- **Memberships (4):** CCIA · FTBA · DBIA-FL · ABC (25 consecutive STEP). All → company (**+added Companies relation col**).
- **Software (3 rows, shared Companies Software DB):** Trimble Stratus (Propeller)[Trimble] · Trimble GPS/Robotic TS/SCS900[Trimble] · Procore[Procore]. All → company, Location=[United States].
- **Locations (4):** Littleton MA HQ (→NE) · Meriden CT (→NE) · Orlando FL SE-HQ (→SE) · Tampa FL (→SE). All → company + division (**+added Companies + Division relation cols**); Adress text filled (table Adress is text, not place).
- **Sources (11):** key dossier sources added (overview/history, ENR Top 400, ENR $1.7B Navy, WALK, GLX, WBUR South Coast Rail, Propeller, Procore, CTDOT West Haven, Awards, Leadership).

## Audit — 2026-06-10 (post-load pass)
**Filled (1):** Kevin Bennett (People DB `37b90644-d524-81de-9574-f7d3fbb585b7`) → `Location` added `Florida` (was USA only; SE Region FL-based per dossier/RocketReach source). Confirmed write.
**DEFERRED — shared schema (Events Location tags):** `Florida` and `Massachusetts` options don't exist in the page-local Events DB multi-select (`collection://3f590644`). Per anti-clobber rules, adding new shared multi-select options is blocked. Affects: FTBA Annual Conference (FL), DBIA-FL Awards (FL), Charity Golf (MA) — all lack Location tags.
**DEFERRED — structural (People→Division):** People DB `Division` relation points to global Divisions DB (`collection://37690644-d524-8088-abd7-000b818a9b6b`) which holds KBE divisions only. Middlesex divisions live in the page-local Company Map (`collection://0ec90644`). Seth Whiteman, Kevin Bennett, Michael Iapaluccio, Jonathan Hebert have no `Division` set in People DB — structural mismatch, not a data gap.
**Genuinely sourceless (unchanged):** People LinkedIn (Seth Whiteman, Kevin Bennett, Jonathan Hebert — not in dossier) · People email/phone · FTBA event date (annual recurring, no specific date) · Events Place/venue coords · Mass Ready Mix address · Paving LLC Projects relation (paving-only projects not in Construction Projects DB) · division revenue/headcount/project counts · most project parcel/APN/FEMA/seismic.

## Left empty (no sourced value in dossier)
Division-level revenue/headcount/active-project counts · most project parcel/APN/permits/FEMA/seismic · exact license numbers · bond/surety · several project contract values (Brightline Zone 2, Tampa Air Cargo, I-75 Overpass, Niantic, SunRail, Needham, East Selmon — null in dossier) · Mass Ready Mix leader/address · people email/phone (dossier didn't give for the 4 leaders).

## Conflicts (kept existing, flagged)
- Company **Size=Local** (existing) vs dossier **Regional** — kept Local.
- Walk Bridge **$935M** (existing Cianbro page) vs dossier **$1.5B program** — kept existing; dossier value noted in brief.

## Interlink graph (verify by re-fetch)
Company ↔ People (4 new + 4 existing) · Company ↔ Construction Projects (21) · Division→Company (4) · Division→People + Division→Projects · Project→Contractors (Middlesex on all 21) · Location→Company + Division · Event→Company · Membership→Company · Software→Company.

## Manual UI steps outstanding  [TBD]
1. Projects Underway view → clear `__TEMPLATE__` filter, set Contractors = Middlesex.
2. Existing Software view → clear `__TEMPLATE__` filter.

---

## 2nd pass — 2026-06-10 (richer in-context dossier; additive)
**Source note:** a richer dossier appeared in-chat (NOT saved to disk; partially truncated) carrying an exec roster + extra software not in the registered disk file (which was already fully loaded). Zack chose **load new items additively**. Disk top-line ($566.7M/ENR #222, 2024 rev/2025 list) kept; context figures ($609.9M/#203) are a **different reporting year** (2023 rev/2024 list), not a true conflict — not overwritten.

**10 corporate execs created (People DB; Company→`1ce9…21c76` + NE Region division People):**
| Person | ID | Role | LinkedIn |
|---|---|---|---|
| Robert W. Pereira | 37b90644-d524-819f-a234-c2b4b706cb55 | Chairman & CEO (Founder) | — (leadership page) |
| Robert Pereira II | 37b90644-d524-8132-8939-f66824ad2938 | President & COO | ✓ |
| Peter Martinkus | 37b90644-d524-81e4-9d8b-eebff9e5661f | SVP Finance / CFO | ✓ |
| Joshua S. Wernig | 37b90644-d524-81ca-8561-ed2c4f366435 | SVP, CLO & GM | ✓ |
| Neil Mulrooney, DBIA | 37b90644-d524-810b-acd0-e637184040f6 | SVP of Construction | ✓ |
| Dave Socci | 37b90644-d524-8137-a5b6-cbc7c65ad743 | Senior VP | — (award page) |
| Jake Lewon | 37b90644-d524-815a-bd89-d899fe86ef07 | VP of Construction | ✓ |
| Jim Reardon | 37b90644-d524-8175-a49c-faace8a4bc33 | VP, Alternative Delivery | — (award page) |
| Tom Donaruma | 37b90644-d524-8115-bb1f-e68c466d0653 | Director, Human Resources | ✓ |
| Paul West, MBA | 37b90644-d524-817b-8ee9-cadb567a3090 | Director of Enterprise Applications (tech buyer) | ✓ |
All corporate → homed to **Northeast Region** (Littleton HQ) division per existing precedent (Hebert). Company People now **18**; NE Region People now **12**. Dedup: none pre-existed in People DB (Strategy-CRM names were never People records; "Pereira" search hits = unrelated VINCI/Portugal people).

**Middlesex Asphalt LLC** division row created — `37b90644-d524-817a-ae03-f3e437e79f35` (Company Map; Companies rel → company). Was the one named member-company missing as a division (Paving + Mass Ready Mix already existed). No leader/address sourced.

**4 software signals created (Companies Software `37690644…804f`; Company-linked; Location=US):** Bluebeam Revu `…29a6c9f1d96aadaccc` [Bluebeam] · HCSS HeavyJob `…3c8cd3db220d24b430` [**no vendor tag — "HCSS" not in multi-select; avoided rewriting option set; named in title/body**] · Trimble Viewpoint Vista `…3484f7d535282fc5e9` [Trimble] · Primavera P6 `…81a0b5aac3984503fd08` [Primavera P6]. All from one Project Engineer job req (jobs.ourcareerpages.com/job/990386). Companies Software now **7**.

**Company body** Snapshot extended (additive): added "Named in job reqs" tool line + corporate-leadership line. Description/revenue/ENR/Size untouched.

**Not loaded (scope):** safety certs (ABC STEP Diamond/Gold 25+ yrs already on ABC membership; AQC 2025 available to add to ABC row if wanted) · enr_rank_history · richer federal FPDS PIID `N4008521C0077` (PNSY already captured). Bennett/Iapaluccio (SE/Paving leaders) were from the disk file, already loaded — not in this exec roster.

---

## Audit — 2026-06-11 (automated hourly cycle)
**Result: NO WRITES NEEDED. Record is complete against all sourced dossier data.**

**Checks performed (all PASS):**
- **3a Interconnection:** Company→People(18)✓ · Company→Projects(21)✓ · Company→Owners(9)✓ · Divisions(5)→Company✓ · NE Region→People(12)+Projects(14)✓ · SE Region→People(1)+Projects(7)✓ · Paving→People(1)✓ · Asphalt/MassReady→Company only (no sourced people/projects) · Locations(4)→Company+Division✓ · Events(4)→Company✓ · Memberships(4)→Company✓ · Software(7)→Company✓
- **3b Description depth:** All division bodies contain focus/leader/footprint/founded/notable-projects per dossier. Company Snapshot complete. Project bodies contain what-it-is/scope/owner/delivery/JV/timeline per available source data.
- **3c Address/location:** Company Address place set (1 Spectacle Pond Rd, Littleton MA) ✓ · NE/SE/Paving division Adress place set ✓ · Mass Ready Mix + Asphalt LLC address = genuinely sourceless (dossier: "exact address not public") · All 4 Location rows have text Adress filled ✓ · Project Adress place set on sampled records (South Coast Rail, PNSY) ✓
- **3d Memberships:** All 4 sourced memberships present — CCIA ✓ · ABC ✓ · DBIA-FL ✓ · FTBA ✓ — each with company relation and source URL in body.
- **3e Location tags:** Events all tagged — FTBA=Florida ✓ · DBIA-FL=Florida ✓ · CCIA Awards=Connecticut ✓ · Golf=Massachusetts ✓. (Florida + Massachusetts options were added in prior session; confirmed present in schema.)

**Genuinely sourceless (unchanged from prior session):** People LinkedIn (Whiteman, Bennett, Hebert) · People email/phone · FTBA event specific date · Events Place/venue coords · Mass Ready Mix address · Paving LLC Projects relation · division revenue/headcount · most project APN/bond/FEMA/seismic · several project contract values (Brightline Zone 2, Tampa Air Cargo, I-75 Overpass, Niantic, SunRail, Needham, East Selmon).

**Structural deferred (unchanged):** People→Division relation points to global KBE-only Divisions DB — Middlesex page-local Company Map divisions can't link there.

---

## Audit — 2026-06-11 (manual full audit pass)
**Result: 6 fields filled across 2 records; 5 icons fixed.**

**Filled (verified post-write):**
- **PNSY Dry Dock** `37b90644…cbb9b` — `Location` corrected New Hampshire→**Maine** (Kittery ME is in Maine, not NH) · `userDefined:URL` set → https://middlesexco.com/projects/p-381-multi-mission-dry-dock-1/ · `date:Date:start` = 2021-08-13 · `date:Date:end` = 2028-12-31 · body location line updated to "Kittery, ME (Portsmouth Naval Shipyard)". All sourced: https://middlesexco.com/projects/p-381-multi-mission-dry-dock-1/
- **People icons** (placeholder `/icons/user_gray` → emoji): Seth Whiteman 🧭 · Kevin Bennett 🌴 · Michael Iapaluccio 🛣️ · Jonathan Hebert 📡. Confirmed live on re-fetch.

**False positives rejected:**
- Brightman Street Bridge JV partners — dossier `joint_venture_partners:[]` (empty); brief says "largest JV" but no partner named. Sourceless.
- I-75 Overpass contract value/dates — all `null` in dossier. Sourceless.
- Brightline Zone 2 contract value — `null` in dossier. Sourceless.
- Events Place (4 events) — no venue coordinates in dossier. Sourceless.
- FTBA Annual Conference date — no specific date in dossier. Sourceless.
- LinkedIn (Whiteman, Bennett, Hebert, R.W. Pereira) — not in dossier. Sourceless.
- Function Qualification (4 field-ops people) — not in dossier. Sourceless.
- Asphalt LLC / Mass Ready Mix leader/address — not in dossier. Sourceless.

**3a Interconnection:** All confirmed clean (same as prior pass). No new missing edges found.
**3b Description depth:** Project bodies are appropriately thin where source data was thin (I-75 Overpass, Brightline Zone 2 — no contract value or dates sourced).
**3c Address/location:** PNSY location tag corrected to Maine ✓. All other project addresses confirmed set.
**3d Memberships:** All 4 still present and complete. No new memberships found in dossier.
**3e Location tags:** All 4 events tagged (Florida/Florida/Connecticut/Massachusetts). No change needed.

---

## Audit — 2026-06-11 (automated notion-audit skill pass)
**Result: 1 fill — company record icon updated; all other fields confirmed complete.**

**Filled (verified post-write):**
- **Company record** `1ce90644-d524-809e-ab40-e6e6c0a21c76` — icon upgraded from grey placeholder attachment → 🏗️ emoji (per CLAUDE.md icon rule).

**All checks PASS:**
- **3a Interconnection:** Company→People(18)✓ · Company→Projects(21)✓ · Company→Owners(9)✓ · Company→Software(7)✓ · Divisions(5)→Company✓ · NE Region→People(12)+Projects(14)✓ · SE Region→People(1)+Projects(7)✓ · Paving→People(1)+Adress place✓ · Events(4)→Company+Location tags✓ · Memberships(4)→Company✓
- **3b Description depth:** All division bodies confirmed full (focus/leader/footprint/founded/notable projects) · Company Snapshot complete · PNSY body complete with JV/scope/dates.
- **3c Addresses:** Company Adress place set ✓ · NE/SE/Paving division Adress place set ✓ · Mass Ready Mix + Asphalt LLC genuinely sourceless · 4 Location rows Adress text filled ✓ · Project Adress place confirmed set on sampled records ✓
- **3d Memberships:** All 4 present — CCIA ✓ · ABC ✓ · DBIA-FL ✓ · FTBA ✓ — each with company relation and source URL.
- **3e Location tags:** All 4 events tagged — FTBA=Florida ✓ · DBIA-FL=Florida ✓ · CCIA=Connecticut ✓ · Golf=Massachusetts ✓

**Genuinely sourceless (unchanged):** People LinkedIn (Whiteman, Bennett, Hebert, R.W. Pereira) · People email/phone · Event Place/venue coords · FTBA exact date · Mass Ready Mix/Asphalt LLC leader+address · division revenue/headcount · several project contract values (Brightline Zone 2, Tampa Air Cargo, I-75 Overpass, Niantic, SunRail, Needham, East Selmon — null in dossier) · project APN/bond/FEMA/seismic.
**Structural deferred (unchanged):** People→Division relation points to global KBE-only Divisions DB.

---

## Audit — 2026-06-11 (notion-audit skill pass #3 — manual)
**Result: NO WRITES (no fillable data gaps found). ⚠ 3 duplicate membership rows re-confirmed from prior pass — now escalated to open-tasks for Zack deletion.**

Checks performed — all PASS:
- **3a Interconnection:** Company→People(18)✓ · Company→Projects(21)✓ · Company→Owners(9)✓ · Company→Software(7)✓ · Divisions(5)→Company✓ · NE Region→People(12)+Projects(14)✓ · SE Region→People(1)+Projects(7)✓ · Paving→People(1)+Adress place✓ · Events(4)→Company+Location tags✓ · Memberships→Company✓ · Location rows(4)→Company+Division✓
- **3b Description depth:** All division bodies full ✓ · Company Snapshot complete ✓ · Project bodies (South Coast Rail, NE Region division) verified full ✓
- **3c Addresses:** Company place ✓ · NE/SE/Paving division Adress place ✓ · 4 Location rows Adress text ✓ · Mass Ready Mix/Asphalt LLC = genuinely sourceless
- **3d Memberships:** All 4 sourced memberships present (CCIA `37b…1f4e`, ABC `37b…9358`, DBIA-FL `37b…5678`, FTBA `37b…7ced`) ✓ · ⚠ CCIA/DBIA-FL/FTBA each have a duplicate `37c90644` row (created 06-11 09:15 by automated pass) → logged to open-tasks for Zack to delete.
- **3e Location tags:** FTBA=Florida ✓ · DBIA-FL=Florida ✓ · CCIA=Connecticut ✓ · Golf=Massachusetts ✓

**No writes made — record is complete against all sourced dossier data. Dossier has 28 projects total; 21 loaded (7 are older repeat/on-call items not separately recorded); dossier counts confirmed via parse.**

---

## Audit — 2026-06-11 (notion-audit skill pass #4 — manual)
**Result: 1 fill — Meriden CT location body phone number added.**

**Filled (verified post-write):**
- **Meriden, CT — Regional Office** `37b90644-d524-8199-b5a2-e760ce3c2d6b` — body updated to add "Phone (978) 742-4400" (sourced from https://middlesexco.com/contact/; was present in Littleton HQ and Orlando/Tampa bodies but missing from Meriden CT).

**All checks PASS:**
- **3a Interconnection:** Company→People(18)✓ · Company→Projects(21)✓ · Company→Owners(9)✓ · Company→Software(7)✓ · Divisions(5)→Company✓ · NE Region→People(12)+Projects(14)✓ · SE Region→People(1)+Projects(7)✓ · Paving→People(1)✓ · Events(4)→Company+Location tags✓ · Memberships(4)→Company✓ · Location rows(4)→Company+Division✓
- **3b Description depth:** All division bodies full ✓ · Company Snapshot complete ✓ · Project bodies verified ✓
- **3c Addresses:** Company place ✓ · NE/SE/Paving division Adress place ✓ · 4 Location rows Adress text ✓ · Mass Ready Mix/Asphalt LLC = genuinely sourceless
- **3d Memberships:** All 4 sourced memberships present (CCIA ✓ · ABC ✓ · DBIA-FL ✓ · FTBA ✓) · ⚠ CCIA/DBIA-FL/FTBA each have a duplicate `37c90644` row → flagged for Zack deletion.
- **3e Location tags:** FTBA=Florida ✓ · DBIA-FL=Florida ✓ · CCIA=Connecticut ✓ · Golf=Massachusetts ✓

**Genuinely sourceless (unchanged):** People LinkedIn (Whiteman, Bennett, Hebert, R.W. Pereira) · People email/phone · Event Place/venue coords · FTBA exact date · Mass Ready Mix/Asphalt LLC leader+address · division revenue/headcount · several project contract values (Brightline Zone 2, Tampa Air Cargo, I-75 Overpass, Niantic, SunRail, Needham, East Selmon — null in dossier) · project APN/bond/FEMA/seismic.
**Structural deferred (unchanged):** People→Division relation points to global KBE-only Divisions DB.

---

## Audit — 2026-06-12 (notion-audit skill pass — Middlesex TEMPLATE page)
**Target:** Middlesex TEMPLATE page `37b90644-d524-80b2-b047-ef5e4b3a576a` (Companies research, distinct from "The Middlesex Corp" operational page).

**Result: 3 rows added to TEMPLATE Locations table; all other checks PASS.**

**Filled:**
- **TEMPLATE Locations DB** `collection://71c90644-d524-8344-a307-870ecc7d5238` — 3 missing rows added (body listed 7 locations, table had only 4):
  - 🏗️ Mass Ready Mix Plant – Littleton, MA `37d90644-d524-813e-9de1-f4c2b03fd270` · Adress=1 Spectacle Pond Road, Littleton, MA 01460 · [src](https://middlesexco.com/what-we-do/materials/)
  - 🏭 Orlando Asphalt Plant & Rail Terminal `37d90644-d524-81a0-b6a2-df3f6e7a4a2f` · Adress=10801 Cosmonaut Boulevard, Orlando, FL 32824 · [src](https://middlesexco.com/what-we-do/materials/)
  - ⛰️ Sparta Quarry – Sparta, GA `37d90644-d524-818d-af10-cae59ebcf313` · Adress=Sparta, GA 31087 · [src](https://middlesexco.com/what-we-do/materials/aggregates/)

**TEMPLATE page structure note:** TEMPLATE uses its own local collections (separate from "The Middlesex Corp" operational page). TEMPLATE Divisions view filters on "TEMPLATE" row only — by design (template placeholder). TEMPLATE Events and Software views show real operational data via filtered views. TEMPLATE Locations now has 7 rows matching the body count.

**All checks PASS:**
- **3a Interconnection:** TEMPLATE Locations→Companies relation not present in schema (TEMPLATE DB schema is simpler: Location + Adress text only — no Company/Division relations). This is a schema difference from the operational locations DB. Pre-authorized to add column if needed but schema is consistently minimal across all 4 original rows — left as-is.
- **3b Description depth:** TEMPLATE page body is fully sourced with attack plan, software signals, people summaries, memberships ✓
- **3c Addresses:** TEMPLATE Location rows use text `Adress` (not place type) — 7 rows now all have addresses ✓
- **3d Memberships:** Memberships section is body-only on TEMPLATE page (no inline DB here); 5 memberships listed — CCIA, FTBA, DBIA-FL, ABC, NSC ✓
- **3e Location tags:** TEMPLATE Events DB has no rows (view filter = TEMPLATE placeholder only); real events live on "The Middlesex Corp" page ✓

**Genuinely sourceless (TEMPLATE-specific):** TEMPLATE Divisions view shows no real rows by design (filtered to "TEMPLATE" placeholder) · TEMPLATE Locations schema has no Company/Division relations (minimal schema). No venue coordinates available for CCIA/Golf events. No Asphalt LLC People/Projects relation data.

---

## Audit — 2026-06-12 (notion-audit skill pass — auto)
**Result: NO WRITES (no fillable gaps). Record substantially expanded by a prior session since last ledger audit. State delta reconciled below.**

**State delta (new records since 06-11 pass #4 — added by prior sessions):**
- **Divisions (6 now, was 5):** Corridor Mining `37d90644-d524-81a9-8ea8-dae779ede653` (Sparta GA quarry affiliate, place set, Companies rel ✓)
- **Events (6, was 4):** FTBA 2025 Construction Symposium `37d90644…e488edbae6bf` (Date 2025-02-11, Place=Orlando, Location=Florida, Companies ✓) · DBIA-FL 19th Annual Florida Design-Build Conference `37d90644…f41dc750e401` (Date 2025-10-15, Place=Ponte Vedra Beach FL, Location=Florida, Companies ✓)
- **Locations (7, was 4):** Mass Ready Mix Plant–Littleton MA `37d90644…f1cff9156c07` (Adress=Littleton MA 01460, Companies ✓, Division=Mass Ready Mix ✓) · Orlando Asphalt Plant & Rail Terminal `37d90644…d2c4e1af9c25` (Adress=10801 Cosmonaut Blvd Orlando FL 32824, Companies ✓, Division=Middlesex Asphalt LLC ✓) · Sparta Quarry–Sparta GA `37d90644…dbf06b3724f4` (Adress=Sparta GA, Companies ✓, Division=Corridor Mining ✓)
- **Memberships (5, was 4):** NSC — National Safety Council `37d90644…d1a0c23eb6cb` (Companies ✓, source=middlesexco.com/middlesex-receives-nsc-perfect-record-award/)
- **Projects (22, was 21):** PFC Ralph T. Basiliere Bridge Replacement `37d90644…fdbbcc0e2965` ($214.98M, MassDOT, Route 125 Haverhill MA, Aug 2025 D-B, Location=Massachusetts, Contractors=Middlesex ✓, linked to NE Region Projects ✓)
- **People (30, was 18):** 12 Apollo-CSV contacts `37c90644…` linked to Middlesex (Cost Managers, Schedule Engineers, field staff — all Company ✓, no Division — structural deferred)
- **Software (8, was 7):** 1 new row `37d90644-d524-8190-be14-d1554d33bc22` linked (unverified title — fetching skipped per rate limit; Companies ✓)
- ⚠ **Duplicate Orlando location** `37c90644-d524-8138-a94d-fe1e0e886ff1` "Orlando FL — Southeast Regional HQ" — blank body, same address as original `37b90644…81db` row. Flagged for Zack deletion.

**All checks PASS:**
- **3a Interconnection:** Company→People(30)✓ · Company→Projects(22)✓ · Company→Owners(9)✓ · Company→Software(8)✓ · Divisions(6)→Company✓ · NE Region→People(12)+Projects(15)✓ · SE Region→Projects(7)✓ · Events(6)→Company+Location tags✓ · Memberships(5)→Company✓ · Locations(7)→Company+Division✓
- **3b Description depth:** Corridor Mining division body full ✓ · Basiliere Bridge body full ✓ · all existing division/project bodies unchanged ✓
- **3c Addresses:** Company place ✓ · All 7 Location rows Adress text ✓ · Basiliere Bridge Adress place ✓ · NE/SE/Paving/Corridor Mining division Adress place ✓ · Mass Ready Mix/Asphalt LLC divisions = sourceless ✓
- **3d Memberships:** All 5 sourced memberships present (CCIA ✓ · ABC ✓ · DBIA-FL ✓ · FTBA ✓ · NSC ✓) · ⚠ CCIA/DBIA-FL/FTBA each retain prior duplicate `37c90644` rows → still awaiting Zack deletion.
- **3e Location tags:** FTBA Annual=Florida ✓ · DBIA-FL Awards=Florida ✓ · CCIA=Connecticut ✓ · Golf=Massachusetts ✓ · FTBA Symposium=Florida ✓ · DBIA-FL 19th Annual=Florida ✓

**Genuinely sourceless (unchanged):** People LinkedIn (Whiteman, Bennett, Hebert, R.W. Pereira) · People email/phone · Event Place/venue coords · FTBA exact date · Mass Ready Mix/Asphalt LLC division leader/address · division revenue/headcount · several project contract values (Brightline Zone 2, Tampa Air Cargo, I-75 Overpass, Niantic, SunRail, Needham, East Selmon — null in original dossier) · project APN/bond/FEMA/seismic.
**Structural deferred (unchanged):** 12 Apollo-CSV people have no Division (global Divisions DB ≠ page-local Company Map) · `37c90644` Orlando dup location · `37c90644` CCIA/DBIA-FL/FTBA dup memberships — all require Zack manual deletion.

---

## Audit — 2026-06-12 (notion-audit skill pass)
**Result: 4 body-text counter fills on hub page. All structural checks PASS.**

**Filled (verified post-write — hub page `37b90644d5248003baf7e3d038b7c037`):**
- "5 divisions" → **6 divisions** (Corridor Mining now present in live DB)
- "21 projects linked" → **24 projects linked** (Basiliere Bridge + SR-429 + OIA GMP 5S.2 added in prior session)
- "18 people linked" → **30 people linked** (12 Apollo-CSV contacts added in prior session)
- "7 software tools" → **8 software tools** (Virtual Shift Tickets / VST added in prior session)

**All checks PASS:**
- **3a Interconnection:** Company→People(30)✓ · Company→Projects(24)✓ · Company→Owners(12)✓ · Company→Software(8)✓ · Divisions(6)→Company✓ · NE Region→People(12)+Projects(15)✓ · SE Region→Projects(9)✓ · Paving→People(1)+Adress place✓ · Asphalt LLC→Adress place✓ · Corridor Mining→Adress place✓ · Events(6)→Company+Location tags✓ · Memberships(5)→Company✓ · Locations(7+1dup)→Company+Division✓
- **3b Description depth:** All 6 division bodies full ✓ · Company Snapshot complete ✓ · Sampled project bodies (SR-429, OIA GMP 5S.2, Basiliere) full ✓
- **3c Addresses:** Company place ✓ · NE/SE/Paving/Asphalt/Corridor Mining division Adress place ✓ · Mass Ready Mix Adress place ✓ · All 7 Location rows Adress text ✓ · Events with sourced venues have Place field set (FTBA Annual / DBIA 18th / FTBA Symposium / DBIA 19th ✓); CCIA + Golf genuinely sourceless
- **3d Memberships:** CCIA ✓ · ABC ✓ · DBIA-FL ✓ · FTBA ✓ · NSC ✓ (5/5) · ⚠ CCIA/DBIA-FL/FTBA `37c90644` duplicate rows still present — awaiting Zack deletion
- **3e Location tags:** All 6 events tagged — FTBA Annual=Florida ✓ · DBIA-FL 18th=Florida ✓ · CCIA=Connecticut ✓ · Golf=Massachusetts ✓ · FTBA Symposium=Florida ✓ · DBIA-FL 19th=Florida ✓

**State delta since last ledger pass (new records added by prior sessions — now registered):**
- Divisions: 6 total (was 5 in ledger) — Corridor Mining `37d90644…8ea8` ✓
- Projects: 24 total (was 22) — SR-429 Widening `37d90644…4a93adb7` + OIA GMP 5S.2 `37d90644…aa1019b0` (both SE Region; Contractors→Middlesex ✓)
- People: 30 total (was 18 in original ledger; 12 Apollo-CSV contacts added `37c90644…`)
- Software: 8 total (was 7) — Virtual Shift Tickets (VST) `37d90644…d33bc22` ✓
- Owners: 12 total (was 9) — 3 new owners added by prior sessions (FTE `…824ca4b` · CFCCA `…a5a5e9` · Hillsborough `…bb92f`)

**Genuinely sourceless (unchanged):** People LinkedIn (Whiteman, Bennett, Hebert, R.W. Pereira) · People email/phone · CCIA + Golf event Place/venue coords · FTBA Annual exact date · Mass Ready Mix/Asphalt LLC division leader · division revenue/headcount · project contract values (Brightline Zone 2, Tampa Air Cargo, I-75 Overpass, Niantic, SunRail, Needham, East Selmon) · project APN/bond/FEMA/seismic.
**Structural deferred:** People→Division relation → global KBE-only Divisions DB (structural impossibility) · dup Orlando location `37c90644…886ff1` (blank body) · dup CCIA/DBIA-FL/FTBA `37c90644` memberships — Zack deletion required.

---

## Audit — 2026-06-11 (notion-audit skill pass #2 — manual)
**Result: NO WRITES (no fillable data gaps found). ⚠ 3 duplicate membership rows detected — flagged, not deleted (additive-only policy).**

**All checks PASS:**
- **3a Interconnection:** Company→People(18)✓ · Company→Projects(21)✓ · Company→Owners(9)✓ · Company→Software(7)✓ · Divisions(5)→Company✓ · NE Region→People(12)+Projects(14)✓ · SE Region→People(1)+Projects(7)✓ · Paving→People(1)✓ · Events(4)→Company+Location tags✓ · Memberships→Company✓ · Location rows(4)→Company+Division✓
- **3b Description depth:** All division bodies full ✓ · Company Snapshot complete ✓ · Project bodies appropriate to available source data ✓
- **3c Addresses:** Company place ✓ · NE/SE/Paving division Adress place ✓ · 4 Location rows Adress text ✓ · Mass Ready Mix/Asphalt LLC = genuinely sourceless (no address in dossier)
- **3d Memberships:** All 4 sourced memberships present. ⚠ CCIA · DBIA-FL · FTBA each have DUPLICATE rows (created by automated pass on 2026-06-11 09:15). Originals: `37b90644…1f4e` / `…5678` / `…7ced`. Duplicates: `37c90644…b2a1` / `…d97b` / `…4612`. ABC has no duplicate. **Deletion is a destructive operation — flag for Zack to manually remove the `37c90644…` duplicates in Notion UI.**
- **3e Location tags:** All 4 events tagged — FTBA=Florida ✓ · DBIA-FL=Florida ✓ · CCIA=Connecticut ✓ · Golf=Massachusetts ✓

**Genuinely sourceless (unchanged):** People LinkedIn (Whiteman, Bennett, Hebert, R.W. Pereira) · People email/phone · Event Place/venue coords · FTBA exact date · Mass Ready Mix/Asphalt LLC leader+address · division revenue/headcount · several project contract values (Brightline Zone 2, Tampa Air Cargo, I-75 Overpass, Niantic, SunRail, Needham, East Selmon — null in dossier) · project APN/bond/FEMA/seismic.
**Structural deferred (unchanged):** People→Division relation points to global KBE-only Divisions DB.
