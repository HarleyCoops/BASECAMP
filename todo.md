# BASECAMP — Next Steps

## Target: Friends of Yoho presentation for ACC 120th Anniversary (July 8, 2026)

Hero quote: *"Soon after sun-up the thin long line of amateurs, with Excelsior written on face and in eye, crossed the bridge over the Kicking-Horse and took to the road that leads through a silent forest aisle to Emerald lake."* — Frank Yeigh, 1906

---

## Step 1: Build Intelligence Database from Camp Articles

For each article written by someone who was physically at the 1906 camp, extract:

- **People**: name, role (author / guide / mentioned), any biographical detail
- **Places**: every location named, with coordinates where determinable
- **Camps**: campsites described, dates, who was there
- **Routes**: travel routes between named places (these become KML paths)
- **Dates**: any specific dates mentioned in the text

Focus on these camp-present authors first:
- [ ] Frank Yeigh — Canada's First Alpine Club Camp (richest source)
- [ ] A.O. Wheeler — The Canadian Rockies + Observations of the Yoho Glacier
- [ ] Mary M. Vaux — Camping in the Canadian Rockies
- [ ] Rev. C.W. Gordon (Ralph Connor) — How We Climbed Cascade
- [ ] Rev. G.R.B. Kinney — Mt. Stephen (also camp photographer)
- [ ] Elizabeth Parker — The Alpine Club of Canada
- [ ] Julia W. Henshaw — Mountain Wildflowers of Western Canada
- [ ] Geo. & W.S. Vaux — Glacier Observations
- [ ] Chief Mountaineer Report (official account of all climbs)

Output: `intelligence/people.json`, `intelligence/places.json`, `intelligence/camps.json`

## Step 2: Geolocate Places from Articles

Every place mentioned in the articles should be mapped to coordinates. Most resolve around Emerald Lake / Yoho:

- [ ] Field Station (CPR)
- [ ] 7-mile forest road to Emerald Lake
- [ ] Emerald Lake Chalet
- [ ] Northern glacial delta crossing
- [ ] Yoho Pass (6,000 ft camp site)
- [ ] Yoho Lake
- [ ] The Vice-President (10,050 ft — official climb)
- [ ] Mt. Burgess, Mt. Field, Mt. Wapta, Mt. Collie, The President
- [ ] Emerald Glacier
- [ ] Takakkaw Falls, Laughing Falls, Twin Falls
- [ ] Yoho Glacier (upper valley)
- [ ] Burgess Pass trail (return route to Mt. Stephen House)
- [ ] Lake O'Hara, Lake McArthur, Lake Oesa (from Vaux article)
- [ ] Abbot Pass (9,000 ft)
- [ ] Mountains from ascent articles: Goodsir, Hungabee, Ball, Assiniboine, Hermit, Bagheera, Macoun, Crow's Nest, Marpole, Amgadamo, Stephen

Output: `intelligence/places.json` with coordinates, KML file for Google Earth

## Step 3: Build Article-Based Silos

For the richest articles, create silo JSON files:
- [ ] `silos/first-camp-yeigh.json`
- [ ] `silos/camping-rockies-vaux.json`
- [ ] `silos/yoho-glacier-wheeler.json`
- [ ] `silos/climbed-cascade-gordon.json`
- [ ] `silos/mt-stephen-kinney.json`
- [ ] `silos/wildflowers-henshaw.json`
- [ ] `silos/glacier-observations-vaux.json`
- [ ] Additional ascent articles as warranted

Each silo links: article text, author, people mentioned, places geolocated, fonds leads

## Step 4: Locate High-Res Copies of the 3 Maps

The PDF has fold-out maps that scan poorly. Find digital originals:
- [ ] "The All-Red Line Around the World" (p.34) — world map of imperial cable routes
- [ ] "Tongue and Moraines of the Illecillewaet Glacier" (p.142) — Vaux glacier survey
- [ ] "The Wapta Icefield / Yoho Glacier" (p.156) — Wheeler's survey map

Search: Internet Archive high-res scans, LAC Wheeler survey maps, Whyte Museum Vaux originals, McMaster Mountain Legacy Project

## Step 5: Research Fonds and Follow-Up Artifacts

For each article author, search for related fonds:
- [ ] Frank Yeigh — any papers at archives?
- [ ] A.O. Wheeler — LAC survey records, Whyte Museum (already partially done in ELL)
- [ ] Mary M. Vaux — Whyte S5/V18, Smithsonian (already partially done in ELL)
- [ ] Rev. G.R.B. Kinney — photographs from the camp (credited in the journal)
- [ ] Elizabeth Parker — ACC founding documents
- [ ] Gottfried Feuz — Whyte M93/V200 (already found in ELL research)

## Step 6: Build Presentation for Friends of Yoho

Adapt the ELL presentation pattern:
- [ ] `presentation/index.html` — hero page with Yeigh quote and Emerald Lake image
- [ ] Article detail pages (generated from silo data)
- [ ] Interactive map of the 1906 camp route (KML → embedded map)
- [ ] Timeline: July 8 arrival → July 9 march → July 10 first climb → July 16 departure
- [ ] Cross-references to ELL silos where people overlap (Wheeler, Vaux, Feuz, Henshaw)

## Step 7: Package and Deliver

- [ ] README.md with project overview and ACC anniversary context
- [ ] Clean commit to ELL repo
- [ ] Share with Friends of Yoho contact
- [ ] Collect feedback for ELL methodology refinement
