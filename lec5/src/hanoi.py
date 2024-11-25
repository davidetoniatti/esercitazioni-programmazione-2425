#!/usr/bin/env python

def hanoi(n, sorgente = 1, ausiliario = 2, destinazione = 3):
    if n > 0:
        # muovi n-1 dischi dalla sorgente all'asta ausiliaria,
        # usando l'asta target come intermedio
        hanoi(n-1, sorgente, destinazione, ausiliario)

        # muovi un disco dalla sorgente alla destinazione
        print("Muovo disco", n, "dall'asta", sorgente, "all'asta", destinazione)

        # muovi n-1 dischi dal'asta ausiliaria alla destinazione,
        # usando l'asta sorgente come intermedio
        hanoi(n-1, ausiliario, sorgente, destinazione)

print(hanoi(3))
