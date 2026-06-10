# Harvard University Active Construction Projects — Intelligence Report (June 8, 2026)

## Executive Summary

As of early June 2026, Harvard University is advancing a focused but diverse portfolio of capital projects across its Cambridge, Allston, Longwood, and Business School campuses. The most significant active projects include Pritzker Hall (the new Economics department building), the Eliot House Renewal, the American Repertory Theater (ART) and affiliated graduate housing complex at 175 North Harvard Street/100 South Campus Drive, the Enterprise Research Campus (ERC) Phase A completion and associated streetscape work, the William James Hall Plaza Renovation, multiple Harvard Business School renovations (Chase/McCulloch/Dillon), the 12 Palmer Street renovation, and the Bertarelli Building (HMS Building C) in Longwood.[^1][^2][^3][^4][^5]

Harvard’s construction-mitigation site and related planning pages provide the clearest single view of what is currently under construction, with project-specific pages confirming that work is actively underway in 2026 for Pritzker Hall, Eliot House, the ART and affiliate housing complex, the Barker Center roof renewal, William James Hall plaza, and the 12 Palmer renovation. In Allston, ERC Phase A buildings are now operational, with punch-list work and fit-outs ongoing, while public space and streetscape work continues. At Harvard Medical School, Building C (to be named the Bertarelli Building) is in mid-renovation, with completion targeted for October 2026.[^2][^6][^3][^7][^4][^8][^5][^9][^10][^11]

The general-contractor landscape shows a small set of repeat higher-education specialists holding most of the large Harvard work: Shawmut Design and Construction at 175 North Harvard/ART, Consigli Construction on several Harvard projects including House Renewal and other campus work, Turner Construction leading the ERC lab buildings, and regional/lab-focused firms such as Smoot Construction, J&J Contractors, and Janey Construction partnering on ERC and other Allston work. Evidence tying Eliot House and Pritzker Hall specifically to individual CMs is more circumstantial (union notices, licensing hearings, and staff LinkedIn profiles) and therefore carries lower confidence, but points strongly to Shawmut at Eliot and Consigli at Pritzker and 12 Palmer.[^12][^13][^14][^15][^16][^17][^18][^19][^20][^21]

Funding continues to rely heavily on major philanthropic gifts (Pritzker Hall for Economics, Bertarelli Building C), bond financing, and the University’s capital plan, supplemented in Allston by development partnerships and large construction loans (e.g., Otera Capital’s loan to ERC Phase A). Several projects (Pritzker Hall, Eliot House, William James Plaza) appear to be under cost or fundraising pressure, but no public evidence suggests that construction has been paused. Harvard’s updated Sustainable Building Standards (2024) and LBC Core/LEED programs are clearly shaping new projects (e.g., Pritzker Hall, Treehouse, ERC, housing), with explicit targets for Living Building Challenge Core and health-focused materials and systems.[^22][^23][^15][^24][^25][^26][^27][^28][^18][^29][^30][^31][^32]


## Section 2: Project Registry (JSON Records)

