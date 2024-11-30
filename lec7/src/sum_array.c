#include <stdio.h>
#include <stdlib.h>

int *sum_array(int *a, int m, int n) {
  int *p = malloc((m + n) * sizeof(int));

  if (p == NULL)
    return NULL;

  for (int i = 0; i < m; i++) {
    p[i] = a[i];
    p[m] += a[i];
  }

  for (int i = m + 1; i < m + n; i++) {
    p[i] = p[i - 1] * 2;
  }

  return p;
}

int main() {
  int a[] = {1, 2, 3};
  int m = sizeof(a) / sizeof(int); // numero di elementi in a
  int n = 5;
  int *res = sum_array(a, m, n);
  for (int i = 0; i < m + 5; i++) {
    printf("%d ", res[i]);
  }
  printf("\n");
}
