#!/usr/bin/python3
"""
Module that contains a fucntion that writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes string to a text file and returns the number of chars written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to be written.

    Returns:
        int: The number of characters written.

    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
