#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file
"""

import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(args: List[str]) -> None:
    """
    Adds all arguments to a Python list and saves them to a file.

    Args:
        args (List[str]): The list of arguments.

    """
    filename = "add_item.json"
    my_list = []

    if exists(filename):
        my_list = load_from_json_file(filename)

    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item(sys.argv[1:])
