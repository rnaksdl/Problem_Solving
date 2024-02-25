#include <stdio.h>

int gcd(int a, int b) {
    while (a != b) {
        if (a > b) a = a - b;
        else b = b - a;
    }
    return a;
}
/*/* hi */
int main()
{
    int i = 15, j= 20;
    int test = 3;
    printf("%d",gcd(i, j));
}

