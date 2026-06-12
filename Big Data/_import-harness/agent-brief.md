# Agent Brief — one batch, one agent

You are **one** of up to 18 parallel import agents. You own **exactly one batch** and touch nothing else. Another agent may resume your batch later — so the ledger, not your memory, is the truth. Write to it constantly.

## Your inputs (the coordinator gives you these)
- **Batch:** `batch-NN`
- **Agent ID:** e.g. `A07`
- **Ledger:** `Big Data/_import-harness/ledgers/batch-NN.md`
- **Data:** the 5 CSV files in `Big Data/batch-NN/`

## The loop (inter-looping = always resumable)

1. **Claim.** Open your ledger. If `Status: done`, stop — already finished. Otherwise set `Agent`, `Status: in-progress`, `Heartbeat: <now>`. **Edit ONLY your own `batch-NN.md` ledger — never touch BOARD.md** (the coordinator owns it; 18 agents editing one file would clobber it).
2. **Find your place.** Read **Resume cursor**. Start at "Next up" — never re-import rows already past the cursor.
3. **Per record, in order:**
   - **Company must already exist — never create one.** Resolve the person's `Company Name` to an existing Companies-DB record: **check [company-cache.md](company-cache.md) first** (24 GCs already resolved), only search Notion if the string isn't there. Apply the core-name rule: a variant / subsidiary / JV tag maps to the existing parent or sub-record; Bechtel and Alberici each have several — match the closest. New resolution → append a row to the cache. **If no existing company matches, SKIP the person** and append a row to [excluded-not-in-notion.md](excluded-not-in-notion.md) §C. Do **not** create the person unlinked, do **not** create a company.
   - **Dedup-first on the person.** Follow the **`notion-bulk-import`** skill: search Notion before creating; if the person exists, enrich (additive only, fill empty fields); if not, create with the Company relation set. Never overwrite, never duplicate.
   - **Source every field.** Each value carries its inline source (the LinkedIn URL / the CSV export).
   - **Then immediately update the ledger:** bump the file's `x/N` count, advance `cursor: row R`, refresh `Heartbeat`. This is the "constantly updating" part — if you die mid-file, the next agent picks up at row R+1.
4. **File done.** Tick its `- [ ]` → `- [x]`, mark it `done`, append one Log line: `YYYY-MM-DD HH:MM · file · rows a–b · created X / updated Y / skipped Z`. Move cursor to the next file.
5. **Batch done.** When all 5 files are ticked, set `Status: done` in your ledger. Stop. (The coordinator reflects it on the BOARD.)

## Identity & dedup key
- **Key field = `LinkedIn Profile`** (column 9). Normalize: trim, lowercase, drop trailing `/`.
- If LinkedIn is blank → fall back to `Work Email` (column 24, lowercased) → else `Full Name | Company Name`.
- The cursor + this key make the import **idempotent**: a re-run skips anything already in Notion or already past the cursor.

## Column map (CSV → Notion)
| CSV column | Goes to |
|---|---|
| `Company Name` | Company relation (dedup in Company DB) |
| `Full Name` / `First` / `Last` | Person name |
| `Job Title`, `Headline` | Title / role |
| `Location` | Location |
| `Company Domain` | Company website (on the Company record) |
| `LinkedIn Profile` | Person LinkedIn (also the dedup key) |
| `Work Email` | Email |
| `Connections`, `Jobs Count`, `Summary` | Person enrichment fields |

> Match the **field formatting of existing People/Company records** — copy their structure, don't invent fields (per CLAUDE.md).

## Rules you cannot break
- **Stay in your lane.** Only ever edit your own `ledgers/batch-NN.md` (and append to `excluded-not-in-notion.md` §C). Never BOARD.md, never another batch's files — that's how 18 agents run with zero collisions.
- **Heartbeat or you're presumed dead.** No ledger change for ~3 min = the coordinator may relaunch your batch. That's fine — it resumes from your cursor.
- **Additive only.** No `replace_content`, no new databases (CLAUDE.md Notion Safety).
- **Blocked?** Don't guess. Set `Status: blocked`, write the reason in the Log, stop. A human picks it up.
