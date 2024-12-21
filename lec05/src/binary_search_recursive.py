#!/usr/bin/env python

def binary_search_recursive_right(a, k, lx, rx):
    if lx > rx:
        return -1

    cx = int( (lx+rx)/2 )

    if k == a[cx] and (cx == len(a) or a[cx+1] > k):
        return cx

    if k < a[cx]:
        return binary_search_recursive_right(a, k, lx, cx-1)
    else:
        return binary_search_recursive_right(a, k, cx+1, rx)


lista = [1,3,4,4,4,4,5,7,7,7,7,10,10,12,12,15,17]
k = 4
print("Input: ", lista, k)
print("Output: ", binary_search_recursive_right(lista, k, 0, len(lista)-1))

"""
Sia n la lunghezza della lista.
Complessità temporale: O(log n)
Complessità spaziale: O(log n) -> si vanno a creare log_2 n frames, uno per
ogni chiamata ricorsiva (ci sono log_2 n chiamate ricorsive), e ogni frame
occupa memoria costante.
"""

