#!/usr/bin/env python

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt_caesar(plaintext, k):
    """
    Questa funzione utilizza l'artimetica modulare:
    https://it.wikipedia.org/wiki/Aritmetica_modulare
    """
    ciphertext = ""
    for c in plaintext:
        if c == " ":
            ciphertext += " "
        else:
            i = 0
            while c != alphabet[i]:
                i += 1
            index = (i + k) % 26
            ciphertext += alphabet[index]
    return ciphertext


def decrypt_caesar(ciphertext, k):
    """
    Questa funzione utilizza l'artimetica modulare:
    https://it.wikipedia.org/wiki/Aritmetica_modulare
    """
    plaintext = ""
    for c in ciphertext:
        if c == " ":
            plaintext += " "
        else:
            i = 0
            while c != alphabet[i]:
                i += 1
            index = (i + k) % 26
            plaintext += alphabet[index]
    return plaintext
