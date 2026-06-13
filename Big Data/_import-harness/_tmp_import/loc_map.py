import json, sys

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
        ('canyon, tx', 'Texas'),
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
        ('catawba', 'South Carolina'),
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
        ('chile', 'Chile'), ('new mexico', 'USA'), ('mexico', 'Mexico'), ('lebanon', 'Lebanon'),
        ('united states', 'USA'),
    ]
    for keyword, option in mappings:
        if keyword in r:
            return option
    return 'USA'

# Test mode
if __name__ == '__main__':
    with open('Big Data/_import-harness/_tmp_import/sundt.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    pages = data.get('pages', [])
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    for p in pages[start:end]:
        raw = p['properties'].get('Location', '')
        mapped = map_location(raw)
        print(f'{raw!r} -> {mapped!r}')
