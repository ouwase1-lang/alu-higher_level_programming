#!/usr/bin/python3
"""Module 6-base_geometry.

Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """A base class for geometry classes."""

    def area(self):
        """Raise an Exception: area is not implemented in the base class."""
        raise Exception("area() is not implemented")
