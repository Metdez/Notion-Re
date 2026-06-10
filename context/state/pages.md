# State · Built Pages

> **Holds:** the layout + view IDs of the Notion pages built so far — Harvard Projects skim page, Company-profile TEMPLATE, Consigli profile page. Read before editing any of these pages (several host live/shared DBs — see [playbook/safety.md](../playbook/safety.md)).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [databases](databases.md) · [records-harvard](records-harvard.md) · [records-consigli](records-consigli.md) · [open-tasks](open-tasks.md)

---

## Harvard Projects page — skim layout (2026-06-08)
Page: **Harvard Projects** https://app.notion.com/p/37990644d52480fb8847df835e592308 (Zack Folder → Market Research). Holds 5 inline **linked-database views** (not new DBs) + a top summary line. Each view filtered/grouped/trimmed for CEO skim-read.

| Section | View ID | Filter | Group / Sort | Shown columns |
|---|---|---|---|---|
| Owners (top) | `view://37990644-d524-803b-a38b-000cc4dff41c` | none (Harvard is sole owner) | — | Owner, Type, Status, Capital Program, Project Count, Total Project Value, Description |
| Active Projects | `view://37990644-d524-81af-97c5-000cf525f54e` | `Owner` is_not_empty (=12) | Sort: Contrat Value DESC · **No group** | Name, Status, Type, Contrat Value in Million, Location, Owning Department, Contractors |
| General Contractors | `view://37990644-d524-8156-ba07-000cac4a664b` | `Owners` is_not_empty (=11) | Sort: Name ASC · **No group** | Name, Size, Description, Construction Projects, Website  |
| Harvard Departments | `view://37990644-d524-819e-93f1-000c6224db88` | `Owner Institution` is_not_empty (=16) | Sort: Name ASC · **No group** | Name, Parent Company, Description, Owned Projects, People |
| Key Contacts | `view://37990644-d524-8136-bc75-000cd330c055` | `Owner` is_not_empty (=26) | Sort: Name ASC · **No group** | Name, Function, Company, Email, Phone, LinkedIn |

**Key mechanic learned:** the view-config DSL (`notion-update-view`) does NOT support relation `CONTAINS "<page>"` (silently dropped — tried title, page URL, dashed/bare UUID). Only `IS EMPTY`/`IS NOT EMPTY` work on relations. Workaround used: since **Harvard is the only record in the Owners DB**, `IS NOT EMPTY` on each owner-relation isolates exactly the Harvard records. **Caveat:** if a second owner is ever added to the Owners DB, these views will widen — revisit then. Verified counts against Harvard owner rollups (12/11/26/16).

**⚠ Concurrent-session note (2026-06-08):** two assistant sessions built this page in parallel and created duplicate view sets; consolidated to ONE (the table above). The other session's view IDs (`…8184…` GCs · `…8171…` Key Contacts · `…81cc…` Departments) were **removed** — live IDs are `…8193…`, `…81ca…`, `…8180…`. Live views are grouped (Projects→Status, Departments→Parent Company, Key Contacts→Company). `Lead Priority` was dropped from the Key Contacts view and can't be re-added via the DSL ("not found") — re-add in the Notion UI if wanted. **⚠ The Owners DB is physically nested on this page** (real DB, not a linked view) — never `replace_content`/delete the page body.

---

## Company-profile TEMPLATE — clean reusable shell (2026-06-09)
Page: **TEMPLATE** https://app.notion.com/p/37a90644d52480c2a124e7603e47365e (Companies research → Zack Folder → Market Research). A duplicatable hub page for profiling one company; KBE + Consigl are filled copies. **Each page-local table carries 1 merged guide row — in-cell `[fill-in — e.g. sample]` placeholders PLUS a body list explaining every field (incl. the relation/number/date fields the cells can't hint).** 2 shared tables neutralized (not deleted); their on-page notes were extended with a "What goes in this table" line. Body sections also guided: Company Map row Bio + page `## Attack Plan` each have a one-line fill-in instruction. Page block order (unchanged): `# Company Map` → Company Map · Linkedin Post → `### Events` → Events · untitled "Sources" → `### Locations` → Locations → `## Projects Underway` (+note) → Memberships → `# Existing Software` (+note) → `## Attack Plan` (empty).

