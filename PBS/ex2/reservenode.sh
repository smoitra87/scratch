#!/bin/sh

HOST=`hostname -s`
USER=`whoami`
touch $PBS_O_WORKDIR/$HOST.$USER
while [ -e $PBS_O_WORKDIR/$HOST.$USER ] ; do
   sleep 30
done

