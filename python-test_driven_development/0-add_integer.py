#!/usr/bin/python3
"""
Module 0-add_integer.

Provides the function add_integer(a, b=98).
"""


def add_integer(a, b=98):
    """Return the integer sum of a and b.

    Floats are cast to integers; other types raise TypeError."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
