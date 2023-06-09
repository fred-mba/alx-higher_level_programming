#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieve the element at the given index from the list.
    If the index is out of range, return the string "None".
    """
    return my_list[idx] if 0 <= idx < len(my_list) else "None"
