#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int i, j , k; 
    int rows;
    int spaces;

    int columns = 1;

    printf("Insert an odd number between 3 and 21: ");
    scanf("%d", &rows);

    if (rows > 21 || rows < 3 || rows % 2 == 0)
    {
        printf("Your enter a wrong number: %d \n", rows);
        return 0;
    }

    spaces = rows / 2;

    for (i = 1; i <= rows; i++)
    {
        for (j = 0; j < spaces; j++)
        {
            printf(" ");
        }
        for (k = 0; k < columns; k++)
        {
            printf("*");
        }
        printf("\n");

        if (i < (rows+1)/2)
        {
            columns = columns + 2;
            spaces--;
        }
        else
        {
            columns = columns - 2;
            spaces++;
        }        
    }
    return 0;
}
