#!/usr/bin/python3
""" to_json_string module """


import json


def to_json_string(my_obj):
    """ dumps the json repr of an object """
    return (json.dumps(my_obj))
