from pathlib import Path
import json, shutil, html
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

ROOT = Path('/mnt/c/Users/chris/BASECAMP')
OUT = ROOT/'presentation/HermesPresentation'
ASSETS = OUT/'assets_reimagined'
ASSETS.mkdir(parents=True, exist_ok=True)

# Preserve the first attempt rather than destroying it.
idx = OUT/'index.html'
if idx.exists() and not (OUT/'index.v1-coordinate-atlas.html').exists():
    shutil.copy2(idx, OUT/'index.v1-coordinate-atlas.html')

sources = {
    'vaux_hero': 'people/george-vaux/artifacts/descriptions34196_wmcr-vaux-1v-v653-ps-098.jpg',
    'wapta_valley': 'people/george-vaux/artifacts/descriptions34193_wmcr-vaux-1v-v653-ps-095.jpg',
    'bow_range': 'people/george-vaux/artifacts/descriptions34205_wmcr-vaux-1v-v653-ps-107.jpg',
    'victoria_glacier': 'people/mary-vaux/artifacts/descriptions34546_wmcr-vaux-1h-v653-na-328.jpg',
    'mary_forest': 'people/mary-vaux/artifacts/descriptions34174_wmcr-vaux-1v-v653-ps-074.jpg',
    'seracs': 'people/mary-vaux/artifacts/descriptions34158_wmcr-vaux-1v-v653-ps-058.jpg',
    'yoho_glacier': 'people/george-vaux/artifacts/descriptions35061_wmcr-vaux-1n-v653-na-1414.jpg',
    'wapta_glacier': 'people/george-vaux/artifacts/descriptions35063_wmcr-vaux-1n-v653-na-1415.jpg',
    'guides': 'people/edouard-feuz/artifacts/descriptions34149_wmcr-vaux-1v-v653-ps-049.jpg',
    'camp_group': 'people/edouard-feuz/artifacts/descriptions49447_v200_13_na66_184.jpg',
    'glacier_people': 'people/ec-barnes/artifacts/descriptions37968_wmcr-barnes-v48-lc-na66-1567.jpg',
    'elizabeth_report': 'people/fw-freeborn/artifacts/descriptions49267_v14_ac55_5_984_na66_2131.jpg',
    'packtrail': 'people/re-campbell-outfitter/artifacts/descriptions50040_v715_2_na66_487.jpg',
    'lake_louise_chalet': 'people/george-vaux/artifacts/descriptions35093_wmcr-vaux-1n-v653-na-1486.jpg',
    'bridge_spuzzum': 'people/mary-vaux/artifacts/descriptions34103_wmcr-vaux-1v-v653-ps-003.jpg',
    'daytimer_open': 'people/arthur-wheeler/daytimer_pages/1906_jul08_sun_OPEN.png',
    'daytimer_close': 'people/arthur-wheeler/daytimer_pages/1906_jul16_mon_CLOSE.png',
    'contact1': 'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p1.jpg',
    'contact3': 'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p3.jpg',
    'contact4': 'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p4.jpg',
    'contact5': 'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p5.jpg',
    'contact6': 'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p6.jpg',
}

def derivative(name, rel, max_dim=1900, contrast=1.04, sharp=1.05):
    src = ROOT/rel
    dst = ASSETS/f'{name}.jpg'
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    im.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
    if contrast != 1:
        im = ImageEnhance.Contrast(im).enhance(contrast)
    if sharp != 1:
        im = ImageEnhance.Sharpness(im).enhance(sharp)
    im.save(dst, 'JPEG', quality=86, optimize=True, progressive=True)
    return f'assets_reimagined/{name}.jpg'

asset = {}
for k, rel in sources.items():
    md = 1900
    if k.startswith('contact'): md = 1400
    if k.startswith('daytimer'): md = 1500
    asset[k] = derivative(k, rel, md)

# Create a few crops/abstract details from contact sheets for magnified evidence moments.
def crop_asset(name, rel, box_frac, max_dim=1200):
    src = ROOT/rel
    dst = ASSETS/f'{name}.jpg'
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    w,h = im.size
    box = tuple(int(v) for v in (box_frac[0]*w, box_frac[1]*h, box_frac[2]*w, box_frac[3]*h))
    cr = im.crop(box)
    cr.thumbnail((max_dim,max_dim), Image.Resampling.LANCZOS)
    cr = ImageEnhance.Contrast(cr).enhance(1.08)
    cr.save(dst, 'JPEG', quality=88, optimize=True, progressive=True)
    return f'assets_reimagined/{name}.jpg'
