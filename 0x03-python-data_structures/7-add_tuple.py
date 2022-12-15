#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        new = tuple_b + (0, 0)
        res = tuple(map(lambda i, j: i + j, tuple_a, new))
        return(str(res))
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        res = tuple(map(lambda i, j: i + j, tuple_a[0:2], tuple_b[0:2]))
        return(str(res))
    else:
        res = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
        return(str(res))
