#!/usr/bin/env python3
"""A01 chunk prep: emit JSON payloads for rows [start..end] (1-indexed data rows) of a batch-01 CSV."""
import csv, json, sys, re

BASE = "/Users/zackhanna/Desktop/Enlaye to Notion/Big Data/batch-01/"
fname, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

# company string -> notion page id (from company-cache.md, core-name rule)
def page(u): return "https://app.notion.com/p/" + u.replace("-", "")
COMPANIES = {
    "bechtel group": "18490644-d524-80ff-8307-e94405919579",
    "bechtel national": "30a90644-d524-8037-8b5f-e3134e999f7d",
    "bechtel power": "2b590644-d524-8039-8fb4-ce11364a6bdc",
    "kiewit": "17b90644-d524-8055-88ec-f7f399f27e9d",
    "zachry group": "37b90644-d524-813a-a37d-e8d13fa3c23d",
    "gilbane": "17b90644-d524-808d-b137-f747f6931e22",
    "suffolk construction": "17b90644-d524-8044-9514-eda61dd449ae",
    "sundt": "22b90644-d524-8027-af9b-e3c3761a7fb7",
    "hitt": "30a90644-d524-80ef-a7d5-f533e2296b88",
    "consigli building group": "19990644-d524-801a-a283-e806cb9b69b1",
    "clayco": "19990644-d524-80e6-9107-fd693a9ad1e7",
    "shawmut design and construction": "19990644-d524-8021-a4a6-f0a6321589f6",
    "flatirondragados": "24690644-d524-8067-94e4-c40fbc9c089f",
    "the middlesex corporation": "1ce90644-d524-809e-ab40-e6e6c0a21c76",
    "o&g industries": "1cf90644-d524-80bf-9654-e76d70a3ad7d",
    "dellbrook | jks": "19990644-d524-80ac-a13b-cdd8cd7a0946",
    "cianbro": "1cf90644-d524-8019-a5b9-d4d9851426fb",
    "branch group": "26890644-d524-8050-83b7-e663089b3faf",
    "kbe building corporation": "1cf90644-d524-802a-ac06-ea175f0df1fe",
    "fontaine bros.": "19990644-d524-80cb-b37f-d7f58bc63bda",
    "jingoli": "37b90644-d524-8127-824d-f2c6e9f55131",
    "alberici": "27990644-d524-802f-9f84-f3d1fc8af395",
    "alberici constructors, inc.": "37b90644-d524-8129-8d57-fbca3d20307b",
}

def resolve_company(s):
    t = s.strip().lower()
    # exact-ish direct hits
    if t in COMPANIES: return COMPANIES[t]
    # core-name rules
    if "bechtel national" in t: return COMPANIES["bechtel national"]
    if "bechtel power" in t: return COMPANIES["bechtel power"]
    if "bechtel" in t: return COMPANIES["bechtel group"]
    if "kiewit" in t: return COMPANIES["kiewit"]
    if "zachry" in t: return COMPANIES["zachry group"]
    if "gilbane" in t: return COMPANIES["gilbane"]
    if "suffolk" in t: return COMPANIES["suffolk construction"]
    if "sundt" in t: return COMPANIES["sundt"]
    if "hitt" in t: return COMPANIES["hitt"]
    if "consigli" in t: return COMPANIES["consigli building group"]
    if "clayco" in t: return COMPANIES["clayco"]
    if "shawmut" in t: return COMPANIES["shawmut design and construction"]
    if "flatiron" in t: return COMPANIES["flatirondragados"]
    if "middlesex" in t: return COMPANIES["the middlesex corporation"]
    if "o&g" in t: return COMPANIES["o&g industries"]
    if "dellbrook" in t: return COMPANIES["dellbrook | jks"]
    if "cianbro" in t: return COMPANIES["cianbro"]
    if t == "branch" or "branch group" in t or "branch builds" in t: return COMPANIES["branch group"]
    if "kbe" in t: return COMPANIES["kbe building corporation"]
    if "fontaine" in t: return COMPANIES["fontaine bros."]
    if "jingoli" in t or "j.j. white" in t: return COMPANIES["jingoli"]
    if "alberici constructors" in t: return COMPANIES["alberici constructors, inc."]
    if "alberici" in t: return COMPANIES["alberici"]
    return None

