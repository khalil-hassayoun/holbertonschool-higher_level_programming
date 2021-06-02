#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    for i in range(min(len(tuple_a), 2)):
        a[i] += tuple_a[i]
    for i in range(min(len(tuple_b), 2)):
        b[i] += tuple_b[i]
    new_tup = (a[0] + b[0], a[1] + b[1])
    return (new_tup)
