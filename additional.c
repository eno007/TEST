#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	long int a,sum = 0;
	int i;

	a = atoi(argv[i]);
	for(i = 1; i <= argc; i++)
		sum =+ a;
	
	printf("Sum of %ld; is: %ld\n",a,sum);
	
	return 0;
}
