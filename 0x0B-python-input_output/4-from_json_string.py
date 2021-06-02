#!/usr/bin/python3
""" from_json_string module, returns an object from a json string """
import json


def from_json_string(my_str):
    """ returns an object from a json string """
    return json.loads(my_str)
