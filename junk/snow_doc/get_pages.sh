#!/bin/sh

i=0
while read line 
do
i=`expr $i + 1`
wget -O ${i}.html $line
done < "linkswiki.dat"

