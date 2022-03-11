class Match:
    def __init__(self, slug, timestamp) -> None:
        self.slug = slug # Unique match identifier within match_key
        self.timestamp = timestamp # Timestamp of the start of the match from twitch vod
        pass

    def __str__(self):
        if self.slug[:2] == "qm":
            return "Qualification " + self.slug[2:]
        # Quarterfinal
        elif self.slug[:2] == "qf":
            return "Quarterfinal " + self.slug[2] + " Match " + self.slug[-1:]
        # Semifinal
        elif self.slug[:2] == "sf":
            return "Semifinal " + self.slug[2] + " Match " + self.slug[-1:]
        # Final
        elif self.slug[0] == "f":
            return "Final " + self.slug[1] + " Match " + self.slug[-1:]
        return None

    def getName(slug):
        match = Match(slug, "")
        return match.__str__()

class Playlist:
    def __init__(self, matches, video_id) -> None:
        self.matches = matches
        self.video_id = video_id
        pass