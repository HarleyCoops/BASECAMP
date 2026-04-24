# BASECAMP

**The First Camp of the Alpine Club of Canada, Yoho Pass, July 1906**

A research corpus and presentation built for the **Friends of Yoho** to mark the **120th anniversary** of the Alpine Club of Canada's founding camp.

## What this is

BASECAMP reconstructs the ACC's inaugural alpine camp from primary sources — the *Canadian Alpine Journal* Vol.&nbsp;1 No.&nbsp;1 (1907), Whyte Museum archival photographs, survey records, and glacier observation papers. It maps the people, places, routes, and daily events of the July 1906 camp at Yoho Pass near Emerald Lake, Yoho National Park, British Columbia.

## Structure

```
articles/          35 CAJ V1N1 article transcriptions (markdown)
intelligence/      Structured databases: people, places, camps, routes (JSON + schemas)
maps/              GeoJSON, KML, and interactive map data
people/            20 person profiles with archival artifacts (Whyte Museum images)
people_archive_no_artifacts/   10 additional profiles (no artifact downloads yet)
presentation/      Friends of Yoho presentation (index.html)
silos/             18 article-based research silos (JSON)
source/            CAJ V1N1 source material (epub + table of contents)
tools/             Python build scripts for intelligence, HTML, KML, and silos
```

## Key sources

- **Canadian Alpine Journal Vol. 1 No. 1** (1907) — all 31 articles transcribed
- **Whyte Museum of the Canadian Rockies** — archival photographs and lantern slides
- **Wheeler survey records** — daytimer pages, glacier observations
- **Vaux family papers** — glacier photography and 1906 contact sheets

## Presentation

Open `presentation/index.html` in a browser for the Friends of Yoho deliverable — a scrolling narrative with archival images, maps, and the camp timeline.

## Tools

All build scripts use relative paths from the repo root:

```bash
python tools/build_intelligence.py   # Regenerate intelligence databases
python tools/build_silos.py          # Regenerate article silos
python tools/build_kml.py            # Regenerate Google Earth KML
python tools/build_html.py           # Regenerate presentation HTML
python tools/patch_intelligence.py   # Apply coordinate corrections
python tools/whyte_harvest.py        # Download Whyte Museum artifacts
```

## Origin

This project was developed within the [Emerald Lake Lodge (ELL)](https://github.com/HarleyCoops/ELL) research corpus by Warre & Vavasour, then extracted as a standalone deliverable for the ACC 120th anniversary.

## License

Research corpus — not for redistribution. Archival images are sourced from public collections under fair dealing for research purposes (Canadian Copyright Act).