| Table | Heading | Data-source | Local/Shared | State after cleanup |
|---|---|---|---|---|
| Company Map (internal "Zack Database") | `# Company Map` | `collection://e9790644-d524-8371-a5fd-079cc8fcd7db` | local | 1 guided example row (kept stub `1bf90644…`, user_gray icon). Division title = fill-in instruction; Bio body has a one-line guide; Comments/Tasks/Tickets scaffold intact. Props: Division(title)·Adress(place)·rel Companies/People/Projects |
| Linkedin Post | (under Company Map) | `collection://58d90644-d524-826f-a8c3-07ad3d9de16a` | local | 1 guided example row `37a90644…743bef` (98 rows moved to archive): Name + Post Text = instructions, demo selects Post Type=regular · Media Type=image · Topics=[company news]. 19 props incl. formula PostID + rels People/"Linkedin to Compays" |
| Events (internal "New database") | `### Events` | `collection://fc590644-d524-82e0-bbc0-07edd3ce0f59` | local | 1 guided example row (6 moved): Event name = fill-in instruction. Props: Event name(title)·Date·Location tags(multi)·Place·rel Companies |
| Sources (untitled) | none | `collection://f0390644-d524-82d3-bdd0-07133e934957` | local | 1 guided example row (cleared in place): title = fill-in instruction + URL placeholder. Props: "What the source is about"(title)·URL |
| Locations (internal "New database") | `### Locations` | `collection://d9590644-d524-8353-9b42-0742c1d0cd65` | local | 1 guided example row: Location + Adress = fill-in instructions. Props: Location(title)·Adress(text) |
| Memberships shell | "Memberships" (text) | `collection://b0790644-d524-825f-861d-876ef4215d4d` | local | 1 guided example row: Name = fill-in instruction. Prop: Name(title). NOTE block also has a People linked-view tab (global People, hardcoded company filter → re-point per company) |
| **Projects Underway** | `## Projects Underway` | **`collection://4c8ed827-…-3548304199` (Construction Projects — SHARED w/ KBE/Consigl/Harvard)** | **shared** | rows untouched; view `c0490644-…` filtered `Name="__TEMPLATE__"` → shows empty + re-point note |
| **Existing Software** | `# Existing Software` | **`collection://37690644-d524-804f-b966-000b34a1901b` (Companies Software — SHARED)** | **shared** | rows untouched; view `7b590644-…` filtered `Name="__TEMPLATE__"` → shows empty + note (no company filter exists) |

**Archive page (safe to delete):** "TEMPLATE — old data (safe to delete)" `37a90644-d524-818c-bea9-e91b60b57e72` — holds all ~111 moved rows (Company Map 6 + Events 6 + Linkedin 98 + test 1). Deleting this single page trashes them all. Reversible until then.

**Merged guide-row IDs (verified 2026-06-09):** Company Map `1bf90644-d524-830f-bc00-81d4b872423b` · Linkedin `37a90644-d524-814d-b950-f74688d43bef` · Events `37a90644-d524-8148-9035-cd0bf244275d` · Sources `35090644-d524-833b-b7aa-81cd244e1805` · Locations `37a90644-d524-81ff-a25e-d49383cf8f74` · Memberships `37a90644-d524-812c-9d54-c07b32b3285d`. Each = title `[...e.g...]` placeholder + body "What goes in each field" list.

**⚠ Concurrent-session collision (2026-06-09, 2nd occurrence):** two assistant sessions answered the same "tell people what to put in" request in parallel — one wrote in-cell placeholders into the skeleton rows, the other created 6 separate "Fill-in guide" rows. Per Zack (AskUserQuestion: "Keep both, merged") the standalone rows' body field-lists were appended INTO the skeleton rows and the 6 standalone rows (`37a90644…816b/81a4/81e0/815c/814b/8129`) were moved to the archive page. One guide row per table now.

**Mechanic learned (now in mind):** Notion MCP has NO per-row delete — `notion-move-pages` a row to a plain page parent removes it from its collection (non-destructive). The 6 local tables each use a UNIQUE collection per page (TEMPLATE≠KBE≠Consigl); only the 2 shared tables collide. Property names verbatim: `Adress` (misspelled, Company Map + Locations), `Contrat Value in Million`. **Icons:** a valid built-in name normalizes to `icons/<name>` on fetch; an INVALID name (e.g. `award`) is stored as a literal `/icons/<name>.svg` URL = broken image. Verified-good this session: `map, megaphone, calendar, link, location, star` (+ prior `building, user`). **Rows w/ blank title AND blank body are invisible to `notion-search`; once they hold any text they surface — so the skeleton rows became findable only after the placeholder text was added.**

---

