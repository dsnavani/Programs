#include<stdio.h>

void main()
{
	int square; // Determine the size of the graph
	int i = 1, j = 1;
	int x, y;
	printf("Give the outline size ____ units : ");
	
	square = 50 ;
	for(i = 0; i <= square; i++)
	{
		y = square/2 - i;
		for(j = 0; j <= square; j++)
		{
			x = j-square/2;
			if ( y == 0) 
			{
				if(x <= 0)
					printf("%d ",x);
				else
					printf(" %d ",x);
			}
			else if( j == square/2) 
			{
				if(y < 0)
					printf("%d ",y);
				else if(y >= 0)
					printf(" %d ",y);
			}
			else if(y == x*x) printf(" * ");
			else printf("   ");
		}
		printf(" \n");
	}
}