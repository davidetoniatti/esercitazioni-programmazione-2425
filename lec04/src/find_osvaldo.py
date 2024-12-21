#!/usr/bin/env python

def find_osvaldo(a):
    for e in a:
        if e == "osvaldo":
            return True
        elif type(e) == list:
            if find_osvaldo(e):
                return True
    return False

lista = [1,2,3,[1,2,3,4],[1,5,4,2,[1,2,"osvaldo"],4,3,2]]
print(find_osvaldo(lista))
