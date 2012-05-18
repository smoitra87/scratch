#!/bin/sh

#---------------------------------------------------------------------
# Runs dummy background processes and waits

NPROC=6
MAX_PROC=4
CUR_NPROC=0
for id in `seq 1 $NPROC` ; do
	./do_nothing.sh &
	PROC_ID=$!
	echo "Process id is $PROC_ID"
	CUR_NPROC=$(($CUR_NPROC+1))
	if [ $CUR_NPROC -ge $MAX_PROC ] ; then
		wait
		CUR_NPROC=0
	fi
done
