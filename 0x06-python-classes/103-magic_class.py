#!/usr/bin/python3
class MagicClass:
    def __init__(self, radius=0):
        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * 3.14159

    def circumference(self):
        return 2 * 3.14159 * self.__radius

