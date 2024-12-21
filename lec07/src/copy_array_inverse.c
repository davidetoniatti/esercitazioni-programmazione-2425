#include <stdio.h>
#include <stdlib.h>

float *copy_invert_array(float *a, int n) {
  float *p = malloc(n * sizeof(float));
  if (p == NULL)
    return NULL;

  float tmp = 0;
  for (int i = 0; i < n; i++) {
    p[i] = a[n - 1 - i];
  }

  return p;
}

int main() {
  float a[] = {1.4, 2.3, 2.33, 5.66, 1, 4.5};
  int n = sizeof(a) / sizeof(float);

  float *p = copy_invert_array(a, n);

  for (int i = 0; i < n-1; i++) {
    printf("%2.2f, ", p[i]);
  }
  printf("%2.2f\n", p[n-1]);
}
