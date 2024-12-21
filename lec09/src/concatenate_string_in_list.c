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
void stampa(lista);
int concatenate_string_list(lista, char *);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char *);

int main() {
  elemento l[] = {intero(2),    fpoint(3.4),     stringa("python"), intero(77),
                  stringa("C"), stringa("java"), intero(23)};
  lista L = init_array(l, sizeof(l) / sizeof(elemento));
  char s[] = "linguaggio";

  int modified = concatenate_string_list(L, s);

  printf("modified: %d\n", modified);
  stampa(L);
}

char *concatenate_string(char *a, char *b) {
  int n = strlen(a);
  int m = strlen(b);
  int total_length = n + m;
  char *p = malloc(sizeof(int) * total_length + 1);

  int j = 0;

  if (strcmp(a, b) > 0) {
    char *tmp = a;
    a = b;
    b = tmp;
    int tmp2 = n;
    n = m;
    m = tmp2;
  }

  if (p != NULL) {
    for (int i = 0; i < n; i++) {
      p[j] = a[i];
      j++;
    }
    for (int i = 0; i < m; i++) {
      p[j] = b[i];
      j++;
    }
  }
  p[j] = '\0';

  return p;
}

int concatenate_string_list(lista L, char *s) {
  int modified = 0;
  for (int i = 0; i < L.n; i++) {
    if (L.a[i].tipo == 's') {
      modified += 1;
      char *p = concatenate_string(L.a[i].dato, s);
      L.a[i].dato = p;
    }
  }
  return modified;
}

/**************************************************
****** funzioni ausiliarie per le liste ***********
**************************************************/

lista init() {
  lista lista_vuota = {NULL, 0, 0};
  return lista_vuota;
}

lista init_array(elemento *b, int n) {
  lista L = init();
  L.n = n;
  L.c = 2 * (n + 1);
  L.a = malloc(L.c * sizeof(elemento));
  for (int i = 0; i < n; i++)
    L.a[i] = b[i];
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
