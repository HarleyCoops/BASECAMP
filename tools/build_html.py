#!/usr/bin/env python3
"""Build BASECAMP index.html — hybrid map+timeline with real archival artifacts."""
import json, os, html as html_lib

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'presentation', 'index.html')

# Load all data
geo = json.load(open(os.path.join(BASE, 'presentation', 'basecamp.geojson')))
figures = json.load(open(os.path.join(BASE, 'presentation', 'key_figures.json')))['key_figures']
camps = json.load(open(os.path.join(BASE, 'intelligence', 'camps.json')))
people = json.load(open(os.path.join(BASE, 'intelligence', 'people.json')))
places_data = json.load(open(os.path.join(BASE, 'intelligence', 'places.json')))
# Whyte manifest is optional — originally from ELL/ResearchCorpus
_whyte_path = os.path.join(BASE, '..', 'ELL', 'ResearchCorpus', 'downloads', 'whyte', 'manifest.json')
if os.path.exists(_whyte_path):
    whyte = json.load(open(_whyte_path))
else:
    whyte = {"items": []}  # graceful fallback when standalone
timeline = camps['camps'][0]['daily_events']
camp = camps['camps'][0]

def esc(s):
    return html_lib.escape(str(s)) if s else ''

# === WHYTE IMAGE CATALOG ===
# Map useful Whyte images to timeline days / contexts
whyte_by_id = {w['id']: w for w in whyte if w.get('status') == 'ok' and w.get('url')}

# Curated image sets per day - pulling from actual Whyte manifest
day_images = {
    "1906-07-08": [  # Arrival at Field
        ("descriptions34432", "Emerald Lake & Mt. Field (1899, Vaux)", "The first view campers would have had approaching from Field."),
    ],
    "1906-07-09": [  # The march
        ("descriptions34525", "Emerald Lake (1900, Vaux)", "The lake Yeigh described: 'nestling so peacefully at the base of mighty Mt. Burgess.'"),
        ("descriptions35724", "Mt. Burgess from Emerald Lake (1897, Vaux)", "Nine years before the camp, George Vaux captured the same view that greeted the 112 marchers."),
        ("descriptions34670", "Camp at Emerald Lake (1900, Vaux)", "An earlier Vaux family camp in the same spot. The ACC party rounded up here before the delta crossing."),
    ],
    "1906-07-10": [  # Vice-President climb
        ("descriptions30684", "Mt. President & Emerald Lake (Harmon)", "Harmon's photograph of the President massif looming over the lake basin."),
    ],
    "1906-07-11": [],
    "1906-07-12": [  # Scientific glacier work
        ("descriptions32096", "Panorama of Emerald Lake (c.1910, Byron Harmon)", "Byron Harmon — official ACC photographer — shot this panorama a few years after the first camp."),
    ],
    "1906-07-13": [],
    "1906-07-14": [
        ("descriptions30468", "Emerald Lake & Mt. Burgess (Harmon)", "The view the returning climbers saw descending from the Vice-President col."),
    ],
    "1906-07-15": [  # Yoho Valley
        ("descriptions34163", "Emerald Lake & Mt. Vaux (1902, Vaux)", "Mary Vaux's glacier work carried her family's name into these mountains."),
    ],
    "1906-07-16": [  # Camp breaks
        ("descriptions30699", "Chalet Emerald Lake (Harmon)", "The Emerald Lake Chalet — the last comfort before the pack out to Field."),
    ],
    "1906-07-17": [],
    "1906-07-18": [
        ("descriptions34672", "Emerald Lake (1900, Vaux)", "The lake as George Vaux saw it six years earlier — the same shoreline the ACC would return to."),
    ],
}

# Hero images
HERO_IMG = whyte_by_id.get("descriptions35724", {}).get("url", "")
# If the user didn't like the Wikimedia fallback, use the real Whyte Vaux 1897

# Type icons
type_icons = {
    "arrival": "🚂", "camp_life": "⛺", "climb": "🧗",
    "excursion": "🥾", "ceremony": "🎖️", "departure": "👋",
}

# Day map views
day_views = {
    "1906-07-08": {"center": [51.3985, -116.456], "zoom": 13},
    "1906-07-09": {"center": [51.435, -116.49], "zoom": 13},
    "1906-07-10": {"center": [51.481, -116.508], "zoom": 14},
    "1906-07-11": {"center": [51.481, -116.508], "zoom": 13},
    "1906-07-12": {"center": [51.49, -116.50], "zoom": 12},
    "1906-07-13": {"center": [51.481, -116.508], "zoom": 14},
    "1906-07-14": {"center": [51.485, -116.51], "zoom": 14},
    "1906-07-15": {"center": [51.52, -116.52], "zoom": 12},
    "1906-07-16": {"center": [51.4675, -116.511], "zoom": 13},
    "1906-07-17": {"center": [51.435, -116.49], "zoom": 13},
    "1906-07-18": {"center": [51.3985, -116.456], "zoom": 13},
}

