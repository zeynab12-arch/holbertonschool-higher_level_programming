#!/usr/bin/python3
"""Module that reads a file and prints it to stdout."""


def read_file(filename=""):
    """Read a UTF-8 file and print its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
