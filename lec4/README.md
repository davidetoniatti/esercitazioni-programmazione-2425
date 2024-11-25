# Esercitazione 4 - 08/11/2024

## Svolti in aula

- Esercitazione solamente a distanza.

### Esercizio

Scrivere una funzione in Python che, data una lista composta da interi e
sottoliste annidate (composte da interi e altre sottoliste), restituisce
in output la somma di tutti gli interi.

Esempio:

```
Input: [1,2,5,[20,3,1,[40,6,3],2,5,6],5,[7,8]]
Output: 114
```

**[Soluzione](src/deep_sum.py)**

### Esercizio

Scrivere una funzione in python che, data una stringa in input,
ritorna in output la stringa invertita. Fare questo usando la ricorsione
e usando unicamente l'operazione di concatenazione tra stringhe.

**[Soluzione](src/reversed_recursive.py)**

## Esercizi per casa

### Esercizio

Scrivere una funzione in Python che, data una lista di numeri interi
distinti non negativi ordinati in modo crescente, restutisce il più
piccolo elemento non negativo mancante in essa. Se non ci sono
elementi mancanti, restituisce -1.

Esempio:

```
Input: [0,1,2,3,4,5,7,9,11]
Output: 6
```
```
Input: [1,2,3,5,7,9,20]
Output: 0
```
```
Input: [0,1,2,3,4,5]
Output: -1
```

**[Soluzione](src/find_smallest_missing.py)

### Esercizio

In una lista c'è un intruso: *osvaldo*.

Scrivi una funzione in Python che data una lista di elementi, tra cui sottoliste
annidate, ritorna `True` se trova *osvaldo*, `False` altrimenti.

Esempio:

```
Input: [1,2,3,[1,2,3,4],[1,5,4,2,[1,2,"osvaldo"],4,3,2]]
Output: True
```
```
Input: [1,2,3,[1,2,3,4],[1,5,4,2,[1,2,10],4,3,2]]
Output: False
```

**[Soluzione](src/find_osvaldo.py)**

### Esercizio

Scrivere una funzione in Python che, data una lista $a$ di numeri ordinati in
modo non decrescente ed un numero $k$, restituisce la posizione dell'occorrenza
più a sinistra di $k$ in $a$. Se $k$ non è in $a$, ritorna -1.

Esempio:

```
Input: a = [1, 3, 4, 4, 4, 4, 5, 7, 7, 7, 7, 10, 10, 12, 12, 15, 17],
       k = 10
Output:  11
```

**[Soluzione](src/binary_search_left.py)**

### Esercizio

Scrivere una funzione in Python che, data una lista $a$ di numeri ordinati in
modo non decrescente ed un numero $k$, restituisce la posizione della prima
occorrenza di $k$ in $a$ e la posizione dell'ultima occorrenza di $k$ in $a$.
Se $k$ non è in $a$, ritorna -1.

Esempio:

```
Input: a = [1, 3, 4, 4, 4, 4, 5, 7, 7, 7, 7, 10, 10, 12, 12, 15, 17],
       k = 4
Output:  prima occorrenza: posizione 2; ultima occorrenza: posizione 5
```

**[Soluzione](src/first_last_occurrence.py)**
