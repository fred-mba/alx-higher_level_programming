#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    A function that adds 2 tuples.
    """
    tuple_a = tuple_a + (0,) * max(0, 2 - len(tuple_a))
    tuple_b = tuple_b + (0,) * max(0, 2 - len(tuple_b))

    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    result = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    return result
