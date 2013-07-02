#include<stdio.h>

class A{
	int x;
	public:
	A(int _x) {
		x = _x;
	}
	void printx() {
		printf("%d\n",x);
	}
	

};


void spoo(int *i){

	*i=5;
}


#ifdef __cplusplus
extern "C" {
#endif

void bar(int *i) {

	*i=10;
}


#ifdef __cplusplus
}
#endif