## Consigli Building Group — profile page (2026-06-09)
Page: **Consigli Building Group** https://app.notion.com/p/37a90644d524806fa31de6ef42083b66 (Companies research → Zack Folder). Title updated. Bio inserted after `# Company Map` heading. Company Map collection `collection://8e490644-d524-8359-bfab-071b34697cf3` now has **20 division rows** (plus the original guide row). **`Adress` (place type) IS settable via MCP** (2026-06-09 completeness pass) — use the expanded keys `place:Adress:name` / `place:Adress:address` / `place:Adress:latitude` / `place:Adress:longitude` in `update_properties`. All 20 rows now carry name + street address + lat/lng (functional/company-wide units use Milford HQ base coords). Address also remains in each row's body. *(Corrects earlier "could not be set via MCP" note — the prior attempt likely used the flat key instead of the expanded form.)*
> The Consigli projects + people build + cross-linking is in [records-consigli.md](records-consigli.md).

| Division | Notion ID |
|---|---|
| Milford, MA (Corporate HQ) | `37a90644-d524-8199-b6b8-d872499fc497` |
| Boston, MA | `37a90644-d524-8139-bd84-c52fb9691fc9` |
| Portland, ME | `37a90644-d524-81b2-a672-fb8d071bd334` |
| Hartford, CT | `37a90644-d524-81de-b256-cbdc4b0869fc` |
| Providence, RI | `37a90644-d524-8171-bef9-ec4ed31febed` |
| Manchester, NH | `37a90644-d524-8103-bf5f-d137d54a8171` |
| New York City, NY | `37a90644-d524-81d6-acab-deb855738cb2` |
| Melville, NY (Long Island) | `37a90644-d524-8122-8069-de0bf5eed810` |
| Westchester / White Plains, NY | `37a90644-d524-8125-a3dc-c51ef59beb3b` |
| Pleasant Valley, NY (Hudson Valley) | `37a90644-d524-813e-8e6d-c06cbdaf9c82` |
| Albany / Latham, NY (Capital Region) | `37a90644-d524-81a9-b84a-f59738030c15` |
| Washington, DC (Mid-Atlantic) | `37a90644-d524-8117-be59-c82a9a05e0b9` |
| New Brunswick, NJ | `37a90644-d524-81d8-abba-deebf4c4a8eb` |
| Raleigh-Durham, NC | `37a90644-d524-81a7-bfb4-fa6dd2d9b9fe` |
| Caribbean (U.S. Virgin Islands) | `37a90644-d524-8166-bf3d-e93f5f692050` |
| Riggs (Self-Perform Division) | `37a90644-d524-8154-8fc7-f9d5b3f0c33e` |
| Arch Energy (Energy Division) | `37a90644-d524-81ba-ae55-d7b5ade4bb5c` |
| Advanced Technology & Mission Critical | `37a90644-d524-81a9-ad9e-e987081d1b27` |
| Interiors Group | `37a90644-d524-8103-9d88-d530f17d1bd7` |
| Special Projects Group | `37a90644-d524-81b8-9193-c7f9cbb06a99` |

**Other sections filled (2026-06-09):**
- Events (`collection://90790644-d524-8220-8e3e-073d5a6a2d2a`): **6 rows** — AGC Build NE · Women Builders Council · AGC Metro DC · NAIOP DC/MD · ACE Mentor · AGC MA Golf Classic. New multi-select options added: Massachusetts, New York City, Washington DC.
- Sources (`collection://9e890644-d524-8382-bd2a-8743f0aad15a`): **10 rows** — firmographics, ENR rank, Lendlease acquisition, divisions, software stack, CMiC migration, St. Croix project.
- Locations (`collection://bb190644-d524-82ff-a057-8783e2a29ebb`): **15 rows** — all 15 office addresses. `Adress` is a text field here (unlike Company Map where it's `place` type) — all values set successfully.
- Memberships (`collection://e6190644-d524-8234-83c0-87fb9915f4fd`): **8 rows** — USGBC · AGC MA (Jeff Navin Vice-Chair) · AGC Metro DC · BIA NH · BuildingGreen · Women Builders Council · NAIOP DC/MD · DBIA.
- Existing Software (shared `collection://37690644-…`): **7 rows** — Procore · Bluebeam Revu · Autodesk BIM 360 · CMiC · QuickBase · Revizto · Sage/OST/Togal. Category/Notes in body content (shared DB schema has no relation or category fields).
- Attack Plan: **filled** — CMiC migration window, top 3 entry divisions (Mission Critical, ex-Lendlease NY/NJ, public K-12), ESOP angle, AGC MA engagement path, DC gap flagged.
- ⚠ **Projects Underway view still filtered to `Name = "__TEMPLATE__"` — clear this filter manually in Notion UI to show Consigli's projects.**
