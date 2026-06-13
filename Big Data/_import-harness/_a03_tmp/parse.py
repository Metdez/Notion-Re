import csv, json, re, sys

path = sys.argv[1]
out = sys.argv[2]

COMP = [
 (re.compile(r'bechtel national', re.I), 'Bechtel National', '30a90644-d524-8037-8b5f-e3134e999f7d'),
 (re.compile(r'bechtel power', re.I), 'Bechtel Power', '2b590644-d524-8039-8fb4-ce11364a6bdc'),
 (re.compile(r'bechtel', re.I), 'Bechtel Group', '18490644-d524-80ff-8307-e94405919579'),
 (re.compile(r'kiewit', re.I), 'Kiewit', '17b90644-d524-8055-88ec-f7f399f27e9d'),
 (re.compile(r'zachry', re.I), 'Zachry Group', '37b90644-d524-813a-a37d-e8d13fa3c23d'),
 (re.compile(r'gilbane', re.I), 'Gilbane', '17b90644-d524-808d-b137-f747f6931e22'),
 (re.compile(r'suffolk', re.I), 'Suffolk Construction', '17b90644-d524-8044-9514-eda61dd449ae'),
 (re.compile(r'sundt', re.I), 'Sundt', '22b90644-d524-8027-af9b-e3c3761a7fb7'),
 (re.compile(r'hitt', re.I), 'HITT', '30a90644-d524-80ef-a7d5-f533e2296b88'),
 (re.compile(r'consigli', re.I), 'Consigli Building Group', '19990644-d524-801a-a283-e806cb9b69b1'),
 (re.compile(r'clayco', re.I), 'Clayco', '19990644-d524-80e6-9107-fd693a9ad1e7'),
 (re.compile(r'shawmut', re.I), 'Shawmut Design and Construction', '19990644-d524-8021-a4a6-f0a6321589f6'),
 (re.compile(r'flatiron\s*dragados', re.I), 'FlatironDragados', '24690644-d524-8067-94e4-c40fbc9c089f'),
 (re.compile(r'middlesex', re.I), 'The Middlesex Corporation', '1ce90644-d524-809e-ab40-e6e6c0a21c76'),
 (re.compile(r'o&g industries', re.I), 'O&G Industries', '1cf90644-d524-80bf-9654-e76d70a3ad7d'),
 (re.compile(r'dellbrook', re.I), 'Dellbrook | JKS', '19990644-d524-80ac-a13b-cdd8cd7a0946'),
 (re.compile(r'cianbro', re.I), 'Cianbro', '1cf90644-d524-8019-a5b9-d4d9851426fb'),
 (re.compile(r'^branch$', re.I), 'Branch Group', '26890644-d524-8050-83b7-e663089b3faf'),
 (re.compile(r'kbe building', re.I), 'KBE Building Corporation', '1cf90644-d524-802a-ac06-ea175f0df1fe'),
 (re.compile(r'fontaine', re.I), 'Fontaine Bros.', '19990644-d524-80cb-b37f-d7f58bc63bda'),
 (re.compile(r'jingoli|j\.j\. white', re.I), 'Jingoli', '37b90644-d524-8127-824d-f2c6e9f55131'),
 (re.compile(r'alberici constructors', re.I), 'Alberici Constructors, Inc.', '37b90644-d524-8129-8d57-fbca3d20307b'),
 (re.compile(r'alberici', re.I), 'Alberici', '27990644-d524-802f-9f84-f3d1fc8af395'),
]

