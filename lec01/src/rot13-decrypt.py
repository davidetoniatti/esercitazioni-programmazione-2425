#!/usr/bin/env python

"""
Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del 
messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti 
nell'alfabeto.
Scrivere una funzione che, data in input una stringa criptata usando il cifrario
ROT-13, decripta la stringa e la restituisce in output.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher   = "nopqrstuvwxyzabcdefghijklm"

def decrypt_rot13_basic(ciphertext):
    """
    Questa funzione utilizza due liste per associare ad ogni carattere
    dell'alfabeto il carattere con cui sostituirlo per ottenere la stringa
    decifrata
    """
    plaintext = ""
    for c in ciphertext:
        if c == " ":
            plaintext += " "
        else:
            i = 0
            while c != alphabet[i]:
                i += 1
            plaintext += cipher[i]
    return plaintext

def decrypt_rot13(ciphertext):
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
            index = (i + 13) % 26
            plaintext += alphabet[index]
    return plaintext