asset['contact4_ice_detail'] = crop_asset('contact4_ice_detail', sources['contact4'], (.08,.06,.92,.53))
asset['contact5_system_detail'] = crop_asset('contact5_system_detail', sources['contact5'], (.05,.06,.95,.58))
asset['contact6_void'] = crop_asset('contact6_void', sources['contact6'], (.05,.05,.95,.95))

places = json.loads((ROOT/'intelligence/places.json').read_text())['places']
routes = json.loads((ROOT/'intelligence/routes.json').read_text())['routes']
camp = json.loads((ROOT/'intelligence/camps.json').read_text())['camps'][0]
figs = json.loads((ROOT/'presentation/key_figures.json').read_text())['key_figures']
# Keep all coords but mark confidence. Client projects to schematic map.
map_places = []
for p in places:
    if p.get('coordinates'):
        map_places.append({
            'id': p['place_id'], 'name': p['display_name'], 'type': p.get('place_type',''),
            'lat': p['coordinates']['lat'], 'lon': p['coordinates']['lon'],
            'confidence': p.get('coordinate_confidence','unknown'),
            'note': p.get('modern_trail_note',''),
            'desc': p.get('description_from_text','')[:180]
        })
map_routes = [{k:r.get(k) for k in ['route_id','name','description','waypoints','distance_miles','elevation_gain_ft','date']} for r in routes]

story_cards = [
    ('Fever', 'Field Station, July 8', '“ice-axes and alpen-stocks—and umbrellas”', 'A country arrives before it has a ritual.'),
    ('Delta', 'Emerald Lake north shore', '“the pack ponies were requisitioned as bridges”', 'Beauty becomes ordeal. Water edits the map.'),
    ('Town', 'Yoho Pass', '“a tented town nestling amid the realm of trees”', 'A temporary republic: Residence Park, Official Square, horse paddock.'),
    ('Rule', 'Circular No. 1', '“No lady climbing, who wears skirts…”', 'Safety technology disguised as social revolution.'),
    ('Rite', 'The Vice-President', '“Not one… failed.”', 'The mountain becomes a citizenship exam.'),
    ('Mammon', 'Elizabeth Parker', '“the monster, Mammon”', 'The club is born already arguing with tourism.'),
    ('Ice', 'Yoho Glacier', '“76 feet 7 inches”', 'A beautiful arch becomes a measuring instrument.'),
    ('Contradiction', 'Marpole, closing day', '“drenched to the skin but very joyful”', 'The archive disagrees; the weather keeps the truth.'),
]

people = [
    ('Elizabeth Parker','ideology','Co-founder, secretary, anti-Mammon manifesto'),
    ('Arthur O. Wheeler','logistics','Surveyor-president; turns camp into instrument'),
    ('Mary Vaux','vision','Photographer, colorist, glacier witness'),
    ('George & William Vaux','measurement','Repeat photography, plates, 76 ft 7 in'),
    ('Frank Yeigh','myth','Narrator of fever, deluge, fire, tented town'),
    ('Gottfried / Edouard Feuz','risk','Swiss guidecraft and mountain authority'),
    ('Jim Bong','camp body','Cook: the smell, hunger, labor of the tent city'),
    ('McLennan / Hobbs / Jean Parker','proof','Women on the rope as competence, not decoration'),
]

slides = []
def s(content, cls=''):
    slides.append(f'<section class="slide {cls}" data-i="{len(slides)}">{content}</section>')

count_markup = '<div class="count"></div>'
footer = lambda txt='': f'<footer><span>{html.escape(txt)}</span>{count_markup}</footer>'

s(f'''
<img class="bg" src="{asset['vaux_hero']}" alt="Vaux alpine view"><div class="shade"></div>
<div class="chapter">HERMESPRESENTATION / REIMAGINED</div>
<div class="heroBlock"><h1>The Mountain That Invented a Club</h1><p>Not a map deck. Not a heritage copy. A hallucination constrained by evidence: fire, ice, women on the rope, railway spectacle, Quaker cameras, and a glacier quietly becoming a clock.</p></div>
<div class="ribbon">Use ← / → · Press M for map lens · Press E for evidence overlays</div>{footer('BASECAMP corpus · Yoho Pass · July 1906')}
''','cover')

s(f'''
<div class="chapter">THESIS</div><h2>You cannot visit 1906. You can visit the places that hold its shadow.</h2>
<div class="split"><div><p class="lead">Every pin is a claim. Every route is a reading. The story is not “where exactly was it?” but “what kind of machine did these people build in the mountains?”</p><div class="axioms"><b>Known</b><b>Approximate</b><b>Estimated</b><b>Vanished</b><span>Field / Emerald / Takakkaw</span><span>Camp / pass / glacier edges</span><span>viewpoints / ridges / lost trails</span><span>hotel, tents, ice positions</span></div></div><div class="probability"><div>NOT A PIN</div><svg viewBox="0 0 600 420"><circle cx="300" cy="210" r="38"/><circle cx="300" cy="210" r="100"/><circle cx="300" cy="210" r="180"/><path d="M70,330 C210,120 380,360 535,86"/><text x="80" y="70">coordinates are a reading of the archive</text></svg><div>BUT A PROBABILITY</div></div></div>{footer('Spatial method: confidence halos, route corridors, ghost ice')}
''','paper')

