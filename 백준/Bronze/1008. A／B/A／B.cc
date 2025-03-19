#include <stdio.h>

int main(void) {
    int a, b;
    double c;

    scanf("%d %d", &a, &b);
    c = (double)a / (double)b;
    printf("%.15f", c);

    return 0;
}