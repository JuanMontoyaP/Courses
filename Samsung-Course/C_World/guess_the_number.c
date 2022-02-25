#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	srand(time(NULL));

	int tries = 1;
	int guess = 0;
	int keep_playing = 0;
	int random_number, input_number;

	random_number = 1 + (rand() % 100);

	while (guess == 0)
	{
		printf("Introduce your number: ");
		scanf("%d", &input_number);
			
		if (input_number != random_number)
		{
			tries++; 
			
			if (input_number < random_number)
			{
				printf("Your number is less than the number \n");
			}
			else
			{
				printf("Your number is greather than the number \n");
			}
		}
		else 
		{
			printf("YOU GUESS!! \nYou tried %d times \n", tries);
			
			printf("Press 1 if you want to keep playing, otherwise press 0 \n");
			scanf("%d", &keep_playing);
			if (keep_playing == 1)
			{
				random_number = 1 + (rand() % 100);
				tries = 1;
			}
			else
			{
				guess = 1;
			}
		}
	}
	return 0;
}