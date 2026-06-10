# Playbook · Pre-Write Safety (§8)

> **Holds:** the safety protocol to run before any structural Notion change. Zack is safety-alert and will catch destructive ops — flag them first.
> **Part of:** [PLAYBOOK.md](../../PLAYBOOK.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [loop-and-dedup](loop-and-dedup.md) · [schemas](schemas.md) · [conventions](conventions.md) · [recipes](recipes.md) · [notion-mcp](notion-mcp.md)
> **Related:** `replace_content` / nested-DB mechanics in [notion-mcp](notion-mcp.md); pages that host live DBs in [state/pages.md](../state/pages.md).

## 8. Pre-write safety protocol (run before any structural Notion change)
1. **List operations:** before touching anything, write out every planned operation — property adds, view creates, relation links, etc.
2. **Flag destructive steps:** bold any operation that could overwrite or delete existing data (`replace_content`, new databases, column removals).
3. **Wait for confirmation:** do not execute until Zack approves the plan.
4. **Never `replace_content` a page that hosts a live database** — use `update_content` surgical edits instead. Check `notion-fetch` ancestry first.
5. **Prefer additive:** linked views and new filtered tables over restructuring or creating new databases.
