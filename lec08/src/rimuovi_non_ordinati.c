#include <stdio.h>
#include <string.h>

void rimuovi_non_ordinati(char *);
void rimuovi_carattere(char *, int);

int main() {
  char a[] = "zddabeceffgfh";
  rimuovi_non_ordinati(a);
  printf("%s\n", a);
}

void rimuovi_carattere(char *a, int index) {
  int n = strlen(a);
  for (int i = index; i < n; i++)
    a[i] = a[i + 1];
}

void rimuovi_non_ordinati(char *a) {
  int i = 0;
  char grande = a[0]; // lettera più grande
  while (a[i] != '\0') {
    if (a[i] >= grande) {
      grande = a[i];
      i++;
    }
    if (a[i] < grande)
      rimuovi_carattere(a, i);
  }
}
