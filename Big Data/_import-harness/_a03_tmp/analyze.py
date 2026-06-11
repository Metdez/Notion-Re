import csv, sys
from collections import Counter

BASE = '/Users/zackhanna/Desktop/Enlaye to Notion/Big Data/batch-03/'
FILES = ['records-05001-05500.csv','records-05501-06000.csv','records-06001-06500.csv','records-06501-07000.csv','records-07001-07500.csv']

c = Counter()
total = 0
for f in FILES:
    with open(BASE+f) as fh:
        r = csv.DictReader(fh)
        for row in r:
            total += 1
            c[row['Company Name'].strip()] += 1
print('total rows:', total)
print('distinct companies:', len(c))
for name, n in c.most_common():
    print(f'{n}\t{name}')
