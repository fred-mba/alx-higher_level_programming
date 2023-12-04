#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    A function that prints a matrix of integers
    """
    for row in matrix:
        for idx, element in enumerate(row):
            print("{:d}".format(element), end="")

            if idx < len(row) - 1:
                print(", ", end="")
        print()  # Move to the next line for the next row