s(f'''
<div class="chapter">01 / FIELD STATION FEVER</div><div class="triptych"><img src="{asset['packtrail']}"><div class="quote"><span>“Some were armed with ice-axes and alpen-stocks—and umbrellas.”</span><small>Frank Yeigh, First Camp</small></div><img src="{asset['lake_louise_chalet']}"></div><h2>Before the sublime, the logistics are ridiculous.</h2><p class="bottomLead">The opening feeling is not solemn heritage. It is bodies and baggage, fever and comic equipment: a railway platform where Canada rehearses mountain nationhood with horses, wagons, cooks, tents, flags, and 40-pound limits.</p>{footer('Arrival motif: railway enables wilderness and threatens to consume it')}
''')

s(f'''
<div class="chapter">02 / THE DELTA EDITS THE MAP</div><img class="bg ghost" src="{asset['bow_range']}"><div class="shade hard"></div><div class="bigQuote">“After the delta, the deluge.”</div><div class="deltaNotes"><div>Emerald Lake looks like a postcard.</div><div>Then the bridges are gone.</div><div>Then pack ponies become bridges.</div><div>Then the trail climbs 1,000 feet through wet spruce.</div></div>{footer('A route is not a line. It is a negotiation with water.')}
''','imageText')

s(f'''
<div class="chapter">03 / A TEMPORARY REPUBLIC</div><div class="split"><div><h2>A town of canvas appears at 6,000 feet.</h2><p>Residence Park. Official Square. Horse paddock. Dining tent for one hundred. Bulletin board. Camp fire. Speeches. Jokes. Bunting. A club turns wilderness into civic theatre for one week, then disappears.</p><div class="stats"><b>{camp['actual_attendance']}</b><span>attendees</span><b>{camp['capacity']}</b><span>planned capacity</span><b>{camp['graduation_stats']['women_graduates']}</b><span>women graduates</span></div></div><div class="stackedPhotos"><img src="{asset['camp_group']}"><img src="{asset['mary_forest']}"></div></div>{footer('Camp as pop-up city: social heat at night, scientific cold by day')}
''')

s(f'''
<div class="chapter">04 / NO SKIRTS ON THE ROPE</div><div class="fashion"><div><h2>The most radical artifact is a clothing rule.</h2><p>“No lady climbing, who wears skirts, will be allowed to take a place on a rope…” The line reads comic now. In 1906 it is safety policy, gender technology, and permission structure all at once.</p></div><div class="ruleCard">NO LADY<br>CLIMBING<br>IN SKIRTS<br><small>rope rule / Circular No. 1</small></div><img src="{asset['elizabeth_report']}"></div>{footer('Women are not decorative in this story; they are the proof the ritual worked')}
''','paper')

s(f'''
<div class="chapter">05 / THE VICE-PRESIDENT AS EXAM</div><img class="bg ghost" src="{asset['glacier_people']}"><div class="shade"></div><div class="heroBlock right"><h2>The mountain becomes a credentialing machine.</h2><p>Five official ascents. A threshold above 9,000 feet. Rock, snow, ice, ridge, rest places. The archive says 42 in one place and 44 in another. Keep the contradiction: membership is a story told by tired people.</p><div class="badgeRow"><span>5 ascents</span><span>0 failures</span><span>15 women</span><span>42/44 graduates</span></div></div>{footer('Contradictions are not bugs; they are the grain of the archive')}
''','imageText')

s(f'''
<div class="chapter">06 / AGAINST MAMMON</div><div class="manifesto"><h2>Elizabeth Parker writes an anti-tourism manifesto inside a tourism machine.</h2><blockquote>“To popularize mountaineering is not to vulgarize… the way of the monster, Mammon.”</blockquote><p>The railway makes the camp possible. The club immediately fears what steam, electricity, hotels, and commerce will do to the solitude it loves. This contradiction should stay loud.</p></div>{footer('Preservation vs access is already present at the founding')}
''','black')

s(f'''
<div class="chapter">07 / LIGHT TABLE</div><h2>The Vaux material is not a set of pictures. It is a machine for seeing.</h2><div class="lightTable"><img src="{asset['contact1']}"><img src="{asset['contact4']}"><img src="{asset['contact5']}"><div class="loupe"><img src="{asset['contact4_ice_detail']}"><span>contact sheets are field logic: sequence, repetition, label, return</span></div></div>{footer('Vaux contact sheets: abundance as method')}
''')

