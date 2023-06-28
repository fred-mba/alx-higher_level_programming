#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples and returns a new tuple with the sums of 
    corresponding elements.
    """
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    sum_a = tuple_a[0] + tuple_b[0]
    sum_b = tuple_a[1] + tuple_b[1]

    return sum_a, sum_b
