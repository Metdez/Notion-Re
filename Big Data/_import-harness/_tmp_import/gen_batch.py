"""
Generate a JSON batch payload for notion-create-pages from sundt.json.
Usage: python gen_batch.py <start_index> <end_index>
Outputs a JSON array to stdout (UTF-8 encoded file).
"""
import json, sys, os

def map_location(raw):
    if not raw:
        return None
    r = raw.lower()
    mappings = [
        ('arizona', 'Arizona'), ('phoenix', 'Arizona'), ('scottsdale', 'Arizona'),
        ('tempe', 'Arizona'), ('tucson', 'Arizona'), ('chandler', 'Arizona'),
        ('gilbert', 'Arizona'), ('avondale', 'Arizona'), ('flagstaff', 'Arizona'),
        ('buckeye', 'Arizona'), ('casa grande', 'Arizona'), ('benson', 'Arizona'),
        ('citrus park', 'Arizona'), ('chinle', 'Arizona'), ('claypool', 'Arizona'),
        ('peoria, az', 'Arizona'), ('surprise, az', 'Arizona'), ('yuma', 'Arizona'),
        ('glendale, az', 'Arizona'), ('mesa', 'Arizona'),
        ('texas', 'Texas'), ('dallas', 'Texas'), ('houston', 'Texas'),
        ('austin', 'Texas'), ('san antonio', 'Texas'), ('fort worth', 'Texas'),
        ('el paso', 'Texas'), ('plano', 'Texas'), ('arlington, tx', 'Texas'),
        ('grapevine', 'Texas'), ('abilene', 'Texas'), ('amarillo', 'Texas'),
        ('killeen', 'Texas'), ('baytown', 'Texas'), ('carrollton', 'Texas'),
        ('buda', 'Texas'), ('cibolo', 'Texas'), ('adkins', 'Texas'),
        ('bigfoot', 'Texas'), ('big spring', 'Texas'), ('aubrey', 'Texas'),
        ('brazoria', 'Texas'), ('brownsville', 'Texas'), ('waco', 'Texas'),
        ('midland', 'Texas'), ('odessa', 'Texas'), ('lubbock', 'Texas'),
        ('laredo', 'Texas'), ('alpine, tx', 'Texas'), ('canyon lake', 'Texas'),
        ('canyon, tx', 'Texas'), ('georgetown, tx', 'Texas'),
        ('san francisco', 'San Francisco'),
        ('california', 'California'), ('los angeles', 'California'),
        ('san diego', 'California'), ('sacramento', 'California'),
        ('fresno', 'California'), ('bakersfield', 'California'),
        ('anaheim', 'California'), ('chula vista', 'California'),
        ('irvine', 'California'), ('carlsbad', 'California'),
        ('atascadero', 'California'), ('apple valley', 'California'),
        ('chico', 'California'), ('calexico', 'California'), ('campbell', 'California'),
        ('florida', 'Florida'), ('miami', 'Miami'), ('orlando', 'Florida'),
        ('tampa', 'Florida'), ('jacksonville', 'Florida'),
        ('georgia', 'Georgia'), ('atlanta', 'Georgia'), ('acworth', 'Georgia'),
        ('athens, ga', 'Georgia'),
        ('north carolina', 'North Carolina'), ('charlotte', 'North Carolina'),
        ('raleigh', 'North Carolina'), ('bladenboro', 'North Carolina'),
        ('beaufort, nc', 'North Carolina'),
        ('south carolina', 'South Carolina'), ('charleston, sc', 'South Carolina'),
        ('catawba', 'South Carolina'), ('greenville', 'South Carolina'),
        ('district of columbia', 'Washington DC'), ('washington dc', 'Washington DC'),
        ('washington', 'Washington'), ('seattle', 'Washington'),
        ('vancouver, wa', 'Washington'), ('camas', 'Washington'),
        ('centralia', 'Washington'),
        ('virginia', 'Virginia'), ('richmond, va', 'Virginia'),
        ('charlottesville', 'Virginia'), ('chester, va', 'Virginia'),
        ('oregon', 'Oregon'), ('portland', 'Oregon'), ('clackamas', 'Oregon'),
        ('beaverton', 'Oregon'), ('canby', 'Oregon'),
        ('idaho', 'Idaho'), ('boise', 'Idaho'), ('blackfoot', 'Idaho'),
        ('burley', 'Idaho'), ('caldwell, id', 'Idaho'),
        ('nevada', 'Nevada'), ('las vegas', 'Nevada'), ('reno', 'Nevada'),
        ('carlin', 'Nevada'),
        ('colorado', 'Colorado'), ('denver', 'Colorado'), ('aurora, co', 'Colorado'),
        ('castle rock', 'Colorado'),
        ('new york city', 'New York City'), ('brooklyn', 'New York City'),
        ('manhattan', 'New York City'), ('new york', 'New York'),
        ('pennsylvania', 'Pennsylvania'), ('philadelphia', 'Pennsylvania'),
        ('pittsburgh', 'Pennsylvania'),
        ('ohio', 'Ohio'), ('columbus, oh', 'Ohio'), ('cleveland', 'Ohio'),
        ('michigan', 'Michigan'), ('detroit', 'Michigan'),
        ('illinois', 'Illinois'), ('chicago', 'Illinois'),
        ('indiana', 'Indiana'), ('indianapolis', 'Indiana'),
        ('minnesota', 'Minnesota'), ('minneapolis', 'Minnesota'),
        ('andover, mn', 'Minnesota'), ('chaska', 'Minnesota'),
        ('wisconsin', 'Wisconsin'), ('appleton', 'Wisconsin'),
        ('iowa', 'Iowa'),
        ('missouri', 'Missouri'), ('kansas city', 'Missouri'),
        ('kansas', 'Kansas'),
        ('tennessee', 'Tennessee'), ('nashville', 'Tennessee'), ('big rock', 'Tennessee'),
        ('louisiana', 'Louisiana'), ('new orleans', 'Louisiana'),
        ('maryland', 'Maryland'), ('baltimore', 'Maryland'),
        ('boston', 'Boston'), ('massachusetts', 'Massachusetts'),
        ('connecticut', 'Connecticut'),
        ('new jersey', 'New Jersey'),
        ('delaware', 'Delaware'),
        ('rhode island', 'Rhode Island'),
        ('vermont', 'Vermont'),
        ('new hampshire', 'New Hampshire'),
        ('maine', 'Maine'),
        ('north dakota', 'North Dakota'),
        ('ontario', 'Ontario'), ('british columbia', 'British Columbia'),
        ('alberta', 'Alberta'), ('quebec', 'Quebec'), ('canada', 'Canada'),
        ('london', 'London'), ('united kingdom', 'UK'),
        ('paris', 'Paris'), ('france', 'France'),
        ('germany', 'Germany'), ('sweden', 'Sweden'), ('netherlands', 'Netherlands'),
        ('portugal', 'Portugal'), ('spain', 'Spain'), ('italy', 'Italy'),
        ('switzerland', 'Switzerland'), ('belgium', 'Belgium'),
        ('denmark', 'Denmark'), ('norway', 'Norway'), ('morocco', 'Morocco'),
        ('india', 'India'), ('japan', 'Japan'),
        ('south korea', 'South Korea'), ('korea', 'South Korea'),
        ('singapore', 'Singapore'), ('hong kong', 'Hong Kong'),
        ('thailand', 'Thailand'),
        ('melbourne', 'Melbourne'), ('australia', 'Australia'),
        ('new zealand', 'New Zealand'),
        ('dubai', 'UAE'), ('uae', 'UAE'), ('saudi', 'Saudi Arabia'),
        ('chile', 'Chile'), ('new mexico', 'USA'), ('mexico', 'Mexico'),
        ('lebanon', 'Lebanon'),
        ('united states', 'USA'),
    ]
    for keyword, option in mappings:
        if keyword in r:
            return option
    return 'USA'

start = int(sys.argv[1])
end = int(sys.argv[2])
out_file = sys.argv[3] if len(sys.argv) > 3 else None

base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, 'sundt.json')

with open(src, 'r', encoding='utf-8') as f:
    data = json.load(f)
pages = data.get('pages', [])

batch = []
for p in pages[start:end]:
    props = dict(p['properties'])
    # Map Location to valid multi-select value
    raw_loc = props.get('Location', '')
    mapped_loc = map_location(raw_loc)
    if mapped_loc:
        props['Location'] = mapped_loc
    else:
        del props['Location']
    entry = {
        'properties': props,
        'icon': p['icon'],
        'content': p['content']
    }
    batch.append(entry)

if out_file:
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False)
    print(f'Wrote {len(batch)} records to {out_file}')
else:
    sys.stdout.buffer.write(json.dumps(batch, ensure_ascii=False).encode('utf-8'))
