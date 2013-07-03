#!/bin/sh

export LD_LIBRARY_PATH=~/local/lib:${LD_LIBRARY_PATH}
echo $LD_LIBRARY_PATH
echo `pwd`
~/projects/scratch/proglib/ex4/main $*


