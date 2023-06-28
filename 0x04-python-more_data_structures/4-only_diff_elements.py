#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newSet1 = set(set_1)
    newSet2 = set(set_2)

    return newSet1 ^ newSet2
