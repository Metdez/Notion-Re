# Company Cache — canonical GC string → Notion pageID

> **What this is:** the ONE resolved map from a CSV `Company Name` to its existing Companies-DB record. Machine copy: [`_plan/company_ids.json`](_plan/company_ids.json) (same IDs).
> **Read it:** before resolving a person's Company relation — check here first, only search Notion if the company isn't listed.
> **Write to it:** when an agent resolves a new GC string to an existing record. Append a row; never duplicate an existing one.
> **Harness:** [README](README.md) · [BOARD](BOARD.md) · [agent-brief](agent-brief.md) · [excluded](excluded-not-in-notion.md) · registered in [records-bulk-import](../../context/state/records-bulk-import.md)

This replaces the per-agent scratch caches that had drifted apart ([`_a05_tmp/company-cache.md`](_a05_tmp/company-cache.md), [`ledgers/batch-12-company-cache.md`](ledgers/batch-12-company-cache.md), and inline caches in batch-04/07/09/11 ledgers) — those are kept as history but **this file + `_plan/company_ids.json` are the truth**.

## Resolved (24 GC records — core-name rule applied)
Variants / subsidiaries / JV tags map to the closest existing record. Match against these before any Notion search.

| CSV company string(s) → core name | Notion record | pageID |
|---|---|---|
| Bechtel, Bechtel Corporation, Bechtel Corp., Bechtel Enterprises Holdings, Bechtel Government Services, Bechtel Civil Infrastructure, Bechtel Oil Gas & Chemicals, Bechtel Energy Inc | Bechtel Group | `18490644-d524-80ff-8307-e94405919579` |
| Bechtel National, Bechtel National Inc | Bechtel National | `30a90644-d524-8037-8b5f-e3134e999f7d` |
| Bechtel Power, Bechtel Power Corporation | Bechtel Power | `2b590644-d524-8039-8fb4-ce11364a6bdc` |
| Kiewit, Kiewit Corporation, Kiewit Power/Infrastructure/Building/Energy/Nuclear/Power Delivery | Kiewit | `17b90644-d524-8055-88ec-f7f399f27e9d` |
| Zachry Group, Zachry Engineering, Zachry Industrial Inc., Zachry Holdings Inc. | Zachry Group | `37b90644-d524-813a-a37d-e8d13fa3c23d` |
| Gilbane Building Company, Gilbane Building, ITSI Gilbane Company | Gilbane | `17b90644-d524-808d-b137-f747f6931e22` |
| Suffolk Construction | Suffolk Construction | `17b90644-d524-8044-9514-eda61dd449ae` |
| Sundt Construction | Sundt | `22b90644-d524-8027-af9b-e3c3761a7fb7` |
| HITT Contracting Inc. | HITT | `30a90644-d524-80ef-a7d5-f533e2296b88` |
| Consigli Construction Co., Inc. | Consigli Building Group | `19990644-d524-801a-a283-e806cb9b69b1` |
| Clayco | Clayco | `19990644-d524-80e6-9107-fd693a9ad1e7` |
| Shawmut Design and Construction | Shawmut Design and Construction | `19990644-d524-8021-a4a6-f0a6321589f6` |
| FlatironDragados | FlatironDragados | `24690644-d524-8067-94e4-c40fbc9c089f` |
| The Middlesex Corporation | The Middlesex Corporation | `1ce90644-d524-809e-ab40-e6e6c0a21c76` |
| O&G Industries, Inc. | O&G Industries | `1cf90644-d524-80bf-9654-e76d70a3ad7d` |
| Dellbrook \| JKS | Dellbrook \| JKS | `19990644-d524-80ac-a13b-cdd8cd7a0946` |
| Cianbro, Cianbro Corporation, CIANBRO | Cianbro | `1cf90644-d524-8019-a5b9-d4d9851426fb` |
| Branch (branchgroup.com) | Branch Group | `26890644-d524-8050-83b7-e663089b3faf` |
| KBE Building Corporation | KBE Building Corporation | `1cf90644-d524-802a-ac06-ea175f0df1fe` |
| Fontaine Bros., Inc. | Fontaine Bros. | `19990644-d524-80cb-b37f-d7f58bc63bda` |
| Jingoli (J.J. White / Jingoli Nuclear Services) | Jingoli | `37b90644-d524-8127-824d-f2c6e9f55131` |

### Alberici — two valid records (disambiguate by string)
The earlier scratch caches mapped all Alberici strings to one ID; in Notion there are two. Map by the literal string:
| CSV company string | Notion record | pageID |
|---|---|---|
| Alberici, Alberici Corporation (parent / generic) | Alberici | `27990644-d524-802f-9f84-f3d1fc8af395` |
| Alberici Constructors, Inc. / Alberici Constructors (operating sub) | Alberici Constructors, Inc. | `37b90644-d524-8129-8d57-fbca3d20307b` |

> ⚠ If a row's intent is unclear, prefer the parent `Alberici` (`27990644`) — it matches the working-memory [records-alberici](../../context/state/records-alberici.md) ledger.

## Not in Notion → skip + log
Any company string that resolves to none of the above (after the core-name rule) is **skipped, not invented**. Append the person to [excluded-not-in-notion.md](excluded-not-in-notion.md) §C. Standing pre-flight exclusions (30) are already listed there.
