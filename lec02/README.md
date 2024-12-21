# Esercitazione 2 - 25/10/2024

## Svolti in aula

### Esercizio
Scrivere una funzione rimario, a cui vengono passati come parametri una lista di
parole e una parola inserita dall'utente tramite funzione input.

La funzione rimario dovrà confrontare la parola inserita dall'utente con quelle
presenti nell'elenco, alla ricerca di rime, intese come parole le cui ultime 3
lettere siano uguali alla parola inserita dall'utente.

Le rime dovranno essere quindi mostrate in output utilizzando il metodo `join`.

Esempio:
```
Elenco parole:  ['dare', 'fare', 'andare', 'mangiare', 'dormire', 'piacere', 'salutare']
Parola in input:  volare
Le rime corrispondenti alla parola volare sono le seguenti: dare, fare, andare, mangiare, salutare
```

**[Soluzione](src/rimario.py)**

### Esercizio
Scrivere una funzione in Python che, data una lista di numeri, restituisce il
secondo numero più grande all'interno della lista.

Esempio:
```
Numeri:  [30, 20, 20, 30, 30, 20]
Secondo numero più grande:  20
```

**[Soluzione](src/second-largest.py)**

### Esercizio
Scrivere una funzione in Python che, date una lista di interi, genera un'altra
lista contenente solamente gli elementi duplicati.

Esempio:

```
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
```

```
Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]
```

**[Soluzione](src/duplicati.py)**

## Esercizi per casa

### Esercizio
Scrivere una funzione in python che, data una lista, rimuove da quest'ultima
tutte le liste vuote contenute all'interno.

Esempio:

```
Input: [3, 10, [], [], 4, [], 18]
Output: [3, 10, 4, 18]
```

```
Input: [3, 11, [4,3], [], 4, [1], 18]
Output: [3, 11, [4,3], 4, [1], 18]
```

**[Soluzione](src/empty-list.py)**

### Esercizio
Scrivere una funzione in Python che, date due liste `l1` e `l2`, restituisce
`True` se ogni elemento di `l1` è contenuto anche in `l2`, `False` altrimenti.

**[Soluzione](src/intersect.py)**

### Esercizio
Scrivere una funzione in Python che, date due liste `l1` e `l2`, restituisce
una lista senza duplicati che è l'intersezione delle due liste `l1` e `l2`.

**[Soluzione](src/subset.py)**
