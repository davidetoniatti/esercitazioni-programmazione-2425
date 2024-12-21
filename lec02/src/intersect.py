#!/usr/bin/env python

def intersect(list1, list2):
    tmp = []
    for e1 in list1:
        for e2 in list2:
            if e1 == e2:
                tmp.append(e1)
    result = []
    for e in tmp:
        if e not in result:
            result.append(e)
    return result
