#!/usr/bin/python3
"""
Module 4-print_square.

Provides the function print_square(size).
"""


def print_square(size):
    """Print a square of side size using the character #.

    size must be an integer greater than or equal to 0."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
