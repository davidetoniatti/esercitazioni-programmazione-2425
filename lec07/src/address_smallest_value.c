#include <stdio.h>

int *address_of_smallest_value(int *, int);

int *address_of_smallest_value(int *a, int n) {
  int *smallest = a;

  for (int i = 0; i < n; i++) {
    if (*(a + i) < *smallest)
      smallest = a + i;
  }
  return smallest;
}

int main() {

  int numbers[] = {21, 55, 5, 3, 53};
  int size = sizeof(numbers) / sizeof(int);

  int *smallest = address_of_smallest_value(numbers, size);

  printf("Input: {");
  for (int i = 0; i < size - 1; i++)
    printf("%d, ", numbers[i]);
  printf("%d}\n", numbers[size - 1]);

  printf("Il più piccolo elemento dell'array è: %d, memorizzato all'indirizzo: "
         "%p\n",
         *smallest, smallest);

  return 1;
}