s(f'''
<div class="chapter">08 / THE GLACIER CLOCK</div><div class="split"><div class="evidencePane"><img src="{asset['daytimer_open']}"><img src="{asset['daytimer_close']}"></div><div><h2>On July 15, two primary sources click into place.</h2><p class="lead">Wheeler’s daytimer: “Vaux Bros. there helping.” Vaux paper: “76 feet 7 inches.” The camp was not merely recreation; it was a working scientific station.</p><div class="measurement"><b>76 ft 7 in</b><span>distance measured from earlier glacier mark</span></div><p>The glacier is beautiful, shrinking, and measurable. The mountain story suddenly becomes climate history.</p></div></div>{footer('Field diary + published measurement corroborate the same day')}
''','paper')

s(f'''
<div class="chapter">09 / TWO CAMPS, TWO RELIGIONS</div><div class="split"><div class="fireIce"><div>MAIN CAMP<br><small>service, speeches, fire, fellowship</small></div><div>VAUX CAMP<br><small>plates, rocks, camera, readings</small></div></div><div><h2>Sunday splits into hymn and instrument.</h2><p>Wheeler returns from the glacier, lunches at the separate Vaux Camp, and reaches Yoho Camp as service is being held. The day gives us the whole project: reverence by song, reverence by measurement.</p><img class="wide" src="{asset['seracs']}"></div></div>{footer('Fire versus ice: the presentation’s core visual opposition')}
''')

s(f'''
<div class="chapter">10 / CARTOGRAPHIC HUMILITY</div><h2>Make uncertainty visible.</h2><div class="mapStage"><svg id="probMap" viewBox="0 0 1200 620"></svg><div class="legend"><b>Known</b><span class="dot exact"></span><b>Approximate</b><span class="dot approx"></span><b>Estimated</b><span class="dot estimated"></span><p>Solid anchors are modern named places. Halos are interpretive. Route lines are corridors, not GPS tracks.</p></div></div>{footer('Click points in the live deck to open approximate Google Earth searches')}
''','mapslide')

s(f'''
<div class="chapter">11 / THE ARCHIVE DISAGREES</div><div class="split"><div><h2>Closing day: the neat story falls apart.</h2><p>Wheeler’s diary hints the Marpole party left late “no guides” and came back drenched but joyful. The official report names the Feuz guides. The archive is weather. It fogs, clears, contradicts itself, and still leaves a route.</p><div class="contradiction"><span>DAYTIMER</span><b>no guides?</b><span>OFFICIAL REPORT</span><b>Feuz guides</b></div></div><img class="polaroid" src="{asset['guides']}"></div>{footer('Do not over-clean the past; uncertainty is part of the drama')}
''','paper')

s(f'''
<div class="chapter">12 / THE LAST NEGATIVE</div><div class="voidSlide"><img src="{asset['contact6_void']}"><div><h2>The archive ends in white space.</h2><p>The final contact sheet is almost empty: one surviving canoe image floating in the blank. After all the abundance, this emptiness feels honest. A corpus is never complete. A mountain keeps most of what happened.</p></div></div>{footer('Abundance and absence belong together')}
''')

s(f'''
<div class="chapter">13 / WHAT HERMES SHOULD BE HERE</div><h2>A living field atlas, not a finished slide deck.</h2><div class="cards">{''.join(f'<div><b>{html.escape(a)}</b><span>{html.escape(b)}</span><p>{html.escape(c)}</p></div>' for a,b,c in [('Evidence mode','source-first', 'Every quote can reveal its file path.'),('Earth mode','place-first','Modern locations open as approximate searches.'),('Light table','image-first','Contact sheets become navigable objects.'),('Contradiction layer','truth-first','Disagreements are preserved, not flattened.'),('Glacier clock','time-first','Historic photographs become climate instruments.'),('Visitor mode','today-first','Where can someone stand now, and what should they not overclaim?')])}</div>{footer('This is the new HermesPresentation direction')}
''','black')

s(f'''
<img class="bg" src="{asset['wapta_valley']}" alt="Wapta valley"><div class="shade"></div><div class="heroBlock"><div class="chapter">END / BEGIN FIELDWORK</div><h1>This is where the story points.</h1><p>Not the exact bootprint. The probability. The return. The argument between fire and ice. The mountain as institution, camera, ledger, test, and witness.</p></div>{footer('Next build: real Earth flyover frames + clickable source drawer for every quote')}
''','cover')

