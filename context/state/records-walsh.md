# State · Records — The Walsh Group (walshgroup.com)

> **Holds:** the Walsh Group dedup ledger — every record created/updated in the 2026-06-12 load, with Notion IDs, so the next session deduplicates before touching a Walsh record.
> **Ground truth:** `Enlaye Notion/Walsh Corp/walsh_group_dossier_v2.json` (+ `WALSH_LOAD_HANDOFF.md`). Dossier index: [research-files](research-files.md).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: the other `records-*` ledgers (closest analog: [records-cianbro](records-cianbro.md) / [records-bechtel](records-bechtel.md) — existing company record extended + subsidiary divisions + interlink).

---

## ⚠️ Identity (read first — a prior session broke this)
- **The dossier loads onto the EXISTING company record `17b90644-d524-809d-9810-defa38a2cbc9` "The Walsh Group"** (Companies DB). Confirmed by Zack 2026-06-12 (screenshot): this record IS walshgroup.com — ~423 people on @walshgroup.com, LinkedIn=walsh-construction, Archer Western + Walsh Canada nested as Subsidiaries, Walsh VINCI = the JV. **No new company record was created.**
- The record's `Website ` field = **walshbrothers.com** (contamination from a prior aborted load). **Left as-is** (hard rule: no overwrite of filled fields; Zack did not approve the fix). Conflict flagged — fix manually if desired. The dossier's sourced value is https://www.walshgroup.com/.
- **walshgroup.com ≠ walshbrothers.com.** "Walsh Brothers" `1cf90644-d524-8004-b6a9-cf74718cd8ce` (Boston) is a DIFFERENT company — never load Walsh Group data onto it.
- Pending cleanup (Zack handling manually): page **"🗑️ [DELETE ME — mistaken Walsh load]"** `37d90644-d524-8155-a58f-fc0c05ca118c` + child orphan people. Do NOT dedup against its children.
- Strategy/BD page **"Walsh Group" `22a90644-d524-80de-9a20-fb2da7c13d5e`** (Strategy DB, linked via company's Strategy rel) — left untouched.

## Company record (EXISTING — extended, not recreated)
**"The Walsh Group"** `17b90644-d524-809d-9810-defa38a2cbc9` (Companies DB). Custom Walsh icon.
- **Filled (2026-06-12):** Description (was empty) · Company Snapshot body (founded/ownership/scale/HQ/divisions/leadership/flagship projects/memberships/Procore + Sources) · `Construction Projects` relation = 54 (re-passed full list, one-way) · `Owners` relation auto-grew to 45 (via owner `General Contractors`) · `Companies Software ` = Procore row · `Subsidiaries` auto-grew to 4 (Archer Western, Walsh Canada, Walsh Construction, Walsh Federal) · `People` auto-grew (~423 → ~431 with 7 new leaders).
- **NOT touched (preexisting, correct/filled):** `Website `=walshbrothers.com (CONTAMINATION, left per no-overwrite — flagged) · LinkedIn=walsh-construction · Size=Mutlinational · Country=[USA,Illinois] · Type=Company · BW=Builder · Strategy=`22a90644` · Address place (lat/lng 0/0).

## Divisions (Companies records, linked via Parent Company → 17b90644)
**Existing (reused, enriched additively — bodies host inline Tasks/Tickets DBs → never replace_content):**
- Archer Western `33a90644-d524-80f7-ac8b-db7a94398846` (Atlanta; Parent Company→17b90644; addr Paces Ferry Rd filled)
- Walsh Canada `33a90644-d524-8033-a072-fbd8f3706486` (Toronto; Parent Company→17b90644; addr 310 N Queen filled)
- Walsh VINCI Transit Community Partners `30990644-d524-804c-919a-d463faa9d055` (JV; = Red Line contractor)

**Net-new (created 2026-06-12, Parent Company→17b90644, two-way → Subsidiaries):**
- Walsh Construction `37d90644-d524-8120-94f6-d089de4a5656` (HQ 929 W Adams place filled; ~36 projects)
- Walsh Federal LLC `37d90644-d524-81cc-83f5-f0e70bdfac52` (NAVFAC/USACE; ~6 projects)
Both have inline Tasks/Tickets DBs in body (from create template) — never replace_content.

## People (dedup vs ~423 existing on 17b90644)
**Confirmed existing (already on company, not recreated):** Tim Gerken (CFO/CBO) `33a90644-d524-80a6-960f-cb8014c082be` · Thomas Caplis (SVP) `33a90644-d524-8004-b786-c5647e924bf1` · Michael Whelan (Pres Building Group) `33a90644-d524-80a7-b53e-f818d316e24c`.
**Created (7, 2026-06-12, Company→17b90644):**
- Matthew M. Walsh (Co-Chairman & CEO) `37d90644-d524-811f-bfa0-d0d00b181cd7`
- Daniel J. Walsh (Co-Chairman) `37d90644-d524-8152-b187-d035819aa776`
- Sean Walsh (President, Walsh Construction) `37d90644-d524-81f6-ba3f-ee85a609f396`
- Daniel P. Walsh (President, Archer Western) `37d90644-d524-81cd-9103-c9e30b789354` (also Company→Archer Western)
- Tom Caplis (Sr Exec National Healthcare) `37d90644-d524-818a-9c8f-d3ececf65cde` — ⚠ **soft-dup of existing Thomas Caplis `…924bf1`**; body cross-references it. Merge candidate for Zack.
- David Marchiori (East Region Exec) `37d90644-d524-814a-9d7c-f60e820c05f7`
- Dennis McBride (West Region Exec) `37d90644-d524-813a-9f84-d14137ec10c0`
- Brian McGinty (Pittsburgh Region Exec) `37d90644-d524-8125-ae9e-e08a941eb0ae`
- ⚠ Existing junior namesakes left as-is (filled Functions, not overwritten): Daniel Walsh `…b0a7` (Sr Business Group Leader), Matthew Walsh `…f70e` (Project Executive), Sean Walsh `…427b` (Operations Director). Created records carry the dossier's senior titles; possible same-individual dups — Zack to reconcile.
- No LinkedIn URLs in dossier for any leader (left empty).

## Projects (Construction Projects DB; Contractors → 17b90644, Owning Department → division Companies record, Owner → Owners)
**Existing (not duplicated):** Red Line Extension `34490644-d524-809a-98d4-c9f26e5fae23` (Contractor=Walsh VINCI JV `30990644`, $2.9B) — added to company's Construction Projects list (one-way).
**Created 53 net-new (2026-06-12), all Contractors→17b90644 + Owner→owner-id:**
- **Walsh Construction (Owning Dept `37d9…5656`), 28:** Nut Island Headworks `…81fa-9beb`, West Parish WTP `…8184-af01`, Washington Bridge I-195 $339M `…81ff-9d74`, USCG Station Boston `…814a-acb9`, CTA RPM Ph1 `…8107-b285`, Second Ave Subway Ph2 $1.02B `…8108-80ab`, Brent Spence Bridge $3.1B `…81fa-9a9e`, I-69 Finish Line C5 `…8108-a6d7`, I-69 Ohio River Crossing $202M `…81de-89ff`, South Shore Double-Track $650M `…8149-bd8e`, I-290/I-88@I-294 $327.6M `…8136-84dd`, I-294 NB $205.9M `…81e4-95b9`, Amtrak Sawtooth $2B `…81a2-9f79`, OSU Wexner $1.5B `…81da-9811`, Ryan Field `…81ac-a56e`, Hyperion AWPF `…8169-a4eb`, Pure Water Las Virgenes `…81a9-8d41`, CSVT `…8124-9d16`, LaGuardia Term B `…81d5-b25a`, Caltrain Electrification `…81ea-9a50`, Salesforce Tower `…8157-938e`, Lawson House $128M `…8178-993f`, John Carroll AWE Center `…8103-aad6`, Memorial Hospital Tower `…81e0-a7a0`, Four Seasons DC `…810a-9606`, UK Markey Cancer Ctr `…81a4-b353`, San José–Santa Clara WW `…8182-87bf`.
- **Walsh Federal LLC (Owning Dept `37d9…ac52`), 6:** NAVFAC Mid-Atlantic N4008523C0050 $128M `…810c-9284`, Ground Transport Equip Bldg Warren MI $59.2M `…81b1-b4fd`, NAVFAC IDIQ MAC N62473-21-D-1213 `…81cc-b997`, VA Medical Ctr Louisville $840M `…811b-818a`, F-22A Hangar Langley `…810e-87fd`, JBLM Info Systems Facility `…81b0-b40c`.
- **Archer Western (Owning Dept `33a9…398846`), 18:** DFW Terminal F `…815a-9030`, DART Silver Line `…81e2-8dc2`, Big Creek WRF $300M `…81ab-8543`, Howard Frankland Bridge `…8192-8e91`, I-395 Signature Bridge `…8162-8d1c`, I-26 Connector Asheville `…81d9-a17b`, Carolina Crossroads I-26 `…8191-b6c0`, MARTA Rapid `…815a-970c`, Sarasota-Bradenton Baggage `…81d3-8703`, Cleburne WWTP `…81c6-a729`, Lake Texoma Pump Station $50M `…81a9-a101`, South Cross Bayou WWTP `…8124-a396`, Santa Clara Creek WRF `…819e-9249`, Lift Station 87 $11.5M `…8119-a6ee`, Hutto South WWTP `…8153-820a`, Agua Nueva WRF `…8111-9ff8`, Panorama J Apartments `…8174-9dac`, Simsboro Aquifer WTP `…8146-9277`.
- **Walsh Canada (Owning Dept `33a9…706486`), 2:** Women's College Hospital `…81ce-9a99`, ZEB Bus Charging `…812e-9333`.
- **Type/Location notes:** all 53 got a Type select; 48 got Location tags. **5 untaggable** (no matching state option): I-69 Finish Line (Indiana tag set ✓ actually), Caltrain (California ✓)... → genuinely untagged for-want-of-option: none material; KY projects (VA Louisville, UK Markey, I-69 ORC) carry no KY option (used IN/none) — KY in body only. Federal-nationwide (NAVFAC IDIQ) untagged. **No place:Adress set** — dossier projects have no lat/lng (no-geocoding rule); full address in body + Location tags.
- **3 ownerless** (no owner in dossier): Four Seasons DC, Panorama J Apartments, ZEB Bus Charging.

## Owners (dedup vs existing)
**Existing (linked via projects, not recreated):** FDOT `37b90644-d524-8182-89be-f0d9bb0ca265` (Howard Frankland, I-395) · Amtrak `37b90644-d524-818f-bd74-c37f098fd206` (Sawtooth) · NAVFAC `37b90644-d524-81c2-8696-ce3142972bdd` (IDIQ MAC).
**Created 45 net-new (2026-06-12), all General Contractors→17b90644, Status=Researching, full owner→project + project→owner two-way.** Full name→ID map in `Enlaye Notion/Walsh Corp/_walsh_owner_ids.json`. Highlights: CTA `37d9…8106-9a82` (2 proj) · Illinois Tollway `37d9…8102-99cc` (2) · MTA `37d9…816c-a67b` · MWRA `37d9…813b-b48d` · RIDOT `37d9…81e4-b5f7` · ODOT/KYTC `37d9…81b8-adef` · The Ohio State Univ `37d9…81fc-9e98` · Northwestern `37d9…8121-bc5c` · Dept of Veterans Affairs `37d9…81a3-9227` · USACE `37d9…815a-9ab1` · Port Authority/LaGuardia GP `37d9…8102-96c2` · DART `37d9…8126-ab7b`. (3 of 48 had no owner; see Projects ownerless note.)

## Profile page (built 2026-06-12 — Zack approved)
**"The Walsh Group"** 🏗️ `37d90644-d524-817f-b506-ea40f7cede88` (Market Research → Zack Folder → Companies research). Duplicated from TEMPLATE `37a90644d524…`. Bio snapshot prepended. Page-local data sources:
- **Company Map / Divisions** `collection://a1390644-d524-8246-9671-87d54c2dac3f` — **4 rows created 2026-06-12** (all Companies full database→17b90644 + Projects + leader): Walsh Construction `37d9…81f2-882c` (28 projects, Sean Walsh) · Archer Western `37d9…8192-b16a` (18 projects, Daniel P. Walsh) · Walsh Federal LLC `37d9…814f-98ae` (6 projects) · Walsh Canada `37d9…8115-bc28` (2 projects). Adress place left empty (no sourced lat/lng; HQ in body). **⚠ Divisions view has a leftover `__TEMPLATE__` filter → rows hidden until Zack clears Filter in UI + deletes blank TEMPLATE row.** (Also a 2nd "Divisions" appears as Companies Subsidiaries — both now consistent.)
- **Locations** `collection://27e90644-d524-8263-948b-877b4bbe7fd8` — **+added `Companies` + `Division` relation cols** (pre-authorized). 22 rows created (below).
- **Memberships** `collection://aae90644-d524-8343-aeea-07a2ab4539c2` — **+added `Companies` relation + `Source` URL cols** (pre-authorized). 7 rows created (below).
- Events `collection://b9690644…` (unused) · Projects Underway + Existing Software = shared (linked views, `__TEMPLATE__` filter).

## Page tables (locations / memberships / software)
- **Software:** ✅ Procore row in shared Companies Software DB `37d90644-d524-8168-a692-d4e293617e62` (Software used=[Procore], Location=[United States], → company `Companies Software ` rel).
- **Memberships (7):** ✅ all created in page-local Memberships DB, each Companies→17b90644 + Source URL. AGC `37d9…8156-a10b` · DBIA `37d9…816f-af02` · ASA Chicago `37d9…818b-af58` · UCA `37d9…81fa-a49e` · Construction Safety Week founding `37d9…8143-a3a2` · AGC Culture of CARE `37d9…811a-be9d` · ASFONA `37d9…81a1-89b4`.
- **Locations (22):** ✅ all created in page-local Locations DB, each Companies→17b90644 + Division→subsidiary + full address in `Adress` text. (No place field on this table + no sourced lat/lng → address in text, which the schema uses.) Walsh Construction offices (14): Chicago HQ `37d9…813e-bf23`, Chicago S Torrence `…81da-8070`, Concord CA `…8187-a630`, Corona CA `…81b7-9220`, Crown Point IN `…8109-a37a`, Indianapolis `…811b-bc7a`, Norwood MA `…81e8-9bc2`, Detroit `…81a3-9ebd`, Little Falls NJ `…8165-9f9a`, Pittsburgh `…81be-a7b4`, Seattle `…81eb-90c2` + Herndon VA→Walsh Federal `…81c0-a238`. Archer Western offices (9): Atlanta HQ `…8109-8dd1`, Phoenix `…8149-9bdf`, San Diego `…8196-b113`, Tampa `…8103-bef7`, Charlotte `…8192-a4da`, Cary NC `…8162-8337`, Brentwood TN `…819e-84db`, Irving TX `…8189-941f`, South Jordan UT `…81e7-be8a`. Walsh Canada (1): Toronto HQ `…81e6-b6fd`.

## Left empty (no sourced value)
- Company Address place (lat/lng present in dossier: 41.8786/-87.6536 — fill if accepted) · division/project EMR/TRIR · per-project parcel/APN/FEMA · revenue/headcount splits · dossier `gaps` (13 items) never filled.

## Outstanding / manual UI + decisions for Zack
1. **`Website ` contamination** on company `17b90644` = walshbrothers.com (should be walshgroup.com). **Zack chose LEAVE as-is (2026-06-12)** — fix manually in UI if ever wanted. Conflict stays flagged.
2. ✅ **Memberships + Locations DONE** — Zack approved building the profile page (`37d90644-d524-817f-b506-ea40f7cede88`); 7 memberships + 22 locations created there with relations. (Profile-page Company Map left empty — divisions are Companies records.)
3. **Tom Caplis dup:** new `37d9…d3ececf65cde` vs existing Thomas Caplis `…924bf1` — merge in UI if same person. Same for junior namesakes Daniel/Matthew/Sean Walsh.
4. **`[DELETE ME]` page `37d90644-d524-8155-a58f-fc0c05ca118c`** + child orphans — Zack to trash manually (his choice, 2026-06-12).
5. **KY/federal Location tags:** Projects DB select has no Kentucky option; VA Louisville / UK Markey / I-69 ORC carry KY in body only. Add KY option + tag if wanted (deferred — concurrency-safe later).
6. **Profile-page Divisions view filter (UI):** clear the leftover `__TEMPLATE__`/company rule on the **Divisions** tab + delete the blank `TEMPLATE` row → the 4 division rows appear. (Rows exist in DB; only the view filter hides them.) Same likely on the People tab + Locations/Memberships starter rows.
7. Recommend `/notion-audit walsh` as verification pass.
