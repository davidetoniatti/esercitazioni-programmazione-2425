#!/usr/bin/env python

def difference_sorted(l1,l2):
    result = []
    n, m = len(l1), len(l2)
    i, j = 0, 0
    while i < n and j < m:
        if l1[i] == l2[j]:
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            j += 1
    print(i)
    print(j)
    if j == m:
        while i < n:
            result.append(l1[i])
            i += 1
    return result

"""
Complessità temporale: O(n+m), dove n = len(l1) e m = len(l2)
Complessità spaziale: O(1)
"""


l1 = [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
l2 = [1, 3, 4, 6, 7, 10, 13, 22, 23, 24, 25, 26, 45, 69, 99, 121]

print("Input:")
print("l1 = ", l1)
print("l2 = ", l2)
print("Output: ", difference_sorted(l1, l2))
print(set(l1)-set(l2))


