# State · Research Files — ground-truth dossier index

> **Holds:** the map from each company to its research dossier file(s) on disk under `Enlaye Notion/`. Dossiers are the ONLY ground truth for loads and audits — when a task names a company, this is where you find its source files.
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md)
> **Siblings:** the per-company ledgers ([records-harvard](records-harvard.md) · [records-consigli](records-consigli.md) · [records-clayco](records-clayco.md) · [records-zachry](records-zachry.md) · [records-zachry-construction](records-zachry-construction.md) · [records-dellbrook](records-dellbrook.md) · [records-og](records-og.md) · [records-fontaine](records-fontaine.md))
> **Write to it:** the moment a new dossier file lands on disk — add its row here (and create the company's ledger per [harness-maintenance §11.3](../playbook/harness-maintenance.md) before loading).

| Company | Dossier file(s) (ground truth) | Loaded? | Ledger |
|---|---|---|---|
| Harvard | `Enlaye Notion/Harvard Researsch/1Harvard University Construction Intelligence Resea.md` · `2Harvard Researsch.md` | ✅ 2026-06-08 | [records-harvard](records-harvard.md) |
| Consigli | `Enlaye Notion/Consigli Researsch/Consig researsch.md` · `Con more.md` · `Con Perp Re.md` · `2[https___www.consigli.com_].md` (crawl) | ✅ 2026-06-09 (load + ~6 audit passes) | [records-consigli](records-consigli.md) |
| Clayco | `Enlaye Notion/Clayco/Clay 1.md` · `Clayco1.md` · `Clayco3.md` (2nd-pass, 06-10) · `Clayco4.md` (confirmed identical structure to Clayco3.md; registered 06-11) | ✅ 2026-06-09 (+2nd pass 06-10) | [records-clayco](records-clayco.md) |
| Zachry Group | `Enlaye Notion/Zachary Group/zach1.md` | ✅ 2026-06-10 | [records-zachry](records-zachry.md) |
| Dellbrook \| JKS | `Enlaye Notion/DellbrrokJKS/Dell 1.md` (1st) · `Dell2.md` (2nd-pass, captured 06-12 — **⚠ partial:** chat paste truncated; 16/22 projects + company enrichment) | ✅ 2026-06-10 (Dell 1) · ⏳ **Dell2 NOT loaded — no Notion connector 06-12** | [records-dellbrook](records-dellbrook.md) |
| O&G Industries | `Enlaye Notion/O&G/OG1.md` | ✅ 2026-06-10 | [records-og](records-og.md) |
| Fontaine Bros. | `Enlaye Notion/Fontaine Bros/Font1.md` (1st) · `Fontaine.md` (2nd-pass, 16 proj → +6 net-new) | ✅ 2026-06-10 (both passes) | [records-fontaine](records-fontaine.md) |
| HITT Contracting | `Enlaye Notion/HITT/HITT1.md` (HITT2.md empty) | ✅ 2026-06-10 | [records-hitt](records-hitt.md) |
| Jingoli Nuclear Services | `Enlaye Notion/Jingoli/Jingoli.md` | ✅ 2026-06-10 | [records-jingoli](records-jingoli.md) |
| Cianbro | `Enlaye Notion/Cianbro/Cianbro.md` (Cianbro2.md empty) | ✅ 2026-06-10 | [records-cianbro](records-cianbro.md) |
| Bechtel Group | `Enlaye Notion/Bechtel Group/Bechtel2.md` (primary) · `Bechtel1.md` (mapped) | ✅ 2026-06-10 | [records-bechtel](records-bechtel.md) |
| Branch Group | `Enlaye Notion/Branch Group/Branch1.md` (single-line JSON dossier) | ✅ 2026-06-10 | [records-branch](records-branch.md) |
| Alberici | `Enlaye Notion/Alberici Corp/Alb.md` (single sourced JSON dossier) | 🔄 2026-06-10 in progress | [records-alberici](records-alberici.md) |
| KBE Building | `Enlaye Notion/KBE Building/KBE.md` (KBE1.md empty) | ✅ 2026-06-10 (additive gap-fill on pre-existing 06-05 build) | [records-kbe](records-kbe.md) |
| The Middlesex Corporation | `Enlaye Notion/The Middlesex Corp/Middlesex.md` (disk dossier; truncated mid-`sources`) **+ richer in-chat-only dossier** (not on disk: exec roster, $609.9M/#203, more tools) | ✅ 2026-06-10 (disk) · ✅ 2026-06-10 2nd pass (in-chat extras: +10 execs, Middlesex Asphalt div, +4 software) | [records-middlesex](records-middlesex.md) |
| FlatironDragados | `Enlaye Notion/FlatironDragados/Flat.md` (primary) · `Flatiron1.md` (secondary; Flat1.md empty) | ✅ 2026-06-10 | [records-flatirondragados](records-flatirondragados.md) |
| Sundt | `Enlaye Notion/Sundt/Sundt.md` (single-line JSON dossier; no people array) | ✅ 2026-06-10 | [records-sundt](records-sundt.md) |
| Kiewit Corporation | `Enlaye Notion/Kiewitt/Kiewitt.md` · `Kiewitt1.md` (no longer empty — 15-div/14-proj JSON, on disk 06-10) · **`Kiewitt2-PARTIAL.md` = 3rd dossier (28 div · 17 proj, exhaustive), TRUNCATED chat capture 06-12 — projects/people/sources sections missing; awaiting full file from Zack before `/notion-load`** | ✅ 2026-06-10 (1st) · ⏳ 3rd dossier NOT loaded (partial + no Notion connector) | [records-kiewit](records-kiewit.md) |
| Shawmut | `Enlaye Notion/Shawmut/Shawmut3.md` (Shawmut2 truncated/corrupt; 1 & 4 empty) | ✅ 2026-06-10 (prior-session build + this-session audit/complete/record) | [records-shawmut](records-shawmut.md) |
| Zachry Construction Corporation | `Enlaye Notion/Zachary Group/zach3.md` (⚠ ≠ Zachry Group; heavy civil, David Zachry CEO, founded 1924) | ✅ 2026-06-12 | [records-zachry-construction](records-zachry-construction.md) |

| Event attendees (not a company) | `Enlaye Notion/Events/apollo-contacts-export-9.csv` (89 → Paris BW Summit 2026) · `apollo-contacts-export-10.csv` (39 → SB Innovation Day) | ✅ 2026-06-10 | [records-event-imports](records-event-imports.md) |

**Profile pages exist but no dossier on disk yet** (template copies created 2026-06-09, awaiting research): Gilbane · Suffolk. When a dossier arrives: add its row above → create the ledger → run `/notion-load`.

**Prompt that generates dossiers:** `Enlaye Notion/Internal tuff/COMPANY_RESEARCH_PROMPT.md` (+ working copies in `Enlaye Notion/Prompts/`). Loading procedure: [playbook/research-load-prompt.md](../playbook/research-load-prompt.md) or the `/notion-load` skill.
