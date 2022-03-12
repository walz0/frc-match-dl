import os
import tba
import argparse
from download import downloadMatches

def parseArgs():
    parser = argparse.ArgumentParser(description="A tool for easily downloading and processing FRC matches from twitch vods")
    parser.add_argument(
        "action", 
        help="""The action to run: download, submit
download - downloads the matches specified in matches.txt
submit - submits youtube URLs to The Blue Alliance website for given matches""")
    parser.add_argument(
        "-e", "--event", 
        help="Specifies which event to grab the video title from, defaults to video index if omitted.")
    parser.add_argument(
        "-o", "--output", 
        help="Specifies the output folder, creates an output folder in the current directory by default.")
    args = parser.parse_args()

    if args.action:
        if args.action == "download":

        if args.action == "submit":

    if args.output:
        # Check if path exists
        if not os.path.exists(args.output):
            print("Error: output path does not exist")
            return
    if args.event:
        # Check if event key exists
        if tba.isEventKey(args.event):
            downloadMatches(args.event)
        else:
            print("Error: event key does not exist")
            return