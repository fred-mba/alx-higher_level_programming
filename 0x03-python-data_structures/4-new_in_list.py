#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Create a new list with the element replaced at the given index.
    If the index is out of range or the input list is None, return None.
    """
    if my_list is None:
        return (None)
    
    new_list = my_list[:]

    if 0 <= idx < len(new_list):
        new_list[idx] = element

    return (new_list)
