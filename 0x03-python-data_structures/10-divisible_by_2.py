#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Returns a list of booleans indicating whether each element in
    the given list is a multiple of 2.
    If the input list is empty, returns an empty list.
    """
    new_list = []

    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
