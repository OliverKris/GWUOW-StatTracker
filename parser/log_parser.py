import argparse

from factories.event_factory import create_event
from parser.parser_args import PARSER_ARGS

def create_parser(arg_defs=PARSER_ARGS):
    parser = argparse.ArgumentParser(description="Parse ScrimTime log files to CSV.")

    if arg_defs is not None:
        for arg in arg_defs:
            flags = arg.pop("flags")
            parser.add_argument(*flags, **arg)
    return parser

def parse_line(line):
    line = line.strip()
    if not line:
        return None

    parts = line.split(",")
    timestamp = parts[0].strip().lstrip("[").rstrip("]")
    event_type = parts[1]
    fields = parts[3:]

    return create_event(timestamp, event_type, fields )