# Key figure features for each day
day_figures = {
    "1906-07-08": ["gottfried-feuz", "george-kinney"],
    "1906-07-09": ["arthur-wheeler", "frank-yeigh"],
    "1906-07-12": ["mary-vaux"],
    "1906-07-15": ["julia-henshaw"],
    "1906-07-16": ["elizabeth-parker"],
    "1906-07-18": ["edward-whymper"],
}

fig_by_id = {f['person_id']: f for f in figures}

# Route colors for legend
route_colors = []
for f in geo['features']:
    if f['geometry']['type'] == 'LineString':
        route_colors.append({"name": f['properties']['name'], "color": f['properties'].get('color', '#ffffff')})

def figure_card(fig):
    climbs = ', '.join(fig.get('climbs_at_camp', [])) if fig.get('climbs_at_camp') else 'Organizer / observer'
    ell = ''
    if fig.get('ell_silo_id'):
        ell = f'<a class="ell-link" href="../../ResearchCorpus/silos/{fig["ell_silo_id"]}/silo.json" target="_blank">View ELL silo →</a>'
    return f"""
    <div class="figure-card">
      <div class="figure-header">
        <h4>{esc(fig['display_name'])}</h4>
        <span class="figure-role">{esc(fig['role_at_camp'])}</span>
      </div>
      <p class="figure-tagline">{esc(fig['tagline'])}</p>
      <blockquote class="figure-quote">"{esc(fig['key_quote'])}"</blockquote>
      <div class="figure-meta">
        <span>⛰ {esc(climbs)}</span>
        {ell}
      </div>
    </div>"""

def photo_block(images_list):
    """Build inline photo strip for a day."""
    if not images_list:
        return ""
    items = ""
    for img_id, caption, desc in images_list:
        img = whyte_by_id.get(img_id)
        if not img:
            continue
        permalink = f"https://archives.whyte.org/en/permalink/{img_id}"
        items += f"""
        <figure class="day-photo">
          <a href="{img['url']}" target="_blank"><img src="{img['url']}" alt="{esc(caption)}" loading="lazy"></a>
          <figcaption>
            <strong>{esc(caption)}</strong><br>
            <span class="photo-desc">{esc(desc)}</span><br>
            <a href="{permalink}" target="_blank" class="source-link">Whyte Museum {esc(img.get('fonds','').title())} Fonds →</a>
          </figcaption>
        </figure>
        """
    if not items:
        return ""
    return f'<div class="photo-strip">{items}</div>'

# Build timeline HTML
timeline_html = ""
for event in timeline:
    d = event['date']
    day_num = int(d.split('-')[2])
    month_day = f"July {day_num}"
    icon = type_icons.get(event['type'], '📍')
    view = day_views.get(d, {"center": [51.4675, -116.511], "zoom": 13})
    desc = event['description']

    fig_cards = ""
    for pid in day_figures.get(d, []):
        if pid in fig_by_id:
            fig_cards += figure_card(fig_by_id[pid])

    photos_html = photo_block(day_images.get(d, []))

    ppl = len(event.get('people_involved', []))
    places_count = len(event.get('places_involved', []))

    timeline_html += f"""
    <section class="day-section"
             data-date="{d}"
             data-lat="{view['center'][0]}"
             data-lng="{view['center'][1]}"
             data-zoom="{view['zoom']}">
      <div class="day-marker">
        <span class="day-icon">{icon}</span>
        <span class="day-date">{month_day}, 1906</span>
        <span class="day-type">{event['type'].replace('_', ' ').title()}</span>
      </div>
      <h3 class="day-title">{esc(event['title'])}</h3>
      <div class="day-stats">
        <span>👥 {ppl} people</span>
        <span>📍 {places_count} locations</span>
      </div>
      {photos_html}
      <p class="day-description">{esc(desc)}</p>
      {fig_cards}
    </section>
    """

# Route legend
route_legend_html = ""
for r in route_colors:
    route_legend_html += f'<div class="route-item"><span class="route-swatch" style="background:{r["color"]}"></span>{esc(r["name"])}</div>\n'

# === INTELLIGENCE GRIDS ===

