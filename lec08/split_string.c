#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *extract_substring(char *, int, int, int);

char *extract_substring(char *a, int n, int i, int j) {
  char *p = malloc(((j - i) + 2) * sizeof(char));

  int m = 0;
  for (int k = i; k < j + 1; k++) {
    p[m] = a[k];
    m++;
  }

  p[m] = '\0';

  return p;
}

char **string_split(char *a, int n) {
  int words_count = 0;
  int i = 0;
  while (a[i] != '\0') {
    if (a[i] == ' ') {
      words_count++;
    }
    i++;
  }

  // conta ultima parola
  words_count++;

  int words_start_pos[words_count];
  words_start_pos[0] = 0;

  int j = 1;
  i = 0;
  while (a[i] != '\0') {
    if (a[i] == ' ') {
      words_start_pos[j] = i + 1;
      j++;
    }
    i++;
  }

  char **p = malloc(words_count * sizeof(char *));

  for (j = 0; j < words_count - 1; j++)
    p[j] =
        extract_substring(a, n, words_start_pos[j], words_start_pos[j + 1] - 2);
  p[j] = extract_substring(a, n, words_start_pos[j], n - 1);

  return p;
}

int main() {
  char a[] = "programmazione dei calcolatori con laboratorio viva il duce";
  int n = strlen(a);
  char **p = string_split(a, n);

  for (int i = 0; i < 8; i++) {
    printf("%s\n", p[i]);
  }
}
