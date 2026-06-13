# Kiewit — 3rd dossier (PARTIAL — chat paste truncated)

> ⚠️ **PARTIAL CAPTURE — DO NOT LOAD AS-IS.** Pasted into chat 2026-06-12 and truncated at the 50,000-character message limit, mid-way through `projects[0]` (Calcasieu Pass). Dossier meta says **17 projects**; only a fragment of the first survived. Any sections after `projects` (people, events, memberships, software, sources, gaps) are missing entirely.
> **Complete sections captured below:** `dossier_meta` · `company` (incl. hiring_signals, federal_contracting) · all **28 divisions** · all **18 locations**.
> This is NEW research vs. `Kiewitt.md`/`Kiewitt1.md` (28 divisions vs 15/17 loaded; Calcasieu Pass, Texas LNG, Oklo Aurora, Trans Mountain, Oroville, Southeast Connector appear in neither disk file).
> **Action needed:** Zack to save the full JSON to disk (suggested name `Kiewitt2.md` in this folder), then run `/notion-load`. When the full file lands, delete this partial.
> Note: the paste contains a recurring syntax quirk — `"license_numbers": ]` (missing `[`) in every division — preserved verbatim; the full file may need the same cleanup tolerance.

```json
{
"dossier_meta": {
"company": "Kiewit",
"run_date": "2026-06-10",
"lookback_years": 7,
"variables_used": {
"region_hint": null,
"sector_focus": null,
"known_divisions": [],
"max_projects": "exhaustive"
},
"coverage": {
"divisions_found": 28,
"projects_found": 17,
"projects_fully_attributed": 12,
"sources_total": 30
}
},
"company": {
"name": "Kiewit",
"brief": "Kiewit Corporation (legal parent: Peter Kiewit Sons', Inc.) is a privately held, employee-owned construction and engineering organization headquartered in Omaha, Nebraska, founded in 1884. It operates across transportation, power, oil/gas/chemical, water/wastewater, building, industrial, mining, marine, and nuclear markets in the United States, Canada, and Mexico.",
"description": {
"value": "Kiewit Corporation is one of North America's largest privately held, employee-owned construction and engineering organizations. Founded in Omaha, Nebraska in 1884 as a masonry contracting firm, it delivers large-scale infrastructure, energy, and industrial projects across the United States, Canada, and Mexico through a decentralized network of subsidiaries and regional districts, reporting $18.2 billion in fiscal year 2025 revenue with approximately 34,500 craft and staff employees.",
"source_url": "https://www.kiewit.com"
},
"website": {
"value": "https://www.kiewit.com",
"source_url": "https://www.kiewit.com"
},
"linkedin_url": {
"value": "https://www.linkedin.com/company/kiewit",
"source_url": "https://www.linkedin.com/company/kiewit"
},
"hq_address": {
"value": "1550 Mike Fahey St., Omaha, NE 68102",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"size": {
"value": "Multinational",
"source_url": "https://www.kiewit.com"
},
"type": {
"value": "Company",
"source_url": "https://en.wikipedia.org/wiki/Kiewit_Corporation"
},
"bw_category": [
"Builder"
],
"ownership": {
"value": "private",
"source_url": "https://www.kiewit.com/about-us/"
},
"founded": {
"value": 1884,
"source_url": "https://www.kiewit.com/about-us/our-history/"
},
"revenue_usd_m": {
"value": 18200,
"year": 2025,
"source_url": "https://www.kiewit.com"
},
"employees": {
"value": 34500,
"year": 2025,
"source_url": "https://www.kiewit.com"
},
"enr_rank": {
"value": 4,
"list": "ENR Top 400 Contractors",
"year": 2026,
"source_url": "https://www.constructiondive.com/news/top-commercial-contractors-revenue-2026-enr/820930/"
},
"hiring_signals": {
"open_reqs_total": {
"value": 483,
"as_of_date": "2026-06-10",
"source_url": "https://www.indeed.com/cmp/Kiewit-Corporation-cba042a0"
},
"open_reqs_by_category": [
{
"category": "Safety / EHS",
"count": 24,
"source_url": "https://kiewitcareers.kiewit.com/go/Kiewit_Safety/8156900/"
},
{
"category": "IT / Technology",
"count": 13,
"source_url": "https://kiewitcareers.kiewit.com/go/Kiewit_IT-Technology/8156500/"
},
{
"category": "VDC / BIM",
"count": 3,
"source_url": "https://kiewitcareers.kiewit.com/job/lone-tree-bim-specialist-kiewit-infrastructure-engineers-co-80112/1396774300"
}
],
"named_tools_in_job_posts": [
{
"tool": "InEight",
"req_title": "Project Controls Manager - Kiewit Power Constructors (Req 180281)",
"source_url": "https://kiewitcareers.kiewit.com/job/Lenexa-Project-Controls-Manager-Kiewit-Power-Constructors-KS/1380074800/"
},
{
"tool": "Primavera P6",
"req_title": "Project Controls Manager - Kiewit Power Constructors (Req 180281)",
"source_url": "https://kiewitcareers.kiewit.com/job/Lenexa-Project-Controls-Manager-Kiewit-Power-Constructors-KS/1380074800/"
},
{
"tool": "Autodesk Revit",
"req_title": "Field BIM Manager - Industrial (Req 180093)",
"source_url": "https://kiewitcareers.kiewit.com/job/Santa-Teresa-Field-BIM-Manager-Industrial-NM-88008/1374355100/"
},
{
"tool": "Autodesk Navisworks",
"req_title": "Field BIM Manager - Industrial (Req 180093)",
"source_url": "https://kiewitcareers.kiewit.com/job/Santa-Teresa-Field-BIM-Manager-Industrial-NM-88008/1374355100/"
},
{
"tool": "Autodesk BIM 360 / Autodesk Construction Cloud",
"req_title": "Field BIM Manager - Industrial (Req 180093)",
"source_url": "https://kiewitcareers.kiewit.com/job/Santa-Teresa-Field-BIM-Manager-Industrial-NM-88008/1374355100/"
},
{
"tool": "Bentley OpenRoads Designer",
"req_title": "BIM Specialist - Kiewit Infrastructure Engineers (Req 181025)",
"source_url": "https://kiewitcareers.kiewit.com/job/lone-tree-bim-specialist-kiewit-infrastructure-engineers-co-80112/1396774300"
},
{
"tool": "Autodesk Civil 3D",
"req_title": "CAD Engineer - Civil Infrastructure (Req 180157)",
"source_url": "https://kiewitcareers.kiewit.com/job/Lone-Tree-CAD-Engineer-Civil-Infrastructure-CO-80112/1380796500/"
},
{
"tool": "Bentley MicroStation",
"req_title": "Civil Designer - Digital Survey (Req 179879)",
"source_url": "https://kiewitcareers.kiewit.com/job/Lone-Tree-Civil-Designer-Digital-Survey-Kiewit-Infrastructure-Engineers-CO-80112/1368057200/"
},
{
"tool": "AutoCAD",
"req_title": "Civil Designer - Digital Survey (Req 179879)",
"source_url": "https://kiewitcareers.kiewit.com/job/Lone-Tree-Civil-Designer-Digital-Survey-Kiewit-Infrastructure-Engineers-CO-80112/1368057200/"
},
{
"tool": "Trimble Business Center",
"req_title": "Civil Designer - Digital Survey (Req 179879)",
"source_url": "https://kiewitcareers.kiewit.com/job/Lone-Tree-Civil-Designer-Digital-Survey-Kiewit-Infrastructure-Engineers-CO-80112/1368057200/"
},
{
"tool": "Trimble Access",
"req_title": "Surveyors and Crew Chiefs - Heavy Civil Construction (Req 180936)",
"source_url": "https://kiewitcareers.kiewit.com/job/Laredo-Surveyors-and-Crew-Chiefs-Heavy-Civil-Construction-TX/1394709400/"
},
{
"tool": "SAP / SmartMaterials",
"req_title": "Project Procurement Manager - Nuclear (Idaho Falls)",
"source_url": "https://kiewitcareers.kiewit.com/job/Idaho-Falls-Project-Procurement-Manager-ID/1393190700/"
}
]
},
"federal_contracting": {
"active_set_asides": [],
"contract_vehicles": [
{
"vehicle": "USACE Civil Works MACC (parent IDIQ of delivery order W912P523F0056)",
"id": "W912P523D0002",
"source_url": "https://www.usaspending.gov/award/CONT_AWD_W912P523F0056_9700_W912P523D0002_9700"
},
{
"vehicle": "NAVFAC IDIQ MACC for medical treatment facility renovation/repair/construction in AZ, CA, CO, HI, NM, NV ($1B shared ceiling, 8 years, awarded September 2022)",
"id": null,
"source_url": "https://www.executivebiz.com/articles/what-are-the-top-kiewit-government-contract-awards"
},
{
"vehicle": "NAVFAC Hawaii design-build/design-bid-build MACC ($990M shared IDIQ ceiling, 5 years, awarded January 2020)",
"id": null,
"source_url": "https://www.potomacofficersclub.com/articles/top-10-kiewit-corporation-government-contracts/"
}
],
"fpds_awards": [
{
"piid": "W912P523F0056",
"agency": "U.S. Army Corps of Engineers (Civil Works)",
"value_usd": 0.01,
"award_date": null,
"naics": null,
"source_url": "https://www.usaspending.gov/award/CONT_AWD_W912P523F0056_9700_W912P523D0002_9700"
},
{
"piid": null,
"agency": "U.S. Army Corps of Engineers (Anchorage, AK)",
"value_usd": 309.735,
"award_date": null,
"naics": null,
"source_url": "https://www.potomacofficersclub.com/articles/top-10-kiewit-corporation-government-contracts/"
},
{
"piid": null,
"agency": "U.S. Army Corps of Engineers (Honolulu, HI)",
"value_usd": 53.15,
"award_date": null,
"naics": null,
"source_url": "https://www.executivegov.com/articles/top-10-kiewit-government-contracts"
},
{
"piid": null,
"agency": "U.S. Army Corps of Engineers",
"value_usd": 40.502895,
"award_date": null,
"naics": null,
"source_url": "https://www.potomacofficersclub.com/articles/top-10-kiewit-corporation-government-contracts/"
},
{
"piid": null,
"agency": "U.S. Army Corps of Engineers",
"value_usd": 23.5,
"award_date": null,
"naics": null,
"source_url": "https://www.contractornews.com/622/kiewit-corporation-building-eight-massive-government-projects"
},
{
"piid": null,
"agency": "U.S. Army Corps of Engineers",
"value_usd": 136.6,
"award_date": null,
"naics": null,
"source_url": "https://www.contractornews.com/622/kiewit-corporation-building-eight-massive-government-projects"
},
{
"piid": null,
"agency": "NAVFAC",
"value_usd": 37.5,
"award_date": null,
"naics": null,
"source_url": "https://www.potomacofficersclub.com/articles/top-10-kiewit-corporation-government-contracts/"
}
]
}
},
"division_count": 28,
"divisions": [
{
"name": "Kiewit Infrastructure Co.",
"brief": "Operating subsidiary delivering heavy civil infrastructure including transportation, underground/tunneling, and transit work, organized into Central, Eastern, and Underground districts. It is the prime design-builder for the Francis Scott Key Bridge replacement in Baltimore.",
"type": "subsidiary",
"focus": {
"value": "Civil infrastructure construction - heavy civil, transportation, underground/tunneling, transit",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "1550 Mike Fahey St., 3rd Floor, Omaha, NE 68102",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [
"Francis Scott Key Bridge Replacement"
],
"id": "div-01",
"founded": null,
"office_phone": {
"value": "(402) 342-2052",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"NE",
"NJ",
"NY",
"NM",
"TN",
"IL",
"MD",
"DC"
],
"metros_served": [
"Omaha",
"New York City",
"Chicago",
"Baltimore"
],
"sectors_served": [
"Transportation",
"Underground/Tunneling",
"Transit"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Infrastructure West Co.",
"brief": "Operating subsidiary covering civil infrastructure construction in the western United States and Alaska, including Bridge & Marine, Northwest, Northern California, Southern California, and Southwest districts. It holds federal registration UEI YSNNL4FGAQ53 / CAGE 4TJJ4 with $1.18 billion in federal obligations across 20 awards.",
"type": "subsidiary",
"focus": {
"value": "Civil infrastructure construction in the western U.S. and Alaska, including bridge and marine work",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "2200 Columbia House Blvd, Vancouver, WA 98661",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [
"Oroville Dam Spillway Reconstruction",
"Ship Canal Water Quality Project",
"Mid-Coast Trolley Blue Line Extension",
"Federal Way Link Extension",
"Northwest Extension Phase II Light Rail"
],
"id": "div-02",
"founded": null,
"office_phone": {
"value": "(360) 693-1478",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"WA",
"OR",
"CA",
"AK",
"AZ",
"NV",
"UT",
"HI"
],
"metros_served": [
"Seattle",
"Vancouver WA",
"Sacramento",
"San Francisco Bay Area",
"Los Angeles",
"San Diego",
"Phoenix",
"Las Vegas",
"Salt Lake City",
"Honolulu",
"Anchorage"
],
"sectors_served": [
"Transportation",
"Transit",
"Bridge & Marine",
"Water",
"Dams"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Infrastructure South Co.",
"brief": "Operating subsidiary for civil infrastructure construction in the southern and southeastern United States, organized into Southeast and South Central districts. Its Tampa PIPES program won a 2025 DBIA Florida Region Design-Build Honor Award.",
"type": "subsidiary",
"focus": {
"value": "Civil infrastructure construction in the southern and southeastern U.S.",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "2050 Roanoke Rd., Suite 100, Westlake, TX 76262",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [
"Southeast Connector (I-20/I-820/US 287)"
],
"id": "div-03",
"founded": null,
"office_phone": {
"value": "(817) 337-7000",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"TX",
"FL",
"GA",
"MD",
"NC",
"SC"
],
"metros_served": [
"Dallas-Fort Worth",
"Tampa",
"Orlando",
"Fort Lauderdale",
"Atlanta",
"Raleigh",
"Charleston"
],
"sectors_served": [
"Transportation",
"Highway",
"Water",
"Flood Protection"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Engineering Group Inc.",
"brief": "Engineering subsidiary providing integrated engineering across all Kiewit markets, including infrastructure, power, water, oil/gas/chemical, and power delivery engineering, with more than 4,300 engineering professionals.",
"type": "subsidiary",
"focus": {
"value": "Integrated in-house engineering across infrastructure, power, water, OGC, and power delivery markets",
"source_url": "https://www.kiewit.com/services-and-solutions/engineering/"
},
"address": {
"value": "10055 Trainstation Circle, Lone Tree, CO 80124",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-04",
"founded": null,
"office_phone": {
"value": "(303) 325-0300",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"CO",
"KS",
"NE",
"NC",
"TX",
"OH",
"NY",
"VA",
"WA",
"OR"
],
"metros_served": [
"Denver",
"Kansas City",
"Omaha",
"Raleigh",
"Houston",
"New York City"
],
"sectors_served": [
"Engineering - all Kiewit markets"
],
"revenue_usd_m": null,
"employee_count": {
"value": 4300,
"source_url": "https://www.kiewit.com/services-and-solutions/engineering/"
},
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Power Constructors Co.",
"brief": "Operating subsidiary providing EPC services for power generation including gas-fired, renewables, and LNG-related power facilities; ranked #2 in ENR's Power category. It is the design-builder of the 4.5 GW Homer City Energy Campus in Pennsylvania.",
"type": "subsidiary",
"focus": {
"value": "EPC for power generation - fossil fuel, renewables",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "8900 Renner Blvd, Lenexa, KS 66219",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [
"Homer City Energy Campus 4.5 GW Natural Gas Plant"
],
"id": "div-05",
"founded": null,
"office_phone": {
"value": "(913) 928-7000",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"KS",
"OH",
"PA"
],
"metros_served": [
"Kansas City",
"Columbus",
"Pittsburgh"
],
"sectors_served": [
"Power Generation"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Power Delivery",
"brief": "Market unit delivering overhead and underground transmission, substation, and distribution projects, operating from offices including Lenexa KS, Woodcliff Lake NJ, Raleigh NC, San Diego CA, New Albany OH, and Portland OR.",
"type": "market-sector unit",
"focus": {
"value": "Overhead and underground transmission, substation, and distribution projects",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "8900 Renner Blvd, Lenexa, KS 66219",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-06",
"founded": null,
"office_phone": {
"value": "(913) 928-7000",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"KS",
"NJ",
"NC",
"CA",
"OH",
"OR"
],
"metros_served": [
"Kansas City",
"New York City",
"Raleigh",
"San Diego",
"Portland"
],
"sectors_served": [
"Power Delivery / Transmission & Distribution"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Energy Group Inc.",
"brief": "Operating subsidiary for oil, gas, and chemical construction and engineering, also housing Kiewit's Mexico operations. It executed the lump-sum turnkey EPC contract for the Texas LNG export terminal at the Port of Brownsville in March 2026.",
"type": "subsidiary",
"focus": {
"value": "Oil, gas and chemical (OGC) construction and engineering",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "585 N. Dairy Ashford Rd., Suite 100, Houston, TX 77079",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [
"Texas LNG Brownsville Export Terminal"
],
"id": "div-07",
"founded": null,
"office_phone": {
"value": "(281) 848-4800",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"TX",
"LA"
],
"metros_served": [
"Houston",
"The Woodlands"
],
"sectors_served": [
"Oil, Gas & Chemical",
"LNG"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Offshore Services, Ltd.",
"brief": "Subsidiary operating a 555-acre offshore fabrication yard in Ingleside, Texas, established in 1984, serving offshore oil and gas and offshore wind markets. It fabricated the first U.S. offshore topsides gas-insulated substation for South Fork Wind.",
"type": "subsidiary",
"focus": {
"value": "Offshore fabrication - oil and gas and offshore wind structures",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "2440 Kiewit Rd, Ingleside, TX 78362",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [
"South Fork Wind Offshore Substation",
"Charybdis Offshore Wind Turbine Installation Vessel"
],
"id": "div-08",
"founded": {
"value": 1984,
"source_url": "https://www.kiewit.com/about-us/our-history/"
},
"office_phone": {
"value": "(361) 775-4300",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"TX"
],
"metros_served": [
"Corpus Christi"
],
"sectors_served": [
"Offshore Oil & Gas",
"Offshore Wind",
"Marine Fabrication"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Building Group Inc.",
"brief": "Operating subsidiary for commercial and institutional building construction, with offices in Omaha, Lone Tree, Federal Way, McLean, Springfield, and Honolulu. It won the 2024 AGC Marvin M. Black Partnering Excellence award for the Children's Nebraska Hubbard Center.",
"type": "subsidiary",
"focus": {
"value": "Commercial and institutional building construction",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "1550 Mike Fahey St., Omaha, NE 68102",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-09",
"founded": null,
"office_phone": {
"value": "(402) 977-4500",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"NE",
"CO",
"WA",
"VA",
"HI"
],
"metros_served": [
"Omaha",
"Denver",
"Seattle",
"Washington DC",
"Honolulu"
],
"sectors_served": [
"Building",
"Commercial",
"Institutional",
"Healthcare"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Water Facilities South Co.",
"brief": "Operating subsidiary for water and wastewater treatment plant construction in the southern U.S.; Kiewit ranked #1 in ENR's 2024 Wastewater Treatment and Sewer & Waste categories.",
"type": "subsidiary",
"focus": {
"value": "Water and wastewater treatment plant construction",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "2050 Roanoke Rd., Suite 250, Westlake, TX 76262",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-10",
"founded": null,
"office_phone": {
"value": "(469) 276-3800",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"TX",
"GA",
"FL"
],
"metros_served": [
"Dallas-Fort Worth",
"Atlanta",
"Tampa",
"Jupiter FL"
],
"sectors_served": [
"Water",
"Wastewater"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Mining Group Inc.",
"brief": "Operating subsidiary providing contract mining for coal, phosphate, and other minerals, including the Buckskin Mining Company operation in Gillette, Wyoming and the Itafos contract mine in Soda Springs, Idaho.",
"type": "subsidiary",
"focus": {
"value": "Contract mining - coal, phosphate, and other minerals",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "1550 Mike Fahey St., Omaha, NE 68102",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-11",
"founded": null,
"office_phone": {
"value": "(402) 342-2052",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"NE",
"CO",
"ID",
"WY"
],
"metros_served": [
"Omaha",
"Denver"
],
"sectors_served": [
"Mining"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "TIC - The Industrial Company",
"brief": "Industrial construction subsidiary acquired by Kiewit on December 29, 2008, serving petrochemical, refining, power generation, heavy industrial, and mining markets, with sub-groups including TIC Power District and TIC Marine and Heavy Civil.",
"type": "subsidiary",
"focus": {
"value": "Industrial construction - petrochemical, refining, power generation, heavy industrial, mining",
"source_url": "https://en.wikipedia.org/wiki/Kiewit_Corporation"
},
"address": {
"value": "10055 Trainstation Circle, Lone Tree, CO 80124",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-12",
"founded": null,
"office_phone": {
"value": "(303) 325-0300",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"CO",
"KS",
"GA",
"MN",
"TX",
"NV"
],
"metros_served": [
"Denver",
"Kansas City",
"Atlanta",
"Minneapolis",
"Houston",
"Savannah"
],
"sectors_served": [
"Industrial"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Nuclear Solutions Co.",
"brief": "Nuclear construction and engineering subsidiary focused on Department of Energy nuclear security infrastructure and commercial nuclear including small modular reactors, with NQA-1 quality construction capability. It is lead constructor for Oklo's first Aurora powerhouse at Idaho National Laboratory.",
"type": "subsidiary",
"focus": {
"value": "Nuclear construction and engineering - DOE nuclear security infrastructure and commercial nuclear/SMRs",
"source_url": "https://www.kiewit.com/our-markets/nuclear-solutions/"
},
"address": {
"value": "105 Mitchell Road, Ste. 100, Oak Ridge, TN 37830",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": {
"value": "President (Mike Rinehart)",
"source_url": "https://www.kiewit.com/newsroom/powering-new-nuclear-solutions/"
},
"parent_company": "Kiewit",
"project_names": [
"Oklo Aurora Powerhouse at Idaho National Laboratory"
],
"id": "div-13",
"founded": null,
"office_phone": {
"value": "865-482-1812",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"TN",
"ID"
],
"metros_served": [
"Oak Ridge",
"Idaho Falls"
],
"sectors_served": [
"Nuclear"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Canada Group Inc.",
"brief": "Canadian holding and operating entity for all Kiewit construction and engineering operations in Canada, where Kiewit has operated since 1941, with 2025 Canadian revenue of $2.1 billion and approximately 4,000 employees.",
"type": "subsidiary",
"focus": {
"value": "All Kiewit construction and engineering operations in Canada",
"source_url": "https://www.kiewit.com/?lang=en-ca"
},
"address": {
"value": "1425 North Service Road East, Unit 1, Oakville, ON L6H 1A7, Canada",
"lat": null,
"lng": null,
"source_url": "https://gasworlddirectory.com/listing/kiewit-canada/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [
"Trans Mountain Expansion Project - Lower Mainland (KLTP)",
"Trans Mountain Expansion Project - Spread 5B"
],
"id": "div-14",
"founded": {
"value": 1941,
"source_url": "https://www.kiewit.com/?lang=en-ca"
},
"office_phone": {
"value": "+1 905 337 4000",
"source_url": "https://gasworlddirectory.com/listing/kiewit-canada/"
},
"states_served": [
"AB",
"BC",
"ON",
"QC",
"SK",
"MB",
"NL",
"NT"
],
"metros_served": [
"Toronto",
"Vancouver BC",
"Calgary",
"Edmonton",
"Montreal"
],
"sectors_served": [
"Transportation",
"Power",
"Oil, Gas & Chemical",
"Mining",
"Water"
],
"revenue_usd_m": {
"value": 2100,
"year": 2025,
"source_url": "https://www.kiewit.com/?lang=en-ca"
},
"employee_count": {
"value": 4000,
"source_url": "https://www.kiewit.com/?lang=en-ca"
},
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Peter Kiewit Sons ULC",
"brief": "Canadian unlimited liability company within the Kiewit family, listed among Kiewit subsidiaries in ENR's 2024 Top 400 data. It was selected in May 2025 by Canada's Nuclear Waste Management Organization as a vendor for the deep geological repository program.",
"type": "subsidiary",
"focus": {
"value": "Canadian construction operations; selected for construction planning and infrastructure design of Canada's deep geological repository",
"source_url": "https://www.nwmo.ca/en/news/the-nwmo-chooses-vendors-to-design-and-plan-canadas-dgr"
},
"address": null,
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [
"Canada Deep Geological Repository"
],
"id": "div-15",
"founded": null,
"office_phone": null,
"states_served": [
"ON"
],
"metros_served": [],
"sectors_served": [
"Nuclear",
"Mining",
"Heavy Civil"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Louisiana Co.",
"brief": "Kiewit operating entity that executed the turnkey EPC contract for the Calcasieu Pass LNG export facility in Cameron Parish, Louisiana for Venture Global LNG.",
"type": "subsidiary",
"focus": {
"value": "EPC construction in Louisiana, including the Calcasieu Pass LNG export facility",
"source_url": "https://www.prnewswire.com/news-releases/venture-global-lng-and-kiewit-announce-execution-of-epc-contract-for-calcasieu-pass-lng-export-facility-300761731.html"
},
"address": null,
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [
"Calcasieu Pass LNG Export Facility"
],
"id": "div-16",
"founded": null,
"office_phone": null,
"states_served": [
"LA"
],
"metros_served": [],
"sectors_served": [
"Oil, Gas & Chemical",
"LNG"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Ganotec Inc.",
"brief": "Canadian full-service heavy industrial construction subsidiary that joined the Kiewit family in 2007, performing civil, structural steel, heavy mechanical equipment installation, process piping, and E&I&C work for oil and gas, petrochemical, mining, and power clients.",
"type": "subsidiary",
"focus": {
"value": "Heavy industrial construction in Canada",
"source_url": "https://www.ganotec.com/about/"
},
"address": {
"value": "Calgary, Alberta, Canada",
"lat": null,
"lng": null,
"source_url": "https://www.ganotec.com/about/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-17",
"founded": null,
"office_phone": null,
"states_served": [
"AB",
"ON",
"QC"
],
"metros_served": [
"Calgary",
"Toronto"
],
"sectors_served": [
"Industrial",
"Oil, Gas & Chemical",
"Mining",
"Power"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Development Company",
"brief": "Development, investment, and asset management arm of Kiewit Corporation that develops, structures, finances, bids, and executes P3 and concession agreements for U.S. and Canadian agencies, with a team of 20+ professionals and offices in Denver, Los Angeles, Omaha, Dallas, Toronto, and Vancouver.",
"type": "subsidiary",
"focus": {
"value": "P3 and alternative project delivery - developer, concessionaire, investor, asset manager",
"source_url": "https://www.kiewit.com/services-and-solutions/kiewit-development-company/"
},
"address": null,
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-18",
"founded": null,
"office_phone": null,
"states_served": [
"CO",
"CA",
"NE",
"TX"
],
"metros_served": [
"Denver",
"Los Angeles",
"Omaha",
"Dallas",
"Toronto",
"Vancouver BC"
],
"sectors_served": [
"P3 Development"
],
"revenue_usd_m": null,
"employee_count": {
"value": 20,
"source_url": "https://www.kiewit.com/services-and-solutions/kiewit-development-company/"
},
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Supply Network",
"brief": "Centralized procurement and supply chain unit, formally centralized in 2016, managing over $10 billion in annual procurement spend through a network of 22,000 vendors with approximately 380 procurement staff.",
"type": "market-sector unit",
"focus": {
"value": "Centralized procurement and supply chain management for Kiewit projects and external clients",
"source_url": "https://www.kiewit.com/services-and-solutions/procurement/"
},
"address": null,
"leader_title": {
"value": "President (Andrew Gardner)",
"source_url": "https://www.kiewit.com/newsroom/kiewit-supply-network-understanding-and-mitigating-supply-risks/"
},
"parent_company": "Kiewit",
"project_names": [],
"id": "div-19",
"founded": {
"value": 2016,
"source_url": "https://www.kiewit.com/services-and-solutions/procurement/"
},
"office_phone": null,
"states_served": [],
"metros_served": [],
"sectors_served": [
"Procurement / Supply Chain"
],
"revenue_usd_m": null,
"employee_count": {
"value": 380,
"source_url": "https://www.kiewit.com/services-and-solutions/procurement/"
},
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "InEight Inc.",
"brief": "Wholly owned technology subsidiary launched in 2014 providing capital construction project controls software for scope, cost, schedule, and risk management, serving 300,000+ users and 750+ customers. As of June 2026 it remains Kiewit-owned; no sale or divestiture has occurred.",
"type": "subsidiary",
"focus": {
"value": "Capital construction project controls software",
"source_url": "https://www.kiewit.com/about-us/technology-at-kiewit/ineight/"
},
"address": {
"value": "9977 N. 90th Street, Ste. 200, Scottsdale, AZ 85258",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/about-us/technology-at-kiewit/ineight/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-20",
"founded": {
"value": 2014,
"source_url": "https://www.kiewit.com/about-us/technology-at-kiewit/ineight/"
},
"office_phone": {
"value": "(480) 776-2900",
"source_url": "https://www.kiewit.com/about-us/technology-at-kiewit/ineight/"
},
"states_served": [
"AZ",
"NE"
],
"metros_served": [
"Phoenix",
"Omaha"
],
"sectors_served": [
"Construction Technology / Software"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Mass. Electric Construction Co.",
"brief": "Electrical and systems installation subsidiary headquartered in Waltham, Massachusetts, serving power delivery, transit/rail systems, and data center markets in the U.S. and Canada.",
"type": "subsidiary",
"focus": {
"value": "Electrical and systems installation - power delivery, transit/rail, data centers",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "400 Totten Pond Road, Suite 400, Waltham, MA 02451",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-21",
"founded": null,
"office_phone": {
"value": "(781) 290-1000",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"MA",
"NJ",
"CO",
"NC",
"CA",
"TX",
"VA"
],
"metros_served": [
"Boston",
"New York City",
"Denver",
"Charlotte",
"Los Angeles",
"Dallas-Fort Worth",
"Washington DC"
],
"sectors_served": [
"Electrical",
"Transit Systems",
"Data Centers"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Continental Fire Sprinkler Company",
"brief": "Fire protection and fire sprinkler installation subsidiary (also branded Kiewit Fire Sprinklers) with offices across Nebraska, Iowa, Maryland, Missouri, Arizona, and Colorado.",
"type": "subsidiary",
"focus": {
"value": "Fire protection / fire sprinkler installation",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "4518 S 133rd St, Omaha, NE 68137",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-22",
"founded": null,
"office_phone": {
"value": "(402) 330-5170",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"NE",
"IA",
"MD",
"MO",
"AZ",
"CO"
],
"metros_served": [
"Omaha",
"Des Moines",
"Baltimore",
"Phoenix",
"Denver"
],
"sectors_served": [
"Fire Protection"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Weeks Marine, Inc.",
"brief": "Marine construction, dredging, tunneling, aggregates, and stevedoring subsidiary founded in 1919 and acquired by Kiewit effective January 1, 2023 for an undisclosed amount; it operates as an independently branded subsidiary led by President and CEO Eric Ellefsen.",
"type": "subsidiary",
"focus": {
"value": "Marine construction, dredging, tunneling, aggregates production, bulk stevedoring",
"source_url": "https://www.weeksmarine.com/stories/read/weeks-marine-inc-joins-kiewit-corporation/"
},
"address": {
"value": "4 Commerce Drive, Cranford, NJ 07016",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": {
"value": "President and CEO (Eric Ellefsen)",
"source_url": "https://www.weeksmarine.com/stories/read/weeks-marine-inc-joins-kiewit-corporation/"
},
"parent_company": "Kiewit",
"project_names": [],
"id": "div-23",
"founded": {
"value": 1919,
"source_url": "https://www.weeksmarine.com/stories/read/weeks-marine-inc-joins-kiewit-corporation/"
},
"office_phone": {
"value": "(908) 272-4010",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"NJ",
"LA",
"TX"
],
"metros_served": [
"New York City",
"New Orleans",
"Houston"
],
"sectors_served": [
"Marine",
"Dredging",
"Tunneling",
"Aggregates"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Healy Tibbitts Builders, Inc.",
"brief": "Marine and heavy civil construction subsidiary of Weeks Marine serving Hawaii and the Pacific region, acquired by Weeks in 1989 and passed to Kiewit via the 2023 Weeks Marine acquisition. It won a 2025 AGC Build America Merit Award for the Lahaina Harbor project.",
"type": "subsidiary",
"focus": {
"value": "Marine and heavy civil construction in Hawaii and the Pacific",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "99-994 Iwaena Street, Suite A, Aiea, HI 96701",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-24",
"founded": null,
"office_phone": {
"value": "(808) 487-3664",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"HI",
"GU"
],
"metros_served": [
"Honolulu",
"Hagatna"
],
"sectors_served": [
"Marine",
"Heavy Civil"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "McNally Tunneling Corporation / McNally International, Inc.",
"brief": "Tunneling and marine construction subsidiary of Weeks Marine (Canadian arm founded 1949 in Hamilton, Ontario; U.S. arm based in Westlake, Ohio), acquired by Weeks in 2011 and passed to Kiewit via the 2023 Weeks Marine acquisition.",
"type": "subsidiary",
"focus": {
"value": "Tunneling and marine construction in Canada and the U.S.",
"source_url": "https://www.weeksmarine.com/what-we-do/tunneling/"
},
"address": {
"value": "800 Westpoint Parkway, Suite 1130, Westlake, OH 44145",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-25",
"founded": {
"value": 1949,
"source_url": "https://www.cbinsights.com/company/mcnally-international"
},
"office_phone": {
"value": "(440) 835-0053",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"OH",
"ON"
],
"metros_served": [
"Cleveland",
"Hamilton ON"
],
"sectors_served": [
"Tunneling",
"Marine"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "North American Aggregates",
"brief": "Sand and aggregate production subsidiary of Weeks Marine formed in 2016 and passed to Kiewit via the 2023 Weeks Marine acquisition; it is the largest supplier of sand in the New York metropolitan area.",
"type": "subsidiary",
"focus": {
"value": "Sand and aggregate production",
"source_url": "https://www.kiewit.com/newsroom/weeks-marine-a-generational-company-continues-its-legacy-under-kiewit/"
},
"address": null,
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-26",
"founded": {
"value": 2016,
"source_url": "https://www.kiewit.com/newsroom/weeks-marine-a-generational-company-continues-its-legacy-under-kiewit/"
},
"office_phone": null,
"states_served": [
"NY",
"NJ"
],
"metros_served": [
"New York City"
],
"sectors_served": [
"Aggregates"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Kiewit Foundations Co.",
"brief": "Specialty foundations subsidiary headquartered at the Kiewit Omaha campus; it has been an AGC of Washington member since 2023.",
"type": "subsidiary",
"focus": {
"value": "Specialty foundations work",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "1550 Mike Fahey St., Omaha, NE 68102",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-27",
"founded": null,
"office_phone": {
"value": "(402) 346-8535",
"source_url": "https://www.kiewit.com/locations/"
},
"states_served": [
"NE",
"WA"
],
"metros_served": [
"Omaha",
"Seattle"
],
"sectors_served": [
"Foundations / Geotechnical"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
},
{
"name": "Western Summit Constructors Inc.",
"brief": "Industrial and infrastructure construction subsidiary with offices in Lone Tree, Colorado and Alpharetta, Georgia.",
"type": "subsidiary",
"focus": {
"value": "Industrial and infrastructure construction",
"source_url": "https://www.kiewit.com/locations/"
},
"address": {
"value": "10055 Trainstation Circle, Lone Tree, CO 80124",
"lat": null,
"lng": null,
"source_url": "https://www.kiewit.com/locations/"
},
"leader_title": null,
"parent_company": "Kiewit",
"project_names": [],
"id": "div-28",
"founded": null,
"office_phone": null,
"states_served": [
"CO",
"GA"
],
"metros_served": [
"Denver",
"Atlanta"
],
"sectors_served": [
"Industrial",
"Water/Wastewater"
],
"revenue_usd_m": null,
"employee_count": null,
"active_project_count": null,
"aggregate_active_value_usd_m": null,
"license_numbers": ]
}
],
"locations": [
{
"name": "Kiewit Corporation Headquarters - Omaha",
"brief": "Global headquarters campus of Kiewit Corporation, also housing Kiewit Building Group, Kiewit Mining Group, Kiewit Infrastructure Co. Underground District, Kiewit Engineering & Design Co., and Kiewit Foundations Co.",
"address": {
"value": "1550 Mike Fahey St., Omaha, NE 68102",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "HQ",
"phone": "(402) 342-2052",
"opened_date": null,
"owning_division": null
},
{
"name": "Lone Tree, CO Office",
"brief": "Major multi-entity hub housing Kiewit Engineering Group, Kiewit Infrastructure Co., Kiewit Building Group, TIC, Kiewit Mining Group, Western Summit Constructors, and Mass. Electric.",
"address": {
"value": "10055 Trainstation Circle, Lone Tree, CO 80124",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "regional",
"phone": "(303) 325-0300",
"opened_date": null,
"owning_division": "Kiewit Engineering Group Inc."
},
{
"name": "Lenexa, KS Office",
"brief": "Power market hub housing Kiewit Power Constructors, Kiewit Power Delivery, Kiewit Engineering Group power and water teams, and TIC Power District.",
"address": {
"value": "8900 Renner Blvd, Lenexa, KS 66219",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "regional",
"phone": "(913) 928-7000",
"opened_date": null,
"owning_division": "Kiewit Power Constructors Co."
},
{
"name": "Houston, TX Office",
"brief": "Oil, gas and chemical hub housing Kiewit Energy Group Inc. and Kiewit Engineering Group OGC and Mexico engineering teams.",
"address": {
"value": "585 N. Dairy Ashford Rd., Suite 100, Houston, TX 77079",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "regional",
"phone": "(281) 848-4800",
"opened_date": null,
"owning_division": "Kiewit Energy Group Inc."
},
{
"name": "The Woodlands, TX Office",
"brief": "Office housing TIC - The Industrial Company and Kiewit Energy Company (Kiewit Energy District).",
"address": {
"value": "3831 Technology Forest Blvd, The Woodlands, TX 77381",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "regional",
"phone": "(832) 616-4470",
"opened_date": null,
"owning_division": "TIC - The Industrial Company"
},
{
"name": "Ingleside, TX Fabrication Yard",
"brief": "555-acre offshore fabrication yard of Kiewit Offshore Services, established 1984.",
"address": {
"value": "2440 Kiewit Rd, Ingleside, TX 78362",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "yard/shop",
"phone": "(361) 775-4300",
"opened_date": null,
"owning_division": "Kiewit Offshore Services, Ltd."
},
{
"name": "Westlake, TX Office",
"brief": "South Central hub housing Kiewit Infrastructure South Co., Kiewit Engineering Group infrastructure engineers, and Kiewit Water Facilities South.",
"address": {
"value": "2050 Roanoke Rd., Westlake, TX 76262",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "regional",
"phone": "(817) 337-7000",
"opened_date": null,
"owning_division": "Kiewit Infrastructure South Co."
},
{
"name": "Woodcliff Lake, NJ Office",
"brief": "Eastern District hub housing Kiewit Infrastructure Co. Eastern District, Kiewit Power Delivery, and Mass. Electric New York.",
"address": {
"value": "470 Chestnut Ridge Road, Woodcliff Lake, NJ 07677",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "regional",
"phone": "201-571-2500",
"opened_date": null,
"owning_division": "Kiewit Infrastructure Co."
},
{
"name": "Vancouver, WA Office",
"brief": "Northwest District office of Kiewit Infrastructure West Co. (General Construction Co.), the SAM.gov-registered address for the subsidiary's federal contracting entity.",
"address": {
"value": "2200 Columbia House Blvd, Vancouver, WA 98661",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "regional",
"phone": "(360) 693-1478",
"opened_date": null,
"owning_division": "Kiewit Infrastructure West Co."
},
{
"name": "Federal Way, WA Office",
"brief": "Office housing Kiewit Infrastructure West Co. Bridge & Marine and Kiewit Building Group.",
"address": {
"value": "33930 Weyerhaeuser Way S., Suite 300, Federal Way, WA 98001",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "regional",
"phone": "(253) 943-4200",
"opened_date": null,
"owning_division": "Kiewit Infrastructure West Co."
},
{
"name": "Cranford, NJ Office (Weeks Marine HQ)",
"brief": "Headquarters of Weeks Marine, Inc., Kiewit's marine construction and dredging subsidiary.",
"address": {
"value": "4 Commerce Drive, Cranford, NJ 07016",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "HQ",
"phone": "(908) 272-4010",
"opened_date": null,
"owning_division": "Weeks Marine, Inc."
},
{
"name": "Waltham, MA Office (Mass. Electric HQ)",
"brief": "Headquarters of Mass. Electric Construction Co.",
"address": {
"value": "400 Totten Pond Road, Suite 400, Waltham, MA 02451",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "HQ",
"phone": "(781) 290-1000",
"opened_date": null,
"owning_division": "Mass. Electric Construction Co."
},
{
"name": "Scottsdale, AZ Office (InEight HQ)",
"brief": "Headquarters of InEight Inc., Kiewit's construction software subsidiary.",
"address": {
"value": "9977 N. 90th Street, Ste. 200, Scottsdale, AZ 85258",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/about-us/technology-at-kiewit/ineight/",
"office_type": "HQ",
"phone": "(480) 776-2900",
"opened_date": null,
"owning_division": "InEight Inc."
},
{
"name": "Oak Ridge, TN Office",
"brief": "Office of Kiewit Nuclear Solutions Co. serving the DOE nuclear security market.",
"address": {
"value": "105 Mitchell Road, Ste. 100, Oak Ridge, TN 37830",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "regional",
"phone": "865-482-1812",
"opened_date": null,
"owning_division": "Kiewit Nuclear Solutions Co."
},
{
"name": "Idaho Falls, ID Office",
"brief": "Office of Kiewit Nuclear Solutions Co. near Idaho National Laboratory.",
"address": {
"value": "525 Park Ave. #2A, Idaho Falls, ID 83402",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "satellite",
"phone": "208-970-4073",
"opened_date": null,
"owning_division": "Kiewit Nuclear Solutions Co."
},
{
"name": "Oakville, ON Office (Kiewit Canada)",
"brief": "Key Canadian operations hub of Kiewit Canada Group Inc.",
"address": {
"value": "1425 North Service Road East, Unit 1, Oakville, ON L6H 1A7, Canada",
"lat": null,
"lng": null
},
"source_url": "https://gasworlddirectory.com/listing/kiewit-canada/",
"office_type": "regional",
"phone": "+1 905 337 4000",
"opened_date": null,
"owning_division": "Kiewit Canada Group Inc."
},
{
"name": "La Vista, NE Business Center",
"brief": "Kiewit Business Center and Kiewit Technology Group offices supporting enterprise operations.",
"address": {
"value": "12312 Port Grace Blvd., La Vista, NE 68128",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "satellite",
"phone": "402-342-2052",
"opened_date": null,
"owning_division": null
},
{
"name": "Anchorage, AK Office",
"brief": "Bridge & Marine and Northwest District office of Kiewit Infrastructure West Co.",
"address": {
"value": "2000 West International Airport Rd. #C-6, Anchorage, AK 99502",
"lat": null,
"lng": null
},
"source_url": "https://www.kiewit.com/locations/",
"office_type": "satellite",
"phone": null,
"opened_date": null,
"owning_division": "Kiewit Infrastructure West Co."
},
{
"name": "[TRUNCATED] projects array began here",
"brief": "projects[0] = Calcasieu Pass LNG Export Facility (status Done, $5,000M, 10.7 MTPA / 18 trains, Cameron Parish LA, owner Venture Global LNG, Kiewit Louisiana Co., is_recent true, confidence high) — cut off mid-source_url. Remaining ~16 of 17 projects + any people/events/memberships/software/sources/gaps sections were lost to the 50k-char chat limit."
}
]
}
```
