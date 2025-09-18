PARSER_ARGS = [
    {
        "flags": ["-i", "--input"],
        "required": True,
        "help": "Path to ScrimTime Inspector log file",
        "dest": "input_file",
        "type": str
    },
    {
        "flags": ["-o", "--output"],
        "required": False,
        "default": "stats.csv",
        "help": "Output CSV file path",
        "dest": "output_file",
        "type": str
    },
    {
        "flags": ["-v", "--verbose"],
        "required": False,
        "action": "store_true",
        "help": "Enable verbose logging"
    }
]