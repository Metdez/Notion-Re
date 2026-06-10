# STATE — What Exists Right Now (index)

> **What this file is:** the index to the live picture. The actual database registry, record ledgers, page layouts, and open tasks live in small spokes under [context/state/](context/state/) — open the one you need.
> **Read it:** at the start of every chat (this index is cheap); open a spoke before creating a record of that type (it's the first dedup check — see [loop-and-dedup §1](context/playbook/loop-and-dedup.md)).
> **Write to it:** after every create/update, bump the matching spoke + this snapshot row. If STATE drifts from Notion, Notion wins; reconcile the spoke. Health/growth/splitting rules: [harness-maintenance](context/playbook/harness-maintenance.md).
> **Sibling hubs:** [CLAUDE.md](CLAUDE.md) (rules + router) · [PLAYBOOK.md](PLAYBOOK.md) (how-to) · [LOG.md](LOG.md) (history) · [USER_PREFS.md](USER_PREFS.md) (how Zack works).

---

## State spokes
| Spoke | Holds | Open when |
|---|---|---|
| [databases](context/state/databases.md) | The 4 databases — IDs, URLs, Owners schema, template page | any read/write — to get the data-source handle |
| [research-files](context/state/research-files.md) | **Ground-truth index** — company → dossier file(s) on disk, loaded-status | a task names a company; a new dossier arrives |
| [records-harvard](context/state/records-harvard.md) | Harvard dedup ledger: owner, 12 projects, 11 GCs, 27 people, 16 departments | before touching a Harvard record |
| [records-consigli](context/state/records-consigli.md) | Consigli dedup ledger: 34 projects, 41 people, 21 divisions, cross-linking | before touching a Consigli record |
| [records-clayco](context/state/records-clayco.md) | Clayco dedup ledger: company record, CCDI, 19 divisions, 17 projects, page tables | before touching a Clayco record |
| [records-zachry](context/state/records-zachry.md) | Zachry Group dedup ledger: company, 7 divisions, 8 people, 12 projects | before touching a Zachry Group record |
| [records-dellbrook](context/state/records-dellbrook.md) | Dellbrook \| JKS dedup ledger: company, 3 divisions, 28 projects, 25 people, page tables | before touching a Dellbrook record |
| [records-og](context/state/records-og.md) | O&G Industries dedup ledger: company, 7 divisions, 12 projects, page tables | before touching an O&G record |
| [records-fontaine](context/state/records-fontaine.md) | Fontaine Bros. dedup ledger: company, 2 divisions, 13 projects, 8 people, page tables | before touching a Fontaine record |
| [pages](context/state/pages.md) | Built pages + view IDs: Harvard Projects, Company-profile TEMPLATE, Consigli profile | before editing any of those pages |
| [open-tasks](context/state/open-tasks.md) | In-flight items, pending manual UI steps, notes & known gaps | at chat start; when picking up loose ends |

## Snapshot (keep current — one row per build; details live in the ledger)
**Databases:** Owners · Construction Projects · People · Companies (GCs). Path: Sales → Market Research → Zack Projects. IDs in [databases](context/state/databases.md).

| Build | Status | Scale | ⚠ Outstanding | Ledger |
|---|---|---|---|---|
| Harvard | ✅ complete (06-08) | 1 owner · 12 projects · 11 GCs · 27 people · 16 depts · skim page | — | [records-harvard](context/state/records-harvard.md) |
| Consigli | ✅ complete (06-09, +2 projects 06-09) | 34 projects · 41 people · 21 divisions · profile live · dup cleanup done (18 archived) | manual view filters | [records-consigli](context/state/records-consigli.md) |
| Clayco | ✅ complete (06-09) | company + CCDI · 19 divisions · 17 projects · events/locations/sources/software | 2 view filters (UI) | [records-clayco](context/state/records-clayco.md) |
| Zachry Group | ✅ complete (06-10) | company · 7 divisions · 8 people · 12 projects ($9.25B Golden Pass) | 2 view filters + People-tab (UI) · ≠ Zachry Construction Corp | [records-zachry](context/state/records-zachry.md) |
| Dellbrook \| JKS | ✅ complete (06-10) | company ext. · 3 divisions · 28 projects · 25 people · page tables | Size=Local vs dossier Regional kept · 4 view filters (UI) | [records-dellbrook](context/state/records-dellbrook.md) |
| O&G Industries | ✅ complete (06-10) | company ext. · 7 divisions · 12 projects ($2.47B; CT River Bridge $1.3B) · no People (titles-only dossier) | Size conflict kept · 3 view filters (UI) | [records-og](context/state/records-og.md) |
| Fontaine Bros. | ✅ complete (06-10) | company ext. · 2 divisions · 13 projects ($1.3B; Doherty $316M) · 4+1 people · SkillSignal = incumbent risk platform | Size conflict kept · 2 view filters (UI) · survived concurrent-session option clobber | [records-fontaine](context/state/records-fontaine.md) |

**Awaiting dossiers** (profile template pages already exist): Shawmut · Middlesex · Gilbane · Suffolk · Alberici — see [research-files](context/state/research-files.md).
**Open:** TEMPLATE archive-page deletion · Linkedin straggler check · Notion-UI relation-filter steps · stray SKILL.md copies — [open-tasks](context/state/open-tasks.md).
