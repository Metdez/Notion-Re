# A03 company-name → Notion Companies pageID cache

Resolved (confirmed via Notion search of Companies DB collection://041b7f07-9564-4696-ae78-1b61b34df758):

| CSV company string(s) | Notion record | pageID |
|---|---|---|
| Kiewit / Kiewit Building Group Inc. | Kiewit | 17b90644-d524-8055-88ec-f7f399f27e9d |
| Clayco / Clayco, Inc. | Clayco | 19990644-d524-80e6-9107-fd693a9ad1e7 |
| Sundt Construction | Sundt | 22b90644-d524-8027-af9b-e3c3761a7fb7 |
| Suffolk Construction | Suffolk Construction | 17b90644-d524-8044-9514-eda61dd449ae |
| Shawmut Design and Construction | Shawmut Design and Construction | 19990644-d524-8021-a4a6-f0a6321589f6 |
| Bechtel Corporation / Bechtel / Bechtel Equipment Operations / Bechtel Oil Gas & Chemicals / Bechtel Oil and Gas / Bechtel Enterprises / Bechtel Civil Infrastructure | Bechtel Group (parent) | 18490644-d524-80ff-8307-e94405919579 |
| Bechtel National Inc | Bechtel National | 30a90644-d524-8037-8b5f-e3134e999f7d |
| Bechtel Power Corporation | Bechtel Power | 2b590644-d524-8039-8fb4-ce11364a6bdc |

| HITT Contracting Inc. | HITT | 30a90644-d524-80ef-a7d5-f533e2296b88 |
| Gilbane Building Company / Gilbane Building | Gilbane | 17b90644-d524-808d-b137-f747f6931e22 |
| Consigli Construction Co., Inc. / Consigli Construction | Consigli Building Group | 19990644-d524-801a-a283-e806cb9b69b1 |
| Zachry Group | Zachry Group | 37b90644-d524-813a-a37d-e8d13fa3c23d |

TO RESOLVE (search Companies DB; if no match → exclude §C):
- FlatironDragados / Flatiron Dragados (fdcorp.com)
- Alberici Constructors (alberici.com)
- CIANBRO (cianbro.com)
- O&G Industries, Inc. (ogind.com)
- Dellbrook | JKS (dellbrookjks.com)
- Branch (branchgroup.com)
- The Middlesex Corporation (middlesexco.com)

## Notes
- Notion MCP under heavy rate-limit (429 "try again in a few minutes"); pace ~1 call per interval.
- People DB import props: Name(title), Function(text=Job Title), Location(multi_select — pick nearest EXISTING US-state option, NEVER add), LinkedIn(url), Email(email if present), Company(relation pageID).
- Dedup key: LinkedIn URL normalized (lowercase, strip trailing /).
- Body: short sourced "## Role" line.
