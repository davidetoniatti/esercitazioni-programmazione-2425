#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *concatenate_string(char *a, char *b) {
  int n = strlen(a);
  int m = strlen(b);
  int total_length = n + m;
  char *p = malloc(sizeof(int) * total_length+1);

  int j = 0;
  
  if(strcmp(a, b) > 0) {
    char* tmp = a;
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

int main() {
  char b[] = "programmazione";
  char a[] = "prolog";

  char *p = concatenate_string(a, b);
  
  printf("%s\n", p);
}
