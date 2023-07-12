#!/usr/bin/python3
"""
Script: 7-add_item
Adds all arguments to a Python list and saves them to a file
"""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(args):
    """
    Adds all arguments to a Python list and saves them to a file.

    Args:
        args: The list of arguments.

    """
    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item(sys.argv[1:])
