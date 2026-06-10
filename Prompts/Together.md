# Company Research → Notion: Master Orchestration Prompt

**Target path:** Sales > Market Research > Zack Folder > Companies Research > `{{Company Name}}`

---

## PHASE 0 — ORIENT: Does Research Already Exist?

Before doing anything else, search Notion for an existing company research page.

```
notion-search: "{{Company Name}}" within Sales > Market Research > Zack Folder > Companies Research
```

**If a filled-out page already exists → skip to PHASE 3 (Audit Mode).**
**If the page does not exist, or exists but is empty/incomplete → proceed to PHASE 1 (Load Mode).**

The decision rule is simple: if there is substantive, populated data already in Notion for this company, you are in Audit Mode. If the slate is blank or thin, you are in Load Mode.

---

## PHASE 1 — LOAD MODE: Understand the Template

### Step 1A — Find and Read the Template

Navigate to: Sales > Market Research > Zack Folder > Companies Research

Look for the company template page. Read it in full — understand every field, every database relation, every property that is expected to be filled in:

- Company overview & description
- Divisions
- Locations & addresses
- People (contacts, executives, employees)
- Projects
- Software / tools they use
- Memberships / associations
- Contracts & engagements

If a page for `{{Company Name}}` does not yet exist, **duplicate the template** and rename it to the company name. Do not create from scratch — always clone the template so the structure is preserved.

### Step 1B — Read All Attached Research

Read every file, attachment, linked doc, or note the user has provided or that exists inside the company's folder. Extract and catalog:

| Category | What to Pull |
|----------|-------------|
| Company | Full legal name, DBA names, HQ address, founded date, industry, revenue if known, employee count |
| Description | 2–3 sentence executive summary — written for a busy executive who has 10 seconds |
| Divisions | All known business units, subsidiaries, regional offices |
| Locations | Every address — HQ, regional offices, project sites. City + State minimum |
| People | Name, title, division, location (matched by address where possible), contact info |
| Projects | Name, type, status, size, location, contract value, dates, contractor/owner |
| Software | Tools, platforms, tech stack they use or have purchased |
| Memberships | Industry associations, certifications, partnerships |
| Contracts | Any known engagements, vendor relationships, procurement history |

---

## PHASE 2 — LOAD MODE: Fan Out → Parallel Sub-Agents → Fan In

Once all research is extracted and cataloged, dispatch **parallel sub-agents** to load each data category simultaneously. Each sub-agent operates independently and reports back when complete.

### Orchestration Architecture

```
ORCHESTRATOR (this agent)
│
├── SUB-AGENT A: Company Profile + Divisions + Locations
│   └── Loads: company page properties, division records, address fields
│
├── SUB-AGENT B: People Directory
│   └── Loads: all contacts into People DB, links each person → company, division, location
│
├── SUB-AGENT C: Projects
│   └── Loads: all project records, links each → company, division, location, people
│
├── SUB-AGENT D: Software + Memberships + Contracts
│   └── Loads: tools/software, membership records, contract data, links all → company
│
└── [All sub-agents complete → FAN IN]
```

### Fan-In: Link Everything Together

After all sub-agents report completion, the orchestrator performs the final linking pass:

- Every **Person** → linked to their **Company**, their **Division**, and their **Location**
- Every **Division** → linked to the **Company** and its **Location(s)**
- Every **Project** → linked to the **Company**, the **Division** responsible, the **Location**, and any **People** involved
- Every **Software/Membership/Contract** → linked to the **Company** and the relevant **Division**
- Addresses matched wherever possible: if a person's listed address matches a company office, link them to that location record

### Writing Standard — Executive Voice

