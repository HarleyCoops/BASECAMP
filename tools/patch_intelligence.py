"""
BASECAMP Intelligence Patcher
Corrects coordinates from verified sources, adds missing people & places,
adds graduate list to camps.json.
"""
import json
from pathlib import Path
from datetime import date

INTEL = Path(__file__).resolve().parent.parent / "intelligence"
TODAY = date.today().isoformat()

def load(name):
    return json.loads((INTEL / name).read_text(encoding="utf-8"))

def save(data, name):
    (INTEL / name).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  ✓ {name}")

# ============================================================
# 1. COORDINATE CORRECTIONS — verified sources
# ============================================================
print("=== Correcting coordinates ===")
places_data = load("places.json")
place_map = {p["place_id"]: p for p in places_data["places"]}

corrections = {
    # Wikipedia-verified summit coordinates
    "vice-president":      {"lat": 51.5020, "lon": -116.5530, "elev": 10058, "conf": "exact", "src": "PeakVisor (51.502029, -116.553027)"},
    "president":           {"lat": 51.5006, "lon": -116.5617, "elev": 10246, "conf": "exact", "src": "Wikipedia (51°30′02″N 116°33′42″W)"},
    "michael-peak":        {"lat": 51.4828, "lon": -116.5131, "elev": 8862,  "conf": "exact", "src": "Wikipedia (51°28′58″N 116°30′47″W), 2701m"},
    "mt-burgess":          {"lat": 51.4200, "lon": -116.5053, "elev": 8527,  "conf": "exact", "src": "Wikipedia (51°25′12″N 116°30′19″W), 2599m"},
    "mt-field":            {"lat": 51.4308, "lon": -116.4628, "elev": 8671,  "conf": "exact", "src": "Wikipedia (51°25′51″N 116°27′46″W), 2643m"},
    "mt-wapta":            {"lat": 51.4514, "lon": -116.4775, "elev": 9114,  "conf": "exact", "src": "Wikipedia (51°27′05″N 116°28′39″W), 2778m"},
    "mt-collie":           {"lat": 51.6172, "lon": -116.5917, "elev": 10312, "conf": "exact", "src": "Wikipedia (51°37′02″N 116°35′30″W), 3143m"},
    "mt-stephen":          {"lat": 51.3992, "lon": -116.4364, "elev": 10495, "conf": "exact", "src": "Wikipedia (51°23′57″N 116°26′11″W), 3199m"},
    "mt-marpole":          {"lat": 51.4925, "lon": -116.5797, "elev": 9268,  "conf": "exact", "src": "Mapcarta (51°29′33″N 116°34′47″W), 2825m"},
    "emerald-lake":        {"lat": 51.4440, "lon": -116.5310, "elev": 4400,  "conf": "exact", "src": "Wikipedia (51°26′38″N 116°31′52″W), 1200m"},
    "takakkaw-falls":      {"lat": 51.4997, "lon": -116.4728, "elev": 4600,  "conf": "exact", "src": "Wikipedia (51°29′59″N 116°28′22″W)"},
    "cascade-mountain":    {"lat": 51.2681, "lon": -115.5822, "elev": 9836,  "conf": "exact", "src": "Wikipedia (51°16′05″N 115°34′56″W), 2998m"},
    "lake-ohara":          {"lat": 51.3559, "lon": -116.3304, "elev": 6630,  "conf": "exact", "src": "Wikipedia (51°21′21″N 116°19′50″W), 2020m"},
    "abbot-pass":          {"lat": 51.3664, "lon": -116.2844, "elev": 9596,  "conf": "exact", "src": "Wikipedia (51°21′59″N 116°17′04″W), 2925m"},
    "wapta-icefield":      {"lat": 51.6394, "lon": -116.5264, "elev": 9000,  "conf": "approximate", "src": "Wikipedia (51°38′22″N 116°31′35″W) — centre of icefield"},

    # ELL viewpoint-calibrated locations
    "emerald-lake-chalet": {"lat": 51.4400, "lon": -116.5310, "elev": 4300, "conf": "approximate", "src": "ELL deduced_viewpoints.kml (lodge at -116.531, 51.44, 1307m)"},

    # Trail-deduced from Michael Peak position and trail descriptions
    # Yoho Pass is on the ridge SSW of Michael Peak (51.4828, -116.5131)
    # ELL viewpoint at -116.4844, 51.4664, 1800m is consistent with pass area
    "yoho-pass":           {"lat": 51.4670, "lon": -116.5100, "elev": 5955, "conf": "approximate", "src": "Deduced from Michael Peak (51.483, -116.513) + ELL viewpoint (51.467, -116.484, 1800m) + trail descriptions (1815m)"},
    "camp-yoho":           {"lat": 51.4675, "lon": -116.5110, "elev": 6000, "conf": "approximate", "src": "At Yoho Pass summit, near Yoho Lake, per Yeigh text. Slightly NW of pass proper."},
    "yoho-lake":           {"lat": 51.4700, "lon": -116.5050, "elev": 5955, "conf": "approximate", "src": "~0.5 km NE of Yoho Pass, below Michael Peak. ELL viewpoint at 51.4664 nearby."},

    # Corrected from summit positions
    "emerald-glacier":     {"lat": 51.4920, "lon": -116.5400, "elev": 8000, "conf": "approximate", "src": "On NE face of President Range between VP (51.502, -116.553) and Michael (51.483, -116.513)"},
    "angle-peak":          {"lat": 51.4900, "lon": -116.5250, "elev": 9500, "conf": "estimated", "src": "On VP arete, ~1 mile E of VP summit per Chief Mountaineer. Between Michael (51.483) and VP (51.502)."},

    # Minor corrections
    "emerald-lake-north-delta": {"lat": 51.4500, "lon": -116.5250, "elev": 4300, "conf": "approximate", "src": "North end of Emerald Lake (51.444, -116.531), alluvial fan area"},
    "field-station":       {"lat": 51.3985, "lon": -116.4560, "elev": 4075, "conf": "exact", "src": "Modern Field townsite, verified against Mt. Stephen position"},
    "mt-stephen-house":    {"lat": 51.3980, "lon": -116.4570, "elev": 4075, "conf": "approximate", "src": "Adjacent to Field Station, demolished 1918"},
    "kicking-horse-bridge":{"lat": 51.3990, "lon": -116.4580, "elev": 4075, "conf": "approximate", "src": "Near start of Emerald Lake Road at Field"},
    "fossil-bed":          {"lat": 51.3950, "lon": -116.4400, "elev": 7000, "conf": "approximate", "src": "Stephen Formation fossil locality, on S slopes of Mt. Stephen"},
    "banff":               {"lat": 51.1784, "lon": -115.5708, "elev": 4537, "conf": "exact", "src": "Town of Banff"},

    # Trail viewpoints — refined from corrected peak positions
    "inspiration-point":   {"lat": 51.4750, "lon": -116.5000, "elev": 6500, "conf": "estimated", "src": "On corkscrew trail near camp, views of Takakkaw Falls across valley"},
    "lookout-point":       {"lat": 51.4850, "lon": -116.4900, "elev": 5500, "conf": "estimated", "src": "On Lower Yoho Valley trail, view of Takakkaw Falls"},
    "burgess-pass":        {"lat": 51.4295, "lon": -116.4840, "elev": 7136, "conf": "approximate", "src": "ELL deduced_viewpoints.kml has Burgess area point at (51.4295, -116.484, 2175m)"},

    # Amgadamo — on south ridge of Marpole per web search
    "mt-amgadamo":         {"lat": 51.4880, "lon": -116.5750, "elev": 9620, "conf": "estimated", "src": "On south ridge of Mt. Marpole (51.4925, -116.5797). Amgadamo Point at 2932m per web."},

    # Yoho Glacier and waterfalls
    "yoho-glacier":        {"lat": 51.5600, "lon": -116.5500, "elev": 6500, "conf": "approximate", "src": "Wheeler: tongue of Yoho Glacier, largest outflow from Wapta Icefield. NW of Yoho Valley."},
    "laughing-falls":      {"lat": 51.5180, "lon": -116.4750, "elev": 4800, "conf": "approximate", "src": "On Yoho Valley trail, between Takakkaw Falls and Twin Falls"},
    "twin-falls":          {"lat": 51.5350, "lon": -116.4800, "elev": 5400, "conf": "approximate", "src": "Twin Falls, upper Yoho Valley. Twin Falls Chalet nearby."},

    # Lake McArthur and Oesa — minor refinements
    "lake-mcarthur":       {"lat": 51.3440, "lon": -116.3320, "elev": 7400, "conf": "approximate", "src": "3 miles from Lake O'Hara per Vaux, largest lake in O'Hara area"},
    "lake-oesa":           {"lat": 51.3500, "lon": -116.3150, "elev": 7500, "conf": "approximate", "src": "Following stream above Lake O'Hara, below Abbot Pass"},
}

