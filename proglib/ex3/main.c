#include<stdio.h>

extern "C" void bar(int*);
void spoo(int* );



int main(){

	int i;
	bar(&i);
	printf("i=%d\n",i);
	spoo(&i);
	printf("i=%d\n",i);

	return 0;
}

