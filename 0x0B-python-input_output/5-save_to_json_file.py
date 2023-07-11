#!/usr/bin/python3
"""
Module that contains function that writes an 
Object to a text file using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using a JSON representation.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to write to.

    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    my_list = [1, 2, 3]
    save_to_json_file(my_list, "my_list.json")

    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, "my_dict.json")
