#!/usr/bin/env python3
"""BASECAMP Whyte Museum harvester - per-person targeted download.

For each person: run targeted searches, extract permalinks, fetch
metadata + image/pdf URL from each permalink page, download to
BASECAMP/people/<id>/artifacts/, write _manifest.json.

Source restriction: Whyte Museum only. Full-res via dropping ?watermark=wmk.
"""
import requests, re, json, os, time, sys
from pathlib import Path
from bs4 import BeautifulSoup

BASE = "https://archives.whyte.org"
UA = {"User-Agent":"BASECAMP-research/1.0 (1906 ACC camp reconstruction)"}
BASECAMP_ROOT = Path(__file__).resolve().parent.parent

def search_ids(query):
    url = f"{BASE}/en/list?q={query.replace(' ','+')}"
    try:
        r = requests.get(url, timeout=30, headers=UA)
        return set(re.findall(r'/permalink/(descriptions\d+)', r.text))
    except Exception as e:
        print(f"  search fail {query}: {e}", file=sys.stderr)
        return set()

def fetch_meta(pid):
    url = f"{BASE}/en/permalink/{pid}"
    try:
        r = requests.get(url, timeout=30, headers=UA)
        if r.status_code != 200: return None
    except Exception: return None
    soup = BeautifulSoup(r.text, "html.parser")
    og_t = soup.find("meta", property="og:title")
    og_d = soup.find("meta", property="og:description")
    og_i = soup.find("meta", property="og:image")
    title = (og_t["content"] if og_t else (soup.title.string if soup.title else pid)) or pid
    desc  = (og_d["content"] if og_d else "") or ""
    imgurl = og_i["content"] if og_i else None
    if not imgurl:
        for img in soup.find_all("img"):
            src = img.get("src","")
            if "/media/archives/" in src:
                imgurl = src
                break
    if imgurl:
        imgurl = imgurl.split("?")[0]
        if not imgurl.startswith("http"): imgurl = BASE + imgurl
    return {"pid": pid, "permalink": url, "title": title.strip(), "description": desc[:600], "asset_url": imgurl}

def download(url, dest):
    try:
        r = requests.get(url, timeout=120, stream=True, headers=UA)
        if r.status_code != 200: return 0
        with open(dest,"wb") as f:
            for c in r.iter_content(8192): f.write(c)
        return dest.stat().st_size
    except Exception:
        return 0

def harvest_person(person_id, queries, max_items=60):
    out = BASECAMP_ROOT/"people"/person_id/"artifacts"
    out.mkdir(parents=True, exist_ok=True)
    print(f"\n### {person_id}")
    all_pids = set()
    for q in queries:
        got = search_ids(q)
        new = got - all_pids
        all_pids.update(got)
        print(f"  [{q}] +{len(new)}  total={len(all_pids)}")
        time.sleep(0.3)
    if len(all_pids) > max_items:
        all_pids = set(list(all_pids)[:max_items])
    manifest = []
    dl_count = 0
    dl_bytes = 0
    for i, pid in enumerate(sorted(all_pids), 1):
        meta = fetch_meta(pid)
        if not meta:
            print(f"  [{i}] {pid} fetch-fail")
            continue
        if meta["asset_url"]:
            fname = re.sub(r'[^a-zA-Z0-9._-]','_', meta["asset_url"].split("/")[-1])[:100]
            dest = out / f"{pid}_{fname}"
            if dest.exists():
                manifest.append({**meta, "downloaded": True, "file": dest.name, "bytes": dest.stat().st_size, "skipped": True})
                continue
            sz = download(meta["asset_url"], dest)
            if sz > 0:
                dl_count += 1
                dl_bytes += sz
                print(f"  [{i}] {pid} DL {sz//1024}KB  {meta['title'][:55]}")
                manifest.append({**meta, "downloaded": True, "file": dest.name, "bytes": sz})
            else:
                manifest.append({**meta, "downloaded": False})
        else:
            manifest.append({**meta, "downloaded": False, "no_asset": True})
        time.sleep(0.3)
    print(f"  >> {dl_count} files, {dl_bytes/1024/1024:.1f} MB")
    with open(out/"_manifest.json","w") as f:
        json.dump({"person": person_id, "source":"Whyte Museum","queries": queries,
                   "downloaded": dl_count, "total_bytes": dl_bytes, "items": manifest},
                  f, indent=2)