Every description field must be written for an **extremely busy executive**:
- 2–3 sentences maximum
- Lead with what matters most (what they do, why it's relevant)
- Include hard numbers if available (revenue, headcount, projects, square footage)
- No filler phrases, no passive voice, no hedge words

**Example:**
> Turner Construction's Mid-Atlantic division operates out of Washington DC and manages $2B+ in annual construction volume across federal, healthcare, and higher education sectors. Key contacts include [Name], VP of Operations, and [Name], Director of Preconstruction. Active projects span 12 states with a concentration in DC metro institutional work.

---

## PHASE 3 — AUDIT MODE: Full Interlink Verification

> This phase runs whether you just completed a load OR were sent here because data already existed.

### Step 3A — Read Every Page and Database Record

Do not skim. Fetch and read:

1. The company's top-level page and all properties
2. Every linked Division record
3. Every linked Person record
4. Every linked Project record
5. Every linked Software / Membership / Contract record
6. All location/address fields on every record

Build a complete mental map of what exists and how it is (or isn't) connected.

### Step 3B — Fan Out → Parallel Audit Sub-Agents

Dispatch **parallel audit sub-agents**, each checking a specific dimension:

```
AUDIT ORCHESTRATOR
│
├── AUDIT SUB-AGENT 1: Relation Integrity
│   └── Are all people linked to a company? To a division? To a location?
│   └── Are all projects linked to a company? Division? Location? People?
│   └── Are all divisions linked back to the parent company?
│
├── AUDIT SUB-AGENT 2: Data Completeness
│   └── Does every record have an address / location?
│   └── Does every record have a date (projects: start/end; contacts: date added)?
│   └── Does every company/division/person have a description?
│
├── AUDIT SUB-AGENT 3: Cross-Reference Accuracy
│   └── Do people's addresses match known company offices? If so, are they linked?
│   └── Are project locations matching the correct division's geography?
│   └── Are software tools linked to the right divisions (not just the top-level company)?
│
└── [All audit sub-agents report findings → FAN IN]
```

### Step 3C — Fan In: Fix Everything Found

The orchestrator collects all audit findings and **fixes every issue immediately**. There is no "flag for later." If something is broken or missing:

- Missing relation → create it
- Missing address → populate it from available data or note "address unknown — needs verification"
- Missing date → populate from context or note "date unknown"
- Missing description → write one from available data
- Broken link → repair it
- Unlinked person → find their company and division from context and link them

**You are not done until every audit finding has been resolved.**

### Step 3D — Final Completeness Check

After all fixes are applied, do one final pass:

```
For every record in the company's ecosystem:
  ✓ Has a description (2–3 sentences, executive voice)
  ✓ Has an address / location linked
  ✓ Has at least one date field populated
  ✓ Is linked to the parent company
  ✓ Is linked to the correct division (if applicable)
  ✓ Related people, projects, and software are cross-linked
```

Only when every record passes all checks is the work complete.

---

## PHASE 4 — REPORT BACK

Deliver a structured summary to the user:

### What Was Done
- Mode triggered: Load or Audit (and why)
- Sub-agents dispatched: how many, what each handled
- Records created: list with links
- Records updated: list with what changed
- Links established: summary count ("47 relations created")

### What Was Already There (Audit Mode)
- What was already correct and required no changes
- What was missing or broken and has now been fixed

### Attention Required
- Any data points that could not be populated from available research (requires human input)
- Conflicting data encountered (noted with both versions)
- Addresses or dates that could not be determined

### Quick Links
Direct links to the company page, key division records, and the People directory for this company.

---

## Execution Rules — Non-Negotiable

1. **Update first, create only when necessary.** If a record exists, update it. Never duplicate.
2. **Check for duplicates before every create.** Search by name before creating any person, project, division, or company record.
3. **Additive, never destructive.** Never delete existing content. Add, update, annotate — never remove.
4. **Date-stamp all updates.** When changing an existing value, preserve the old value with a date: `"45 employees *(updated June 2026; previously ~40)*"`
5. **Every sub-agent reports completion before the orchestrator fans in.** No partial fan-in.
6. **Descriptions are mandatory.** No record is complete without a 2–3 sentence executive description.
7. **Every fix must be applied.** Audit findings are not suggestions. Everything identified must be corrected before reporting done.
8. **All data must flow.** People → Divisions → Company. Projects → Divisions → Company → Locations. Software → Company → Divisions. The full graph must be connected.

Do all do not be lazy /goal

Read: 