#!/usr/bin/env python

def duplicati(numeri):
    n = len(numeri)
    ripetuti = []
    for i in range(n):
        k = i+1
        for j in range(k,n):
            if numeri[i] == numeri[j] and numeri[i] not in ripetuti:
                ripetuti.append(numeri[i])
    return ripetuti
