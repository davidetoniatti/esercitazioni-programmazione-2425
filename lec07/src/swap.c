#include <stdio.h>

int swap(int *, int *, int *);

int swap(int *a, int *b, int *c) {
  int tmp = 0;

  if (*a > *b) {
    tmp = *a;
    *a = *b;
    *b = tmp;
  }

  if (*b > *c) {
    tmp = *b;
    *b = *c;
    *c = tmp;
  }

  if (*a > *b) {
    tmp = *a;
    *a = *b;
    *b = tmp;
  }

  return 1;
}

int main() {
  int a = 8;
  int b = 7;
  int c = 7;
  swap(&a, &b, &c);
  printf("%d, %d, %d\n", a, b, c);
}
