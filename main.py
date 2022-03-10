from video import Video
import tba
from match import Match
from twitchdl.commands import download

matches = """
qf2m1
"4:58:42"
qf2m2
"5:50:55"
sf1m1
"6:24:33"
sf1m2
"6:48:12"
sf1m3
"7:06:11
"""

def parseMatches(data):
    # Remove leading / trailing whitespace and newlines
    data = data.strip()
    lines = data.split("\n")
    print(lines)
    # Each match_key should have a timestamp
    if len(lines) % 2 != 0:
        return None
    # Group lines into groups of two
    lines = zip(*(iter(lines),) * 2)
    matches = list(map(lambda x : Match(slug=x[0], timestamp=x[1]), lines))
    print(matches)


parseMatches(matches)


# output_path = "./output/"
# video_id = "1417226844"
# title = "2022 FIN District Kokomo Event - "

# for _ in range(len(timestamps)):
#     vod = download(
#         Video(
#             video_id=video_id,
#             start=timestamps[_],
#             output=output_path + title + str(_) + ".mp4"
#         )
#     )