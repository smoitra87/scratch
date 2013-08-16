#! /bin/sh

s="'hello'"
matlab -nodesktop -nojvm -nosplash -r "ex2(5,$s)" 
