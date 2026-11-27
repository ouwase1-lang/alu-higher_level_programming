#!/usr/bin/python3
"""Defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square, which is a rectangle with equal sides."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and the height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes from positional or keyword arguments."""
        if args:
            kwargs = dict(zip(("id", "size", "x", "y"), args))
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
