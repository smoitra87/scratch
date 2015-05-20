#include<stdio.h>

int main(int argc, char *argv[]) {

	int numbers[4] = {0};
	char name[4] = {'a', 'a', 'a', 'a'};
	name[3] = 'A';

	printf("numbers: %d %d %d %d\n",
			numbers[0], numbers[1],
			numbers[2], numbers[2]);

	printf("name: %c %c %c %c\n",
			name[0], name[1],
			name[2], name[3]);

	printf("name: %s\n", name);

	//setup the numbers
	numbers[0] = 1;
	numbers[1] = 2;
	numbers[2] = 3;
	numbers[3] = 4;

	// setup the name
	name[0] = 1;
	name[1] = 1;
	name[2] = 1;
	name[3] = '\0';

	// then print them out initialized
	printf("numbers: %c %c %c %c\n",
			numbers[0], numbers[1],
			numbers[2], numbers[3]);

	printf("name each: %c %c %c %c\n",
			name[0], name[1],
			name[2], name[3]);

	printf("name: %s\n", name);

	char *another = "Zed";
	int *another_number = {1,2,3,4};

	printf("another: %s\n", another);

	printf("another each: %c %c %c %c \n",
		another[0], another[1],
		another[2], another[3]);

	printf("another_number each: %d %d %d %d \n",
		another_number[0], another_number[1],
		another_number[2], another_number[3]);

	return 0;
}
