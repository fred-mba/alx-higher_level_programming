#!/usr/bin/python3
"""This module finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    The algorithm finds the length & mid of list then
    it compares the items on the left and right from the mid
    to obtain the heighest value(peak)
    Note: there may be more than one peak in the list
    """
    n = len(list_of_integers)

    if n == 0:
        return None

    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
