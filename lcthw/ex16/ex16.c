#include<stdio.h>
#include<assert.h>
#include<stdlib.h>
#include<string.h>

struct Person {
	char *name;
	int age;
	int height;
	int weight;
};

struct Person *Person_create(char *name, int age, int height, int weight) 
{
	struct Person *who  = malloc(sizeof(struct Person));
	assert(who != NULL);

	who->name = strdup(name);
	who->age = age;
	who->height = height;
	who->weight = weight;

	return who;
}

void Person_destroy(struct Person *who) 
{
	assert(who != NULL);
	
	free(who->name);
	free(who);
}

void Person_print(struct Person *who)
{
	printf("Name: %s\n", who->name);
	printf("\tAge: %d\n", who->age);
	printf("\tHeight: %d\n", who->height);
	printf("\tWeight: %d\n", who->weight);
}

void Person_print_byvalue(struct Person who)
{
	printf("Name: %s\n", who.name);
	printf("\tAge: %d\n", who.age);
	printf("\tHeight: %d\n", who.height);
	printf("\tWeight: %d\n", who.weight);
}

int main(int argc, char *argv[]) 
{

	struct Person subho = {"Subho", 27, 170, 160};
	struct Person *basu = Person_create("Basu", 28, 180, 180);

	printf("Subho is at memory location: %p\n", &subho);
	Person_print_byvalue(subho);

	printf("Basu is at memory location: %p\n", basu);
	Person_print(basu);

	subho.age += 20;
	subho.height += 2;
	subho.weight -=20;
	Person_print_byvalue(subho);

	//destroy the objects and clean up
	//Person_destroy(subho);
	Person_destroy(basu);

	return 0;
}
