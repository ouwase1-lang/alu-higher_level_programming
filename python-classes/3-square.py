#!/usr/bin/python3
"""Module 3-square.

Defines a class Square with a validated size and an area method.
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

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
