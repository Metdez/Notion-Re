# Playbook · Notion MCP Mechanics (§9)

> **Holds:** the hard-won gotchas of the Notion MCP — read before writing anything to Notion.
> **Part of:** [PLAYBOOK.md](../../PLAYBOOK.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [loop-and-dedup](loop-and-dedup.md) · [schemas](schemas.md) · [conventions](conventions.md) · [recipes](recipes.md) · [safety](safety.md)

## 9. Notion MCP mechanics (gotchas — read before writing)
- **Relations:** value = the related page's **full URL** (`https://app.notion.com/p/<id>`), not a bare ID. Multiple → JSON-array string, e.g. `"[\"url1\",\"url2\"]"`.
- **Multi-select / multi-value:** JSON-array string. A bare comma-joined string is read as ONE option.
- **Select / multi-select options do NOT auto-create.** Add them first via `notion-update-data-source` → `ALTER COLUMN "X" SET MULTI_SELECT(...)` **including the full existing option list** (matches by name → preserves existing cell values; only colors reset).
- **Icons:** Notion built-in icons accepted as `/icons/<name>_<color>.svg` (confirmed: `building_*`, `user_gray`). Set via `icon` on create-pages / update-page. (No emoji per Zack.) **Icon-validity:** a valid built-in name normalizes to `icons/<name>` on fetch; an INVALID name (e.g. `award`) is stored as a literal `/icons/<name>.svg` URL = broken image. Verified-good names live in [state/open-tasks.md](../state/open-tasks.md).
- **Page bodies / newlines:** `create-pages` `content` renders `\n` correctly. **`update-page` (`insert_content`/`replace_content`/`update_content`) needs REAL newlines** — escaped `\n` renders as a literal "n". Use actual line breaks. `replace_content` fails safely if the page has child databases (won't delete them) — for those (e.g. BOND with inline Tasks/Tickets) use `update_content` instead.
- **Property name quirks:** Companies DB `Website ` and `Competitor Involvement ` have a **trailing space**; Projects value field is misspelled `Contrat Value in Million`; Companies Size option is misspelled `Mutlinational`; `Adress` is misspelled in Company Map + Locations collections. Match verbatim.
- **Dates:** set via expanded `date:<Prop>:start` (+ optional `:end`, `:is_datetime`). **Properties named `url`/`id`** → prefix `userDefined:` (e.g. `userDefined:URL`).
- **Stale reads:** `notion-fetch` can return a cached snapshot (old `Last edited`). Re-fetch to confirm a write landed.
- **No per-row delete:** the MCP has no per-row delete/archive tool (only create/update + trash-whole-data-source). Workaround: `notion-move-pages` a row to a plain page parent REMOVES it from its collection (becomes a child page; reversible; relation/property values drop since it leaves the schema).
- **Invisible rows:** a row with blank title AND blank body is invisible to `notion-search`; once it holds any text it surfaces.
- **Linked DB views:** `notion-create-view parent_page_id` appends a linked view to the **page end** (no mid-page insert). Filters: only `IS EMPTY`/`IS NOT EMPTY` parse on relations — relation `CONTAINS "<page>"` is **silently dropped**. A property removed from a view's visible columns can't be re-added/sorted via DSL ("could not find property") — fix in the UI.
- **Nested databases on a page:** a page can physically *host* a database (the real DB, parent = that page), not just reference it via a linked view — check `notion-fetch` ancestry (`<parent-page>`). **Never `replace_content`/delete such a page's body** (it deletes the DB). The **Owners DB lives on the Harvard Projects page** (`37990644-d524-80fb-…`) — see [state/pages.md](../state/pages.md).
