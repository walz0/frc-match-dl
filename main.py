import os
import tba
import util
from video import Video
from match import Match, Playlist
from twitchdl.commands import download

# Read raw match data
matchData = util.readInput()
playlists = util.parseMatches(matchData)

for playlist in playlists:
    title = tba.getEvent("2022inkok")["name"]
    output_path = "./output/" + playlist.video_id + "/"

    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    for match in playlist.matches:
        print(match.slug)
        vod = download(
            Video(
                video_id=playlist.video_id,
                start=match.timestamp,
                output=output_path + title + " - " + match.__str__() + ".mp4"
            )
        )