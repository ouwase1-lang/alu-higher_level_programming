#!/usr/bin/python3
"""Module 4-square.

Defines a class Square with a size that can be read and updated.
"""


class Square:
    """A class that defines a square by its size.

    Attributes:
        __size: the size of the square (private, validated).
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: the size of the square (must be an integer >= 0).
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
