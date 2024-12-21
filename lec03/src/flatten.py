#!/usr/bin/env python


def flatten(a):
    tmp = []

    # lista temporanea con gli elementi di a e
    # appiattita
    for e in a:
        if type(e) != list:
            tmp.append(e)
        else:
            for e1 in e:
                tmp.append(e1)

    # ora bisogna modificare la lista in input,
    # come richiesto dall'esercizio, e renderla uguale
    # alla lista temporanea
    i = 0
    while i < len(tmp):
        if i < len(a):
            a[i] = tmp[i]
        # la lista tmp potrebbe essere più grande di a
        # in tal caso bisogna appendere in a.
        else:
            a.append(tmp[i])
        i += 1

    # se ci sono elementi di troppo in a, li eliminiamo
    while i < len(a):
        del a[-1]


a = ["casa", [4, 5, 6], 3, ["a", 8, "l"], "programmazione"]

flatten(a)
print(a)
