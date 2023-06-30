#!/usr/bin/python3
"""
Module - Square
"""


class Square:
    """
    Class defining a square
    """
    def __init__(self, size=0):
        """
        Initializes a square

        Args:
            size: int size of the square
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Getter method for size attribute

        Returns:
            int: int size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute

        Args:
            value: The int size value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
