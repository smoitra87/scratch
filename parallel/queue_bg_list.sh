#!/bin/bash

#----------------------------------------------------------------------
# Runs commands in parallel and maintains a queue by reading from a list
#
#----------------------------------------------------------------------

QUEUE_SIZE=0
NPROC=4 # Number of parallel processes to be run
QUEUE=""
COLFILE=$1 # File containing columns to run gremlin on 

function queue {
	QUEUE="$QUEUE $1"
	QUEUE_SIZE=$(($QUEUE_SIZE+1))
}

function refreshqueue {
	OLDQUEUE=$QUEUE
	QUEUE=""
	QUEUE_SIZE=0
	for p in $OLDQUEUE ; do
		if [ -d /proc/$p ] ; then
			QUEUE="$QUEUE $p"
			QUEUE_SIZE=$(($QUEUE_SIZE+1))
		fi
	done
}

function checkqueue {
	OLDCHKQUEUE=$QUEUE
	for p in $OLDCHKQUEUE ; do
		if [ ! -d /proc/$p ] ; then
			refreshqueue	
		fi
	done
}


cat $COLFILE | while read LINE ; do
	echo "Job $LINE"
	./do_nothing.sh &
	PROCID=$!
	queue $PROCID 
	echo "Executing process $PROCID"
	echo "QUEUESIZE $QUEUE_SIZE"
	while [ $QUEUE_SIZE -ge $NPROC ] ; do
		checkqueue
		sleep 0.4
	done
done

