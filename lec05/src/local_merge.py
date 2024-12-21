#!/usr/bin/env python


def local_merge(l1, l2):
    n = len(l1)
    m = len(l2)

    for i in range(n):
        if l1[i] > l2[0]:
            tmp = l1[i]
            l1[i] = l2[0]
            l2[0] = tmp

        first = l2[0]

        k = 1
        while k < m and l2[k] < first:
            l2[k - 1] = l2[k]
            k += 1

        l2[k - 1] = first

"""
Complessità temporale: O(n*m) nel caso peggiore
Complessità spaziale: O(1)
"""

x = [1, 4, 7, 8, 10]
y = [2, 3, 9]
local_merge(x, y)
print("x:", x)
print("y:", y)