PLANS = {
    "mary-vaux": ["mary+vaux+walcott","mary+vaux+emerald","vaux+walcott+yoho","mary+vaux+1906","mary+vaux+glacier"],
    "george-vaux": ["george+vaux+emerald","george+vaux+yoho","vaux+1906","vaux+glacier+1906","vaux+illecillewaet","v653+yoho"],
    "william-s-vaux": ["william+vaux+emerald","william+vaux+yoho","w.s.+vaux","vaux+brothers+glacier"],
    "byron-harmon": ["harmon+1906","harmon+yoho+camp","harmon+alpine+club","harmon+emerald+1906","harmon+vice+president","v263+1906","v263+yoho"],
    "edouard-feuz": ["edouard+feuz","feuz+yoho","feuz+1906","feuz+vice+president","m93+feuz","v200+feuz","edward+feuz"],
    "gottfried-feuz": ["gottfried+feuz","feuz+brothers","gottfried+1906","feuz+guide+1906"],
    "george-kinney": ["kinney+1906","kinney+yoho","kinney+stephen","kinney+alpine","rev+kinney","g.r.b.+kinney","kinney+robson"],
    "julia-henshaw": ["henshaw+1906","henshaw+yoho","julia+henshaw","henshaw+wildflower","henshaw+emerald"],
    "frank-yeigh": ["yeigh+1906","yeigh+yoho","frank+yeigh","yeigh+alpine+club","yeigh+emerald"],
    "elizabeth-parker": ["elizabeth+parker","parker+alpine+club","parker+1906+alpine","parker+yoho","parker+winnipeg"],
    "morrison-bridgland": ["bridgland","m.p.+bridgland","bridgland+1906","bridgland+yoho","bridgland+survey","bridgland+photo"],
    "ralph-connor": ["ralph+connor","charles+gordon+1906","connor+cascade","c.w.+gordon","gordon+yoho","connor+alpine"],
    "fw-freeborn": ["freeborn+1906","freeborn+alpine","f.w.+freeborn","freeborn+yoho","freeborn+photograph"],
    "eo-wheeler": ["edward+wheeler+1906","e.o.+wheeler","wheeler+son+1906","e+o+wheeler"],
    "hg-wheeler": ["clara+wheeler","h.g.+wheeler","hector+wheeler","mrs.+wheeler"],
    "otto-brothers": ["otto+brothers","otto+banff","otto+outfitter","otto+1906"],
    "re-campbell-outfitter": ["r.e.+campbell","campbell+outfitter+1906","campbell+banff"],
    "sh-baker": ["s.h.+baker","baker+1906+alpine"],
    "ec-barnes": ["e.c.+barnes","barnes+alpine+1906"],
    "jd-patterson": ["j.d.+patterson","patterson+1906+alpine","patterson+ball"],
    "jc-herdman": ["herdman+1906","j.c.+herdman","herdman+alpine"],
    "am-gordon": ["a.m.+gordon","gordon+cascade+1906"],
    "alex-dunn": ["alex+dunn+alpine","dunn+1906+climb"],
    "ao-macrae": ["a.o.+macrae","macrae+alpine+1906"],
    "pd-mctavish": ["mctavish+1906","p.d.+mctavish","mctavish+crows+nest"],
    "jh-miller": ["j.h.+miller+alpine","miller+1906+yoho"],
    "jean-parker": ["jean+parker","parker+jean+1906"],
    "edna-sutherland": ["edna+sutherland","sutherland+1906"],
    "k-mclennan": ["k.+mclennan","mclennan+1906+alpine"],
    "eb-hobbs": ["e.b.+hobbs","hobbs+1906+alpine"],
    "d-warner": ["d.+warner+1906","warner+alpine+photo"],
    "jim-bong": ["jim+bong","bong+cook+1906"],
}

if __name__ == "__main__":
    targets = sys.argv[1:] if len(sys.argv) > 1 else list(PLANS.keys())
    for p in targets:
        if p not in PLANS: print(f"unknown {p}"); continue
        harvest_person(p, PLANS[p])
    print("\ndone")
