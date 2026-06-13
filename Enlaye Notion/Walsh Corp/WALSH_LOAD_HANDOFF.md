# Walsh Load — Handoff (read fully before any Notion write)

**Task:** `/notion-load` of `Enlaye Notion/Walsh Corp/walsh_group_dossier_v2.json` for **The Walsh Group** (walshgroup.com, Chicago GC, ENR #16).

## ⛔ Hard rules (a prior session broke these — do not repeat)
1. **Preexisting Notion is ALWAYS right. Never edit, overwrite, or relink an existing record/field.** Additive only.
2. **walshgroup.com ≠ walshbrothers.com — different companies.** Do not "fix" walshbrothers.com anywhere.
3. **Confirm the target with Zack BEFORE creating anything.** Don't auto-start the load.
4. Dedup before every create: search the state ledger, then live Notion (incl. People DB), incl. name variants.

## ⚠️ Known dedup landmines (verified this session)
- **`17b90644-d524-809d-9810-defa38a2cbc9` — "The Walsh Group"** in Companies DB. Skeletal but PREEXISTING: ~423 scraped people, `Website=walshbrothers.com`, `LinkedIn=walsh-construction`, blank Description/body, Country=[USA,Illinois], linked to Strategy `22a90644…`. **Zack says leave it exactly as-is.** Do NOT load the dossier onto it without explicit say-so.
- **`22a90644-d524-80de-9a20-fb2da7c13d5e` — "Walsh Group"** in **Strategy DB** (not Companies). BD/Conquest page (Red Line pilot, Innovation team contacts). Leave untouched.
- **`24e90644…` — "Walsh Brothers"** = different company (Richard C. Walsh CEO). Leave untouched.
- Leadership already exist as People (linked to `17b90644…`, `@walshgroup.com`): Matthew Walsh `33a90644…f70e`, Sean Walsh `…427b`, Tim Gerken (CFO) `…c082be`, Thomas Caplis `…924bf1`, Michael Whelan `…16e24c`, Daniel Walsh (ambiguous) `…b0a7`. Dedup against these — don't recreate.
- Existing project **"Red Line Extension" `34490644…`** (=dossier project #4; Contractors=`30990644…` JV, value stored as raw 2900000000). Update/skip — don't duplicate.

## ❓ Unresolved — ASK ZACK FIRST
- Which record does `walsh_group_dossier_v2.json` go to? Options: (a) brand-new Companies record, (b) the preexisting `17b90644…`, (c) don't load. **He has not confirmed.** No loading until he picks.
- Pending cleanup: a page titled **"[DELETE ME — mistaken Walsh load, safe to trash]"** (`37d90644-d524-8155-a58f-fc0c05ca118c`) holds a tombstoned dup company + 5 stray people from the aborted attempt. Ask if he wants it trashed.

## Dossier contents (ground truth = the JSON only)
- **Company:** founded 1898, ENR #16 (2025), $7.69B 2024 rev, 8000+ staff, HQ 929 W Adams St, Chicago IL 60607, family-owned, Size=Mutlinational.
- **4 divisions:** Walsh Construction (1949, Chicago, ~36 proj), Archer Western (1983, Atlanta, ~26), Walsh Canada (2009, Toronto, ~3), Walsh Federal LLC (NAVFAC/USACE).
- **54 projects** (fully attributed). Mojibake in names: fix via `s.encode('latin-1').decode('utf-8')` (em-dash `–`, accents).
- **10 leadership** (in `extra.leadership`, NOT a top-level `people` key): 2 co-chairmen, 2 fourth-gen, 6 execs. No LinkedIn URLs in dossier.
- **22 locations** (all have addresses), **7 memberships** (AGC, DBIA, ASA Chicago, UCA, Construction Safety Week, AGC Culture of CARE, ASFONA), **1 software** (Procore), **48 owners/clients**, **61 sources**.
- **`gaps` list (13)** = genuinely unknown; never fill.

## DB handles
- Companies: `collection://041b7f07-9564-4696-ae78-1b61b34df758` (props: Name, Description, Size[Mutlinational/Regional/Local/Start-up], Type, BW Category[Builder], Country[multi], `Website ` (trailing space), LinkedIn, Address[place], rel Construction Projects/People/Subsidiaries/Parent Company/Strategy)
- Construction Projects: `collection://4c8ed827-78b9-4d34-9cca-0c3548304199` (Name, Status[Done/In progress/Not started], Type, `Contrat Value in Million`, Date[range], Location[multi], `Adress`+`Adresss`[place], rel Contractors→Companies / Owning Department→Companies / Owner→Owners, userDefined:URL)
- People: `collection://0b7ff339-0887-4bbf-a218-7f8d4ede89ef` (Name, Function, Function Qualification[multi], Location[multi], LinkedIn, rel Company→Companies. NOTE People.`Division` rel points to a fixed "Zack Database" collection, NOT the profile's page-local Company Map.)
- Owners: `collection://37990644-d524-80da-92f8-000b22169334`
- Template page to duplicate (only if Zack approves new build): `37a90644d52480c2a124e7603e47365e`. Duplicating gives fresh page-local collections for Company Map(divisions)/Events/Sources/Locations/Memberships; Projects & Software tables are SHARED (filtered to `__TEMPLATE__`).

## Interlink (only if loading is approved)
Person→Company + Person→Division (via the division row's `People` rel, not People.Division). Division→Company/People/Projects. Project→Contractors+Owning Department+Owner. Every located row carries its address in the `place` field + a location tag. Load all 7 memberships. Serialize creates per record type.

## Harness bookkeeping
No `records-walsh.md` ledger exists yet — create one before first write, add its row to STATE.md + research-files.md, append to `context/log/2026-06.md`. (Skill: `context/state/`, `STATE.md`.)
