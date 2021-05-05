#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newtuple_a = tuple_a + (0, 0)
    newtuple_b = tuple_b + (0, 0)
    result = newtuple_a[0] + newtuple_b[0], newtuple_a[1] + newtuple_b[1]
    return result
