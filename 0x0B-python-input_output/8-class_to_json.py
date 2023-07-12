#!/usr/bin/python3
"""
Module with a function that contains the function class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        A dictionary representation of the object.

    """
    return obj.__dict__
