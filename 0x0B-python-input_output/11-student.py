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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs: Optional list of attribute names to be retrieved.

        Returns:
            A dictionary representation of the student.

        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json: A dictionary representation of the student.

        """
        for attr, value in json.items():
            setattr(self, attr, value)
