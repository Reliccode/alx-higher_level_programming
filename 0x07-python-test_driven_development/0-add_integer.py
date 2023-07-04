#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: Sum of the two integers.

    Raises:
        TypeError: If a or b are not either an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
