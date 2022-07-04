#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    for i in range(len(tuple_a)):
        tuple_c += (tuple_a[i] + tuple_b[i])
    return tuple_c