LOC_OPTIONS = ["USA","France","Europe","Portugal","Canada","Quebec","Sweden","UK","Netherlands","New York City","Germany","Ontario","Illinois","Massachusetts","South America","Maryland","UAE","Indiana","Colorado","Boston","Florida","Virginia","North Carolina","Morocco","Africa","Denmark","Norway","California","Texas","London","Michigan","San Francisco","Missouri","Pennsylvania","Melbourne","Australia","Jersey","Belgium","Japan","Italy","Switzerland","Thailand","Asia","Saudi Arabia","Hong Kong","Maine","Lebanon","Spain","New Hampshire","Vermont","Connecticut","Rhode Island","Mexico","Washington DC","Delaware","Tennessee","Kansas","Georgia","Arizona","New York","Iowa","Minnesota","Wisconsin","Louisiana","Washington","British Columbia","Ohio","North Dakota","South Korea","New Jersey","Nevada","South Carolina","Alberta","Singapore","New Zealand","India","Chile","Paris","Idaho","Miami","Oregon"]

def map_location(loc):
    if not loc: return None
    parts = [p.strip() for p in loc.split(",")]
    if "district of columbia" in loc.lower(): return "Washington DC"
    # try state (second-to-last for US strings), then any part
    for cand in reversed(parts):
        for o in LOC_OPTIONS:
            if cand.lower() == o.lower(): return o
    # Washington state vs DC handled above; "United States" -> USA
    if "united states" in loc.lower(): return "USA"
    return None

FQ_RULES = [
    (r"chief executive|\bceo\b", "CEO"),
    (r"vice president|\bvp\b|\bsvp\b|\bevp\b", "Vice President"),
    (r"president", "President"),
    (r"director", "Director"),
    (r"superintendent", "Superintendent"),
    (r"principal", "Principal"),
    (r"safety|ehs|hse", "Safety"),
    (r"\brisk\b", "Risk"),
    (r"\bbim\b", "BIM"),
    (r"\bvdc\b|virtual design", "VDC"),
    (r"preconstruction|pre-construction", "Preconstruction"),
    (r"procurement|supply chain", "Procurement"),
    (r"estimat", "Cost Estimation"),
    (r"business development", "Business Development"),
    (r"innovation", "Innovation"),
    (r"\bit\b|information technology|technology officer|\bcio\b", "IT"),
    (r"finance|financial|\bcfo\b|controller", "Finance"),
    (r"legal|counsel", "Legal"),
    (r"contract", "Contract"),
    (r"sustainab", "Sustainability"),
    (r"quality|qa/qc", "QHSE"),
    (r"civil", "Civil"),
    (r"environment", "Environment"),
]

def map_fq(title):
    t = (title or "").lower()
    out = []
    for pat, opt in FQ_RULES:
        if re.search(pat, t) and opt not in out:
            out.append(opt)
        if ("president" in t) and opt == "President" and "Vice President" in out:
            if "President" in out: out.remove("President")
    return out[:3]

ICONS = ["user_gray","user_brown","user_blue","user_green","user_orange","user_purple","user_red","user_yellow","user_pink"]

def norm_li(u):
    u = (u or "").strip().lower()
    return u[:-1] if u.endswith("/") else u

rows = list(csv.DictReader(open(BASE + fname)))
out = []
for i in range(start, min(end, len(rows)) + 1):
    r = rows[i - 1]
    comp = r["Company Name"].strip()
    cid = resolve_company(comp)
    name = r["Full Name"].strip()
    li = norm_li(r["LinkedIn Profile"])
    email = (r.get("Work Email") or "").strip()
    title = (r.get("Job Title") or "").strip()
    rec = {
        "row": i, "name": name, "company_csv": comp, "company_id": cid,
        "linkedin": li, "email": email, "title": title,
        "location_opt": map_location(r.get("Location", "")),
        "fq": map_fq(title),
        "icon": "/icons/" + ICONS[i % len(ICONS)] + ".svg",
    }
    if cid:
        props = {
            "Name": name,
            "Function": title,
            "Company": json.dumps([page(cid)]),
            "LinkedIn": li,
        }
        if email: props["Email"] = email
        if rec["location_opt"]: props["Location"] = json.dumps([rec["location_opt"]])
        if rec["fq"]: props["Function Qualification"] = json.dumps(rec["fq"])
        body = "## Role\n- " + (title or "Role n/a") + " at " + comp + " ([LinkedIn](" + li + "))" if li else "## Role\n- " + title + " at " + comp
        rec["page"] = {"properties": props, "icon": rec["icon"], "content": body}
    out.append(rec)
print(json.dumps(out, indent=1))
