# Esercitazione 9 - 13/12/2024

## Svolti in aula (online)

### Esercizio

Scrivere una funzione in C che, data in input una `lista L` e un indice `p`,
elimina l'elemento in posizione `p` di `L`. In output, restituisce `L`.

**[Soluzione](src/delete-from-list.c)**

### Esercizio

Scrivere una funzione in C che, dati in input due array di interi `a` e `b`,
ordinati in ordine non decrescente, crea una `lista L` contenente gli elementi
nell'**unione** di `a` e di `b`.

Esempio:

```
Input:  int a[] = {2, 5, 6, 8, 8, 8, 8, 10, 12, 13};
        int b[] = {0, 0, 0, 1, 2, 3, 4, 5, 6, 13, 14};
Output: L = {0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 14};
```

**[Soluzione](src/union.c)**

### Esercizio

Scrivere una funzione in C che, date in input due stringhe `a` e `b`, rimuove
`b` da `a` nel caso in cui `b` sia **sottostringa** di `a`. La funzione deve
restituire `0` se `b` non è sottostringa di `a`, `1` altrimenti.

Esempio:

```
Input: a[] = "programmazionedei calcolatori"; b[] = "azione";
Output: return 1; a[] = "programm dei calcolatori"
```

**[Soluzione](src/remove-string.c)**

## Esercizi per casa

### Esercizio

Scrivere una funzione in C che, dati in input due array di interi `a` e `b`
ordinati in ordine non decrescente, crea una `lista L` contenente gli elementi
nell'**intersezione** di `a` e di `b`.

Esempio:

```
Input:  int a[] = {2, 5, 6, 8, 8, 8, 8, 10, 12, 13};
        int b[] = {0, 0, 0, 1, 2, 3, 4, 5, 6, 13, 14};
Output: L = {2, 5, 6, 13};
```

**[Soluzione](src/intersect.c)**

### Esercizio

Scrivere una funzione in C che, dati in input una `lista L` e una stringa `s`,
modifica la lista `L` nel modo seguente: per ogni stringa `s'` contenuta in
`L`, la funzione deve **concatenare** le due stringhe `s` e `s'`.
In particolare, se `s'` precede o è uguale a `s`, allora la
concatenazione deve avere prima la stringa `s'` e poi `s`; viceversa, se
`s` precede `s'`, allora la concatenazione deve avere prima la stringa `s` e poi
`s'`.
La funzione deve ritornare il numero di elementi modificati nella lista `L`.

Esempio:

```
Input: lista L = {2, 3.4, "python", 77, "C", "java", 23};
        char s[] = "linguaggio";
Output: lista L = {2, 3.4, "linguaggiopython", 77, "Clinguaggio", "javalinguaggio", 23}
```

**[Soluzione](src/concatenate_string_in_list.c)**
