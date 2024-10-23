# -*- coding: utf-8 -*-

"""
Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del 
messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti 
nell'alfabeto.
Scrivere una funzione in grado di criptare una stringa in input, o decriptarla
se la stringa è già stata precedentemente codificata.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher   = "nopqrstuvwxyzabcdefghijklm"

def encrypt_rot13_basic(plaintext):
    """
    Questa funzione utilizza due liste per associare ad ogni carattere
    dell'alfabeto il carattere con cui sostituirlo per ottenere la stringa
    cifrata
    """
    ciphertext = ""
    for c in plaintext:
        if c == " ":
            ciphertext += " "
        else:
            i = 0
            while c != alphabet[i]:
                i += 1
            ciphertext += cipher[i]
    return ciphertext

def encrypt_rot13(plaintext):
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
            index = (i + 13) % 26
            ciphertext += alphabet[index]
    return ciphertext


s = input("type the string to encrypt: ")
c = encrypt_rot13_basic(s)
print(c)