corrected_count = 0
for pid, fix in corrections.items():
    if pid in place_map:
        p = place_map[pid]
        p["coordinates"] = {"lat": fix["lat"], "lon": fix["lon"]}
        if fix.get("elev"):
            p["elevation_ft"] = fix["elev"]
        p["coordinate_confidence"] = fix["conf"]
        p["coordinate_source"] = fix["src"]
        corrected_count += 1
    else:
        print(f"  WARN: {pid} not in places — skipped")

places_data["last_updated"] = TODAY
print(f"  Corrected {corrected_count} place coordinates")

# ============================================================
# 2. ADD MISSING PLACES
# ============================================================
print("\n=== Adding missing places ===")
new_places = [
    {
        "place_id": "upper-yoho-trail",
        "display_name": "Upper Yoho Valley Trail",
        "historical_names": ["upper trail"],
        "place_type": "trail",
        "coordinates": {"lat": 51.5100, "lon": -116.4900},
        "elevation_ft": None,
        "elevation_source": "",
        "coordinate_confidence": "estimated",
        "coordinate_source": "Trail midpoint approximation",
        "description_from_text": "Return route for Yoho Valley round trip. Yeigh: 'from lofty platforms of rock we saw the entire fifteen-mile valley lying below us as in a picture.'",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report"],
        "route_connections": ["camp-yoho", "yoho-glacier"],
        "modern_trail_note": "Modern Iceline Trail follows similar high route."
    },
    {
        "place_id": "lower-yoho-trail",
        "display_name": "Lower Yoho Valley Trail",
        "historical_names": ["lower trail"],
        "place_type": "trail",
        "coordinates": {"lat": 51.5050, "lon": -116.4800},
        "elevation_ft": None,
        "elevation_source": "",
        "coordinate_confidence": "estimated",
        "coordinate_source": "Trail midpoint approximation",
        "description_from_text": "Outbound route for Yoho Valley round trip, passing Takakkaw Falls and Laughing Falls.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report"],
        "route_connections": ["takakkaw-falls", "laughing-falls", "twin-falls"],
        "modern_trail_note": "Modern Yoho Valley Trail."
    },
    {
        "place_id": "yoho-peak",
        "display_name": "Yoho Peak",
        "historical_names": [],
        "place_type": "mountain",
        "coordinates": {"lat": 51.5556, "lon": -116.5528},
        "elevation_ft": 9150,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "PeakVisor — 2789m",
        "description_from_text": "Wheeler: separates Yoho Glacier from Habel Glacier. Flanks the western side of the Yoho Glacier.",
        "mentioned_in_articles": ["yoho-glacier-wheeler"],
        "route_connections": ["yoho-glacier"],
        "modern_trail_note": "Yoho Peak, 2789m."
    },
    {
        "place_id": "cathedral-crags",
        "display_name": "Cathedral Crags (Cathedral Spires)",
        "historical_names": ["Cathedral spires"],
        "place_type": "mountain",
        "coordinates": {"lat": 51.4850, "lon": -116.4550},
        "elevation_ft": 9925,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "approximate",
        "coordinate_source": "modern_topo — Cathedral Crags area",
        "description_from_text": "Yeigh: 'bordered by the Cathedral spires on the south and the Yoho glacier on the north.' Visible from upper trail.",
        "mentioned_in_articles": ["first-camp-yeigh"],
        "route_connections": [],
        "modern_trail_note": "Cathedral Crags / Cathedral Mountain area, south side of Yoho Valley."
    },
    {
        "place_id": "natural-bridge",
        "display_name": "Natural Bridge",
        "historical_names": [],
        "place_type": "bridge",
        "coordinates": {"lat": 51.4170, "lon": -116.5080},
        "elevation_ft": 4200,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Photo caption by Mary Vaux: 'MOUNT STEPHEN FROM THE NATURAL BRIDGE.' On Kicking Horse River en route to Emerald Lake.",
        "mentioned_in_articles": ["mt-stephen-kinney"],
        "route_connections": ["emerald-lake-road"],
        "modern_trail_note": "Natural Bridge, Yoho NP. Popular viewpoint on Emerald Lake Road."
    },
]

