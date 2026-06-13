"""
Build batch JSON files for kiewit import, starting from index 113.
Applies location mapping and formats Company as JSON array string.
"""
import json, sys, math
sys.stdout.reconfigure(encoding='utf-8')

ALLOWED = ['USA', 'France', 'Europe', 'Portugal', 'Canada', 'Quebec', 'Sweden', 'UK', 'Netherlands',
 'New York City', 'Germany', 'Ontario', 'Illinois', 'Massachusetts', 'South America', 'Maryland',
 'UAE', 'Indiana', 'Colorado', 'Boston', 'Florida', 'Virginia', 'North Carolina', 'Morocco', 'Africa',
 'Denmark', 'Norway', 'California', 'Texas', 'London', 'Michigan', 'San Francisco', 'Missouri',
 'Pennsylvania', 'Melbourne', 'Australia', 'Jersey', 'enw', 'Belgium', 'Japan', 'Italy', 'Switzerland',
 'Thailand', 'Asia', 'Saudi Arabia', 'Hong Kong', 'Maine', 'Lebanon', 'Spain', 'New Hampshire',
 'Vermont', 'Connecticut', 'Rhode Island', 'Mexico', 'Washington DC', 'Delaware', 'Tennessee', 'Kansas',
 'Georgia', 'Arizona', 'New York', 'Iowa', 'Minnesota', 'Wisconsin', 'Louisiana', 'Washington',
 'British Columbia', 'Ohio', 'North Dakota', 'South Korea', 'New Jersey', 'Nevada', 'South Carolina',
 'Alberta', 'Whatever', 'Singapore', 'New Zealand', 'India', 'Chile', 'Paris', 'Idaho', 'Miami',
 'Oregon', 'Caribbean / Southeast']

ALLOWED_LOWER = {a.lower(): a for a in ALLOWED}

STATE_MAP = {
    'California': 'California', 'Texas': 'Texas', 'New York': 'New York',
    'Florida': 'Florida', 'Colorado': 'Colorado',
    'Georgia': 'Georgia', 'Virginia': 'Virginia', 'Washington': 'Washington',
    'Kansas': 'Kansas', 'Missouri': 'Missouri', 'Nebraska': 'USA',
    'Pennsylvania': 'Pennsylvania', 'Tennessee': 'Tennessee', 'North Carolina': 'North Carolina',
    'South Carolina': 'South Carolina', 'Indiana': 'Indiana', 'Ohio': 'Ohio',
    'Michigan': 'Michigan', 'Illinois': 'Illinois', 'Minnesota': 'Minnesota',
    'Wisconsin': 'Wisconsin', 'Iowa': 'Iowa', 'Louisiana': 'Louisiana',
    'Nevada': 'Nevada', 'Arizona': 'Arizona', 'Idaho': 'Idaho',
    'Oregon': 'Oregon', 'Maryland': 'Maryland', 'Massachusetts': 'Massachusetts',
    'North Dakota': 'North Dakota', 'South Dakota': 'USA', 'Wyoming': 'USA',
    'Montana': 'USA', 'Utah': 'USA', 'New Mexico': 'USA', 'Oklahoma': 'USA',
    'Arkansas': 'USA', 'Mississippi': 'USA', 'Alabama': 'USA', 'Kentucky': 'USA',
    'West Virginia': 'Virginia', 'Delaware': 'Delaware', 'Maine': 'Maine',
    'Vermont': 'Vermont', 'New Hampshire': 'New Hampshire', 'Connecticut': 'Connecticut',
    'Rhode Island': 'Rhode Island', 'New Jersey': 'New Jersey',
    'Hawaii': 'USA', 'Alaska': 'USA',
    'District of Columbia': 'Washington DC',
    'British Columbia': 'British Columbia',
    'Ontario': 'Ontario', 'Alberta': 'Alberta', 'Quebec': 'Quebec',
    'Saskatchewan': 'Canada', 'Manitoba': 'Canada', 'Nova Scotia': 'Canada',
}