```json
[
  {
    "project_id": "HARV-2025-PRITZKER",
    "project_name": "Pritzker Hall (Economics Department Building)",
    "project_nickname": "Pritzker Economics Building",
    "status": "Active / Under Construction",
    "project_type": {
      "primary": "Academic / Research Lab",
      "secondary": "New Construction"
    },
    "description": "Ground-up construction of a nine-story academic building (one level below grade, eight above) to house Harvard's Department of Economics, including offices, classrooms, meeting and event rooms, and collaboration space.",
    "purpose": "To consolidate the Economics Department in a modern facility, improve collaboration among faculty, graduate students, and undergraduates, and provide upgraded teaching and research space, funded in part by a $100 million gift from Penny Pritzker.",
    "location": {
      "campus": "Main Campus",
      "street_address": "Approx. 1805 Cambridge Street (site behind Littauer Center)",
      "city": "Cambridge",
      "state": "MA",
      "zip_code": "02138",
      "building_name": "Pritzker Hall (future)",
      "coordinates": "[NOT DISCLOSED]",
      "neighborhood_or_district": "Harvard Yard / FAS North Yard"
    },
    "timeline": {
      "groundbreaking_date": "06/2025",
      "estimated_completion": "12/2027",
      "actual_completion": "[NOT DISCLOSED]",
      "duration_months": "30 [ESTIMATED]",
      "current_phase": "Structure / Envelope and early Interiors (steel erection spring–fall 2026)"
    },
    "financials": {
      "total_project_budget": "$175 million fundraising goal [PARTIAL]",
      "construction_contract_value": "[NOT DISCLOSED]",
      "funding_source": "Donor gifts (including $100 million from Penny Pritzker) plus Harvard capital/bond financing",
      "donor_name": "Penny Pritzker; additional alumni donors (Tsai family, Slusky, Smith)"
    },
    "scale": {
      "gross_square_footage": "[NOT DISCLOSED]",
      "floors_above_grade": "8",
      "floors_below_grade": "1",
      "number_of_units_or_beds": "[NOT APPLICABLE]",
      "parking_spaces": "[NOT DISCLOSED]"
    },
    "sustainability": {
      "leed_target": "[NOT DISCLOSED] (likely LEED Gold or better) [ESTIMATED]",
      "other_certifications": "Targeting Living Building Challenge Core under Harvard's 2024 Sustainable Building Standards [ESTIMATED]",
      "harvard_sustainability_commitment": "https://sustainable.harvard.edu/our-plan/how-we-build/sustainable-building-standards/"
    },
    "design_team": {
      "architect_of_record": "[NOT DISCLOSED] (Grafton Architects widely referenced as design architect) [LOW CONFIDENCE]",
      "design_architect": "Grafton Architects [LOW CONFIDENCE — inferred from social media and architectural coverage]",
      "landscape_architect": "[NOT DISCLOSED]",
      "structural_engineer": "[NOT DISCLOSED]",
      "mep_engineer": "[NOT DISCLOSED]",
      "owner_representative": "Harvard Planning & Project Management / FAS Capital Projects [ESTIMATED]"
    },
    "construction_team": {
      "general_contractor": "Consigli Construction Co., Inc. [MEDIUM CONFIDENCE]",
      "construction_manager": "Consigli Construction Co., Inc. (CM-at-Risk) [MEDIUM CONFIDENCE]",
      "contract_type": "CM-at-Risk / GMP [ESTIMATED]",
      "key_subcontractors": [
        "[NOT DISCLOSED]"
      ],
      "notable_trade_packages": "Finishes and envelope trades anticipated to follow Harvard's Healthy Building and LBC Core materials requirements."
    },
    "harvard_oversight": {
      "harvard_project_manager": "Amy Finlayson (Associate Director, Campus Growth & Redevelopment) has publicly discussed the Pritzker construction project [LOW CONFIDENCE as day-to-day PM]",
      "reporting_entity": "Faculty of Arts and Sciences / Harvard Planning & Project Management",
      "school_or_unit_sponsor": "Faculty of Arts and Sciences — Department of Economics"
    },
    "community_impact": {
      "community_benefits_agreement": "No project-specific CBA disclosed for this site.",
      "neighborhood_liaison_contacts": "Construction mitigation hotline and email per Harvard Construction Mitigation.",
      "construction_impact_notices": [
        "https://construction.harvard.edu/current-projects/allston-development/new-fas-building/",
        "https://construction.harvard.edu/2026/06/01/week-of-june-1-2026-5/",
        "https://www.cambridgema.gov/-/media/Files/publicworksdepartment/Engineering/Resources/constructionmeetingminutes/2025/minutes06022025.pdf"
      ]
    },
    "sources": [
      {
        "source_label": "Harvard Construction Mitigation — Pritzker Hall project page",
        "url": "https://construction.harvard.edu/current-projects/allston-development/new-fas-building/",
        "date_accessed": "2026-06-08",
        "document_type": "Official project page"
      },
      {
        "source_label": "Harvard Crimson — construction underway for Pritzker Hall",
        "url": "https://www.thecrimson.com/article/2025/10/9/new-economics-building-construction/",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      },
      {
        "source_label": "Harvard Crimson — funding shortfall for Pritzker Hall",
        "url": "https://www.thecrimson.com/article/2026/3/11/pritzker-hall-funding-shortfall/",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      },
      {
        "source_label": "Harvard Magazine / Gazette — Penny Pritzker gift announcement",
        "url": "https://news.harvard.edu/gazette/story/2021/09/gift-from-penny-pritzker-81-to-spark-new-era-for-harvard-economics/",
        "date_accessed": "2026-06-08",
        "document_type": "Official news release"
      },
      {
        "source_label": "Harvard Construction Mitigation — weekly work summaries for Pritzker",
        "url": "https://construction.harvard.edu/2026/05/31/week-of-june-1-2026-5/",
        "date_accessed": "2026-06-08",
        "document_type": "Construction notice"
      }
    ]
  },
  {
    "project_id": "HARV-2025-ELIOT",
    "project_name": "Eliot House Renewal",
    "project_nickname": "Eliot House Renovation",
    "status": "Active / Under Construction",
    "project_type": {
      "primary": "Student Housing / Dormitory",
      "secondary": "Gut Renovation / Historic Landmark"
    },
    "description": "Comprehensive renewal of Eliot House, including exterior restoration (roofs, chimneys, dormers, brick repointing) and full interior gut renovations to create new student and staff units, modern building systems, and improved accessibility.",
    "purpose": "To bring one of Harvard's historic River Houses up to modern life-safety, accessibility, and residential standards while preserving its architectural character as part of the Undergraduate House Renewal program.",
    "location": {
      "campus": "Main Campus",
      "street_address": "101 Dunster Street",
      "city": "Cambridge",
      "state": "MA",
      "zip_code": "02138",
      "building_name": "Eliot House",
      "coordinates": "42.37022,-71.12082",
      "neighborhood_or_district": "River Houses / Charles River"
    },
    "timeline": {
      "groundbreaking_date": "06/2025",
      "estimated_completion": "Fall 2027",
      "actual_completion": "[NOT DISCLOSED]",
      "duration_months": "27 [ESTIMATED]",
      "current_phase": "Demolition and structural / envelope work; interior reconstruction ongoing in 2026"
    },
    "financials": {
      "total_project_budget": "[NOT DISCLOSED] (part of House Renewal program, >$1.4 billion overall) [LOW CONFIDENCE]",
      "construction_contract_value": "[NOT DISCLOSED]",
      "funding_source": "Harvard College capital plan, philanthropy, and University financing",
      "donor_name": "[NOT DISCLOSED]"
    },
    "scale": {
      "gross_square_footage": "[NOT DISCLOSED]",
      "floors_above_grade": "5",
      "floors_below_grade": "[NOT DISCLOSED]",
      "number_of_units_or_beds": "More than 400 student beds [ESTIMATED based on house size]",
      "parking_spaces": "[NOT APPLICABLE]"
    },
    "sustainability": {
      "leed_target": "[NOT DISCLOSED] (House Renewal projects have typically targeted LEED Gold or equivalent) [ESTIMATED]",
      "other_certifications": "Potential LBC Core alignment under 2024 Sustainable Building Standards [LOW CONFIDENCE]",
      "harvard_sustainability_commitment": "https://sustainable.harvard.edu/our-plan/how-we-build/sustainable-building-standards/"
    },
    "design_team": {
      "architect_of_record": "KieranTimberlake",
      "design_architect": "KieranTimberlake",
      "landscape_architect": "[NOT DISCLOSED] (likely similar River House design teams) [LOW CONFIDENCE]",
      "structural_engineer": "[NOT DISCLOSED]",
      "mep_engineer": "[NOT DISCLOSED]",
      "owner_representative": "House Renewal Project Management Office / Jacobs for earlier phases [ESTIMATED]"
    },
    "construction_team": {
      "general_contractor": "Shawmut Design and Construction [HIGH CONFIDENCE]",
      "construction_manager": "Shawmut Design and Construction (CM-at-Risk) [HIGH CONFIDENCE]",
      "contract_type": "CM-at-Risk / GMP [ESTIMATED]",
      "key_subcontractors": [
        "Marr Scaffolding (scaffolding supplier) [LOW CONFIDENCE, based on regional patterns]",
        "IUPAT DC35-affiliated finishing trades [LOW CONFIDENCE]"
      ],
      "notable_trade_packages": "Extensive historic masonry restoration, roofing, and interior finishes for a 220,000 SF historic dormitory."
    },
    "harvard_oversight": {
      "harvard_project_manager": "House Renewal Project Management Office; specific PM not publicly named [NOT DISCLOSED]",
      "reporting_entity": "Undergraduate House Renewal Program / Harvard College",
      "school_or_unit_sponsor": "Harvard College (FAS Undergraduate Residential System)"
    },
    "community_impact": {
      "community_benefits_agreement": "Not applicable; on-campus renovation.",
      "neighborhood_liaison_contacts": "Construction mitigation hotline and email; Harvard Transportation notices on parking impacts.",
      "construction_impact_notices": [
        "https://construction.harvard.edu/current-projects/harvard-undergrad-house-renewal/eliot-house-2/",
        "https://construction.harvard.edu/2026/06/04/week-of-june-8-2026-3/",
        "https://transportation.harvard.edu/news/2025/06/parking-impacts-during-eliot-house-renewal-project"
      ]
    },
    "sources": [
      {
        "source_label": "Harvard Construction Mitigation — Eliot House project description",
        "url": "https://construction.harvard.edu/current-projects/harvard-undergrad-house-renewal/eliot-house-2/",
        "date_accessed": "2026-06-08",
        "document_type": "Official project page"
      },
      {
        "source_label": "Harvard Gazette — Eliot House next for renewal",
        "url": "https://news.harvard.edu/gazette/story/2024/05/next-harvard-undergraduate-residence-up-for-renovation-eliot-house/",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      },
      {
        "source_label": "Harvard Crimson — Eliot renovations timeline and scope",
        "url": "https://www.thecrimson.com/article/2024/12/19/eliot-renovations-begin-june/",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      },
      {
        "source_label": "Harvard Crimson — Eliot renovations to proceed amid funding uncertainty",
        "url": "https://www.thecrimson.com/article/2025/3/31/eliot-house-renovations-ongoing/",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      },
      {
        "source_label": "Harvard Construction Mitigation — weekly Eliot House updates",
        "url": "https://construction.harvard.edu/2026/06/04/week-of-june-8-2026-3/",
        "date_accessed": "2026-06-08",
        "document_type": "Construction notice"
      }
    ]
  },
  {
    "project_id": "HARV-2023-175NHV",
    "project_name": "American Repertory Theater (Goel Center) and Affiliate Housing Complex",
    "project_nickname": "ART & 100 South Campus Drive / 175 North Harvard",
    "status": "Active / Under Construction (late-stage)",
    "project_type": {
      "primary": "Arts / Cultural",
      "secondary": "Mixed-Use Development / New Construction"
    },
    "description": "New construction of the David E. and Stacey L. Goel Center for Creativity & Performance (a new home for the American Repertory Theater) alongside a multi-story Harvard University affiliate graduate housing building and related bike pavilion and public-realm improvements.",
    "purpose": "To relocate the American Repertory Theater to Allston, expand performance and rehearsal facilities, and provide additional graduate affiliate housing adjacent to Harvard's athletics and ERC developments.",
    "location": {
      "campus": "Allston",
      "street_address": "175 North Harvard Street and 100 South Campus Drive",
      "city": "Boston",
      "state": "MA",
      "zip_code": "02134",
      "building_name": "David E. and Stacey L. Goel Center for Creativity & Performance; Harvard University Affiliate Housing",
      "coordinates": "[NOT DISCLOSED]",
      "neighborhood_or_district": "Allston athletics district / near Harvard Business School"
    },
    "timeline": {
      "groundbreaking_date": "2023 (housing earlier, ART mobilization 2024)",
      "estimated_completion": "Fall 2026 (ART); late summer/fall 2026 (housing)",
      "actual_completion": "[NOT DISCLOSED]",
      "duration_months": "36+ [ESTIMATED]",
      "current_phase": "Exterior cladding and interior fit-out; sitework, hardscape, and landscaping ongoing; inspections and fire alarm testing for housing"
    },
    "financials": {
      "total_project_budget": "$122 million ERC estimate for ART and housing package [LOW CONFIDENCE, from third-party construction database]",
      "construction_contract_value": "[NOT DISCLOSED]",
      "funding_source": "Harvard capital plan plus donor gift from David and Stacey Goel for ART; may be supported by broader ERC financing structures",
      "donor_name": "David E. and Stacey L. Goel (ART gift)"
    },
    "scale": {
      "gross_square_footage": "Approx. 68,000 SF for ART plus ~276 housing units [ESTIMATED from press coverage]",
      "floors_above_grade": "ART: 3; housing tower: mid- to high-rise (approx. 14 stories) [ESTIMATED]",
      "floors_below_grade": "1 (parking under housing) [LOW CONFIDENCE]",
      "number_of_units_or_beds": "Approximately 264–276 graduate units",
      "parking_spaces": "Approx. 75 underground spaces (per early filings) [LOW CONFIDENCE]"
    },
    "sustainability": {
      "leed_target": "Likely LEED Gold or better [ESTIMATED]",
      "other_certifications": "ART and housing designed to meet Living Building Challenge or Passive House standards; two Shawmut-built projects at 175 North Harvard targeting LBC Core and/or PHIUS per Harvard sustainability messaging [LOW CONFIDENCE for exact labels]",
      "harvard_sustainability_commitment": "https://sustainable.harvard.edu/our-plan/how-we-build/"
    },
    "design_team": {
      "architect_of_record": "ARC/Architectural Resources Cambridge",
      "design_architect": "Haworth Tompkins (design lead for ART)",
      "landscape_architect": "[NOT DISCLOSED]",
      "structural_engineer": "[NOT DISCLOSED]",
      "mep_engineer": "[NOT DISCLOSED]",
      "owner_representative": "NorthStar Project & Real Estate Services (project manager for housing per trade press) [MEDIUM CONFIDENCE]"
    },
    "construction_team": {
      "general_contractor": "Shawmut Design and Construction (construction manager) [HIGH CONFIDENCE]",
      "construction_manager": "Shawmut Design and Construction",
      "contract_type": "CM-at-Risk / GMP [ESTIMATED]",
      "key_subcontractors": [
        "Charcoalblue (theater and acoustics consultant)",
        "Various specialty theatrical, mass timber, and façade trades [NOT DISCLOSED by name]"
      ],
      "notable_trade_packages": "Mass timber structure for ART; high-performance cladding; theater-specific interiors (balconies, catwalks, stage systems)."
    },
    "harvard_oversight": {
      "harvard_project_manager": "Harvard Capital Projects; specific PM not publicly identified [NOT DISCLOSED]",
      "reporting_entity": "Harvard Capital Projects / Office of the Executive Vice President",
      "school_or_unit_sponsor": "Faculty of Arts and Sciences (ART) and Harvard University Housing / Campus Services (housing)"
    },
    "community_impact": {
      "community_benefits_agreement": "Community review and mitigation commitments via BPDA process; no separate CBA published.",
      "neighborhood_liaison_contacts": "Harvard Construction Mitigation program; Allston development community meetings.",
      "construction_impact_notices": [
        "https://construction.harvard.edu/current-projects/allston-development/artproject100southcampusdrive/",
        "https://construction.harvard.edu/2026/06/01/week-of-june-1-2026-4/",
        "https://construction.harvard.edu/2026/06/02/allston-development-update-june-2026/",
        "https://harvardsquare.com/media_room/harvard-building-project-would-move-a-r-t-to-allston/"
      ]
    },
    "sources": [
      {
        "source_label": "Harvard Construction Mitigation — ART Project & 100 South Campus Drive",
        "url": "https://construction.harvard.edu/current-projects/allston-development/artproject100southcampusdrive/",
        "date_accessed": "2026-06-08",
        "document_type": "Official project page"
      },
      {
        "source_label": "Harvard Construction Mitigation — Allston Development Update June 2026",
        "url": "https://construction.harvard.edu/2026/06/02/allston-development-update-june-2026/",
        "date_accessed": "2026-06-08",
        "document_type": "Construction update"
      },
      {
        "source_label": "School Construction News — topping out of 175 North Harvard mixed-use building",
        "url": "https://schoolconstructionnews.com/2025/01/13/mixed-use-harvard-university-project-celebrates-topping-out/",
        "date_accessed": "2026-06-08",
        "document_type": "Trade news"
      },
      {
        "source_label": "Charcoalblue — ART topping off announcement",
        "url": "https://www.charcoalblue.com/news/view/construction-reaches-topping-off-milestone-for-the-new-home-of-the-american-repertory-theater",
        "date_accessed": "2026-06-08",
        "document_type": "Firm news release"
      },
      {
        "source_label": "New England Council — ART nearing completion",
        "url": "https://www.newenglandcouncil.com/news-article/harvard-universitys-american-repertory-theater-nears-completion-in-allston/",
        "date_accessed": "2026-06-08",
        "document_type": "News brief"
      }
    ]
  },
  {
    "project_id": "HARV-2021-ERC-A",
    "project_name": "Enterprise Research Campus (ERC) Phase A",
    "project_nickname": "ERC Phase A",
    "status": "Active / Punch-list and Fit-out (core buildings operational)",
    "project_type": {
      "primary": "Mixed-Use Development",
      "secondary": "New Construction"
    },
    "description": "First phase of a mixed-use research and innovation district in Allston including two lab buildings, two residential apartment buildings (Verra), a hotel (Atlas), the David Rubenstein Treehouse conference center, structured parking, and public greenway/street network.",
    "purpose": "To create a commercial and academic innovation node adjacent to Harvard Business School and the Science and Engineering Complex, delivering lab, office, residential, hotel, and conference space to support research-industry collaboration and university needs.",
    "location": {
      "campus": "Allston",
      "street_address": "100–112 Western Avenue",
      "city": "Boston",
      "state": "MA",
      "zip_code": "02134",
      "building_name": "Enterprise Research Campus Phase A (Milestone East/West, Verra, Atlas, Rubenstein Treehouse)",
      "coordinates": "[NOT DISCLOSED]",
      "neighborhood_or_district": "Allston / Western Avenue corridor"
    },
    "timeline": {
      "groundbreaking_date": "11/2023",
      "estimated_completion": "Early 2026 (labs, hotel, residences; Treehouse opened late 2025)",
      "actual_completion": "Buildings open and occupied by mid-2026; streetscape balance work ongoing",
      "duration_months": "28–30 [ESTIMATED]",
      "current_phase": "Operational with fit-outs and punch-list; ERC 1.4 streetscape and Western Avenue markings/streetscape construction ongoing"
    },
    "financials": {
      "total_project_budget": "$750 million construction loan plus sponsor equity (Phase A) [LOW CONFIDENCE as total dev cost]",
      "construction_contract_value": "Lab buildings: approx. $290 million (Turner/Janey/J&J JV) [LOW CONFIDENCE]",
      "funding_source": "Private commercial development led by Tishman Speyer and Breakthrough Properties, financed by Otera Capital construction loan; Harvard as landowner and partner.",
      "donor_name": "David Rubenstein (Treehouse naming gift); other donors not disclosed"
    },
    "scale": {
      "gross_square_footage": "Approx. 900,000 SF total Phase A (440,000 SF lab, 343 units residential, 246-room hotel, Treehouse conference center)",
      "floors_above_grade": "Varies by building (labs mid-rise, residential mid/high-rise, hotel tower) [NOT DISCLOSED in detail]",
      "floors_below_grade": "1–2 (parking/garage) [ESTIMATED]",
      "number_of_units_or_beds": "343 residential units (approx. 25% income restricted)",
      "parking_spaces": "Structured parking serving campus, count not publicly summarized [NOT DISCLOSED]"
    },
    "sustainability": {
      "leed_target": "LEED Gold for major buildings; Fitwel for office/lab spaces",
      "other_certifications": "Treehouse targeting Living Building Challenge Core Green Building Certification and Materials Petal; ERC seeking Envision Platinum for infrastructure, 100% electric residential buildings, 38% energy reduction, 60% carbon reduction.",
      "harvard_sustainability_commitment": "https://sustainable.harvard.edu/our-plan/how-we-build/david-rubenstein-treehouse-conference-center-new-construction/"
    },
    "design_team": {
      "architect_of_record": "Henning Larsen (overall), Studio Gang (Treehouse, architecture co-lead), MVRDV and Moody Nolan (residential), Marlon Blackwell (hotel)",
      "design_architect": "Studio Gang (Treehouse), Henning Larsen (masterplan and labs), others as above",
      "landscape_architect": "SCAPE and Utile",
      "structural_engineer": "Arup and others (per project components) [NOT DETAILED]",
      "mep_engineer": "Cosentini (selected components)",
      "owner_representative": "Harvard Allston Land Company / Tishman Speyer development team"
    },
    "construction_team": {
      "general_contractor": "Turner Construction Company (lab buildings, in joint venture with Janey Construction Management and J&J Contractors); Consigli Construction and Smoot Construction (Treehouse, residential, hotel/other components)",
      "construction_manager": "Turner (labs); Consigli/Smoot (other buildings)",
      "contract_type": "Private development CM/GC contracts; likely GMP for major components [ESTIMATED]",
      "key_subcontractors": [
        "Various specialty façade, lab, and MEP subcontractors (not named publicly)"
      ],
      "notable_trade_packages": "Large lab MEP systems; mass timber and advanced envelope for Treehouse; extensive landscape/greenway and stormwater management systems."
    },
    "harvard_oversight": {
      "harvard_project_manager": "Harvard Allston Land Company leadership; specific individual PMs not disclosed",
      "reporting_entity": "Harvard Allston Land Company / Office of the Executive Vice President",
      "school_or_unit_sponsor": "University-wide enterprise (no single school sponsor); HBS and SEAS as adjacent stakeholders"
    },
    "community_impact": {
      "community_benefits_agreement": "ERC includes commitments to affordable housing (25% income-restricted units), minority ownership participation ($30 million equity from Black and Latinx investors), and community programming on the greenway via BPDA approvals.",
      "neighborhood_liaison_contacts": "BPDA project page and Allston development meetings; Harvard Construction Mitigation Allston Development updates.",
      "construction_impact_notices": [
        "http://www.bostonplans.org/projects/development-projects/harvard-enterprise-research-campus-phase-b",
        "https://construction.harvard.edu/category/allston-development-monthly-updates/",
        "https://construction.harvard.edu/2026/06/02/allston-development-update-june-2026/",
        "https://worldconstructionnetwork.com/projects/enterprise-research-campus-massachusetts-usa/"
      ]
    },
    "sources": [
      {
        "source_label": "Harvard Construction Mitigation — Allston Development Update June 2026",
        "url": "https://construction.harvard.edu/2026/06/02/allston-development-update-june-2026/",
        "date_accessed": "2026-06-08",
        "document_type": "Construction update"
      },
      {
        "source_label": "World Construction Network — ERC project overview",
        "url": "https://www.worldconstructionnetwork.com/projects/enterprise-research-campus-massachusetts-usa/",
        "date_accessed": "2026-06-08",
        "document_type": "Project profile"
      },
      {
        "source_label": "Harvard Office for Sustainability — Treehouse case study",
        "url": "https://sustainable.harvard.edu/our-plan/how-we-build/david-rubenstein-treehouse-conference-center-new-construction/",
        "date_accessed": "2026-06-08",
        "document_type": "Sustainability case study"
      },
      {
        "source_label": "Studio Gang — Rubenstein Treehouse project page",
        "url": "https://studiogang.com/projects/david-rubenstein-treehouse/",
        "date_accessed": "2026-06-08",
        "document_type": "Architect project page"
      },
      {
        "source_label": "Boston Real Estate Times — ERC construction managers overview",
        "url": "https://bostonrealestatetimes.com/largest-construction-projects-series-harvard-enterprise-research-campus-transforming-allston-in-boston/",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      }
    ]
  },
  {
    "project_id": "HARV-2025-WJH-PLAZA",
    "project_name": "William James Hall Plaza Renovation",
    "project_nickname": "WJH Plaza Waterproofing and Accessibility",
    "status": "Active / Under Construction",
    "project_type": {
      "primary": "Landscape / Open Space",
      "secondary": "Renovation / Historic Preservation"
    },
    "description": "Multi-phase renovation of the plaza surrounding William James Hall, including replacement of plaza waterproofing and pavers, landscape improvements, and accessibility upgrades from Kirkland Street.",
    "purpose": "To address long-standing waterproofing and structural issues at the WJH plaza, improve accessibility to the main entrance, and soften the public realm with new landscaping.",
    "location": {
      "campus": "Main Campus",
      "street_address": "33 Kirkland Street",
      "city": "Cambridge",
      "state": "MA",
      "zip_code": "02138",
      "building_name": "William James Hall",
      "coordinates": "[NOT DISCLOSED]",
      "neighborhood_or_district": "Harvard Yard / FAS core"
    },
    "timeline": {
      "groundbreaking_date": "01/2025",
      "estimated_completion": "Spring / Summer 2026",
      "actual_completion": "[NOT DISCLOSED]",
      "duration_months": "18 [ESTIMATED]",
      "current_phase": "Exterior plaza demolition, waterproofing, and new paver/landscape installation ongoing in spring 2026"
    },
    "financials": {
      "total_project_budget": "[NOT DISCLOSED]",
      "construction_contract_value": "[NOT DISCLOSED]",
      "funding_source": "FAS capital budget",
      "donor_name": "[NOT DISCLOSED]"
    },
    "scale": {
      "gross_square_footage": "Plaza area approx. 48,000 SF [LOW CONFIDENCE based on historic permit]",
      "floors_above_grade": "[NOT APPLICABLE]",
      "floors_below_grade": "[NOT DISCLOSED] (garage/occupied floor below plaza)",
      "number_of_units_or_beds": "[NOT APPLICABLE]",
      "parking_spaces": "[NOT DISCLOSED] (impacted indirectly by plaza work)"
    },
    "sustainability": {
      "leed_target": "[NOT DISCLOSED]",
      "other_certifications": "Project acts as pilot for LBC Core-aligned landscape and accessibility improvements [LOW CONFIDENCE]",
      "harvard_sustainability_commitment": "https://sustainable.harvard.edu/our-plan/how-we-build/"
    },
    "design_team": {
      "architect_of_record": "Bruner/Cott Architects (campus architect) [HIGH CONFIDENCE]",
      "design_architect": "Bruner/Cott Architects",
      "landscape_architect": "Michael Van Valkenburgh Associates [HIGH CONFIDENCE]",
      "structural_engineer": "Simpson Gumpertz & Heger (SGH)",
      "mep_engineer": "[NOT DISCLOSED]",
      "owner_representative": "FAS Campus Planning / Capital Projects"
    },
    "construction_team": {
      "general_contractor": "G. Greene Construction Co., Inc. [HIGH CONFIDENCE]",
      "construction_manager": "G. Greene Construction Co., Inc.",
      "contract_type": "Lump Sum / CM [LOW CONFIDENCE]",
      "key_subcontractors": [
        "Landscape and sitework subcontractors not named publicly"
      ],
      "notable_trade_packages": "Extensive plaza waterproofing replacement; complex staging and tenting over work zones to manage weather and campus operations."
    },
    "harvard_oversight": {
      "harvard_project_manager": "Anne-Sophie Divenyi, AIA (Harvard project manager) [HIGH CONFIDENCE]",
      "reporting_entity": "Faculty of Arts and Sciences Campus Planning and Capital Projects",
      "school_or_unit_sponsor": "FAS (Department of Psychology and associated programs in WJH)"
    },
    "community_impact": {
      "community_benefits_agreement": "Not applicable; on-campus open-space renovation.",
      "neighborhood_liaison_contacts": "Construction Mitigation notices to WJH occupants and nearby buildings.",
      "construction_impact_notices": [
        "https://construction.harvard.edu/current-projects/faculty-of-arts-sciences-fas-projects/william-james-hall-plaza-renovation-project/",
        "https://construction.harvard.edu/2026/02/13/",
        "https://construction.harvard.edu/category/william-james-hall/",
        "https://www.thecrimson.com/article/2025/5/5/william-james-rennovations-waterproof/"
      ]
    },
    "sources": [
      {
        "source_label": "Harvard Construction Mitigation — William James Hall Plaza project page",
        "url": "https://construction.harvard.edu/current-projects/faculty-of-arts-sciences-fas-projects/william-james-hall-plaza-renovation-project/",
        "date_accessed": "2026-06-08",
        "document_type": "Official project page"
      },
      {
        "source_label": "Harvard Construction Mitigation — general occupant info and completion target",
        "url": "https://construction.harvard.edu/2026/01/23/week-of-january-26-2026-2/",
        "date_accessed": "2026-06-08",
        "document_type": "Construction notice"
      },
      {
        "source_label": "Harvard Crimson — WJH plaza renovation article",
        "url": "https://www.thecrimson.com/article/2025/5/5/william-james-rennovations-waterproof/",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      },
      {
        "source_label": "LinkedIn post by Harvard PM describing WJH plaza design and CM",
        "url": "https://www.linkedin.com/posts/anne-sophie-divenyi-aia-77546414_extensive-renovation-project-on-william-james-activity-7325172415973578752-CWcM/",
        "date_accessed": "2026-06-08",
        "document_type": "LinkedIn post"
      },
      {
        "source_label": "MassDEP construction/demolition notifications referencing G. Greene and WJH plaza work",
        "url": "https://www.mass.gov/doc/constructiondemolition-notifications-2016/download",
        "date_accessed": "2026-06-08",
        "document_type": "Regulatory filing"
      }
    ]
  },
  {
    "project_id": "HARV-2025-BARKER-ROOF",
    "project_name": "Barker Center Roofing Project",
    "project_nickname": "Barker Center Roof Renewal",
    "status": "Active / Nearing Completion (June 2026)",
    "project_type": {
      "primary": "Renovation / Historic Preservation",
      "secondary": "Building Envelope / Roof Replacement"
    },
    "description": "Roof dismantling and installation project at the Barker Center, involving repair and replacement of roofing assemblies and associated access infrastructure (stair tower, scaffolding).",
    "purpose": "To renew the roof system of the historic Barker Center, protecting interior academic spaces and extending the life of the building envelope.",
    "location": {
      "campus": "Main Campus",
      "street_address": "12 Quincy Street",
      "city": "Cambridge",
      "state": "MA",
      "zip_code": "02138",
      "building_name": "Barker Center for the Humanities",
      "coordinates": "[NOT DISCLOSED]",
      "neighborhood_or_district": "Harvard Yard"
    },
    "timeline": {
      "groundbreaking_date": "02/2026 (mobilization)",
      "estimated_completion": "06/2026",
      "actual_completion": "[NOT DISCLOSED — project scheduled to complete June 2026]",
      "duration_months": "4 [ESTIMATED]",
      "current_phase": "Roof replacement and associated work in final phase as of week of June 8, 2026"
    },
    "financials": {
      "total_project_budget": "[NOT DISCLOSED]",
      "construction_contract_value": "[NOT DISCLOSED]",
      "funding_source": "FAS capital maintenance budget",
      "donor_name": "[NOT APPLICABLE]"
    },
    "scale": {
      "gross_square_footage": "Roof area only; building GSF not directly impacted [NOT DISCLOSED]",
      "floors_above_grade": "[NOT APPLICABLE]",
      "floors_below_grade": "[NOT APPLICABLE]",
      "number_of_units_or_beds": "[NOT APPLICABLE]",
      "parking_spaces": "[NOT APPLICABLE]"
    },
    "sustainability": {
      "leed_target": "[NOT DISCLOSED]",
      "other_certifications": "Project complies with Harvard Sustainable Building Standards for envelope upgrades [LOW CONFIDENCE]",
      "harvard_sustainability_commitment": "https://sustainable.harvard.edu/our-plan/how-we-build/"
    },
    "design_team": {
      "architect_of_record": "[NOT DISCLOSED]",
      "design_architect": "[NOT DISCLOSED]",
      "landscape_architect": "[NOT APPLICABLE]",
      "structural_engineer": "[NOT DISCLOSED]",
      "mep_engineer": "[NOT APPLICABLE]",
      "owner_representative": "FAS Capital Projects"
    },
    "construction_team": {
      "general_contractor": "[NOT DISCLOSED]",
      "construction_manager": "[NOT DISCLOSED]",
      "contract_type": "[NOT DISCLOSED]",
      "key_subcontractors": [
        "Roofing contractor not named; scaffolding and stair tower erection subcontractors not named."
      ],
      "notable_trade_packages": "Roofing, scaffolding, stair tower access structures."
    },
    "harvard_oversight": {
      "harvard_project_manager": "FAS Capital Projects staff (not named)",
      "reporting_entity": "FAS Capital Projects",
      "school_or_unit_sponsor": "Faculty of Arts and Sciences"
    },
    "community_impact": {
      "community_benefits_agreement": "Not applicable; short-duration maintenance project.",
      "neighborhood_liaison_contacts": "Construction Mitigation notices to Barker Center occupants and neighbors.",
      "construction_impact_notices": [
        "https://construction.harvard.edu/current-projects/faculty-of-arts-sciences-fas-projects/barker-center-roofing-project/",
        "https://construction.harvard.edu/2026/06/03/week-of-june-8-2026-3/"
      ]
    },
    "sources": [
      {
        "source_label": "Harvard Construction Mitigation — Barker Center roofing project page",
        "url": "https://construction.harvard.edu/current-projects/faculty-of-arts-sciences-fas-projects/barker-center-roofing-project/",
        "date_accessed": "2026-06-08",
        "document_type": "Official project page"
      }
    ]
  },
  {
    "project_id": "HARV-2025-12PALMER",
    "project_name": "12 Palmer Street Renovation",
    "project_nickname": "12 Palmer Renovation / Coop Annex Redevelopment",
    "status": "Active / Under Construction (interior and façade work in 2026)",
    "project_type": {
      "primary": "Administrative / Office",
      "secondary": "Adaptive Reuse / Renovation"
    },
    "description": "Multi-phase renovation of the former Harvard Coop Annex property at 12 Palmer Street to convert the bookstore building into office and retail space, with associated site preparation, interior demolition, window replacement, curtain wall installation, and MEP upgrades.",
    "purpose": "To repurpose an underutilized retail building in Harvard Square into modern office and commercial space as part of Harvard Real Estate's strategy to enliven Palmer Street and adjacent alleys.",
    "location": {
      "campus": "Main Campus / Harvard Square commercial district",
      "street_address": "12 Palmer Street",
      "city": "Cambridge",
      "state": "MA",
      "zip_code": "02138",
      "building_name": "12 Palmer Street (former Coop Annex)",
      "coordinates": "[NOT DISCLOSED]",
      "neighborhood_or_district": "Harvard Square"
    },
    "timeline": {
      "groundbreaking_date": "12/2025 (early mobilization)",
      "estimated_completion": "April 2026 (initial Harvard Real Estate notice) with work still active March 2026",
      "actual_completion": "[NOT DISCLOSED] — scaffolding removal and interior work ongoing March 2026",
      "duration_months": "4–6 [ESTIMATED for main phases]",
      "current_phase": "Scaffolding removal, interior saw-cutting, and miscellaneous interior work as of March 2026; exterior façade work largely complete"
    },
    "financials": {
      "total_project_budget": "[NOT DISCLOSED]",
      "construction_contract_value": "[NOT DISCLOSED]",
      "funding_source": "Harvard Real Estate capital budget",
      "donor_name": "[NOT APPLICABLE]"
    },
    "scale": {
      "gross_square_footage": "[NOT DISCLOSED]",
      "floors_above_grade": "[NOT DISCLOSED] (low-rise commercial building)",
      "floors_below_grade": "[NOT DISCLOSED]",
      "number_of_units_or_beds": "[NOT APPLICABLE]",
      "parking_spaces": "[NOT APPLICABLE]"
    },
    "sustainability": {
      "leed_target": "[NOT DISCLOSED]",
      "other_certifications": "Adaptive reuse expected to follow Harvard sustainable building guidance [LOW CONFIDENCE]",
      "harvard_sustainability_commitment": "https://sustainable.harvard.edu/our-plan/how-we-build/"
    },
    "design_team": {
      "architect_of_record": "[NOT DISCLOSED]",
      "design_architect": "[NOT DISCLOSED]",
      "landscape_architect": "[NOT APPLICABLE]",
      "structural_engineer": "[NOT DISCLOSED]",
      "mep_engineer": "[NOT DISCLOSED]",
      "owner_representative": "Harvard University Housing & Real Estate / Harvard Planning & Design"
    },
    "construction_team": {
      "general_contractor": "Consigli Construction Co., Inc. [HIGH CONFIDENCE]",
      "construction_manager": "Consigli Construction Co., Inc.",
      "contract_type": "CM / GMP [LOW CONFIDENCE]",
      "key_subcontractors": [
        "Various façade, scaffolding, and interior demolition contractors"
      ],
      "notable_trade_packages": "Scaffolding and façade restoration along Palmer Street; interior selective demolition and MEP upgrades in constrained urban alley."
    },
    "harvard_oversight": {
      "harvard_project_manager": "Harvard Real Estate project management; specific PM not named",
      "reporting_entity": "Harvard Real Estate / Campus Services",
      "school_or_unit_sponsor": "Harvard Real Estate (commercial portfolio)"
    },
    "community_impact": {
      "community_benefits_agreement": "Not applicable; small-scale commercial renovation.",
      "neighborhood_liaison_contacts": "Construction notices to Palmer Street abutters via Construction Mitigation and Cambridge DPW coordination.",
      "construction_impact_notices": [
        "https://construction.harvard.edu/current-projects/faculty-of-arts-sciences-fas-projects/12-palmer-renovation-project/",
        "https://construction.harvard.edu/2026/01/23/week-of-january-26-2026-6/",
        "https://construction.harvard.edu/2026/03/16/week-of-march-16-2026-5/"
      ]
    },
    "sources": [
      {
        "source_label": "Harvard Construction Mitigation — 12 Palmer Renovation project page",
        "url": "https://construction.harvard.edu/current-projects/faculty-of-arts-sciences-fas-projects/12-palmer-renovation-project/",
        "date_accessed": "2026-06-08",
        "document_type": "Official project page"
      },
      {
        "source_label": "Construction Mitigation weekly updates with Consigli named",
        "url": "https://construction.harvard.edu/2026/01/23/week-of-january-26-2026-6/",
        "date_accessed": "2026-06-08",
        "document_type": "Construction notice"
      },
      {
        "source_label": "Construction Mitigation update — March 16, 2026 (Consigli managing site)",
        "url": "https://construction.harvard.edu/2026/03/16/week-of-march-16-2026-5/",
        "date_accessed": "2026-06-08",
        "document_type": "Construction notice"
      },
      {
        "source_label": "Harvard Planning project record for 12 Palmer Coop redevelopment",
        "url": "https://harvardplanning.emuseum.com/events/11233/12%20Palmer%20Street%20Coop%20redevelopment%20-%20base%20building",
        "date_accessed": "2026-06-08",
        "document_type": "Internal planning archive"
      }
    ]
  },
  {
    "project_id": "HARV-2024-HBS-CHASE-MCC-DILLON",
    "project_name": "Harvard Business School Chase/McCulloch/Dillon Renovation",
    "project_nickname": "HBS Chase/McCulloch/Dillon Residence and Office Renovations",
    "status": "Active / Under Construction (through Summer 2026)",
    "project_type": {
      "primary": "Student Housing / Dormitory",
      "secondary": "Gut Renovation / Historic Preservation"
    },
    "description": "Extensive renovation of two Harvard Business School student residence halls (Chase Hall and McCulloch Hall) and Dillon House (MBA Admissions office), including complete interior demolition, abatement, and subsequent rebuilding with updated systems and finishes.",
    "purpose": "To modernize HBS residential and administrative facilities, including safety, mechanical systems, and interior layouts, while preserving historic exteriors.",
    "location": {
      "campus": "Allston / Harvard Business School",
      "street_address": "Chase Hall, 34 Harvard Way; McCulloch Hall and Dillon House on HBS campus",
      "city": "Boston",
      "state": "MA",
      "zip_code": "02163",
      "building_name": "Chase Hall, McCulloch Hall, Dillon House",
      "coordinates": "[NOT DISCLOSED]",
      "neighborhood_or_district": "Harvard Business School campus"
    },
    "timeline": {
      "groundbreaking_date": "2024 (enabling and interior demolition)",
      "estimated_completion": "Summer 2026",
      "actual_completion": "[NOT DISCLOSED]",
      "duration_months": "24 [ESTIMATED]",
      "current_phase": "Renovation project underway at HBS through this summer (2026); interior reconstruction and fit-out ongoing"
    },
    "financials": {
      "total_project_budget": "$4–5 million range for Select Demo demolition package only; total project value higher but not disclosed.",
      "construction_contract_value": "[NOT DISCLOSED]",
      "funding_source": "HBS capital funds and philanthropy",
      "donor_name": "[NOT DISCLOSED]"
    },
    "scale": {
      "gross_square_footage": "Chase Hall 50,000 SF; McCulloch Hall 53,000 SF; Dillon House 5,800 SF for Select Demo scope.",
      "floors_above_grade": "4 (Chase, McCulloch); 3 (Dillon)",
      "floors_below_grade": "[NOT DISCLOSED]",
      "number_of_units_or_beds": "Approx. 84 MBA beds in McCulloch; similar in Chase [ESTIMATED]",
      "parking_spaces": "[NOT APPLICABLE]"
    },
    "sustainability": {
      "leed_target": "[NOT DISCLOSED] (HBS projects historically aim for LEED Gold/Platinum) [LOW CONFIDENCE]",
      "other_certifications": "May align with Harvard Sustainable Building Standards.",
      "harvard_sustainability_commitment": "https://sustainable.harvard.edu/our-plan/how-we-build/"
    },
    "design_team": {
      "architect_of_record": "[NOT DISCLOSED] (HBS campus architects, possibly ARC or other)",
      "design_architect": "[NOT DISCLOSED]",
      "landscape_architect": "[NOT APPLICABLE]",
      "structural_engineer": "[NOT DISCLOSED]",
      "mep_engineer": "[NOT DISCLOSED]",
      "owner_representative": "HBS Facilities / Planning & Design"
    },
    "construction_team": {
      "general_contractor": "Suffolk Construction Co., Inc. [HIGH CONFIDENCE]",
      "construction_manager": "Suffolk Construction Co., Inc.",
      "contract_type": "CM-at-Risk / GMP [ESTIMATED]",
      "key_subcontractors": [
        "Select Demo Services, LLC (interior demolition and abatement contractor)"
      ],
      "notable_trade_packages": "Complete interior demolition and abatement of two residence halls and Dillon House, including ACM abatement and extensive interior rebuild."
    },
    "harvard_oversight": {
      "harvard_project_manager": "HBS Facilities / Capital Projects staff (names not disclosed)",
      "reporting_entity": "Harvard Business School",
      "school_or_unit_sponsor": "Harvard Business School"
    },
    "community_impact": {
      "community_benefits_agreement": "Not applicable; internal campus renovation.",
      "neighborhood_liaison_contacts": "HBS campus communications; Construction Mitigation Allston Development updates.",
      "construction_impact_notices": [
        "https://construction.harvard.edu/2026/06/02/allston-development-update-june-2026/",
        "https://www.selectdemo.com/harvard-business-school-chase-mcculloch-halls-and-dillon-house/"
      ]
    },
    "sources": [
      {
        "source_label": "Harvard Construction Mitigation — Allston Development Update (HBS section)",
        "url": "https://construction.harvard.edu/2026/06/02/allston-development-update-june-2026/",
        "date_accessed": "2026-06-08",
        "document_type": "Construction update"
      },
      {
        "source_label": "Select Demo Services — HBS Chase, McCulloch, Dillon project description",
        "url": "https://www.selectdemo.com/post/harvard-business-school-chase-mcculloch-halls-and-dillon-house",
        "date_accessed": "2026-06-08",
        "document_type": "Contractor project description"
      }
    ]
  },
  {
    "project_id": "HARV-2023-HMS-BLDGC",
    "project_name": "Harvard Medical School Building C / Bertarelli Building Renovation",
    "project_nickname": "HMS Building C Atrium and Modernization (Bertarelli Building)",
    "status": "Active / Under Construction",
    "project_type": {
      "primary": "Healthcare / Medical (Longwood)",
      "secondary": "Renovation / Historic Preservation"
    },
    "description": "Major renovation of Harvard Medical School's Building C, including transformation of the central courtyard into an expansive skylighted atrium, modernization of interior research and collaboration spaces, and building systems upgrades, with the building to be renamed the Bertarelli Building upon completion.",
    "purpose": "To modernize a 119-year-old historic marble building for contemporary biomedical research and therapeutic science, improve collaboration space, and support the HMS Therapeutics Initiative, funded by a $75 million Bertarelli gift.",
    "location": {
      "campus": "Longwood Medical Area",
      "street_address": "240 Longwood Avenue",
      "city": "Boston",
      "state": "MA",
      "zip_code": "02115",
      "building_name": "Building C (future Bertarelli Building)",
      "coordinates": "[NOT DISCLOSED]",
      "neighborhood_or_district": "Longwood Medical Area"
    },
    "timeline": {
      "groundbreaking_date": "02/2025",
      "estimated_completion": "10/2026",
      "actual_completion": "[NOT DISCLOSED]",
      "duration_months": "20 [ESTIMATED]",
      "current_phase": "Renovation underway with façade restoration complete and interior/atrium construction in progress as of 2025–2026"
    },
    "financials": {
      "total_project_budget": "$75 million gift from Ernesto Bertarelli (likely total project budget of this magnitude)",
      "construction_contract_value": "[NOT DISCLOSED]",
      "funding_source": "Bertarelli Foundation gift plus HMS capital funds",
      "donor_name": "Ernesto S.M. Bertarelli"
    },
    "scale": {
      "gross_square_footage": "[NOT DISCLOSED] (building is one of five HMS marble quad buildings)",
      "floors_above_grade": "[NOT DISCLOSED] (historic multi-story lab/academic building)",
      "floors_below_grade": "[NOT DISCLOSED]",
      "number_of_units_or_beds": "[NOT APPLICABLE]",
      "parking_spaces": "[NOT APPLICABLE]"
    },
    "sustainability": {
      "leed_target": "[NOT DISCLOSED] (modernization expected to align with HMS sustainable building standards)",
      "other_certifications": "[NOT DISCLOSED]",
      "harvard_sustainability_commitment": "https://campusplanning.hms.harvard.edu/planning-design-construction"
    },
    "design_team": {
      "architect_of_record": "Architectural Resources Cambridge (ARC) [LOW–MEDIUM CONFIDENCE, based on HMS design partnerships]",
      "design_architect": "ARC (for lobby and atrium components) [LOW CONFIDENCE]",
      "landscape_architect": "[NOT DISCLOSED]",
      "structural_engineer": "[NOT DISCLOSED]",
      "mep_engineer": "[NOT DISCLOSED]",
      "owner_representative": "HMS Planning, Design & Construction Office"
    },
    "construction_team": {
      "general_contractor": "Shawmut Design and Construction [MEDIUM CONFIDENCE — referenced by HMS communications and social media posts as GC for Building C]",
      "construction_manager": "Shawmut Design and Construction",
      "contract_type": "CM-at-Risk / GMP [ESTIMATED]",
      "key_subcontractors": [
        "Specialty façade and atrium-glazing contractors (not named publicly)"
      ],
      "notable_trade_packages": "Atrium structure and skylight, interior lab and collaboration space modernization, and complex work in a historic marble-clad structure."
    },
    "harvard_oversight": {
      "harvard_project_manager": "HMS Planning, Design & Construction PM (not named)",
      "reporting_entity": "Harvard Medical School",
      "school_or_unit_sponsor": "Harvard Medical School (Therapeutics Initiative and basic science departments)"
    },
    "community_impact": {
      "community_benefits_agreement": "Not applicable; interior campus modernization.",
      "neighborhood_liaison_contacts": "HMS campus communications; no separate municipal CBA.",
      "construction_impact_notices": [
        "https://www.thecrimson.com/article/2025/2/24/hms-renovates-building-c/",
        "https://www.bizjournals.com/boston/news/2025/02/12/hms-building-c-redesign-construction.html",
        "https://hms.harvard.edu/about-hms/office-dean/messages/big-news-about-building-c",
        "https://www.eurekalert.org/news-releases/979195"
      ]
    },
    "sources": [
      {
        "source_label": "Harvard Crimson — construction on HMS Building C begins",
        "url": "https://www.thecrimson.com/article/2025/2/24/hms-renovates-building-c/",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      },
      {
        "source_label": "Boston Business Journal — HMS Building C redesign and construction",
        "url": "https://www.bizjournals.com/boston/news/2025/02/12/hms-building-c-redesign-construction.html",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      },
      {
        "source_label": "HMS Dean's message — big news about Building C",
        "url": "https://hms.harvard.edu/about-hms/office-dean/messages/big-news-about-building-c",
        "date_accessed": "2026-06-08",
        "document_type": "Official communication"
      },
      {
        "source_label": "EurekAlert — Bertarelli pledge and Building C atrium plans",
        "url": "https://www.eurekalert.org/news-releases/979195",
        "date_accessed": "2026-06-08",
        "document_type": "Press release"
      },
      {
        "source_label": "Lifestyles Magazine / philanthropic coverage — construction underway on Building C",
        "url": "https://lifestylesmagazine.com/latest-news/75-million-gift-from-ernesto-s-m-bertarelli-launches-rejuvenation-of-medical-school/",
        "date_accessed": "2026-06-08",
        "document_type": "News article"
      }
    ]
  }
]
```


