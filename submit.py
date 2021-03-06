import tba
import util
from match import Match

def submitMatches(event_key):
    data = util.readURLInput()
    # Youtube URLs to submit to The Blue Alliance for review
    urls = util.parseURLs(data)

    for url in urls:
        print("Submitting", Match.getName(url["slug"]), "at", url["url"])
        tba.submitVideo(event_key + "_" + url["slug"], url["url"])
