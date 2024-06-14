#!/usr/bin/python3
"""
Multiplication matrix module using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrices.

    This function mutiplies 2D matrices m_a & m_b using numpy. NumPy
    shall ease the lengthy multlication in the previous task.

    Parameters
    ----------
    m_a : list, int, floats
    m_b : list, int, floats

    Return
    ------
    A mutiplied matrix result
    """
    if not isinstance(m_a, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if not all(isinstance(row_a, list) for row_a in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row_b, list) for row_b in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row_a) == 0 for row_a in m_a):
        raise ValueError("shapes (1,0) and (2,2) not aligned: 0 \
(dim 1) != 2 (dim 0)")

    if len(m_b) == 0 or any(len(row_b) == 0 for row_b in m_b):
        raise ValueError("shapes (2,2) and (1,0) not aligned: 2 \
(dim 1) != 1 (dim 0)")

    if any(not all(isinstance(el, (int, float)) for el in row) for row in m_a):
        raise TypeError("invalid data type for einsum")

    if any(not all(isinstance(el, (int, float)) for el in row) for row in m_b):
        raise TypeError("invalid data type for einsum")

    if any(len(row_a) != len(m_a[0]) for row_a in m_a):
        raise ValueError("setting an array element with a sequence.")

    if any(len(row_b) != len(m_b[0]) for row_b in m_b):
        raise ValueError("setting an array element with a sequence.")

    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes (2,3) and (2,2) not aligned: 3 \
(dim 1) != 2 (dim 0)")

    arr1 = np.array(m_a)
    arr2 = np.array(m_b)
    matrix_result = np.matmul(arr1, arr2)

    return matrix_result
