<!-- TRUNCATED CHAT CAPTURE — 2026-06-12. Zack pasted this 2nd-pass Sundt dossier in chat ("add to notion"); the paste cut off mid-Water & Wastewater division (sector_focus, at "Pipelines",). MISSING sections: rest of div_water, div_heavy_industrial_mining, div_renewables, div_concrete (per division_count brief), locations array (all loc_* ids undefined), projects array (all p_* ids undefined), people array, events, memberships, software, sources, gaps. Ask Zack for the full file before treating those as ground truth. Captured portion loaded additively 2026-06-12 — see context/state/records-sundt.md. -->
{
  "dossier_meta": {
    "company": "Sundt Construction",
    "company_website": "https://www.sundt.com",
    "run_date": "2026-06-12",
    "lookback_years": 7,
    "region_hint": null,
    "sector_focus": "all",
    "analyst_role": "Senior Construction GC Intelligence Analyst for Enlaye BD research",
    "brief": "Structured GC intelligence dossier on Sundt Construction, focusing on divisions, offices, project mapping, recent awards/groundbreakings, firmographics, events, memberships and incumbent technology evidence.",
    "source_url": "https://www.sundt.com/wp-content/uploads/2025/06/Sundt-Fact-Sheet-2025.pdf",
    "methodology": {
      "brief": "Evidence was gathered from Sundt official pages, official PDFs, project pages, press/news pages, and selected authoritative third-party pages for software and federal-contract identifiers. Division ownership is explicit where pages name a group and otherwise mapped by sector and region with confidence flags.",
      "source_url": "https://www.sundt.com/what-we-build/"
    }
  },
  "company": {
    "name": "Sundt Construction, Inc.",
    "website": "https://www.sundt.com",
    "brief": "Sundt Construction, Inc. is a Tempe-headquartered general contractor founded in 1890; the 2025 fact sheet says it specializes in transportation, water and wastewater, advanced facilities, heavy industrial and mining, building, concrete and renewable power work and is owned entirely by approximately 4,500 employees. A May 2026 acquisition announcement describes Sundt as 136 years old, 5,000-plus employee-owned, with 13 offices and ranked No. 46 on ENR Top 400 Contractors.",
    "source_url": "https://www.sundt.com/wp-content/uploads/2025/06/Sundt-Fact-Sheet-2025.pdf",
    "legal_name": "SUNDT CONSTRUCTION, INC.",
    "dba": "SUNDT CONSTRUCTION INC",
    "hq_location_id": "loc_tempe_hq",
    "ownership": "100% employee-owned / ESOP",
    "founded_year": 1890,
    "employee_count_public": {
      "value": "approximately 4,500 in 2025 fact sheet; 5,000-plus in May 2026 acquisition announcement",
      "source_url": "https://www.sundt.com/2026/valley-construction-firm-acquires-electrical-contractor/"
    },
    "enr_rank": {
      "rank": 46,
      "list": "ENR Top 400 Contractors",
      "year": 2025,
      "source_url": "https://www.sundt.com/wp-content/uploads/2025/06/Sundt-Fact-Sheet-2025.pdf"
    },
    "federal_identifiers": {
      "uei": "NEV1XR5H3FG5",
      "cage": "0C5E8",
      "primary_naics": "236220 Commercial and Institutional Building Construction",
      "source_url": "https://www.highergov.com/awardee/sundt-construction-inc-10136753/"
    },
    "licenses_summary": {
      "brief": "Sundt lists contractor license numbers by state on its contact page, including Arizona, Florida, Georgia, Idaho, Texas, Utah and Washington-related entries.",
      "source_url": "https://www.sundt.com/contact/"
    }
  },
  "division_count": {
    "count": 7,
    "brief": "The dossier treats Sundt as having seven externally evidenced operating or operating-adjacent groups: Building, Transportation, Advanced Facilities, Water & Wastewater, Heavy Industrial & Mining, Renewables, and Concrete/Self-Perform. Some groups are formal operating groups while Concrete is a self-perform division used across projects.",
    "source_url": "https://www.sundt.com/wp-content/uploads/2025/06/Sundt-Fact-Sheet-2025.pdf",
    "confidence": "medium"
  },
  "divisions": [
    {
      "id": "div_building",
      "name": "Building Group",
      "type": "operating group",
      "brief": "Sundt’s Building Group delivers commercial, education, healthcare, aviation, government, office and other building work across California, the Southwest, Texas and newer Southeast markets. Chad Buck was promoted to president of the Building Group in 2025, succeeding Teri Jones.",
      "region_focus": [
        "California",
        "Southwest",
        "Texas",
        "Southeast"
      ],
      "sector_focus": [
        "Buildings",
        "Education",
        "Healthcare",
        "Aviation",
        "Government",
        "Office",
        "Student housing"
      ],
      "office_ids": [
        "loc_tempe_hq",
        "loc_san_diego",
        "loc_irvine",
        "loc_sacramento",
        "loc_el_paso",
        "loc_dallas",
        "loc_charlotte",
        "loc_tampa"
      ],
      "leadership": [
        {
          "name": "Chad Buck",
          "title": "President, Building",
          "source_url": "https://www.sundt.com/2025/sundt-construction-announces-chad-buck-as-new-building-group-president/"
        },
        {
          "name": "Teri Jones",
          "title": "Former President, Building; advisor through September 30, 2025 per announcement",
          "source_url": "https://www.sundt.com/2025/sundt-construction-announces-chad-buck-as-new-building-group-president/"
        },
        {
          "name": "Ryan Nessen",
          "title": "SVP, California District Manager",
          "source_url": "https://www.sundt.com/about-sundt/regions/california/"
        },
        {
          "name": "Sarah Owen",
          "title": "Southwest District Business Development Manager",
          "source_url": "https://www.sundt.com/employees/sarah-owen/"
        }
      ],
      "project_ids": [
        "p_bna_conrac",
        "p_csuf_phasev",
        "p_csuf_expansion",
        "p_sdsu_brawley",
        "p_utep_amac",
        "p_san_airport_support",
        "p_banner_tucson",
        "p_bspb",
        "p_el_paso_police",
        "p_sac_state_science"
      ],
      "source_url": "https://www.sundt.com/2025/sundt-construction-announces-chad-buck-as-new-building-group-president/"
    },
    {
      "id": "div_transportation",
      "name": "Transportation Group",
      "type": "operating group",
      "brief": "Sundt’s Transportation Group builds roadways, bridges, aviation infrastructure, transit, rail, flood-control and dam projects and is led by President Jeff Williamson. The group has expanded across Arizona, Texas, New Mexico, Utah, Idaho and the Northwest.",
      "region_focus": [
        "Southwest",
        "Texas",
        "Intermountain",
        "Northwest",
        "Southeast expansion"
      ],
      "sector_focus": [
        "Roadways",
        "Bridges",
        "Transit rail",
        "Aviation infrastructure",
        "Flood control",
        "Dams"
      ],
      "office_ids": [
        "loc_tempe_hq",
        "loc_el_paso",
        "loc_dallas",
        "loc_san_antonio",
        "loc_slc",
        "loc_vancouver",
        "loc_charlotte"
      ],
      "leadership": [
        {
          "name": "Jeff Williamson",
          "title": "President, Transportation",
          "source_url": "https://www.sundt.com/employees/jeff-williamson/"
        },
        {
          "name": "Ken Kubacki",
          "title": "Vice President & Northwest Regional Manager, Transportation Group",
          "source_url": "https://www.sundt.com/employees/ken-kubacki/"
        },
        {
          "name": "Jasen Bennie",
          "title": "SVP, Intermountain Regional Manager, Transportation Group",
          "source_url": "https://www.sundt.com/employees/jasen-bennie/"
        },
        {
          "name": "Jeffrey Hamilton",
          "title": "VP, Business Development Manager, Transportation Group",
          "source_url": "https://www.sundt.com/employees/jeffrey-hamilton/"
        }
      ],
      "project_ids": [
        "p_sr347",
        "p_rocky_point",
        "p_us89_ped_bridge",
        "p_i20_odessa",
        "p_i10_phase2",
        "p_i10_widening",
        "p_windhaven",
        "p_lake_mcqueeney_placid",
        "p_upper_brushy_dam101",
        "p_san_pedro",
        "p_go10",
        "p_i10_connect",
        "p_boeckman",
        "p_sellwood",
        "p_west_7th",
        "p_valley_metro_nw",
        "p_valley_metro_4_5",
        "p_hausman",
        "p_white_tanks",
        "p_los_alamos_dam",
        "p_london_bridge",
        "p_183_north"
      ],
      "source_url": "https://www.sundt.com/employees/jeff-williamson/"
    },
    {
      "id": "div_advanced_facilities",
      "name": "Advanced Facilities Group",
      "type": "operating group",
      "brief": "Sundt created the Advanced Facilities Group in 2024 to focus on semiconductor manufacturing, electric vehicle and battery, solar-cell and other advanced manufacturing projects. Alex Charland was promoted to president of the new group.",
      "region_focus": [
        "Western United States",
        "Southwest",
        "California",
        "National advanced manufacturing pursuits"
      ],
      "sector_focus": [
        "Semiconductors",
        "Data centers",
        "Cleanrooms",
        "EV and battery",
        "Solar cells",
        "Advanced manufacturing"
      ],
      "office_ids": [
        "loc_tempe_hq",
        "loc_phx_ops",
        "loc_sacramento",
        "loc_irvine"
      ],
      "leadership": [
        {
          "name": "Alex Charland",
          "title": "President, Advanced Facilities",
          "source_url": "https://www.sundt.com/2024/sundt-promotes-charland-to-lead-advanced-facilities-group/"
        },
        {
          "name": "Josh Anderson",
          "title": "Sector Manager, Data Centers",
          "source_url": "https://www.sundt.com/projects/data-center-campus-for-confidential-client/"
        }
      ],
      "project_ids": [
        "p_apache_junction_osm",
        "p_data_center_campus",
        "p_project_fusion",
        "p_sitewide_semiconductor_iwtr"
      ],
      "source_url": "https://www.sundt.com/2024/sundt-promotes-charland-to-lead-advanced-facilities-group/"
    },
    {
      "id": "div_water",
      "name": "Water & Wastewater Group",
      "type": "operating group",
      "brief": "Sundt announced Sam Reidy as president of its Water & Wastewater Group in 2024; the firm says it has completed more than $7.5 billion in water-treatment construction since 1950.",
      "region_focus": [
        "Southwest",
        "California",
        "Texas",
        "Intermountain",
        "Southeast"
      ],
      "sector_focus": [
        "Water treatment",
        "Wastewater treatment",
        "Water reuse",
        "Pipelines",
<!-- PASTE ENDS HERE — truncated -->
