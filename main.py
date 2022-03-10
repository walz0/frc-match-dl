from video import Video
from twitchdl.commands import download

timestamps = [
    "4:58:42",
    "5:50:55",
    "6:24:33",
    "6:48:12",
    "7:06:11"
]

output_path = "./output/"
video_id = "1417226844"
title = "2022 FIN District Kokomo Event - "

for _ in range(len(timestamps)):
    vod = download(
        Video(
            video_id=video_id,
            start=timestamps[_],
            output=output_path + title + str(_) + ".mp4"
        )
    )