#!/usr/ibn/python3
'''This module returns json to objcet'''

import json

def from_json_string(my_str):
    '''Returns object from json'''
    return json.loads(my_str)
