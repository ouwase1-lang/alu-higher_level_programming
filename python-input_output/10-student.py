#!/usr/bin/python3
"""Module that defines a Student class with a filtered JSON export."""


class Student:
    """Defines a student by first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student.

        If attrs is a list of strings, only those attribute names
        are retrieved. Otherwise, all attributes are retrieved.
        """
        if (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()
