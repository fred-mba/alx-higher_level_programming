#!/usr/bin/python3
"""Mylist module that inherits from list"""


class MyList(list):
    """Inherits from  list and print sorted list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print(sorted_list)
