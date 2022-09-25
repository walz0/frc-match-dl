# frc-match-dl
A tool for easily downloading and processing FRC matches from twitch vods

# Pre-Requisites
- Python 3
- twitch-dl
- ffmpeg

[ffmpeg](https://www.ffmpeg.org/download.html) must be installed and in your PATH for this to work, twitch-dl will throw an error if it isn't.

[twitch-dl](https://github.com/ihabunek/twitch-dl) can be installed with pip:
```
pip install twitch-dl
```

# Match Naming Scheme
This tool uses The Blue Alliance match key naming scheme to set the title for each match

Here is a Blue Alliance match key for example:
```
2022inkok_qm1
```
The Blue Alliance uses the event key as a prefix for each match key followed by an identifier for what
type of match was played.

Here is a Blue Alliance event key for the 2022 FIN District Kokomo Event:
```
2022inkok
```

```
# The empty brackets are a placeholder for match numbers

Qualification Match
- qm[] e.g. qm34
Quarterfinal
- qf[]m[] e.g. qf1m3
Semifinal
- sf[]m[] e.g. sf2m1
Final
- f[]m[] e.g. f1m2 (Finals will almost always be f1 to start because there is only one finals)
```

# Usage
Enter all match keys and timestamps in the ```matches.txt``` file. You should omit the event key (e.g. ```2022inkok_qm34``` would be just ```qm34```) when entering your matches.

Example:
```
qm1
01:24:04
qm6
02:04:14
```

