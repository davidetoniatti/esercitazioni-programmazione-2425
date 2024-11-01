# Esercitazione 1

## Svolti in aula

### Esercizio 1
Scrivere un programma che date due stringe in input, in output stampa solo i
caratteri che la prima stringa ha in comune con la seconda stringa.
Utilizzare le funzioni.

**[Soluzione](src/filter.py)**

### Esercizio 2
Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori
positivi, escluso sé stesso. Scrivere una funzione che verifichi se un numero è
perfetto oppure no.

**[Soluzione](src/perfetto.py)**

### Esercizio 3
Il [ROT-13](https://en.wikipedia.org/wiki/ROT13) è un semplice cifrario monoalfabetico,
in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta
13 posizioni più avanti nell'alfabeto.

Scrivere una funzione in grado di criptare, usando il cifrario ROT-13 una stringa in input. 

_Nota: utilizzare l'alfabeto inglese (26 lettere) e per semplicità considerare
solamente le lettere minuscole (no maiuscole o numeri)._

**[Soluzione](src/rot13.py)**

## Esercizi per casa

### Esercizio 1
Scrivere una funzione che, data in input una stringa criptata usando il cifrario
ROT-13, decripta la stringa e restituisce in output la stringa decriptata.

Esempio: data in input la stringa
```
cebtenzznmvbar qrv pnypbyngbev
```
la funzione deve restituire in output la stringa
```
programmazione dei calcolatori
```
_Nota: utilizzare l'alfabeto inglese (26 lettere) e per semplicità considerare
solamente le lettere minuscole (no maiuscole o numeri)._

*Suggerimento: è sufficiente fare qualche modifica al codice scritto per
risolvere l'esercizio 3.*

**[Soluzione](src/rot13-decrypt.py)**

### Esercizio 2
Il [Cifrario di Cesare](https://en.wikipedia.org/wiki/Caesar_cipher) è un
cifrario a sostituzione monoalfabetica, in cui ogni lettera del messaggio
è sostituita, nel testo cifrato, dalla lettera posta $k$ posizioni più avanti
nell'alfabeto. Il numero $k$ è detto **chiave**. 

Scrivere una funzione che, data in input la chiave $k$ e una stringa, ritorna
in output una stringa criptata secondo il cifrario di Cesare con chiave $k$.

Scrivere inoltre una funzione che, data in input la chiave $k$ e una stringa
criptata (con chiave $k$), ritorna in output la stringa decriptata.

_Nota: utilizzare l'alfabeto inglese (26 lettere) e per semplicità considerare
solamente le lettere minuscole (no maiuscole o numeri)._

*Suggerimento: sembra più semplice risolvere l'esercizio usando l'aritmeitca
modulare, come abbiamo fatto per l'esercizio 3.*

**[Soluzione](src/caesar-cipher.py)**

### Esercizio 3
La [Congettura di Collatz](https://en.wikipedia.org/wiki/Collatz_conjecture) è
una congettura matematica tuttora irrisolta. Fu enunciata per la prima volta
nel 1937 da Lothar Collatz, da cui prende il nome.

La congettura riguarda il seguente algoritmo:

1. Si prende un intero positivo $n$;
2. Se $n=1$, l'algoritmo termina;
3. Se $n$ è pari, si divide per due; altrimenti si moltiplica per $3$ e si
   aggiunge $1$

La congettura di Collatz asserisce che questo algoritmo giunge **sempre a termine**,
indipendentemente dal valore di partenza.

Scrivere una funzione che, dato un intero $n$ in input, restituisce il numero di
iterazioni necessarie affinché l'algoritmo termini, cioè dopo quante iterazioni
risulta $n=1$.

Esempio: per $n=6$, allora abbiamo la successione

$$
6,3,10,5,16,8,4,2,1
$$

dunque l'algoritmo termina dopo $8$ iterazioni.

**[Soluzione](src/collatz.py)**
