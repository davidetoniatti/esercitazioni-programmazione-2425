#!/usr/bin/env python


def intersect_sorted(l1, l2):
    result = []
    i, j = 0, 0
    # scorri contemporaneamente le liste
    while i < len(l1) and j < len(l2):
        # se i-esimo elemento di l1 e j-esimo
        # elemento di l2 sono uguali, allora
        # tale elemento appartiene alla intersezione
        # delle due liste
        if l1[i] == l2[j]:
            result.append(l1[i])
            i += 1
            j += 1
        # se l'i-esimo elemento di l1 è più piccolo
        # del j-esimo elemento di l2, allora, dato che la lista
        # l2 è ordinata, l'elemento i-esimo di l1 non si trova in l2,
        # dunque non fa parte dell'intersezione delle due liste.
        # Avanza l'indice i.
        elif l1[i] < l2[j]:
            i += 1
        # se il j-esimo elemento di l2 è più piccolo
        # del i-esimo elemento di l1, allora, dato che la lista
        # l1 è ordinata, l'elemento j-esimo di l2 non si trova in l1,
        # dunque non fa parte dell'intersezione delle due liste.
        # Avanza l'indice j.
        else:
            j += 1
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
print("Output: ", intersect_sorted(l1, l2))
