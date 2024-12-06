#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int *a;
  int n;
} array_int;

array_int applica_soglia(int *a_int, int n, int t) {
  array_int x = {NULL, 0};
  int i, j = 0;

  // calcolo il nro di interi < di soglia
  for (i = 0; i < n; i++) {
    if (a_int[i] < t)
      x.n += 1;
  }

  // alloco un array di dimensione pari al nro di interi <= di soglia
  x.a = malloc(sizeof(int) * x.n);

  // copio gli indici degli interi < di soglia all'interno dell'array appena allocato
  for (i = 0; i < n; i++) {
    if (a_int[i] < t) {
      x.a[j] = i;
      j++;
    }
  }

  return x;
}

/*
 * Numero di operazioni: lineare (scansiono tutta la stringa due volte, quindi
 * 2n operazioni).
 * la memoria supplementare utilizzata è costante.
 * */

int main() {
  int b[] = {2, 5, 3, 1, 5, 6, 4, 3, 10, 2};
  int n = sizeof(b) / sizeof(int);
  int t = 5;

  array_int x = applica_soglia(b, n, t);

  for (int i = 0; i < x.n; i++)
    printf("%d\n", x.a[i]);
}
