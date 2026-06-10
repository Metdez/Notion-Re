# STATE — What Exists Right Now (index)

> **What this file is:** the index to the live picture. The actual database registry, record ledgers, page layouts, and open tasks live in small spokes under [context/state/](context/state/) — open the one you need.
> **Read it:** at the start of every chat (this index is cheap); open a spoke before creating a record of that type (it's the first dedup check — see [loop-and-dedup §1](context/playbook/loop-and-dedup.md)).
> **Write to it:** after every create/update, bump the matching spoke. If STATE drifts from Notion, Notion wins; reconcile the spoke. Split a spoke when it outgrows its file — see [context/MAP.md](context/MAP.md).
> **Sibling hubs:** [CLAUDE.md](CLAUDE.md) (rules + router) · [PLAYBOOK.md](PLAYBOOK.md) (how-to) · [LOG.md](LOG.md) (history) · [USER_PREFS.md](USER_PREFS.md) (how Zack works).

---

## State spokes
| Spoke | Holds | Open when |
|---|---|---|
| [databases](context/state/databases.md) | The 4 databases — IDs, URLs, Owners schema, template page | any read/write — to get the data-source handle |
| [records-harvard](context/state/records-harvard.md) | Harvard dedup ledger: owner, 12 projects, 11 GCs, 27 people, 16 departments | before touching a Harvard record |
| [records-consigli](context/state/records-consigli.md) | Consigli dedup ledger: 19 projects, 21 people, cross-linking | before touching a Consigli record |
| [records-clayco](context/state/records-clayco.md) | Clayco dedup ledger: company record, CCDI, 19 divisions, 17 projects, events/locations/sources/software | before touching a Clayco record |
| [records-zachry](context/state/records-zachry.md) | Zachry Group dedup ledger: company record, 7 divisions, 8 people, 12 projects, page tables | before touching a Zachry Group record |
| [records-dellbrook](context/state/records-dellbrook.md) | Dellbrook \| JKS dedup ledger: company record, 3 divisions, 28 projects, 25 people, events/memberships/locations/sources/software | before touching a Dellbrook record |
| [records-og](context/state/records-og.md) | O&G Industries dedup ledger: company record, 7 divisions, 12 projects, events/sources/locations/memberships/software | before touching an O&G record |
| [records-fontaine](context/state/records-fontaine.md) | Fontaine Bros. dedup ledger: company record, 2 divisions, 13 projects, 8 people, page tables | before touching a Fontaine record |
| [pages](context/state/pages.md) | Built pages + view IDs: Harvard Projects, Company-profile TEMPLATE, Consigli profile | before editing any of those pages |
| [open-tasks](context/state/open-tasks.md) | In-flight items, pending manual UI steps, notes & known gaps | at chat start; when picking up loose ends |

## Snapshot (keep current)
- **Databases:** Owners · Construction Projects · People · Companies (GCs). Path: Sales → Market Research → Zack Projects. IDs in [databases](context/state/databases.md).
- **Harvard build:** complete — 1 owner, 12 projects, 11 GCs, 27 people, 16 dept companies, skim page live. [records-harvard](context/state/records-harvard.md) · [pages](context/state/pages.md).
- **Consigli build:** complete — 34 projects (+ Fort Meade UEPH & Watervliet Fire Station, 2026-06-09) + 41 people + 21 divisions, profile page live, all Division links set. Duplicate cleanup done (18 copies archived). [records-consigli](context/state/records-consigli.md).
- **Clayco build:** complete (2026-06-09, from Clay 1.md) — company record extended, CCDI created, 19 division rows, 17 projects, 3 events, 9 locations, 19 sources, 3 memberships, 4 software rows, all cross-linked. Profile page bio + Attack Plan filled. ⚠ 2 view filters need manual UI fix. [records-clayco](context/state/records-clayco.md).
- **Zachry Group build:** complete (2026-06-10, from zach1.md) — company record created, 7 division rows, 8 people, 12 projects, 3 events, 12 sources, 13 locations, 1 membership, 5 software rows, all cross-linked. Profile page bio + Attack Plan filled, renamed "Zachry Group". ⚠ 2 view filters + People-tab filter need manual UI fix. Distinct from Zachry Construction Corp. [records-zachry](context/state/records-zachry.md).
- **Dellbrook | JKS build:** complete (2026-06-10, from Dell 1.md) — company record extended (Description/Type/Address/Snapshot body/28-project relation), 3 division rows, 28 projects, 16 people created (9 pre-existing kept), 6 events, 8 memberships, 2 locations, 32 sources, 7 software rows, cross-linked. Profile page bio + Attack Plan filled. ⚠ Size=Local vs dossier "Regional" conflict kept; 4 view filters need manual UI fix. [records-dellbrook](context/state/records-dellbrook.md).
- **O&G Industries build:** complete (2026-06-10, from OG1.md) — company record extended (Type/Description/Address/Country/Snapshot body/12-project relation), 7 division rows, 12 projects ($2.47B tracked; CT River Bridge $1.3B), 3 events, 25 sources, 12 locations, 4 memberships, 4 software rows (2 created, 2 extended), cross-linked. Profile page bio + Attack Plan filled, renamed "O&G Industries". ⚠ Size=Local vs dossier "Regional" conflict kept; no People created (titles-only dossier); 3 view filters need manual UI fix. [records-og](context/state/records-og.md).
- **Fontaine Bros. build:** complete (2026-06-10, from Font1.md) — company record extended (Description/Type/Country/Address/Snapshot body/13-project relation), 2 division rows, 13 projects ($1.3B sourced; Doherty $316M), 4 people created + D. Fontaine Jr. enriched, 2 events, 8 sources, 2 locations, 1 membership, 4 software rows (SkillSignal = incumbent risk platform), cross-linked. Profile page bio + Attack Plan filled. ⚠ Size=Local vs dossier "Regional" conflict kept; 2 view filters need manual UI fix; survived a concurrent-session Type/Location option clobber (re-applied as union). [records-fontaine](context/state/records-fontaine.md).
- **Open:** TEMPLATE archive-page deletion + Linkedin straggler check + several Notion-UI relation-filter steps. [open-tasks](context/state/open-tasks.md).
