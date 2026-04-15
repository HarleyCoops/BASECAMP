"""
BASECAMP Silo Builder
Generates article-based silos from CAJ Vol.1 No.1 articles.
Emerald Lake references come ONLY from the article text itself.
ELL cross-refs are person-bio only (silo_id pointer, nothing more).
"""
import json
from pathlib import Path
from datetime import date

BASE = Path(__file__).resolve().parent.parent
SILOS = BASE / "silos"
SILOS.mkdir(parents=True, exist_ok=True)
INTEL = BASE / "intelligence"
TODAY = date.today().isoformat()

people = json.loads((INTEL / "people.json").read_text())["people"]
places = json.loads((INTEL / "places.json").read_text())["places"]
person_map = {p["person_id"]: p for p in people}
place_map = {p["place_id"]: p for p in places}

def write_silo(silo):
    d = SILOS / silo["silo_id"]
    d.mkdir(parents=True, exist_ok=True)
    (d / "silo.json").write_text(json.dumps(silo, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  + {silo['silo_id']}")

# ============================================================
# CAMP-PRESENT AUTHOR SILOS
# ============================================================
silos = []

# --- 1. YEIGH ---
silos.append({
    "silo_id": "first-camp-yeigh",
    "title": "Canada's First Alpine Club Camp — Frank Yeigh",
    "article_slug": "first-camp-yeigh",
    "article_number": 6,
    "section": "MISCELLANEOUS",
    "author": {
        "person_id": "frank-yeigh",
        "display_name": "Frank Yeigh",
        "at_camp": True,
        "ell_silo_id": None
    },
    "summary": "The richest narrative of the 1906 camp. Covers the full arc from arrival at Field Station through the march to Emerald Lake, delta crossing, camp life at Yoho Pass, the Vice-President climbs, Emerald Glacier trip, Yoho Valley excursion, and departure via Burgess Pass.",
    "emerald_lake_references": [
        {
            "passage": "Let us return to the straggling procession of Alpinists as they round up at the Emerald Lake Chalet. The world yet awaits the heaven-gifted artist of brush or pen who will transmit to canvas or paper the transcendent beauty of this mountain lake nestling so peacefully at the base of mighty Mt. Burgess",
            "context": "Arrival at Emerald Lake, start of the ascent to camp",
            "place_ids": ["emerald-lake-chalet", "emerald-lake", "mt-burgess"]
        },
        {
            "passage": "It was at Emerald lake that the real part of the first day's work began, involving the traverse of the broad glacial delta on its northern shore and the ascent of the steep cliff wall",
            "context": "Delta crossing — streams from Emerald Glacier, log bridges swept away, pack ponies as bridges",
            "place_ids": ["emerald-lake-north-delta", "emerald-glacier"]
        },
        {
            "passage": "entrancing glimpses were had of the lake valley, of the enclosing ranks of peaks, and, nearer at hand, of the massive buttresses of Mt. Vice-President, carrying on their granite slopes tumultuous floods of milk-white waters to the lake reservoir of emerald hue",
            "context": "View back to Emerald Lake during cliff ascent",
            "place_ids": ["emerald-lake", "vice-president"]
        }
    ],
    "people_mentioned": [
        "arthur-wheeler", "jc-herdman", "otto-brothers", "gottfried-feuz",
        "k-mclennan", "eb-hobbs", "jd-patterson", "edna-sutherland",
        "re-campbell-outfitter", "ec-barnes", "sh-baker", "jim-bong",
        "edward-whymper", "henrietta-tuzo", "byron-harmon", "fw-freeborn", "d-warner"
    ],
    "places_mentioned": [
        "field-station", "kicking-horse-bridge", "emerald-lake-road",
        "emerald-lake-chalet", "emerald-lake", "emerald-lake-north-delta",
        "yoho-pass", "camp-yoho", "yoho-lake", "vice-president",
        "michael-peak", "emerald-glacier", "mt-burgess", "mt-wapta",
        "mt-collie", "mt-field", "mt-marpole", "mt-amgadamo",
        "takakkaw-falls", "laughing-falls", "twin-falls", "yoho-glacier",
        "burgess-pass", "inspiration-point"
    ],
    "dates_mentioned": [
        {"date": "1906-07-08", "event": "Arrival at Field Station"},
        {"date": "1906-07-09", "event": "March to camp via Emerald Lake"},
        {"date": "1906-07-10", "event": "First official climb — McLennan and Hobbs graduate"},
        {"date": "1906-07-16", "event": "Camp breaks up"},
        {"date": "1906-07-18", "event": "Pack out complete"}
    ],
    "photos_in_article": [
        {"caption": "MOUNT BURGESS AND EMERALD LAKE", "credit": "Rev. G.R. Kinney"},
        {"caption": "THE DINING PAVILION AT YOHO CAMP", "credit": "Byron Harmon"},
        {"caption": "MOUNT VICE-PRESIDENT—THE OFFICIAL CLIMB", "credit": "F.W. Freeborn"},
        {"caption": "RESIDENCE PARK—YOHO CAMP", "credit": "F.W. Freeborn"},
        {"caption": "OUR BIVOUACS ON THE YOHO TRAIL", "credit": "uncredited"},
        {"caption": "THE MEN IN BUCKSKIN", "credit": "uncredited"},
        {"caption": "TWO VETERANS", "credit": "uncredited"},
        {"caption": "AROUND THE CAMP FIRE", "credit": "Frank Yeigh"},
        {"caption": "CROSSING TWIN FALLS CREEK—YOHO VALLEY TRAIL", "credit": "D. Warner"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 47,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/Canada%27s_First_Alpine_Club_Camp"
    },
    "fonds_leads": [
        "Archives of Ontario — Frank Yeigh papers?",
        "Toronto Reference Library"
    ]
})

# --- 2. WHEELER — Canadian Rockies ---
silos.append({
    "silo_id": "canadian-rockies-wheeler",
    "title": "The Canadian Rockies, a Field for an Alpine Club — A.O. Wheeler",
    "article_slug": "canadian-rockies-field-wheeler",
    "article_number": 5,
    "section": "MISCELLANEOUS",
    "author": {
        "person_id": "arthur-wheeler",
        "display_name": "Arthur O. Wheeler, F.R.G.S.",
        "at_camp": True,
        "ell_silo_id": "arthur-oliver-wheeler"
    },
    "summary": "Wheeler's comprehensive survey of the Canadian Rockies as alpine territory. Describes geology, vegetation, glaciers across four ranges. Historical account of all significant expeditions from 1884 to 1906. Makes the case for a Canadian alpine club.",
    "emerald_lake_references": [
        {
            "passage": "turquoise green, in Hector, Bow and Emerald lakes; turquoise blue in Peyto lake; transparent emerald in Yoho lake",
            "context": "Catalogue of lake colors in the Main range",
            "place_ids": ["emerald-lake", "yoho-lake"]
        }
    ],
    "people_mentioned": [
        "sandford-fleming", "charles-fay", "edward-whymper", "james-outram",
        "norman-collie", "herschel-parker"
    ],
    "places_mentioned": [
        "emerald-lake", "yoho-lake", "mt-stephen", "fossil-bed",
        "lake-ohara", "lake-mcarthur", "abbot-pass", "wapta-icefield"
    ],
    "dates_mentioned": [
        {"date": "1884", "event": "Fleming first calls attention to Rockies"},
        {"date": "1888", "event": "Green surveys Selkirks"},
        {"date": "1890", "event": "Topham, Huber, Sulzer visit; Fay visits"},
        {"date": "1897", "event": "Habel explores Yoho Valley"},
        {"date": "1901", "event": "Whymper visits; Outram captures Assiniboine"},
        {"date": "1902", "event": "Outram's big season — Columbia, Bryce, Lyall, Alexandra"}
    ],
    "photos_in_article": [
        {"caption": "A PARTY OF GRADUATES AND GUIDES RETURNED FROM THE OFFICIAL CLIMB OF MT. VICE-PRESIDENT", "credit": "Byron Harmon"},
        {"caption": "MOUNT WAPTA FROM YOHO CAMP", "credit": "uncredited"},
        {"caption": "ICE CAVES ON THE VICE-PRESIDENT GLACIER", "credit": "uncredited"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 36,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/The_Canadian_Rockies,_a_Field_for_an_Alpine_Club"
    },
    "fonds_leads": ["LAC Wheeler survey records", "Whyte Museum ACC fonds"]
})

# --- 3. WHEELER — Yoho Glacier ---
silos.append({
    "silo_id": "yoho-glacier-wheeler",
    "title": "Observations of the Yoho Glacier — A.O. Wheeler",
    "article_slug": "yoho-glacier-wheeler",
    "article_number": 21,
    "section": "SCIENTIFIC",
    "author": {
        "person_id": "arthur-wheeler",
        "display_name": "Arthur O. Wheeler, F.R.G.S.",
        "at_camp": True,
        "ell_silo_id": "arthur-oliver-wheeler"
    },
    "summary": "Scientific report on Yoho Glacier observations initiated July 14-15, 1906. Describes Wapta Icefield geography (20-25 sq mi), glacier flow measurement using metal plates, retreat measurements (76 ft since Vaux 1901 marks). First systematic observations by the ACC.",
    "emerald_lake_references": [],
    "people_mentioned": [
        "george-vaux", "william-s-vaux", "mary-vaux"
    ],
    "places_mentioned": [
        "yoho-glacier", "wapta-icefield", "mt-collie", "yoho-peak",
        "laughing-falls", "twin-falls"
    ],
    "dates_mentioned": [
        {"date": "1906-07-14", "event": "Committee leaves camp for glacier, overnight at Laughing Falls"},
        {"date": "1906-07-15", "event": "Metal plates set, retreat measured"},
        {"date": "1901", "event": "Miss Vaux's earlier marks — 76 ft retreat since then"},
        {"date": "1904", "event": "Dr. Sherzer's marks — 79.6 ft, practically unchanged since 1904"}
    ],
    "photos_in_article": [
        {"caption": "MAP OF WAPTA ICEFIELD", "credit": "from Government photographic surveys"},
        {"caption": "THE ICEFALL OF THE YOHO GLACIER", "credit": "Byron Harmon"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 149,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/Observations_of_the_Yoho_Glacier"
    },
    "fonds_leads": ["LAC Wheeler survey records", "Smithsonian — Sherzer monograph"]
})

# --- 4. VAUX — Camping in the Rockies ---
silos.append({
    "silo_id": "camping-rockies-vaux",
    "title": "Camping in the Canadian Rockies — Mary M. Vaux",
    "article_slug": "camping-rockies-vaux",
    "article_number": 8,
    "section": "MISCELLANEOUS",
    "author": {
        "person_id": "mary-vaux",
        "display_name": "Mary M. Vaux",
        "at_camp": True,
        "ell_silo_id": "mary-vaux-walcott"
    },
    "summary": "Practical guide to camping in the Rockies. Describes Lake O'Hara as finest 4-day trip from Laggan. Detailed equipment lists (clothing, food, photography). Describes Abbot Pass crossing, Lake McArthur goats, Lake Oesa. Photography technique notes.",
    "emerald_lake_references": [],
    "people_mentioned": [],
    "places_mentioned": [
        "lake-ohara", "lake-mcarthur", "lake-oesa", "abbot-pass"
    ],
    "dates_mentioned": [],
    "photos_in_article": [
        {"caption": "MOUNT BIDDLE AND LAKE McARTHUR", "credit": "Mary M. Vaux"},
        {"caption": "AROUND THE CAMP FIRE", "credit": "Frank Yeigh"},
        {"caption": "CROSSING TWIN FALLS CREEK—YOHO VALLEY TRAIL", "credit": "D. Warner"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 67,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/Camping_in_the_Canadian_Rockies"
    },
    "fonds_leads": ["Whyte Museum S5/V18", "Smithsonian Institution", "Academy of Natural Sciences of Philadelphia"]
})

# --- 5. VAUX — Glacier Observations ---
silos.append({
    "silo_id": "glacier-observations-vaux",
    "title": "Glacier Observations — George & William S. Vaux",
    "article_slug": "glacier-observations-vaux",
    "article_number": 20,
    "section": "SCIENTIFIC",
    "author": {
        "person_id": "george-vaux",
        "display_name": "George Vaux, Jr. and William S. Vaux",
        "at_camp": True,
        "ell_silo_id": None
    },
    "summary": "Comprehensive glacier science primer and summary of Vaux brothers' systematic observations since 1887. Covers theory of glacier formation and flow, Illecillewaet recession data (1898-1906), Asulkan observations, Victoria glacier, Yoho glacier. Explains weather patterns driving precipitation.",
    "emerald_lake_references": [],
    "people_mentioned": ["george-vaux", "william-s-vaux"],
    "places_mentioned": ["yoho-glacier", "wapta-icefield"],
    "dates_mentioned": [
        {"date": "1887", "event": "First Illecillewaet photographs"},
        {"date": "1894", "event": "Systematic observations begin"},
        {"date": "1898-1906", "event": "Recession measurements tabulated"}
    ],
    "photos_in_article": [
        {"caption": "TEST PICTURE OF THE ILLECILLEWAET GLACIER FOR THE YEAR 1905", "credit": "Geo. Vaux, Jr. and Mary M. Vaux"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 138,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/Glacier_Observations"
    },
    "fonds_leads": ["Academy of Natural Sciences of Philadelphia proceedings"]
})

# --- 6. GORDON / RALPH CONNOR — Cascade ---
silos.append({
    "silo_id": "climbed-cascade-gordon",
    "title": "How We Climbed Cascade — Ralph Connor (Rev. C.W. Gordon)",
    "article_slug": "climbed-cascade-gordon",
    "article_number": 7,
    "section": "MISCELLANEOUS",
    "author": {
        "person_id": "ralph-connor",
        "display_name": "Rev. C.W. Gordon (Ralph Connor)",
        "at_camp": True,
        "ell_silo_id": None
    },
    "summary": "Humorous narrative of an amateur Cascade Mountain ascent in September 1891 — 15 years before the ACC. Party of 6 (the Professor, Lady from Montreal, Lady from Winnipeg, Man from California, Lady from Banff, the Missionary). No guides, no equipment, ladies in petticoats and kid boots. Two men reach summit, ladies turn back 200 yards short. Fossil remains found near top.",
    "emerald_lake_references": [],
    "people_mentioned": [],
    "places_mentioned": ["cascade-mountain", "banff"],
    "dates_mentioned": [
        {"date": "1891-09", "event": "The climb — a Thursday afternoon in early September"}
    ],
    "photos_in_article": [
        {"caption": "CASCADE MOUNTAIN, BANFF, ALBERTA", "credit": "Byron Harmon"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 58,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/How_We_Climbed_Cascade"
    },
    "fonds_leads": ["University of Manitoba Archives — Ralph Connor papers"]
})

# --- 7. KINNEY — Mt. Stephen ---
silos.append({
    "silo_id": "mt-stephen-kinney",
    "title": "Mt. Stephen — Rev. G.R.B. Kinney",
    "article_slug": "mt-stephen-kinney",
    "article_number": 18,
    "section": "MOUNTAINEERING",
    "author": {
        "person_id": "george-kinney",
        "display_name": "Rev. G.R.B. Kinney",
        "at_camp": True,
        "ell_silo_id": None
    },
    "summary": "Solo ascent of Mt. Stephen, October 21, 1904. Left Field 8am, fossil bed by 10am, summit by late afternoon, returned 8pm. Vivid descriptions of cloud sea below, trilobite fossils, views of Burgess, Field, Wapta, Vice-President with Emerald Glacier. Dangerous cliff climbing near summit. Descent by snow gully. Editorial note: only 5th guideless ascent ever.",
    "emerald_lake_references": [
        {
            "passage": "the Vice-President, with an emerald glacier in its lap, came in full view from behind",
            "context": "View during ascent — looking NW from Mt. Stephen slopes toward President Range and Emerald Lake area",
            "place_ids": ["vice-president", "emerald-glacier"]
        }
    ],
    "people_mentioned": [],
    "places_mentioned": [
        "field-station", "mt-stephen", "fossil-bed", "mt-burgess",
        "mt-field", "mt-wapta", "vice-president", "emerald-glacier",
        "burgess-pass"
    ],
    "dates_mentioned": [
        {"date": "1904-10-21", "event": "Solo ascent, 12-hour round trip"}
    ],
    "photos_in_article": [
        {"caption": "MOUNT STEPHEN FROM THE NATURAL BRIDGE", "credit": "Mary M. Vaux"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 118,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/Mt._Stephen"
    },
    "fonds_leads": ["Whyte Museum", "ACC Archives — camp photographs"]
})

# --- 8. PARKER — Alpine Club of Canada ---
silos.append({
    "silo_id": "alpine-club-parker",
    "title": "The Alpine Club of Canada — Elizabeth Parker",
    "article_slug": "alpine-club-parker",
    "article_number": 2,
    "section": "MISCELLANEOUS",
    "author": {
        "person_id": "elizabeth-parker",
        "display_name": "Elizabeth Parker",
        "at_camp": True,
        "ell_silo_id": None
    },
    "summary": "Philosophical manifesto for the ACC. Six objects of the club. Defense of mountaineering as national character-building. Opposition to cog railways and commercialization of mountain places. Plans for huts, bivouacs, trails. Ethical and spiritual value of mountaineering.",
    "emerald_lake_references": [],
    "people_mentioned": [
        "arthur-wheeler", "sandford-fleming", "william-whyte",
        "herschel-parker", "charles-fay"
    ],
    "places_mentioned": [],
    "dates_mentioned": [
        {"date": "1905-11", "event": "Positive movement towards organization begins"},
        {"date": "1906-03", "event": "Club organized in Winnipeg"}
    ],
    "photos_in_article": [
        {"caption": "ROLL CALL FOR THE OFFICIAL CLIMB OF MT. VICE-PRESIDENT", "credit": "Byron Harmon"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 3,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/The_Alpine_Club_of_Canada"
    },
    "fonds_leads": ["ACC founding documents", "Whyte Museum ACC records"]
})

# --- 9. HENSHAW — Wildflowers ---
silos.append({
    "silo_id": "wildflowers-henshaw",
    "title": "The Mountain Wildflowers of Western Canada — Julia W. Henshaw",
    "article_slug": "wildflowers-henshaw",
    "article_number": 19,
    "section": "SCIENTIFIC",
    "author": {
        "person_id": "julia-henshaw",
        "display_name": "Julia W. Henshaw",
        "at_camp": True,
        "ell_silo_id": "julia-henshaw"
    },
    "summary": "Botanical survey of wildflowers across Banff, Lake Louise, Field, and Glacier. Detailed species identifications with Latin names. Covers Banff Hotel area, Sulphur Mountain trail, Lake Louise slopes, Field moraine, Glacier yellow lilies.",
    "emerald_lake_references": [
        {
            "passage": "Field is the place where you will find the large Yellow Lady's Slipper (Cypripedium pubescens) in all its rare perfection. On a long moraine which stretches up from Emerald lake to the foot of the Yoho valley, these huge orchids grow in thick clumps in the month of July.",
            "context": "Botanical observation — specific species at specific location",
            "place_ids": ["emerald-lake"]
        }
    ],
    "people_mentioned": [],
    "places_mentioned": ["emerald-lake", "banff", "field-station"],
    "dates_mentioned": [],
    "photos_in_article": [
        {"caption": "YELLOW ADDER'S TONGUE (Erythronium Giganteum)", "credit": "Julia W. Henshaw"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 130,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/The_Mountain_Wildflowers_of_Western_Canada"
    },
    "fonds_leads": ["Vancouver Archives", "UBC Special Collections"]
})

# --- 10. CHIEF MOUNTAINEER REPORT ---
silos.append({
    "silo_id": "chief-mountaineer-report",
    "title": "Report of Chief Mountaineer — M.P. Bridgland",
    "article_slug": "chief-mountaineer-report",
    "article_number": 28,
    "section": "OFFICIAL",
    "author": {
        "person_id": "morrison-bridgland",
        "display_name": "M.P. Bridgland",
        "at_camp": True,
        "ell_silo_id": None
    },
    "summary": "Official record of all climbs. Vice-President route details (arete, Angle Peak, snowfield). Daily climb logs with times, parties, graduates. Side climbs: Burgess, Wapta (x4), Collie, Field, President, Marpole, Amgadamo (first ascents). Yoho Valley trips (60 people), Emerald Glacier trips (27 people), Takakkaw Falls trip (19 people).",
    "emerald_lake_references": [
        {
            "passage": "The Burgess trail seemed a favorite... from which the Presidents range and Emerald mountains with their glaciers, icefalls and torrents, are seen to the greatest advantage; while below, Emerald lake nestles in a setting of deep green forest.",
            "context": "View from Burgess Pass trail — return route for many campers",
            "place_ids": ["burgess-pass", "emerald-lake"]
        },
        {
            "passage": "Three trips were made, under the leadership of the Rev. J.C. Herdman, to the glacier below the northeastern escarpment of the President range, known as the Emerald glacier.",
            "context": "Emerald Glacier trips — glacier named for its relation to Emerald Lake",
            "place_ids": ["emerald-glacier"]
        }
    ],
    "people_mentioned": [
        "morrison-bridgland", "hg-wheeler", "edouard-feuz", "gottfried-feuz",
        "jc-herdman", "jd-patterson", "eo-wheeler", "pd-mctavish",
        "am-gordon", "ao-macrae", "alex-dunn", "george-kinney",
        "jh-miller", "ec-barnes", "henrietta-tuzo", "christian-kaufmann",
        "byron-harmon", "jean-parker", "sh-baker"
    ],
    "places_mentioned": [
        "camp-yoho", "yoho-pass", "michael-peak", "angle-peak",
        "vice-president", "president", "mt-burgess", "mt-wapta",
        "mt-collie", "mt-field", "mt-marpole", "mt-amgadamo",
        "emerald-glacier", "takakkaw-falls", "laughing-falls", "twin-falls",
        "yoho-glacier", "burgess-pass", "inspiration-point", "lookout-point",
        "emerald-lake"
    ],
    "dates_mentioned": [
        {"date": "1906-07-08", "event": "Route scouting party departs for VP"},
        {"date": "1906-07-09", "event": "Camp opens officially"},
        {"date": "1906-07-10", "event": "First official climb + Burgess. 9 graduate."},
        {"date": "1906-07-11", "event": "Second climb + Wapta. 9 graduate."},
        {"date": "1906-07-12", "event": "Third climb + Collie + Field + Wapta. 13 graduate."},
        {"date": "1906-07-13", "event": "Fourth climb + Wapta. 7 graduate."},
        {"date": "1906-07-14", "event": "Fifth climb + President summit. 4 graduate."},
        {"date": "1906-07-16", "event": "Marpole + Amgadamo first ascents."}
    ],
    "photos_in_article": [
        {"caption": "AN AWKWARD CORNER — Mount Vice-President", "credit": "uncredited"},
        {"caption": "A PIECE OF ROCK WORK — Mount Vice-President", "credit": "uncredited"},
        {"caption": "THE UPPER SNOWFIELD—MOUNT VICE-PRESIDENT", "credit": "Rev. Geo. B. Kinney"},
        {"caption": "A CLIMBING PARTY — Mt. Burgess", "credit": "uncredited"},
        {"caption": "DESCENDING THE GLACIER — Mt. Vice-President", "credit": "uncredited"},
        {"caption": "LAUGHING FALL CAMP — Yoho Valley Trip", "credit": "uncredited"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 169,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1"
    },
    "fonds_leads": ["LAC Topographical Survey records"]
})

# --- 11. YOHO CAMP REPORT (Official) ---
silos.append({
    "silo_id": "yoho-camp-report",
    "title": "Report of the Yoho Camp, July, 1906 — Official Circular",
    "article_slug": "yoho-camp-report",
    "article_number": 23,
    "section": "OFFICIAL",
    "author": {
        "person_id": "hg-wheeler",
        "display_name": "H.G. Wheeler / Elizabeth Parker (signatories)",
        "at_camp": True,
        "ell_silo_id": None
    },
    "summary": "Official circular for the camp. Rules, charges ($1-2/day), equipment requirements (hobnailed boots, knickerbockers, puttees, colored glasses). 40 lb baggage limit. No skirts on rope. Camp opens July 9, closes July 16. First Annual Meeting held at camp.",
    "emerald_lake_references": [],
    "people_mentioned": ["hg-wheeler", "elizabeth-parker"],
    "places_mentioned": ["field-station", "camp-yoho"],
    "dates_mentioned": [
        {"date": "1906-07-08", "event": "Arrive at Field by evening train"},
        {"date": "1906-07-09", "event": "Camp opens"},
        {"date": "1906-07-16", "event": "Camp closes"}
    ],
    "photos_in_article": [
        {"caption": "GUIDES IN CHARGE OF CLIMBING—YOHO CAMP", "credit": "uncredited"},
        {"caption": "A WELL EARNED REST—MOUNT VICE-PRESIDENT", "credit": "uncredited"},
        {"caption": "YOHO CAMP", "credit": "uncredited"}
    ],
    "source": {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "page": 169,
        "wikisource": "https://en.wikisource.org/wiki/Canadian_Alpine_Journal/Volume_1/Number_1/Report_of_the_Yoho_Camp,_July,_1906"
    },
    "fonds_leads": []
})

# ============================================================
# MOUNTAINEERING SECTION SILOS
# ============================================================
ascent_silos = [
    {
        "silo_id": "ascent-goodsir-fay",
        "title": "The Ascent of Mt. Goodsir — Charles E. Fay",
        "article_slug": "ascent-goodsir-fay",
        "article_number": 9,
        "section": "MOUNTAINEERING",
        "author": {"person_id": "charles-fay", "display_name": "Charles E. Fay, Litt.D.", "at_camp": False, "ell_silo_id": None},
        "summary": "Account of the ascent of Mt. Goodsir, the highest peak in the Ottertail Range.",
    },
    {
        "silo_id": "ascent-hungabee-parker",
        "title": "The Ascent of Mt. Hungabee — Herschel C. Parker",
        "article_slug": "ascent-hungabee-parker",
        "article_number": 10,
        "section": "MOUNTAINEERING",
        "author": {"person_id": "herschel-parker", "display_name": "Herschel C. Parker, Ph.D.", "at_camp": False, "ell_silo_id": None},
        "summary": "Ascent of Mt. Hungabee near Lake O'Hara.",
    },
    {
        "silo_id": "ascent-ball-patterson",
        "title": "The Ascent of Mt. Ball — J.D. Patterson",
        "article_slug": "ascent-ball-patterson",
        "article_number": 11,
        "section": "MOUNTAINEERING",
        "author": {"person_id": "jd-patterson", "display_name": "J.D. Patterson", "at_camp": True, "ell_silo_id": None},
        "summary": "Ascent of Mt. Ball in the Ball Range.",
    },
    {
        "silo_id": "ascent-assiniboine-benham",
        "title": "The Ascent of Mt. Assiniboine — Gertrude E. Benham",
        "article_slug": "ascent-assiniboine-benham",
        "article_number": 12,
        "section": "MOUNTAINEERING",
        "author": {"person_id": "gertrude-benham", "display_name": "Gertrude E. Benham", "at_camp": False, "ell_silo_id": None},
        "summary": "Ascent of the 'Matterhorn of the Rockies' by pioneering woman mountaineer.",
    },
    {
        "silo_id": "ascent-hermit-gray",
        "title": "The Ascent of Mt. Hermit — Rev. S.H. Gray",
        "article_slug": "ascent-hermit-gray",
        "article_number": 13,
        "section": "MOUNTAINEERING",
        "author": {"person_id": "sh-gray", "display_name": "Rev. S.H. Gray", "at_camp": False, "ell_silo_id": None},
        "summary": "Ascent of Mt. Hermit in the Selkirk Range near Rogers Pass.",
    },
    {
        "silo_id": "ascent-bagheera-jackson",
        "title": "The First Ascent of Central Peak of Mt. Bagheera — W.S. Jackson",
        "article_slug": "ascent-bagheera-jackson",
        "article_number": 14,
        "section": "MOUNTAINEERING",
        "author": {"person_id": "ws-jackson", "display_name": "W.S. Jackson", "at_camp": False, "ell_silo_id": None},
        "summary": "First ascent of the central peak of Mt. Bagheera.",
    },
    {
        "silo_id": "ascent-macoun-herdman",
        "title": "The Ascent of Mt. Macoun — Rev. J.C. Herdman",
        "article_slug": "ascent-macoun-herdman",
        "article_number": 15,
        "section": "MOUNTAINEERING",
        "author": {"person_id": "jc-herdman", "display_name": "Rev. J.C. Herdman, D.D.", "at_camp": True, "ell_silo_id": None},
        "summary": "Ascent of Mt. Macoun by the man Yeigh called 'a born mountaineer.'",
    },
    {
        "silo_id": "climb-crows-nest-mctavish",
        "title": "The Climb of Crow's Nest Mountain — P.D. McTavish",
        "article_slug": "climb-crows-nest-mctavish",
        "article_number": 16,
        "section": "MOUNTAINEERING",
        "author": {"person_id": "pd-mctavish", "display_name": "P.D. McTavish", "at_camp": True, "ell_silo_id": None},
        "summary": "Climb of Crow's Nest Mountain in the Crowsnest Pass area.",
    },
    {
        "silo_id": "ascents-marpole-amgadamo",
        "title": "The Ascents of Mts. Marpole and Amgadamo — Gordon, Dunn, MacRae",
        "article_slug": "ascents-marpole-amgadamo",
        "article_number": 17,
        "section": "MOUNTAINEERING",
        "author": {"person_id": "am-gordon", "display_name": "Revs. A.M. Gordon, Alex. Dunn and A.O. MacRae", "at_camp": True, "ell_silo_id": None},
        "summary": "First ascents of both peaks on July 16, 1906 — the last day of camp. Amgadamo named at camp (AM Gordon, A Dunn, AO MacRae initials).",
    },
]

# Fill in standard fields for ascent silos
for s in ascent_silos:
    s.setdefault("emerald_lake_references", [])
    s.setdefault("people_mentioned", [])
    s.setdefault("places_mentioned", [])
    s.setdefault("dates_mentioned", [])
    s.setdefault("photos_in_article", [])
    s.setdefault("source", {
        "journal": "Canadian Alpine Journal",
        "volume": 1, "number": 1, "year": 1907,
        "wikisource": ""
    })
    s.setdefault("fonds_leads", [])

silos.extend(ascent_silos)

# ============================================================
# WRITE ALL SILOS
# ============================================================
print("Building BASECAMP Silos...")
for s in silos:
    write_silo(s)

# Write index
index = {
    "schema_version": "1.0",
    "last_updated": TODAY,
    "total_silos": len(silos),
    "silos": [
        {
            "silo_id": s["silo_id"],
            "title": s["title"],
            "section": s.get("section", ""),
            "author": s["author"]["display_name"],
            "at_camp": s["author"]["at_camp"],
            "has_emerald_lake_refs": len(s.get("emerald_lake_references", [])) > 0,
            "emerald_lake_ref_count": len(s.get("emerald_lake_references", []))
        }
        for s in silos
    ]
}
(SILOS / "silo_index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\n✓ silo_index.json")

# Summary
el_silos = [s for s in silos if s.get("emerald_lake_references")]
print(f"\nDone. {len(silos)} silos built.")
print(f"Silos with Emerald Lake references: {len(el_silos)}")
for s in el_silos:
    print(f"  - {s['silo_id']}: {len(s['emerald_lake_references'])} refs")
print(f"ELL cross-refs (person bio only): {sum(1 for s in silos if s['author'].get('ell_silo_id'))}")
