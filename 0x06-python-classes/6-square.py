#!/usr/bin/python3
"""
Module - Square
"""


class Square:
    """
    Class defining a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square

        Args:
            size: int size of the square
            position (tuple): tuple position of the square
        """
        self.__size = 0
        self.__position = (0, 0)
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for position attribute

        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute

        Args:
            value (tuple): position value to set

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints square using '#' character and the position
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