CITY_MAP = {
    'Houston': 'Texas', 'Dallas': 'Texas', 'Austin': 'Texas', 'San Antonio': 'Texas',
    'Fort Worth': 'Texas', 'Corpus Christi': 'Texas', 'Katy': 'Texas', 'Spring': 'Texas',
    'Baytown': 'Texas', 'Navasota': 'Texas', 'Orange': 'Texas', 'La Porte': 'Texas',
    'Ingleside': 'Texas', 'Montgomery': 'Texas', 'Abilene': 'Texas', 'Albany': 'Texas',
    'Taylor': 'Texas', 'Walker': 'Louisiana',
    'Lenexa': 'Kansas', 'Overland Park': 'Kansas', 'Shawnee': 'Kansas', 'Prairie Village': 'Kansas',
    'Omaha': 'USA', 'Papillion': 'USA', 'Plattsmouth': 'USA',
    'Denver': 'Colorado', 'Littleton': 'Colorado', 'Golden': 'Colorado',
    'Lone Tree': 'Colorado', 'Parker': 'Colorado', 'Englewood': 'Colorado',
    'Kansas City': 'Missouri', 'Lees Summit': 'Missouri',
    'Atlanta': 'Georgia', 'Gainesville': 'Georgia', 'Savannah': 'Georgia', 'Cumming': 'Georgia',
    'Charlotte': 'North Carolina', 'Raleigh': 'North Carolina',
    'San Diego': 'California', 'San Francisco': 'San Francisco',
    'Los Angeles': 'California', 'Sacramento': 'California', 'Benicia': 'California',
    'West Sacramento': 'California', 'Bakersfield': 'California',
    'Seattle': 'Washington', 'Eatonville': 'Washington',
    'Portland': 'Oregon',
    'Philadelphia': 'Pennsylvania', 'Pittsburgh': 'Pennsylvania',
    'Boston': 'Boston',
    'Baltimore': 'Maryland',
    'Nashville': 'Tennessee', 'Memphis': 'Tennessee', 'Johnson City': 'Tennessee',
    'Collierville': 'Tennessee', 'Knoxville': 'Tennessee',
    'Phoenix': 'Arizona', 'Tucson': 'Arizona',
    'Chicago': 'Illinois',
    'Detroit': 'Michigan', 'Grand Rapids': 'Michigan',
    'Miami': 'Miami', 'Tampa': 'Florida', 'Orlando': 'Florida', 'Jacksonville': 'Florida',
    'Cape Coral': 'Florida',
    'New City': 'New York', 'Brooklyn': 'New York City',
    'Las Vegas': 'Nevada', 'Reno': 'Nevada',
    'Minneapolis': 'Minnesota',
    'Milwaukee': 'Wisconsin',
    'New Orleans': 'Louisiana',
    'Boise': 'Idaho', 'Idaho Falls': 'Idaho', 'Blackfoot': 'Idaho',
    'Oklahoma City': 'USA', 'Tulsa': 'USA',
    'Indianapolis': 'Indiana', 'West Lafayette': 'Indiana',
    'Columbus': 'Ohio', 'Cleveland': 'Ohio', 'Cincinnati': 'Ohio',
    'Louisville': 'USA',
    'Martinsburg': 'Virginia', 'Yorktown': 'Virginia', 'Hampton': 'Virginia',
    'Fargo': 'North Dakota',
}

METRO_MAP = [
    ('Denver Metropolitan', 'Colorado'),
    ('Greater Houston', 'Texas'),
    ('Greater Chicago', 'Illinois'),
    ('Greater Seattle', 'Washington'),
    ('Greater Tampa', 'Florida'),
    ('Greater Corpus Christi', 'Texas'),
    ('Greater St. Louis', 'Missouri'),
    ('Omaha Metropolitan', 'USA'),
    ('Kansas City Metropolitan', 'Missouri'),
    ('Dallas-Fort Worth', 'Texas'),
    ('New York City Metropolitan', 'New York City'),
    ('Hampton Roads', 'Virginia'),
    ('Washington DC-Baltimore', 'Washington DC'),
    ('Miami-Fort Lauderdale', 'Miami'),
    ('Detroit Metropolitan', 'Michigan'),
    ('Charlotte Metro', 'North Carolina'),
    ('San Francisco Bay', 'San Francisco'),
]

