#define _REENTRANT
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <fcntl.h>

#define BUFFER_SIZE 15
#define END_MARKER '*'

// Circular buffer and its control variables
char buffer[BUFFER_SIZE];
int in = 0;
int out = 0;

// Semaphores
sem_t full;
sem_t empty;
sem_t mutex;

void* producer(void* param) {
    FILE* fp = fopen("mytest.dat", "r");
    if (fp == NULL) {
        perror("Error opening file");
        exit(1);
    }

    char newChar;
    while (fscanf(fp, "%c", &newChar) != EOF) {
        sem_wait(&empty);
        sem_wait(&mutex);

        buffer[in] = newChar;
        in = (in + 1) % BUFFER_SIZE;

        sem_post(&mutex);
        sem_post(&full);
    }

    // Signal EOF to consumer
    sem_wait(&empty);
    sem_wait(&mutex);

    buffer[in] = END_MARKER;
    in = (in + 1) % BUFFER_SIZE;

    sem_post(&mutex);
    sem_post(&full);

    fclose(fp);
    pthread_exit(0);
}

void* consumer(void* param) {
    char item;
    while (1) {
        sem_wait(&full);
        sem_wait(&mutex);

        item = buffer[out];
        out = (out + 1) % BUFFER_SIZE;

        sem_post(&mutex);
        sem_post(&empty);

        if (item == END_MARKER) {
            break;
        }

        printf("%c", item);
        sleep(0.5); // Slow down consumer
    }
    pthread_exit(0);
}

int main() {
    pthread_t tid1, tid2;

    // Initialize semaphores
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
    sem_init(&mutex, 0, 1);

    // Create producer and consumer threads
    pthread_create(&tid1, NULL, producer, NULL);
    pthread_create(&tid2, NULL, consumer, NULL);

    // Wait for the threads to finish
    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);

    // Clean up
    sem_destroy(&empty);
    sem_destroy(&full);
    sem_destroy(&mutex);

    return 0;
}
