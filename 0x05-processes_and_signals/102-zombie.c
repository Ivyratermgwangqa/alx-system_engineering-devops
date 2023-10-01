#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * main - Creates 5 zombie processes
 *
 * Return: Always 0
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		pid_t child_pid = fork();
		
		if (child_pid == 0)
		{
			exit(0);
		}
		else if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
		}
		else
		{
			perror("Fork failed");
			exit(1);
		}
	}
	return (0);
}
