# Esercitazione 3

## No esercizi svolti in aula (giorno di festa, università chiusa)

## Esercizi per casa

### Esercizio

Scrivere una funzione `Min` in python che, data in input una lista `a` e una funzione
`key`, restituisce l'elemento `e` in `a` tale che `key(e) = min(key(x) per x in
a)`; se `key` è `None`, restitusce il minimo nella lista.

_Suggerimento: vedere la funzione `Max` in `lezione_10.py` nel repository del
professore_

### Esercizio
Scrivere una funzione in python che, data una lista di interi in input, esegue
le seguenti operazioni:

1. rimuove i duplicati dalla lista in input (modificare la lista in input);
2. crea una tupla a partire dalla lista modificata;
3. restituisce l'elemento massimo e l'elemento minimo nella tupla;

**Esempio**:

```
Input: [87, 45, 41, 65, 94, 41, 99, 94]

Lista modificata con duplicati rimossi: [87, 45, 41, 65, 99]

Si crea la tupla: (87, 45, 41, 65, 99)

Output: min: 41, max: 99
```

### Esercizio

Scrivere una funzione in python che, date due stringhe in input, restituisce
`True` se le due stringhe sono tra loro **anagrammi**, `False` altrimenti.

Vi ricordo che, date due parole `p1` e `p2`, la parola `p1` è un **anagramma**
della parola `p2` se spostando i caratteri di `p1` è possibile ottenere la
parola `p2` e viceversa.

**Esempio**:
```
Le parole `riso` e `orsi` sono anagrammi
Le parole `cattive` e `civetta` sono anagrammi
```

### Esercizio

Scrivere una funzione che, data in input una lista che **può contenere liste**,
modifichi la lista in input ***appiattendola***, cioè la lista deve contenere
tutti gli elementi originali ma eliminando le liste annidate. Guardate l'esempio
per capire cosa si intende.

**Esempio**:
```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output : [1,2,3,4,5,6,7,8,9]
```
```
Input: ["casa",[4,5,6],3,['a',8,'l'], "programmazione"]
Output : ["casa", 4, 5, 6, 3, 'a', 8, 'l', "programmazione"]
```