def map_location(raw):
    if not raw:
        return None
    r = raw.strip()
    if not r:
        return None

    if r.lower() in ALLOWED_LOWER:
        return ALLOWED_LOWER[r.lower()]

    for metro, val in METRO_MAP:
        if metro.lower() in r.lower():
            return val

    for city, val in CITY_MAP.items():
        if r.startswith(city):
            return val

    for state, val in STATE_MAP.items():
        if state in r:
            return val

    if 'United States' in r or 'USA' in r:
        return 'USA'
    if 'Canada' in r:
        return 'Canada'
    if 'France' in r:
        return 'France'
    if 'UK' in r or 'United Kingdom' in r or 'England' in r:
        return 'UK'
    if 'Germany' in r:
        return 'Germany'
    if 'Australia' in r:
        return 'Australia'
    if 'India' in r:
        return 'India'
    if 'Singapore' in r:
        return 'Singapore'
    if 'Mexico' in r:
        return 'Mexico'
    if 'Chile' in r:
        return 'Chile'
    if 'Spain' in r:
        return 'Spain'
    if 'Italy' in r:
        return 'Italy'
    if 'Switzerland' in r:
        return 'Switzerland'
    if 'Japan' in r:
        return 'Japan'
    if 'Hong Kong' in r:
        return 'Hong Kong'
    if 'Saudi Arabia' in r:
        return 'Saudi Arabia'
    if 'UAE' in r or 'United Arab Emirates' in r:
        return 'UAE'
    if 'Morocco' in r:
        return 'Morocco'
    if 'Lebanon' in r:
        return 'Lebanon'
    if 'South Korea' in r or 'Korea' in r:
        return 'South Korea'
    if 'Norway' in r:
        return 'Norway'
    if 'Denmark' in r:
        return 'Denmark'
    if 'Sweden' in r:
        return 'Sweden'
    if 'Netherlands' in r:
        return 'Netherlands'
    if 'Belgium' in r:
        return 'Belgium'
    if 'Portugal' in r:
        return 'Portugal'
    if 'Thailand' in r:
        return 'Thailand'
    if 'New Zealand' in r:
        return 'New Zealand'
    if 'Melbourne' in r:
        return 'Melbourne'

    return 'USA'

def build_page(p):
    props = dict(p['properties'])

    # Map Location from city string to allowed multi-select
    raw_loc = props.get('Location', '')
    mapped_loc = map_location(raw_loc)
    if mapped_loc:
        props['Location'] = json.dumps([mapped_loc])
    else:
        del props['Location']

    # Company is already a URL string — wrap as JSON array for relation
    company_url = props.get('Company', '')
    if company_url:
        props['Company'] = json.dumps([company_url])

    # Remove empty Email (avoid validation issues)
    if 'Email' in props and not props['Email']:
        del props['Email']

    return {
        'properties': props,
        'icon': p.get('icon', ''),
        'content': p.get('content', '')
    }

with open('c:/Users/John Doe/Documents/Enlaye/Big Data/_import-harness/_tmp_import/kiewit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
pages = data['pages']

START = 113
remaining = pages[START:]
BATCH_SIZE = 50
num_batches = math.ceil(len(remaining) / BATCH_SIZE)

print(f'Total remaining: {len(remaining)}, batches: {num_batches}', file=sys.stderr)

# Write all batches
for b in range(num_batches):
    start_i = b * BATCH_SIZE
    end_i = min(start_i + BATCH_SIZE, len(remaining))
    batch_pages = remaining[start_i:end_i]
    payload = [build_page(p) for p in batch_pages]
    fname = f'c:/Users/John Doe/Documents/Enlaye/Big Data/_import-harness/_tmp_import/batch_{b:03d}.json'
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False)
    # Print first name of batch for verification
    first_name = batch_pages[0]['name']
    last_name = batch_pages[-1]['name']
    print(f'batch_{b:03d}: {START + start_i}-{START + end_i - 1} ({len(payload)}) [{first_name} .. {last_name}]')

print(f'Done: {num_batches} batch files written', file=sys.stderr)
