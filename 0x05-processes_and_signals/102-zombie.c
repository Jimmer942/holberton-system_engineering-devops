#include <stdlib.h>
#include<stdio.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - infinite loop.
 * Return: 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Program that creates a zombie process
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t ZOMBIE_PID;

	for (i = 0; i < 5; i++)
	{
		ZOMBIE_PID = fork();
		if (ZOMBIE_PID > 0)
			printf("Zombie process created, PID: %i\n", ZOMBIE_PID);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
