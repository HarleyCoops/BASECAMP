from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
import csv, json, re, shutil, html

ROOT = Path('/mnt/c/Users/chris/BASECAMP')
OUT = ROOT/'presentation/HermesPresentation/LightTable'
ASSETS = OUT/'assets'
ASSETS.mkdir(parents=True, exist_ok=True)

manifest = json.loads((ROOT/'people/george-vaux/artifacts/_manifest.json').read_text())
manifest_items = manifest['items']
by_url = {}
by_perm = {}
for it in manifest_items:
    by_url[Path(it['asset_url']).name.lower()] = it
    by_perm[it['permalink']] = it

# Contact sheets, including the almost-empty absence sheet.
contacts = []
for i in range(1,7):
    src = ROOT/f'people/george-vaux/research/1906_shotlist/thumbs/contact_1906_p{i}.jpg'
    name = f'contact_1906_p{i}.jpg'
    dst = ASSETS/name
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    im.thumbnail((1900,1900), Image.Resampling.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(1.05)
    im.save(dst,'JPEG',quality=88,optimize=True,progressive=True)
    contacts.append({
        'id': f'contact-{i}',
        'title': f'Vaux 1906 contact sheet {i}',
        'src': f'assets/{name}',
        'role': 'absence' if i == 6 else 'sequence',
        'note': 'Almost empty: one surviving frame and a field of blank paper.' if i == 6 else 'Contact sheet as method: sequence, repetition, labels, return.'
    })

# Build selected image records from CSV rows that have local downloaded files, plus priority known images.
rows = []
for fn in ['vaux_1906_flagged.csv','vaux_1906_rockies.csv']:
    with open(ROOT/f'people/george-vaux/research/1906_shotlist/{fn}', newline='', encoding='utf-8-sig') as fh:
        for r in csv.DictReader(fh):
            rows.append(r)
seen = set()
records = []
priority_words = ['Wapta','Yoho','Ice arch','Forefoot','Mt. Stephen','Takakkaw','Emerald','camp','Camp','Glacier','Horseshoe','Vice','Lake Louise','Summit Lake']
for r in rows:
    img_name = Path(r.get('image_url','')).name.lower()
    it = by_url.get(img_name)
    if not it or not it.get('downloaded'):
        continue
    if it['file'] in seen:
        continue
    text = ' '.join([r.get('title',''), r.get('scope',''), r.get('ref','')])
    score = sum(3 for w in priority_words if w.lower() in text.lower()) + (5 if it.get('yoho_1906') else 0)
    records.append((score,r,it))
    seen.add(it['file'])
records.sort(key=lambda x: (-x[0], x[1].get('ref','')))
records = records[:32]

images = []
for idx,(score,r,it) in enumerate(records):
    src = ROOT/'people/george-vaux/artifacts'/it['file']
    ext = Path(it['file']).suffix.lower() or '.jpg'
    safe = re.sub(r'[^a-z0-9]+','-', Path(it['file']).stem.lower()).strip('-')[:70]
    name = f'{idx+1:02d}-{safe}.jpg'
    dst = ASSETS/name
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    im.thumbnail((1800,1800), Image.Resampling.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    im.save(dst,'JPEG',quality=87,optimize=True,progressive=True)
    low = (r.get('title','')+' '+r.get('scope','')).lower()
    tags = []
    for t in ['yoho','wapta','glacier','camp','takakkaw','emerald','summit lake','ice arch','lake louise','horseshoe','mt. stephen']:
        if t in low: tags.append(t)
    if it.get('yoho_1906') and 'yoho' not in tags: tags.append('yoho')
    images.append({
        'id': f'img-{idx+1:02d}',
        'src': f'assets/{name}',
        'title': r.get('title') or it.get('title') or it['file'],
        'scope': r.get('scope',''),
        'ref': r.get('ref',''),
        'date': r.get('date',''),
        'permalink': r.get('permalink') or it.get('permalink'),
        'asset_url': r.get('image_url') or it.get('asset_url'),
        'file': it['file'],
        'yoho_1906': bool(it.get('yoho_1906')),
        'tags': tags,
        'score': score
    })

places = json.loads((ROOT/'intelligence/places.json').read_text())['places']
place_pick = []
for p in places:
    if p.get('coordinates') and p['place_id'] in ['field-station','emerald-lake-chalet','emerald-lake-north-delta','yoho-pass','camp-yoho','yoho-lake','takakkaw-falls','yoho-glacier','wapta-glacier','laughing-falls','twin-falls','mt-stephen-house']:
        place_pick.append({
            'id': p['place_id'], 'name': p['display_name'], 'lat': p['coordinates']['lat'], 'lon': p['coordinates']['lon'],
            'confidence': p.get('coordinate_confidence','estimated'), 'type': p.get('place_type',''),
            'note': p.get('modern_trail_note') or p.get('description_from_text','')[:160]
        })

DATA = {'contacts': contacts, 'images': images, 'places': place_pick}
(OUT/'data.json').write_text(json.dumps(DATA, indent=2))

css = r'''
:root{--bg:#060504;--ink:#f3e8d4;--muted:#b9a98e;--dim:#786d5c;--gold:#d8aa54;--rust:#a64e2e;--ice:#9bcbd6;--paper:#e2d0ad;--line:rgba(243,232,212,.18);--panel:rgba(13,12,10,.82);--mono:ui-monospace,SFMono-Regular,Consolas,monospace;--serif:Georgia,'Times New Roman',serif;--sans:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif}*{box-sizing:border-box}html,body{margin:0;height:100%;background:var(--bg);color:var(--ink);font-family:var(--sans);overflow:hidden}body:before{content:"";position:fixed;inset:0;background:radial-gradient(circle at 20% 10%,rgba(166,78,46,.2),transparent 32%),radial-gradient(circle at 80% 30%,rgba(155,203,214,.11),transparent 35%),linear-gradient(180deg,#090807,#020202);pointer-events:none}.app{position:relative;height:100vh;display:grid;grid-template-columns:340px 1fr 410px;grid-template-rows:82px 1fr 120px;gap:14px;padding:18px}.top{grid-column:1/-1;display:flex;align-items:center;justify-content:space-between;border:1px solid var(--line);background:rgba(0,0,0,.36);padding:14px 18px}.brand{display:flex;gap:18px;align-items:baseline}.brand h1{font-family:var(--serif);font-size:38px;letter-spacing:-.05em;margin:0}.brand span{font:12px var(--mono);letter-spacing:.22em;color:var(--gold);text-transform:uppercase}.modes{display:flex;gap:8px}.modes button,.ghostbtn{border:1px solid var(--line);background:rgba(255,255,255,.04);color:var(--ink);padding:10px 12px;border-radius:999px;font:12px var(--mono);letter-spacing:.08em;text-transform:uppercase;cursor:pointer}.modes button.active,.ghostbtn:hover{background:var(--gold);color:#171006;border-color:var(--gold)}.left,.right,.stage,.strip{border:1px solid var(--line);background:var(--panel);backdrop-filter:blur(14px);min-height:0}.left{grid-row:2/4;overflow:hidden;display:grid;grid-template-rows:auto auto 1fr}.leftIntro{padding:18px;border-bottom:1px solid var(--line)}.leftIntro h2,.right h2{font-family:var(--serif);font-size:28px;line-height:.95;margin:0 0 10px}.leftIntro p,.right p{color:var(--muted);font-size:15px;line-height:1.38;margin:0}.filters{display:flex;gap:8px;flex-wrap:wrap;padding:12px 14px;border-bottom:1px solid var(--line)}.filters button{border:1px solid rgba(243,232,212,.14);background:rgba(255,255,255,.035);color:var(--muted);border-radius:999px;padding:8px 10px;font:11px var(--mono);cursor:pointer}.filters button.active{color:#111;background:var(--ice);border-color:var(--ice)}.thumbs{overflow:auto;padding:12px;display:grid;grid-template-columns:1fr 1fr;gap:10px}.thumb{border:1px solid rgba(243,232,212,.15);background:#111;min-height:110px;position:relative;cursor:pointer;overflow:hidden}.thumb img{width:100%;height:122px;object-fit:cover;display:block;filter:sepia(.12) contrast(1.05)}.thumb.active{outline:2px solid var(--gold)}.thumb b{position:absolute;left:7px;right:7px;bottom:6px;font:10px/1.15 var(--mono);text-shadow:0 1px 6px #000;color:#fff}.stage{grid-column:2;grid-row:2;position:relative;overflow:hidden;display:grid;place-items:center}.viewer{position:absolute;inset:0;display:grid;place-items:center;overflow:hidden;background:#050505}.viewer img{max-width:92%;max-height:88%;object-fit:contain;transition:transform .2s ease, filter .2s ease;filter:sepia(.08) contrast(1.05);box-shadow:0 30px 100px rgba(0,0,0,.55)}.viewer.zoomed img{transform:scale(1.7)}.loupe{position:absolute;width:280px;height:220px;border:2px solid var(--gold);border-radius:4px;box-shadow:0 20px 50px rgba(0,0,0,.55);background-repeat:no-repeat;background-color:#111;pointer-events:none;display:none}.viewer.inspecting .loupe{display:block}.overTitle{position:absolute;left:24px;top:22px;max-width:720px;text-shadow:0 2px 14px #000}.overTitle .kicker{font:12px var(--mono);letter-spacing:.18em;color:var(--gold);text-transform:uppercase}.overTitle h2{font-family:var(--serif);font-size:52px;line-height:.9;letter-spacing:-.05em;margin:8px 0 0}.hint{position:absolute;left:24px;bottom:20px;font:12px var(--mono);letter-spacing:.1em;color:#e6d4ad;text-transform:uppercase;background:rgba(0,0,0,.72);border:1px solid rgba(243,232,212,.16);border-radius:999px;padding:10px 13px;text-shadow:0 2px 8px #000}.right{grid-column:3;grid-row:2/4;display:grid;grid-template-rows:auto 1fr auto;overflow:hidden}.meta{padding:22px;border-bottom:1px solid var(--line)}.meta .ref{font:12px var(--mono);letter-spacing:.12em;color:var(--gold);text-transform:uppercase}.meta h2{font-size:34px}.chips{display:flex;gap:7px;flex-wrap:wrap;margin-top:14px}.chips span{border:1px solid rgba(243,232,212,.14);padding:6px 8px;border-radius:999px;font:10px var(--mono);color:var(--muted);text-transform:uppercase}.sourceBox{padding:18px;overflow:auto}.sourceBox dl{display:grid;grid-template-columns:86px 1fr;gap:10px;font-size:13px;line-height:1.3}.sourceBox dt{font:11px var(--mono);letter-spacing:.12em;color:var(--dim);text-transform:uppercase}.sourceBox dd{margin:0;color:#d8c8aa;word-break:break-word}.sourceBox a{color:var(--ice)}.notes{border-top:1px solid var(--line);padding:16px;color:var(--muted);font-size:14px;line-height:1.4}.strip{grid-column:2;grid-row:3;display:flex;gap:12px;overflow:auto;padding:12px}.contactCard{min-width:250px;border:1px solid rgba(243,232,212,.16);position:relative;cursor:pointer;background:#0d0c0a}.contactCard img{width:250px;height:92px;object-fit:cover;display:block;filter:sepia(.16) contrast(1.05)}.contactCard.active{outline:2px solid var(--gold)}.contactCard span{position:absolute;left:8px;bottom:7px;font:11px var(--mono);text-shadow:0 2px 8px #000}.mapMode .viewer,.sequenceMode .viewer,.absenceMode .viewer{background:radial-gradient(circle at 50% 50%,rgba(243,232,212,.08),transparent 28%),#050505}.mapCanvas{width:100%;height:100%;display:none}.mapMode .mapCanvas{display:block}.mapMode .viewer>img,.mapMode .overTitle{display:none}.sequenceGrid{display:none;position:absolute;inset:18px;grid-template-columns:repeat(5,1fr);gap:12px;overflow:auto}.sequenceMode .sequenceGrid{display:grid}.sequenceMode .viewer>img,.sequenceMode .overTitle{display:none}.seqCard{border:1px solid var(--line);background:#0b0a08;min-height:170px;cursor:pointer}.seqCard img{width:100%;height:135px;object-fit:cover}.seqCard p{font:11px/1.2 var(--mono);color:var(--muted);margin:7px}.absenceMode .viewer img{filter:grayscale(.1) contrast(1.08) brightness(1.06)}.absenceMode .overTitle h2:after{content:' / the archive ends in white space';color:var(--gold)}.mapLabel{font:13px var(--mono);fill:#f3e8d4;text-shadow:0 2px 8px #000}.mapTiny{font:10px var(--mono);fill:#b9a98e}.corridor{fill:none;stroke:var(--gold);stroke-width:4;stroke-dasharray:10 12;opacity:.78}.halo{fill:rgba(216,170,84,.18);stroke:rgba(216,170,84,.28)}.point{fill:#f3e8d4;stroke:#060504;stroke-width:2}.emptyState{padding:40px;text-align:center;color:var(--muted)}@media(max-width:1100px){html,body{overflow:auto}.app{height:auto;display:block}.top,.left,.stage,.right,.strip{margin:12px 0}.stage{height:70vh}.right{display:block}.thumbs{grid-template-columns:repeat(3,1fr)}}
'''

js = r'''
const DATA = __DATA__;
let mode='light', selected=null, filter='all';
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
function esc(s){return (s||'').replace(/[&<>]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[m]));}
function allItems(){return [...DATA.contacts.map(c=>({...c,kind:'contact'})),...DATA.images.map(i=>({...i,kind:'image'}))];}
function filteredImages(){let items=allItems(); if(filter==='all') return items; if(filter==='contact') return DATA.contacts.map(c=>({...c,kind:'contact'})); if(filter==='absence') return DATA.contacts.filter(c=>c.role==='absence').map(c=>({...c,kind:'contact'})); return DATA.images.filter(i=>(i.tags||[]).includes(filter)).map(i=>({...i,kind:'image'}));}
function pick(item){selected=item; renderStage(); renderMeta(); $$('.thumb,.contactCard,.seqCard').forEach(el=>el.classList.toggle('active',el.dataset.id===item.id)); localStorage.setItem('lighttable-selected', item.id)}
function renderThumbs(){const items=filteredImages(); $('.thumbs').innerHTML=items.map(it=>`<div class="thumb" data-id="${it.id}"><img src="${it.src}"><b>${esc(it.kind==='contact'?it.title:(it.ref||it.title))}</b></div>`).join('')||'<div class="emptyState">No images for this filter.</div>'; $$('.thumb').forEach(el=>el.onclick=()=>pick(allItems().find(i=>i.id===el.dataset.id)));}
function renderContacts(){ $('.strip').innerHTML=DATA.contacts.map(c=>`<div class="contactCard" data-id="${c.id}"><img src="${c.src}"><span>${esc(c.title)}</span></div>`).join(''); $$('.contactCard').forEach(el=>el.onclick=()=>pick(allItems().find(i=>i.id===el.dataset.id)));}
function renderStage(){ if(!selected) selected=allItems()[0]; document.body.className=mode+'Mode'; $('.viewer>img').src=selected.src; $('.viewer>img').alt=selected.title; $('.overTitle .kicker').textContent=selected.kind==='contact'?'CONTACT SHEET / SEQUENCE':'VAUX FRAME / EVIDENCE'; $('.overTitle h2').textContent=selected.title; drawMap(); renderSequence(); }
function renderMeta(){const it=selected; const tags=(it.tags||[it.role||'contact']).map(t=>`<span>${esc(t)}</span>`).join(''); $('.meta').innerHTML=`<div class="ref">${esc(it.ref||it.id)}</div><h2>${esc(it.title)}</h2><p>${esc(it.scope||it.note||'Contact sheet: sequence, adjacency, repetition, return.')}</p><div class="chips">${tags}</div>`; $('.sourceBox').innerHTML=`<dl><dt>kind</dt><dd>${esc(it.kind)}</dd><dt>date</dt><dd>${esc(it.date||'1906 / reconstructed')}</dd><dt>file</dt><dd>${esc(it.file||it.src)}</dd><dt>source</dt><dd>${it.permalink?`<a href="${it.permalink}" target="_blank">Whyte record</a>`:'local contact sheet derivative'}</dd><dt>claim</dt><dd>${it.yoho_1906?'flagged as Yoho 1906 in local manifest':'use as visual/evidentiary texture; do not overclaim exact place'}</dd></dl>`; $('.notes').innerHTML= mode==='map'? 'Map mode deliberately uses halos and route corridors. The pins are research handles, not truth.' : mode==='sequence'? 'Sequence mode shows the corpus as an editing room. Click a frame to make it evidence.' : mode==='absence'? 'Absence mode treats the nearly empty contact sheet as part of the story: abundance always ends at a blank edge.' : 'Inspect mode: hover over the large image for a loupe. Click to toggle zoom.';}
function setFilter(f){filter=f; $$('.filters button').forEach(b=>b.classList.toggle('active',b.dataset.filter===f)); renderThumbs();}
function setMode(m){mode=m; if(m==='absence') selected=allItems().find(i=>i.id==='contact-6')||selected; $$('.modes button').forEach(b=>b.classList.toggle('active',b.dataset.mode===m)); renderStage(); renderMeta();}
function renderSequence(){const grid=$('.sequenceGrid'); grid.innerHTML=DATA.images.slice(0,30).map(it=>`<div class="seqCard" data-id="${it.id}"><img src="${it.src}"><p>${esc(it.ref||it.title)}</p></div>`).join(''); $$('.seqCard').forEach(el=>el.onclick=()=>{pick(allItems().find(i=>i.id===el.dataset.id)); setMode('light')});}
function drawMap(){const svg=$('.mapCanvas'); const ps=DATA.places; if(!ps.length){svg.innerHTML=''; return} const minLat=Math.min(...ps.map(p=>p.lat))-.01,maxLat=Math.max(...ps.map(p=>p.lat))+.01,minLon=Math.min(...ps.map(p=>p.lon))-.015,maxLon=Math.max(...ps.map(p=>p.lon))+.015; const X=lon=>70+(lon-minLon)/(maxLon-minLon)*1060; const Y=lat=>650-(lat-minLat)/(maxLat-minLat)*560; let s='<rect width="1200" height="720" fill="#060908"/>'; for(let i=0;i<80;i++) s+=`<circle cx="${(i*149)%1200}" cy="${(i*83)%720}" r="${1+i%3}" fill="rgba(243,232,212,.08)"/>`; const route=['field-station','emerald-lake-chalet','emerald-lake-north-delta','yoho-pass','camp-yoho','yoho-lake','takakkaw-falls','yoho-glacier']; const by=Object.fromEntries(ps.map(p=>[p.id,p])); s+=`<polyline class="corridor" points="${route.map(id=>by[id]).filter(Boolean).map(p=>`${X(p.lon)},${Y(p.lat)}`).join(' ')}"/>`; for(const p of ps){const x=X(p.lon),y=Y(p.lat), r=p.confidence==='exact'?16:p.confidence==='approximate'?34:54; s+=`<a href="https://earth.google.com/web/search/${p.lat},${p.lon}" target="_blank"><circle class="halo" cx="${x}" cy="${y}" r="${r}"/><circle class="point" cx="${x}" cy="${y}" r="7"/><text class="mapLabel" x="${x+14}" y="${y-8}">${esc(p.name)}</text><text class="mapTiny" x="${x+14}" y="${y+9}">${esc(p.confidence)} · ${esc(p.type)}</text></a>`} s+=`<text class="mapLabel" x="70" y="52" style="font-size:20px;letter-spacing:.18em">MAP GUESSES, NOT MAP TRUTH</text><text class="mapTiny" x="70" y="78">click a halo to open an approximate Google Earth search</text>`; svg.innerHTML=s;}
function initLoupe(){const viewer=$('.viewer'), img=$('.viewer>img'), loupe=$('.loupe'); viewer.addEventListener('mousemove',e=>{ if(mode==='map'||mode==='sequence') return; const r=viewer.getBoundingClientRect(); const x=e.clientX-r.left,y=e.clientY-r.top; viewer.classList.add('inspecting'); loupe.style.left=Math.min(Math.max(x+18,10),r.width-300)+'px'; loupe.style.top=Math.min(Math.max(y+18,10),r.height-240)+'px'; loupe.style.backgroundImage=`url(${img.src})`; loupe.style.backgroundSize='220% auto'; loupe.style.backgroundPosition=`${(x/r.width)*100}% ${(y/r.height)*100}%`; }); viewer.addEventListener('mouseleave',()=>viewer.classList.remove('inspecting')); viewer.addEventListener('click',()=>viewer.classList.toggle('zoomed'));}
function boot(){renderContacts(); renderThumbs(); const params=new URLSearchParams(location.search); const requested=params.get('id'); const saved=localStorage.getItem('lighttable-selected'); selected=allItems().find(i=>i.id===requested)||allItems().find(i=>i.id===saved)||DATA.contacts[3]||allItems()[0]; $$('.modes button').forEach(b=>b.onclick=()=>setMode(b.dataset.mode)); $$('.filters button').forEach(b=>b.onclick=()=>setFilter(b.dataset.filter)); $('.openDeck').onclick=()=>location.href='../index.html'; addEventListener('keydown',e=>{if(e.key==='1')setMode('light');if(e.key==='2')setMode('sequence');if(e.key==='3')setMode('map');if(e.key==='4')setMode('absence');}); initLoupe(); setMode(params.get('mode')||'light'); renderMeta();}
boot();
'''.replace('__DATA__', json.dumps(DATA))

html_doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Vaux LightTable — HermesPresentation</title><style>{css}</style></head><body><main class="app"><header class="top"><div class="brand"><span>HermesPresentation / LightTable</span><h1>Vaux 1906 as a machine for seeing</h1></div><nav class="modes"><button class="active" data-mode="light">1 Light</button><button data-mode="sequence">2 Sequence</button><button data-mode="map">3 Map guesses</button><button data-mode="absence">4 Absence</button><button class="ghostbtn openDeck" type="button">Deck</button></nav></header><aside class="left"><div class="leftIntro"><h2>Contact, frame, claim.</h2><p>This is a darkroom interface for the Vaux material. Click a sheet or frame; hover the large image for a loupe; switch modes to treat sequence, map uncertainty, and absence as evidence.</p></div><div class="filters"><button class="active" data-filter="all">all</button><button data-filter="contact">contacts</button><button data-filter="yoho">yoho</button><button data-filter="wapta">wapta</button><button data-filter="glacier">glacier</button><button data-filter="camp">camp</button><button data-filter="ice arch">ice arch</button><button data-filter="absence">absence</button></div><div class="thumbs"></div></aside><section class="stage"><div class="viewer"><img alt=""><svg class="mapCanvas" viewBox="0 0 1200 720"></svg><div class="sequenceGrid"></div><div class="loupe"></div></div><div class="overTitle"><div class="kicker"></div><h2></h2></div><div class="hint">hover for loupe · click to zoom · keys 1/2/3/4 switch modes</div></section><aside class="right"><div class="meta"></div><div class="sourceBox"></div><div class="notes"></div></aside><section class="strip"></section></main><script>{js}</script></body></html>'''
(OUT/'index.html').write_text(html_doc)
(OUT/'run.sh').write_text('#!/usr/bin/env bash\nset -euo pipefail\ncd "$(dirname "$0")"\npython3 -m http.server 8766\n')
(OUT/'README.md').write_text('''# Vaux LightTable\n\nA local darkroom/explorer for the Vaux 1906 material.\n\nRun standalone:\n\n```bash\ncd /mnt/c/Users/chris/BASECAMP/presentation/HermesPresentation/LightTable\n./run.sh\n```\n\nOpen http://127.0.0.1:8766/index.html\n\nIf the parent HermesPresentation server is already running on port 8765, open:\n\nhttp://127.0.0.1:8765/LightTable/index.html\n\nModes: `1` Light, `2` Sequence, `3` Map guesses, `4` Absence. Hover the main image for the loupe; click to zoom.\n''')
print('OUT', OUT)
print('contacts', len(contacts), 'images', len(images), 'assets', len(list(ASSETS.glob('*.jpg'))))
