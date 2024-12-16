#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  char tipo; // 'i' intero; 'f' float; 's' stringa
  void *dato;
} elemento;

typedef struct {
  elemento *a;
  int c;
  int n;
} lista;

lista init();
lista append(lista, elemento);
void stampa(lista);
lista insert(lista, elemento, int);
lista unione(int *, int, int *, int);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char *);

lista unione(int *a, int n, int *b, int m) {
  lista L = init();
  int i = 0, j = 0;

  while (i < n && j < m) {
    if (a[i] <= b[j]) {
      if (L.n == 0 || (L.n > 0 && *(int *)L.a[L.n - 1].dato != a[i]))
        L = append(L, intero(a[i]));
      i += 1;
    } else {
      if (L.n == 0 || (L.n > 0 && *(int *)L.a[L.n - 1].dato != b[j]))
        L = append(L, intero(b[j]));
      j += 1;
    }
  }

  while (i < n) {
    if (L.n == 0 || (L.n > 0 && *(int *)L.a[L.n - 1].dato != a[i]))
      L = append(L, intero(a[i]));
    i += 1;
  }

  while (j < m) {
    if (L.n == 0 || (L.n > 0 && *(int *)L.a[L.n - 1].dato != b[j]))
      L = append(L, intero(b[j]));
    i += 1;
  }

  return L;
}
