# -*- coding: utf-8 -*-

"""
Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del 
messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti 
nell'alfabeto.
Scrivere una funzione in grado di criptare una stringa in input, o decriptarla
se la stringa è già stata precedentemente codificata.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt_rot13(plaintext):
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


def decrypt_rot13(ciphertext):
    plaintext = ""
    for c in ciphertext:
        if c == " ":
            plaintext += " "
        else:
            i = 0
            while c != alphabet[i]:
                i += 1
            index = (i - 13) % 26
            plaintext += alphabet[index]
    return plaintext


s = input("type the string to encrypt: ")
c = encrypt_rot13(s)
print("")
print(c)
print("")
print(decrypt_rot13(c))
