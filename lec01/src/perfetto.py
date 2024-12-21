# -*- coding: utf-8 -*-

"""
Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori
positivi, escluso sé stesso. Scrivere una funzione che verifichi se un numero è
perfetto oppure no.
"""


def perfetto(n):
    somma_divisori = 0
    i = 1
    # Itera sui numeri da 1 a n (escluso n)

    while i <= n//2:
        # Se i è un divisore di n, si aggiunge alla somma
        if n % i == 0:
            somma_divisori += i
        i += 1

    # Se la somma dei divisori è uguale a n, allora n è un numero perfetto
    if somma_divisori == n:
        return True
    else:
        return False


n = int(input("Inserisci un numero intero positivo: "))


if perfetto(n):
    print("Il numero " + str(n) + " è un numero perfetto.")
else:
    print("Il numero " + str(n) + " non è un numero perfetto.")
