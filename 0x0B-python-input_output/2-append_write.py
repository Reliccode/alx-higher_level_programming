#!/usr/bin/python3
"""
Module that contains a function that appends a string to a
text file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended.

    Returns:
        int: The number of characters added.

    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
