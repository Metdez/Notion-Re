import json

# All LinkedIn URLs extracted from existing Notion pages
extracted = [
    ('Nate Clark', 'https://www.linkedin.com/in/nate-clark-a41a7712b/'),
    ('Peter Biava', 'http://www.linkedin.com/in/peterbiava'),
    ('Ann Esbeck', 'http://www.linkedin.com/in/ann-esbeck-ab0b2229'),
    ('Trent Legendre', 'http://www.linkedin.com/in/trent-legendre-b1a1415b'),
    ('John Tottenham', 'http://www.linkedin.com/in/john-tottenham-9342a138'),
    ('Rugwed Damle', 'http://www.linkedin.com/in/rugwed14'),
    ('Mark Wynne', 'http://www.linkedin.com/in/markwynne-digital'),
    ('Stephen Smith', 'http://www.linkedin.com/in/stephensmithuk'),
    ('Namrta Gupta', 'http://www.linkedin.com/in/namrtagr'),
    ('Mariane P Costa Peixoto Costa', 'https://www.linkedin.com/in/mariane-peixoto-costa-6aa19039/'),
    ('Hasan Salih', 'http://www.linkedin.com/in/hasan-salih-6884425'),
    ('Fernando Vicente', 'http://www.linkedin.com/in/fernando-vicente-81b696106'),
    ('David Lewis', 'http://www.linkedin.com/in/david-lewis-85797811'),
    ('Francisco Bautista', 'http://www.linkedin.com/in/franciscombautista'),
    ('Aaron Santos', 'http://www.linkedin.com/in/aaron-s-a1516a77'),
    ('Eduardo Rochna', 'http://www.linkedin.com/in/eduardo-rochna-21689361'),
    ('Engin Goktepe', 'http://www.linkedin.com/in/engin-goktepe-b0874266'),
    ('Hector Estrada', 'http://www.linkedin.com/in/hector-estrada-4712b1109'),
    ('Allen McCord', 'http://www.linkedin.com/in/allen-mccord-b14225273'),
    ('Michael Dorris', 'http://www.linkedin.com/in/michael-dorris-b9357814'),
    ('Robert Batres', 'http://www.linkedin.com/in/robert-batres-a2a71132'),
    ('Nicole Franklin', 'http://www.linkedin.com/in/nicole-franklin'),
    ('Carrie Mohandessi', 'http://www.linkedin.com/in/carrie-corbitt-mohandessi-0b796b38'),
    ('Peter Toth', 'http://www.linkedin.com/in/peter-toth-b7875a2a'),
    ('Cara Strom', 'http://www.linkedin.com/in/cara-strom-pe-0928894'),
    ('Atessa Farzami', 'http://www.linkedin.com/in/atessafarzami'),
    ('Nwakaego Uzoh', 'http://www.linkedin.com/in/nwakaego-uzoh-b9445692'),
    ('Rob Chapman', 'http://www.linkedin.com/in/rob-chapman-75058524'),
    ('Ken Brown', 'http://www.linkedin.com/in/ken-brown-65120824'),
    ('Drew S', 'http://www.linkedin.com/in/drew-s-59614534'),
    ('Dinesh Kumar', 'http://www.linkedin.com/in/dinesh-kumar-b4183b97'),
    ('Brooke Varela', 'http://www.linkedin.com/in/brooke-wilhelm-a06a23a4'),
    ('Austin Henderson', 'http://www.linkedin.com/in/henderson-austinl'),
    ('Bernard C. Parks., Jr.', 'https://www.linkedin.com/in/bernard-parks-jr-aa1745179'),
    ('Felicia Bell', 'https://www.linkedin.com/in/felicia-bell-cpcm-618b7/'),
    ('Brendan Bechtel', 'https://www.linkedin.com/in/brendanbechtel'),
    ('Craig Albert', 'https://www.linkedin.com/in/craigalbert-bechtel'),
    ('Keith Hennessey', 'https://www.linkedin.com/in/keithbhennessey/'),
    ('Paul Marsden', 'https://www.linkedin.com/in/paul-marsden-51a06512/'),
    ('Darren Mort', 'https://www.linkedin.com/in/darren-mort/'),
    ('Dena Volovar', 'https://www.linkedin.com/in/dena-volovar-b493256/'),
    ('Catherine Hunt Ryan', 'https://www.linkedin.com/in/catherine-hunt-ryan-9235a22/'),
    ('Hamidreza Sarmadi', 'https://www.linkedin.com/in/hamidrezasarmadi'),
    ('Nancy Pena', 'https://www.linkedin.com/in/nancy-pena-25b8bb10'),
    ('Jagat Sinha', 'https://www.linkedin.com/in/jagatjsinha'),
    ('Michael T.', 'https://www.linkedin.com/in/michaelthompson-cqp-fcqi'),
    ('Robin Wappler Scrivens', 'https://www.linkedin.com/in/robin-wappler-scrivens-shrm-scp-7b36185'),
    ('Apryl Jacoby Ashburn', 'https://www.linkedin.com/in/jacobyashburn1'),
    ('Smita Vikram', 'https://www.linkedin.com/in/smita-vikram-3478978'),
    ('Andrea San Martin', 'https://www.linkedin.com/in/andrea-san-martin-35652652'),
    ('Stephanie Mellis', 'https://www.linkedin.com/in/stephanie-mellis-2751b8a1'),
    ('Victor R.', 'https://www.linkedin.com/in/tebicast'),
    ('Timmy Locklear', 'https://www.linkedin.com/in/timmy-locklear-92a87683'),
    ('Arnab Baksi', 'https://www.linkedin.com/in/arnabbaksi'),
    ('Manny Singh PE', 'https://www.linkedin.com/in/manny-singh-pe-p-eng-mba-8627788'),
    ('Charles Gibbons', 'https://www.linkedin.com/in/charles-gibbons-384a718a'),
    ('Scott Dietz', 'https://www.linkedin.com/in/scott-dietz-csp-stsc-89b25546'),
    ('Mohamed Maghawri', 'https://www.linkedin.com/in/mohamed-maghawri-4524ab19'),
    ('Franklyn Francois', 'https://www.linkedin.com/in/franklyn-fran%c3%a7ois-182939211'),
    ('LF Mathew Tan', 'https://www.linkedin.com/in/lfmathewtan'),
    ('Shiva Mandari', 'https://www.linkedin.com/in/shiva-mandari-aa151234a'),
    ('Anuj Batta', 'https://www.linkedin.com/in/anujbatta'),
]

def normalize_li(url):
    if not url:
        return ''
    url = url.strip().lower().rstrip('/')
    url = url.replace('https://', 'http://')
    if '?' in url:
        url = url.split('?')[0]
    return url

normalized = set()
for name, li in extracted:
    n = normalize_li(li)
    if n:
        normalized.add(n)

print(f'Total unique normalized LinkedIn keys collected: {len(normalized)}')

# Cross-reference with bechtel_group.json
with open('C:/Users/John Doe/Documents/Enlaye/Big Data/_import-harness/_tmp_import/bechtel_group.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

pages = data['pages']
matches = 0
match_indices = []
for i, p in enumerate(pages):
    nk = normalize_li(p.get('li_key', ''))
    if nk in normalized:
        matches += 1
        match_indices.append(i)

print(f'Matched in bechtel_group.json: {matches}')
print(f'Match indices first 20: {sorted(match_indices)[:20]}')

# Save progress
with open('C:/Users/John Doe/Documents/Enlaye/Big Data/_import-harness/_tmp_import/bechtel_state/known_existing_li.json', 'w') as f:
    json.dump(list(normalized), f, indent=2)
print('Saved known existing li keys')
