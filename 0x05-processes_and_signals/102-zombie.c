#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - Initializes an infinite while loop.
 *
 * Return: 0 if interrupted by a signal.
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
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t pid;
	char count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
