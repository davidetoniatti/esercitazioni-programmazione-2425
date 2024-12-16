#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct array_int {
  int *a;
  int n;
};
typedef struct array_int array_int;

array_int posizione_vocali(char s[]) {
  array_int a = {NULL, 0};
  int n = strlen(s);
  int i, k, j = 0;

  // conto il numero delle vocali
  for (i = 0; i < n; i++) {
    if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' ||
        s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' ||
        s[i] == 'O' || s[i] == 'U')
      a.n = a.n + 1;
  }

  // se ci sono n vocali, dovremo salvare n indici
  a.a = malloc(sizeof(int) * a.n);

  // salviamo questi indici
  for (k = 0; k < n; k++) {
    if (s[k] == 'a' || s[k] == 'e' || s[k] == 'i' || s[k] == 'o' ||
        s[k] == 'u' || s[k] == 'A' || s[k] == 'E' || s[k] == 'I' ||
        s[k] == 'O' || s[k] == 'U') {
      a.a[j] = k;
      j++;
    }
  }

  return a;
}

/*
 * numero di operazioni: lineare (scansiono tutta la stringa due volte, quindi
 * 2n operazioni);
 * la memoria supplementare utilizzata è costante.
 * */
