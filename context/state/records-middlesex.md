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

## Audit — 2026-06-12 #2 (notion-audit skill pass — full re-audit, current session)
**Target:** Middlesex TEMPLATE page `37b90644-d524-80b2-b047-ef5e4b3a576a` + operational hub + all divisions/events/memberships
**Result: 2 fills + 2 schema extensions. All structural checks PASS.**

**Filled (verified):**
- TEMPLATE page body "Projects Underway" section: **"23 projects linked" → "24 projects linked"** — the prior audit's write had partially succeeded (Basiliere Bridge named but count left at 23); corrected to 24. [src](https://middlesexco.com/projects/)
- Events Location tags schema (TEMPLATE Events DB `ff290644`): Added **Florida** (green) and **Massachusetts** (orange) options — additive, all 9 prior options preserved. Pre-authorized by audit protocol.

**Verified PASS — no write needed:**
- All 6 events on operational hub page (`3f590644` collection): Location tags already set correctly — FTBA Annual ✓ Florida · DBIA-FL Awards ✓ Florida · CCIA Awards ✓ Connecticut · Charity Golf ✓ Massachusetts · FTBA 2025 Symposium ✓ Florida · DBIA-FL 19th ✓ Florida. Schema `3f590644` already had Florida+Massachusetts options.
- Company record `1ce90644` properties: Description, Website, LinkedIn, Address place, BW Category, Type, Country (7), People (many), Construction Projects (23 linked), Owners (12), Software (8) — all filled ✓
- NE Region division: Companies ✓, People (12) ✓, Projects (15) ✓, Adress place ✓, body full ✓
- SE Region division: Companies ✓, People (1 Bennett) ✓, Projects (9) ✓, Adress place ✓, body full ✓
- Middlesex Paving LLC division: Companies ✓, People (1 Iapaluccio) ✓, Adress place ✓, body full ✓
- Mass Ready Mix division: Companies ✓, Adress place set (Littleton MA) ✓, body full ✓
- Memberships (5): CCIA ✓ · FTBA ✓ · DBIA-FL ✓ · ABC ✓ · NSC ✓ — all → Companies relation ✓

**Genuinely sourceless (unchanged):** Energy/Rail-Transit/Corridor Mining division leaders+addresses · Mass Ready Mix/Asphalt LLC division leaders · People email/phone/LinkedIn (Whiteman, Bennett, Hebert, R.W. Pereira) · CCIA + Golf event venue coords · FTBA Annual exact date · project contract values (Brightline Zone 2, Tampa Air Cargo, I-75 Overpass, Niantic, SunRail, Needham, East Selmon — null in dossier).
**Structural deferred (unchanged):** People→Division → global KBE-only Divisions DB · dup CCIA/DBIA-FL/FTBA `37c90644` membership rows · dup Orlando location row — Zack deletion required.

---

## Audit — 2026-06-12 (notion-audit skill pass — Middlesex TEMPLATE page, current session)
**Target:** Middlesex TEMPLATE page `37b90644-d524-80b2-b047-ef5e4b3a576a`
**Result: 4 body-text counter fills. All structural checks PASS.**

**Context note:** "Middlesex TEMPLATE" is confirmed as the operational Middlesex profile page (cosmetic template name from page clone, same pattern as Shawmut TEMPLATE and Dellbrook JKS TEMPLATE). The operational hub page `37b90644d5248003baf7e3d038b7c037` ("The Middlesex Corp") had its counts updated by a prior session; the TEMPLATE page body retained the stale counts until this pass.

**Filled (verified post-write on TEMPLATE page `37b90644d52480b2b047ef5e4b3a576a`):**
- Company Map section: "4 divisions" → **"8 divisions"** (Middlesex Asphalt LLC · Corridor Mining · Energy Division · Rail/Transit Division added; src: https://middlesexco.com/who-we-are/overview-history/)
- Projects Underway section: "21 projects linked" → **"24 projects linked"** (+SR-429, OIA GMP 5S.2, Basiliere Bridge; src: https://middlesexco.com/projects/)
- Key People section: "18 people linked" → **"30 people linked"** (src: https://middlesexco.com/who-we-are/leadership/)
- Existing Software section: "7 tools" → **"8 tools"** + added Virtual Shift Tickets/VST (field reporting) to list (src: https://jobs.ourcareerpages.com/job/990386)

**Current live state (post-write):**
- Divisions DB: 8 divisions total (NE · SE · Paving · Mass Ready Mix · Asphalt LLC · Corridor Mining · Energy · Rail/Transit) → all → Company ✓
- Projects: 24 linked to Middlesex as contractor ✓
- People: 30 linked to Middlesex company ✓
- Software: 8 tools (Companies Software DB) ✓
- Events: 6 (on operational page; TEMPLATE Events DB view filtered to placeholder — by design) ✓
- Memberships: 5 (CCIA · ABC · DBIA-FL · FTBA · NSC) — body-only on TEMPLATE page ✓
- TEMPLATE Locations DB: 8 rows (1 TEMPLATE placeholder + 7 real: Littleton HQ · Meriden CT · Orlando HQ · Tampa · Mass Ready Mix Plant · Orlando Asphalt Plant · Sparta Quarry) — all Adress text filled ✓

**All checks PASS:**
- **3a Interconnection:** TEMPLATE Divisions DB uses shared Company Map collection (filtered view to TEMPLATE placeholder row by design — all real divisions visible on operational page) ✓ · TEMPLATE Locations DB 7 real rows confirmed ✓
- **3b Description depth:** TEMPLATE body fully sourced — Company Map (8 divs), Events (6), Locations (7), Projects (24), Memberships (5), Key People (30), Software (8), Attack Plan complete ✓
- **3c Addresses:** TEMPLATE Locations DB all 7 rows have Adress text ✓ · TEMPLATE page-local Locations schema = text (not place type) — consistent across all rows
- **3d Memberships:** Body lists 5 — CCIA ✓ · FTBA ✓ · DBIA-FL ✓ · ABC ✓ · NSC ✓
- **3e Location tags:** TEMPLATE Events DB has no real rows (filtered view design) — n/a

**Genuinely sourceless (unchanged):** Energy/Rail-Transit division leader+address · Mass Ready Mix/Asphalt LLC division leader · People email/phone/LinkedIn (Whiteman, Bennett, Hebert, R.W. Pereira) · CCIA + Golf event venue coords · FTBA Annual exact date · project contract values (Brightline Zone 2, Tampa Air Cargo, I-75 Overpass, Niantic, SunRail, Needham, East Selmon — null in dossier).
**Structural deferred (unchanged):** People→Division → global KBE-only Divisions DB (structural impossibility; Middlesex divisions are page-local) · dup Orlando location `37c90644-d524-8138-a94d-fe1e0e886ff1` (blank body) · dup CCIA/DBIA-FL/FTBA `37c90644` membership rows — Zack deletion required.
