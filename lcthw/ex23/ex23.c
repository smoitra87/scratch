#include <stdio.h>
#include "dbg.h"
#include "ex23.h"

int main(int argc, char *argv[])
{
	int x = 1;
	switch(x) {
		CASE8(printf("Hello World\n"),1,2,3,4,5,6,7,8)
	}

	return 0;
}
