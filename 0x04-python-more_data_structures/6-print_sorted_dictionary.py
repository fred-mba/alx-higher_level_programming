#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for j in sorted(my_dict):
        print('{}: {}'.format(j, my_dict[j]))
