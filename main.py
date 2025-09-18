# main.py

"""
This file is the CLI script for the program. It creates a parser and takes in arguments
to determine its execution style. After creating the parser, it'll parse the input file
formatted based on the Overwatch Custom Game: ScrimTime output.
"""

import re
import argparse
import sys
import os
from parser.log_parser import parse_line, create_parser
from match.timeline import Timeline
from match.match import Match, MatchStartEvent, MatchEndEvent
from match.player import PlayerStats
from event_handler import dispatch

# Create parser and collect arguments
parser = create_parser()
args = parser.parse_args()

# Save arguments
log_file_path = args.input_file

# Error checking
if not os.path.isfile(log_file_path):
    print(f"Error: Input file '{log_file_path}' does not exist. Please double check your spelling or its location.")
    sys.exit(1)

# Create context representing the state of the game
context = {
    "match": None
}

# Open file and parse
with open(log_file_path) as f:
    for line in f:
        event = parse_line(line)
        if not event:
            continue
        print(event)
        # Dispatches using the different event handlers
        dispatch(event, context)
        
result = context["match"]
print(result.summary())
print(result.print_events())