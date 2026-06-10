# State · Open Tasks & Known Gaps

> **Holds:** what's in flight (pending manual steps, stragglers to confirm) + standing notes and known gaps (decisions, icon conventions, schema facts).
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [databases](databases.md) · [records-harvard](records-harvard.md) · [records-consigli](records-consigli.md) · [pages](pages.md)

---

## Open tasks / in-flight
- **Stray SKILL.md copies (2026-06-09):** `SKILL.md` (repo root) and `Enlaye Notion/SKILL.md` are byte-identical copies of `.claude/skills/notion-audit/SKILL.md` (the canonical one Claude Code loads). Zack to confirm they're not used elsewhere (e.g. pasted into claude.ai) → then delete or archive. Until confirmed, edits to the audit skill go in `.claude/skills/notion-audit/` only.
- **TEMPLATE guide rows (2026-06-09):** done in place. Each of the 6 page-local tables has 1 merged guide row = in-cell `[…e.g…]` placeholders + a body "What goes in each field" list (every field, incl. relations/numbers); Bio + Attack Plan also guided. **Shared tables (Projects Underway, Existing Software) intentionally have NO example row** — their rows are shared across KBE/Consigl/Harvard, so a sample there would pollute every profile; guidance lives in their on-page notes (extended this session with "What goes in this table"). Pending Zack: (1) **delete archive page** `37a90644-d524-818c-bea9-e91b60b57e72` once the template looks right (now also holds the 6 retired standalone guide rows); (2) ⚠ **2 likely Linkedin stragglers found** — `58090644-d524-835f-909c-81e16563b0d3` ("41 Years ABC Member") + `49590644-d524-8318-a259-01918055016d` ("August Steelpointe Pre-Leasing") surfaced under the local Linkedin collection; confirm in UI and move to archive if they're leftover KBE data (left untouched — could be global-DB false positives); (3) optional — mark TEMPLATE as a native "New ▾" template (manual; MCP can't); (4) optional cleanup — Linkedin `Author` + Events `Location tags` select options are still KBE-specific leftovers (schema, not data); genericize if wanted.
- Harvard construction-research build + department hierarchy + Harvard Projects page skim layout complete (2026-06-08).
- **Consigli manual UI steps** (MCP can't set relation filters on shared/embedded views) — see [records-consigli.md](records-consigli.md) "Still manual in Notion UI".
- **⚠ Software DB duplicates (found 2026-06-10, O&G audit round 2):** shared Companies Software DB `37690644-d524-804f…` now holds **Procore ×3** (canonical Consigli+O&G `37a90644-d524-817b…` · Zachry `37b90644-d524-812e-8ada-f4656dd5a13c` · Dellbrook `37b90644-d524-8163-9279-f314cfd1ebe7`) and **Bluebeam ×3** (canonical `37a90644-d524-81f1…` · Zachry `…815c-8592…` · Dellbrook `…8170-8e04…`) — concurrent sessions created per-company rows instead of extending the canonical one-row-per-tool pattern. Zack to decide: merge into canonical rows (move Companies relations + body notes, then archive dupes) or accept per-company rows as the new pattern. **Deletion = destructive, needs explicit OK.**

- **Audit pass 2026-06-10 deferred items:** the full-portfolio `/notion-audit` (all 18 builds) left manual-OK follow-ups — shared Projects `Location` + Company `Country` options to add in UI; Events location-tag options (FL/MA/VA/NC/Las Vegas/San Diego); **KBE Mozaic dup** (`…814b` vs `…81d1`); **Cianbro** partial memberships (~12 of ~30); **Memberships collection missing `Company` relation** (Clayco, Zachry); **O&G `OD.md` needs `/notion-load`** (net-new); **Bechtel UEI/CAGE** verify (SAM.gov). Full list → [audit-pass-2026-06-10-deferred.md](audit-pass-2026-06-10-deferred.md).

---

## Notes / known gaps
- **Single-owner decision:** all Harvard projects link to one "Harvard" owner record; owning department captured as text in each project brief (per Zack, 2026-06-08).
- **Icons:** people `/icons/user_gray.svg`, owner/GC companies `/icons/building_blue.svg`. **Projects now use varied emojis** (per Zack, 2026-06-08): 🔬 ERC · 🎭 ART/100 South · 🏘️ Eliot · 📈 Pritzker · 🌳 William James Plaza · 🔨 Barker · 🏪 12 Palmer · 🎓 HBS · 🧬 HMS Bertarelli · 🌊 NASDEP · ♨️ Tunnel 29/30 · 🔧 ESL. Department companies also use varied emojis (see below).
- **Verified-good built-in icon names** (normalize to `icons/<name>` on fetch): `building, user, map, megaphone, calendar, link, location, star`. INVALID names (e.g. `award`) store as a literal broken URL — see [playbook/notion-mcp.md](../playbook/notion-mcp.md).
- Schema additions to Construction Projects: Type option `Infrastructure`; Location options `Massachusetts, Cambridge, Allston, Boston, Longwood`.
- **New relations (2026-06-08, for departments):** Companies `Owned Projects`⇄ Projects `Owning Department`; Companies `Owner Institution`⇄ Owners `Departments`. Use these for owner-department links — NOT the GC relations (`Contractors`/`General Contractors`).
- **Dept emoji exception (per Zack):** Harvard *department companies* use varied emoji icons (🏛️🏗️🗺️🏢⚡🏬🏠🧭🌱📐🛠️⚕️⚙️💼🎭📣); the earlier "no-emoji" rule still applies to projects/people/GCs.
- Architects & developers (KieranTimberlake, Studio Gang, Tishman Speyer, Breakthrough, NorthStar, etc.) captured as **text in project briefs**, not separate company records (kept GC-focused/lean).
- Owners DB schema is live (see [playbook/schemas.md](../playbook/schemas.md)).
- One manual step pending in Notion: mark the "⟨Owner Name⟩ — TEMPLATE" page as the DB's native template (MCP can't register it in the **New ▾** dropdown).