# People grid — all 45 with roles
people_list = people.get('people', [])
people_grid = ""
for p in sorted(people_list, key=lambda x: x.get('display_name', '')):
    roles = ', '.join(p.get('roles', []))
    at_camp = '⛺' if p.get('at_camp') else '○'
    climbs = p.get('climbs', [])
    climb_str = f" · {len(climbs)} climbs" if climbs else ""
    ell_link = ''
    if p.get('ell_silo_id'):
        ell_link = f' <a class="ell-chip" href="../../ResearchCorpus/silos/{p["ell_silo_id"]}/silo.json" target="_blank">ELL</a>'
    people_grid += f"""
    <div class="person-chip">
      <div class="person-name">{at_camp} {esc(p.get('display_name',''))}{ell_link}</div>
      <div class="person-role">{esc(roles)}{climb_str}</div>
    </div>
    """

# Places grid
places_list = places_data.get('places', [])
places_grid = ""
for pl in sorted(places_list, key=lambda x: (x.get('type', ''), x.get('name', ''))):
    elev = pl.get('elevation_ft', '')
    elev_str = f" · {elev} ft" if elev else ""
    lat = pl.get('coordinates', {}).get('lat', '')
    lon = pl.get('coordinates', {}).get('lon', '')
    coord_str = f"{lat:.4f}, {lon:.4f}" if lat else ""
    places_grid += f"""
    <div class="place-chip" data-lat="{lat}" data-lng="{lon}">
      <div class="place-name">{esc(pl.get('name',''))}</div>
      <div class="place-meta">{esc(pl.get('type',''))}{elev_str}</div>
      <div class="place-coord">{coord_str}</div>
    </div>
    """

# === WHYTE MUSEUM GALLERY ===
gallery_html = ""
for w in whyte:
    if w.get('status') != 'ok' or not w.get('url') or w.get('url','').endswith('.pdf'):
        continue
    permalink = f"https://archives.whyte.org/en/permalink/{w['id']}"
    label = w['label'].replace('_', ' ')
    gallery_html += f"""
    <figure class="gallery-item">
      <a href="{w['url']}" target="_blank"><img src="{w['url']}" alt="{esc(label)}" loading="lazy"></a>
      <figcaption>
        <strong>{esc(label)}</strong><br>
        <span class="gallery-fonds">{esc(w.get('fonds','').title())} Fonds</span><br>
        <a href="{permalink}" target="_blank" class="source-link">View at Whyte Museum →</a>
      </figcaption>
    </figure>
    """

