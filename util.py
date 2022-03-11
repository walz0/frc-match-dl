from match import Match, Playlist

def readInput():
    with open("./matches.txt", "r") as matches:
        # Remove leading / trailing whitespace and newlines
        return matches.read().strip()

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
        if _ != len(ids) - 1:
            # Group match keys and timestamps into pairs
            pairs = list(zip(*(iter(lines[ids[_]+1:ids[_ + 1]]),) * 2))
            # Convert pairs to Match objects
            matches = list(map(lambda x : Match(slug=x[0], timestamp=x[1]), pairs))
            video_id = lines[_][1:-1]
            playlists += [Playlist(matches, video_id)]
        else:
            # Group match keys and timestamps into pairs
            pairs = list(zip(*(iter(lines[ids[_]+1:]),) * 2))
            # Convert pairs to Match objects
            matches = list(map(lambda x : Match(slug=x[0], timestamp=x[1]), pairs))
            video_id = lines[_][1:-1]
            playlists += [Playlist(matches, video_id)]
    return playlists