import csv, sys, json
from collections import Counter

f = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'companies'

with open(f) as fh:
    rows = list(csv.reader(fh))

header = rows[0]
data = rows[1:]

# column indices (0-based) per header map
# 1 Company Name, 2 First, 3 Last, 4 Full Name, 5 Job Title, 6 Location,
# 7 Company Domain, 8 LinkedIn Profile, 24 Work Email, 26 Connections,
# 27 Headline, 28 Summary, 29 Jobs Count

def g(row, i):
    return row[i].strip() if len(row) > i and row[i] else ''

if mode == 'companies':
    c = Counter(g(row,1) for row in data)
    print('rows:', len(data), 'distinct companies:', len(c))
    for name, cnt in c.most_common():
        print(f'{cnt}\t{name}')
elif mode == 'rows':
    lo = int(sys.argv[3]); hi = int(sys.argv[4])
    out = []
    for idx in range(lo, min(hi, len(data))+1):
        row = data[idx-1]
        out.append({
            'row': idx,
            'company': g(row,1),
            'name': g(row,4) or (g(row,2)+' '+g(row,3)).strip(),
            'title': g(row,5),
            'location': g(row,6),
            'domain': g(row,7),
            'linkedin': g(row,8),
            'email': g(row,24),
            'headline': g(row,27),
        })
    print(json.dumps(out, indent=None))
