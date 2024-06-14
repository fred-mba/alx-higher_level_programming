#!/usr/bin/python3
"""
Multiplication matrix module using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrices.

    This function mutiplies 2D matrices m_a & m_b using numpy. Using numpy,
    it is intended to ease the lenghty multlication in the previous task.

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

    arr1 = np.array(m_a)
    arr2 = np.array(m_b)

    matrix_result = np.matmul(arr1, arr2)

    return matrix_result
