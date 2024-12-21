#!/usr/bin/env python


def modify_list(a):
    # si rimuovono i duplicati dalla lista
    # in input (quindi dalla lista a)
    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[i] == a[j]:
                del a[j]
            else:
                j += 1
        i += 1
    # si converte la lista in una tupla
    numbers_tuple = ()
    for e in a:
        # concatenazione di tuple, come le stringhe
        # mettendo la virgola dopo e, convertiamo
        # l'intero e in una tupla
        numbers_tuple += (e,)

    print(numbers_tuple)

    # restituiamo max e min nella tupla
    maximum = max(numbers_tuple)
    minimum = min(numbers_tuple)

    return maximum, minimum


a = [87, 45, 41, 65, 94, 41, 99, 94]
print(modify_list(a))
print(a)
