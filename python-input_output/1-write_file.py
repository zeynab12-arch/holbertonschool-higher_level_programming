#!/usr/bin/python3
"""Module that writes a string to a UTF8 text file."""


def write_file(filename="", text=""):
    """Write a string to a file and return number of chars written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
