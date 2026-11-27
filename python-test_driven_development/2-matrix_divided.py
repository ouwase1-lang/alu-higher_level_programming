#!/usr/bin/python3
"""
Module 2-matrix_divided.

Provides the function matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided by div.

    Results are rounded to 2 decimal places."""
    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(type_error)
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(type_error)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(type_error)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
