#!/usr/bin/python3
"""Module 6-square.

Defines a class Square with a size and a position, that can print itself.
"""


class Square:
    """A class that defines a square by its size and position.

    Attributes:
        __size: the size of the square (private, validated).
        __position: the offset used when printing (private, validated).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size: the size of the square (must be an integer >= 0).
            position: a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get or set the position of the square.

        Raises:
            TypeError: if the value is not a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #, using position.

        Prints an empty line if the size is 0.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
