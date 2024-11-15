# Esercitazione 5

## Visti in aula

### Esercizio

Scrivere una funzione in Python che, data una lista *binaria* `a`, cioè contenente
unicamente elementi in `{0,1}`, ordina la lista `a`. La funzione deve avere
complessità temporale **lineare** in `len(a)` e complessità spaziale **costante**.

Esempio:
```
Input:  [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
Output:  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
```

**[Soluzione](src/sort_binary_list.py)**

### Esercizio

Scrivere una funzione in Python che, date due liste `l1` e `l2` **entrambe ordinate**,
restituisce una lista che è l'intersezione delle due liste `l1` e `l2`.
La soluzione deve avere complessità temporale **lineare** in `len(l1) + len(l2)`, e 
memoria supplementare costante, possibilmente.

*Nota*: considerate le liste come insiemi, ovvero, non ci sono elementi ripetuti.

Esempio:
```python
Input:
l1 =  [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
l2 =  [1, 3, 4, 6, 7, 10, 13, 22, 23, 24, 25, 26, 45, 69, 99, 121]
Output:  [1, 3, 6, 7, 22, 23, 45, 99]
```

**[Soluzione](src/intersect_sorted.py)**

### Esercizio
Scrivere una funzione in Python che implementa l'algoritmo di ricerca binaria
destra usando la **ricorsione**. In particolare dunque, data una lista $a$ di
numeri ordinati in modo non decrescente ed un numero $k$, la funzione
restituisce la posizione dell'occorrenza più a destra di $k$ in $a$.
Se $k$ non è in $a$, ritorna -1.

**[Soluzione](src/binary_search_recursive.py)**

## Esercizi per casa

### Esercizio

- Scrivere una lambda function che prenda una stringa e restituisce `True`
se la stringa è palindroma, `False` altrimenti;
 
- Scrivere una lambda function che prenda una lista di tuple e restituisca
una lista di tuple ordinate per il secondo elemento di ciascuna tupla;

### Esercizio

Scrivere una funzione in Python che, date due liste `l1` e `l2` **entrambe ordinate**,
restituisce una lista che è la differenza delle due liste `l1` e `l2`,
ovvero, la nuova lista deve contenere tutti gli elementi di `l1` tranne quelli che sono
presenti anche in `l2`.
La soluzione deve avere complessità temporale **lineare** in `len(l1) + len(l2)`, e 
memoria supplementare costante, possibilmente.

*Nota*: considerate le liste come insiemi, ovvero, non ci sono elementi ripetuti.

Esempio:
```
Input:
l1 =  [1, 3, 5, 6, 7, 8, 12, 22, 23, 45, 67, 99, 123]
l2 =  [1, 3, 6, 7, 22, 23, 45, 99]
Output:  [5, 8, 12, 67, 123]
```

### Esercizio

Scrivere una funzione in Python che, date due liste `l1` e `l2` **entrambe ordinate**,
effettua l'operazione di `merge` **in loco**, ovvero senza costruire una nuova lista.
In particolare, se `len(l1) = n` e `len(l2) = m`, allora la funzione deve scrivere in
`l1` i primi `n` elementi più piccoli e in `l2` gli elementi rimanenti.

Esempio:
```python
Input: l1 = [1, 4, 7, 8, 10] l2 = [2, 3, 9]
Output: l1 = [1, 2, 3, 4, 7] l2 = [8, 9, 10]
```

### Esercizio

La [Torre di Hanoi](https://it.wikipedia.org/wiki/Torre_di_Hanoi) è un famoso rompicapo matematico.
Ci sono tre aste e $n$ dischi di diverse dimensioni che possono scorrere su
ogni asta. Inizialmente i dischi sono impilati in ordine crescente di
dimensioni su un'asta, con il più piccolo in cima, a creare una forma conica.
L'obiettivo del puzzle è spostare l'intera pila su un'altra asta, 
rispettando le seguenti semplici regole:

- Si può spostare un solo disco alla volta;
- Ogni spostamento consiste nel prendere il disco superiore da una delle pile 
e metterlo in cima a un'altra pila, cioè un disco può essere spostato solo se
è quello più in alto nella pila;
- Nessun disco può essere posizionato sopra un disco più piccolo.

Il numero minimo di mosse necessarie per risolvere un puzzle della Torre di
Hanoi è $2^n-1$, dove $n$ è il numero totale di dischi.

Scrivere una funzione in Python che risolva il rompicapo: ad esempio, inizialmente
i dischi si trovano tutti sulla prima asta; al termine della funzione, tutti i
dischi devono trovarsi sulla terza asta.
