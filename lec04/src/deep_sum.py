#!/usr/bin/env python

def deep_sum(l):
    sum = 0
    for e in l:
        if type(e) is not list:
            sum += e
        else:
            sum += deep_sum(e)
    return sum
"""
la dimensione dell'input n è data dal numero degli elementi interi nella
lista ed in tutte le sottoliste annidate.
Complessità temporale:
    T(n) lineare in n 
Complessità spaziale:
    O(n) nel caso peggiore, cioà quando ci sono n livelli di
    annidamento
"""

lista = [1,2,5,[20,3,1,[40,6,3],2,5,6],5,[7,8]]
print(deep_sum(lista))
