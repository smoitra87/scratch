#include<iostream>
#include<string>

using namespace std;

void print_str(string s) {
	for(string::iterator it = s.begin() ; it != s.end() ; it++) {
		cout<<*it;
	}
	cout<<endl;
}

int main() {
	string s1,s2;
	s1 = "Hello World";
	s2 = s1 + "\n" + "Hello!";
	print_str(s2);	
	return 0;
}
