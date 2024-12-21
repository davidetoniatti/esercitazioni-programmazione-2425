#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *extract_substring(char *, int, int, int);

char *extract_substring(char *a, int n, int i, int j) {
  char *p = malloc(((j-i)+2)*sizeof(char));

  int m = 0;
  for(int k = i; k < j+1; k++) {
    p[m] = a[k];
    m++;
  }

  p[m] = '\0';

  return p;

}

int main() {
  char a[] = "Programmazione dei calcolatori";
  int n = strlen(a);
  char *p = extract_substring(a, n, 4, 18);
  printf("%s\n",p);
}
