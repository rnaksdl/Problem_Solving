#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>

/* semaphore key */
#define SHM_KEY 1234
#define SEMKEY ((key_t) 400L)
#define NSEMS 1

/* Global semaphore ID */
int sem_id;

/* Semaphore buffers */
static struct sembuf OP = {0, -1, 0};
static struct sembuf OV = {0, 1, 0};
struct sembuf *P = &OP;
struct sembuf *V = &OV;

/* Semaphore union used to generate semaphore */
typedef union {
    int val;
    struct semid_ds *buf;
    ushort *array;
} semunion;

/* POP (wait) function for semaphore to protect critical section */
int POP() {
    int status;
    status = semop(sem_id, P, 1);
    return status;
}

/* VOP (signal()) function for semaphore to release protection */
int VOP() {
    int status;
    status = semop(sem_id, V, 1);
    return status;
}

struct SharedData {
    int total;
};

void childProcess(int processNumber, struct SharedData* sharedData) {
    /* Define an array that holds the specific target increments for each process */
    int targets[4] = {100000, 200000, 300000, 500000};
    // int targets[4] = {25078, 58334, 108305, 908283};
    // int targets[4] = {25000, 50000, 75000, 950000};
    int increment = targets[processNumber - 1]; // Arrays are 0-indexed
    for (int i = 1; i <= increment; i++) {
        POP();
        sharedData->total++;
        VOP();
    }
    printf("From Process %d: counter = %d.\n", processNumber, sharedData->total);
}

int main() {
    int shmID = shmget(SHM_KEY, sizeof(struct SharedData), IPC_CREAT | 0666);
    if (shmID == -1) {
        perror("shmget");
        exit(1);
    }

    struct SharedData* sharedData = (struct SharedData*)shmat(shmID, NULL, 0);
    if (sharedData == (void*)-1) {
        perror("shmat");
        exit(1);
    }

    sharedData->total = -0;

    /* Create semaphores */
    sem_id = semget(SEMKEY, NSEMS, IPC_CREAT | 0666);
    if (sem_id < 0) {
        printf("Error in creating the semaphore.\n");
        exit(1); /* Exit if semaphore not created */
    }

    /* Initialize semaphore */
    semunion semctl_arg;
    semctl_arg.val = 1;
    int value1 = semctl(sem_id, 0, SETVAL, semctl_arg); /* Updated index to 0 */
    if (value1 < 0) {
        printf("Error detected in SETVAL.\n");
        exit(1); /* Exit if SETVAL failed */
    }

    pid_t childPids[4];
    
    for (int i = 0; i < 4; i++) {
        pid_t child = fork();
        if (child == 0) {
            childProcess(i + 1, sharedData);
            shmdt(sharedData);
            exit(0);
        } else if (child == -1) {
            perror("fork");
            exit(1);
        } else {
            childPids[i] = child;
        }
    }

    int status;
    pid_t pid;
    while ((pid = wait(&status)) > 0) {
        printf("Child with ID %d has just exited.\n", pid);
    }

    printf("End of Program.\n");

    shmdt(sharedData);
    shmctl(shmID, IPC_RMID, NULL);

    /* De-allocate semaphore */
    semctl_arg.val = 0;
    status = semctl(sem_id, 0, IPC_RMID, semctl_arg);
    if (status < 0) {
        printf("Error in removing the semaphore.\n");
    }

    return 0;
}
