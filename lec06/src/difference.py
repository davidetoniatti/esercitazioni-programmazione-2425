#!/usr/bin/env python

def difference(l1,l2):
    d1, d2 = {}, {}

    for e in l1:
        d1[e] = None

    for e in l2:
        d2[e] = None

    diff = []
    
    for e in d1:
        if e not in d2:
            diff.append(e)
    
    return diff

l1 =  [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
l2 =  [1, 3, 6, 7, 22, 23, 45, 99]

print(difference(l1,l2))
