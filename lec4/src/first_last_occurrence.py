#!/usr/bin/env python


def binary_search_right(a, k):
    n = len(a)
    lx, rx = 0, len(a) - 1

    while lx <= rx:
        cx = int((lx + rx) / 2)
        if k < a[cx]:
            rx = cx - 1
        elif k == a[cx] and (cx == n - 1 or a[cx + 1] > k):
            return cx
        else:
            lx = cx + 1

    return -1


def binary_search_left(a, k):
    lx, rx = 0, len(a) - 1

    while lx <= rx:
        cx = int((lx + rx) / 2)
        if k > a[cx]:
            lx = cx + 1
        elif k == a[cx] and (cx == 0 or a[cx - 1] < k):
            return cx
        else:
            rx = cx - 1

    return -1


def first_last_occurrence(a, k):
    # usando binary_search_left, troviamo la prima occorrenza di k
    first = binary_search_left(a, k)
    # usando binary_search_right, troviamo l'ultima occorrenza di k
    last = binary_search_right(a, k)

    # se k non è in a (cioè le ricerche binarie restituiscono -1), allora
    # si restituisce -1
    if first == -1:
        return -1

    return first, last


a = [1, 3, 4, 4, 4, 4, 5, 7, 7, 7, 7, 10, 10, 12, 12, 15, 17]
k = 4

print(first_last_occurrence(a, k))
