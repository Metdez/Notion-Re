# Batch-05 Company → pageID cache (A05)

Resolved existing Companies-DB records. Use these for the Company relation on people.

| Company string (CSV) | Resolved record | pageID |
|---|---|---|
| Kiewit (+ Kiewit Power Engineers, Kiewit Infrastructure West, Kiewit Building Group, Kiewit Energy Company, Kiewit Power Delivery, Kiewit Nuclear) | Kiewit | 17b90644-d524-8055-88ec-f7f399f27e9d |
| Alberici Constructors | Alberici Constructors, Inc. | 37b90644-d524-8129-8d57-fbca3d20307b |
| The Middlesex Corporation | The Middlesex Corporation | 1ce90644-d524-809e-ab40-e6e6c0a21c76 |
| Gilbane Building Company / Gilbane Building | Gilbane | 17b90644-d524-808d-b137-f747f6931e22 |
| KBE Building Corporation | KBE Building Corporation | 1cf90644-d524-802a-ac06-ea175f0df1fe |
| Consigli Construction Co., Inc. | Consigli Building Group | 19990644-d524-801a-a283-e806cb9b69b1 |
| Shawmut Design and Construction | Shawmut Design and Construction | 19990644-d524-8021-a4a6-f0a6321589f6 |
| Bechtel Corporation / Bechtel Oil Gas & Chemicals / Bechtel Energy Inc | Bechtel Group | 18490644-d524-80ff-8307-e94405919579 |
| Bechtel Power | Bechtel Power | 2b590644-d524-8039-8fb4-ce11364a6bdc |
| Bechtel National, Inc. | Bechtel National | 30a90644-d524-8037-8b5f-e3134e999f7d |
| Zachry Group / Zachry Industrial, Inc. | Zachry Group | 37b90644-d524-813a-a37d-e8d13fa3c23d |
| Suffolk Construction | Suffolk Construction | 17b90644-d524-8044-9514-eda61dd449ae |

## Still to resolve (search when rate limit clears)
- HITT Contracting Inc.
- Sundt Construction
- Clayco
- FlatironDragados
- CIANBRO / Cianbro Corporation
- Branch (branchgroup.com)
- Dellbrook | JKS (dellbrookjks.com)
- O&G Industries, Inc. (ogind.com)
- Fontaine Bros., Inc. (fontainebros.com)

## Notes
- People schema: Name(title), Function(text), LinkedIn(url), Email(email), Company name(text), Company(relation→Companies), Location(multi_select, existing options ONLY).
- Location options include US states (Texas, Kansas, etc.), Boston, New York City, San Francisco, Miami, Washington DC, USA. Map "City, State, United States" → state option if it exists; metro areas → nearest state; else leave blank.
- Body: "## Role\n**Role**: <Job Title> · <Company>\nSource: Apollo CSV export (LinkedIn <url>)"
- Dedup key: LinkedIn URL normalized (lowercase, strip trailing /).
- RATE LIMIT is brutal (~1 call/30-60s). Process sequentially, single calls.
