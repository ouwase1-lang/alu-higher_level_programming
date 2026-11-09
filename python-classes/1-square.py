#!/usr/bin/python3
"""Module 1-square.

Defines a class Square with a private size attribute.
"""


class Square:
    """A class that defines a square by its size.

    Attributes:
        __size: the size of the square (private, not validated).
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the size of the square.
        """
        self.__size = size
