from match import Match, Playlist

def readMatchInput():
    with open("./matches.txt", "r") as matches:
        # Remove leading / trailing whitespace and newlines
        return matches.read().strip()

def readURLInput():
    with open("./urls.txt", "r") as urls:
        # Remove leading / trailing whitespace and newlines
        return urls.read().strip()

def parseMatches(data):
    lines = data.split("\n")
    # Check for video ids and store them in a list
    ids = []
    for _ in range(len(lines)):
        if lines[_][0] == "[":
            ids += [_]
    # Group match playlists
    playlists = []
    for _ in range(len(ids)):
        # Group match keys and timestamps into pairs
        if _ != len(ids) - 1:
            pairs = list(zip(*(iter(lines[ids[_]+1:ids[_ + 1]]),) * 2))
        else:
            pairs = list(zip(*(iter(lines[ids[_]+1:]),) * 2))
        # Convert pairs to Match objects
        matches = list(map(lambda x : Match(slug=x[0], timestamp=x[1]), pairs))
        video_id = lines[ids[_]][1:-1]
        playlists += [Playlist(matches, video_id)]
    return playlists

def parseURLs(data):
    lines = data.split("\n")
    pairs = list(zip(*(iter(lines),) * 2))
    urls = list(map(lambda x: {"slug":x[0], "url": x[1]}, pairs))
    return urls
