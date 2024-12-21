#!/usr/bin/env python


def sort_binary_list(a):
    """
    l'idea è la seguente: sia z il numero di zeri in a.
    Allora è sufficiente modificare la lista inserendo 0
    nelle prime z posizioni e inserendo 1 nelle ultime
    len(a)-z posizioni
    """
    z = 0
    for e in a:
        if e == 0:
            z += 1
    k = 0
    while z:
        a[z] = 0
        z = z - 1
        k = k + 1

    for j in range(k, len(a)):
        a[j] = 1


"""
Complessità temporale: O(n)
Complessità spaziale: O(1)
"""


a = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]

print("Input: ", a)
sort_binary_list(a)
print("Output: ", a)
