# State · Records — Event Imports (Apollo CSVs)

> **What this is:** dedup ledger for event-attendee imports from Apollo contact exports — Paris Global Summit by BuiltWorlds 2026 + Soletanche Bachy Innovation Day (loaded 2026-06-10).
> **Read it:** before touching any attendee/company from these two events; before importing another Apollo export (dedup check §1).
> **Write to it:** after any enrichment of these records or a new event-CSV import.
> **Part of:** [STATE.md](../../STATE.md) · map: [MAP.md](../MAP.md) · siblings: [records-kiewit](records-kiewit.md) · [databases](databases.md)
> **Ground truth:** `Enlaye Notion/Events/apollo-contacts-export-9.csv` (89 contacts → Paris BW 2026) · `Enlaye Notion/Events/apollo-contacts-export-10.csv` (39 contacts → SB Innovation Day).

---

## Event rows (Enlaye Events Calendar `9bc41c63-…`)
| Event | Page ID | CSV | Date | People linked | Companies attending |
|---|---|---|---|---|---|
| Paris Global Summit by BuiltWorlds 2026 | `2aa90644-d524-806a-9adc-f32f0cf4cd11` | export-9 | 2026-06-09→11 | 89 (32 existing + 57 new) | 53 |
| Soletanche Bachy Innovation Day | `2f790644-d524-8022-bf39-d1ab2c89afef` | export-10 | 2026-05-27 | 39 (1 existing + 38 new) | 1 (Soletanche Bachy) |

NOT used: "BuiltWorlds Paris Summit" `18590644-d524-80df…` = the **2025** edition (June 2025, Completed) — distinct row, untouched.

## Companies — existing, used as-is (33)
Soletanche Bachy `17b90644…802b` · BuiltWorlds `18390644…80c3` · VINCI Group `18690644…80fd` · VINCI Construction `18690644…8028` · VINCI Concessions `18690644…80f1` · Bouygues Construction `1ac90644…809e` · Saint-Gobain `18690644…8052` · Kajima `18290644…80aa` · Takenaka Corporation `18290644…804c` · Trimble `18990644…80a2` · Autodesk `32090644…80fd` · Ferrovial `17a90644…8056` · Acciona `17b90644…8074` · Arcadis `1a090644…80d4` · DPR Construction `18490644…80dc` · Arup `18490644…dc89` · AECOM `17b90644…800e` · Hilti `18990644…80b8` · NVIDIA `18990644…80cb` · Dassault Systemes `17a90644…80db` · Nemetschek Group `2b190644…802f` · CEMEX `18490644…800b` · Zacua Ventures `18990644…80ba` · Brick & Mortar Ventures `33390644…80d0` · GS Futures `22390644…80d8` · Imad Ventures `34990644…80a8` · Kier Group `18290644…806e` · Kaya AI `17c90644…8085` · Converge `18990644…8097` · Xpanner `17c90644…8039` · GScan `18990644…804b` · AMC Bridge, Inc. `18990644…80da` · Gray Capital `22390644…803b`

**Core-name mappings (CSV name → record):** Cemex Ventures→CEMEX · Hilti North America→Hilti · Trimble Finland Oy→Trimble · Kajima Corporation→Kajima · Nemetschek SE→Nemetschek Group · VINCI CONSTRUCTION USA→VINCI Construction · Dassault Systmes→Dassault Systemes · "Imad Ventures (CVC of Nesma & Partners)"→Imad Ventures · MEXT / "MEXT, Mota-Engil NEXT"→Mota-Engil Next (new). CSV literal preserved in person `Company name` text where it differs.

