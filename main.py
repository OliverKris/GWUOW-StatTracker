# main.py

import re
import argparse
import sys
import os
from parser.log_parser import parse_line, create_parser
from timeline import Timeline
from match.match import Match, MatchStartEvent, MatchEndEvent
from match.player import PlayerStats
from event_handler import dispatch

parser = create_parser()
args = parser.parse_args()

# Collect arguments
log_file_path = args.input_file

# --- Error Handling ---

if not os.path.isfile(log_file_path):
    print(f"Error: Input file '{log_file_path}' does not exist. Please double check your spelling or its location.")
    sys.exit(1)

context = {
    "match": None
}

with open(log_file_path) as f:
    for line in f:
        event = parse_line(line)
        if not event:
            continue
        print(event)
        dispatch(event, context)
        
result = context["match"]

print(result.summary())
print(result.print_events())