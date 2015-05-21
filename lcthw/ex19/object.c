#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "object.h"
#include <assert.h>

void Object_destroy(void *self) 
{
	Object *obj = self;

	if(obj) {
		if(obj->description) free(obj->description);
		free(obj);
	}
}

void Object_describe(void *self)
{
	Object *obj = self;
	assert(obj);
	assert(obj->description);
	printf("%s.\n", obj->description);
}

int Object_init(void *self)
{
	assert(self);
	// do nothing
	return 1;
}

void *Object_move(void *self, Direction direction)
{
	printf("You can't go that direction.\n");
	return NULL;
}

int Object_attack(void *self, int damage)
{
	printf("You can't attack that.\n");
	return 0;
}

void *Object_new(size_t size, Object proto, char *description)
{
	assert(description);
	assert(size > 0);
	//setup default functions in case they aren't already.set. 
	// proto should have some functions already set
	if(!proto.init) proto.init = Object_init;
	if(!proto.describe) proto.describe = Object_describe;
	if(!proto.destroy) proto.destroy = Object_destroy;
	if(!proto.attack) proto.attack = Object_attack;
	if(!proto.move) proto.move = Object_move;

	// calloc incurs a performance overhead over malloc
	// by setting things to zero
	Object *el = calloc(1, size);
	if(!el) {
		printf("Error: Could not allocation object\n");
		exit(1);	
	}
	*el = proto; // is this a case of struct copy
	
	el->description = strdup(description);
	if(!el->description) {
		printf("Could not duplicate string\n");
		exit(1);
	}
	
	if(!el->init(el)) {
		el->destroy(el);
		return NULL;
	} else {
		assert(el);
		return el;
	}
}
