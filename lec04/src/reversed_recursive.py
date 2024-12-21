#!/usr/bin/env python

def reverse_recursive_basic(s):
    if len(s) == 1:
        return s[0]
    else:
        reversed = reverse_recursive_basic(s[1:])
        reversed += s[0]
        return reversed 

print(reverse_recursive_basic("programmazione")) 
"""
Sia n la lunghezza della stringa.
Complessità temporale: O(n**2), in quanto vengono fatte n chiamate ricorsive
e all'interno di ogni chiamata ricorsiva avviene un'operazione di slicing
(come l'analisi temporale del massimo ricorsivo visto a lezione).
Complessità spaziale: O(n**2) per lo slicing.
"""

def reversed_recursive_maybe_better(s, i = 0):
    if i == len(s)-1:
        return s[i]
    else:
        reversed = reversed_recursive_maybe_better(s, i+1)
        reversed += s[i]
        return reversed
"""
Sia n la lunghezza della stringa.
Complessità temporale: O(n**2), in quanto vengono fatte n chiamate ricorsive
e per ogni chiamata ricorsiva viene copiato il contenuto della stringa.
Complessità spaziale: O(n**2) dato che ogni chiamata ricorsiva mantiene tutta
la stringa.
"""

print(reversed_recursive_maybe_better("programmazione")) 

def reversed_recursive_much_better(s, i = 0):
    if type(s) is str:
        l = []
        for c in s:
            l.append(c)
        s = l
    if i == len(s)-1:
        return s[i]
    else:
        reversed = reversed_recursive_much_better(s, i+1)
        reversed += s[i]
        return reversed
"""
Sia n la lunghezza della stringa, dunque n è anche la lunghezza della
lista d'appoggio creata.
Complessità temporale: O(n), in quanto vengono fatte n chiamate ricorsive
e in ogni chiamata ricorsiva si effettuano un numero costante di operazioni.
Complessità spaziale: O(n+n)=O(n) dato che vengono aperti n frame dalle
chiamate ricorsive e viene mantenuta una lista ausiliaria contenente tutti i
caratteri della stringa.
"""

print(reversed_recursive_much_better("programmazione")) 
