#!/bin/sh


allpdfs=""
for f in "$@" ; do 
    filename=$(basename "$f")
    filename="${filename%.*}"
    pygmentize -f tex -O linenos -O title="$f" -O full -O style=default -o /tmp/$filename.tex $f
    pdflatex -jobname=$filename -output-directory=/tmp /tmp/$filename.tex
    allpdfs="$allpdfs /tmp/$filename.pdf"
done

pdftk $allpdfs cat output /tmp/combined.pdf
