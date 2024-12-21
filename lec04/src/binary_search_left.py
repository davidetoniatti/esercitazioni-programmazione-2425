#!/usr/bin/env python

def binary_search_left(a, k):
    n = len(a)
    lx, rx = 0, len(a)-1

    while lx <= rx:
        cx = int( (lx+rx)/2 )
        if k > a[cx]:
            lx = cx + 1
        elif k == a[cx] and (cx == 0 or a[cx-1] < k):
            return cx
        else:
            rx = cx-1

    return -1

"""
Sia n la lunghezza della lista.
Complessità temporale: O(log n)
Complessità spaziale: O(1)
"""

lista = [1,3,4,4,4,4,5,7,7,7,7,10,10,12,12,15,17]
k = 4
print("Input: ", lista, k)
print("Output: ", binary_search_left(lista, k))


