# Mountain Legacy Project - Wheeler Photo-Topographic Plates Archive

**Project:** BASECAMP 1906 Alpine Club of Canada Camp Reconstruction  
**Harvesting Date:** April 10, 2026  
**Target:** Arthur Oliver Wheeler's Dominion Land Survey photo-topographic plates, Yoho/Field area, 1904-1910

---

## Contents

### `mlp_search_findings.json`
Structured JSON document containing:
- All sources investigated (with URLs and access status)
- 13 MLP research projects identified
- Access challenges and limitations
- Contact information for MLP Director
- Specific data requests and alternative approaches
- Recommendations for direct institutional contact

**Format:** JSON (machine-readable)  
**Best for:** Technical documentation, API access planning, data requestor reference

### `SEARCH_REPORT.txt`
Comprehensive narrative search report detailing:
- Objective and search scope
- Complete inventory of 6 archive sources investigated
- Key findings and access restrictions
- Next steps prioritized by feasibility
- Technical notes on API attempts
- Conclusion and recommendations

**Format:** Plain text  
**Best for:** Overview, institutional correspondence, project documentation

### `CONTACT_MLP_REQUEST.md`
Email template for requesting data from Mountain Legacy Project Director
- Pre-formatted request with specific data fields needed
- Geographic scope and station list
- Use case documentation
- Alternative access paths
- Technical specifications and delivery preferences

**Format:** Markdown (copy-paste ready)  
**Best for:** Institutional outreach, data request initiation

---

## Search Status

**Plates Downloaded:** 0  
**Total Data Size:** 0 MB  
**Access Achieved:** Limited (web interfaces only, no bulk download)

### Why No Downloads?

The Mountain Legacy Project holds digitized Wheeler plates, but:

1. **MLP Explorer** (primary search tool) is offline
2. **No public API** for bulk metadata or image export
3. **DSpace institutional repository** blocks automated access
4. **LAC collection search** is HTML-based only
5. **No batch export** available for plate records

**Key Blocker:** The primary digital image repository (explorer.mountainlegacy.ca) is not accessible. Individual plates can be viewed through manual web browsing, but systematic data harvesting requires direct institutional contact.

---

## Stations Targeted (1906 ACC Camp Area)

The following surveyed stations from Wheeler's work would be relevant for BASECAMP:

- **Yoho Pass** - Camp base location, primary survey station
- **Emerald Lake** - Access route, glacial documentation
- **Summit Lake** - Wapta Icefield access point
- **Wapta Icefield** - Glacier baseline measurement (critical for climate research)
- **Burgess Pass** - Secondary survey location
- **Mount Stephen** - Peak triangulation point
- **Takakkaw Falls** - Landscape and geological reference

---

## Next Steps for BASECAMP

### Immediate Action Required
**Contact:** Eric Higgs, MLP Director  
**Email:** ehiggs@uvic.ca  
**Phone:** +1-250-721-8228  

Use `CONTACT_MLP_REQUEST.md` as template. Request:
1. Metadata CSV/JSON for Wheeler Yoho/Field plates (1904-1910)
2. Station numbers, dates, coordinates for each plate
3. Direct image URLs to LAC digitized collection
4. Associated repeat photographs from MLP field campaigns

### Alternative/Supplementary Approaches

1. **Manual LAC Search**
   - Go to: https://recherche-collection-search.bac-lac.gc.ca/
   - Query: "Arthur Wheeler" + location terms + date range
   - Download plates individually as found

2. **Alpine Club of Canada Archives**
   - Contact through Whyte Museum partnership
   - Seek original 1906 camp documentation
   - Cross-reference with Wheeler station data

3. **Supplementary Collections**
   - Whyte Museum of the Canadian Rockies (M-series photography)
   - Canadian Geological Survey historical records
   - Canadian Alpine Journal 1906-1907 volumes

---

## Archive Infrastructure Notes

### Sources Accessible
- **MLP Main Site** ✓ (mountainlegacy.ca) - WordPress CMS with REST API
- **MLP Image Analysis Toolkit** ✓ (viewer-only, no bulk download)
- **LAC Collection Search** ✓ (HTML interface, manual navigation only)
- **UVic DSpace** ✓ (institutional repository, automated access blocked)

### Sources Offline/Unreachable
- **MLP Explorer** ✗ (explorer.mountainlegacy.ca) - Connection refused
- **Borealis Data Repository** ✗ (borealis.ca) - Network unreachable

### API Attempts
- WordPress REST API: ✓ Successful (harvested project list)
- DSpace REST API: ✗ Blocked
- DSpace OAI-PMH: ✗ Not functional
- LAC SRU/OAI-PMH: ✗ Not responding
- Borealis CKAN: ✗ Network error

---

## Metadata Schema Expected

When data is received from MLP or LAC, expect fields such as:

```
{
  "station_number": "XX-YZ",
  "date": "1906-07-15",
  "location": "Yoho Pass, BC",
  "latitude": "53.1234",
  "longitude": "-116.5678",
  "map_reference": "NTS 82N/04",
  "surveyor": "Arthur Oliver Wheeler",
  "survey_type": "phototopographic",
  "image_url": "https://...",
  "image_format": "TIFF",
  "image_resolution": "4000x5000px",
  "repeat_photo_available": true,
  "repeat_photo_date": "2015-09-22",
  "repeat_photo_url": "https://..."
}
```

---

## Contact Information

**Mountain Legacy Project**
- Director: Eric Higgs, PhD
- Email: ehiggs@uvic.ca
- Phone: +1-250-721-8228
- Institution: Environmental Studies, University of Victoria
- Website: https://mountainlegacy.ca/

**BASECAMP Project Researcher**
- Purpose: 1906 Alpine Club of Canada camp reconstruction
- Geographic Focus: Yoho Pass area, BC
- Comparative Analysis: Historical glacier documentation (1906) vs. contemporary (2024)

---

## References

1. Mountain Legacy Project. "Capturing change in Canada's mountains." https://mountainlegacy.ca/
2. Library and Archives Canada. Collection Search. https://recherche-collection-search.bac-lac.gc.ca/
3. University of Victoria. DSpace Institutional Repository. https://dspace.library.uvic.ca/
4. Alpine Club of Canada. (2025). ACC-MLP Citizen Science Repeat Photography Project. https://alpineclubofcanada.ca/

---

**Last Updated:** April 10, 2026  
**Status:** Initial harvest incomplete; direct institutional contact required for data access  
**Next Review:** After MLP director response (estimated 2-4 weeks)
