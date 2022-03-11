import os
import tba
import util
from video import Video
from match import Match, Playlist
from twitchdl.commands import download

# Read raw match data
matchData = util.readInput()
playlists = util.parseMatches(matchData)

print(playlists)
# for playlist in playlists:
#     title = tba.getEvent("2022inkok")["name"]
#     output_path = "./output/"

#     for match in playlist.matches:
#         vod = download(
#             Video(
#                 video_id=match.video_id,
#                 start=match.start,
#                 output=output_path + title + " - " + match.__str__() + ".mp4"
#             )
#         )