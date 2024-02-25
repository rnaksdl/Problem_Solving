/*
CS 3113 (Dr. Fang)
Programming Assignment 1
Author: Kyumin Lee
Date: 09.28.2023
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/shm.h>
 
/*
Define the total shared memory key
*/
#define SHM_KEY 1234

/*
Structure to hold shared data
*/
struct SharedData {
	int total;
};


/*
Function to simulate the process for each child
*/
void childProcess(int processNumber, struct SharedData* sharedData) {
	/*
	Each child will have processNumber
	and it'll get multiplied to 100,000.
	For loop to increment by 1 to the desired value
	Then print value
	*/
	int increment = processNumber * 100000;
	for (int i = 1; i <= increment; i++) {
	sharedData->total++;
	}
	printf("From Process %d: counter = %d.\n", processNumber, sharedData->total);
}

int main() {
	/*
	Create shared memory
	*/
	int shmID = shmget(SHM_KEY, sizeof(struct SharedData), IPC_CREAT | 0666);

	/*
	Error detection
	*/
	if (shmID == -1) {
		perror("shmget");
		exit(1);
	}

	/*
	Attach shared memory
	*/
	struct SharedData* sharedData = (struct SharedData*)shmat(shmID, NULL, 0);
	/*
	Error detection
	*/
	if (sharedData == (void*)-1) {
    	perror("shmat");
    	exit(1);
	}

	/*
	Initialize the shared variable
	*/
	sharedData->total = 0;

	/*
	Array to store child PIDs
	*/
	pid_t childPids[4];
	
	/*
	Create four child processes
	*/
	for (int i = 0; i < 4; i++) {
		pid_t child = fork();

		/*
		if created
		*/
		if (child == 0) {
			/*
			We are in child process now.

			Pass 1-based process number
			*/
			childProcess(i + 1, sharedData);
			/*
			Detach shared memory
			*/
			shmdt(sharedData);
			/*
			Exit the child process
			*/
			exit(0);

		/*
		Error detection
		*/
		} else if (child == -1) {
			perror("fork");
			exit(1);
		
		
		} else {
			/*
			We are in the parent process
			Store the child PID in the array
			*/
			childPids[i] = child;
		}
	}

	/*
	Wait for all child processes to finish
	*/
	for (int i = 0; i < 4; i++) {
		int status;
		waitpid(childPids[i], &status, 0);
	}

	/*
	Print the "exited" lines after all children have exited
	*/
	for (int i = 0; i < 4; i++) {
		printf("Child with ID: %d has just exited.\n", childPids[i]);
	}

	/*
	Print the final result
	*/
	printf("End of Simulation.\n");

	/*
	Release shared memory
	*/
	shmdt(sharedData);
	shmctl(shmID, IPC_RMID, NULL);

	return 0;
}
