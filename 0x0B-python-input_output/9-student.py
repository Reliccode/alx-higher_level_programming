#!/usr/bin/python3
"""
Module with function that contains the class Student
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            A dictionary representation of the student.

        """
        return self.__dict__
