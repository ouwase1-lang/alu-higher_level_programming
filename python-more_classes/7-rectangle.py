#!/usr/bin/python3
"""Module 7-rectangle.

Defines a class Rectangle with a configurable print symbol.
"""


class Rectangle:
    """A class that defines a rectangle by its width and height.

    Attributes:
        number_of_instances: the number of Rectangle instances alive.
        print_symbol: the symbol used to draw the rectangle (any type).
        __width: the width of the rectangle (private, validated).
        __height: the height of the rectangle (private, validated).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width: the width of the rectangle (integer >= 0).
            height: the height of the rectangle (integer >= 0).
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        The perimeter is 0 if the width or the height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle drawn with print_symbol.

        Returns an empty string if the width or the height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = str(self.print_symbol) * self.__width
        return "\n".join([row] * self.__height)

    def __repr__(self):
        """Return a string that eval() can use to recreate the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and update the instance count on deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