# Stats
graduates_total = 42
mountains_climbed = 8
days_in_camp = 10
total_people = len(people_list)
at_camp_count = sum(1 for p in people_list if p.get('at_camp'))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BASECAMP — The First Alpine Club of Canada Camp, Yoho Pass 1906</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Source+Sans+3:wght@300;400;600&family=JetBrains+Mono:wght@400&display=swap');

  :root {{
    --bg-dark: #0a0a0a;
    --bg-card: #141414;
    --bg-card-hover: #1a1a1a;
    --text-primary: #e8e0d4;
    --text-secondary: #a09888;
    --text-muted: #6a5f52;
    --accent-gold: #c4956a;
    --accent-ice: #7bb8c9;
    --accent-forest: #5a8a5e;
    --accent-rock: #8b7355;
    --accent-snow: #d4cfc7;
    --border: #2a2520;
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Source Sans 3', sans-serif;
    background: var(--bg-dark);
    color: var(--text-primary);
    overflow-x: hidden;
  }}

  a {{ color: var(--accent-ice); }}

  /* === HERO === */
  .hero {{
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: relative;
    background: linear-gradient(180deg, rgba(10,10,10,0.4) 0%, rgba(10,10,10,0.7) 50%, rgba(10,10,10,0.95) 100%), url('{HERO_IMG}') center/cover;
  }}

  .hero-badge {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--accent-gold);
    margin-bottom: 1.5rem;
    border: 1px solid var(--accent-gold);
    padding: 0.4rem 1.2rem;
    display: inline-block;
  }}

  .hero h1 {{
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.5rem, 6vw, 5rem);
    font-weight: 900;
    line-height: 1.1;
    max-width: 900px;
    margin-bottom: 1rem;
    color: #fff;
  }}

  .hero h1 em {{ font-style: italic; color: var(--accent-gold); }}

  .hero-subtitle {{
    font-size: 1.2rem;
    font-weight: 300;
    color: var(--text-secondary);
    max-width: 700px;
    line-height: 1.6;
    margin-bottom: 2rem;
  }}

  .hero-stats {{ display: flex; gap: 3rem; margin-top: 2rem; flex-wrap: wrap; justify-content: center; }}
  .hero-stat {{ text-align: center; }}
  .hero-stat .number {{
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--accent-gold);
    display: block;
  }}
  .hero-stat .label {{
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-muted);
  }}

  .scroll-hint {{
    position: absolute;
    bottom: 2rem;
    animation: pulse 2s infinite;
    color: var(--text-muted);
    font-size: 0.8rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
  }}
  @keyframes pulse {{
    0%, 100% {{ opacity: 0.4; transform: translateY(0); }}
    50% {{ opacity: 1; transform: translateY(5px); }}
  }}

  /* === SECTION HEADERS === */
  .section-header {{
    padding: 5rem 3rem 2rem;
    max-width: 1400px;
    margin: 0 auto;
  }}
  .section-header .eyebrow {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--accent-gold);
  }}
  .section-header h2 {{
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0.5rem 0 1rem;
  }}
  .section-header p {{
    color: var(--text-secondary);
    font-size: 1.05rem;
    line-height: 1.7;
    max-width: 800px;
  }}

  /* === MAIN: MAP + TIMELINE === */
  .main-container {{ display: flex; min-height: 100vh; border-top: 1px solid var(--border); }}
  .map-panel {{ position: sticky; top: 0; width: 50%; height: 100vh; z-index: 10; }}
  #map {{ width: 100%; height: 100%; background: #0a0a0a; }}

  .map-overlay {{
    position: absolute;
    top: 1rem;
    left: 1rem;
    z-index: 1000;
    background: rgba(10,10,10,0.88);
    backdrop-filter: blur(10px);
    padding: 0.8rem 1.2rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    pointer-events: none;
  }}
  .map-overlay .current-date {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--accent-gold);
    letter-spacing: 0.2em;
  }}
  .map-overlay .current-location {{
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    color: #fff;
    margin-top: 0.2rem;
  }}

  .route-legend {{
    position: absolute;
    bottom: 1rem;
    left: 1rem;
    z-index: 1000;
    background: rgba(10,10,10,0.88);
    backdrop-filter: blur(10px);
    padding: 0.8rem 1rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    font-size: 0.75rem;
  }}
  .route-legend h5 {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.5rem;
  }}
  .route-item {{
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.3rem;
    color: var(--text-secondary);
  }}
  .route-swatch {{ width: 20px; height: 3px; border-radius: 2px; display: inline-block; }}

  /* === TIMELINE === */
  .timeline-panel {{ width: 50%; padding: 4rem 3rem; }}
  .timeline-intro {{ margin-bottom: 4rem; padding-bottom: 2rem; border-bottom: 1px solid var(--border); }}
  .timeline-intro h2 {{ font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 1rem; }}
  .timeline-intro p {{ color: var(--text-secondary); line-height: 1.8; font-weight: 300; }}

  .day-section {{
    padding: 3rem 0;
    border-bottom: 1px solid var(--border);
    opacity: 0.45;
    transform: translateY(20px);
    transition: all 0.6s ease;
  }}
  .day-section.active {{ opacity: 1; transform: translateY(0); }}

  .day-marker {{ display: flex; align-items: center; gap: 0.8rem; margin-bottom: 1rem; }}
  .day-icon {{ font-size: 1.5rem; }}
  .day-date {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: var(--accent-gold);
    letter-spacing: 0.1em;
  }}
  .day-type {{
    font-size: 0.7rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    background: rgba(196,149,106,0.1);
    padding: 0.2rem 0.6rem;
    border-radius: 2px;
  }}
  .day-title {{
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.8rem;
    line-height: 1.3;
  }}
  .day-stats {{
    display: flex;
    gap: 1.5rem;
    margin-bottom: 1rem;
    font-size: 0.8rem;
    color: var(--text-muted);
  }}
  .day-description {{
    line-height: 1.8;
    color: var(--text-secondary);
    font-weight: 300;
    font-size: 0.95rem;
  }}

  /* === PHOTO STRIP === */
  .photo-strip {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
  }}
  .day-photo {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 4px;
    overflow: hidden;
  }}
  .day-photo img {{
    width: 100%;
    height: 180px;
    object-fit: cover;
    display: block;
    filter: sepia(0.1) saturate(0.9);
    transition: filter 0.3s;
  }}
  .day-photo img:hover {{ filter: sepia(0) saturate(1); }}
  .day-photo figcaption {{
    padding: 0.8rem;
    font-size: 0.8rem;
    color: var(--text-secondary);
    line-height: 1.5;
  }}
  .day-photo figcaption strong {{ color: var(--accent-snow); font-family: 'Playfair Display', serif; }}
  .photo-desc {{ color: var(--text-muted); font-style: italic; font-size: 0.75rem; }}
  .source-link {{ color: var(--accent-gold); text-decoration: none; font-size: 0.7rem; letter-spacing: 0.05em; }}
  .source-link:hover {{ text-decoration: underline; }}

  /* === FIGURE CARDS === */
  .figure-card {{
    margin-top: 1.5rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent-gold);
    padding: 1.2rem 1.5rem;
    border-radius: 0 4px 4px 0;
  }}
  .figure-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.5rem;
    flex-wrap: wrap;
    gap: 0.5rem;
  }}
  .figure-header h4 {{ font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #fff; }}
  .figure-role {{
    font-size: 0.7rem;
    color: var(--accent-gold);
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }}
  .figure-tagline {{ color: var(--text-secondary); font-style: italic; font-size: 0.9rem; margin-bottom: 0.8rem; }}
  .figure-quote {{
    border-left: 2px solid var(--accent-rock);
    padding-left: 1rem;
    color: var(--text-secondary);
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 0.8rem;
  }}
  .figure-meta {{ font-size: 0.75rem; color: var(--text-muted); display: flex; gap: 1rem; flex-wrap: wrap; }}
  .ell-link {{ color: var(--accent-ice); text-decoration: none; }}

  /* === INTELLIGENCE GRIDS === */
  .intel-section {{
    padding: 3rem 3rem 5rem;
    max-width: 1400px;
    margin: 0 auto;
  }}
  .intel-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 0.8rem;
    margin-top: 2rem;
  }}
  .person-chip, .place-chip {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 0.8rem 1rem;
    border-radius: 4px;
    transition: all 0.2s;
  }}
  .person-chip:hover, .place-chip:hover {{
    background: var(--bg-card-hover);
    border-color: var(--accent-gold);
    transform: translateY(-2px);
  }}
  .person-name, .place-name {{
    font-family: 'Playfair Display', serif;
    font-size: 0.95rem;
    color: var(--text-primary);
    margin-bottom: 0.2rem;
  }}
  .person-role, .place-meta {{
    font-size: 0.72rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}
  .place-coord {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: var(--accent-ice);
    margin-top: 0.3rem;
  }}
  .ell-chip {{
    font-size: 0.6rem;
    background: var(--accent-ice);
    color: var(--bg-dark);
    padding: 0.1rem 0.4rem;
    border-radius: 2px;
    text-decoration: none;
    margin-left: 0.3rem;
    vertical-align: middle;
  }}

  /* === GALLERY === */
  .gallery-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1.2rem;
    margin-top: 2rem;
  }}
  .gallery-item {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 4px;
    overflow: hidden;
    transition: transform 0.3s;
  }}
  .gallery-item:hover {{ transform: translateY(-4px); border-color: var(--accent-gold); }}
  .gallery-item img {{
    width: 100%;
    height: 200px;
    object-fit: cover;
    display: block;
    filter: sepia(0.15) saturate(0.85);
  }}
  .gallery-item figcaption {{
    padding: 0.8rem;
    font-size: 0.75rem;
    color: var(--text-secondary);
  }}
  .gallery-item figcaption strong {{
    color: var(--accent-snow);
    display: block;
    margin-bottom: 0.3rem;
    font-family: 'Playfair Display', serif;
  }}
  .gallery-fonds {{ color: var(--text-muted); font-size: 0.7rem; }}

  /* === SOURCES === */
  .sources-section {{
    padding: 5rem 3rem;
    background: var(--bg-card);
    border-top: 1px solid var(--border);
  }}
  .sources-section .container {{ max-width: 1400px; margin: 0 auto; }}
  .sources-section h3 {{ font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 2rem; }}
  .source-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
  }}
  .source-card {{
    background: var(--bg-dark);
    border: 1px solid var(--border);
    padding: 1.5rem;
    border-radius: 4px;
    transition: border-color 0.2s;
  }}
  .source-card:hover {{ border-color: var(--accent-gold); }}
  .source-card h4 {{ font-size: 0.95rem; color: var(--accent-gold); margin-bottom: 0.5rem; }}
  .source-card p {{ font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 0.8rem; }}
  .source-card a {{ color: var(--accent-ice); text-decoration: none; font-size: 0.8rem; }}
  .source-card a:hover {{ text-decoration: underline; }}

  .colophon {{
    text-align: center;
    padding: 3rem;
    color: var(--text-muted);
    font-size: 0.75rem;
    letter-spacing: 0.1em;
  }}

  /* === LEAFLET DARK === */
  .leaflet-tile-pane {{ filter: brightness(0.7) contrast(1.1) saturate(0.7); }}
  .leaflet-popup-content-wrapper {{
    background: rgba(10,10,10,0.92) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
  }}
  .leaflet-popup-tip {{ background: rgba(10,10,10,0.92) !important; }}
  .leaflet-popup-content {{ font-family: 'Source Sans 3', sans-serif !important; font-size: 0.85rem !important; }}
  .leaflet-popup-content strong {{ color: var(--accent-gold); }}

  @media (max-width: 900px) {{
    .main-container {{ flex-direction: column; }}
    .map-panel {{ width: 100%; height: 50vh; position: sticky; top: 0; }}
    .timeline-panel {{ width: 100%; padding: 2rem 1.5rem; }}
    .section-header, .intel-section {{ padding: 3rem 1.5rem; }}
  }}
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-badge">Intelligence Reconstruction</div>
  <h1>The First Camp at <em>Yoho Pass</em></h1>
  <p class="hero-subtitle">
    July 1906. One hundred and twelve Canadians marched into the wilderness
    to found the Alpine Club of Canada. This is their story, reconstructed
    from the Canadian Alpine Journal and museum archives.
  </p>
  <div class="hero-stats">
    <div class="hero-stat"><span class="number">{camp['actual_attendance']}</span><span class="label">Attendees</span></div>
    <div class="hero-stat"><span class="number">{graduates_total}</span><span class="label">Graduates</span></div>
    <div class="hero-stat"><span class="number">{mountains_climbed}</span><span class="label">Peaks Climbed</span></div>
    <div class="hero-stat"><span class="number">{days_in_camp}</span><span class="label">Days</span></div>
  </div>
  <div class="scroll-hint">↓ Scroll to begin ↓</div>
