#!/usr/bin/env python


def bubble_sort(a, key=None):
    def identity(e):
        return e

    n = len(a)

    if key == None:
        key = identity

    for c in range(n - 1):
        # se non effettua scambi, la lista è ordinata
        terminato = True
        for i in range(n - 1 - c):
            if key(a[i]) > key(a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                terminato = False
        if terminato:
            # la lista è ordinata
            break


def anagrams(word1, word2):
    # convertiamo le parole (stringhe) in liste di caratteri
    # perché la funzione bubble_sort prende in input una stringa
    # complessità temporale: lineare nella lunghezza delle stringhe
    word1_list = list(word1)
    word2_list = list(word2)

    # ordiniamo le liste corrispndenti alle due parole con bubble_sort
    # complessità temporale: quadratica nella lunghezza delle stringhe (liste)
    bubble_sort(word1_list)
    bubble_sort(word2_list)

    # controlliamo che le due parole siano anagrammi:
    # se le due liste corrispondenti alle parole sono diverse,
    # allora non possono essere anagrammi: restituisci False.
    if word1_list != word2_list:
        return False

    # se le due liste sono uguali, allora le parole sono anagrammi:
    # restituisci True.
    return True


print(anagrams("riso", "orsi"))
print(anagrams("cattive", "civetta"))
print(anagrams("programmazione", "calcolatori"))
