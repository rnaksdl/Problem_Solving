#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

/*
	Defining SumArgs struct to share necessary data in between threads
	'start' and 'end' will be each thread's starting and ending point
	and each will calculate sum and store the result in 'sum'.
*/
typedef struct {
    int start;
    int end;
    int sum;
} SumArgs;

/*
	sum calculation function
	it takes SumArgs object of the thread it's on and calculates the sum of numbers in bewteen 'start' and 'end inclusivly
	then updates the sum of SumArgs with the calculated sum
*/
void* sum_calc(void* args) {
    SumArgs* sum_args = (SumArgs*) args;
    int start = sum_args->start;
    int end = sum_args->end;
    int sum = 0;

    for (int i = start; i <= end; ++i) {
        sum += i;
    }

    sum_args->sum = sum;

    return NULL;
}

/*
	main method
	creats 10 threads and thread args and let them calculate the each sums
	(the numer is in between 0 and 9999)
	then calculate the sum of sums and outputs the result
*/
int main() {
    const int num_threads = 10;
    pthread_t threads[num_threads];
    SumArgs thread_args[num_threads];
    int total_sum = 0;

    for (int i = 0; i < num_threads; ++i) {
        thread_args[i].start = i * 1000;
        thread_args[i].end = (i + 1) * 1000 - 1;
        pthread_create(&threads[i], NULL, sum_calc, &thread_args[i]);
    }

    for (int i = 0; i < num_threads; ++i) {
        pthread_join(threads[i], NULL);
        total_sum += thread_args[i].sum;
    }

    printf("Total Sum: %d\n", total_sum);

    return 0;
}
