#!/usr/bin/env python

def collatz(n):
    n = int(n) # Il numero n deve essere intero
    iterazioni = 0
    # quando n = 1, ciclo deve terminare
    while n > 1:
        # Se il numero è pari, dividi per due
        if n%2 == 0:
            # con "//" la divisione risulta in un numero intero,
            # verificare con type(n)
            n = n//2 
        # altrimenti, moltiplica per 3 e aggiungi 1
        else:
            n = 3*n + 1
        # stampa il valore calcolato
        print(n, end=' ')
        iterazioni += 1
    print("")
    return iterazioni

print("Numero di iterazioni: ", collatz(27))
