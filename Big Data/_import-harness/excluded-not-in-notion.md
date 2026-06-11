# Excluded — companies NOT in Notion

The track record of contacts **skipped** during the import because their employer is not an existing record in the Companies DB. Per Zack's rule, the import **never creates new companies** — anyone whose company isn't already in Notion is skipped and logged here, not guessed into a new record.

- **Decision (2026-06-10):** import the 44,639 contacts that map to existing GCs; **skip these 30**; create zero new companies.
- **Linked from:** [README](README.md) · [BOARD](BOARD.md) · rule lives in [agent-brief](agent-brief.md) ("Unmatched company → skip + log here").
- **Pre-flight basis:** 517 distinct company strings → 487 map to a known GC (44,639 people, 99.93%); 30 don't (below). Validated against live Notion search of the Companies DB (`collection://041b7f07…`).

## A. Real third-party employers not in Notion (12) — skipped
These are genuine companies that simply aren't in the GC database. Each is a single contact. If Zack wants any of them, add the Company record first, then re-run that batch (the agent will pick them up).

| Person | Company (as written) | LinkedIn | Source location |
|---|---|---|---|
| Richard Hatten | Energy Northwest | [link](https://www.linkedin.com/in/richard-hatten-55681a9/) | batch-09/records-21501-22000.csv row 481 |
| Kerry Shapiro | NorthStar Demolition and Remediation | [link](https://www.linkedin.com/in/kerry-shapiro-88791642/) | batch-13/records-30001-30500.csv row 416 |
| Matthew McLean | (Confidential) | [link](https://www.linkedin.com/in/matthew-mclean-786b9912/) | batch-13/records-30501-31000.csv row 429 |
| Marty West | Zahl-PMC | [link](https://www.linkedin.com/in/marty-west-3343013b/) | batch-14/records-33501-34000.csv row 488 |
| Nasim Moghadam | Booz Allen Hamilton | [link](https://www.linkedin.com/in/nasim-moghadam-4791035/) | batch-14/records-34001-34500.csv row 472 |
| Dennis Pyron | TECSAS Services | [link](https://www.linkedin.com/in/dennis-pyron-1217a67a/) | batch-15/records-35001-35500.csv row 202 |
| Kevin Graeve | Burns & McDonnell | [link](https://www.linkedin.com/in/kevin-graeve-2134795/) | batch-15/records-35001-35500.csv row 408 |
| John Lehmann | Sordoni Construction Services | [link](https://www.linkedin.com/in/john-lehmann-7ab1787/) | batch-15/records-35501-36000.csv row 115 |
| Krystal Peterson | Kwajalein Range Services | [link](https://www.linkedin.com/in/krystal-peterson-71132b4/) | batch-15/records-35501-36000.csv row 320 |
| Stidger Andrew | Dynamic Industrial Services | [link](https://www.linkedin.com/in/stidger-andrew-38675264/) | batch-15/records-36001-36500.csv row 20 |
| Margaret Lunsford | Georgia Power | [link](https://www.linkedin.com/in/margaret-lunsford-657769129/) | batch-16/records-39001-39500.csv row 439 |
| Claudia Dimaria | KMTC | [link](https://www.linkedin.com/in/claudia-dimaria-36558319/) | batch-17/records-40501-41000.csv row 48 |

## B. Junk / no real company (18) — skipped
The "Company" cell is noise (tenure strings, "undefined", a restaurant, generic words). Person rows left out entirely. Listed so nothing silently vanishes.

| Person | Company cell (as written) | LinkedIn | Source location |
|---|---|---|---|
| Robert Kennedy, PE | 4 yrs | [link](https://www.linkedin.com/in/robertkennedy89/) | batch-03/records-06501-07000.csv row 145 |
| Dan Morrison | Retired Safety Specialist | [link](https://www.linkedin.com/in/dan-morrison-9a1b6429/) | batch-04/records-09501-10000.csv row 456 |
| Elise Torre | undefined | [link](https://www.linkedin.com/in/elisetorre/) | batch-07/records-15001-15500.csv row 308 |
| Vera Bella | oil and gas | [link](https://www.linkedin.com/in/vera-bella-45ba391a9/) | batch-07/records-16001-16500.csv row 345 |
| Mark Gmerek | 11 yrs 1 mo | [link](https://www.linkedin.com/in/mark-gmerek-498b403/) | batch-08/records-18001-18500.csv row 45 |
| Jerry Cibuls | Semi Retired | [link](https://www.linkedin.com/in/jerry-cibuls-661060a/) | batch-10/records-22501-23000.csv row 15 |
| John Dante | Papa Dante's Restaurant | [link](https://www.linkedin.com/in/john-dante-b7892639/) | batch-10/records-22501-23000.csv row 22 |
| Kathy Lizbinski | Private Contractor | [link](https://www.linkedin.com/in/kathy-lizbinski-60b8718/) | batch-11/records-26501-27000.csv row 369 |
| James Vanderbilt | Self employed | [link](https://www.linkedin.com/in/james-vanderbilt-14633627/) | batch-13/records-31001-31500.csv row 221 |
| Kristen Jones | self parking | [link](https://www.linkedin.com/in/kristen-jones-21a27010b/) | batch-14/records-33001-33500.csv row 493 |
| Sherman Bush | Sherman Bush's Life | [link](https://www.linkedin.com/in/sherman-bush-921a5214/) | batch-14/records-34001-34500.csv row 40 |
| tony daley | built | [link](https://www.linkedin.com/in/tony-daley-2a663b9a/) | batch-15/records-36501-37000.csv row 216 |
| Michael Fabian | low land construction | [link](https://www.linkedin.com/in/michael-fabian-94998013a/) | batch-15/records-36501-37000.csv row 428 |
| Corey Shapuras | Oil and Gas | [link](https://www.linkedin.com/in/corey-shapuras-78b04b126/) | batch-16/records-37501-38000.csv row 125 |
| alfredo gutierrez | caballos roffing and construction | [link](https://www.linkedin.com/in/alfredo-gutierrez-aa9846b1/) | batch-17/records-40001-40500.csv row 100 |
| Dennis Ingram | sub contractor | [link](https://www.linkedin.com/in/dennis-ingram-0538368a/) | batch-17/records-41001-41500.csv row 249 |
| Shay Shay | GM | [link](https://www.linkedin.com/in/shay-shay-228074130/) | batch-17/records-41001-41500.csv row 337 |
| sam moujahed | studio 2020 | [link](https://www.linkedin.com/in/sam-moujahed-09623576/) | batch-17/records-41501-42000.csv row 403 |

## C. Discovered during import — others not in Notion (append-only)
The pre-flight matched on the literal "Company Name" cell. If an agent searches Notion for a record and **cannot find a match** (after the core-name rule), it **skips that person and appends a row here** — so we catch anything the string-match missed.

| Person | Company searched | LinkedIn | Batch · file · row | Agent | When |
|---|---|---|---|---|---|
| _(none yet)_ | | | | | |
