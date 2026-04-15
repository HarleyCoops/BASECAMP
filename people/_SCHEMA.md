# BASECAMP People — Folder Contract

Each at-camp person gets:

```
people/<person_id>/
  profile.md              # intelligence profile (human readable)
  fonds.json              # structured fonds + findings
  artifacts/              # any downloaded digital assets
    <slugified-filename>  # photos, PDFs, scans, notes
    _manifest.json        # what we downloaded, from where, size, caption, permalink, date
```

## fonds.json schema
{
  "person_id": "",
  "display_name": "",
  "researched_on": "YYYY-MM-DD",
  "fonds": [
    {
      "institution": "Whyte Museum of the Canadian Rockies",
      "fonds_id": "M106/V771",
      "fonds_title": "Arthur Oliver Wheeler fonds",
      "url": "https://...",
      "scope": "correspondence, diaries, field notebooks, photographs",
      "relevance_to_1906_yoho": "high|medium|low|unknown",
      "has_digital_access": true,
      "searched_camp_materials": true,
      "findings": "what was found relevant to the 1906 Yoho camp",
      "notes": ""
    }
  ],
  "digital_assets_downloaded": [
    { "filename": "", "source_url": "", "permalink": "", "caption": "", "date": "", "license": "" }
  ],
  "leads_pending_manual_access": [
    { "institution": "", "reason": "", "contact": "" }
  ]
}

## profile.md structure
# <Display Name>
Role at 1906 Yoho camp: ...
Bio hook: ...

## Fonds & Archives Located
- Institution — Fonds ID — URL — Relevance

## 1906 Yoho Camp Artifacts Found
- (downloaded assets, with captions and source)

## Leads that need human hands
- (archives without online access, or restricted material)

## Search log
- date, query, result
