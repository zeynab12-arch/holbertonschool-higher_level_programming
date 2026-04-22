#!/usr/bin/python3
"""Module that reads a file and prints it to stdout."""

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
