#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set1 = set(set_1)
    new_set2 = set(set_2)

    return new_set1 ^ new_set2
    # return new_set1.symmetric_difference(new_set2)
