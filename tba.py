import requests
import urllib.parse
from match import Match

TBA_API_KEY = "Z37IOn5LR76k6oZX42Yj6qktALW6DNd1aoQMeUSGzf1EEq1Cf2yX9jJcjiiKGIDx"

def submitVideo(match_key, url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "ACSID=~AJKiYcGeegduQLHJXj5q2wQRn5_oadnPvzfOdUcA3NhNAb-ALPVlyGz8TL02bTm7Y4Hm5W9w5Zraz4aaEMlO6TZ7DlndOXQpiLOkVAtIjjgNNTxY0HS6T_YpiKi8ZSvsfzkGpBL368AecSnuDU44_OkCF5XoOOMOc9_x9J0GO_4m8uaxxa-kaWF1z9WCHHO_x9tKXWaeXgOZPFYyIOzTSAYU9DkZrCnwcUoWaaxTZLiw0OTCB4tBOy22_TPAM1zsJ-rFZ4caSHV6GHp4Y0_YE_W27XZMETOi8FxVtBeBN4P41qICI8ej6zcpK_eQ_Fgpx9bYkHtNEVnIoy_irIe84afxeoCKYMydFg; tba-favorite-teams={\"frc5484\":true}",
        "origin": "https://www.thebluealliance.com"
    }
    youtube = urllib.parse.quote(url)
    res = requests.post(
        "http://www.thebluealliance.com/suggest/match/video?match_key={0}&youtube_url={1}".format(match_key, youtube), 
        headers=headers
    )

def api(query):
    headers = { "X-TBA-Auth-Key": TBA_API_KEY }
    res = requests.get("https://www.thebluealliance.com/api/v3" + query, headers=headers)
    return res.json()

def getMatchKeys(event_key):
    return api("/event/" + event_key + "/matches/keys")

def getEvent(event_key):
    return api("/event/" + event_key)

def getTitle(event_key, match_key):
    event = getEvent(event_key)
    name = event["name"]
    # Isolate the match slug from the match key
    slug = match_key[len(event_key) + 1:]
    name += " - " + Match.getName(slug)
    return name