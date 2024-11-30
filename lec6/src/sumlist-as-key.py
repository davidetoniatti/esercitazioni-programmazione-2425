#!/usr/bin/env python

def sumlist_as_key(d):
    d_new = {}
    for k in d:
       sumlist = 0
       for e in d[k]:
           sumlist += e
       d_new[sumlist] = k

    return d_new

d = {'a': [2,4,5,7], 'b': [6,2,4,5], (2,'A'): [4,5,6]}

print("Input:", d)
print("Output:", sumlist_as_key(d))

