#!/usr/bin/python3
"""Write an object to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Save object as JSON into a file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
