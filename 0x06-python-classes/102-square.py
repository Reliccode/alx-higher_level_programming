#!/usr/bin/python3
"""
Module - Square
"""


class Square:
    """
    Class defining square
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
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute

        Args:
            value: int size value to set

        Raises:
            TypeError: If value is not a number (float or integer)
            ValueError: If value is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates area of square

        Returns:
            float: area of square
        """
        return self.__size ** 2

    def __equality__(self, other):
        """
        Equality comparison btn 2 Square instances

        Args:
            other (Square): other Square instance to compare to

        Returns:
            bool: True if both squares have equal areas, false if not
        """
        return self.area() == other.area()

    def __inequality__(self, other):
        """
        Inequality comparison between two Square instances

        Args:
            other (Square): other Square instance to compare to

        Returns:
            bool: True if both squares have different areas
        """
        return self.area() != other.area()

    def __greater__(self, other):
        """
        Greater than comparison between two Square instances

        Args:
            other (Square): other Square instance to compare to

        Returns:
            bool: True if current square has greater area
        """
        return self.area() > other.area()

    def __greq__(self, other):
        """
        Greater than or equal comparison between two Square instances

        Args:
            other (Square): other Square instance to compare to

        Returns:
            bool: True if the current square has >= area
        """
        return self.area() >= other.area()

    def __lessthan__(self, other):
        """
        Less than comparison between two Square instances

        Args:
            other (Square): other Square instance to compare to

        Returns:
            bool: True if current square has a smaller area
        """
        return self.area() < other.area()

    def __lessequal__(self, other):
        """
        Less than or equal comparison btn two Square instances

        Args:
            other (Square): other Square instance to compare to

        Returns:
            bool: True if current square has a smaller or equal area
        """
        return self.area() <= other.area()
