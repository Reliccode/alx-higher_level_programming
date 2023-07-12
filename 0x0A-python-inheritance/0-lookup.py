#!/usr/bin/python3

def lookup(obj):
    """
    Returns list of available attributes and methods of object.

    Args:
        obj: object to look up.

    Returns:
        List of strings representing available attributes and methods of object.
    """
    return dir(obj)
