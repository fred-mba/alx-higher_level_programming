#!/usr/bin/python3
"""
This module uses the function matrix_divided and return a new matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    The divided elements must be a float or an int. Each row of the matrix
    must have the same size

    Parameters
    ----------
    matrix : List, int
    div : int, float

    Return
    ------
    A new divided matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not all(isinstance(row, list) and len(row) > 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if all elements are int or floats and perform division
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            divided_element = element / div
            rounded_element = round(divided_element, 2)
            new_row.append(rounded_element)
        result.append(new_row)

    return result