</div>

<!-- MAIN: MAP + TIMELINE -->
<div class="main-container">
  <div class="map-panel">
    <div id="map"></div>
    <div class="map-overlay">
      <div class="current-date" id="current-date">JULY 8, 1906</div>
      <div class="current-location" id="current-location">Field Station</div>
    </div>
    <div class="route-legend">
      <h5>Routes</h5>
      {route_legend_html}
    </div>
  </div>

  <div class="timeline-panel">
    <div class="timeline-intro">
      <h2>Ten Days That Founded Canadian Mountaineering</h2>
      <p>
        From the evening arrival at Field Station on July 8th to the final pack-out
        on July 18th, the first camp of the Alpine Club of Canada at Yoho Pass was
        an extraordinary feat of organization, ambition, and alpine spirit.
        {camp['actual_attendance']} people camped at 6,000 feet, {graduates_total} graduated
        as active members through five official climbs of Mt. Vice-President, and
        the Scientific Section initiated the first systematic glacier observations
        in Canada. Archival photographs below are drawn from the Vaux, Byron Harmon,
        and Nicholas Morant fonds at the Whyte Museum of the Canadian Rockies.
      </p>
    </div>
    {timeline_html}
  </div>
</div>

<!-- ARCHIVAL GALLERY -->
<div class="section-header">
  <div class="eyebrow">Archival Record</div>
  <h2>The Whyte Museum Collection</h2>
  <p>
    Every photograph below is pulled live from the Whyte Museum of the Canadian Rockies archives.
    Click any image to view at full resolution, or follow the permalink to the museum's catalog record.
    These are the original glass-plate negatives and prints from the Vaux family (1897-1903, the earliest
    photographs of Emerald Lake), Byron Harmon (the Alpine Club's official photographer from 1906-1942),
    and Nicholas Morant (CPR's signature photographer, responsible for the Emerald Lake image on the 1954 $10 bill).
  </p>
</div>
<div class="intel-section">
  <div class="gallery-grid">
    {gallery_html}
  </div>
</div>

<!-- PEOPLE INTELLIGENCE -->
<div class="section-header">
  <div class="eyebrow">Intelligence Database · People</div>
  <h2>{total_people} People · {at_camp_count} At Camp</h2>
  <p>
    Every person mentioned by name in the Canadian Alpine Journal Vol.1 No.1 — from Arthur Wheeler and
    the Swiss guides to Jim Bong the cook and Byron Harmon at age 29, just beginning his 36-year run as the
    ACC's official photographer. The ⛺ marker indicates camp attendance. ELL chips link to full biographical silos.
  </p>
</div>
<div class="intel-section">
  <div class="intel-grid">
    {people_grid}
  </div>
</div>

<!-- PLACES INTELLIGENCE -->
<div class="section-header">
  <div class="eyebrow">Intelligence Database · Places</div>
  <h2>{len(places_list)} Geolocated Features</h2>
  <p>
    Every mountain, lake, pass, glacier, and waypoint referenced in the camp narratives, with verified
    coordinates from Wikipedia, PeakVisor, and ELL's deduced viewpoints dataset. Click any place to
    focus the map above.
  </p>
</div>
<div class="intel-section">
  <div class="intel-grid">
    {places_grid}
  </div>
</div>

<!-- SOURCES -->
<div class="sources-section">
  <div class="container">
    <h3>Primary Sources</h3>
    <div class="source-grid">
      <div class="source-card">
        <h4>Canadian Alpine Journal, Vol. 1, No. 1 (1907)</h4>
        <p>The primary source. Every quote, date, participant list, and climb description in this reconstruction
        is traceable to articles in this journal. Full scan available from University of Toronto Library via Internet Archive.</p>
        <a href="https://archive.org/details/canadianalpinejo01alpiuoft" target="_blank">View on Internet Archive →</a>
      </div>
      <div class="source-card">
        <h4>Whyte Museum — Vaux Family Fonds (V653)</h4>
        <p>47 digitized photographs of Emerald Lake from 1897-1903, including the earliest known images.
        George, Mary, and William Vaux Jr. — Philadelphia scientists who pioneered glacier photography in Canada.</p>
        <a href="https://archives.whyte.org/en/list?q=Vaux+V653" target="_blank">Browse fonds →</a>
      </div>
      <div class="source-card">
        <h4>Whyte Museum — Byron Harmon Fonds (V263)</h4>
        <p>Official photographer of the Alpine Club of Canada from 1906. Over 6,500 negatives documenting
        the club's expeditions. Harmon was at the 1906 camp at age 29 and graduated as an active member on July 13.</p>
        <a href="https://archives.whyte.org/en/list?q=Harmon+V263" target="_blank">Browse fonds →</a>
      </div>
      <div class="source-card">
        <h4>Whyte Museum — J.W. Kelly Fonds (V634)</h4>
        <p>44 photographs taken by J.W. Kelly during his stay at the 1906 Yoho camp, July 9-21.
        Album inscribed "Photos by J.W. Kelly during stay in Yoho Valley."</p>
        <a href="https://archives.whyte.org/en/permalink/descriptions492" target="_blank">View record →</a>
      </div>
      <div class="source-card">
        <h4>Whyte Museum — Alexander Lambie Fonds (V345)</h4>
        <p>52 photographs from the cook's perspective. Alexander Lambie was the cook for the first Alpine Club
        of Canada camp. His album documents camp scenes plus the Yoho area and Banff.</p>
        <a href="https://archives.whyte.org/en/permalink/descriptions498" target="_blank">View record →</a>
      </div>
      <div class="source-card">
        <h4>Whyte Museum — Edward Feuz Fonds (V200)</h4>
        <p>Swiss guide documentation including a confirmed group photo from the 1906 Yoho camp showing
        members posed amongst the trees.</p>
        <a href="https://archives.whyte.org/en/permalink/descriptions49447" target="_blank">View record →</a>
      </div>
      <div class="source-card">
        <h4>BASECAMP Intelligence Database</h4>
        <p>{len(geo['features'])} geolocated features · {total_people} people · {len(timeline)} daily events · 20 article silos.
        Built from systematic extraction of all CAJ Vol.1 No.1 articles. Coordinates verified against Wikipedia,
        PeakVisor, and ELL's deduced viewpoints.</p>
        <a href="basecamp.geojson" target="_blank">View GeoJSON →</a>
      </div>
      <div class="source-card">
        <h4>ELL — Emerald Lake Lodge Research Corpus</h4>
        <p>Cross-referenced for biographical silos on key figures (Wheeler, Vaux, Henshaw, Whymper, Feuz).
        The Whyte Museum image pipeline was borrowed from ELL's harvest_whyte.py.</p>
        <a href="../../ResearchCorpus/" target="_blank">Browse ELL corpus →</a>
      </div>
    </div>
  </div>
</div>

<div class="colophon">
  BASECAMP — An intelligence reconstruction of Canada's first alpine camp<br>
  Built from the Canadian Alpine Journal, Vol. 1, No. 1, 1907 and the Whyte Museum of the Canadian Rockies
</div>

<script>
const geojsonData = {json.dumps(geo)};

const map = L.map('map', {{ zoomControl: false, attributionControl: false }}).setView([51.4675, -116.511], 12);

L.tileLayer('https://tile.opentopomap.org/{{z}}/{{x}}/{{y}}.png', {{ maxZoom: 17 }}).addTo(map);
L.control.zoom({{ position: 'bottomright' }}).addTo(map);

const markerStyles = {{
  'Camp': {{ color: '#c4956a', radius: 10, fillOpacity: 0.9 }},
  'Mountain': {{ color: '#d4cfc7', radius: 6, fillOpacity: 0.7 }},
  'Lake': {{ color: '#7bb8c9', radius: 6, fillOpacity: 0.7 }},
  'Glacier': {{ color: '#a8d4e0', radius: 5, fillOpacity: 0.6 }},
  'Waterfall': {{ color: '#7bb8c9', radius: 5, fillOpacity: 0.6 }},
  'Pass': {{ color: '#8b7355', radius: 5, fillOpacity: 0.6 }},
  'Station': {{ color: '#c4956a', radius: 7, fillOpacity: 0.8 }},
  'Hotel': {{ color: '#c4956a', radius: 5, fillOpacity: 0.6 }},
  'Viewpoint': {{ color: '#5a8a5e', radius: 4, fillOpacity: 0.5 }},
}};
const defaultStyle = {{ color: '#888', radius: 4, fillOpacity: 0.5 }};

const routeLayer = L.layerGroup().addTo(map);
const markerLayer = L.layerGroup().addTo(map);

geojsonData.features.forEach(f => {{
  if (f.geometry.type === 'LineString') {{
    const coords = f.geometry.coordinates.map(c => [c[1], c[0]]);
    const color = f.properties.color || '#ffffff';
    L.polyline(coords, {{
      color: color, weight: 3, opacity: 0.75,
      dashArray: f.properties.name && f.properties.name.includes('approach') ? '8,6' : null
    }}).bindPopup(`<strong>${{f.properties.name}}</strong>`).addTo(routeLayer);
  }} else if (f.geometry.type === 'Point') {{
    const [lng, lat] = f.geometry.coordinates;
    const type = f.properties.type || 'default';
    const style = markerStyles[type] || defaultStyle;
    L.circleMarker([lat, lng], {{
      radius: style.radius, fillColor: style.color, color: style.color,
      weight: 1.5, opacity: 0.9, fillOpacity: style.fillOpacity
    }}).bindPopup(`
      <strong>${{f.properties.name}}</strong><br>
      <span style="color:#a09888">${{type}}</span>
      ${{f.properties.elevation_ft ? `<br>${{f.properties.elevation_ft}} ft` : ''}}
    `).addTo(markerLayer);
  }}
}});

const daySections = document.querySelectorAll('.day-section');
const currentDateEl = document.getElementById('current-date');
const currentLocationEl = document.getElementById('current-location');

const observer = new IntersectionObserver((entries) => {{
  entries.forEach(entry => {{
    if (entry.isIntersecting) {{
      daySections.forEach(s => s.classList.remove('active'));
      entry.target.classList.add('active');
      const lat = parseFloat(entry.target.dataset.lat);
      const lng = parseFloat(entry.target.dataset.lng);
      const zoom = parseInt(entry.target.dataset.zoom);
      const date = entry.target.dataset.date;
      map.flyTo([lat, lng], zoom, {{ duration: 1.5, easeLinearity: 0.25 }});
      const day = parseInt(date.split('-')[2]);
      currentDateEl.textContent = `JULY ${{day}}, 1906`;
      const title = entry.target.querySelector('.day-title');
      if (title) {{
        const short = title.textContent.split(';')[0].split(':')[0].trim();
        currentLocationEl.textContent = short;
      }}
    }}
  }});
}}, {{ root: null, rootMargin: '-30% 0px -30% 0px', threshold: 0.1 }});

daySections.forEach(section => observer.observe(section));

// Place chip click -> fly map
document.querySelectorAll('.place-chip').forEach(chip => {{
  chip.addEventListener('click', () => {{
    const lat = parseFloat(chip.dataset.lat);
    const lng = parseFloat(chip.dataset.lng);
    if (!isNaN(lat) && !isNaN(lng)) {{
      window.scrollTo({{ top: document.querySelector('.main-container').offsetTop, behavior: 'smooth' }});
      setTimeout(() => map.flyTo([lat, lng], 14, {{ duration: 1.5 }}), 600);
    }}
  }});
}});

setTimeout(() => {{ if (daySections[0]) daySections[0].classList.add('active'); }}, 500);
</script>
</body>
</html>"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Written {len(html):,} bytes to {OUT}")
print(f"  {len(timeline)} timeline days with photo strips")
print(f"  {len(geo['features'])} map features")
print(f"  {total_people} people in intelligence grid ({at_camp_count} at camp)")
print(f"  {len(places_list)} places in grid")
print(f"  {sum(1 for w in whyte if w.get('status')=='ok' and w.get('url') and not w['url'].endswith('.pdf'))} Whyte images in gallery")
