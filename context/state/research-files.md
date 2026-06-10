# State · Research Files — ground-truth dossier index

> **Holds:** the map from each company to its research dossier file(s) on disk under `Enlaye Notion/`. Dossiers are the ONLY ground truth for loads and audits — when a task names a company, this is where you find its source files.
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md)
> **Siblings:** the per-company ledgers ([records-harvard](records-harvard.md) · [records-consigli](records-consigli.md) · [records-clayco](records-clayco.md) · [records-zachry](records-zachry.md) · [records-dellbrook](records-dellbrook.md) · [records-og](records-og.md) · [records-fontaine](records-fontaine.md))
> **Write to it:** the moment a new dossier file lands on disk — add its row here (and create the company's ledger per [harness-maintenance §11.3](../playbook/harness-maintenance.md) before loading).

| Company | Dossier file(s) (ground truth) | Loaded? | Ledger |
|---|---|---|---|
| Harvard | `Enlaye Notion/Harvard Researsch/1Harvard University Construction Intelligence Resea.md` · `2Harvard Researsch.md` | ✅ 2026-06-08 | [records-harvard](records-harvard.md) |
| Consigli | `Enlaye Notion/Consigli Researsch/Consig researsch.md` · `Con more.md` · `Con Perp Re.md` · `2[https___www.consigli.com_].md` (crawl) | ✅ 2026-06-09 (load + ~6 audit passes) | [records-consigli](records-consigli.md) |
| Clayco | `Enlaye Notion/Clayco/Clay 1.md` | ✅ 2026-06-09 | [records-clayco](records-clayco.md) |
| Zachry Group | `Enlaye Notion/Zachary Group/zach1.md` | ✅ 2026-06-10 | [records-zachry](records-zachry.md) |
| Dellbrook \| JKS | `Enlaye Notion/DellbrrokJKS/Dell 1.md` | ✅ 2026-06-10 | [records-dellbrook](records-dellbrook.md) |
| O&G Industries | `Enlaye Notion/O&G/OG1.md` | ✅ 2026-06-10 | [records-og](records-og.md) |
| Fontaine Bros. | `Enlaye Notion/Fontaine Bros/Font1.md` | ✅ 2026-06-10 | [records-fontaine](records-fontaine.md) |

**Profile pages exist but no dossier on disk yet** (template copies created 2026-06-09, awaiting research): Shawmut · Middlesex · Gilbane · Suffolk · Alberici · KBE (pre-existing profile). When a dossier arrives: add its row above → create the ledger → run `/notion-load`.

**Prompt that generates dossiers:** `Enlaye Notion/Internal tuff/COMPANY_RESEARCH_PROMPT.md` (+ working copies in `Enlaye Notion/Prompts/`). Loading procedure: [playbook/research-load-prompt.md](../playbook/research-load-prompt.md) or the `/notion-load` skill.
