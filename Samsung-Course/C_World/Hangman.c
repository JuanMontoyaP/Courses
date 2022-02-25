#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void print_array(char* array, int size)
{
	int i;
	for (i = 0; i < size; i++)
	{
		printf(" %c ", array[i]);
	}
	printf("\n");
}

int different_letters(char array[100], int size)
{
	int i, j, count;
	int letters = 0;

	for (i = 0; i < size; i++)
	{
		count = 0;
		for (j = i+1; j < size; j++)
		{
			if (array[i] == array[j])
			{
				count++;
			}	
		}
		if (count == 0)
		{
			letters++;
		}
	}
	return letters;
}

int main()
{
	int i, j, k;
	int word_length, letters;	
	char letter;

	int tries = 5;
	int guess = 0;

	char player[100];
	char word[100];
	char old_letters[100];

	printf("Type your name: ");
	scanf("%s", player);

	printf("Type the word to guess: ");
	scanf("%s", word);

	word_length = strlen(word);
	char guess_word[word_length];

	for (i = 0; i < word_length; i++)
	{
		guess_word[i] = '_';
	}

	letters = different_letters(word, word_length);
	printf("%d \n", letters);

	while (tries > 0)
	{
		printf("Hiden word \n");
		print_array(guess_word, word_length);
		
		printf("Tries: %d \n", tries);
		
		printf("Enter a letter: ");
		getchar();
		letter = getchar();

		if (strchr(word, letter) && !strchr(old_letters, letter))
		{
			for (i = 0; i < word_length; i++)
			{
				if (word[i] == letter)
				{
					guess_word[i] = letter;
				}
			}

			guess++;

			if (guess == letters)
			{
				printf("YOU WIN! \n");
				print_array(guess_word, word_length);
				break;
			}

			strcat(old_letters, &letter);
		}
		else
		{
			if (strchr(old_letters, letter))
			{
				printf("You already tried this letter: %c \n", letter);
			}
			else
			{
				strcat(old_letters, &letter);
			}
			tries--;
			
			if (tries <= 0)
			{
				printf("You lose, try again! \n");
			}
		}
	}

	FILE *f = fopen("history.txt", "a");
	fprintf(f, "name = %s, word = %s, tries = %d \n", player, word, 6-tries);
	fclose(f);

	return 0;
}
