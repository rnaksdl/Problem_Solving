#include <stdio.h>

int main() {
	char myName[100];
	printf("What is your name?\n");
	scanf("%s", myName);

	printf("hello %s\n", myName);

	return 0;
}