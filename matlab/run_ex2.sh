#! /bin/sh

DIR=$(dirname $0)

s="'hello'"
echo matlab -nodesktop -nojvm -nosplash -r "addpath('./ex2') ; ex2(5,$s)" 
matlab -nodesktop -nojvm -nosplash -r "addpath('./ex2') ; ex2(5,$s)" 