## Companies — created 2026-06-10 (20, all `37b90644-d524-81xx`, Network Intro=BuiltWorlds)
| Company | ID tail | Type/notes |
|---|---|---|
| EarthVisio | `…81b9-b18f` | Start-up |
| Cemvision | `…8127-9854` | Start-up |
| Center for Offsite Construction | `…81d0-8040` | Company |
| Strategic Building Innovation | `…819b-9eae` | Consultant/Advisor |
| Volve Technologies | `…817c-96c2` | Start-up |
| SafeBuild Group Ltd. | `…81dd-bb29` | Start-up |
| Group PMX | `…81c8-91df` | Consultant, USA, site+LI |
| Mota-Engil Next | `…8193-aca1` | Builder, mota-engil.pt (aka MEXT) |
| GS E&C | `…81b4-ac58` | Builder, Mutlinational, Korea→Asia |
| Larsen & Toubro | `…81d6-9314` | Builder, Mutlinational, India |
| Umdasch Group | `…81bd-a673` | Company, Austria |
| Casais Group | `…8157-bae0` | Builder, Europe |
| MEPbrain | `…810d-ac26` | Start-up |
| Blue Auditor GmbH | `…8187-ad34` | Start-up, Germany |
| ecoworks GmbH | `…81c1-b679` | Start-up, Germany |
| Kapture | `…81cd-8d2f` | Start-up, Australia, kapture.earth |
| Aqar | `…812b-8f6c` | Start-up |
| Temelion | `…81f3-861e` | Start-up |
| Presidio Advisors | `…818b-a042` | Consultant/Advisor |
| Neuroject | `…8183-b5b9` | Start-up |

## People — created 2026-06-10 (95, all `37b90644-d524-81xx`, icons user_* rotation, Events+Company relations set at create)
**SB Innovation Day (38, all → Soletanche Bachy):** Yann Amicel, Matthieu Gueydier, Julien Landrot, Cyrille Fargier, Van Nguyen, Yves Barge, Aurelien Prugnaud, Axel Terlaud, Tony Chignard, Maia Lacassagne, Martin Pedley, Daniel Sanchez, Semih Cuhadar, Emmanuel Ollier, Thomas Becuwe, Romain Brieu, Marco Fontana, Jose Pena, Marcos Samudio, Sandrine Camus (CEO), Francois Pageron, Philippe Durville, Steven England, Robert Rocha (Leonard LatAm; Network=LEONARD powered by VINCI), Norbert Seiler (President), Alistair Briffett, Romain Fourcade, Fabien Cassisa, Julien Dubreuil, Pierre Doignon, Alissa Weiss, Martin Stanley, Richard Taylor, Nathalie Jamard, Jean-Francois Mosser, Alexis Behaghel, Lilian Lagarde (CFO), Adil Zerouali.
**Paris BW 2026 (57):** EarthVisio: Chao Liu, Jo Cheng · Trimble: Pascal Laumet, Nassim Saoud, Pascal Devynck, Aviad Almagor, Jorma Zielinski, Julien Debjay · Strategic Building Innovation: Edwin Jeu · Bouygues: Maureen Bucket · Xpanner: Shin Kim · Mota-Engil Next: Andrea Fontecilla, António Rui Solheiro · Cemvision: Oscar Hellén · GScan: Marek Helm · Kier: Andrew Dewdney · Autodesk: Emmanuel Di Giacomo · Kajima: Byron Haigh, Takeshi Torichigai, Mayuko Hirata · Acciona: Clara López Pliego · AMC Bridge: Andy Parnell-Hopkinson · COC: Jason Van Nest · Arcadis: Karin Formigoni · DPR: Justin Robbins · Volve: Herman Smith · SafeBuild: Stuart Cornforth · Group PMX: Michael Giaramita · Umdasch: Matthias Götz · (no company): Mazen Haidar · Takenaka: Rie Shimada · Casais: Pedro Andrade · GS E&C: Fanny Choi · Zacua: Anas Bataw, Juan Nieto · MEPbrain: Jerome Dumarty · CEMEX: Jesús Ortiz · Aqar: Ibrahim Ashshohail · Temelion: Rodolphe Héliot · Dassault: Chris McMahon, Corinne Bulota, Remi Dornier · VINCI Group: Carmen Rouanet · VINCI Construction: Yogesh Patel · Blue Auditor: Wolfgang Lukaschek · Imad: Amin Aljaber, Serge Marashlian, Tatiana Gholmie, Juan Carlos Sanchez · Nemetschek: Katja Hintz · Neuroject: Brian Taammoli · Presidio: Jourdan Younis · AECOM: Aurélien Louis · L&T: Sarbajit Deb · ecoworks: Emanuel Heisenberg · Kapture: Raj Bagri · Gray Capital: Daniel Tarlas.

