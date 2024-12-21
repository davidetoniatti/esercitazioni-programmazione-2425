#!/usr/bin/env python


def rimario(elenco, parola):
    rime = []
    for elemento in elenco:
        if elemento[-3:] == parola[-3:]:
            rime.append(elemento)

    if not rime:
        print("Non sono state trovate rime corrispondenti alla parola in input!")
    else:
        output = ", ".join(rime)
        print(
            "Le rime corrispondenti alla parola "
            + parola
            + " sono le seguenti: "
            + output
        )


elenco = ["dare", "fare", "andare", "mangiare", "dormire", "piacere", "salutare"]
parola = input("Inserisci la parola di cui desideri cercare le rime: ")
print("Elenco parole: ", elenco)
print("Parola in input: ", parola)

rimario(elenco, parola)


