"""
BASECAMP Intelligence Builder
Generates people.json, places.json, camps.json from article extraction.
All data extracted from CAJ Vol.1 No.1 (1907) articles about the 1906 Yoho Camp.
"""
import json
from pathlib import Path
from datetime import date

OUT = Path(__file__).resolve().parent.parent / "intelligence"
OUT.mkdir(parents=True, exist_ok=True)

TODAY = date.today().isoformat()

# ============================================================
# PEOPLE
# ============================================================
people = [
    # --- CAMP ORGANIZERS & LEADERS ---
    {
        "person_id": "arthur-wheeler",
        "display_name": "Arthur O. Wheeler",
        "formal_name": "Arthur Oliver Wheeler, F.R.G.S.",
        "roles": ["author", "president", "organizer", "scientist"],
        "titles": ["F.R.G.S.", "President, Alpine Club of Canada"],
        "affiliations": ["Alpine Club of Canada", "Topographical Survey of Canada"],
        "biographical_detail": "President of the ACC, organized the first camp. Surveyor by profession. Led scientific observations of Yoho Glacier. Chairman of Camp Committee.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-18",
        "articles_authored": [
            {"slug": "canadian-rockies-field-wheeler", "title": "The Canadian Rockies, a Field for an Alpine Club", "mentions_emerald_lake": True, "emerald_lake_content": "Lists Emerald Lake among turquoise-green lakes of the Main range, describes its setting amid forests and peaks."},
            {"slug": "yoho-glacier-wheeler", "title": "Observations of the Yoho Glacier", "mentions_emerald_lake": False, "emerald_lake_content": ""},
            {"slug": "glossary-wheeler", "title": "Glossary of Mountaineering Terms", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["first-camp-yeigh", "yoho-camp-report", "chief-mountaineer-report", "alpine-club-parker"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": "arthur-oliver-wheeler",
        "fonds_leads": ["LAC survey records", "Whyte Museum Wheeler papers", "ACC Archives"]
    },
    {
        "person_id": "frank-yeigh",
        "display_name": "Frank Yeigh",
        "formal_name": "Frank Yeigh",
        "roles": ["author"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Writer and publicist. Authored the richest narrative account of the 1906 camp. His article is the primary source for camp life details.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-16",
        "articles_authored": [
            {"slug": "first-camp-yeigh", "title": "Canada's First Alpine Club Camp", "mentions_emerald_lake": True, "emerald_lake_content": "Describes arrival at Emerald Lake Chalet, crossing the glacial delta on northern shore, ascending cliff wall. Notes transcendent beauty of lake at base of Mt. Burgess. Describes Emerald glacier trip, camp fire scene."}
        ],
        "articles_mentioned_in": [],
        "photos_credited": ["AROUND THE CAMP FIRE"],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": ["Archives of Ontario — Frank Yeigh papers?", "Toronto Reference Library"]
    },
    {
        "person_id": "elizabeth-parker",
        "display_name": "Elizabeth Parker",
        "formal_name": "Elizabeth Parker",
        "roles": ["author", "secretary"],
        "titles": ["Secretary, Alpine Club of Canada"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Secretary of the ACC. Key founding figure. Address: 160 Furby Street, Winnipeg, Man. Wrote philosophical manifesto for the club.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-16",
        "articles_authored": [
            {"slug": "alpine-club-parker", "title": "The Alpine Club of Canada", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["yoho-camp-report"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": ["ACC founding documents", "Whyte Museum ACC records"]
    },
    {
        "person_id": "mary-vaux",
        "display_name": "Mary M. Vaux",
        "formal_name": "Mary M. Vaux",
        "roles": ["author", "scientist", "photographer"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada", "Academy of Natural Sciences of Philadelphia"],
        "biographical_detail": "Photographer and glacier researcher. Part of the Vaux family of Philadelphia scientists. Authored guide to camping in the Rockies with detailed equipment lists.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [
            {"slug": "camping-rockies-vaux", "title": "Camping in the Canadian Rockies", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["yoho-glacier-wheeler"],
        "photos_credited": ["MOUNT BIDDLE AND LAKE McARTHUR", "MOUNT STEPHEN FROM THE NATURAL BRIDGE"],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": ["Whyte Museum S5/V18", "Smithsonian Institution", "Academy of Natural Sciences of Philadelphia"]
    },
    {
        "person_id": "george-vaux",
        "display_name": "George Vaux, Jr.",
        "formal_name": "George Vaux, Jr.",
        "roles": ["author", "scientist"],
        "titles": [],
        "affiliations": ["Academy of Natural Sciences of Philadelphia"],
        "biographical_detail": "Co-authored glacier observations with brother William S. Vaux. Began systematic glacier measurements in 1894. Present at Yoho Glacier observation on July 14-15, 1906.",
        "at_camp": True,
        "camp_dates": "1906-07-14/1906-07-15",
        "articles_authored": [
            {"slug": "glacier-observations-vaux", "title": "Glacier Observations", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["yoho-glacier-wheeler"],
        "photos_credited": ["TEST PICTURE OF THE ILLECILLEWAET GLACIER FOR THE YEAR 1905"],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": ["Academy of Natural Sciences of Philadelphia proceedings", "Appalachia journal articles"]
    },
    {
        "person_id": "william-s-vaux",
        "display_name": "William S. Vaux",
        "formal_name": "William S. Vaux",
        "roles": ["author", "scientist"],
        "titles": [],
        "affiliations": ["Academy of Natural Sciences of Philadelphia"],
        "biographical_detail": "Co-authored glacier observations with brother George. Pioneered metal plate method for measuring glacier flow on the Illecillewaet.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [
            {"slug": "glacier-observations-vaux", "title": "Glacier Observations", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["yoho-glacier-wheeler"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": ["Academy of Natural Sciences of Philadelphia"]
    },
    {
        "person_id": "ralph-connor",
        "display_name": "Rev. C.W. Gordon (Ralph Connor)",
        "formal_name": "Reverend Charles William Gordon",
        "roles": ["author", "climber"],
        "titles": ["Reverend"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Presbyterian minister and bestselling novelist writing as 'Ralph Connor'. Describes himself as 'the Missionary' in his Cascade article. Climbed Cascade Mountain in September 1891 — before the ACC existed.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [
            {"slug": "climbed-cascade-gordon", "title": "How We Climbed Cascade", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": [],
        "photos_credited": [],
        "climbs": [{"mountain": "Cascade Mountain", "date": "1891-09", "role": "climber"}],
        "ell_silo_id": None,
        "fonds_leads": ["University of Manitoba Archives — Ralph Connor papers"]
    },
    {
        "person_id": "george-kinney",
        "display_name": "Rev. G.R.B. Kinney",
        "formal_name": "Reverend George R.B. Kinney",
        "roles": ["author", "climber", "photographer", "active_member"],
        "titles": ["Reverend"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Camp photographer. Made solo ascent of Mt. Stephen in October 1904 — described as remarkable. Assisted on multiple official climbs of Vice-President. Later famous for 1909 Mt. Robson attempt.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-16",
        "articles_authored": [
            {"slug": "mt-stephen-kinney", "title": "Mt. Stephen", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": ["MOUNT BURGESS AND EMERALD LAKE", "THE UPPER SNOWFIELD—MOUNT VICE-PRESIDENT"],
        "climbs": [
            {"mountain": "Mt. Stephen", "date": "1904-10-21", "role": "solo climber"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-10", "role": "assistant"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-13", "role": "assistant"}
        ],
        "ell_silo_id": None,
        "fonds_leads": ["Whyte Museum", "ACC Archives — camp photographs"]
    },
    {
        "person_id": "julia-henshaw",
        "display_name": "Julia W. Henshaw",
        "formal_name": "Julia W. Henshaw",
        "roles": ["author", "scientist"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Botanist and author. Detailed the wildflowers of the Rockies and Selkirks. Notes Yellow Lady's Slipper (Cypripedium pubescens) growing on moraine from Emerald Lake to Yoho Valley in July.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [
            {"slug": "wildflowers-henshaw", "title": "The Mountain Wildflowers of Western Canada", "mentions_emerald_lake": True, "emerald_lake_content": "Describes Yellow Lady's Slipper orchids growing in thick clumps on a long moraine stretching from Emerald Lake to the foot of the Yoho Valley, blooming in July."}
        ],
        "articles_mentioned_in": [],
        "photos_credited": ["YELLOW ADDER'S TONGUE photo"],
        "climbs": [],
        "ell_silo_id": "julia-henshaw",
        "fonds_leads": ["Vancouver Archives", "UBC Special Collections"]
    },
    # --- CHIEF MOUNTAINEER & GUIDES ---
    {
        "person_id": "morrison-bridgland",
        "display_name": "M.P. Bridgland",
        "formal_name": "Morrison P. Bridgland",
        "roles": ["chief_mountaineer", "organizer"],
        "titles": ["Chief Mountaineer"],
        "affiliations": ["Topographical Survey of the Rocky Mountains", "Alpine Club of Canada"],
        "biographical_detail": "Chief Mountaineer of the 1906 camp. Led or co-led all official climbs of the Vice-President. From Topographical Survey.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-16",
        "articles_authored": [
            {"slug": "chief-mountaineer-report", "title": "Report of Chief Mountaineer", "mentions_emerald_lake": True, "emerald_lake_content": "Describes Emerald glacier trips and Burgess trail views of Emerald Lake and President range."}
        ],
        "articles_mentioned_in": ["first-camp-yeigh"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-08", "role": "route scout"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-10", "role": "leader"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-11", "role": "leader"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-13", "role": "leader"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-14", "role": "leader"},
            {"mountain": "Mt. Wapta", "date": "1906-07-12", "role": "climber"}
        ],
        "ell_silo_id": None,
        "fonds_leads": ["LAC Topographical Survey records"]
    },
    {
        "person_id": "hg-wheeler",
        "display_name": "H.G. Wheeler",
        "formal_name": "H.G. Wheeler",
        "roles": ["organizer", "secretary", "climber"],
        "titles": ["Secretary, Yoho Camp Committee"],
        "affiliations": ["Topographical Survey of the Rocky Mountains", "Alpine Club of Canada"],
        "biographical_detail": "Secretary of Yoho Camp Committee, based in Banff. Son of A.O. Wheeler. Assisted Bridgland. Led July 12 climb and special Takakkaw Falls trip.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-16",
        "articles_authored": [],
        "articles_mentioned_in": ["chief-mountaineer-report", "yoho-camp-report"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-08", "role": "route scout"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-12", "role": "leader"}
        ],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "edouard-feuz",
        "display_name": "Edouard Feuz, Jr.",
        "formal_name": "Edouard Feuz, Jr.",
        "roles": ["guide"],
        "titles": ["Swiss Guide"],
        "affiliations": ["Canadian Pacific Railway"],
        "biographical_detail": "Swiss guide from Interlaken, loaned by CPR for the camp. Led numerous climbs including Burgess, Wapta, Vice-President, and first ascent of Marpole/Amgadamo.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-16",
        "articles_authored": [],
        "articles_mentioned_in": ["chief-mountaineer-report", "first-camp-yeigh"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-08", "role": "guide"},
            {"mountain": "Mt. Burgess", "date": "1906-07-10", "role": "guide"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-11", "role": "guide"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-12", "role": "guide"},
            {"mountain": "Mt. Wapta", "date": "1906-07-13", "role": "guide"},
            {"mountain": "Mt. Vice-President / Mt. President", "date": "1906-07-14", "role": "guide"},
            {"mountain": "Mt. Marpole / Mt. Amgadamo", "date": "1906-07-16", "role": "guide"}
        ],
        "ell_silo_id": None,
        "fonds_leads": ["Whyte Museum Swiss Guides collection"]
    },
    {
        "person_id": "gottfried-feuz",
        "display_name": "Gottfried Feuz",
        "formal_name": "Gottfried Feuz",
        "roles": ["guide"],
        "titles": ["Swiss Guide"],
        "affiliations": ["Canadian Pacific Railway"],
        "biographical_detail": "Swiss guide from Interlaken, loaned by CPR. Led climbs of Wapta, Collie. Accompanied Bridgland on Vice-President route scouting.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-16",
        "articles_authored": [],
        "articles_mentioned_in": ["chief-mountaineer-report", "first-camp-yeigh"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-08", "role": "guide"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-10", "role": "guide"},
            {"mountain": "Mt. Wapta", "date": "1906-07-11", "role": "guide"},
            {"mountain": "Mt. Collie", "date": "1906-07-12", "role": "guide"},
            {"mountain": "Mt. Wapta", "date": "1906-07-14", "role": "guide"},
            {"mountain": "Mt. Marpole / Mt. Amgadamo", "date": "1906-07-16", "role": "guide"}
        ],
        "ell_silo_id": "gottfried-feuz",
        "fonds_leads": ["Whyte Museum M93/V200"]
    },
    # --- OUTFITTERS ---
    {
        "person_id": "re-campbell-outfitter",
        "display_name": "R.E. Campbell",
        "formal_name": "R.E. Campbell",
        "roles": ["outfitter"],
        "titles": [],
        "affiliations": [],
        "biographical_detail": "Outfitter from Laggan and Field. Donated services, men, horses and outfits for the camp.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [],
        "articles_mentioned_in": ["first-camp-yeigh"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "otto-brothers",
        "display_name": "Martin and Jack Otto",
        "formal_name": "Martin and Otto (Otto Bros.)",
        "roles": ["outfitter"],
        "titles": [],
        "affiliations": [],
        "biographical_detail": "Outfitters from Field, Leanchoil and Golden. Donated services for the camp. Jack Otto told bear stories around the camp fire.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [],
        "articles_mentioned_in": ["first-camp-yeigh"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "ec-barnes",
        "display_name": "E.C. Barnes",
        "formal_name": "E.C. Barnes",
        "roles": ["outfitter", "active_member"],
        "titles": [],
        "affiliations": [],
        "biographical_detail": "Outfitter from Banff. Donated services for the camp. Assisted on July 14 Vice-President/President climb.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [],
        "articles_mentioned_in": ["first-camp-yeigh", "chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Vice-President / Mt. President", "date": "1906-07-14", "role": "assistant"}],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "sh-baker",
        "display_name": "S.H. Baker",
        "formal_name": "S.H. Baker",
        "roles": ["outfitter", "climber"],
        "titles": [],
        "affiliations": [],
        "biographical_detail": "Outfitter from Glacier. Donated services for the camp. Climbed Mt. Wapta July 13.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [],
        "articles_mentioned_in": ["first-camp-yeigh", "chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Wapta", "date": "1906-07-13", "role": "climber"}],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    # --- KEY CLIMBERS & ACTIVE MEMBERS ---
    {
        "person_id": "jc-herdman",
        "display_name": "Rev. J.C. Herdman, D.D.",
        "formal_name": "Reverend J.C. Herdman, D.D.",
        "roles": ["climber", "active_member", "author"],
        "titles": ["Reverend", "D.D."],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Presbyterian minister from Calgary. 'Born mountaineer' per Yeigh. Pioneered delta crossing. Led Emerald Glacier trips and Mt. Field ascent. Also authored Ascent of Mt. Macoun.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-16",
        "articles_authored": [
            {"slug": "ascent-macoun-herdman", "title": "The Ascent of Mt. Macoun", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["first-camp-yeigh", "chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-08", "role": "route scout"},
            {"mountain": "Mt. Field", "date": "1906-07-12", "role": "leader"},
            {"mountain": "Emerald Glacier", "date": "1906-07", "role": "trip leader (3 trips)"}
        ],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "jd-patterson",
        "display_name": "J.D. Patterson",
        "formal_name": "J.D. Patterson",
        "roles": ["climber", "active_member", "author"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "From Woodstock. Key climber. Ascended Mt. Collie with Gottfried Feuz on July 12, meeting Miss Tuzo on summit by different route.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [
            {"slug": "ascent-ball-patterson", "title": "The Ascent of Mt. Ball", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["first-camp-yeigh", "chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-10", "role": "assistant"},
            {"mountain": "Mt. Collie", "date": "1906-07-12", "role": "climber"}
        ],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "eo-wheeler",
        "display_name": "E.O. Wheeler",
        "formal_name": "E.O. Wheeler",
        "roles": ["climber", "active_member"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Son of A.O. Wheeler. Active climber at camp — Wapta (3 times), Vice-President assist.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [],
        "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-12", "role": "assistant"},
            {"mountain": "Mt. Wapta", "date": "1906-07-11", "role": "climber"},
            {"mountain": "Mt. Wapta", "date": "1906-07-13", "role": "climber"}
        ],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "pd-mctavish",
        "display_name": "P.D. McTavish",
        "formal_name": "P.D. McTavish",
        "roles": ["climber", "active_member", "author"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Experienced climber, assisted on multiple official ascents. Co-authored Crow's Nest Mountain article.",
        "at_camp": True,
        "camp_dates": "1906-07-08/1906-07-16",
        "articles_authored": [
            {"slug": "climb-crows-nest-mctavish", "title": "The Climb of Crow's Nest Mountain", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-08", "role": "route scout"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-10", "role": "assistant"},
            {"mountain": "Mt. Wapta", "date": "1906-07-12", "role": "climber"},
            {"mountain": "Mt. Vice-President", "date": "1906-07-13", "role": "assistant"},
            {"mountain": "Mt. Wapta", "date": "1906-07-14", "role": "climber"}
        ],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "am-gordon",
        "display_name": "Rev. A.M. Gordon",
        "formal_name": "Reverend A.M. Gordon",
        "roles": ["climber", "active_member", "author"],
        "titles": ["Reverend"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Co-authored Marpole/Amgadamo first ascent article.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [
            {"slug": "ascents-marpole-amgadamo", "title": "The Ascents of Mts. Marpole and Amgadamo", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-12", "role": "assistant"},
            {"mountain": "Mt. Wapta", "date": "1906-07-11", "role": "climber"},
            {"mountain": "Mt. Marpole / Mt. Amgadamo", "date": "1906-07-16", "role": "first ascent"}
        ],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "ao-macrae",
        "display_name": "Rev. A.O. MacRae",
        "formal_name": "Reverend A.O. MacRae",
        "roles": ["climber", "graduate", "author"],
        "titles": ["Reverend"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Graduated July 12. Co-authored Marpole/Amgadamo article.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [
            {"slug": "ascents-marpole-amgadamo", "title": "The Ascents of Mts. Marpole and Amgadamo", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-12", "role": "graduate"},
            {"mountain": "Mt. Wapta", "date": "1906-07-11", "role": "climber"},
            {"mountain": "Mt. Marpole / Mt. Amgadamo", "date": "1906-07-16", "role": "first ascent"}
        ],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "alex-dunn",
        "display_name": "Rev. Alex. Dunn",
        "formal_name": "Reverend Alexander Dunn",
        "roles": ["climber", "graduate", "author"],
        "titles": ["Reverend"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Graduated July 13. Co-authored Marpole/Amgadamo article. Also climbed Mt. Field.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [
            {"slug": "ascents-marpole-amgadamo", "title": "The Ascents of Mts. Marpole and Amgadamo", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-13", "role": "graduate"},
            {"mountain": "Mt. Field", "date": "1906-07-12", "role": "climber"},
            {"mountain": "Mt. Marpole / Mt. Amgadamo", "date": "1906-07-16", "role": "first ascent"}
        ],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "henrietta-tuzo",
        "display_name": "Henrietta L. Tuzo",
        "formal_name": "Miss Henrietta L. Tuzo",
        "roles": ["climber", "active_member"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "From Warlingham, England. Climbed Mt. Collie on July 12 by different route from Patterson, meeting on summit. Was NOT visiting the camp — climbed independently with guide Christian Kaufmann.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [],
        "articles_mentioned_in": ["first-camp-yeigh", "chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Collie", "date": "1906-07-12", "role": "climber (independent)"}],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "christian-kaufmann",
        "display_name": "Christian Kaufmann",
        "formal_name": "Christian Kaufmann",
        "roles": ["guide"],
        "titles": ["Swiss Guide"],
        "affiliations": [],
        "biographical_detail": "Swiss guide who accompanied Henrietta Tuzo on her independent ascent of Mt. Collie July 12.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [],
        "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Collie", "date": "1906-07-12", "role": "guide"}],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    # --- PHOTOGRAPHERS ---
    {
        "person_id": "byron-harmon",
        "display_name": "Byron Harmon",
        "formal_name": "Byron Harmon",
        "roles": ["photographer", "graduate"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Professional photographer from Banff. Graduated to active membership July 13. Multiple photos credited in the journal.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [],
        "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": [
            "CASCADE MOUNTAIN, BANFF, ALBERTA",
            "THE DINING PAVILION AT YOHO CAMP",
            "A PARTY OF GRADUATES AND GUIDES RETURNED FROM THE OFFICIAL CLIMB",
            "ROLL CALL FOR THE OFFICIAL CLIMB OF MT. VICE-PRESIDENT",
            "THE ICEFALL OF THE YOHO GLACIER"
        ],
        "climbs": [{"mountain": "Mt. Vice-President", "date": "1906-07-13", "role": "graduate"}],
        "ell_silo_id": "byron-harmon",
        "fonds_leads": ["Whyte Museum Byron Harmon Collection"]
    },
    {
        "person_id": "fw-freeborn",
        "display_name": "F.W. Freeborn",
        "formal_name": "F.W. Freeborn",
        "roles": ["photographer"],
        "titles": [],
        "affiliations": [],
        "biographical_detail": "Photographer at the camp. Credited for Vice-President and Residence Park photos.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [],
        "articles_mentioned_in": [],
        "photos_credited": ["MOUNT VICE-PRESIDENT—THE OFFICIAL CLIMB", "RESIDENCE PARK—YOHO CAMP"],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "d-warner",
        "display_name": "D. Warner",
        "formal_name": "D. Warner",
        "roles": ["photographer", "climber", "graduate"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Graduated July 12. Photographer credited for Twin Falls Creek crossing photo.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [],
        "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": ["CROSSING TWIN FALLS CREEK—YOHO VALLEY TRAIL"],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-12", "role": "graduate"},
            {"mountain": "Mt. Wapta", "date": "1906-07-11", "role": "climber"}
        ],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    # --- CAMP STAFF ---
    {
        "person_id": "jim-bong",
        "display_name": "Jim Bong (Ping-Pong)",
        "formal_name": "Jim Bong",
        "roles": ["cook", "employee"],
        "titles": [],
        "affiliations": ["Canadian Pacific Railway"],
        "biographical_detail": "Chinese cook from the CPR Yoho camps. Called 'Ping-Pong' by campers. Yeigh: 'May his fat shade never grow less.'",
        "at_camp": True,
        "camp_dates": "1906-07-09/1906-07-18",
        "articles_authored": [],
        "articles_mentioned_in": ["first-camp-yeigh"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    {
        "person_id": "edna-sutherland",
        "display_name": "Miss Edna Sutherland",
        "formal_name": "Miss Edna Sutherland",
        "roles": ["graduate"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "From Winnipeg. Graduated July 13. Singled out by Yeigh for wit and artistic talent at evening entertainments.",
        "at_camp": True,
        "camp_dates": "1906-07",
        "articles_authored": [],
        "articles_mentioned_in": ["first-camp-yeigh", "chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [{"mountain": "Mt. Vice-President", "date": "1906-07-13", "role": "graduate"}],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    # --- FIRST GRADUATES (July 10) ---
    {
        "person_id": "k-mclennan",
        "display_name": "Miss K. McLennan",
        "formal_name": "Miss K. McLennan",
        "roles": ["graduate"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "From Toronto. One of first two women to graduate at the camp (July 10). Singled out by Yeigh.",
        "at_camp": True, "camp_dates": "1906-07",
        "articles_authored": [], "articles_mentioned_in": ["first-camp-yeigh", "chief-mountaineer-report"],
        "photos_credited": [], "climbs": [{"mountain": "Mt. Vice-President", "date": "1906-07-10", "role": "graduate"}],
        "ell_silo_id": None, "fonds_leads": []
    },
    {
        "person_id": "eb-hobbs",
        "display_name": "Miss E.B. Hobbs",
        "formal_name": "Miss E.B. Hobbs",
        "roles": ["graduate"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "From Revelstoke. One of first two women to graduate at the camp (July 10).",
        "at_camp": True, "camp_dates": "1906-07",
        "articles_authored": [], "articles_mentioned_in": ["first-camp-yeigh", "chief-mountaineer-report"],
        "photos_credited": [], "climbs": [{"mountain": "Mt. Vice-President", "date": "1906-07-10", "role": "graduate"}],
        "ell_silo_id": None, "fonds_leads": []
    },
    # --- PATRON ---
    {
        "person_id": "sandford-fleming",
        "display_name": "Sir Sandford Fleming",
        "formal_name": "Sir Sandford Fleming, K.C.M.G.",
        "roles": ["patron", "honorary_member", "author"],
        "titles": ["K.C.M.G.", "Patron, Alpine Club of Canada"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Honorary President and Patron of the ACC. First called attention to the Rockies as a field for alpine work in his 1884 book 'England and Canada'. Engineer of the CPR.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [
            {"slug": "memories-fleming", "title": "Memories of the Mountains", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["canadian-rockies-field-wheeler", "alpine-club-parker"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": ["LAC Sir Sandford Fleming fonds"]
    },
    # --- CPR ---
    {
        "person_id": "william-whyte",
        "display_name": "William Whyte",
        "formal_name": "William Whyte",
        "roles": ["patron", "author"],
        "titles": ["Second Vice-President, Canadian Pacific Railway"],
        "affiliations": ["Canadian Pacific Railway", "Alpine Club of Canada"],
        "biographical_detail": "CPR Second Vice-President. Wrote Greetings for the journal. Mentioned by Parker as associate member who would deplore defacement of mountain beauty.",
        "at_camp": False,
        "camp_dates": "",
        "articles_authored": [
            {"slug": "greetings-whyte", "title": "Greetings", "mentions_emerald_lake": False, "emerald_lake_content": ""}
        ],
        "articles_mentioned_in": ["alpine-club-parker"],
        "photos_credited": [],
        "climbs": [],
        "ell_silo_id": None,
        "fonds_leads": []
    },
    # --- OTHER NOTABLE GRADUATES ---
    {
        "person_id": "jh-miller",
        "display_name": "Rev. J.H. Miller",
        "formal_name": "Reverend J.H. Miller",
        "roles": ["climber", "active_member"],
        "titles": ["Reverend"],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Experienced mountaineer, assisted on July 11 official climb.",
        "at_camp": True, "camp_dates": "1906-07",
        "articles_authored": [], "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": [], "climbs": [{"mountain": "Mt. Vice-President", "date": "1906-07-11", "role": "assistant"}],
        "ell_silo_id": None, "fonds_leads": []
    },
    {
        "person_id": "jean-parker",
        "display_name": "Miss Jean Parker",
        "formal_name": "Miss Jean Parker",
        "roles": ["graduate", "climber"],
        "titles": [],
        "affiliations": ["Alpine Club of Canada"],
        "biographical_detail": "Daughter of Elizabeth Parker? Graduated July 12. Also climbed Wapta July 13.",
        "at_camp": True, "camp_dates": "1906-07",
        "articles_authored": [], "articles_mentioned_in": ["chief-mountaineer-report"],
        "photos_credited": [],
        "climbs": [
            {"mountain": "Mt. Vice-President", "date": "1906-07-12", "role": "graduate"},
            {"mountain": "Mt. Wapta", "date": "1906-07-13", "role": "climber"}
        ],
        "ell_silo_id": None, "fonds_leads": []
    },
]

# ============================================================
# PLACES — with precision coordinates
# Coordinate sources:
#   - "modern_topo" = modern topographic maps / GIS
#   - "text_deduction" = deduced from article descriptions + modern trails
#   - "peakbagger" = PeakBagger.com summit database
# ============================================================
places = [
    # --- APPROACH: Field to Emerald Lake ---
    {
        "place_id": "field-station",
        "display_name": "Field Station (CPR)",
        "historical_names": ["Field"],
        "place_type": "station",
        "coordinates": {"lat": 51.3980, "lon": -116.4592},
        "elevation_ft": 4075,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Railway station where campers arrived evening of July 8th. 'That spacious hostelry' under the shadow of Mt. Stephen.",
        "mentioned_in_articles": ["first-camp-yeigh", "yoho-camp-report", "mt-stephen-kinney"],
        "route_connections": ["kicking-horse-bridge", "mt-stephen-house"],
        "modern_trail_note": "Modern Field townsite, Trans-Canada Highway."
    },
    {
        "place_id": "mt-stephen-house",
        "display_name": "Mt. Stephen House",
        "historical_names": ["Mt. Stephen House"],
        "place_type": "hotel",
        "coordinates": {"lat": 51.3978, "lon": -116.4600},
        "elevation_ft": 4075,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "approximate",
        "coordinate_source": "text_deduction",
        "description_from_text": "CPR tourist hotel at Field. Mt. Stephen now 'the stock climb from Mt. Stephen House'. Return route via Burgess Pass trail.",
        "mentioned_in_articles": ["mt-stephen-kinney", "first-camp-yeigh"],
        "route_connections": ["field-station", "burgess-pass-trail"],
        "modern_trail_note": "Site now within Field townsite. Hotel demolished 1918."
    },
    {
        "place_id": "kicking-horse-bridge",
        "display_name": "Bridge over the Kicking-Horse",
        "historical_names": [],
        "place_type": "bridge",
        "coordinates": {"lat": 51.3985, "lon": -116.4610},
        "elevation_ft": 4075,
        "elevation_source": "text_deduction",
        "coordinate_confidence": "approximate",
        "coordinate_source": "text_deduction",
        "description_from_text": "Yeigh: 'crossed the bridge over the Kicking-Horse and took to the road that leads through a silent forest aisle to Emerald lake.'",
        "mentioned_in_articles": ["first-camp-yeigh"],
        "route_connections": ["field-station", "emerald-lake-road"],
        "modern_trail_note": "Near modern bridge on Emerald Lake Road at Field."
    },
    {
        "place_id": "emerald-lake-road",
        "display_name": "Forest Road to Emerald Lake",
        "historical_names": ["seven-mile path through the trees"],
        "place_type": "road",
        "coordinates": {"lat": 51.4200, "lon": -116.5000},
        "elevation_ft": None,
        "elevation_source": "",
        "coordinate_confidence": "approximate",
        "coordinate_source": "text_deduction — midpoint of 7-mile road",
        "description_from_text": "Yeigh: 'That seven-mile path through the trees, with a snow-enshrined peak closing the view at either end.' Some walked, some rode carriages or commissariat wagons.",
        "mentioned_in_articles": ["first-camp-yeigh"],
        "route_connections": ["kicking-horse-bridge", "emerald-lake-chalet"],
        "modern_trail_note": "Modern Emerald Lake Road, 8.5 km paved."
    },
    {
        "place_id": "emerald-lake-chalet",
        "display_name": "Emerald Lake Chalet",
        "historical_names": ["Emerald Lake Chalet"],
        "place_type": "chalet",
        "coordinates": {"lat": 51.4430, "lon": -116.5330},
        "elevation_ft": 4300,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo — site of modern Emerald Lake Lodge",
        "description_from_text": "Yeigh: 'as they round up at the Emerald Lake Chalet... transcendent beauty of this mountain lake nestling so peacefully at the base of mighty Mt. Burgess.'",
        "mentioned_in_articles": ["first-camp-yeigh"],
        "route_connections": ["emerald-lake-road", "emerald-lake-north-delta"],
        "modern_trail_note": "Now Emerald Lake Lodge (CRMR). Same site."
    },
    {
        "place_id": "emerald-lake",
        "display_name": "Emerald Lake",
        "historical_names": [],
        "place_type": "lake",
        "coordinates": {"lat": 51.4430, "lon": -116.5300},
        "elevation_ft": 4300,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Wheeler: 'turquoise green, in... Emerald lakes'. Yeigh: 'mountain lake nestling so peacefully at the base of mighty Mt. Burgess'. Henshaw: moraine stretching from Emerald Lake to Yoho Valley had Yellow Lady's Slippers in July.",
        "mentioned_in_articles": ["first-camp-yeigh", "canadian-rockies-field-wheeler", "wildflowers-henshaw", "chief-mountaineer-report"],
        "route_connections": ["emerald-lake-chalet", "emerald-lake-north-delta", "burgess-pass-trail"],
        "modern_trail_note": "Emerald Lake, Yoho National Park."
    },
    {
        "place_id": "emerald-lake-north-delta",
        "display_name": "Northern Glacial Delta",
        "historical_names": ["broad glacial delta on its northern shore"],
        "place_type": "delta",
        "coordinates": {"lat": 51.4480, "lon": -116.5280},
        "elevation_ft": 4300,
        "elevation_source": "text_deduction",
        "coordinate_confidence": "approximate",
        "coordinate_source": "text_deduction — north end of Emerald Lake where alluvial fan enters",
        "description_from_text": "Yeigh: 'traverse of the broad glacial delta on its northern shore and the ascent of the steep cliff wall... passage of an endless number of streams flowing from the Emerald glacier, thousands of feet higher. Pioneering the first section of the party was the Rev. Dr. Herdman... log bridges had been swept away... pack ponies were requisitioned as bridges.'",
        "mentioned_in_articles": ["first-camp-yeigh"],
        "route_connections": ["emerald-lake-chalet", "yoho-pass-trail-climb"],
        "modern_trail_note": "Now alluvial fan at north end of Emerald Lake. Modern Yoho Pass trail crosses this area."
    },
    # --- CAMP AREA ---
    {
        "place_id": "yoho-pass",
        "display_name": "Yoho Pass",
        "historical_names": ["summit of Yoho pass"],
        "place_type": "pass",
        "coordinates": {"lat": 51.4575, "lon": -116.5190},
        "elevation_ft": 6000,
        "elevation_source": "article text — Yeigh: '6000 feet above the sea'",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Yeigh: 'At last, the summit of Yoho pass! At last, that striking picture of a tented town nestling amid the realm of trees!' Camp site at 6000 ft.",
        "mentioned_in_articles": ["first-camp-yeigh", "yoho-camp-report", "chief-mountaineer-report"],
        "route_connections": ["emerald-lake-north-delta", "yoho-lake", "camp-yoho"],
        "modern_trail_note": "Yoho Pass, elevation ~1815m. Modern trail from Emerald Lake to Yoho Valley."
    },
    {
        "place_id": "camp-yoho",
        "display_name": "Camp Yoho (1906)",
        "historical_names": ["Yoho Camp", "the Camp"],
        "place_type": "camp",
        "coordinates": {"lat": 51.4580, "lon": -116.5200},
        "elevation_ft": 6000,
        "elevation_source": "article text",
        "coordinate_confidence": "approximate",
        "coordinate_source": "text_deduction — at summit of Yoho Pass near Yoho Lake",
        "description_from_text": "Yeigh: 'tented town nestling amid the realm of trees... under a sky of blue, with grey old Wapta and Michael's mount standing sentinel, three thousand feet higher still.' Three sections: Residence Park, Official Square, horse paddock. Dining tent for 100. Bulletin board, central fire.",
        "mentioned_in_articles": ["first-camp-yeigh", "yoho-camp-report", "chief-mountaineer-report"],
        "route_connections": ["yoho-pass", "yoho-lake", "vice-president-trail", "emerald-glacier-trail", "upper-yoho-trail"],
        "modern_trail_note": "Near modern Yoho Pass junction. Exact camp clearing likely overgrown."
    },
    {
        "place_id": "yoho-lake",
        "display_name": "Yoho Lake",
        "historical_names": [],
        "place_type": "lake",
        "coordinates": {"lat": 51.4595, "lon": -116.5125},
        "elevation_ft": 5955,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Yeigh: 'the incomparable scene beside the incomparable Yoho lake, holding in its translucent waters all the emerald and amethyst shades in Nature's color box.' Wheeler: 'transparent emerald in Yoho lake.'",
        "mentioned_in_articles": ["first-camp-yeigh", "canadian-rockies-field-wheeler"],
        "route_connections": ["camp-yoho", "yoho-pass"],
        "modern_trail_note": "Yoho Lake, accessible from Yoho Pass trail."
    },
    # --- VICE-PRESIDENT CLIMB ROUTE ---
    {
        "place_id": "michael-peak",
        "display_name": "Michael Peak (Michael's Mount)",
        "historical_names": ["Michaels Mt.", "Michael's mount"],
        "place_type": "mountain",
        "coordinates": {"lat": 51.4540, "lon": -116.5030},
        "elevation_ft": 8750,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Yeigh: 'grey old Wapta and Michael's mount standing sentinel, three thousand feet higher still' above the 6000 ft camp. Chief Mountaineer: climbed en route to Vice-President. July 14 party did interesting rock climb up face to summit.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report"],
        "route_connections": ["camp-yoho", "vice-president-arete"],
        "modern_trail_note": "Michael Peak, 2667m."
    },
    {
        "place_id": "angle-peak",
        "display_name": "Angle Peak",
        "historical_names": ["Angle peak"],
        "place_type": "peak",
        "coordinates": {"lat": 51.4630, "lon": -116.5020},
        "elevation_ft": 9500,
        "elevation_source": "text_deduction",
        "coordinate_confidence": "estimated",
        "coordinate_source": "text_deduction — on arete between Michael Peak and Vice-President, about 1 mile east of VP summit",
        "description_from_text": "Chief Mountaineer: 'Angle peak, a sharp angle of rock rising above the north escarpment of the Vice-President ridge, about a mile east of the summit. Name first applied by Rev. James Outram.'",
        "mentioned_in_articles": ["chief-mountaineer-report"],
        "route_connections": ["michael-peak", "vice-president"],
        "modern_trail_note": "Feature on the VP ridge. Not officially named on modern maps."
    },
    {
        "place_id": "vice-president",
        "display_name": "The Vice-President",
        "historical_names": ["Mt. Vice-President"],
        "place_type": "mountain",
        "coordinates": {"lat": 51.4730, "lon": -116.5170},
        "elevation_ft": 10050,
        "elevation_source": "article text — 10,049 ft per Chief Mountaineer",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Official graduation climb. Yeigh: 'so called by Mr. Edward Whymper, of Matterhorn fame, in honor of the Vice-Presidency of the CPR.' 44 graduated, 15 ladies, no failures. Record time: 9.5 hrs. Average: 10.5 hrs.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report", "yoho-camp-report", "mt-stephen-kinney"],
        "route_connections": ["angle-peak", "president", "emerald-glacier"],
        "modern_trail_note": "The Vice President, 3066m, President Range."
    },
    {
        "place_id": "president",
        "display_name": "The President",
        "historical_names": ["Mt. President"],
        "place_type": "mountain",
        "coordinates": {"lat": 51.4790, "lon": -116.5180},
        "elevation_ft": 10287,
        "elevation_source": "Chief Mountaineer report — 10,287 ft",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Climbed July 14 by Feuz guides via snow col from Vice-President summit. ~200 ft descent to col, similar ascent. Cairn built. Hour round trip from VP.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report", "mt-stephen-kinney"],
        "route_connections": ["vice-president"],
        "modern_trail_note": "The President, 3138m, President Range."
    },
    {
        "place_id": "emerald-glacier",
        "display_name": "Emerald Glacier",
        "historical_names": [],
        "place_type": "glacier",
        "coordinates": {"lat": 51.4650, "lon": -116.5090},
        "elevation_ft": 8000,
        "elevation_source": "Yeigh text — 'elevation of 8000 feet'",
        "coordinate_confidence": "approximate",
        "coordinate_source": "modern_topo",
        "description_from_text": "Yeigh: 'Bordering the palisades of the Vice-President for a mile or more.' Visited in detachments. Snow line at ~8000 ft. Séracs, crevasses, green-blue walls. Three trips led by Herdman, 27 people total.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report"],
        "route_connections": ["camp-yoho", "vice-president"],
        "modern_trail_note": "Remnant of Emerald Glacier on NE face of President Range."
    },
    # --- MOUNTAINS CLIMBED FROM CAMP ---
    {
        "place_id": "mt-burgess",
        "display_name": "Mt. Burgess",
        "historical_names": [],
        "place_type": "mountain",
        "coordinates": {"lat": 51.4380, "lon": -116.5120},
        "elevation_ft": 8463,
        "elevation_source": "Chief Mountaineer report",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Yeigh: 'mighty Mt. Burgess' above Emerald Lake. Chief Mountaineer: 'one of the lowest, one of the most difficult climbs.' Climbed July 10 by party of 7 under Edouard Feuz.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report", "mt-stephen-kinney"],
        "route_connections": ["emerald-lake", "burgess-pass"],
        "modern_trail_note": "Mt. Burgess, 2599m. Burgess Shale fossil site on its shoulder."
    },
    {
        "place_id": "mt-field",
        "display_name": "Mt. Field",
        "historical_names": [],
        "place_type": "mountain",
        "coordinates": {"lat": 51.4190, "lon": -116.4910},
        "elevation_ft": 8645,
        "elevation_source": "Chief Mountaineer report",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Climbed July 12 under Herdman's guidance. Party of 6.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report", "mt-stephen-kinney"],
        "route_connections": ["camp-yoho"],
        "modern_trail_note": "Mt. Field, 2635m."
    },
    {
        "place_id": "mt-wapta",
        "display_name": "Mt. Wapta",
        "historical_names": [],
        "place_type": "mountain",
        "coordinates": {"lat": 51.4430, "lon": -116.4970},
        "elevation_ft": 9106,
        "elevation_source": "Chief Mountaineer report",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Yeigh: 'seemed to be the favorite, ascents having been made of it by four separate parties, by two different routes.' West face and southwestern arete routes. NE face 'difficult.'",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report", "mt-stephen-kinney"],
        "route_connections": ["camp-yoho", "burgess-pass"],
        "modern_trail_note": "Mt. Wapta, 2778m."
    },
    {
        "place_id": "mt-collie",
        "display_name": "Mt. Collie",
        "historical_names": [],
        "place_type": "mountain",
        "coordinates": {"lat": 51.5330, "lon": -116.4850},
        "elevation_ft": 10315,
        "elevation_source": "Chief Mountaineer report",
        "coordinate_confidence": "approximate",
        "coordinate_source": "modern_topo",
        "description_from_text": "Climbed July 12 by Patterson + Gottfried Feuz from Twin Falls camp. Met Miss Tuzo (independent climb with Kaufmann) on summit.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report", "yoho-glacier-wheeler"],
        "route_connections": ["twin-falls", "yoho-glacier"],
        "modern_trail_note": "Mt. Collie, 3143m."
    },
    {
        "place_id": "mt-marpole",
        "display_name": "Mt. Marpole",
        "historical_names": [],
        "place_type": "mountain",
        "coordinates": {"lat": 51.4350, "lon": -116.5500},
        "elevation_ft": 9822,
        "elevation_source": "Chief Mountaineer report",
        "coordinate_confidence": "approximate",
        "coordinate_source": "modern_topo",
        "description_from_text": "First ascent July 16 by Revs. MacRae, Gordon, Dunn with both Feuz guides.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report"],
        "route_connections": ["mt-amgadamo"],
        "modern_trail_note": "Mt. Marpole, 2994m."
    },
    {
        "place_id": "mt-amgadamo",
        "display_name": "Mt. Amgadamo",
        "historical_names": ["Amgadamo — unnamed peak christened at the 1906 camp"],
        "place_type": "mountain",
        "coordinates": {"lat": 51.4340, "lon": -116.5450},
        "elevation_ft": 9537,
        "elevation_source": "Chief Mountaineer report",
        "coordinate_confidence": "estimated",
        "coordinate_source": "text_deduction — peak between Marpole and McMullen",
        "description_from_text": "Yeigh: 'the peak lying between it and Mt. McMullen, both as far as known, virgin ascents. The unnamed peak was christened Amgadamo.' First ascent July 16.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report"],
        "route_connections": ["mt-marpole"],
        "modern_trail_note": "Mt. Amgadamo. Named at the 1906 camp."
    },
    # --- YOHO VALLEY ---
    {
        "place_id": "inspiration-point",
        "display_name": "Inspiration Point",
        "historical_names": [],
        "place_type": "viewpoint",
        "coordinates": {"lat": 51.4700, "lon": -116.5050},
        "elevation_ft": 6500,
        "elevation_source": "text_deduction",
        "coordinate_confidence": "approximate",
        "coordinate_source": "text_deduction — on corkscrew trail near camp",
        "description_from_text": "Chief Mountaineer: 'reached by a corkscrew trail branching from the Upper Yoho valley trail at a point near the camp. This point is well named, for the view from it not only takes one's breath away.' Dramatic view of Takakkaw Falls across valley.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report"],
        "route_connections": ["camp-yoho", "upper-yoho-trail"],
        "modern_trail_note": "Near modern Yoho Pass / Iceline trail junction area."
    },
    {
        "place_id": "takakkaw-falls",
        "display_name": "Takakkaw Falls",
        "historical_names": [],
        "place_type": "waterfall",
        "coordinates": {"lat": 51.4970, "lon": -116.4830},
        "elevation_ft": 4600,
        "elevation_source": "modern_topo (base)",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Yeigh: 'Canada's highest Niagara.' Chief Mountaineer: 'magnificent view of the full majesty of the Takakkaw falls, with its thousand feet of a sheer drop.' Special trip made by HG Wheeler, 19 people.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report"],
        "route_connections": ["lower-yoho-trail", "upper-yoho-trail"],
        "modern_trail_note": "Takakkaw Falls, 373m total drop. Yoho Valley Road."
    },
    {
        "place_id": "laughing-falls",
        "display_name": "Laughing Falls",
        "historical_names": [],
        "place_type": "waterfall",
        "coordinates": {"lat": 51.5050, "lon": -116.4790},
        "elevation_ft": 4800,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Yeigh: overnight camp near Laughing Falls on Yoho Valley trip. 'In the silent watches of the night... God's stars seemed to hover nearer.' Overnight camp for glacier observation committee July 14.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report", "yoho-glacier-wheeler"],
        "route_connections": ["takakkaw-falls", "twin-falls", "yoho-glacier"],
        "modern_trail_note": "Laughing Falls, Yoho Valley trail. Campground nearby."
    },
    {
        "place_id": "twin-falls",
        "display_name": "Twin Falls",
        "historical_names": [],
        "place_type": "waterfall",
        "coordinates": {"lat": 51.5140, "lon": -116.4730},
        "elevation_ft": 5400,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Yeigh: 'past the Laughing falls and the Twin falls, and many another no less beautiful.' Patterson camped at Twin Falls foot before Collie ascent.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report"],
        "route_connections": ["laughing-falls", "yoho-glacier"],
        "modern_trail_note": "Twin Falls, Yoho Valley. Twin Falls Chalet nearby."
    },
    {
        "place_id": "yoho-glacier",
        "display_name": "Yoho Glacier",
        "historical_names": [],
        "place_type": "glacier",
        "coordinates": {"lat": 51.5200, "lon": -116.4700},
        "elevation_ft": 6500,
        "elevation_source": "text_deduction — tongue elevation",
        "coordinate_confidence": "approximate",
        "coordinate_source": "modern_topo",
        "description_from_text": "Wheeler: 'largest outflow from the Wapta icefield, less than two miles long, remarkable purity.' Metal plates set July 14-15 to measure flow. Main stream issues from ice cave. Retreat of 76 ft since Vaux 1901 marks (15 ft/year average).",
        "mentioned_in_articles": ["first-camp-yeigh", "yoho-glacier-wheeler", "chief-mountaineer-report"],
        "route_connections": ["twin-falls", "wapta-icefield"],
        "modern_trail_note": "Yoho Glacier, significantly retreated since 1906."
    },
    {
        "place_id": "wapta-icefield",
        "display_name": "Wapta Icefield",
        "historical_names": ["Waputik Snowfield"],
        "place_type": "snowfield",
        "coordinates": {"lat": 51.5100, "lon": -116.4500},
        "elevation_ft": 9000,
        "elevation_source": "text_deduction",
        "coordinate_confidence": "approximate",
        "coordinate_source": "modern_topo",
        "description_from_text": "Wheeler: 'approximately twenty to twenty-five square miles, enclosed in a basin surrounded by Mts. Gordon, Olive, Thompson, Baker, Aysha peak, Mts. Collie, Habel and McArthur.' Feeds four watersheds — Bow, Mistaya, Blaeberry, Kicking-Horse.",
        "mentioned_in_articles": ["yoho-glacier-wheeler"],
        "route_connections": ["yoho-glacier"],
        "modern_trail_note": "Wapta Icefield, still significant but retreating."
    },
    # --- BURGESS PASS ROUTE ---
    {
        "place_id": "burgess-pass",
        "display_name": "Burgess Pass",
        "historical_names": ["Burgess pass trail"],
        "place_type": "pass",
        "coordinates": {"lat": 51.4300, "lon": -116.5050},
        "elevation_ft": 7000,
        "elevation_source": "text_deduction",
        "coordinate_confidence": "approximate",
        "coordinate_source": "modern_topo",
        "description_from_text": "Kinney: 'that most beautiful of passes, Burgess pass.' Chief Mountaineer: 'The Burgess trail seemed a favorite... from which the Presidents range and Emerald mountains with their glaciers, icefalls and torrents, are seen to greatest advantage; while below, Emerald lake nestles in a setting of deep green forest.' Return route to Mt. Stephen House.",
        "mentioned_in_articles": ["first-camp-yeigh", "chief-mountaineer-report", "mt-stephen-kinney"],
        "route_connections": ["camp-yoho", "mt-stephen-house", "emerald-lake"],
        "modern_trail_note": "Burgess Pass trail, Parks Canada. Access to Burgess Shale."
    },
    # --- LOOKOUT POINT ---
    {
        "place_id": "lookout-point",
        "display_name": "Lookout Point",
        "historical_names": [],
        "place_type": "viewpoint",
        "coordinates": {"lat": 51.4750, "lon": -116.5100},
        "elevation_ft": 5500,
        "elevation_source": "text_deduction",
        "coordinate_confidence": "estimated",
        "coordinate_source": "text_deduction — on Lower Yoho Valley trail",
        "description_from_text": "Chief Mountaineer: 'Lookout point on the Lower Yoho valley trail, presenting a magnificent view of the full majesty of the Takakkaw falls.'",
        "mentioned_in_articles": ["chief-mountaineer-report"],
        "route_connections": ["lower-yoho-trail", "takakkaw-falls"],
        "modern_trail_note": "On the Yoho Valley trail system."
    },
    # --- MT. STEPHEN ---
    {
        "place_id": "mt-stephen",
        "display_name": "Mt. Stephen",
        "historical_names": [],
        "place_type": "mountain",
        "coordinates": {"lat": 51.3830, "lon": -116.4370},
        "elevation_ft": 10495,
        "elevation_source": "Kinney text — 'ten thousand five hundred feet'",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Kinney: solo October 1904 ascent, left Field 8am, summit at ~4pm, returned 8pm. Fossil bed at 7000 ft. View of Field, Burgess, Wapta, Vice-President, Cathedral. 'The grim old King of the Rockies.'",
        "mentioned_in_articles": ["first-camp-yeigh", "mt-stephen-kinney", "canadian-rockies-field-wheeler"],
        "route_connections": ["field-station", "fossil-bed"],
        "modern_trail_note": "Mt. Stephen, 3199m. Stock climb from Field."
    },
    {
        "place_id": "fossil-bed",
        "display_name": "Fossil Bed (Mt. Stephen)",
        "historical_names": ["trilobite beds"],
        "place_type": "fossil_bed",
        "coordinates": {"lat": 51.3860, "lon": -116.4420},
        "elevation_ft": 7000,
        "elevation_source": "Wheeler text — 'altitude of 7000 feet'",
        "coordinate_confidence": "approximate",
        "coordinate_source": "modern_topo — Stephen Formation fossil locality",
        "description_from_text": "Kinney: 'opened Nature's book, and there, page after page, were trilobites of rarest form.' Wheeler: 'beds containing fossilized species, closely allied to the trilobite... at an altitude of 7000 feet, has become famous.'",
        "mentioned_in_articles": ["mt-stephen-kinney", "canadian-rockies-field-wheeler"],
        "route_connections": ["mt-stephen", "field-station"],
        "modern_trail_note": "Mt. Stephen trilobite beds. Protected fossil site."
    },
    # --- RALPH CONNOR'S CASCADE ---
    {
        "place_id": "cascade-mountain",
        "display_name": "Cascade Mountain",
        "historical_names": [],
        "place_type": "mountain",
        "coordinates": {"lat": 51.2020, "lon": -115.5450},
        "elevation_ft": 9836,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Gordon/Connor: 'sheer, rocky and bare, its great base thrust into the pine forest, its head into the clouds.' Climbed September 1891. Two men reached summit, three women turned back ~200 yards short. Fossil remains found near top.",
        "mentioned_in_articles": ["climbed-cascade-gordon"],
        "route_connections": ["banff", "forty-mile-creek"],
        "modern_trail_note": "Cascade Mountain, 2998m, Banff National Park."
    },
    {
        "place_id": "banff",
        "display_name": "Banff",
        "historical_names": ["capital of the Canadian National Park"],
        "place_type": "station",
        "coordinates": {"lat": 51.1784, "lon": -115.5708},
        "elevation_ft": 4537,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Gordon: 'capital of the Canadian National Park.' Henshaw: wildflowers within reach at Banff, Banff Hotel on cliff above confluence of Spray and Bow rivers.",
        "mentioned_in_articles": ["climbed-cascade-gordon", "wildflowers-henshaw"],
        "route_connections": ["cascade-mountain"],
        "modern_trail_note": "Town of Banff."
    },
    # --- VAUX CAMPING LOCATIONS ---
    {
        "place_id": "lake-ohara",
        "display_name": "Lake O'Hara",
        "historical_names": [],
        "place_type": "lake",
        "coordinates": {"lat": 51.3530, "lon": -116.3380},
        "elevation_ft": 6660,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Vaux: 'no place more delightful... a lovely clear sheet of water, filtered through the rock slide at its head. Banks carpeted with flowers.' Views of Biddle, Hungabee, Yukness, Lefroy, Victoria, Huber, Wiwaxy. 10 miles from Hector station.",
        "mentioned_in_articles": ["camping-rockies-vaux"],
        "route_connections": ["lake-mcarthur", "lake-oesa", "abbot-pass"],
        "modern_trail_note": "Lake O'Hara, Yoho NP. Bus access only."
    },
    {
        "place_id": "lake-mcarthur",
        "display_name": "Lake McArthur",
        "historical_names": ["McArthur lake"],
        "place_type": "lake",
        "coordinates": {"lat": 51.3380, "lon": -116.3350},
        "elevation_ft": 7400,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Vaux: 'a true alpine lake, with glaciers from the slopes of Mt. Biddle breaking off in miniature icebergs; grassy moss-grown slopes are a favorite feeding ground of the mountain goat.'",
        "mentioned_in_articles": ["camping-rockies-vaux", "canadian-rockies-field-wheeler"],
        "route_connections": ["lake-ohara"],
        "modern_trail_note": "Lake McArthur, largest lake in Lake O'Hara area."
    },
    {
        "place_id": "lake-oesa",
        "display_name": "Lake Oesa",
        "historical_names": [],
        "place_type": "lake",
        "coordinates": {"lat": 51.3430, "lon": -116.3250},
        "elevation_ft": 7500,
        "elevation_source": "modern_topo",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Vaux: 'whose surface is only melted for a very few weeks at midsummer.' Reached by following stream feeding Lake O'Hara through chain of lakes with cascades.",
        "mentioned_in_articles": ["camping-rockies-vaux"],
        "route_connections": ["lake-ohara", "abbot-pass"],
        "modern_trail_note": "Lake Oesa, 2275m."
    },
    {
        "place_id": "abbot-pass",
        "display_name": "Abbot Pass",
        "historical_names": ["Abbott pass"],
        "place_type": "pass",
        "coordinates": {"lat": 51.3190, "lon": -116.3640},
        "elevation_ft": 9000,
        "elevation_source": "Vaux text — '9000 feet above sea'",
        "coordinate_confidence": "exact",
        "coordinate_source": "modern_topo",
        "description_from_text": "Vaux: 'one can venture across Abbot pass (9000 feet above sea) and down the Victoria glacier to Lake Louise. But this is only safe with an experienced Swiss guide, as the pass is frequently traversed by avalanches on its northern side.'",
        "mentioned_in_articles": ["camping-rockies-vaux"],
        "route_connections": ["lake-oesa", "lake-louise"],
        "modern_trail_note": "Abbot Pass, 2925m. Abbot Pass Hut (National Historic Site)."
    },
]

# ============================================================
# CAMPS
# ============================================================
camps = [
    {
        "camp_id": "yoho-camp-1906",
        "name": "First Annual Camp of the Alpine Club of Canada — Yoho Camp",
        "place_id": "camp-yoho",
        "dates": {
            "open": "1906-07-09",
            "close": "1906-07-16",
            "pack_out_complete": "1906-07-18",
            "arrival_at_field": "1906-07-08"
        },
        "elevation_ft": 6000,
        "capacity": 100,
        "actual_attendance": 112,
        "layout": {
            "sections": ["Residence Park", "Official Square", "Horse Paddock"],
            "description": "Gay with banners, flags and bunting. Dining tent for 100. Central fire for evening gatherings. Bulletin board with daily programmes."
        },
        "logistics": {
            "distance_from_station_miles": 7,
            "transport": "Walking, carriages, commissariat wagons, pack ponies for supplies. 30-40 tents carried by pack ponies.",
            "provisions": "CPR cooks from Yoho camps placed at disposal. Provisions cost $613.12.",
            "cook": "Jim Bong ('Ping-Pong'), Chinese cook from CPR Yoho camps",
            "baggage_limit_lbs": 40
        },
        "funding": {
            "total_receipts": 1278.87,
            "total_expenditures": 1252.40,
            "balance": 26.47,
            "sources": [
                "Dominion Government: $500 (not in camp receipts — separate)",
                "Government of Alberta: $250",
                "Private subscriptions: $170",
                "Board and accommodation: $458.25",
                "Employee tips: $61",
                "Ice-axe auction: $75.75",
                "Surplus supplies sold: $263.87"
            ]
        },
        "graduation_stats": {
            "total_graduates": 42,
            "women_graduates": 15,
            "failures": 0,
            "official_mountain": "The Vice-President (10,049 ft)",
            "graduation_threshold_ft": 9000,
            "best_time_hrs": 9.5,
            "average_time_hrs": 10.5,
            "official_climb_dates": ["1906-07-10", "1906-07-11", "1906-07-12", "1906-07-13", "1906-07-14"]
        },
        "other_mountains_climbed": [
            {"mountain": "Mt. Burgess", "date": "1906-07-10", "elevation_ft": 8463},
            {"mountain": "Mt. Wapta", "date": "1906-07-11", "elevation_ft": 9106, "note": "4 ascents total, 2 routes"},
            {"mountain": "Mt. Collie", "date": "1906-07-12", "elevation_ft": 10315},
            {"mountain": "Mt. Field", "date": "1906-07-12", "elevation_ft": 8645},
            {"mountain": "Mt. President", "date": "1906-07-14", "elevation_ft": 10287},
            {"mountain": "Mt. Marpole", "date": "1906-07-16", "elevation_ft": 9822, "note": "first ascent"},
            {"mountain": "Mt. Amgadamo", "date": "1906-07-16", "elevation_ft": 9537, "note": "first ascent, named at camp"}
        ],
        "trips": [
            {"name": "Yoho Valley Round Trip", "duration_days": 2, "trips_made": 4, "participants_total": 60, "description": "Lower trail out, upper trail return. Overnight at Laughing Falls."},
            {"name": "Emerald Glacier Trip", "trips_made": 3, "participants_total": 27, "leader": "Rev. J.C. Herdman"},
            {"name": "Takakkaw Falls Trip", "trips_made": 1, "participants_total": 19, "leader": "H.G. Wheeler"},
            {"name": "Yoho Glacier Observation", "date": "1906-07-14/1906-07-15", "participants_total": 7, "description": "Scientific committee. Metal plates set for flow measurement. Retreat of 76 ft since 1901 measured."}
        ],
        "events": [
            {"date": "1906-07-08", "event": "Campers arrive at Field Station. Route-scouting party departs for Vice-President."},
            {"date": "1906-07-09", "event": "Camp opens. March from Field: bridge, 7-mile road, Emerald Lake Chalet, delta crossing, cliff ascent to Yoho Pass."},
            {"date": "1906-07-10", "event": "First official climb of Vice-President. 9 graduate (first: Miss McLennan, Miss Hobbs). Burgess also climbed."},
            {"date": "1906-07-11", "event": "Second official climb. 9 graduate. Wapta climbed."},
            {"date": "1906-07-12", "event": "Third official climb. 13 graduate. Collie, Field, Wapta climbed."},
            {"date": "1906-07-13", "event": "Fourth official climb. 7 graduate. Wapta climbed."},
            {"date": "1906-07-14", "event": "Fifth official climb. 4 graduate. President summit added. Yoho Glacier observation begins."},
            {"date": "1906-07-15", "event": "Yoho Glacier observation continues. Daily trips to Inspiration Point."},
            {"date": "1906-07-16", "event": "Camp breaks up. Marpole and Amgadamo first ascents. Many return via Burgess Pass."},
            {"date": "1906-07-17", "event": "Pack out continues."},
            {"date": "1906-07-18", "event": "Pack out complete."}
        ],
        "supporters": {
            "government": ["Dominion Government ($500)", "Alberta Government ($250)"],
            "railway": ["Canadian Pacific Railway (Swiss guides, tents, canopies, cooks)"],
            "outfitters": ["R.E. Campbell (Laggan/Field)", "Martin & Otto Bros. (Field/Leanchoil/Golden)", "E.C. Barnes (Banff)", "S.H. Baker (Glacier)"],
            "police": ["Royal North-West Mounted Police at Calgary and Banff (tents)"],
            "parks": ["Superintendent of Rocky Mountains Parks (bunting)"]
        }
    },
    # Sub-camp: Laughing Falls overnight
    {
        "camp_id": "laughing-falls-overnight",
        "name": "Laughing Falls Bivouac",
        "place_id": "laughing-falls",
        "dates": {
            "open": "1906-07-10",
            "close": "1906-07-15"
        },
        "elevation_ft": 4800,
        "capacity": 15,
        "actual_attendance": 60,
        "layout": {
            "sections": ["Bivouac site"],
            "description": "Overnight camp for Yoho Valley round trips and glacier observation. Ponies carried baggage."
        },
        "logistics": {
            "distance_from_station_miles": 0,
            "transport": "Ponies from Camp Yoho",
            "provisions": "Carried from Camp Yoho",
            "cook": "",
            "baggage_limit_lbs": 0
        },
        "funding": {},
        "people_present": [],
        "events": []
    }
]

# ============================================================
# ROUTES
# ============================================================
routes = [
    {
        "route_id": "field-to-camp",
        "name": "Field Station to Camp Yoho (1906 approach march)",
        "description": "The march of July 9, 1906. Crossed Kicking-Horse bridge, 7-mile forest road to Emerald Lake Chalet, traverse of northern glacial delta with stream crossings, 1000-ft cliff ascent through spruce forest to Yoho Pass summit.",
        "waypoints": [
            "field-station",
            "kicking-horse-bridge",
            "emerald-lake-road",
            "emerald-lake-chalet",
            "emerald-lake-north-delta",
            "yoho-pass",
            "camp-yoho"
        ],
        "distance_miles": 10,
        "elevation_gain_ft": 1925,
        "date": "1906-07-09",
        "sources": ["first-camp-yeigh", "yoho-camp-report"]
    },
    {
        "route_id": "vice-president-official",
        "name": "Official Climb of The Vice-President",
        "description": "From camp, trail to Yoho Pass summit, right to Michael Peak shoulder near timber-line, long rock slide, steep snow slopes to arete, knife-edge arete to Angle Peak, snowfield walk to summit.",
        "waypoints": [
            "camp-yoho",
            "yoho-pass",
            "michael-peak",
            "angle-peak",
            "vice-president"
        ],
        "distance_miles": 5,
        "elevation_gain_ft": 4050,
        "date": "1906-07-10 to 1906-07-14 (5 official ascents)",
        "sources": ["chief-mountaineer-report"]
    },
    {
        "route_id": "yoho-valley-round",
        "name": "Yoho Valley Round Trip (2-day)",
        "description": "Lower trail past Takakkaw Falls and Laughing Falls to Twin Falls and Yoho Glacier, overnight at Laughing Falls camp, return by upper trail with views of entire 15-mile valley.",
        "waypoints": [
            "camp-yoho",
            "takakkaw-falls",
            "laughing-falls",
            "twin-falls",
            "yoho-glacier",
            "camp-yoho"
        ],
        "distance_miles": 30,
        "elevation_gain_ft": 2000,
        "date": "4 consecutive trips during camp week",
        "sources": ["first-camp-yeigh", "chief-mountaineer-report"]
    },
    {
        "route_id": "emerald-glacier-trip",
        "name": "Emerald Glacier Trip",
        "description": "From camp, partly same route as Upper Yoho trail to Inspiration Point, then left turn toward glacier foot. Stiff ascent over boulders. Snow line at ~8000 ft. Ice-step climbing to main icefield with seracs and crevasses.",
        "waypoints": [
            "camp-yoho",
            "inspiration-point",
            "emerald-glacier"
        ],
        "distance_miles": 4,
        "elevation_gain_ft": 2000,
        "date": "3 trips during camp week",
        "sources": ["first-camp-yeigh", "chief-mountaineer-report"]
    },
    {
        "route_id": "burgess-pass-return",
        "name": "Burgess Pass Return Route",
        "description": "Return from camp to Mt. Stephen House via Burgess Pass trail. Views of President Range, Emerald mountains, glaciers, Emerald Lake below.",
        "waypoints": [
            "camp-yoho",
            "burgess-pass",
            "mt-stephen-house"
        ],
        "distance_miles": 8,
        "elevation_gain_ft": 1000,
        "date": "1906-07-16 (many campers used this return)",
        "sources": ["first-camp-yeigh", "chief-mountaineer-report"]
    }
]

# ============================================================
# WRITE ALL FILES
# ============================================================
def write_json(data, filename):
    path = OUT / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ✓ {path} ({len(json.dumps(data))} bytes)")

print("Building BASECAMP Intelligence Database...")
print(f"Date: {TODAY}")
print()

write_json({
    "schema_version": "1.0",
    "last_updated": TODAY,
    "total_people": len(people),
    "at_camp_count": sum(1 for p in people if p["at_camp"]),
    "people": people
}, "people.json")

write_json({
    "schema_version": "1.0",
    "last_updated": TODAY,
    "total_places": len(places),
    "places": places
}, "places.json")

write_json({
    "schema_version": "1.0",
    "last_updated": TODAY,
    "total_camps": len(camps),
    "camps": camps
}, "camps.json")

write_json({
    "schema_version": "1.0",
    "last_updated": TODAY,
    "total_routes": len(routes),
    "routes": routes
}, "routes.json")

print(f"\nDone. {len(people)} people, {len(places)} places, {len(camps)} camps, {len(routes)} routes.")
print(f"People at camp: {sum(1 for p in people if p['at_camp'])}")
print(f"People with Emerald Lake mentions: {sum(1 for p in people if any(a.get('mentions_emerald_lake') for a in p.get('articles_authored', [])))}")
