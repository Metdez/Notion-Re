# Playbook · The Write Gate (§12) — STOP before any Notion write

> **What this is:** the hard gate that runs before **any** Notion write — create *or* update, every task type (load, import, audit, one-off edit). Prose alone didn't stop the wrong-entity / canonical-edit disasters; this gate must be **shown to Zack and satisfied** before the write tool is called.
> **Read it:** the moment a task will write to Notion — before the first `notion-create-pages` / `notion-update-page` / `notion-update-data-source` / `notion-duplicate-page` call.
> **Write to it:** when a new write failure mode is found — add a check, keep it to one line.
> **Part of:** [PLAYBOOK.md](../../PLAYBOOK.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [loop-and-dedup](loop-and-dedup.md) (§0 step 4 routes here) · [safety](safety.md) (§8 structural changes) · [notion-mcp](notion-mcp.md)

---

## 12. The Write Gate (mandatory — no Notion write without passing it)

Before the **first** write of a task, state these four lines back to Zack with the real values filled in. Do not call a write tool until each is ✅. If any line cannot be made ✅, **stop and ask** — never guess.

1. **🎯 Identity confirmed.** Target = `<exact record name>` · ID `<page/data-source id>` · domain `<domain>`. Verified just now against **live Notion** (`notion-fetch` / `notion-search`), not from a brief, filename, or memory. *(Wrong-entity loads are the #1 disaster — walshbrothers.com ≠ walshgroup.com.)*
2. **➕ Additive only.** This write **adds** new sourced facts. It does **not** edit, overwrite, relink, or clear any preexisting field on an existing record. If an existing field looks wrong → I will **flag it**, not "fix" it.
3. **🔀 Distinct-entity check.** Any similarly-named record (shared surname, `.com` vs `.org`, parent vs subsidiary) is treated as a **different** entity until proven the same. I have not merged two distinct entities.
4. **🔁 Dedup done.** Ran [§1 dedup](loop-and-dedup.md) — searched state index + live Notion. Result: `<found→update / absent→create>`.

**Then, and only then,** call the write tool.

### One-liners that make the gate cheap
- **Re-confirm identity per target, not per task.** A batch that touches 5 companies passes line 1 five times. The cost of one `notion-fetch` is nothing next to a full revert.
- **`replace_content` and new databases stay behind the [§8 safety gate](safety.md)** too — the Write Gate is *in addition to*, not instead of, §8 for structural changes.
- **A failed write is fully reverted, never patched.** If a write lands wrong, undo it completely (Notion is additive-only / source-of-truth — see [USER_PREFS](../../USER_PREFS.md) data-hygiene), then re-run the gate.

---

## 12a. Long-run resilience (any multi-write run)

Applies to any run with many writes (bulk import, full dossier load, portfolio audit) — runs die mid-flight on spend limits / interrupts, and progress is lost.

- **Checkpoint before you start, update as you go.** Write a tiny progress file (last cursor / last record ID / counts) under `.tmp/` and update it every batch. On any interrupt, **resume from it** instead of restarting.
- **Batch into verifiable chunks.** Smaller batches = a clean resume point and a smaller blast radius if the gate was wrong.
- **Report the tail honestly.** End every run with created / updated / skipped / **remaining** counts. A halted run says so — never imply full coverage it didn't reach.
