# State · Databases

> **Holds:** the live database registry (IDs, URLs, purpose) + the Owners schema and template page.
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md)
> **Siblings:** [records-harvard](records-harvard.md) · [records-consigli](records-consigli.md) · [pages](pages.md) · [open-tasks](open-tasks.md)
> **Related:** full field schemas in [playbook/schemas.md](../playbook/schemas.md).

> **Path:** Sales → Market Research → Zack Projects (Notion workspace).
>
> **How to use these entries:**
> - `Data source ID` — pass to `notion-update-data-source`, `notion-fetch`, property writes, and schema reads. This is the MCP handle.
> - `Page URL` — use for navigation or linking. Opens the database view in Notion. Not an API endpoint.
> - When in doubt about a field schema, call `notion-fetch` on the Page URL to inspect live properties before writing.

| Database | Purpose | Data source ID | Page URL | Last verified |
|---|---|---|---|---|
| Owners | Owner organizations (universities, hospitals, govt, developers). Outreach pipeline for Enlaye. | `collection://37990644-d524-80da-92f8-000b22169334` | https://app.notion.com/p/37990644d52480848882f285bd794889 | 2026-06-08 |
| Construction Projects | Active/past capital construction projects linked to Owners and GCs. Holds project value data. | `collection://4c8ed827-78b9-4d34-9cca-0c3548304199` | https://app.notion.com/p/17c90644d524808c86eae940f56c68b1 | 2026-06-08 |
| People | Contact/relationship records. Linked to Companies and Owners. | `collection://0b7ff339-0887-4bbf-a218-7f8d4ede89ef` | https://app.notion.com/p/17a90644d524807abc2bfedd86563c70 | 2026-06-08 |
| Companies (GCs) | General contractor company records. Full company database linked from Owners. | `collection://041b7f07-9564-4696-ae78-1b61b34df758` | https://app.notion.com/p/17a90644d5248038a9bddbfb2c59a644 | 2026-06-08 |

**Owners schema (Companies-style + owner fields):** `Owner` (title) · Description · Type · Size · Location · Website · LinkedIn · Priority · Status · Capital Program · Source · Last edited. Three two-way relations — `Projects` ↔ Construction Projects ("Owner") · `Key Contacts` ↔ People ("Owner") · `General Contractors` ↔ Companies ("Owners"). Rollups: `Project Count`, `Total Project Value` (sum of Construction Projects' "Contrat Value in Million"). Full table in [playbook/schemas.md](../playbook/schemas.md).
**Owners template page:** "⟨Owner Name⟩ — TEMPLATE" → https://app.notion.com/p/37990644d5248109a665dc6b1da594d3. Body mirrors the Companies template (Description · Comments · Where we loose/win · Needs/Opportunities). Regular row; convert to native template via ••• → Turn into template.
