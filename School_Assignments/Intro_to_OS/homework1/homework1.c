#include <stdio.h>
#include <stdlib.h>

/*
[Declaring a function]
Declare a function with two integer parameters,
which calculates and returns the multiple of the two numbers. 
*/
int multiply(int num1, int num2);

int main() {

	int userArrSize;

	printf("Start program.\n");
	printf("Input array size: ");
	scanf("%d", &userArrSize);
	printf("\n");

/*
[Arrays and pointers]
Declare two integer arrays with the same size
using pointers and dynamic memory allocation.
The size should be determined by a user’s input.
*/
	int *arr1 = (int *)malloc(userArrSize * sizeof(int));
	if (arr1 == NULL) {
		printf("Memory allocation failed for arr1.\n");
		return 1;
	}

	int *arr2 = (int *)malloc(userArrSize * sizeof(int));
	if (arr2 == NULL) {
		printf("Memory allocation failed for arr2.\n");
		return 1;
	}

/*
[Pointer]
Print the address of the first array. 
*/
	printf("Address of arr1 after allocation: %p", (void *)arr1);

/*
[Address space]
Try the operator sizeof and print size of the first array pointer.
Compare with the above one and think about the reason. 
*/
	printf("Size of pointer arr1:%zu", sizeof(arr1));

/*
[Loop and array]
Use the array size provided by the user and
assign an integer value to the array’s element.
Again, each integer value must be provided by the user.
Repeat the procedure to fill both arrays we declared.
*/
	printf("Input content of arr1:\n");
	for(int i = 0; i < userArrSize; i++) {
		printf("Enter value of arr1[%d]: ", i);
		scanf("%d", &arr1[i]);
		printf("\n");

	}
	printf("Input content of arr2:\n");
	for(int i = 0; i < userArrSize; i++) {
		printf("Enter value of arr2[%d]: ", i);
		scanf("%d", &arr2[i]);
		printf("\n");
		
	}

	printf("Multiplication start.\n");

	printf("Multiplication done.\n");

/*
[Calculation, condition statements, and file write]
Using the function we declared,
multiply i-th element of the first array by i-th element of the second array.
For each result, check if the multiplication result is an even or odd number
using condition statements.
Declare a file pointer and write the multiplication results in the new file
named “hw1_output.txt”.
Once the file write is done,
do not forget to close the file.
*/
	FILE *file = fopen("hw1_output.txt", "w");
	if (file == NULL) {
		printf("Error opening the file.\n");
		free(arr1);
		free(arr2);
		return 1;
	}

	for (int i = 0; i < userArrSize; i++) {
		int result = multiply(arr1[i], arr2[i]);
		const char *evenOdd = (result % 2 == 0) ? "even" : "odd";
		fprintf(file, "arr[%d] * arr2[%d] = %d\n\n", i, i, result);
		fprintf(file, "\t\t%d is an %s numer\n\n", result, evenOdd);

	}

	fclose(file);

/*
[File read]
Open “hw1_output.txt” file in your program,
read, and print the content of the file. Again,
please close the file.
*/
	printf("Read file.\n");

	file = fopen("hw1_output.txt", "r");
	if (file == NULL) {
		printf("Error opening the file.\n");
		return 1;
	}

	char character;
	while ((character = fgetc(file)) != EOF) {
		putchar(character);
	}

	fclose(file);

	free(arr1);
	free(arr2);

return 0;

}


int multiply(int num1, int num2) {
    return num1 * num2;
}