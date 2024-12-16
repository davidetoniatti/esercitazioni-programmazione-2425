# Esercitazione 8 - 06/12/2024

## Svolti in aula

### Esercizio

Scrivere una funzione in C che, dato in input un array di elementi `b` di
lunghezza `n`, crea e restituisce in output una `lista` contenente gli elementi
di `b`.

**[Soluzione](src/lista_from_array.c)**

### Esercizio

Scrivere una funzione in C che, data una stringa `a`, rimuove da `a` tutti i
caratteri che non sono in ordine lessicografico con i precedenti a partire dal
primo simbolo. Dopo l'operazione `a` risulterà ordinata lessicograficamente.

**Attenzione**: non possono essere utilizzate funzioni della libreria `string`
tranne la funzione `strlen()`.

Esempio:

```
Input: char a[] = "ddabeceffgfh"
Ouput: a = "ddeeffgh"
```

```
Input: char a[] = "zhasdrddabeceffgfh"
Ouput: a = "z"
```

**[Soluzione](src/rimuovi_non_ordinati.c)**

### Esercizio

Si consideri la seguente definizione di struttura dati

```c
typedef struct {
    int *a;
    int n;
} array_int;

```

Se `x` è una variabile di tipo `array_int`, allora `x.a` è un puntatore ad un
array di interi e `x.n` è la dimensione di quest'ultimo.
Scrivere una funzione in C che, dato un array di interi `b`, la sua dimensione
`m` e un intero `t` detto **soglia**, restituisce un
`array_int` contenente nel campo `a` gli indici di `b` che contengono un valore
al di sotto della soglia `t`. In altre parole, l'indice `i` di `b` è contenuto
in `x.a` se e soltanto se `b[i] < t`.

Esempio:

```
Input: int b[] = {2,5,3,1,5,6,4,3,10,2}; int n = 10; int t = 5;
Output: x.a = {0,2,3,6,7,9}, x.n = 6
```

**[Soluzione](src/array_soglia.c)**

## Esercizi per casa

### Esercizio

Si consideri la seguente definizione di struttura dati

```c
typedef struct {
    int *a;
    int n;
} array_int;

```

Se `x` è una variabile di tipo `array_int`, allora `x.a` è un puntatore ad un
array di interi e `x.n` è la dimensione di quest'ultimo.
Scrivere una funzione in C che, data una stringa `s`, restituisce un
`array_int` contenente nel campo `a` gli indici delle vocali nella stringa `s`.
In altre parole, la posizione (indice) `i` di `s` è contenuta in `x.a`
se e soltanto se `s[i]` è una vocale.

**Attenzione**: non possono essere utilizzate funzioni della libreria `string`
tranne la funzione `strlen()`.

Esempio:

```
Input: int s[] = "Algoritmi";
Output: x.a = {0,3,5,8}, x.n = 4
```

**[Soluzione](src/posizione_vocali.c)**

### Esercizio

Scrivere una funzione in C che, date in input due stringhe `a` e `b`, crea una
nuova stringa che è la **concatenazione** delle due stringhe.
In particolare, se `a` precede o è uguale a `b`, allora la concatenazione deve
avere prima la stringa `a` e poi `b`; viceversa, se `b` precede `a`, allora la
concatenazione deve avere prima la stringa `b` e poi `a`.

Esempio:

```
Input: char *a = "prolog", char *b = "programmazione"
Output: char *p = "programmazioneprolog"
```

**[Soluzione](src/concatenate_string.c)**

### Esercizio

Scrivere una funzione in C che, data in input una stringa `a`, la sua lunghezza
`n` e due interi `i, j` con `i <= j`, crea una nuova stringa che è la
**sottostringa** di `a` compresa tra gli indici `i` e `j`. La funzione ritorna
l'indirizzo in cui è memorizzata la stringa appena creata in questo modo.

Esempio:

```
Input: char *a = "Programmazione dei calcolatori", int n = , int i = 4, int j = 18
Output: char *p = "rammazione dei"
```

**[Soluzione](src/extract_substring.c)**