## People — existing, linked to event + enriched (33)
| Person | ID | Enriched with (from CSV) |
|---|---|---|
| Serge BOREL (SB) | `18590644…8114` | event link only (already complete) |
| Luis Amorim (Ferrovial) | `35d90644…8014` | Function, LinkedIn, Location |
| Julien Villalongue (Leonard/VINCI) | `18590644…80f1-a21c` | Location |
| Kevin Cardona (Leonard/VINCI) | `18590644…80c4` | Location |
| Valentin Piperno (Leonard/VINCI) | `18590644…8044` | Location |
| James McClister (BuiltWorlds) | `22390644…8179` | Email, LinkedIn, Location |
| Guillaume MALOCHET (VINCI Constr.) | `18590644…8122` | LinkedIn |
| Henri Lee (Xpanner) | `33390644…8179` | Location |
| Rui Coutinho (Mota-Engil) | `33390644…81e1` | **Company→Mota-Engil Next**, Email, LinkedIn, Location |
| Basma KHARRAT (Saint-Gobain) | `18590644…8159` | LinkedIn |
| Will Cavendish (Arup) | `33390644…81af` | Location |
| Ryan Park (Xpanner) | `22390644…81d9` | Email |
| Justin Schwaiger (DPR) | `33390644…8111` | Location |
| Sean Young (NVIDIA) | `18990644…80a3` | LinkedIn |
| Matt Gray (BuiltWorlds/Graycor) | `22390644…81a1` | LinkedIn, Location |
| Kara Dinolfo (BuiltWorlds) | `30390644…807d` | Location |
| Subham Kedia (Hilti) | `30390644…8054` | Location |
| Darren Bechtel (B&M Ventures) | `33390644…8101` | Location |
| Rosemarie Lipman (BuiltWorlds) | `22390644…8150` | Location |
| Audrey Lynch (BuiltWorlds) | `22390644…8194` | Function→"Director of Research" (newer title), Location |
| Raphael Scheps (Converge) | `33390644…81e4` | **Company→Converge**, Location |
| Jonathan WILLIET (Saint-Gobain EMEA) | `18590644…81b6` | LinkedIn |
| Tanja Kufner (Nemetschek) | `2b190644…8049` | Email |
| No-gap skips (event link only) | — | Nathalie Martin-Sorvillo `18590644…81cc` · Dai Ohama `18390644…80ba` · Telmo Pérez Luaces `33390644…81ae` · Yuji Doi `1e090644…8017` · Gilles GODARD `18590644…81c7` · Sangyoon Choi `33390644…8186` · Philip Reid `18590644…8188` · Sean Wrenn `22390644…81b9` · Ojonimi Bako `1ea90644…8044` · Miguel Carralón `1c990644…80b4` |

## Flags / decisions
- ⚠ **Pre-existing dup company records (not merged — destructive, needs Zack):** DPR Construction ×2 (`18490644…80dc` used ✓ vs `2c490644…80f2` — Schwaiger linked to the latter) · Xpanner ×2 (`17c90644…8039` used ✓ vs `33390644…80e5` — Henri Lee linked to the latter).
- **Accent restoration:** CSV had stripped accents; restored where unambiguous (Hellén, López, António, Götz, Jesús, Héliot, Aurélien). Flag: "Oscar Hellén" restored from CSV "Hlln" — verify spelling if it matters.
- Mazen Haidar = no company in CSV → person created without Company relation.
- Alexis Behaghel: CSV company = Soletanche Bachy (kept) though email domain is soletanchefreyssinet.com.
- **No shared-select ALTERs** (anti-clobber): person Location options missing Qatar/Martinique/Ireland/Finland/Paraguay→nearest existing or skipped; Companies Country missing Ireland/Portugal/South Korea/Denmark→Europe/Asia.
- Two-way relations: person↔event via People.Events; event row updated with existing people BEFORE creates (clobber-safe order); Companies attending set on event rows (= Companies "Present at Events").
- Stage/Lists/Apollo IDs from CSV not loaded (no matching fields; event relation covers list membership).