for np in new_places:
    places_data["places"].append(np)
    print(f"  + {np['display_name']}")

places_data["total_places"] = len(places_data["places"])
save(places_data, "places.json")

# ============================================================
# 3. ADD MISSING PEOPLE
# ============================================================
print("\n=== Adding missing people ===")
people_data = load("people.json")

# Missing ascent article authors
new_people = [
    {
        "person_id": "herschel-parker",
        "display_name": "Herschel C. Parker, Ph.D.",
        "formal_name": "Herschel C. Parker, Ph.D.",
        "roles": ["author", "climber", "active_member"],
        "titles": ["Ph.D.", "First Life Member of ACC"],
        "affiliations": ["Columbia University", "Alpine Club of Canada", "American Alpine Club"],
        "biographical_detail": "Professor at Columbia University. First life member of the ACC. Bold pioneer per Parker. Authored Ascent of Mt. Hungabee.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [
            {"slug": "ascent-hungabee-parker", "title": "The Ascent of Mt. Hungabee", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["alpine-club-parker"],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Hungabee", "date": "pre-1906", "role": "climber"}],
        "ell_silo_id": None,
        "fonds_leads": ["Columbia University Archives"]
    },
    {
        "person_id": "gertrude-benham",
        "display_name": "Gertrude E. Benham",
        "formal_name": "Gertrude E. Benham",
        "roles": ["author", "climber"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Pioneering woman mountaineer. Authored Ascent of Mt. Assiniboine. Later became one of the most-travelled women of her era.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [
            {"slug": "ascent-assiniboine-benham", "title": "The Ascent of Mt. Assiniboine", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": [],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Assiniboine", "date": "pre-1906", "role": "climber"}],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "ws-jackson",
        "display_name": "W.S. Jackson",
        "formal_name": "W.S. Jackson",
        "roles": ["author", "climber"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Authored First Ascent of Central Peak of Mt. Bagheera.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [
            {"slug": "ascent-bagheera-jackson", "title": "The First Ascent of Central Peak of Mt. Bagheera", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": [],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Bagheera (Central Peak)", "date": "pre-1906", "role": "first ascent"}],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "sh-gray",
        "display_name": "Rev. S.H. Gray",
        "formal_name": "Reverend S.H. Gray",
        "roles": ["author", "climber"],
        "titles": ["Reverend"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Authored Ascent of Mt. Hermit.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [
            {"slug": "ascent-hermit-gray", "title": "The Ascent of Mt. Hermit", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": [],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Hermit", "date": "pre-1906", "role": "climber"}],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "charles-fay",
        "display_name": "Charles E. Fay, Litt.D.",
        "formal_name": "Charles E. Fay, Litt.D.",
        "roles": ["author", "climber", "honorary_member"],
        "titles": ["Litt.D.", "President, American Alpine Club"],
        "affiliations": ["American Alpine Club", "Appalachian Mountain Club", "Alpine Club of Canada"],
        "biographical_detail": "President of the American Alpine Club. Honorary member of ACC. Visited Selkirks in 1890, brought many others. Drove formation of AAC Alpine section. Authored Ascent of Mt. Goodsir.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [
            {"slug": "ascent-goodsir-fay", "title": "The Ascent of Mt. Goodsir", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["canadian-rockies-field-wheeler"],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Goodsir", "date": "pre-1906", "role": "climber"}],
        "ell_silo_id": None,
        "fonds_leads": ["Appalachian Mountain Club archives", "AAC archives"]
    },
    # Honorary Members worth tracking
    {
        "person_id": "edward-whymper",
        "display_name": "Edward Whymper",
        "formal_name": "Edward Whymper",
        "roles": ["honorary_member"],
        "titles": [],
        "affiliations": ["Alpine Club (London)", "Alpine Club of Canada"],
        "biographical_detail": "Of Matterhorn fame. Named The Vice-President and The President. Visited Canadian Rockies 1901 with four Swiss guides. Honorary member ACC.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [],
        "articles_mentioned_in": ["first-camp-yeigh", "canadian-rockies-field-wheeler"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": "edward-whymper",
        "fonds_leads": ["Alpine Club London archives"]
    },
    {
        "person_id": "norman-collie",
        "display_name": "J. Norman Collie, F.R.S.",
        "formal_name": "J. Norman Collie, F.R.S.",
        "roles": ["honorary_member", "climber"],
        "titles": ["F.R.S."],
        "affiliations": ["Alpine Club (London)", "Alpine Club of Canada"],
        "biographical_detail": "Explored the Rockies 1897-1902. Climbed extensively in the Blaeberry area. Co-authored 'Climbs and Explorations in the Canadian Rockies.' Honorary member ACC.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [],
        "articles_mentioned_in": ["canadian-rockies-field-wheeler"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": ["Alpine Club London"]
    },
    {
        "person_id": "james-outram",
        "display_name": "Rev. James Outram",
        "formal_name": "Reverend James Outram",
        "roles": ["climber", "honorary_member"],
        "titles": ["Reverend"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Captured Mt. Assiniboine 1901. Made 'big killing' 1902: Columbia, Bryce, Lyall, Alexandra. Named Angle Peak on VP ridge. Author of 'In the Heart of the Canadian Rockies.' Honorary member ACC.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [],
        "articles_mentioned_in": ["canadian-rockies-field-wheeler", "chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Assiniboine", "date": "1901", "role": "first ascent"}, {"mountain": "Mt. Columbia", "date": "1902", "role": "first ascent"}],
        "ell_silo_id": "james-outram",
        "fonds_leads": []
    },
]

for np in new_people:
    people_data["people"].append(np)
    print(f"  + {np['display_name']}")

people_data["total_people"] = len(people_data["people"])
people_data["at_camp_count"] = sum(1 for p in people_data["people"] if p["at_camp"])
people_data["last_updated"] = TODAY
save(people_data, "people.json")

# ============================================================
# 4. ADD GRADUATE LIST TO CAMPS.JSON
# ============================================================
print("\n=== Adding graduate list to camps.json ===")
camps_data = load("camps.json")

graduates_by_date = {
    "1906-07-10": [
        "Dr. A.M. Campbell", "R. Haggen", "Miss E.B. Hobbs",
        "Stanley L. Jones", "T. Kilpatrick", "C.R. Merrill",
        "H.W. McLean", "Miss K. McLennan", "D.N. McTavish"
    ],
    "1906-07-11": [
        "T.A. Hornibrook", "Mrs. Stanley Jones", "J.W. Kelly",
        "Miss L.E. Marshall", "S.H. Mitchell", "W. Nicholson",
        "Miss A.R. Power", "Rev. J.R. Robertson", "Miss A.M. Stewart"
    ],
    "1906-07-12": [
        "F.C. Brown", "J.A. Campbell", "P.M. Campbell",
        "Miss M.T. Durham", "Geo. Harrower", "H.G. Langlois",
        "Rev. A.O. MacRae", "Miss Jean Parker", "Miss F. Pearce",
        "C.B. Sissons", "Miss K.R. Smith", "H.M. Snell", "D. Warner"
    ],
    "1906-07-13": [
        "Rev. Alex. Dunn", "Miss I.W. Griffith", "B. Harmon",
        "Miss A.L. Laird", "D.H. Laird", "A.H. Smith",
        "Miss E. Sutherland"
    ],
    "1906-07-14": [
        "J.H. Graham", "H.G.H. Neville",
        "Miss J.M. Porte", "Miss J.L. Sherman"
    ]
}

# Find the main camp
for camp in camps_data["camps"]:
    if camp["camp_id"] == "yoho-camp-1906":
        camp["graduates_by_date"] = graduates_by_date
        all_grads = []
        for date_key, names in graduates_by_date.items():
            all_grads.extend(names)
        camp["graduation_stats"]["graduate_names"] = all_grads
        print(f"  Added {len(all_grads)} graduates across {len(graduates_by_date)} days")
        break

camps_data["last_updated"] = TODAY
save(camps_data, "camps.json")

print(f"\nFinal counts:")
print(f"  People: {people_data['total_people']} ({people_data['at_camp_count']} at camp)")
print(f"  Places: {places_data['total_places']}")
print(f"  Graduates: {len(all_grads)}")
print(f"  Coordinate corrections applied: {corrected_count}")
