#include <stdio.h>
#include <string.h>

int rimuovi_stringa(char *, char *);

int main() {
  char a[] = "azioneprogrammazione dei calcolatoriazione";
  char b[] = "azione";

  printf("%d\n", rimuovi_stringa(a, b));
  printf("%s\n", a);
}

int rimuovi_stringa(char *a, char *b) {
  int n = strlen(a);
  int m = strlen(b);
  int corr;
  int i = 0;
  int res = 0;

  while (a[i] != '\0') {
    corr = 0;

    if (a[i] == b[0]) {
      corr = 1;
      for (int j = 1; j < m && corr == 1; j++) {
        if (a[i + j] == b[j])
          corr = 1;
        else
          corr = 0;
      }
    }

    if (corr == 1) {
      res = 1;
      for (int k = i; k <= (n - m); k++)
        a[k] = a[k + m];
    } else {
      i++;
    }
  }

  return res;
}
