<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# [https://www.consigli.com/](https://www.consigli.com/)

## ROLE \& PERSONA

You are a **Senior Construction GC Intelligence Analyst** doing business-development research for **Enlaye** — a B2B SaaS that sells **construction risk-management software** to **large General Contractors (GCs)**.

You understand how a large GC is actually structured: a parent company that operates through **divisions / business units / operating groups** (often split by *region* — e.g. "Northeast", "West" — and/or by *market sector* — e.g. healthcare, higher-ed, aviation, data centers), each running its own portfolio of projects with its own leadership and P\&L. You know where construction project data hides: company "our work"/portfolio pages, press releases, ENR rankings, permit portals, owner capital-project sites, trade press (ENR, Construction Dive, High-Profile, BD+C), and association rosters.

Your job: produce an **exhaustive, citation-backed intelligence dossier** on `{{COMPANY}}` — its corporate structure, divisions, project portfolio (mapped to the division running each one), industry footprint (events, memberships), and incumbent software stack. This drives BD targeting and competitive analysis for Enlaye.

---

## PRIMARY RESEARCH OBJECTIVE

Compile a complete, current, structured profile of `{{COMPANY}}` that answers — explicitly and with sources — these five questions:

1. **How many divisions / business units / operating groups does `{{COMPANY}}` have?**
2. **What are they?** (name, type, region/sector focus, office address, leadership)
3. **What projects belong to each division?**
4. **Which division is running each project?**
5. **What are the latest / most recent projects** (newest awards, groundbreakings, ongoing builds)?

Then enrich with: company firmographics, office/location footprint, industry events the company shows up at, trade-association memberships, and the construction software it currently uses.

The definitive starting point is the company's own site: `{{COMPANY_WEBSITE}}` (especially its "About", "Our Work"/"Projects", "Markets"/"Sectors", "Locations"/"Offices", and "News"/"Press" pages).

---

## DATA-COLLECTION DOCTRINE — READ FIRST  *(// [ADDED])*

This dossier exists to find **correlations** across a buyer's portfolio (which owners give repeat work, which delivery methods carry the most risk exposure, which partners recur, which divisions are scaling). Correlation is only possible on **raw, verifiable, atomic data**. Therefore:

- **Record facts, never judgments.** Capture the *number*, the *date*, the *address*, the *name*, the *classification* — never an opinion, ranking of importance, recommendation, or "what this means for Enlaye." (The single exception is the pre-existing `why_it_matters` field on events; do not add new interpretive fields anywhere.)
- **Every datum is atomic and sourced.** One fact = one value + one `source_url`. Do not bundle multiple facts into prose.
- **Never infer a hard number.** If a square footage, contract value, or date is not stated in a source, leave it `null` and log it in `gaps`. Do not estimate, average, or "reason out" a figure.
- **Derived fields are allowed only as arithmetic on already-sourced data** (e.g. `duration_months` = completion − NTP; `repeat_client` = owner appears on >1 project). Cite the inputs.
- **Prefer primary, machine-of-record sources** (permit portals, SAM.gov, OSHA, court dockets, owner CIP dashboards, SEC filings) over trade-press paraphrase. When both exist, capture both.
- **Geocode everything geocodable** (project sites, offices, owner HQs) to enable spatial correlation.
- Capture full **provenance + date of capture** so stale data can be re-pulled.

---

## SCOPE \& BOUNDARIES

**In scope**

- `{{COMPANY}}`'s corporate structure: parent entity, all divisions / business units / operating groups / regional offices / named subsidiaries.
- Every construction project where `{{COMPANY}}` is the GC / CM / builder — active and recently completed (last ~3 yrs). Map each to the division that runs it.
- Firmographics: HQ, founding year, revenue, employee count, ENR rank, ownership (private/public/ESOP/PE).
- Office/location footprint (all physical offices).
- Industry events the company sponsors/exhibits/attends (conferences, golf outings, association meetings).
- Trade-association memberships (AGC, ABC, DBIA, USGBC, sector groups, regional chapters).
- Incumbent construction software / tech stack (PM, BIM, estimating, field, risk).
- *// [ADDED]* Hard risk \& compliance data: safety record (EMR/TRIR/DART/OSHA), bonding \& surety capacity, insurance carriers/wrap-ups, litigation, mechanics liens, contractor licenses, certifications (ISO/MBE/WBE/DBE/8(a)).
- *// [ADDED]* Per-project hard attributes: full street address + parcel, delivery method, contract type, procurement route, full date set (announce → award → permit → groundbreak → NTP → top-out → substantial/actual completion), size metrics (SF, floors, units, beds, keys, acreage, height), permit numbers \& valuations, funding source, geographic hazard zone.
- *// [ADDED]* Relationship/correlation data: owner/client identity + profile (and repeat-client flag), joint-venture partners, full design team (AOR, design architect, structural/MEP/civil), key subcontractors, competing bidders from public bid tabs.
- *// [ADDED]* Buying-intent hard signals: open job-req counts by category (esp. risk/insurance, safety/EHS, project controls, VDC/BIM), tools named in job reqs, M\&A events, federal contract activity.

**Out of scope**

