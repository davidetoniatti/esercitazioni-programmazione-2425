#include <stdio.h>
#include <stdlib.h>

int *concatenate(int *a, int *b, int n, int m) {
  int total_length = n + m;
  int *c = malloc(sizeof(int) * total_length);

  int j = 0;

  if (c != NULL) {
    for (int i = 0; i < n; i++) {
      c[j] = a[i];
      j++;
    }
    for (int i = 0; i < m; i++) {
      c[j] = b[i];
      j++;
    }
  }
  return c;
}

int main() {
  int a[] = {1, 2, 3, 4, 5};
  int b[] = {6, 7, 8, 9};

  int n = sizeof(a) / sizeof(int);
  int m = sizeof(b) / sizeof(int);

  int *p = concatenate(a, b, n, m);

  for (int i = 0; i < n + m; i++) {
    printf("%d\n", p[i]);
  }
}
