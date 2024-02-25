#include <stdio.h>

int main() {

    char myName[100];

    printf("Hi, what's your name?\n");
    
    scanf("%s", myName);

    printf("Hi, %s", myName);

    return 0;
}