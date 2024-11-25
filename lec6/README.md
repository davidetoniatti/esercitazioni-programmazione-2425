# Esercitazione 6 - 22/11/2024

## Visti in aula

- Non c'è stata esercitazione in aula.

## Esercizi per casa

### Esercizio

Scrivere una funzione in Python che, date due liste `l1` e `l2`,
restituisce una lista che è la differenza delle due liste `l1` e `l2`,
ovvero, la nuova lista deve contenere tutti gli elementi di `l1` tranne quelli che sono
presenti anche in `l2`.
La soluzione deve avere complessità temporale **lineare** (in media) in `len(l1) + len(l2)`.

*Nota*: considerate le liste come insiemi, ovvero, non ci sono elementi ripetuti.

Esempio:
```
Input:
l1 =  [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
l2 =  [1, 3, 6, 7, 22, 23, 45, 99]
Output:  [5, 8, 12, 67, 123]
```

### Esercizio

Scrivere una funzione in Python che, dato un dizionario `d` con all'interno
coppie del tipo `(key, list[int])`, crea un dizionario con coppie del tipo
`(sum(list[int]), key)`.

Esempio:
```
Input: {'a': [2, 4, 5, 7], 'b': [6, 2, 4, 5], (2, 'A'): [4, 5, 6]}
Output: {18: 'a', 17: 'b', 15: (2, 'A')}
```

### Esercizio

Scrivere una funzione in Python che, data una lista `words` di parole e una
stringa `letters` di caratteri, stampa in output tutte e sole le parole in
`words` che possono essere ottenute usando un sottoinsieme delle lettere
in `letters`.

Esempio:
```
Input: words = ["cane", "gatto", "tartaruga", "canto"]
    letters = "anetougc"
Output: cane, gatto, canto
```
```
Input: words = ["cane", "gatto", "tartaruga", "canto"]
    letters = "anetougcr"
Output: cane, gatto, tartaruga, canto
```