STATES = {"Illinois","Massachusetts","Maryland","Indiana","Colorado","Florida","Virginia","North Carolina","California","Texas","Michigan","Missouri","Pennsylvania","Maine","New Hampshire","Vermont","Connecticut","Rhode Island","Delaware","Tennessee","Kansas","Georgia","Arizona","New York","Iowa","Minnesota","Wisconsin","Louisiana","Washington","Ohio","North Dakota","New Jersey","Nevada","South Carolina","Idaho","Oregon"}
METRO = [("Greater Chicago","Illinois"),("Greater Boston","Massachusetts"),("Boston","Massachusetts"),("Greater Phoenix","Arizona"),("Greater St. Louis","Missouri"),("St Louis","Missouri"),("St. Louis","Missouri"),("New York City Metropolitan","New York"),("Greater Houston","Texas"),("Dallas-Fort Worth","Texas"),("San Francisco Bay Area","California"),("Greater Seattle","Washington"),("Los Angeles","California"),("San Diego","California"),("Washington DC-Baltimore","Washington DC"),("Greater Philadelphia","Pennsylvania"),("Atlanta Metropolitan","Georgia"),("Greater Hartford","Connecticut"),("Denver Metropolitan","Colorado"),("Greater Minneapolis","Minnesota"),("Miami-Fort Lauderdale","Florida"),("Greater Tampa","Florida"),("Greater Orlando","Florida"),("Portland, Oregon","Oregon"),("Greater Milwaukee","Wisconsin"),("Greater Madison","Wisconsin"),("Omaha Metropolitan","USA"),("Greater Cleveland","Ohio"),("Cincinnati Metropolitan","Ohio"),("Columbus, Ohio","Ohio"),("Greater Pittsburgh","Pennsylvania"),("District of Columbia","Washington DC"),("Las Vegas","Nevada"),("Greater Richmond","Virginia"),("Charlotte Metro","North Carolina"),("Raleigh-Durham","North Carolina"),("Greater Savannah","Georgia"),("Austin, Texas Metropolitan","Texas"),("San Antonio","Texas"),("Greater Sacramento","California"),("Salt Lake City","USA"),("Nashville Metropolitan","Tennessee"),("Greater Indianapolis","Indiana"),("Kansas City Metropolitan","Missouri"),("Knoxville Metropolitan","Tennessee"),("Greater New Orleans","Louisiana"),("Buffalo-Niagara","New York"),("Albany, New York","New York"),("Rochester, New York","New York"),("Greater Bridgeport","Connecticut"),("Hartford","Connecticut"),("Springfield, Massachusetts","Massachusetts"),("Portland, Maine","Maine"),("Bangor, Maine","Maine"),("Greater Jacksonville","Florida"),("Reno","Nevada"),("Greater Boise","Idaho"),("Greater Wilmington","Delaware"),("Vermont","Vermont")]

def loc_map(loc):
    if not loc: return "USA"
    m = re.search(r',\s*([A-Za-z .]+?),\s*United States', loc)
    if m:
        st = m.group(1).strip()
        if st == "District of Columbia": return "Washington DC"
        if st in STATES: return st
        return "USA"
    if loc.strip() in STATES: return loc.strip()
    for k,v in METRO:
        if k.lower() in loc.lower(): return v
    return "USA"

rows = []
with open(path, newline='', encoding='utf-8-sig') as f:
    r = csv.DictReader(f)
    for i, row in enumerate(r, start=1):
        comp = (row.get('Company Name') or '').strip()
        name = (row.get('Full Name') or '').strip() or ((row.get('First Name') or '').strip() + ' ' + (row.get('Last Name') or '').strip()).strip()
        title = (row.get('Job Title') or '').strip()
        loc = (row.get('Location') or '').strip()
        li = (row.get('LinkedIn Profile') or '').strip()
        li_key = li.strip().lower().rstrip('/')
        email = (row.get('Work Email') or '').strip().lower()
        cid = None; cname = None
        for rx, nm, pid in COMP:
            if rx.search(comp):
                cname, cid = nm, pid
                break
        rows.append({"row": i, "name": name, "title": title, "loc_raw": loc, "loc": loc_map(loc), "company_raw": comp, "company": cname, "cid": cid, "li": li, "li_key": li_key, "email": email})

with open(out, 'w') as f:
    json.dump(rows, f, indent=0)
unres = sorted(set(r['company_raw'] for r in rows if not r['cid']))
print(f"{len(rows)} rows; unresolved companies: {unres}")
