#!/usr/bin/python3
"""Pascal's principle
triangle[i][j]=triangle[i−1][j−1]+triangle[i−1][j]
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
       the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for r in range(1, n):
        prev_row = triangle[r - 1]
        new_row = [1]  # Start row with 1

        for i in range(1, r):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
