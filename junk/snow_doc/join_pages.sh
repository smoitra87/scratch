#!/bin/sh
rm all_pages.html
KEEP=`grep -n '<div id="column-one">' 1.html | cut -f 1  | cut -d: -f1`
head -n $KEEP 1.html >> all_pages.html

for i in `seq 2 51` 
do
echo "Processing $i"
KEEP1=`grep -n '<div id="column-one">' ${i}.html | cut -f 1  | cut -d: -f1`
KEEP2=`grep -n '<div id="content">' ${i}.html | cut -f 1  | cut -d: -f1`
head -n $KEEP1 ${i}.html | tail -n+${KEEP2} >> all_pages.html
echo "</body></html>" >> all_pages.html
done

