# Esercitazione 7

## Svolti in aula

### Esercizio
Scrivere una funzione in C che, date tre varibili intere `a`, `b` e `c`,
**scambia** gli interi contenuti in queste variabile in modo che 
`a <= b <= c`.

Esempio:
``` 
Input: int a = 5; int b = 7; int c = 2;
dopo l'esecuzione della funzione, si deve ottenere che
Output: a = 2; b = 5; c = 7;
```

**[Soluzione](src/swap.c)**

### Esercizio
Scrivere una funzione in C che, dato un array di interi `a` e la sua
dimensione `n`, restituisce l'**indirizzo** del più piccolo elemento
contenuto in `a`.

Esempio:
```
Input: {21, 55, 5, 3, 53}
Output: Il più piccolo elemento dell'array è: 3,
        memorizzato all'indirizzo: 0x7ffe881412bc.
```

**[Soluzione](src/address_smallest_value.c)**

### Esercizio
Scrivere una funzione in C che, dato un array di lunghezza $m$ di interi
e un intero $n$, crea un array di lunghezza $m+n$ che contiene:

- nelle prime $m$ posizioni, gli interi contenuti nell'array in input nello
stesso ordine;
- in ognuna delle $m+1 \leqslant i \leqslant m+n$ posizioni successiva, la somma di tutti
gli interi nelle posizioni precedenti ad $i$;

Esempio:
```
Input: {1,2,3},3,5
Output: {1,2,3,6,12,24,48,96}
```

**[Soluzione](sum_array.c)**

## Esercizi per casa

### Esercizio
Scrivere una funzione in C che, dato un'array `a` di `float` di lunghezza `n`,
crea un'array che è l'**inverso** di `a`, ossia, il nuovo array memorizza gli
elementi di `a` al contrario.

Esempio:
```
Input: {1.4, 2.3, 2.33, 5.66, 1, 4.5}
Output: {4.5, 1, 5.66, 2.33, 2.3, 1.4}
```

**[Soluzione](src/copy_array_inverse.c)**

### Esercizio
Scrivere una funzione in C che, dati due array `a` e `b` di `int` di lunghezza
rispettivamente `n` e `m`, crea un'array che è la **concatenazione** di `a` e `b`,
ossia, il nuovo array memorizza prima gli elementi di `a` e, a seguire, gli
elementi di `b`.

Esempio:
```
Input: int a[] = {1, 2, 3, 4, 5}; int b[] = {6, 7, 8, 9};
Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

**[Soluzione](src/concatenate.c)**

### Esercizio
Scrivere una funzione in C che, dato un'intero `n`, crea un'array di
interi tale che nella posizione `0 <= i <= n` è contenuta il valore di
`i!`, ovvero il fattoriale di `i`.

Esempio:
```
Input: int n = 5
Output: {1, 1, 2, 6, 24, 120}
```
dove in posizione `0` è memorizzato `0! = 1`, in posizione `1` è memorizzato
`1! = 1`, in posizione `2`: `2! = 2`, in posizione `3`: `3! = 6`,... e cosi via.

**[Soluzione](src/factorial_array.c)**