slides_html='\n'.join(slides)
CSS = r'''
:root{--ink:#f4ead8;--muted:#c9bda7;--dim:#8f806b;--bg:#070707;--paper:#e8d8b9;--paperInk:#1a130b;--rust:#b9572e;--gold:#d9a84e;--ice:#8fc6d4;--green:#6c8261;--line:rgba(244,234,216,.24);--mono:ui-monospace,SFMono-Regular,Consolas,monospace;--sans:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif;--serif:Georgia,'Times New Roman',serif}*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;background:#030303;color:var(--ink);font-family:var(--sans);overflow:hidden}.deck{width:100vw;height:100vh;position:relative}.slide{position:absolute;inset:0;padding:62px 74px 52px;display:grid;grid-template-rows:auto 1fr auto;opacity:0;pointer-events:none;transform:translate3d(28px,0,0) scale(.985);transition:opacity .45s ease,transform .45s ease;background:radial-gradient(circle at 10% 0%,rgba(185,87,46,.16),transparent 34%),linear-gradient(145deg,#111,#050505 60%)}.slide.active{opacity:1;transform:none;pointer-events:auto;z-index:2}.paper{background:linear-gradient(135deg,#eadbbc,#d0bb92);color:var(--paperInk)}.black{background:radial-gradient(circle at 70% 30%,rgba(185,87,46,.16),transparent 36%),#050505}.chapter{font:800 13px/1 var(--mono);letter-spacing:.28em;text-transform:uppercase;color:var(--gold);z-index:3}.paper .chapter{color:#84512d}h1,h2{font-family:var(--serif);letter-spacing:-.055em;line-height:.91;margin:0;text-wrap:balance}h1{font-size:124px;max-width:1320px}h2{font-size:82px;max-width:1280px}.paper h1,.paper h2{color:var(--paperInk)}p{font-size:27px;line-height:1.32;color:var(--muted);margin:0}.paper p{color:#443624}.lead{font-size:34px;color:inherit;line-height:1.24}.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:contrast(1.08) saturate(.86) brightness(.78)}.ghost{filter:grayscale(.18) contrast(1.12) brightness(.62)}.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.93),rgba(0,0,0,.58) 48%,rgba(0,0,0,.18)),radial-gradient(circle at 70% 30%,transparent,rgba(0,0,0,.72));z-index:1}.shade.hard{background:linear-gradient(90deg,rgba(0,0,0,.88),rgba(0,0,0,.42)),linear-gradient(0deg,rgba(0,0,0,.82),transparent 55%,rgba(0,0,0,.45))}.heroBlock{position:relative;z-index:2;align-self:center;max-width:1250px}.heroBlock p{font-size:32px;max-width:910px;margin-top:28px;color:#dac7a5}.heroBlock.right{margin-left:auto;max-width:980px}.ribbon{position:absolute;right:72px;top:66px;z-index:5;border:1px solid rgba(244,234,216,.25);border-radius:999px;padding:13px 18px;font:13px var(--mono);letter-spacing:.08em;color:#d8c89e;background:rgba(0,0,0,.28);backdrop-filter:blur(8px)}footer{display:flex;justify-content:space-between;gap:20px;position:relative;z-index:4;font:13px/1.35 var(--mono);letter-spacing:.08em;color:#b9aa8c;text-transform:uppercase}.paper footer{color:#6a563a}.count{color:var(--gold)}.split{display:grid;grid-template-columns:1fr 1fr;gap:52px;align-items:center;height:100%;position:relative;z-index:2}.triptych{height:560px;display:grid;grid-template-columns:.9fr 1.1fr .9fr;gap:22px;align-items:stretch}.triptych img,.stackedPhotos img,.wide,.polaroid{width:100%;height:100%;object-fit:cover;border:1px solid var(--line);box-shadow:0 28px 80px rgba(0,0,0,.35)}.quote{display:flex;flex-direction:column;justify-content:center;border:1px solid var(--line);padding:38px;background:rgba(255,255,255,.055)}.quote span{font:italic 50px/1.1 var(--serif)}.quote small{font:14px var(--mono);color:var(--gold);margin-top:26px;letter-spacing:.12em;text-transform:uppercase}.bottomLead{position:relative;z-index:3;font-size:29px;margin-top:28px;max-width:1500px}.axioms{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:36px}.axioms>*{border:1px solid rgba(20,15,9,.22);padding:16px}.axioms b{font:18px var(--mono);text-transform:uppercase}.axioms span{font-size:17px;color:#5b4a33}.probability{height:620px;border:1px solid rgba(20,15,9,.25);display:grid;place-items:center;background:rgba(255,255,255,.16)}.probability div{font:800 18px var(--mono);letter-spacing:.24em}.probability svg{width:82%;height:70%}.probability circle{fill:none;stroke:#98562d;stroke-width:2;stroke-dasharray:8 9}.probability path{fill:none;stroke:#1b130a;stroke-width:5}.probability text{font:18px var(--mono);fill:#1b130a}.deltaNotes{position:relative;z-index:2;align-self:end;display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.deltaNotes div{background:rgba(0,0,0,.52);border:1px solid rgba(244,234,216,.18);padding:22px;font:24px/1.15 var(--serif)}.bigQuote{position:relative;z-index:2;align-self:center;font:italic 92px/.95 var(--serif);max-width:900px}.stats{display:grid;grid-template-columns:auto 1fr;gap:4px 18px;margin-top:38px;align-items:end}.stats b{font:86px/.8 var(--serif);color:var(--gold)}.stats span{font:17px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}.stackedPhotos{display:grid;grid-template-rows:1fr 1fr;gap:20px;height:690px}.fashion{display:grid;grid-template-columns:1fr .72fr .9fr;gap:34px;align-items:center;height:100%}.fashion img{width:100%;height:680px;object-fit:cover;filter:sepia(.18);border:1px solid rgba(20,15,9,.24)}.ruleCard{background:#1b130b;color:#eadbbc;font:900 66px/.92 var(--mono);padding:44px;box-shadow:16px 16px 0 #b9572e;transform:rotate(-2deg)}.ruleCard small{display:block;font:16px var(--mono);letter-spacing:.12em;color:#d9a84e;margin-top:25px}.badgeRow{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}.badgeRow span{border:1px solid rgba(244,234,216,.28);border-radius:999px;padding:13px 17px;background:rgba(0,0,0,.34);font:14px var(--mono);letter-spacing:.1em;text-transform:uppercase}.manifesto{display:grid;align-content:center;height:100%;max-width:1500px}.manifesto blockquote{font:italic 70px/1.05 var(--serif);color:var(--gold);margin:34px 0}.lightTable{height:720px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px;position:relative}.lightTable>img{width:100%;height:100%;object-fit:cover;border-radius:22px;border:1px solid var(--line);filter:sepia(.16) contrast(1.04);box-shadow:0 26px 70px rgba(0,0,0,.38)}.loupe{position:absolute;right:80px;bottom:38px;width:460px;background:#0a0a0a;border:1px solid rgba(244,234,216,.32);padding:18px;box-shadow:0 30px 80px rgba(0,0,0,.64);transform:rotate(2deg)}.loupe img{width:100%;height:260px;object-fit:cover}.loupe span{display:block;margin-top:12px;font:16px/1.25 var(--mono);color:#e5d3ac;text-transform:uppercase;letter-spacing:.08em}.evidencePane{display:grid;grid-template-columns:1fr 1fr;gap:18px}.evidencePane img{width:100%;height:650px;object-fit:cover;filter:contrast(1.25) sepia(.18);border:1px solid rgba(30,20,8,.24);box-shadow:0 20px 50px rgba(0,0,0,.25)}.measurement{margin:36px 0;padding:30px;border:2px solid #8a552f;background:rgba(255,255,255,.2)}.measurement b{font:86px/.9 var(--serif);display:block}.measurement span{font:18px var(--mono);text-transform:uppercase;letter-spacing:.12em}.fireIce{display:grid;grid-template-columns:1fr 1fr;height:560px;border:1px solid var(--line)}.fireIce div{display:grid;place-items:center;text-align:center;font:800 48px/1 var(--mono);letter-spacing:.08em}.fireIce div:first-child{background:radial-gradient(circle,#b9572e,transparent 58%),#120807}.fireIce div:last-child{background:radial-gradient(circle,#8fc6d4,transparent 58%),#061016}.fireIce small{font:15px/1.3 var(--mono);color:var(--muted);letter-spacing:.12em;max-width:280px;margin-top:18px}.wide{height:270px;margin-top:24px}.mapStage{height:720px;display:grid;grid-template-columns:1fr 310px;gap:24px}#probMap{width:100%;height:100%;border:1px solid var(--line);background:radial-gradient(circle at 45% 35%,rgba(143,198,212,.16),transparent 40%),#07100f}.legend{border:1px solid var(--line);padding:24px;display:grid;grid-template-columns:auto 1fr;align-content:start;gap:16px 12px}.legend p{grid-column:1/-1;font-size:20px}.dot{display:block;width:35px;height:35px;border-radius:50%;margin-left:auto}.dot.exact{background:#f4ead8}.dot.approx{background:#f4ead8;box-shadow:0 0 0 18px rgba(217,168,78,.2)}.dot.estimated{background:#8fc6d4;box-shadow:0 0 0 35px rgba(143,198,212,.15)}.contradiction{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:40px}.contradiction span{font:14px var(--mono);letter-spacing:.16em;color:#7b5838}.contradiction b{font:44px var(--serif);padding:24px;border:1px solid rgba(20,15,9,.24)}.polaroid{height:670px;transform:rotate(1deg);filter:sepia(.2)}.voidSlide{display:grid;grid-template-columns:.95fr 1fr;gap:52px;align-items:center;height:100%}.voidSlide img{width:100%;height:700px;object-fit:cover;background:white;border:1px solid var(--line)}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-self:center}.cards div{border:1px solid var(--line);padding:26px;min-height:210px;background:rgba(255,255,255,.045)}.cards b{font:34px var(--serif);display:block}.cards span{font:13px var(--mono);color:var(--gold);letter-spacing:.18em;text-transform:uppercase}.cards p{font-size:20px;margin-top:18px}.evidenceOn .slide:after{content:attr(data-source);position:absolute;left:74px;bottom:22px;right:220px;color:#f0c36a;font:11px var(--mono);letter-spacing:.06em;z-index:7}.mapLens #probMap{filter:saturate(1.3) contrast(1.12)}.controls{position:fixed;right:28px;bottom:22px;z-index:20;display:flex;gap:8px}.controls button{border:1px solid rgba(244,234,216,.28);background:rgba(0,0,0,.55);color:var(--ink);border-radius:999px;padding:10px 14px;font:13px var(--mono);cursor:pointer}.controls button:hover{background:rgba(244,234,216,.15)}.toast{position:fixed;left:28px;bottom:20px;z-index:30;font:12px var(--mono);color:#d8be82;letter-spacing:.08em}.mapLabel{font:12px var(--mono);fill:#f4ead8;text-shadow:0 2px 6px #000}.mapTiny{font:9px var(--mono);fill:#a99a7f}@media(max-width:900px){html,body{overflow:auto}.deck{height:auto}.slide{position:relative;min-height:100vh;opacity:1;transform:none;pointer-events:auto;display:block;padding:34px 20px}h1{font-size:56px}h2{font-size:44px}.split,.triptych,.fashion,.mapStage,.voidSlide,.cards{display:grid;grid-template-columns:1fr;height:auto}.bg{position:absolute}.controls{display:none}}
'''

