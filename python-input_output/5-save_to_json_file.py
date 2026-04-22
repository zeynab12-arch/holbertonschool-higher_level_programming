#!/usr/bin/python3

'''Writes to text file.'''

import json
def save_to_json_file(my_obj, filename):
    '''This module writes to atext file''
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
