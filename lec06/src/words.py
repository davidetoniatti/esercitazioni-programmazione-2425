#!/usr/bin/env python

def words_with_letters(words, letters):
    d_letters = {}
    res = []

    for c in letters:
        d_letters[c] = None
    
    for word in words:
        flag = True
        for c in word:
            if c not in d_letters:
                flag = False
        if flag:
            res.append(word)

    print(", ".join(res))

words = ["cane", "gatto", "tartaruga", "canto"]
letters = "anetougc"

words_with_letters(words, letters)
