"""
BASECAMP KML Generator
Reads places.json and routes.json, generates Google Earth KML.
"""
import json
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

BASE = Path(__file__).resolve().parent.parent
INTEL = BASE / "intelligence"
MAPS = BASE / "maps"
MAPS.mkdir(parents=True, exist_ok=True)

places = json.loads((INTEL / "places.json").read_text())["places"]
routes = json.loads((INTEL / "routes.json").read_text())["routes"]

# Build place lookup
place_map = {p["place_id"]: p for p in places}

# --- KML Structure ---
kml = Element("kml", xmlns="http://www.opengis.net/kml/2.2")
doc = SubElement(kml, "Document")
SubElement(doc, "name").text = "BASECAMP — 1906 Alpine Club of Canada Camp"
SubElement(doc, "description").text = "Places, routes and camps from the first ACC camp at Yoho Pass, July 1906. Extracted from Canadian Alpine Journal Vol.1 No.1."

# --- STYLES ---
styles = {
    "camp": {"icon": "http://maps.google.com/mapfiles/kml/shapes/campground.png", "color": "ff0000ff", "scale": "1.4"},
    "station": {"icon": "http://maps.google.com/mapfiles/kml/shapes/rail.png", "color": "ff0088ff", "scale": "1.0"},
    "hotel": {"icon": "http://maps.google.com/mapfiles/kml/shapes/lodging.png", "color": "ff00aaff", "scale": "1.0"},
    "chalet": {"icon": "http://maps.google.com/mapfiles/kml/shapes/lodging.png", "color": "ff00aaff", "scale": "1.0"},
    "mountain": {"icon": "http://maps.google.com/mapfiles/kml/shapes/mountains.png", "color": "ff00ff00", "scale": "1.0"},
    "peak": {"icon": "http://maps.google.com/mapfiles/kml/shapes/mountains.png", "color": "ff00dd00", "scale": "0.8"},
    "glacier": {"icon": "http://maps.google.com/mapfiles/kml/shapes/snowflake_simple.png", "color": "ffffcc00", "scale": "1.0"},
    "snowfield": {"icon": "http://maps.google.com/mapfiles/kml/shapes/snowflake_simple.png", "color": "ffffcc00", "scale": "1.0"},
    "lake": {"icon": "http://maps.google.com/mapfiles/kml/shapes/water.png", "color": "ffff8800", "scale": "1.0"},
    "waterfall": {"icon": "http://maps.google.com/mapfiles/kml/shapes/water.png", "color": "ffff4400", "scale": "0.9"},
    "pass": {"icon": "http://maps.google.com/mapfiles/kml/shapes/trail.png", "color": "ff00ffff", "scale": "0.9"},
    "viewpoint": {"icon": "http://maps.google.com/mapfiles/kml/shapes/camera.png", "color": "ff00ffff", "scale": "0.8"},
    "default": {"icon": "http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png", "color": "ff00ffff", "scale": "0.8"},
}

for style_id, props in styles.items():
    style = SubElement(doc, "Style", id=f"style-{style_id}")
    icon_style = SubElement(style, "IconStyle")
    SubElement(icon_style, "scale").text = props["scale"]
    icon = SubElement(icon_style, "Icon")
    SubElement(icon, "href").text = props["icon"]

# Route line styles
route_colors = {
    "field-to-camp": "ff0000ff",       # red — approach march
    "vice-president-official": "ff00ff00",  # green — official climb
    "yoho-valley-round": "ffff8800",    # orange — valley trip
    "emerald-glacier-trip": "ffffff00",  # cyan — glacier
    "burgess-pass-return": "ff8800ff",  # purple — return
}

for route_id, color in route_colors.items():
    style = SubElement(doc, "Style", id=f"route-{route_id}")
    line_style = SubElement(style, "LineStyle")
    SubElement(line_style, "color").text = color
    SubElement(line_style, "width").text = "3"

# --- PLACE FOLDERS ---
type_groups = {}
for p in places:
    pt = p["place_type"]
    type_groups.setdefault(pt, []).append(p)

# Order for folders
folder_order = ["camp", "station", "hotel", "chalet", "mountain", "peak",
                "glacier", "snowfield", "lake", "waterfall", "pass", "viewpoint",
                "delta", "bridge", "road", "trail", "fossil_bed", "cave", "river", "creek",
                "ridge", "arete", "moraine"]

for pt in folder_order:
    group = type_groups.get(pt, [])
    if not group:
        continue
    folder = SubElement(doc, "Folder")
    SubElement(folder, "name").text = pt.replace("_", " ").title() + "s"
    for p in group:
        coords = p.get("coordinates", {})
        if not coords:
            continue
        pm = SubElement(folder, "Placemark")
        SubElement(pm, "name").text = p["display_name"]

        desc_parts = []
        if p.get("elevation_ft"):
            desc_parts.append(f"Elevation: {p['elevation_ft']} ft")
        if p.get("historical_names"):
            desc_parts.append(f"Also known as: {', '.join(p['historical_names'])}")
        if p.get("description_from_text"):
            desc_parts.append(p["description_from_text"])
        if p.get("coordinate_confidence"):
            desc_parts.append(f"Coordinate confidence: {p['coordinate_confidence']}")
        if p.get("modern_trail_note"):
            desc_parts.append(f"Modern: {p['modern_trail_note']}")

        SubElement(pm, "description").text = "\n".join(desc_parts)

        style_key = pt if pt in styles else "default"
        SubElement(pm, "styleUrl").text = f"#style-{style_key}"

        point = SubElement(pm, "Point")
        elev = p.get("elevation_ft", 0) or 0
        elev_m = elev * 0.3048
        SubElement(point, "coordinates").text = f"{coords['lon']},{coords['lat']},{elev_m:.0f}"

# --- ROUTE FOLDER ---
route_folder = SubElement(doc, "Folder")
SubElement(route_folder, "name").text = "Routes (1906)"

for r in routes:
    pm = SubElement(route_folder, "Placemark")
    SubElement(pm, "name").text = r["name"]
    SubElement(pm, "description").text = r["description"]

    style_id = f"route-{r['route_id']}" if r["route_id"] in route_colors else "route-field-to-camp"
    SubElement(pm, "styleUrl").text = f"#{style_id}"

    line = SubElement(pm, "LineString")
    SubElement(line, "tessellate").text = "1"
    SubElement(line, "altitudeMode").text = "clampToGround"

    coord_strings = []
    for wp_id in r["waypoints"]:
        wp = place_map.get(wp_id)
        if wp and wp.get("coordinates"):
            c = wp["coordinates"]
            elev = (wp.get("elevation_ft") or 0) * 0.3048
            coord_strings.append(f"{c['lon']},{c['lat']},{elev:.0f}")

    SubElement(line, "coordinates").text = " ".join(coord_strings)

# --- Write KML ---
xml_str = parseString(tostring(kml, encoding="unicode")).toprettyxml(indent="  ")
# Remove extra xml declaration from minidom
lines = xml_str.split("\n")
if lines[0].startswith("<?xml"):
    lines[0] = '<?xml version="1.0" encoding="UTF-8"?>'

kml_path = MAPS / "basecamp-1906.kml"
kml_path.write_text("\n".join(lines), encoding="utf-8")
print(f"✓ KML written: {kml_path}")
print(f"  {len(places)} placemarks, {len(routes)} routes")
