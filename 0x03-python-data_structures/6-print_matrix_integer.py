#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers, where each row is represented as a sublist.
    """
    for sublist in matrix:
        for i in range(len(sublist)):
            print("{:d}".format(sublist[i]), end="")
            if i != len(sublist) - 1:
                print(" ", end="")
        print("")
