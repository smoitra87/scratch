#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <time.h>
#include "ex19.h"

Map *create_Map() 
{ 
	// make thre map to work with

	Object *map_proto = malloc(sizeof(Object));
	if(!map_proto) {
		printf("Could not allocate map\n");
		exit(1);
	}
	map_proto->init = Map_init;
	map_proto->attack = Map_attack;
	map_proto->move = Map_move;

	Map *game = Object_new(
			sizeof(Map), *map_proto, "The Hall of the Minotaur.");

	return game;
}


int main(int argc, char *argv[]){
	
	// set up way randomness
	srand(time(NULL));
	
	// get the map
	Map *game = create_Map();
	
	printf("You enter the ");
	game->location->_(describe)(game->location);

	while(process_input(game)) {
	}

	return 0;
}
