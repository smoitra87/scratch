#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main() {
	printf("sizeof(int8_t) = %u\n",sizeof(int8_t));
	printf("INT8_MAX = %u\n", INT8_MAX);
	printf("sizeof(uint8_t) = %u\n",sizeof(uint8_t));
	printf("UINT8_MAX = %u\n", UINT8_MAX);
	printf("sizeof(int) = %d\n",sizeof(int));
	printf("sizeof(size_t) = %d\n",sizeof(size_t));
	printf("SIZE_MAX = %zu\n", SIZE_MAX);
	printf("sizeof(intmax_t) = %d\n",sizeof(intmax_t));
	printf("INTMAX_MAX = %ju\n", INTMAX_MAX);
	return 0;
}
