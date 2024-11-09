#!/usr/bin/env python


def Min(a, key=None):

    def identity(e):
        return e

    if key == None:
        key = identity

    v_min = key(a[0])
    r_min = a[0]

    for e in a:
        if key(e) < v_min:
            v_min, r_min = key(e), e

    return r_min


def t1(e):
    return e[1]


a = [("A", 6), ("B", -2), ("E", 3), ("C", 0), ("D", 5)]

print(Min(a))
print(Min(a, key=t1))
