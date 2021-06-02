#!/usr/bin/python3
"""
load_from_json_file - creates an object from a file containing json data
"""
import json


def load_from_json_file(filename):
    """ loads a json object from a file """
    with open(filename, 'r') as f:
        return json.load(f)
