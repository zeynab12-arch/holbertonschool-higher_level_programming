#!/usr/bin/python3
'''This module appends to a file'''


def append_write(filename="", text=""):
    '''appends to a file'''
    with open(filename, "a", encoding="utf-8") as f:
        returnf.write(text)
