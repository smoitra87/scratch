#include<iostream>

using namespace std;

int main() {

	const int i = 34;
	cout<<"i="<<i<<endl;

	const void *ptr = &i;
	cout<<"using void i="<<*((const int*)ptr)<<endl;

	return 0;
}
