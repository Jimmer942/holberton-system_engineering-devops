#include <stdlib.h>
#include<stdio.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * main - Program that creates a zombie process
 * Return: 0
 */
int main(void)
{
	pid_t ZOMBIE_PID;

	while (1)
	{
		ZOMBIE_PID = fork();
		if (ZOMBIE_PID > 0)
		{
			printf("Zombie process created, PID: %i\n", ZOMBIE_PID);
			sleep(1);
		}
		else
			exit(0);
	}
	return (0);
}
