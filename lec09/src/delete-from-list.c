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
lista pop(lista);
lista delete(lista, int);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char *);

lista delete(lista L, int p) {

  if (p < 0)
    p = 0;
  if (p > L.n)
    p = L.n;

  elemento e = L.a[p];

  for (int i = p + 1; i < L.n; i++) {
    L.a[i - 1] = L.a[i];
    L.a[i] = e;
  }

  L = pop(L);

  return L;
}

/**************************************************
****** funzioni ausiliarie per le liste ***********
**************************************************/

lista init() {
  lista lista_vuota = {NULL, 0, 0};
  return lista_vuota;
}

lista append(lista L, elemento e) {
  if (L.n == L.c) {
    L.c = 2 * (L.c + 1);
    L.a = realloc(L.a, L.c * sizeof(elemento));
  }
  L.a[L.n] = e;
  L.n++;
  return L;
}

lista pop(lista L) {
  if (L.n > 0) {
    L.n--;
    if (L.n < L.c / 4) {
      L.c = L.c / 2;
      L.a = realloc(L.a, (L.c) * sizeof(elemento));
    }
    if (L.a[L.n].tipo != 's')
      free(L.a[L.n].dato);
  }
  return L;
}

void stampa(lista L) {
  for (int i = 0; i < L.n; i++) {
    switch (L.a[i].tipo) {
    case 'i':
      printf("%d: %d\n", i, *((int *)L.a[i].dato));
      break;
    case 'f':
      printf("%d: %f\n", i, *((float *)L.a[i].dato));
      break;
    case 's':
      printf("%d: %s\n", i, (char *)L.a[i].dato);
      break;
    }
  }
}

elemento intero(int d) {
  elemento e = {'i', NULL};

  e.dato = malloc(sizeof(int));
  *(int *)(e.dato) = d;

  return e;
}

elemento fpoint(float d) {
  elemento e = {'f', NULL};

  e.dato = malloc(sizeof(float));
  *(float *)(e.dato) = d;

  return e;
}

elemento stringa(char *c) {
  elemento e = {'s', NULL};

  e.dato = c;

  return e;
}
