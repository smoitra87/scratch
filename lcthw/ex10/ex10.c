#include<stdio.h>

int main(int argc, char *argv[]) {

	int i = 0;
	
	char *states[] = {
		"California", "Oregon", 
		"Washington", "Texas", NULL
	};
	int num_states = 10;

	states[1] = argv[1];
	printf("Address states[1]: %p\n", states[1]);
	printf("Address argv[1]: %p\n", argv[1]);

	for(i = 0; i < argc; i++) {
		printf("arg %d: %s\n", i, argv[i]);
	}
	for(i = 0; i < num_states; i++) { 
		printf("state %d: %s\n", i, states[i]);
	}

	return 0;
}
