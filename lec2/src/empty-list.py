#!/usr/bin/env python

def empty_list(lista):
    tmp = []
    
    for e in lista:
        if e != []:
            tmp.append(e)
            
    i = 0
    while i < len(tmp):
        lista[i] = tmp[i]
        i += 1
        
    # i è la posizione del primo elemento da eliminare da a
    while i < len(lista):
        del(lista[-1])
