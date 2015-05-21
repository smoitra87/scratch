#include<stdio.h>
#include<stdlib.h>

typedef struct Point Point;
Point* Point_new(int x, int y);

struct Point {
	int x;
	int y;
};

Point * Point_new(int x, int y)
{
	Point *p;
	if( p = malloc(sizeof(Point))) {
		p->x = x ;
		p->y = y;
	} else {
		printf("Error: Could not allocate\n");
		exit(1);
	}
	return p;
	
}

void Point_print(Point *p){
	if(p) {
		printf("Point(p) = {%d,%d}\n",p->x,p->y);
	}
}

int main() {

	Point *p = Point_new(1,2);
	Point_print(p);

	return 0;
}