CSS += r'''
/* QA readability overrides: safer projector margins, brighter body text, calmer controls */
.slide{padding:72px 92px 60px}
p{color:#dfd1b8}.black p,.slide:not(.paper) p{color:#ddd0b8}.paper p{color:#362818}
footer{font-size:14px;color:#d4c29e}.paper footer{color:#59442b}
.controls{opacity:.12}.controls:hover{opacity:.75}
.toast{opacity:.68}
.manifesto{max-width:1660px}.manifesto p{max-width:1260px}.manifesto blockquote{color:#e2b45e}
.cards{align-self:start;margin-top:20px}.cards p{font-size:23px;line-height:1.25}.cards span{font-size:14px}.cards div{min-height:230px;background:rgba(255,255,255,.06)}
.lightTable{height:680px}.loupe{width:520px}.loupe span{font-size:18px}
.heroBlock p{color:#ead8b6}
.stats span{font-size:20px;color:#dfd1b8}
.mapLabel{font-size:14px}.mapTiny{font-size:10px;fill:#d0c1a5}
.evidenceOn .slide:after{font-size:13px;color:#ffd27a}
'''

JS = f'''
const PLACES={json.dumps(map_places)};
const ROUTES={json.dumps(map_routes)};
const slides=[...document.querySelectorAll('.slide')];
const params=new URLSearchParams(location.search);
let idx=params.has('slide')?Number(params.get('slide')):Number(localStorage.getItem('hp-reimagined-slide')||0);
if(!Number.isFinite(idx)||idx<0||idx>=slides.length) idx=0;
function show(n){{slides[idx].classList.remove('active');idx=(n+slides.length)%slides.length;slides[idx].classList.add('active');localStorage.setItem('hp-reimagined-slide',idx);document.querySelectorAll('.count').forEach(c=>c.textContent=`${{String(idx+1).padStart(2,'0')}} / ${{slides.length}}`);}}
document.querySelector('#prev').onclick=()=>show(idx-1);document.querySelector('#next').onclick=()=>show(idx+1);
addEventListener('keydown',e=>{{if(['ArrowRight','PageDown',' '].includes(e.key)){{e.preventDefault();show(idx+1)}} if(['ArrowLeft','PageUp'].includes(e.key)){{e.preventDefault();show(idx-1)}} if(e.key==='Home')show(0); if(e.key==='End')show(slides.length-1); if(e.key.toLowerCase()==='e')document.body.classList.toggle('evidenceOn'); if(e.key.toLowerCase()==='m')document.body.classList.toggle('mapLens');}});
function drawMap(){{const svg=document.querySelector('#probMap'); if(!svg) return; const chosen=['field-station','emerald-lake-chalet','emerald-lake-north-delta','camp-yoho','yoho-pass','yoho-lake','takakkaw-falls','laughing-falls','twin-falls','yoho-glacier','emerald-glacier','vice-president','michael-peak','burgess-pass','mt-stephen-house']; const ps=PLACES.filter(p=>chosen.includes(p.id)); const lats=ps.map(p=>p.lat), lons=ps.map(p=>p.lon); const minLat=Math.min(...lats)-.01,maxLat=Math.max(...lats)+.012,minLon=Math.min(...lons)-.012,maxLon=Math.max(...lons)+.012; const X=lon=>70+(lon-minLon)/(maxLon-minLon)*1030; const Y=lat=>570-(lat-minLat)/(maxLat-minLat)*500; const by=Object.fromEntries(PLACES.map(p=>[p.id,p])); let s='';
 for(let i=0;i<52;i++){{s+=`<circle cx="${{(i*137)%1200}}" cy="${{(i*73)%620}}" r="${{1+(i%4)}}" fill="rgba(244,234,216,.07)"/>`;}}
 const colors={{'field-to-camp':'#d9a84e','vice-president-official':'#b9572e','yoho-valley-round':'#8fc6d4','emerald-glacier-trip':'#c4e1e7','burgess-pass-return':'#8aa36f'}};
 for(const r of ROUTES){{const pts=r.waypoints.map(id=>by[id]).filter(Boolean).map(p=>`${{X(p.lon)}},${{Y(p.lat)}}`).join(' '); if(pts) s+=`<polyline points="${{pts}}" fill="none" stroke="${{colors[r.route_id]||'#fff'}}" stroke-width="${{r.route_id==='field-to-camp'?5:3}}" stroke-dasharray="${{r.route_id==='field-to-camp'?'':'9 10'}}" stroke-linecap="round" stroke-linejoin="round" opacity=".78"/>`;}}
 for(const p of ps){{const x=X(p.lon),y=Y(p.lat); const conf=p.confidence||'approximate'; const rr=conf==='exact'?9:conf==='estimated'?32:20; const fill=conf==='estimated'?'#8fc6d4':'#f4ead8'; const halo=conf==='exact'?'rgba(244,234,216,.18)':conf==='estimated'?'rgba(143,198,212,.20)':'rgba(217,168,78,.22)'; const label=p.name.replace(/&/g,'&amp;'); s+=`<a href="https://earth.google.com/web/search/${{p.lat}},${{p.lon}}" target="_blank"><circle cx="${{x}}" cy="${{y}}" r="${{rr}}" fill="${{halo}}"/><circle cx="${{x}}" cy="${{y}}" r="7" fill="${{fill}}" stroke="#050505" stroke-width="2"/><text x="${{x+13}}" y="${{y-9}}" class="mapLabel">${{label}}</text><text x="${{x+13}}" y="${{y+7}}" class="mapTiny">${{conf}} · ${{p.type}}</text></a>`;}}
 s+=`<text x="70" y="45" class="mapLabel" style="font-size:17px;letter-spacing:.18em">NOT A PIN, BUT A PROBABILITY</text><text x="70" y="70" class="mapTiny">route corridors · confidence halos · approximate historic terrain</text>`; svg.innerHTML=s;}}
drawMap(); show(idx);
'''

html_doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HermesPresentation — The Mountain That Invented a Club</title><link rel="icon" href="favicon.svg" type="image/svg+xml"><style>{CSS}</style></head><body><main class="deck">{slides_html}</main><div class="controls"><button id="prev">←</button><button id="next">→</button></div><div class="toast">M map lens · E evidence overlay</div><script>{JS}</script></body></html>'''
idx.write_text(html_doc)
(OUT/'README.reimagined.md').write_text('''# HermesPresentation — Reimagined\n\nThis is the second, creative-first version. It intentionally does not copy the earlier coordinate atlas.\n\nRun:\n\n```bash\ncd /mnt/c/Users/chris/BASECAMP/presentation/HermesPresentation\n./run.sh\n```\n\nOpen http://127.0.0.1:8765/index.html\n\nControls: left/right arrows, Home/End, M for map lens, E for evidence overlay.\n\nConcept: The Mountain That Invented a Club — a visual field atlas about uncertainty, fire, ice, Vaux repeat photography, women on the rope, anti-Mammon preservation politics, and the glacier as a clock.\n''')
print(idx)
print(idx.stat().st_size)
print('assets', len(list(ASSETS.glob('*.jpg'))), sum(p.stat().st_size for p in ASSETS.glob('*.jpg')))
