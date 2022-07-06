#!/usr/bin/python3
""" Writes an Object to a text file using
a JSON representation
"""
import json

def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file
    by a JSON representation
    
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
