
int MyVar = 10;
int printf(const char *s, ...);

test2(int *i)
{
   *i=100;
	printf("%d",*i);
}

int main() { 
	int *i;
	test2(i);
	return 0;
}
    
