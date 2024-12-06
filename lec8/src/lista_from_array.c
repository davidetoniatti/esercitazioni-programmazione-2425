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
lista init_array(elemento *, int);
lista append(lista, elemento);
void stampa(lista);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char *);

/*
 *
 * funzione richiesta dall'esercizio
 *
 * */
lista init_array(elemento *b, int n) {
  lista L = init();
  L.n = n;
  L.c = 2 * (n + 1);
  L.a = malloc(L.c * sizeof(elemento));
  for (int i = 0; i < n; i++)
    L.a[i] = b[i];
  return L;
}
/*
 *
 *
 * */

int main() {
  elemento a[] = {intero(10), stringa("ciao"), fpoint(3.14)};
  int n = sizeof(a) / sizeof(elemento);
  lista L = init_array(a, n);
  stampa(L);
  L = append(L, fpoint(2.71));
  stampa(L);
}

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

void stampa(lista L) {
  int i;

  printf("==================================\n");

  for (i = 0; i < L.n; i++) {
    switch (L.a[i].tipo) {
    case 'i':
      printf("%d\n", *((int *)L.a[i].dato));
      break;
    case 'f':
      printf("%f\n", *((float *)L.a[i].dato));
      break;
    case 's':
      printf("%s\n", (char *)L.a[i].dato);
      break;
    }
  }

  printf("dimensione %d, capacita' %d\n", L.n, L.c);
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
