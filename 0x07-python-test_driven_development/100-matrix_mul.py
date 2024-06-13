#!/usr/bin/python3
"""
Multiplication matrix module
"""


def matrix_mul(m_a, m_b):
    """
    Multiply 2 matrices.

    This function mutiplies two matrices m_a & m_b which are in form 2D
    list arrays.

    Parameters
    ----------
    m_a : list, int, floats
    m_b : list, int, floats

    Return
    ------
    A mutiplied matrix result
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row_a, list) for row_a in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row_b, list) for row_b in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row_a) == 0 for row_a in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or any(len(row_b) == 0 for row_b in m_b):
        raise ValueError("m_b can't be empty")

    if any(not all(isinstance(el, (int, float)) for el in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")

    if any(not all(isinstance(el, (int, float)) for el in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row_a) != len(m_a[0]) for row_a in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if any(len(row_b) != len(m_b[0]) for row_b in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):  # Iter over the rows of m_a
        for j in range(len(m_b[0])):  # Iter over the columns of m_b
            for k in range(len(m_b)):  # Iter over the rows of m_b
                matrix_result[i][j] += m_a[i][k] * m_b[k][j]

    return matrix_result