- LinkedIn posts and individual people/contacts (collected separately — do **not** spend research budget here).
- The company's own financial statements beyond headline revenue/employees.
- Projects where the company is only a subcontractor of an unrelated GC (note them, don't deep-research them).
- Marketing fluff, awards with no project substance.

**Depth required:** Exhaustive, not a summary. Prioritize depth and completeness over brevity. If you find a relevant data field not listed in the schema, include it under `extra`. Keep prose factual — no marketing language.

---

## SEARCH STRATEGY

### Phase 1 — Seed pages (crawl these first)

Fetch and fully extract these before broader searching. Replace the bracketed paths with the company's real URLs:

- `{{COMPANY_WEBSITE}}` — home + About / Company / History
- `{{COMPANY_WEBSITE}}/projects` or `/our-work` or `/portfolio` — the project list (paginate through ALL of it)
- `{{COMPANY_WEBSITE}}/markets` or `/sectors` or `/services` — reveals market-sector divisions
- `{{COMPANY_WEBSITE}}/locations` or `/offices` or `/contact` — reveals regional divisions + addresses
- `{{COMPANY_WEBSITE}}/news` or `/press` or `/insights` — recent project awards \& groundbreakings
- `{{COMPANY_WEBSITE}}/leadership` or `/team` — confirms division structure via org titles (e.g. "President, Northeast")
- *// [ADDED]* `{{COMPANY_WEBSITE}}/careers` or `/jobs` — open-req counts + named tools in postings reveal the real stack and which divisions are scaling
- *// [ADDED]* `{{COMPANY_WEBSITE}}/safety` — published EMR/TRIR/safety program data
- *// [ADDED]* `{{COMPANY_WEBSITE}}/subcontractors` or `/prequalification` — surety/bonding language, insurance requirements, software portals named


### Phase 2 — Deep search queries (run each, iterate until exhausted)

**Corporate structure \& divisions**

- `"{{COMPANY}}"` divisions OR "business units" OR "operating groups"
- `"{{COMPANY}}"` regional offices OR "office locations"
- `"{{COMPANY}}"` subsidiaries OR "family of companies" OR "operating companies"
- `"{{COMPANY}}"` "president of" OR "general manager" [region/sector] — org structure via titles
- `"{{COMPANY}}"` annual revenue OR employees OR "ENR rank" OR "ENR Top"

**Project discovery (map each to a division)**

- `"{{COMPANY}}"` project awarded OR "selected as general contractor" 2024 2025 2026
- `"{{COMPANY}}"` groundbreaking OR "tops out" OR "ribbon cutting" OR "breaks ground"
- `"{{COMPANY}}"` construction "general contractor" [city/state of each known office]
- `site:constructiondive.com OR site:enr.com OR site:bdcnetwork.com "{{COMPANY}}"`
- `"{{COMPANY}}"` building permit [each metro it operates in] 2024 2025 2026
- `"{{COMPANY}}"` "[market sector]" project (healthcare / higher education / data center / aviation / life sciences / multifamily)
- For each project found: `"[project name]" "{{COMPANY}}" contract value OR cost OR "$" million`

**Events**

- `"{{COMPANY}}"` sponsor OR exhibitor OR booth conference 2025 2026
- `"{{COMPANY}}"` AGC OR ABC OR DBIA event OR "golf outing" OR "annual meeting"
- [each region] construction conference OR trade show 2026 `"{{COMPANY}}"`

**Memberships**

- `"{{COMPANY}}"` member OR membership association (AGC, ABC, DBIA, USGBC, NAIOP, ULI, sector councils)
- `"{{COMPANY}}"` site:agc.org OR site:abc.org OR association member directory

**Existing software / tech stack**

- `"{{COMPANY}}"` Procore OR Autodesk OR Trimble OR Kahua OR Bluebeam OR Oracle Aconex OR Bentley
- `"{{COMPANY}}"` "powered by" OR "uses" OR case study construction software OR BIM OR "project management software"
- `"{{COMPANY}}"` careers OR job posting [software name] — job reqs reveal the real stack

**// [ADDED] Per-project hard attributes (run for EVERY named project)**

- `"[project name]"` delivery method OR "design-build" OR "CM at risk" OR "GMP" OR "lump sum"
- `"[project name]"` square feet OR stories OR floors OR units OR beds OR keys OR acres
- `"[project name]"` architect OR "designed by" OR "architect of record" OR structural engineer OR MEP
- `"[project name]"` joint venture OR "JV" OR "in partnership with" OR "design-build team"
- `"[project name]"` groundbreaking date OR "broke ground" OR "topped out" OR "notice to proceed" OR "substantial completion"
- `"[project name]"` LEED OR "net zero" OR WELL OR sustainability certification
- `"[city/county]"` building permit `"{{COMPANY}}"` valuation OR "project value" — permit number + APN
- `"[project name]"` bid OR "bid tabulation" OR "lowest responsible bidder" — competing bidders + bid amounts

**// [ADDED] Owner / client profiling (run for EVERY distinct owner found)**

- `"[owner name]"` headquarters OR revenue OR employees OR "owns" OR "operates" OR "portfolio"
- `"[owner name]"` capital projects OR "capital improvement plan" OR "request for proposals" OR "board approved"
- `"[owner name]"` public OR private OR REIT OR developer OR "health system" OR university OR "ticker"

**// [ADDED] Risk, safety, compliance \& financial hard data**

- `"{{COMPANY}}"` EMR OR "experience modification rate" OR TRIR OR DART OR "incident rate"
- `"{{COMPANY}}"` site:osha.gov inspection OR citation OR penalty
- `"{{COMPANY}}"` bonding capacity OR surety OR "single project limit" OR "aggregate bonding"
- `"{{COMPANY}}"` lawsuit OR "mechanics lien" OR claim OR "bid protest" OR litigation
- `"{{COMPANY}}"` MBE OR WBE OR DBE OR "8(a)" OR HUBZone OR SDVOSB OR "ISO 9001" OR "ISO 45001"
- `"{{COMPANY}}"` site:sam.gov OR UEI OR CAGE code
- `"{{COMPANY}}"` site:usaspending.gov OR FPDS contract award
- `"{{COMPANY}}"` acquired OR merger OR "has acquired" OR "joins" 2022 2023 2024 2025
- `"{{COMPANY}}"` site:[state] contractor license OR "license number" OR "license verification"
- `"{{COMPANY}}"` revenue 2021 2022 2023 2024 — build the multi-year trend, not one point


### Phase 3 — Gap-filling

After Phases 1–2, list every division, project, event, membership, or tool mentioned but not fully researched. Run targeted follow-ups for each. Do not stop until each gap is closed or explicitly marked unresolvable in `gaps`.

### Phase 4 — Hard-data public-record sources *(// [ADDED] — pull these so the new fields don't come back null)*

For each entity, hit the system-of-record directly. These return atomic, verifiable data:


| Data you need | Source of record |
| :-- | :-- |
| UEI, CAGE, NAICS, set-asides, active registration | **SAM.gov** |
| Federal contract awards (PIID, agency, value, dates, NAICS) | **USASpending.gov / FPDS** |
| OSHA inspections, citations, penalties, violation type | **OSHA Establishment Search (osha.gov/ords)** |
| Wage/safety enforcement | **DOL Enforcement Data (enforcedata.dol.gov)** |
| Contractor license \#, status, expiration, classification, bond | **State license boards** (e.g. CSLB-CA, CSLB look-alikes per state, DPOR-VA, TDLR-TX) |
| Entity ID, incorporation date, status, registered agent, officers | **State Secretary of State business registries** |
| Permit \#, valuation, issued date, scope, status | **County/municipal permit portals** (Accela, eTRAKiT, SagesGov, Socrata open-data) |
| Parcel APN, owner of record, lot size, assessed value | **County assessor / GIS parcel viewers** |
| Flood zone by address | **FEMA Flood Map Service Center (msc.fema.gov)** |
| Seismic design category by lat/lng | **USGS Seismic Design Maps / ASCE Hazard Tool** |
| Litigation, judgments, mechanics liens | **PACER, state court dockets, county recorder of deeds** |
| DUNS, corporate family tree, credit (Paydex), trade lines | **D\&B / OpenCorporates** |
| ENR Top 400 / Top Contractors rank + revenue history | **ENR archives / ENR.com lists** |
| Project value, schedule, delivery method, bid tabs, competing bidders | **Owner capital-project dashboards** (university/health-system/airport/DOT/GSA CIP pages) |
| Open req counts by category, named tools in postings | **Company careers page + Indeed / job aggregators** |
| Public-company financials, segment revenue, backlog | **SEC EDGAR** (10-K/10-Q, if public) |
| Project leads, values, stakeholders, bid dates | **Dodge / ConstructConnect / BidClerk** (if accessible) |


---

## DIVISION → PROJECT MAPPING (the core mechanic)

This is the most important and most error-prone part. For **every** project, determine which division runs it, using this evidence hierarchy (highest confidence first):

1. **Explicit:** the project page / press release names the division or office ("built by `{{COMPANY}}`'s Boston office", "`{{COMPANY}}` Healthcare division").
2. **Geographic:** the project's city/metro matches a single regional office's territory → assign to that regional division (confidence: medium).
3. **Sector:** the project's building type matches a named market-sector division → assign there (confidence: medium).
4. **Unresolved:** if no division can be tied, set `owning_division: null`, `confidence: "low"`, and add a note. Never guess silently.

Set each division's `division_count` to the real total. In Notion, a division is its own **company record** (Parent Company = `{{COMPANY}}`); the project links to it via the **`Owning Department`** relation.

---

## DATA FIELDS REQUIRED (per entity)

**Per division** — name · type (regional office / market-sector unit / subsidiary) · region or sector focus · office address (geocodable) · division leader (title only; people collected separately) · count of projects · source URL.
*// [ADDED]* founded year · office phone · states \& metros served · sectors served · division revenue ($M, if disclosed) · division employee count · active project count · aggregate active contract value ($M) · per-state license numbers.

**Per project** — name · status · type/sector · contract value (\$M, if disclosed) · scope one-liner · location(s) · start date · est. completion · **owning division** · owner/client · architect (text) · primary source + all sources · confidence.
*// [ADDED]* one- to two-sentence factual brief · full street address + lat/lng · parcel/APN · delivery method · contract type · procurement route · bonded (Y/N + bond value + surety) · prevailing wage (Y/N) · PLA (Y/N) · union project (Y/N) · square footage · floors · units · beds · keys · site acreage · height (ft) · sustainability target · **full date set** (announced, award, permit issued, groundbreaking, NTP, topping-out, substantial completion, actual completion) · derived duration (months) · permit number(s) + valuation + jurisdiction · **JV partners** · **full design team** (architect of record, design architect, structural, MEP, civil) · **key subcontractors** · **competing bidders** (from public bid tabs) · **structured owner object** (name, type, sector, address, NAICS, ticker, parent, 1–2 sentence profile, repeat-client flag) · funding source · FEMA flood zone · seismic design category · AHJ (city/county/state authority) · disclosed change orders · project-level claims/litigation · reported incidents · current phase.

**Per event** — name (+ "(YYYY)") · date · venue/place · location tags · what it is · audience · why it matters to BD · is the company confirmed attending or inferred.
*// [ADDED]* company role (sponsor / exhibitor / speaker / attendee) · sponsorship tier · booth number · recurrence (annual/one-off).

**Per membership** — association name · membership level (if stated) · URL · source.
*// [ADDED]* member since (year) · chapter · member/ID number · board or committee seat held (Y/N + role).

**Per software** — tool name · category (PM / BIM / estimating / field / risk / ERP) · evidence (job post / case study / press) · source.
*// [ADDED]* first-seen date · evidence URL (the exact posting/case study) · division(s) using it · deployment scope (enterprise / division / project-specific).

---

## OUTPUT — return ONE JSON object matching this schema exactly

Field names map to Notion. Use `null` for unknowns and log them in `gaps`. Dates ISO `YYYY-MM-DD`. Money = USD millions, number only (`50` = \$50M). Every value object carries a `source_url`. **All fields marked `// [ADDED]` are new hard-data extensions — populate them where sourceable, else `null` + log in `gaps`. New fields with no Notion mapping go to their named array or to `extra`.**

```json
{
  "company": {
    "name": "{{COMPANY}}",
    "description": { "value": "", "source_url": "" },
    "website": { "value": "", "source_url": "" },
    "linkedin_url": { "value": "", "source_url": "" },
    "hq_address": { "value": "", "lat": null, "lng": null, "source_url": "" },
    "size": { "value": "Mutlinational | Regional | Local | Start-up", "source_url": "" },
    "type": { "value": "Company | Joint Venture | Consultant | Government | ...", "source_url": "" },
    "bw_category": ["Builder | Owner | Developer | Design and Architecture | Advisor | ..."],
    "ownership": { "value": "private | public | ESOP | PE-backed", "source_url": "" },
    "founded": { "value": "", "source_url": "" },
    "revenue_usd_m": { "value": null, "year": null, "source_url": "" },
    "employees": { "value": null, "source_url": "" },
    "enr_rank": { "value": null, "list": "", "year": null, "source_url": "" },


    "// [ADDED] HARD FIRMOGRAPHIC IDENTIFIERS": "----",
    "legal_name": { "value": "", "source_url": "" },
    "former_names": [ { "name": "", "used_until_year": null, "source_url": "" } ],
    "dba_names": [ "" ],
    "duns_number": { "value": "", "source_url": "" },
    "uei_sam": { "value": "", "source_url": "" },
    "cage_code": { "value": "", "source_url": "" },
    "ein": { "value": "", "source_url": "" },
    "naics_codes": [ { "code": "", "description": "", "primary": false, "source_url": "" } ],
    "sic_codes": [ "" ],
    "state_of_incorporation": { "value": "", "source_url": "" },
    "incorporation_date": { "value": "", "source_url": "" },
    "state_entity_ids": [ { "state": "", "entity_id": "", "status": "", "source_url": "" } ],
    "stock_ticker": { "value": "", "exchange": "", "source_url": "" },
    "fiscal_year_end": { "value": "", "source_url": "" },


    "// [ADDED] FINANCIAL TREND (multi-year for correlation)": "----",
    "financials": {
      "revenue_history": [ { "year": null, "revenue_usd_m": null, "source_url": "" } ],
      "backlog_usd_m": { "value": null, "year": null, "source_url": "" },
      "enr_rank_history": [ { "list": "", "rank": null, "year": null, "source_url": "" } ],
      "segment_revenue": [ { "segment": "", "revenue_usd_m": null, "year": null, "source_url": "" } ],
      "credit": { "dnb_rating": "", "paydex": null, "source_url": "" }
    },


    "// [ADDED] BONDING & INSURANCE (risk-critical)": "----",
    "bonding": {
      "single_project_limit_usd_m": { "value": null, "source_url": "" },
      "aggregate_limit_usd_m": { "value": null, "source_url": "" },
      "surety_provider": { "value": "", "source_url": "" },
      "surety_am_best_rating": { "value": "", "source_url": "" }
    },
    "insurance": {
      "carriers": [ { "name": "", "line": "GL | builders risk | professional | workers comp", "source_url": "" } ],
      "wrap_up_programs": [ "OCIP | CCIP" ]
    },


    "// [ADDED] SAFETY RECORD (public, gold for risk software)": "----",
    "safety_record": {
      "emr": [ { "year": null, "value": null, "source_url": "" } ],
      "trir": [ { "year": null, "value": null, "source_url": "" } ],
      "dart": [ { "year": null, "value": null, "source_url": "" } ],
      "osha_recordables": [ { "year": null, "count": null, "source_url": "" } ],
      "osha_fatalities": [ { "year": null, "count": null, "source_url": "" } ],
      "osha_inspections": [ { "date": "", "citations": null, "penalty_usd": null, "violation_type": "", "source_url": "" } ],
      "safety_awards": [ { "name": "", "year": null, "issuer": "", "source_url": "" } ]
    },


    "// [ADDED] LITIGATION & LIENS": "----",
    "litigation_and_claims": [
      { "case_name": "", "court": "", "case_number": "", "filed_date": "", "type": "payment dispute | defect | injury | lien | bid protest | other", "status": "", "amount_usd": null, "counterparty": "", "source_url": "" }
    ],
    "mechanics_liens": [
      { "project": "", "jurisdiction": "", "amount_usd": null, "filed_date": "", "claimant": "", "source_url": "" }
    ],


    "// [ADDED] CERTIFICATIONS & LICENSES": "----",
    "certifications": [ { "name": "ISO 9001 | ISO 45001 | LEED firm | MBE | WBE | DBE | SBA 8(a) | SDVOSB | HUBZone", "issuer": "", "valid_until": "", "source_url": "" } ],
    "contractor_licenses": [ { "state": "", "license_number": "", "classification": "", "status": "active | expired", "expiration_date": "", "bond_amount_usd": null, "source_url": "" } ],
    "states_licensed": [ "" ],


    "// [ADDED] LABOR PROFILE": "----",
    "labor_profile": {
      "union_status": { "value": "union | open-shop | double-breasted", "source_url": "" },
      "self_perform_trades": [ { "trade": "", "source_url": "" } ],
      "trade_agreements": [ { "union": "", "trade": "", "source_url": "" } ]
    },


    "// [ADDED] M&A / STRUCTURAL CHANGE HISTORY": "----",
    "m_and_a_history": [
      { "event_type": "acquisition | merger | divestiture | rebrand", "date": "", "counterparty": "", "deal_value_usd_m": null, "resulting_division": "", "source_url": "" }
    ],


    "// [ADDED] HIRING SIGNALS (buying-intent, counts only — no opinion)": "----",
    "hiring_signals": {
      "open_reqs_total": { "value": null, "as_of_date": "", "source_url": "" },
      "open_reqs_by_category": [ { "category": "risk/insurance | safety/EHS | preconstruction | VDC/BIM | project controls | IT/software | field ops", "count": null, "source_url": "" } ],
      "named_tools_in_job_posts": [ { "tool": "", "req_title": "", "source_url": "" } ]
    },


    "// [ADDED] FEDERAL CONTRACTING (public via SAM/FPDS/USASpending)": "----",
    "federal_contracting": {
      "active_set_asides": [ "" ],
      "contract_vehicles": [ { "vehicle": "GSA Schedule | IDIQ | JOC | SEWP | other", "id": "", "source_url": "" } ],
      "fpds_awards": [ { "piid": "", "agency": "", "value_usd": null, "award_date": "", "naics": "", "source_url": "" } ]
    }
  },


  "division_count": 0,
  "divisions": [
    {
      "name": "",                          // -> Divisions DB `Division` (title)
      "type": "regional office | market-sector unit | subsidiary",
      "focus": { "value": "", "source_url": "" },   // region or sector served
      "address": { "value": "", "lat": null, "lng": null, "source_url": "" },  // -> `Adress` (place; note misspelling)
      "leader_title": { "value": "", "source_url": "" },   // title only — people collected separately
      "parent_company": "{{COMPANY}}",     // -> relation to Companies DB
      "project_names": [],                 // -> relation to Projects (cross-ref projects[].name)


      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "",
      "founded": { "value": "", "source_url": "" },
      "office_phone": { "value": "", "source_url": "" },
      "states_served": [ "" ],
      "metros_served": [ "" ],
      "sectors_served": [ "" ],
      "revenue_usd_m": { "value": null, "year": null, "source_url": "" },
      "employee_count": { "value": null, "source_url": "" },
      "active_project_count": { "value": null, "source_url": "" },
      "aggregate_active_value_usd_m": { "value": null, "source_url": "" },
      "license_numbers": [ { "state": "", "number": "", "source_url": "" } ]
    }
  ],


  "locations": [                           // -> Locations DB (office footprint)
    {
      "name": "",
      "address": { "value": "", "lat": null, "lng": null },
      "source_url": "",
      "// [ADDED]": "----",
      "office_type": "HQ | regional | satellite | yard/shop",
      "phone": "",
      "opened_date": "",
      "owning_division": ""
    }
  ],


  "projects": [                            // -> shared Construction Projects DB (filtered by Contractors = company)
    {
      "name": "",                          // -> `Name` (title)
      "status": "Not started | In progress | Done",   // -> `Status`
      "type": "Higher Education | Senior Living | Transportation | Mixed-Use Residential | Infrastructure",  // -> `Type` (extend if needed)
      "contract_value_usd_m": null,        // -> `Contrat Value in Million` (number; VERBATIM typo)
      "size_summary": "",                  // -> `Size` text, format: "<scope> | ≈$<val>M, role: <GC/CM>"
      "location": [],                      // -> `Location` multi-select (city + state, sometimes country)
      "start_date": "",                    // -> `Date`
      "est_completion": "",
      "owning_division": "",               // -> `Owning Department` relation == WHICH DIVISION RUNS IT
      "contractor": "{{COMPANY}}",         // -> `Contractors` relation (scopes project to this company)
      "owner_client": { "value": "", "source_url": "" },   // -> `Owner` relation
      "architect": { "value": "", "source_url": "" },      // text in body
      "is_recent": false,                  // newest projects flagged true
      "confidence": "high | medium | low",
      "source_url": "",
      "sources": [ { "title": "", "url": "", "primary": true } ],


      "// [ADDED] PROJECT IDENTITY & BRIEF": "----",
      "id": "",
      "brief": "",                         // 1–2 sentence FACTUAL scope, no marketing language
      "full_address": { "value": "", "lat": null, "lng": null, "source_url": "" },
      "parcel_apn": { "value": "", "source_url": "" },
      "jurisdiction": { "city": "", "county": "", "state": "", "ahj": "", "source_url": "" },
      "phase": "",                         // current phase if reported


      "// [ADDED] DELIVERY & CONTRACT (risk correlation)": "----",
      "delivery_method": { "value": "Design-Bid-Build | Design-Build | Progressive Design-Build | CM-at-Risk | CM-Agency | IPD", "source_url": "" },
      "contract_type": { "value": "GMP | Lump Sum | Cost-Plus | Unit Price | T&M", "source_url": "" },
      "procurement": { "value": "competitive bid | negotiated | RFP | RFQ | JOC | sole source", "source_url": "" },
      "bonded": { "value": null, "bond_value_usd_m": null, "surety": "", "source_url": "" },
      "prevailing_wage": { "value": null, "source_url": "" },
      "project_labor_agreement": { "value": null, "source_url": "" },
      "union_project": { "value": null, "source_url": "" },
      "funding_source": { "value": "private | municipal bond | state appropriation | federal grant | P3 | tax credit | mixed", "source_url": "" },


      "// [ADDED] SIZE METRICS (hard, sector-specific)": "----",
      "square_footage": { "value": null, "source_url": "" },
      "num_floors": { "value": null, "source_url": "" },
      "num_units": { "value": null, "source_url": "" },     // residential
      "num_beds": { "value": null, "source_url": "" },      // healthcare / senior living
      "num_keys": { "value": null, "source_url": "" },      // hospitality
      "site_acreage": { "value": null, "source_url": "" },
      "height_ft": { "value": null, "source_url": "" },
      "sustainability_target": { "value": "LEED Silver | LEED Gold | LEED Platinum | WELL | Net Zero | none", "source_url": "" },


      "// [ADDED] FULL DATE SET (ISO; derive duration only from sourced dates)": "----",
      "announced_date": "",
      "award_date": "",
      "permit_issued_date": "",
      "groundbreaking_date": "",
      "notice_to_proceed_date": "",
      "topping_out_date": "",
      "substantial_completion_date": "",
      "actual_completion_date": "",
      "duration_months": null,             // derived: NTP -> substantial completion


      "// [ADDED] PERMITS (public record)": "----",
      "permits": [ { "number": "", "jurisdiction": "", "type": "", "valuation_usd": null, "issued_date": "", "status": "", "source_url": "" } ],


      "// [ADDED] PARTNERS & TEAM (firm-to-firm correlation)": "----",
      "joint_venture_partners": [ { "firm": "", "role": "lead | partner", "source_url": "" } ],
      "design_team": {
        "architect_of_record": { "value": "", "source_url": "" },
        "design_architect": { "value": "", "source_url": "" },
        "structural_engineer": { "value": "", "source_url": "" },
        "mep_engineer": { "value": "", "source_url": "" },
        "civil_engineer": { "value": "", "source_url": "" }
      },
      "key_subcontractors": [ { "firm": "", "trade": "", "source_url": "" } ],
      "competing_bidders": [ { "firm": "", "bid_amount_usd_m": null, "source_url": "" } ],


      "// [ADDED] STRUCTURED OWNER / CLIENT (+ profile + repeat flag)": "----",
      "owner": {
        "id": "",
        "name": "",
        "type": "public | private | federal | state | municipal | REIT | developer | university | healthcare system | corporate | nonprofit",
        "sector": "",
        "address": { "value": "", "lat": null, "lng": null },
        "naics": "",
        "stock_ticker": "",
        "parent_entity": "",
        "profile": "",                     // 1–2 sentence FACTUAL: what the owner is / does / size
        "repeat_client": null,             // true if this owner appears on >1 project for {{COMPANY}}
        "source_url": ""
      },


      "// [ADDED] GEOGRAPHIC HAZARD (public, geocoded)": "----",
      "fema_flood_zone": { "value": "", "source_url": "" },
      "seismic_design_category": { "value": "", "source_url": "" },


      "// [ADDED] PROJECT-LEVEL RISK EVENTS (only if publicly reported)": "----",
      "change_orders_disclosed": [ { "amount_usd": null, "reason": "", "date": "", "source_url": "" } ],
      "project_claims_litigation": [ { "type": "", "amount_usd": null, "status": "", "source_url": "" } ],
      "reported_incidents": [ { "type": "safety | stop-work | OSHA | delay | failure", "date": "", "description": "", "source_url": "" } ]
    }
  ],


  "events": [                              // -> Events DB
    {
      "name": "",                          // -> `Event name` ("(YYYY)" suffix, plain text)
      "date": "",                          // -> `Date`
      "place": { "value": "", "address": "", "lat": null, "lng": null },  // -> `Place`
      "location_tags": [],                 // -> `Location tags` multi-select (state + city)
      "what_it_is": { "value": "", "source_url": "" },
      "audience": { "value": "", "source_url": "" },
      "why_it_matters": { "value": "", "source_url": "" },
      "company_attendance": "confirmed | inferred",   // -> relation to Companies DB
      "source_url": "",


      "// [ADDED] EVENT HARD DATA": "----",
      "company_role": "sponsor | exhibitor | speaker | attendee | host",
      "sponsorship_tier": "",
      "booth_number": "",
      "recurrence": "annual | biennial | one-off"
    }
  ],


  "memberships": [                         // -> Memberships DB (industry associations / trade orgs)
    {
      "association": "",
      "level": "",
      "url": "",
      "source_url": "",
      "// [ADDED]": "----",
      "member_since": "",
      "chapter": "",
      "member_id": "",
      "board_or_committee_seat": { "value": null, "role": "", "source_url": "" }
    }
  ],


  "existing_software": [                   // -> Existing Software DB (incumbent tech stack)
    {
      "company": "{{COMPANY}}",
      "software_used": [],                 // -> `Software used` multi: Procore | Autodesk | Trimble | Kahua | <extend>
      "category": "PM | BIM | estimating | field | risk | ERP",
      "evidence": "job post | case study | press | vendor site",
      "location": [],                      // -> `Location` multi: United States | France | Canada | <extend>
      "source_url": "",


      "// [ADDED] SOFTWARE HARD DATA": "----",
      "first_seen_date": "",
      "evidence_url": "",                  // exact posting / case study URL
      "used_by_division": [ "" ],
      "deployment_scope": "enterprise | division | project-specific"
    }
  ],


  "// [ADDED] CORRELATION ROLLUPS (computed only from sourced data above)": "============",
  "owners_clients": [
    { "id": "", "name": "", "type": "", "sector": "", "address": { "value": "", "lat": null, "lng": null }, "project_count": null, "project_names": [], "total_value_usd_m": null, "profile": "", "source_url": "" }
  ],
  "jv_partners_rollup": [
    { "firm": "", "project_count": null, "project_names": [], "source_url": "" }
  ],
  "design_partners_rollup": [
    { "firm": "", "discipline": "architect | structural | MEP | civil", "project_count": null, "project_names": [], "source_url": "" }
  ],
  "subcontractor_network": [
    { "firm": "", "trade": "", "project_count": null, "project_names": [], "source_url": "" }
  ],
  "competitors_rollup": [
    { "firm": "", "encountered_on": [], "source_url": "" }
  ],
  "portfolio_metrics": {
    "total_projects": null,
    "total_active_value_usd_m": null,
    "value_by_sector": [ { "sector": "", "count": null, "value_usd_m": null } ],
    "value_by_division": [ { "division": "", "count": null, "value_usd_m": null } ],
    "value_by_delivery_method": [ { "method": "", "count": null, "value_usd_m": null } ],
    "value_by_state": [ { "state": "", "count": null, "value_usd_m": null } ],
    "avg_project_value_usd_m": null,
    "avg_duration_months": null
  },


  "sources": [                             // -> Sources register DB (citation ledger)
    {
      "about": "",
      "url": "",
      "// [ADDED]": "----",
      "source_type": "company site | press | permit portal | SAM/FPDS | OSHA | court | owner CIP | ENR | SEC | job board | other",
      "date_captured": "",
      "publication_date": ""
    }
  ],


  "extra": {},                             // any relevant fields not in the schema
  "gaps": [ "facts that could not be sourced and were intentionally left null" ]
}
```


---

## VERBATIM NOTION QUIRKS (preserve exactly when writing to Notion)

- `Contrat Value in Million` — misspelled, number in \$M.
- `Adress` (Divisions/Locations) — one "d".
- `Website ` / `Tasks ` / `Competitor Involvement ` — trailing space (Companies DB).
- Size option `Mutlinational`, BW Category `Environnement` — misspelled options.
- Divisions are **company records** in the Companies DB (Parent Company set), not a field.
- `Owning Department` = division linkage; `Contractors` = company linkage. Both relate to the Companies DB.
- Projects live in ONE shared DB; each profile is a filtered view on `Contractors`.
- Existing Software options are a controlled list (Procore/Autodesk/Trimble/Kahua) — extend the multi-select before writing new tools.
- Empty shells today: **Memberships** (Name only), **Locations**, **Sources register** — structure defined here, no rows to mirror.
- *// [ADDED]* New fields above (safety, bonding, permits, owner profile, partners, rollups, portfolio_metrics) have **no existing Notion column** — write them to `extra`, or create the column/DB first, before mapping. Do not silently drop them.


## DATA SOURCE IDS (for the Notion write step)

| Section | Data source |
| :-- | :-- |
| Divisions (Company Map) | `collection://37690644-d524-8088-abd7-000b818a9b6b` |
| Events | `collection://37690644-d524-80cb-82b1-000b78799305` |
| Sources register | `collection://37690644-d524-805b-bdeb-000b6591168e` |
| Locations | `collection://37690644-d524-803c-b832-000b0ca49c9e` |
| Projects (shared) | `collection://4c8ed827-78b9-4d34-9cca-0c3548304199` |
| Memberships | `collection://37690644-d524-80b0-b5eb-000b53bf2cd2` |
| Existing Software | `collection://37690644-d524-804f-b966-000b34a1901b` |
| Companies (parent/divisions) | `collection://041b7f07-9564-4696-ae78-1b61b34df758` |

{
"company": {
"name": "Consigli Construction Co., Inc.",
"description": {
"value": "Consigli Construction Co., Inc. is a fifth-generation, family-owned construction manager and general contractor that has grown from a local masonry firm founded in 1905 in Milford, Massachusetts into one of the largest employee-owned construction managers in the Northeast and Mid-Atlantic, with more than 2,600 employees, 15 regional offices and over \$4.4 billion in annual construction volume.",[^1][^2]
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"website": {
"value": "https://www.consigli.com/",
"source_url": "https://www.consigli.com/"
},
"linkedin_url": {
"value": "https://www.linkedin.com/company/consigli-construction",
"source_url": "https://www.linkedin.com/company/consigli-construction"
},
"hq_address": {
"value": "72 Sumner Street, Milford, MA 01757",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/wp-content/uploads/2013/10/SAMPLE-Long-From-Agreement-CT.pdf"
},
"size": {
"value": "Mutlinational",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"type": {
"value": "Company",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"bw_category": [
"Builder"
],
"ownership": {
"value": "ESOP",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"founded": {
"value": "1905",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"revenue_usd_m": {
"value": 4400,
"year": null,
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"employees": {
"value": 2600,
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"enr_rank": {
"value": null,
"list": "",
"year": null,
"source_url": ""
},

    "// [ADDED] HARD FIRMOGRAPHIC IDENTIFIERS": "----",
    "legal_name": {
      "value": "Consigli Construction Co., Inc.",
      "source_url": "https://www.consigli.com/wp-content/uploads/2013/10/SAMPLE-Long-From-Agreement-CT.pdf"
    },
    "former_names": [],
    "dba_names": [],
    "duns_number": {
      "value": "",
      "source_url": ""
    },
    "uei_sam": {
      "value": "CJXKHZS1NVC5",
      "source_url": "https://www.sweetspot.so/markets/federal/contractors/consigli-construction-co-inc-cjxkhzs1nvc5/"
    },
    "cage_code": {
      "value": "1YUV8",
      "source_url": "https://www.sweetspot.so/markets/federal/contractors/consigli-construction-co-inc-cjxkhzs1nvc5/"
    },
    "ein": {
      "value": "",
      "source_url": ""
    },
    "naics_codes": [
      {
        "code": "236220",
        "description": "Commercial and Institutional Building Construction",
        "primary": true,
        "source_url": "https://www.sweetspot.so/markets/federal/contractors/consigli-construction-co-inc-cjxkhzs1nvc5/"
      }
    ],
    "sic_codes": [],
    "state_of_incorporation": {
      "value": "",
      "source_url": ""
    },
    "incorporation_date": {
      "value": "",
      "source_url": ""
    },
    "state_entity_ids": [],
    "stock_ticker": {
      "value": "",
      "exchange": "",
      "source_url": ""
    },
    "fiscal_year_end": {
      "value": "",
      "source_url": ""
    },
    
    "// [ADDED] FINANCIAL TREND (multi-year for correlation)": "----",
    "financials": {
      "revenue_history": [
        {
          "year": null,
          "revenue_usd_m": 4400,
          "source_url": "https://www.consigli.com/our-story/who-we-are/"
        }
      ],
      "backlog_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "enr_rank_history": [
        {
          "list": "ENR Top 100 Green Building Contractors",
          "rank": 15,
          "year": 2023,
          "source_url": "https://www.consigli.com/our-story/awards-rankings-2/"
        }
      ],
      "segment_revenue": [],
      "credit": {
        "dnb_rating": "",
        "paydex": null,
        "source_url": ""
      }
    },
    
    "// [ADDED] BONDING & INSURANCE (risk-critical)": "----",
    "bonding": {
      "single_project_limit_usd_m": {
        "value": null,
        "source_url": ""
      },
      "aggregate_limit_usd_m": {
        "value": null,
        "source_url": ""
      },
      "surety_provider": {
        "value": "",
        "source_url": ""
      },
      "surety_am_best_rating": {
        "value": "",
        "source_url": ""
      }
    },
    "insurance": {
      "carriers": [],
      "wrap_up_programs": []
    },
    
    "// [ADDED] SAFETY RECORD (public, gold for risk software)": "----",
    "safety_record": {
      "emr": [],
      "trir": [],
      "dart": [],
      "osha_recordables": [],
      "osha_fatalities": [],
      "osha_inspections": [],
      "safety_awards": []
    },
    
    "// [ADDED] LITIGATION & LIENS": "----",
    "litigation_and_claims": [],
    "mechanics_liens": [],
    
    "// [ADDED] CERTIFICATIONS & LICENSES": "----",
    "certifications": [],
    "contractor_licenses": [],
    "states_licensed": [],
    
    "// [ADDED] LABOR PROFILE": "----",
    "labor_profile": {
      "union_status": {
        "value": "",
        "source_url": ""
      },
      "self_perform_trades": [
        {
          "trade": "Carpentry",
          "source_url": "https://www.consigli.com/our-story/who-we-are/"
        },
        {
          "trade": "Laborers",
          "source_url": "https://www.consigli.com/our-story/who-we-are/"
        },
        {
          "trade": "Masonry",
          "source_url": "https://www.consigli.com/our-story/who-we-are/"
        }
      ],
      "trade_agreements": []
    },
    
    "// [ADDED] M&A / STRUCTURAL CHANGE HISTORY": "----",
    "m_and_a_history": [
      {
        "event_type": "acquisition",
        "date": "2009-01-01",
        "counterparty": "Kirchhoff Construction Management, Inc.",
        "deal_value_usd_m": null,
        "resulting_division": "Pleasant Valley, NY office",
        "source_url": "https://www.consigli.com/our-story/who-we-are/"
      },
      {
        "event_type": "strategic partnership",
        "date": "2019-01-01",
        "counterparty": "J. Benton Construction",
        "deal_value_usd_m": null,
        "resulting_division": "Caribbean operations",
        "source_url": "https://www.consigli.com/our-story/who-we-are/"
      },
      {
        "event_type": "acquisition",
        "date": "2024-09-15",
        "counterparty": "Lendlease’s New York & New Jersey construction operations (substantial portions)",
        "deal_value_usd_m": 1800,
        "resulting_division": "New York & New Jersey healthcare and life sciences work",
        "source_url": "https://www.consigli.com/cbg-completes-acquisition-of-lendleases-ny-and-nj-construction-operations/"
      }
    ],
    
    "// [ADDED] HIRING SIGNALS (buying-intent, counts only — no opinion)": "----",
    "hiring_signals": {
      "open_reqs_total": {
        "value": null,
        "as_of_date": "",
        "source_url": ""
      },
      "open_reqs_by_category": [],
      "named_tools_in_job_posts": [
        {
          "tool": "Procore",
          "req_title": "Project Engineer",
          "source_url": "https://seasonalworks.labor.ny.gov/pleasant-valley-ny/project-engineer/0AABF2CADD6D47AB9AE45913AE296CEF/job/"
        },
        {
          "tool": "Timberline / Sage",
          "req_title": "Project Engineer",
          "source_url": "https://seasonalworks.labor.ny.gov/pleasant-valley-ny/project-engineer/0AABF2CADD6D47AB9AE45913AE296CEF/job/"
        },
        {
          "tool": "Primavera P6",
          "req_title": "Project Engineer",
          "source_url": "https://seasonalworks.labor.ny.gov/pleasant-valley-ny/project-engineer/0AABF2CADD6D47AB9AE45913AE296CEF/job/"
        },
        {
          "tool": "Procore",
          "req_title": "Self-Perform Project Engineer",
          "source_url": "https://apply.workable.com/consigli-construction-1/j/43C1FC52CF/"
        },
        {
          "tool": "Bluebeam",
          "req_title": "Self-Perform Project Engineer",
          "source_url": "https://apply.workable.com/consigli-construction-1/j/43C1FC52CF/"
        },
        {
          "tool": "Sage",
          "req_title": "Self-Perform Project Engineer",
          "source_url": "https://www.tealhq.com/job/self-perform-project-engineer_7ea1acf770c1ed378bc44e84a24f188cfcb59"
        }
      ]
    },
    
    "// [ADDED] FEDERAL CONTRACTING (public via SAM/FPDS/USASpending)": "----",
    "federal_contracting": {
      "active_set_asides": [],
      "contract_vehicles": [],
      "fpds_awards": [
        {
          "piid": "W912DR23C0017",
          "agency": "U.S. Army Corps of Engineers (Baltimore District)",
          "value_usd": 83789463,
          "award_date": "2023-06-01",
          "naics": "236220",
          "source_url": "https://www.highergov.com/contract/W912DR23C0017/"
        },
        {
          "piid": "47PC0323C0001",
          "agency": "General Services Administration",
          "value_usd": 48376670,
          "award_date": "2023-03-01",
          "naics": "236220",
          "source_url": "https://www.usaspending.gov/award/CONT_AWD_47PC0323C0001_4740_-NONE-_-NONE-"
        },
        {
          "piid": "W912DS-26-C-A004",
          "agency": "U.S. Army Corps of Engineers (New York District)",
          "value_usd": 32322313,
          "award_date": "2026-02-10",
          "naics": "236220",
          "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/"
        }
      ]
    }
    },

"division_count": 31,
"divisions": [
{
"name": "Milford, MA Headquarters",
"type": "regional office",
"focus": {
"value": "Headquarters and regional office supporting projects across New England and the broader Northeast.",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"address": {
"value": "72 Sumner Street, Milford, MA 01757",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/wp-content/uploads/2013/10/SAMPLE-Long-From-Agreement-CT.pdf"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [
"Watervliet Arsenal Fire Station",
"Fort Meade UEPH Barracks Replacement",
"Lincoln Memorial Rehabilitation"
],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "milford-ma-hq",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "508-473-2580",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Boston, MA Office",
"type": "regional office",
"focus": {
"value": "Regional office supporting academic, healthcare, life sciences, commercial and institutional projects in Greater Boston and Massachusetts.",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"address": {
"value": "313 Congress Street, Boston, MA 02210",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "boston-ma",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "617-259-1007",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Hartford, CT Office",
"type": "regional office",
"focus": {
"value": "Regional office serving Connecticut markets including higher education and institutional projects.",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"address": {
"value": "100 Allyn Street, Hartford, CT 06103",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "hartford-ct",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "860-741-9850",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Portland, ME Office",
"type": "regional office",
"focus": {
"value": "Regional office serving Maine and northern New England.",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"address": {
"value": "15 Franklin Street, Portland, ME 04101",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "portland-me",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "207-773-3000",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Latham, NY Office (Albany area)",
"type": "regional office",
"focus": {
"value": "Regional office in New York’s Capital Region.",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"address": {
"value": "3 Lear Jet Lane, Suite 201S, Latham, NY 12110",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [
"Watervliet Arsenal Fire Station"
],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "latham-ny",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "518-621-3230",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Manchester, NH Office",
"type": "regional office",
"focus": {
"value": "Regional office in Manchester, New Hampshire.",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"address": {
"value": "875 Elm Street, Suite 3, Manchester, NH 03101",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "manchester-nh",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "603-696-6767",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Melville, NY Office (Long Island)",
"type": "regional office",
"focus": {
"value": "Regional office on Long Island, New York.",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"address": {
"value": "445 Broadhollow Road, Suite 418, Melville, NY 11747",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "melville-ny",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "646-679-3500",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "New Brunswick, NJ Office",
"type": "regional office",
"focus": {
"value": "Regional office in New Brunswick, New Jersey.",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"address": {
"value": "317 George Street, Suite 300, New Brunswick, NJ 08901",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "new-brunswick-nj",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "New York City, NY Office",
"type": "regional office",
"focus": {
"value": "Regional office serving New York City across academic, healthcare, corporate, residential and mixed-use markets.",
"source_url": "https://www.consigli.com/location/new-york-city/"
},
"address": {
"value": "1155 6th Ave, 12th Floor, New York, NY 10036",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "new-york-city-ny",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Pleasant Valley, NY Office (Hudson Valley)",
"type": "regional office",
"focus": {
"value": "Regional office in Pleasant Valley, New York, originating from the acquisition of Kirchhoff Construction Management.",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"address": {
"value": "199 West Road, Suite 100, Pleasant Valley, NY 12569",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [
"Fort Meade UEPH Barracks Replacement"
],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "pleasant-valley-ny",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "845-635-1800",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Providence, RI Office",
"type": "regional office",
"focus": {
"value": "Regional office in Providence, Rhode Island.",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"address": {
"value": "101 Dyer Street, Suite 2A, Providence, RI 02903",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "providence-ri",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "401-267-2140",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Durham, NC Office (Raleigh–Durham)",
"type": "regional office",
"focus": {
"value": "Regional office supporting Consigli’s expansion into North Carolina and the Raleigh–Durham market.",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"address": {
"value": "4819 Emperor Blvd., Suite 130, Durham, NC 27703",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "durham-nc",
"founded": {
"value": "2023",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"office_phone": {
"value": "984-489-7137",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "Washington, DC Office",
"type": "regional office",
"focus": {
"value": "Regional office supporting federal and institutional work in Washington, DC and the Mid-Atlantic.",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"address": {
"value": "1825 K Street NW, Suite 1000, Washington, DC 20006",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [
"Lincoln Memorial Rehabilitation"
],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "washington-dc",
"founded": {
"value": "2014",
"source_url": "https://www.consigli.com/our-story/who-we-are/"
},
"office_phone": {
"value": "202-800-2800",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},
{
"name": "White Plains, NY Office",
"type": "regional office",
"focus": {
"value": "Regional office in White Plains, New York.",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"address": {
"value": "50 Main Street, 3rd Floor, White Plains, NY 10606",
"lat": null,
"lng": null,
"source_url": "https://www.consigli.com/our-story/locations/"
},
"leader_title": {
"value": "",
"source_url": ""
},
"parent_company": "Consigli Construction Co., Inc.",
"project_names": [],
"// [ADDED] DIVISION HARD DATA": "----",
"id": "white-plains-ny",
"founded": {
"value": "",
"source_url": ""
},
"office_phone": {
"value": "",
"source_url": "https://www.consigli.com/our-story/locations/"
},
"states_served": [],
"metros_served": [],
"sectors_served": [],
"revenue_usd_m": {
"value": null,
"year": null,
"source_url": ""
},
"employee_count": {
"value": null,
"source_url": ""
},
"active_project_count": {
"value": null,
"source_url": ""
},
"aggregate_active_value_usd_m": {
"value": null,
"source_url": ""
},
"license_numbers": []
},

    {
      "name": "Academic",
      "type": "market-sector unit",
      "focus": {
        "value": "Academic market sector delivering K–12 and higher education projects.",
        "source_url": "https://www.consigli.com/our-work/all-markets/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-academic",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Academic"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Advanced Technology",
      "type": "market-sector unit",
      "focus": {
        "value": "Advanced Technology market delivering smart factory and critical infrastructure projects.",
        "source_url": "https://www.consigli.com/our-work/all-markets/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-advanced-technology",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Advanced Technology"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Corporate",
      "type": "market-sector unit",
      "focus": {
        "value": "Corporate market sector delivering workplaces and corporate interiors.",
        "source_url": "https://www.consigli.com/our-work/all-markets/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-corporate",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Corporate"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Energy (Arch Energy)",
      "type": "market-sector unit",
      "focus": {
        "value": "Energy and decarbonization projects delivered through Arch Energy, focusing on high-performance buildings and low-carbon infrastructure.",
        "source_url": "https://www.consigli.com/our-work/all-markets/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-energy",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Energy"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Federal",
      "type": "market-sector unit",
      "focus": {
        "value": "Federal market sector delivering secure, durable facilities for federal agencies.",
        "source_url": "https://www.consigli.com/our-work/all-markets/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [
        "Fort Meade UEPH Barracks Replacement",
        "Watervliet Arsenal Fire Station",
        "Lincoln Memorial Rehabilitation"
      ],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-federal",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Federal"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Healthcare",
      "type": "market-sector unit",
      "focus": {
        "value": "Healthcare market sector delivering hospitals, medical centers and related facilities.",
        "source_url": "https://members.agcmass.org/list/member/consigli-construction-co-inc-milford-31"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-healthcare",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Healthcare"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Hotels & Hospitality",
      "type": "market-sector unit",
      "focus": {
        "value": "Hotels & Hospitality market sector delivering hospitality environments.",
        "source_url": "https://www.consigli.com/our-work/all-markets/page/2/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-hotels-hospitality",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Hotels & Hospitality"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Interiors",
      "type": "market-sector unit",
      "focus": {
        "value": "Interiors group delivering high-quality interior environments across markets.",
        "source_url": "https://www.consigli.com/our-work/all-markets/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-interiors",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Interiors"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Landmark Restoration",
      "type": "market-sector unit",
      "focus": {
        "value": "Landmark Restoration market sector focused on historic preservation and restoration.",
        "source_url": "https://www.consigli.com/our-work/all-markets/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [
        "Lincoln Memorial Rehabilitation"
      ],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-landmark-restoration",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Landmark Restoration"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Libraries",
      "type": "market-sector unit",
      "focus": {
        "value": "Libraries market sector delivering library projects from historic to modern facilities.",
        "source_url": "https://www.consigli.com/our-work/all-markets/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-libraries",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Libraries"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Life Sciences",
      "type": "market-sector unit",
      "focus": {
        "value": "Life Sciences market sector delivering laboratories, research and manufacturing facilities.",
        "source_url": "https://www.consigli.com/industry/life-sciences-construction/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-life-sciences",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Life Sciences"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Mission Critical",
      "type": "market-sector unit",
      "focus": {
        "value": "Mission Critical market sector focused on data centers and other facilities requiring continuous operation.",
        "source_url": "https://www.consigli.com/industry/mission-critical/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-mission-critical",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Mission Critical"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Multi-Family Residential",
      "type": "market-sector unit",
      "focus": {
        "value": "Multi-Family Residential market sector delivering residential and mixed-use housing.",
        "source_url": "https://www.consigli.com/our-work/all-markets/page/2/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-multi-family-residential",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Multi-Family Residential"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Museums & Cultural",
      "type": "market-sector unit",
      "focus": {
        "value": "Museums & Cultural market sector delivering cultural and museum facilities.",
        "source_url": "https://www.consigli.com/our-work/all-markets/page/2/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-museums-cultural",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Museums & Cultural"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Non-Profit Organizations",
      "type": "market-sector unit",
      "focus": {
        "value": "Non-Profit Organizations market sector delivering projects for nonprofit clients.",
        "source_url": "https://www.consigli.com/our-work/all-markets/page/2/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-non-profit-organizations",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Non-Profit Organizations"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    },
    {
      "name": "Special Projects",
      "type": "market-sector unit",
      "focus": {
        "value": "Special Projects group delivering smaller, fast-track and unique assignments.",
        "source_url": "https://www.consigli.com/market/special-projects/"
      },
      "address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "leader_title": {
        "value": "",
        "source_url": ""
      },
      "parent_company": "Consigli Construction Co., Inc.",
      "project_names": [],
      "// [ADDED] DIVISION HARD DATA": "----",
      "id": "market-special-projects",
      "founded": {
        "value": "",
        "source_url": ""
      },
      "office_phone": {
        "value": "",
        "source_url": ""
      },
      "states_served": [],
      "metros_served": [],
      "sectors_served": [
        "Special Projects"
      ],
      "revenue_usd_m": {
        "value": null,
        "year": null,
        "source_url": ""
      },
      "employee_count": {
        "value": null,
        "source_url": ""
      },
      "active_project_count": {
        "value": null,
        "source_url": ""
      },
      "aggregate_active_value_usd_m": {
        "value": null,
        "source_url": ""
      },
      "license_numbers": []
    }
    ],

"locations": [
{
"name": "Milford, MA Headquarters",
"address": {
"value": "72 Sumner Street, Milford, MA 01757",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "HQ",
"phone": "508-473-2580",
"opened_date": "",
"owning_division": "Milford, MA Headquarters"
},
{
"name": "Boston, MA Office",
"address": {
"value": "313 Congress Street, Boston, MA 02210",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "617-259-1007",
"opened_date": "2012-01-01",
"owning_division": "Boston, MA Office"
},
{
"name": "Hartford, CT Office",
"address": {
"value": "100 Allyn Street, Hartford, CT 06103",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "860-741-9850",
"opened_date": "2008-01-01",
"owning_division": "Hartford, CT Office"
},
{
"name": "Portland, ME Office",
"address": {
"value": "15 Franklin Street, Portland, ME 04101",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "207-773-3000",
"opened_date": "2003-01-01",
"owning_division": "Portland, ME Office"
},
{
"name": "Latham, NY Office",
"address": {
"value": "3 Lear Jet Lane, Suite 201S, Latham, NY 12110",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "518-621-3230",
"opened_date": "",
"owning_division": "Latham, NY Office (Albany area)"
},
{
"name": "Manchester, NH Office",
"address": {
"value": "875 Elm Street, Suite 3, Manchester, NH 03101",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "603-696-6767",
"opened_date": "",
"owning_division": "Manchester, NH Office"
},
{
"name": "Melville, NY Office",
"address": {
"value": "445 Broadhollow Road, Suite 418, Melville, NY 11747",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "646-679-3500",
"opened_date": "",
"owning_division": "Melville, NY Office (Long Island)"
},
{
"name": "New Brunswick, NJ Office",
"address": {
"value": "317 George Street, Suite 300, New Brunswick, NJ 08901",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "",
"opened_date": "",
"owning_division": "New Brunswick, NJ Office"
},
{
"name": "New York City, NY Office",
"address": {
"value": "1155 6th Ave, 12th Floor, New York, NY 10036",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "",
"opened_date": "",
"owning_division": "New York City, NY Office"
},
{
"name": "Pleasant Valley, NY Office",
"address": {
"value": "199 West Road, Suite 100, Pleasant Valley, NY 12569",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "845-635-1800",
"opened_date": "2009-01-01",
"owning_division": "Pleasant Valley, NY Office (Hudson Valley)"
},
{
"name": "Providence, RI Office",
"address": {
"value": "101 Dyer Street, Suite 2A, Providence, RI 02903",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "401-267-2140",
"opened_date": "",
"owning_division": "Providence, RI Office"
},
{
"name": "Durham, NC Office",
"address": {
"value": "4819 Emperor Blvd., Suite 130, Durham, NC 27703",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "984-489-7137",
"opened_date": "2023-01-01",
"owning_division": "Durham, NC Office (Raleigh–Durham)"
},
{
"name": "Washington, DC Office",
"address": {
"value": "1825 K Street NW, Suite 1000, Washington, DC 20006",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "202-800-2800",
"opened_date": "2014-01-01",
"owning_division": "Washington, DC Office"
},
{
"name": "White Plains, NY Office",
"address": {
"value": "50 Main Street, 3rd Floor, White Plains, NY 10606",
"lat": null,
"lng": null
},
"source_url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"office_type": "regional",
"phone": "",
"opened_date": "",
"owning_division": "White Plains, NY Office"
}
],

"projects": [
{
"name": "Fort Meade UEPH Barracks Replacement",
"status": "In progress",
"type": "Federal",
"contract_value_usd_m": 83.789463,
"size_summary": "Unaccompanied Enlisted Personnel Housing (UEPH) barracks replacement at Fort Meade, MD | ≈\$83.8M, role: GC/CM",
"location": [
"Fort Meade, MD"
],
"start_date": "",
"est_completion": "2025-03-12",
"owning_division": "Pleasant Valley, NY Office (Hudson Valley)",
"contractor": "Consigli Construction Co., Inc.",
"owner_client": {
"value": "U.S. Army Corps of Engineers",
"source_url": "https://www.highergov.com/contract/W912DR23C0017/"
},
"architect": {
"value": "",
"source_url": ""
},
"is_recent": true,
"confidence": "medium",
"source_url": "https://www.highergov.com/contract/W912DR23C0017/",
"sources": [
{
"title": "W912DR23C0017 – UEPH Barracks Replacement at Fort Meade, MD",
"url": "https://www.highergov.com/contract/W912DR23C0017/",
"primary": true
}
],
"// [ADDED] PROJECT IDENTITY \& BRIEF": "----",
"id": "proj-fort-meade-ueph",
"brief": "Firm-fixed-price contract to construct new unaccompanied enlisted personnel housing barracks at Fort Meade, Maryland, for the U.S. Army Corps of Engineers.",[^3]
"full_address": {
"value": "",
"lat": null,
"lng": null,
"source_url": ""
},
"parcel_apn": {
"value": "",
"source_url": ""
},
"jurisdiction": {
"city": "Fort Meade",
"county": "",
"state": "MD",
"ahj": "U.S. Army Corps of Engineers, Baltimore District",
"source_url": "https://www.highergov.com/contract/W912DR23C0017/"
},
"phase": "Construction",

      "// [ADDED] DELIVERY & CONTRACT (risk correlation)": "----",
      "delivery_method": {
        "value": "",
        "source_url": ""
      },
      "contract_type": {
        "value": "Lump Sum",
        "source_url": "https://www.highergov.com/contract/W912DR23C0017/"
      },
      "procurement": {
        "value": "competitive bid",
        "source_url": "https://www.highergov.com/contract/W912DR23C0017/"
      },
      "bonded": {
        "value": null,
        "bond_value_usd_m": null,
        "surety": "",
        "source_url": ""
      },
      "prevailing_wage": {
        "value": null,
        "source_url": ""
      },
      "project_labor_agreement": {
        "value": null,
        "source_url": ""
      },
      "union_project": {
        "value": null,
        "source_url": ""
      },
      "funding_source": {
        "value": "federal grant",
        "source_url": "https://www.highergov.com/contract/W912DR23C0017/"
      },
    
      "// [ADDED] SIZE METRICS (hard, sector-specific)": "----",
      "square_footage": {
        "value": null,
        "source_url": ""
      },
      "num_floors": {
        "value": null,
        "source_url": ""
      },
      "num_units": {
        "value": null,
        "source_url": ""
      },
      "num_beds": {
        "value": null,
        "source_url": ""
      },
      "num_keys": {
        "value": null,
        "source_url": ""
      },
      "site_acreage": {
        "value": null,
        "source_url": ""
      },
      "height_ft": {
        "value": null,
        "source_url": ""
      },
      "sustainability_target": {
        "value": "",
        "source_url": ""
      },
    
      "// [ADDED] FULL DATE SET (ISO; derive duration only from sourced dates)": "----",
      "announced_date": "",
      "award_date": "2023-06-01",
      "permit_issued_date": "",
      "groundbreaking_date": "",
      "notice_to_proceed_date": "",
      "topping_out_date": "",
      "substantial_completion_date": "",
      "actual_completion_date": "",
      "duration_months": null,
    
      "// [ADDED] PERMITS (public record)": "----",
      "permits": [],
    
      "// [ADDED] PARTNERS & TEAM (firm-to-firm correlation)": "----",
      "joint_venture_partners": [],
      "design_team": {
        "architect_of_record": {
          "value": "",
          "source_url": ""
        },
        "design_architect": {
          "value": "",
          "source_url": ""
        },
        "structural_engineer": {
          "value": "",
          "source_url": ""
        },
        "mep_engineer": {
          "value": "",
          "source_url": ""
        },
        "civil_engineer": {
          "value": "",
          "source_url": ""
        }
      },
      "key_subcontractors": [],
      "competing_bidders": [
        {
          "firm": "",
          "bid_amount_usd_m": null,
          "source_url": "https://www.highergov.com/contract/W912DR23C0017/"
        }
      ],
    
      "// [ADDED] STRUCTURED OWNER / CLIENT (+ profile + repeat flag)": "----",
      "owner": {
        "id": "owner-usace",
        "name": "U.S. Army Corps of Engineers",
        "type": "federal",
        "sector": "Defense",
        "address": {
          "value": "",
          "lat": null,
          "lng": null
        },
        "naics": "236220",
        "stock_ticker": "",
        "parent_entity": "U.S. Department of the Army",
        "profile": "The U.S. Army Corps of Engineers is a federal agency providing engineering and construction services for military and civil works programs.",
        "repeat_client": true,
        "source_url": "https://www.highergov.com/contract/W912DR23C0017/"
      },
    
      "// [ADDED] GEOGRAPHIC HAZARD (public, geocoded)": "----",
      "fema_flood_zone": {
        "value": "",
        "source_url": ""
      },
      "seismic_design_category": {
        "value": "",
        "source_url": ""
      },
    
      "// [ADDED] PROJECT-LEVEL RISK EVENTS (only if publicly reported)": "----",
      "change_orders_disclosed": [],
      "project_claims_litigation": [],
      "reported_incidents": []
    },
    {
      "name": "Watervliet Arsenal Fire Station",
      "status": "Not started",
      "type": "Federal",
      "contract_value_usd_m": 32.322313,
      "size_summary": "New two-story fire station building at Watervliet Arsenal, NY | ≈$32.3M, role: GC/CM",
      "location": [
        "Watervliet, NY"
      ],
      "start_date": "",
      "est_completion": "2028-03-08",
      "owning_division": "Latham, NY Office (Albany area)",
      "contractor": "Consigli Construction Co., Inc.",
      "owner_client": {
        "value": "U.S. Army Corps of Engineers, New York District",
        "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/"
      },
      "architect": {
        "value": "",
        "source_url": ""
      },
      "is_recent": true,
      "confidence": "medium",
      "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/",
      "sources": [
        {
          "title": "Contracts for Feb. 11, 2026 – Watervliet Arsenal Fire Station",
          "url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/",
          "primary": true
        }
      ],
      "// [ADDED] PROJECT IDENTITY & BRIEF": "----",
      "id": "proj-watervliet-fire-station",
      "brief": "Firm-fixed-price contract to construct a new two-story fire station building, including apparatus bays, dorm rooms and administrative spaces at Watervliet Arsenal, New York.",[^4]
      "full_address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "parcel_apn": {
        "value": "",
        "source_url": ""
      },
      "jurisdiction": {
        "city": "Watervliet",
        "county": "",
        "state": "NY",
        "ahj": "U.S. Army Corps of Engineers, New York District",
        "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/"
      },
      "phase": "Preconstruction",
    
      "// [ADDED] DELIVERY & CONTRACT (risk correlation)": "----",
      "delivery_method": {
        "value": "",
        "source_url": ""
      },
      "contract_type": {
        "value": "Lump Sum",
        "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/"
      },
      "procurement": {
        "value": "competitive bid",
        "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/"
      },
      "bonded": {
        "value": null,
        "bond_value_usd_m": null,
        "surety": "",
        "source_url": ""
      },
      "prevailing_wage": {
        "value": null,
        "source_url": ""
      },
      "project_labor_agreement": {
        "value": null,
        "source_url": ""
      },
      "union_project": {
        "value": null,
        "source_url": ""
      },
      "funding_source": {
        "value": "federal grant",
        "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/"
      },
    
      "// [ADDED] SIZE METRICS (hard, sector-specific)": "----",
      "square_footage": {
        "value": null,
        "source_url": ""
      },
      "num_floors": {
        "value": 2,
        "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/"
      },
      "num_units": {
        "value": null,
        "source_url": ""
      },
      "num_beds": {
        "value": null,
        "source_url": ""
      },
      "num_keys": {
        "value": null,
        "source_url": ""
      },
      "site_acreage": {
        "value": null,
        "source_url": ""
      },
      "height_ft": {
        "value": null,
        "source_url": ""
      },
      "sustainability_target": {
        "value": "",
        "source_url": ""
      },
    
      "// [ADDED] FULL DATE SET (ISO; derive duration only from sourced dates)": "----",
      "announced_date": "",
      "award_date": "2026-02-10",
      "permit_issued_date": "",
      "groundbreaking_date": "",
      "notice_to_proceed_date": "",
      "topping_out_date": "",
      "substantial_completion_date": "",
      "actual_completion_date": "",
      "duration_months": null,
    
      "// [ADDED] PERMITS (public record)": "----",
      "permits": [],
    
      "// [ADDED] PARTNERS & TEAM (firm-to-firm correlation)": "----",
      "joint_venture_partners": [],
      "design_team": {
        "architect_of_record": {
          "value": "",
          "source_url": ""
        },
        "design_architect": {
          "value": "",
          "source_url": ""
        },
        "structural_engineer": {
          "value": "",
          "source_url": ""
        },
        "mep_engineer": {
          "value": "",
          "source_url": ""
        },
        "civil_engineer": {
          "value": "",
          "source_url": ""
        }
      },
      "key_subcontractors": [],
      "competing_bidders": [
        {
          "firm": "",
          "bid_amount_usd_m": null,
          "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/"
        }
      ],
    
      "// [ADDED] STRUCTURED OWNER / CLIENT (+ profile + repeat flag)": "----",
      "owner": {
        "id": "owner-usace",
        "name": "U.S. Army Corps of Engineers",
        "type": "federal",
        "sector": "Defense",
        "address": {
          "value": "",
          "lat": null,
          "lng": null
        },
        "naics": "236220",
        "stock_ticker": "",
        "parent_entity": "U.S. Department of the Army",
        "profile": "The U.S. Army Corps of Engineers is a federal agency providing engineering and construction services for military and civil works programs.",
        "repeat_client": true,
        "source_url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/"
      },
    
      "// [ADDED] GEOGRAPHIC HAZARD (public, geocoded)": "----",
      "fema_flood_zone": {
        "value": "",
        "source_url": ""
      },
      "seismic_design_category": {
        "value": "",
        "source_url": ""
      },
    
      "// [ADDED] PROJECT-LEVEL RISK EVENTS (only if publicly reported)": "----",
      "change_orders_disclosed": [],
      "project_claims_litigation": [],
      "reported_incidents": []
    },
    {
      "name": "Lincoln Memorial Rehabilitation",
      "status": "In progress",
      "type": "Landmark Restoration",
      "contract_value_usd_m": 48.37667,
      "size_summary": "Rehabilitation of the Lincoln Memorial in Washington, DC | ≈$48.4M, role: GC/CM",
      "location": [
        "Washington, DC"
      ],
      "start_date": "",
      "est_completion": "",
      "owning_division": "Washington, DC Office",
      "contractor": "Consigli Construction Co., Inc.",
      "owner_client": {
        "value": "U.S. National Park Service (National Mall and Memorial Parks)",
        "source_url": "https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view"
      },
      "architect": {
        "value": "",
        "source_url": ""
      },
      "is_recent": true,
      "confidence": "medium",
      "source_url": "https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view",
      "sources": [
        {
          "title": "NAMA 216042 Lincoln Memorial Rehabilitation – Contract award",
          "url": "https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view",
          "primary": true
        }
      ],
      "// [ADDED] PROJECT IDENTITY & BRIEF": "----",
      "id": "proj-lincoln-memorial-rehab",
      "brief": "Firm-fixed-price contract to rehabilitate the Lincoln Memorial in Washington, DC under National Park Service contract NAMA 216042.",[^5]
      "full_address": {
        "value": "",
        "lat": null,
        "lng": null,
        "source_url": ""
      },
      "parcel_apn": {
        "value": "",
        "source_url": ""
      },
      "jurisdiction": {
        "city": "Washington",
        "county": "District of Columbia",
        "state": "DC",
        "ahj": "National Park Service",
        "source_url": "https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view"
      },
      "phase": "Construction",
    
      "// [ADDED] DELIVERY & CONTRACT (risk correlation)": "----",
      "delivery_method": {
        "value": "",
        "source_url": ""
      },
      "contract_type": {
        "value": "Lump Sum",
        "source_url": "https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view"
      },
      "procurement": {
        "value": "",
        "source_url": ""
      },
      "bonded": {
        "value": null,
        "bond_value_usd_m": null,
        "surety": "",
        "source_url": ""
      },
      "prevailing_wage": {
        "value": null,
        "source_url": ""
      },
      "project_labor_agreement": {
        "value": null,
        "source_url": ""
      },
      "union_project": {
        "value": null,
        "source_url": ""
      },
      "funding_source": {
        "value": "federal grant",
        "source_url": "https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view"
      },
    
      "// [ADDED] SIZE METRICS (hard, sector-specific)": "----",
      "square_footage": {
        "value": null,
        "source_url": ""
      },
      "num_floors": {
        "value": null,
        "source_url": ""
      },
      "num_units": {
        "value": null,
        "source_url": ""
      },
      "num_beds": {
        "value": null,
        "source_url": ""
      },
      "num_keys": {
        "value": null,
        "source_url": ""
      },
      "site_acreage": {
        "value": null,
        "source_url": ""
      },
      "height_ft": {
        "value": null,
        "source_url": ""
      },
      "sustainability_target": {
        "value": "",
        "source_url": ""
      },
    
      "// [ADDED] FULL DATE SET (ISO; derive duration only from sourced dates)": "----",
      "announced_date": "",
      "award_date": "",
      "permit_issued_date": "",
      "groundbreaking_date": "",
      "notice_to_proceed_date": "",
      "topping_out_date": "",
      "substantial_completion_date": "",
      "actual_completion_date": "",
      "duration_months": null,
    
      "// [ADDED] PERMITS (public record)": "----",
      "permits": [],
    
      "// [ADDED] PARTNERS & TEAM (firm-to-firm correlation)": "----",
      "joint_venture_partners": [],
      "design_team": {
        "architect_of_record": {
          "value": "",
          "source_url": ""
        },
        "design_architect": {
          "value": "",
          "source_url": ""
        },
        "structural_engineer": {
          "value": "",
          "source_url": ""
        },
        "mep_engineer": {
          "value": "",
          "source_url": ""
        },
        "civil_engineer": {
          "value": "",
          "source_url": ""
        }
      },
      "key_subcontractors": [],
      "competing_bidders": [],
    
      "// [ADDED] STRUCTURED OWNER / CLIENT (+ profile + repeat flag)": "----",
      "owner": {
        "id": "owner-nps",
        "name": "U.S. National Park Service",
        "type": "federal",
        "sector": "Parks and Historic Sites",
        "address": {
          "value": "",
          "lat": null,
          "lng": null
        },
        "naics": "",
        "stock_ticker": "",
        "parent_entity": "U.S. Department of the Interior",
        "profile": "The U.S. National Park Service manages national parks and historic sites, including the Lincoln Memorial on the National Mall in Washington, DC.",
        "repeat_client": false,
        "source_url": "https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view"
      },
    
      "// [ADDED] GEOGRAPHIC HAZARD (public, geocoded)": "----",
      "fema_flood_zone": {
        "value": "",
        "source_url": ""
      },
      "seismic_design_category": {
        "value": "",
        "source_url": ""
      },
    
      "// [ADDED] PROJECT-LEVEL RISK EVENTS (only if publicly reported)": "----",
      "change_orders_disclosed": [],
      "project_claims_litigation": [],
      "reported_incidents": []
    }
    ],

"events": [],

"memberships": [
{
"association": "Associated General Contractors of Massachusetts (AGC MA)",
"level": "Member",
"url": "https://members.agcmass.org/list/member/consigli-construction-co-inc-milford-31",
"source_url": "https://members.agcmass.org/list/member/consigli-construction-co-inc-milford-31",
"// [ADDED]": "----",
"member_since": "",
"chapter": "Massachusetts",
"member_id": "",
"board_or_committee_seat": {
"value": null,
"role": "",
"source_url": ""
}
}
],

"existing_software": [
{
"company": "Consigli Construction Co., Inc.",
"software_used": [
"Procore"
],
"category": "PM",
"evidence": "case study",
"location": [
"United States"
],
"source_url": "https://www.procore.com/casestudies/consigli",
"// [ADDED] SOFTWARE HARD DATA": "----",
"first_seen_date": "2023-02-21",
"evidence_url": "https://www.procore.com/casestudies/consigli",
"used_by_division": [
"Boston, MA Office",
"New York City, NY Office"
],
"deployment_scope": "enterprise"
},
{
"company": "Consigli Construction Co., Inc.",
"software_used": [
"Procore"
],
"category": "PM",
"evidence": "vendor site",
"location": [
"United States"
],
"source_url": "https://www.procore.com/network/p/consigli-construction-new-york",
"// [ADDED] SOFTWARE HARD DATA": "----",
"first_seen_date": "2024-08-18",
"evidence_url": "https://www.procore.com/network/p/consigli-construction-new-york",
"used_by_division": [
"New York City, NY Office"
],
"deployment_scope": "division"
},
{
"company": "Consigli Construction Co., Inc.",
"software_used": [
"Bluebeam"
],
"category": "field",
"evidence": "job post",
"location": [
"United States"
],
"source_url": "https://apply.workable.com/consigli-construction-1/j/43C1FC52CF/",
"// [ADDED] SOFTWARE HARD DATA": "----",
"first_seen_date": "",
"evidence_url": "https://apply.workable.com/consigli-construction-1/j/43C1FC52CF/",
"used_by_division": [],
"deployment_scope": "enterprise"
},
{
"company": "Consigli Construction Co., Inc.",
"software_used": [
"Sage"
],
"category": "ERP",
"evidence": "job post",
"location": [
"United States"
],
"source_url": "https://seasonalworks.labor.ny.gov/pleasant-valley-ny/project-engineer/0AABF2CADD6D47AB9AE45913AE296CEF/job/",
"// [ADDED] SOFTWARE HARD DATA": "----",
"first_seen_date": "",
"evidence_url": "https://seasonalworks.labor.ny.gov/pleasant-valley-ny/project-engineer/0AABF2CADD6D47AB9AE45913AE296CEF/job/",
"used_by_division": [],
"deployment_scope": "enterprise"
}
],

"// [ADDED] CORRELATION ROLLUPS (computed only from sourced data above)": "============",
"owners_clients": [
{
"id": "owner-usace",
"name": "U.S. Army Corps of Engineers",
"type": "federal",
"sector": "Defense",
"address": {
"value": "",
"lat": null,
"lng": null
},
"project_count": 2,
"project_names": [
"Fort Meade UEPH Barracks Replacement",
"Watervliet Arsenal Fire Station"
],
"total_value_usd_m": 116.111776,
"profile": "Federal engineering and construction agency delivering military and civil works projects for the U.S. Army and Department of Defense.",
"source_url": "https://www.highergov.com/contract/W912DR23C0017/"
},
{
"id": "owner-nps",
"name": "U.S. National Park Service",
"type": "federal",
"sector": "Parks and Historic Sites",
"address": {
"value": "",
"lat": null,
"lng": null
},
"project_count": 1,
"project_names": [
"Lincoln Memorial Rehabilitation"
],
"total_value_usd_m": 48.37667,
"profile": "Federal agency responsible for managing national parks and historic properties in the United States.",
"source_url": "https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view"
}
],
"jv_partners_rollup": [],
"design_partners_rollup": [],
"subcontractor_network": [],
"competitors_rollup": [],
"portfolio_metrics": {
"total_projects": 3,
"total_active_value_usd_m": 164.488446,
"value_by_sector": [
{
"sector": "Federal",
"count": 2,
"value_usd_m": 116.111776
},
{
"sector": "Landmark Restoration",
"count": 1,
"value_usd_m": 48.37667
}
],
"value_by_division": [
{
"division": "Pleasant Valley, NY Office (Hudson Valley)",
"count": 1,
"value_usd_m": 83.789463
},
{
"division": "Latham, NY Office (Albany area)",
"count": 1,
"value_usd_m": 32.322313
},
{
"division": "Washington, DC Office",
"count": 1,
"value_usd_m": 48.37667
}
],
"value_by_delivery_method": [],
"value_by_state": [
{
"state": "MD",
"count": 1,
"value_usd_m": 83.789463
},
{
"state": "NY",
"count": 1,
"value_usd_m": 32.322313
},
{
"state": "DC",
"count": 1,
"value_usd_m": 48.37667
}
],
"avg_project_value_usd_m": 54.829482,
"avg_duration_months": null
},

"sources": [
{
"about": "Company history, ownership and scale",
"url": "https://www.consigli.com/our-story/who-we-are/",
"// [ADDED]": "----",
"source_type": "company site",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Office locations and addresses",
"url": "https://www.consigli.com/our-story/locations/",
"// [ADDED]": "----",
"source_type": "company site",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Markets and sectors served",
"url": "https://www.consigli.com/our-work/all-markets/",
"// [ADDED]": "----",
"source_type": "company site",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Safety program overview (S.A.F.E.)",
"url": "https://www.consigli.com/approach/safety/",
"// [ADDED]": "----",
"source_type": "company site",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Subcontractor prequalification and use of iSqFt",
"url": "https://www.consigli.com/wp-content/uploads/2013/10/SAMPLE-Long-From-Agreement-CT.pdf",
"// [ADDED]": "----",
"source_type": "company site",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Awards and ENR Top 100 Green rank",
"url": "https://www.consigli.com/our-story/awards-rankings-2/",
"// [ADDED]": "----",
"source_type": "company site",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "LinkedIn company profile (markets, ESOP)",
"url": "https://www.linkedin.com/company/consigli-construction",
"// [ADDED]": "----",
"source_type": "other",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "AGC Massachusetts membership listing",
"url": "https://members.agcmass.org/list/member/consigli-construction-co-inc-milford-31",
"// [ADDED]": "----",
"source_type": "association",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Procore case study – enterprise deployment",
"url": "https://www.procore.com/casestudies/consigli",
"// [ADDED]": "----",
"source_type": "vendor site",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Procore Network – New York office",
"url": "https://www.procore.com/network/p/consigli-construction-new-york",
"// [ADDED]": "----",
"source_type": "vendor site",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Federal contractor identifiers and UEI/CAGE",
"url": "https://www.sweetspot.so/markets/federal/contractors/consigli-construction-co-inc-cjxkhzs1nvc5/",
"// [ADDED]": "----",
"source_type": "other",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Fort Meade UEPH Barracks replacement contract",
"url": "https://www.highergov.com/contract/W912DR23C0017/",
"// [ADDED]": "----",
"source_type": "USASpending/FPDS derivative",
"date_captured": "2026-06-10",
"publication_date": ""
},
{
"about": "Watervliet Arsenal Fire Station contract",
"url": "https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/",
"// [ADDED]": "----",
"source_type": "Department of Defense press",
"date_captured": "2026-06-10",
"publication_date": "2026-02-10"
},
{
"about": "Lincoln Memorial Rehabilitation contract",
"url": "https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view",
"// [ADDED]": "----",
"source_type": "SAM/FPDS",
"date_captured": "2026-06-10",
"publication_date": ""
}
],

"extra": {},
"gaps": [
"Division-level leadership titles (e.g., regional presidents or office heads) are not listed on the public site and remain unknown.",
"Division-level revenue, employee count, active project count and aggregate contract value are not disclosed.",
"Detailed project portfolio by division (all projects over last 3 years) is not fully accessible; only selected federal projects are captured here.",
"Per-project full street addresses, parcel/APN, and local permit numbers/valuations are not available for the sampled federal projects from the public summaries used.",
"Per-project delivery method, contract type beyond \"firm-fixed-price\", and procurement route are generally not specified in the high-level federal contract summaries.",
"Per-project size metrics (square footage, units, beds, acreage, height) are not provided in the sources reviewed for the sampled projects.",
"Per-project full date sets (announce, permit, groundbreaking, NTP, topping out, substantial and actual completion) are not disclosed in the sources used.",
"Per-project detailed design teams (architect of record, structural, MEP, civil) and key subcontractors are not named in the public federal award summaries used.",
"Competing bidders and bid tabulations are not provided in the publicly available summaries for the sampled federal contracts.",
"Company EMR, TRIR, DART and detailed OSHA recordables/fatalities are not published in the S.A.F.E. safety overview or other easily accessible sources.",
"Company bonding capacity (single-project and aggregate limits) and surety provider details are not disclosed publicly.",
"Corporate contractor license numbers, state license IDs and list of states licensed are not published centrally.",
"Event attendance (conferences, trade shows, golf outings) tied specifically to Consigli is not consistently documented in easily searchable public sources.",
"Trade-association memberships beyond AGC Massachusetts (e.g., other AGC chapters, ABC, DBIA, USGBC, NAIOP, ULI) are not comprehensively enumerated in one place.",
"Federal contracting rollup values reflect only a subset of available contracts and may not represent total current backlog.",
"Existing software stack beyond Procore, Bluebeam and Sage inferred from job posts and vendor case studies may include additional tools not captured here.",
"OSHA establishment search results for Consigli list inspections but individual inspection details were not extracted in this pass."
]
}
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^6][^60][^61][^62][^63][^64][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://www.consigli.com/our-story/who-we-are/

[^2]: https://www.linkedin.com/company/consigli-construction

[^3]: https://www.highergov.com/contract/W912DR23C0017/

[^4]: https://www.war.gov/News/Contracts/Contract/Article/4404316/contracts-for-feb-11-2026/

[^5]: https://sam.gov/opp/39d051a9e1d942f08a5e3bb3c36abb70/view

[^6]: https://pestel-analysis.com/blogs/brief-history/consigli

[^7]: https://www.consigli.com/cbg-completes-acquisition-of-lendleases-ny-and-nj-construction-operations/

[^8]: https://talents.vaia.com/companies/consigli-construction-co-inc/safety-manager-34114325/

[^9]: https://www.consigli.com/our-story/locations/

[^10]: http://consigliconstruction.com/eap/cc2428/ssp

[^11]: https://www.consigli.com/our-work/all-markets/

[^12]: https://www.consigli.com/wp-content/uploads/2013/10/SAMPLE-Long-From-Agreement-CT.pdf

[^13]: https://www.consigli.com/location/new-york-city/

[^14]: https://www.consigli.com/approach/safety/

[^15]: https://www.forbes.com/companies/consigli-construction/

[^16]: https://www.consigli.com/tag/new-jersey/

[^17]: https://jobs.workable.com/view/kKWjMyTuySZRxSj9pn9mHS/safety-manager-in-greenwich-at-consigli-construction

[^18]: https://www.consigli.com/character-builder-ceo-anthony-consigli-reflects-on-construction-industry-nyc-growth-in-commercial-observer/

[^19]: https://www.consigli.com/industry/life-sciences-construction/

[^20]: https://www.consigli.com/careers/our-people/

[^21]: https://www.consigli.com/industry/mission-critical/

[^22]: https://www.consigli.com/market/special-projects/

[^23]: https://www.consigli.com/approach/our-impact/

[^24]: https://www.consigli.com/our-story/giving-back/

[^25]: https://newworlddev.com/wp-content/uploads/2023/03/ConsigliConstruction-Caribbean.pdf

[^26]: https://www.consigli.com/consigli-is-a-best-place-to-work-in-all-offices/

[^27]: https://members.agcmass.org/list/member/consigli-construction-co-inc-milford-31

[^28]: https://careers.procore.com

[^29]: https://www.procore.com/network/p/consigli-construction-new-york

[^30]: https://www.linkedin.com/in/ian-maynard-69231a3b

[^31]: https://apply.workable.com/consigli-construction-1/j/43C1FC52CF/

[^32]: https://www.procore.com/network/p/consigli-and-associates-llc-new-york

[^33]: https://www.ziprecruiter.com/Jobs/Procore-Internship/--in-California

[^34]: https://www.consigli.com/careers/working-at-consigli/

[^35]: https://seasonalworks.labor.ny.gov/pleasant-valley-ny/project-engineer/0AABF2CADD6D47AB9AE45913AE296CEF/job/

[^36]: https://www.jobleads.com/us/job/vdc-manager-bim-revit-mep-coordination-lead--new-york--eb0be8d5b7d78401ef1a5b2cd624908a6

[^37]: https://www.tealhq.com/job/self-perform-project-engineer_7ea1acf770c1ed378bc44e84a24f188cfcb59

[^38]: https://pcn.procore.com/p/consigli-construction-boston

[^39]: https://www.facebook.com/ManufactOnCorporation/mentions/

[^40]: https://www.bluebeam.com/company/careers/

[^41]: https://www.procore.com/casestudies/consigli

[^42]: https://remotescout24.com/en/job/7332498-69204179-cc1d-4c8e-8271-d7ca660e4a87

[^43]: https://www.consigli.com/consigli-chosen-as-construction-manager-for-new-attleboro-high-school/

[^44]: https://builtworlds.com/companies/consigli-construction-co-inc/

[^45]: https://www.consigli.com/tag/k-12/

[^46]: https://www.consigli.com/consigli-again-honored-by-the-boston-globe-as-one-of-the-top-places-to-work/

[^47]: https://www.youtube.com/watch?v=EzOBKoOOaLM

[^48]: https://www.instagram.com/consigliconstruction/?hl=en

[^49]: https://topworkplaces.com/company/consigli-construction-co-inc/

[^50]: https://legislature.maine.gov/legis/bills/getTestimonyDoc.asp?id=172790

[^51]: https://acppubs.com/CER/article/1BA3782B-consigli-construction-celebrates-topping-out-at-4650-broadway-new-mixed-use-property-in-manhattan

[^52]: https://www.openspace.ai/resources/webinars/consigli-construction-revolutionizing-project-delivery-with-leading-edge-technology/

[^53]: https://www.linkedin.com/in/matthew-sliney-baa61960

[^54]: https://www.consigli.com/our-story/awards-rankings-2/

[^55]: https://www.sweetspot.so/markets/federal/contractors/consigli-construction-co-inc-cjxkhzs1nvc5/

[^56]: https://www.highergov.com/awardee/consigli-building-group-inc-10004810/

[^57]: https://www.osha.gov/ords/imis/establishment.search?establishment=CONSIGLI+CONSTRUCTION+CO\&p_logger=1

[^58]: https://www.highergov.com/awardee/consigli-construction-co-inc-10115750/

[^59]: https://www.consigli.com/wp-content/uploads/2017/02/SAMPLE-Long-From-Agreement-ME.pdf

[^60]: https://sam.gov/workspace/contract/opp/3371a4267f4a4f0f93c44ec2435f7c08/view

[^61]: https://www.usaspending.gov/award/CONT_AWD_47PC0323C0001_4740_-NONE-_-NONE-

[^62]: https://www.linkedin.com/in/sam-meyerhoff-8928326b

[^63]: https://www.cleat.ai/government/contractors/consigli-construction-co-inc-unby

[^64]: http://consigliconstruction.com/eap/cc507/ssp

