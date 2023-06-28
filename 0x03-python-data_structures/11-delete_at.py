#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the element at the specified index in the given list and returns the modified list.
    If the index is out of range, returns the original list without any modifications.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]

    return my_list