## Section 3: General Contractor Profiles (JSON Records)

```json
[
  {
    "gc_id": "GC-CONSIGLI",
    "legal_name": "Consigli Construction Co., Inc.",
    "trade_name": "Consigli Construction",
    "headquarters": {
      "street": "72 Summer Street",
      "city": "Milford",
      "state": "MA",
      "zip": "01757"
    },
    "regional_offices": [
      "Boston, MA",
      "Cambridge, MA",
      "Washington, DC",
      "New York, NY",
      "Portland, ME",
      "Hartford, CT",
      "Caribbean offices (Puerto Rico, USVI)"
    ],
    "founded_year": "1905",
    "ownership_structure": "Private, 100% employee-owned (ESOP)",
    "parent_company": "[NOT APPLICABLE]",
    "subsidiaries": [
      "[NOT DISCLOSED] (operates as single corporate entity)"
    ],
    "employee_count": "1,600+ employees",
    "annual_revenue_estimate": "$3 billion (approximate annual revenue)",
    "ens_ranking": "Regularly listed in ENR Top 100/Top 400 contractors (specific 2025 rank [NOT DISCLOSED])",
    "bonding_capacity": "[NOT DISCLOSED] (described as large regional CM with significant bonding capacity)",
    "leadership": {
      "ceo_or_president": "Anthony Consigli",
      "coo": "[NOT DISCLOSED]",
      "regional_vp_new_england": "Multiple regional project executives; names vary by office [NOT DISCLOSED]",
      "project_executive_on_harvard_projects": "Project executives not named publicly for Pritzker Hall or 12 Palmer [NOT DISCLOSED]",
      "superintendent_on_site": "Site superintendents not named publicly [NOT DISCLOSED]"
    },
    "harvard_relationship": {
      "total_harvard_projects_active": "At least 2 active projects (Pritzker Hall [MEDIUM CONFIDENCE], 12 Palmer Renovation [HIGH CONFIDENCE]); additional ongoing work likely in campus portfolio [LOW CONFIDENCE]",
      "harvard_project_ids": [
        "HARV-2025-PRITZKER [MEDIUM CONFIDENCE]",
        "HARV-2025-12PALMER"
      ],
      "known_past_harvard_projects": [
        "Smith Campus Center renovation (construction manager)",
        "Winthrop House Renewal (construction manager)",
        "Gore Hall Complex (House Renewal, ENR-awarded project)",
        "Newell & Weld Boathouses renovation"
      ],
      "estimated_total_value_at_harvard": "$500+ million cumulative across multiple projects [ESTIMATED, LOW CONFIDENCE]",
      "years_working_with_harvard": "At least since early House Renewal phases (circa 2010s)"
    },
    "specializations": [
      "Higher Education",
      "Laboratory / Life Sciences",
      "Historic Renovation",
      "Student Housing",
      "Conference and Common Spaces"
    ],
    "notable_other_clients": [
      "Massachusetts Institute of Technology (MIT)",
      "Boston College",
      "Brown University",
      "Yale University",
      "UMass system"
    ],
    "certifications": [
      "Union-signatory on selected projects",
      "Strong safety and sustainability programs; not a certified MBE/WBE (family-owned ESOP)"
    ],
    "union_affiliation": "Mixed; employs both union and open-shop labor depending on region and project.",
    "safety_record": "Recognized for safety performance; detailed OSHA incident rate not disclosed.",
    "recent_news": [
      {
        "headline": "Consigli expands in DC with new project executives",
        "url": "https://www.wbcnet.org/member_news/consigli-expands-in-dc-with-new-hires/",
        "date": "2023-10-30"
      },
      {
        "headline": "ENR award for Harvard Gore Hall Complex House Renewal",
        "url": "https://www.enr.com/articles/45992-award-of-merit-renovationrestoration-and-excellence-in-safety-best-project-harvard-university-gore-hall-complex",
        "date": "2019-10-01"
      },
      {
        "headline": "Harvard Club profile of Anthony Consigli and Harvard work",
        "url": "https://www.harvardclub.com/anthony-consigli/",
        "date": "2022-05-01"
      }
    ],
    "sources": [
      "https://www.consigli.com/",
      "https://www.harvardclub.com/anthony-consigli/",
      "https://www.enr.com/articles/45992-award-of-merit-renovationrestoration-and-excellence-in-safety-best-project-harvard-university-gore-hall-complex",
      "https://www.consigli.com/project/schwartz-common-and-pavilion/",
      "https://construction.harvard.edu/2026/01/23/week-of-january-26-2026-6/"
    ]
  },
  {
    "gc_id": "GC-SHAWMUT",
    "legal_name": "Shawmut Design and Construction, Inc.",
    "trade_name": "Shawmut Design and Construction",
    "headquarters": {
      "street": "560 Harrison Avenue",
      "city": "Boston",
      "state": "MA",
      "zip": "02118"
    },
    "regional_offices": 

---

## References

1. [Harvard Land Development Plans for Allston](https://www.harvardmagazine.com/2025/03/harvard-land-development-plans-allston) - Harvard presents its 10-year plan for institutional development in Allston.

2. [2026 – Harvard Construction Mitigation](https://construction.harvard.edu/2026/)

3. [Pritzker Hall - Harvard Construction Mitigation](https://construction.harvard.edu/current-projects/allston-development/new-fas-building/) - About this Project · Mobilization began the week of June 16, 2025. · Construction is scheduled for s...

4. [Allston Development Update June 2026](https://construction.harvard.edu/2026/06/02/allston-development-update-june-2026/)

5. [Construction on HMS Building C Begins After $75 Million Donation](https://www.thecrimson.com/article/2025/2/24/hms-renovates-building-c/) - Construction is underway on Harvard Medical School's Building C following a $75 million gift from Er...

6. [Eliot House Renovation Project - Harvard Construction Mitigation](https://construction.harvard.edu/current-projects/harvard-undergrad-house-renewal/eliot-house-2/) - Harvard House Renewal has engaged contractors to renovate Eliot House, one of Harvard's undergraduat...

7. [12 Palmer Renovation Project - Harvard Construction Mitigation](https://construction.harvard.edu/current-projects/faculty-of-arts-sciences-fas-projects/12-palmer-renovation-project/) - The renovation project is targeting an April 2026 completion date. Additional notices will be shared...

8. [Barker Center Roofing Project - Harvard Construction Mitigation](https://construction.harvard.edu/current-projects/faculty-of-arts-sciences-fas-projects/barker-center-roofing-project/)

9. [William James Hall Plaza Renovation Project](https://construction.harvard.edu/current-projects/faculty-of-arts-sciences-fas-projects/william-james-hall-plaza-renovation-project/) - William James Hall Plaza Renovation Project. Project Information. As part of the Harvard University'...

10. [Allston Development Monthly Update January 2025](https://construction.harvard.edu/2025/01/06/january-2025/) - Enterprise Research Campus Phase A Development work is underway of the future Enterprise Research Ca...

11. [$75 million gift from Ernesto S.M. Bertarelli launches rejuvenation of ...](https://lifestylesmagazine.com/latest-news/75-million-gift-from-ernesto-s-m-bertarelli-launches-rejuvenation-of-medical-school/)

12. [Mixed-Use Harvard University Project Celebrates Topping Out](https://schoolconstructionnews.com/2025/01/13/mixed-use-harvard-university-project-celebrates-topping-out/) - The project is part of a larger transformation of 175 North Harvard Street, which includes the new h...

13. [Harvard University Begins Construction on Enterprise Research ...](https://www.tradelineinc.com/news/2023-11/harvard-university-begins-construction-enterprise-research-campus) - Breakthrough Properties is responsible for building, leasing, and operating the research facilities,...

14. [Top Development & Construction Projects: Harvard Enterprise ...](https://bostonrealestatetimes.com/largest-construction-projects-series-harvard-enterprise-research-campus-transforming-allston-into-a-global-innovation-hub/) - BOSTON–The Harvard Enterprise Research Campus (ERC) is a transformative nine-acre development in Bos...

15. [For Our Members, With Our Members - iupatdc35](https://iupatdc35.org/for-our-members-with-our-members/) - ... general contractor, Consigli, and together we informed our ... Harvard Pritzker Hall; Harvard El...

16. [Owen Tyson - Project Engineer | Consigli Construction | LinkedIn](https://www.linkedin.com/in/owen-tyson-2822bb1b9) - Consigli Construction Co., Inc. Sep 2025 - Present 10 months. Boston, MA. Harvard University's Pritz...

17. [Schwartz Common and Pavilion - Consigli Construction](https://www.consigli.com/project/schwartz-common-and-pavilion/) - To create a new gathering space in the heart of its well-traveled Commons, Harvard Business School e...

18. [Enterprise Research Campus, Massachusetts, USA](https://www.worldconstructionnetwork.com/projects/enterprise-research-campus-massachusetts-usa/) - Harvard University’s Enterprise Research Campus (ERC) in Boston, Massachusetts, US, is a mixed-use u...

19. [Week of May 23, 2026 – Harvard Construction Mitigation](https://construction.harvard.edu/2026/05/22/week-of-may-23-2026/) - Harvard University homepage · HARVARD.EDU ... Categories: Eliot House. The following summarizes the ...

20. [Week of January 26, 2026 - Harvard Construction Mitigation](https://construction.harvard.edu/2026/01/23/week-of-january-26-2026-6/) - The following summarizes the work planned at 12 Palmer St for the week of January 26. ... Consigli w...

21. [Week of March 16, 2026 – Harvard Construction Mitigation](https://construction.harvard.edu/2026/03/16/week-of-march-16-2026-5/) - Harvard University homepage · HARVARD.EDU ... The following summarizes the work planned at 12 Palmer...

22. [Pritzker Hall Still Nearly $40 Million Short of Fundraising Goal as ...](https://www.thecrimson.com/article/2026/3/11/pritzker-hall-funding-shortfall/) - Construction on Pritzker Hall began in June 2025 and is expected to conclude in December 2027. Locat...

23. [Penny Pritzker Gives $100 Million for New Harvard Economics Facility](https://www.harvardmagazine.com/2021/09/penny-pritzker-100-million-new-harvard-economics-building) - Penny Pritzker '81, a member of the Harvard Corporation since 2018, has made a $100-million commitme...

24. [Gift from Penny Pritzker '81 to spark new era for Harvard economics](https://news.harvard.edu/gazette/story/2021/09/gift-from-penny-pritzker-81-to-spark-new-era-for-harvard-economics/) - Gift from Harvard alumna Penny Pritzker to support collaboration and connection in pursuit of soluti...

25. [Updated Harvard Sustainable Building Standards advance climate ...](https://news.harvard.edu/gazette/story/newsplus/updated-harvard-sustainable-building-standards-advance-climate-health-and-equity/) - Harvard University released its 2024 Sustainable Building Standards, which mark the most significant...

26. [How We Build - Harvard Office for Sustainability](https://sustainable.harvard.edu/our-plan/how-we-build/) - Harvard is accelerating sustainable building to enhance health, productivity, and quality of life on...

27. [Harvard's Sustainable Building Standards](https://sustainable.harvard.edu/our-plan/how-we-build/sustainable-building-standards/) - Harvard’s Sustainable Building Standards incorporate holistic requirements for significant emissions...

28. [Harvard receives first LBC Core certifications for 3 major ...](https://news.harvard.edu/gazette/story/newsplus/harvard-receives-first-lbc-core-certifications-for-3-major-sustainable-renovations/) - With the recent approval of its first three projects under Living Future's rigorous Living Building ...

29. [Extensive Renovation Project on William James Plaza To Continue Through Spring 2026 | News | The Harvard Crimson](https://www.thecrimson.com/article/2025/5/5/william-james-rennovations-waterproof/) - Harvard began construction on the William James Plaza at the start of this year, launching the first...

30. [Eliot Renovations To Proceed As Planned Amid Funding Uncertainty](https://www.thecrimson.com/article/2025/3/31/eliot-house-renovations-ongoing/) - Renovations to Eliot House are on schedule to begin after Commencement and conclude by fall 2027 — d...

31. [Bondholder Information - Office of Treasury Management](https://otm.finance.harvard.edu/pages/bondholder-information-0)

32. [David Rubenstein Treehouse Conference Center](https://sustainable.harvard.edu/our-plan/how-we-build/david-rubenstein-treehouse-conference-center-new-construction/) - The David Rubenstein Treehouse is a new 55,000 square foot Conference center that meets Harvard’s Su...

