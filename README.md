# frc-match-dl
A tool for easily downloading and processing FRC clips from twitch vods

# Match Naming Scheme
This tool uses The Blue Alliance match key naming scheme to set the title for each match

Here is Blue Alliance match key for example:
```
    2022inkok_qm1
```
The Blue Alliance uses the event key as a prefix for each match key followed by an identifier for what
type of match was played.

```
    The empty brackets are a placeholder for the match numbers

    Qualification Match
    - qm[] e.g. qm34
    Quarterfinal
    - qf[]m[] e.g. qf1m2
    Semifinal
    - sf[]m[] e.g. sf2m1
    Final
    - f[]m[] e.g. f1m2 (Finals will almost always be f1 to start because there is only one finals)
```

You should omit the event key (2022inkok in this case) when entering your matches.
Your file should look something like this:
```
    qm1
    01:24:04
    qm6
    02:04:14
```

# Dependencies
- twitch-dl
- ffmpeg