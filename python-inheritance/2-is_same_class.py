#!/usr/bin/python3
"""Module 2-is_same_class.

Defines a function that checks the exact class of an object.
"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    return type(obj) is a_class
