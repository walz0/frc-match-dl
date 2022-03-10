class Video:
    def convertTimestamp(self, timestamp):
        h,m,s = map(lambda x: int(x), timestamp.split(":"))
        return (h * 60 * 60) + (m * 60) + s

    def __init__(self, video_id, start, output) -> None:
        self.video = video_id
        self.start = self.convertTimestamp(start)
        # Add 160 seconds for match length + tolerance
        self.end = self.convertTimestamp(start) + 160
        self.output = output
        self.format = "mkv"
        self.overwrite = True
        self.quality = "1080p"
        self.max_workers = 5
        self.no_join = False
        self.keep = False
        pass