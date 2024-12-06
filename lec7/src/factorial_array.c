#include <stdio.h>
#include <stdlib.h>

int* factorial_array(int);

int* factorial_array(int n){
  int *p = malloc((n+1)*sizeof(int));

  *p = 1;
  for(int i = 1; i < n+1; i++) {
    p[i] = p[i-1]*i;
  }

  return p;
}


int main() {
  int n = 10;
  int *p = factorial_array(n);

  printf("Output: {");
  for(int i = 0; i < n; i++){
    printf("%d, ", p[i]);
  }
  printf("%d}", p[n]);
}
