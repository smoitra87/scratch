#!/bin/bash

#----------------------------------------------------------------------
# Runs commands in parallel and maintains a queue
#
#----------------------------------------------------------------------

QUEUE_SIZE=0
NPROC=4 # Number of parallel processes to be run
QUEUE=""


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

for i in `seq 1 6` ; do
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



