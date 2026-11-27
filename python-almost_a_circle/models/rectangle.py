#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A rectangle with a size and a position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        self.__check_size("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        self.__check_size("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the horizontal offset."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal offset."""
        self.__check_offset("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the vertical offset."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical offset."""
        self.__check_offset("y", value)
        self.__y = value

    @staticmethod
    def __check_size(name, value):
        """Validate that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def __check_offset(name, value):
        """Validate that value is an integer of at least 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Return the area."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #."""
        row = " " * self.x + "#" * self.width + "\n"
        print("\n" * self.y + row * self.height, end="")

    def __str__(self):
        """Return the string representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes from positional or keyword arguments."""
        if args:
            kwargs = dict(zip(("id", "width", "height", "x", "y"), args))
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
