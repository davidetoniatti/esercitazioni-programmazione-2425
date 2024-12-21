# -*- coding: utf-8 -*- #

"""
Scrivere un programma che date due stringe in input,
in output stampa solo i caratteri che la prima stringa
ha in comune con la seconda stringa.
"""


def string_filter(string, filter_string):
    common_characters = ""
    i = 0
    while i < len(string):
        j = 0
        while j < len(filter_string):
            if string[i] == filter_string[j] and string[i] not in common_characters:
                common_characters += string[i]
            j += 1
        i += 1

    return common_characters


def string_filter_compact(string, filter_string):
    common_characters = ""
    for c in string:
        if c in filter_string:
            common_characters += c

    return common_characters


x = input("type first string: ")
y = input("type second string: ")

print(string_filter(x, y))
