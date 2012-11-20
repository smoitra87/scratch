#!/bin/bash

HOST=$1
WGET="/usr/bin/wget"

$WGET -q --tries=10 --timeout=5 $HOST
RESULT=$?

if [ $RESULT -eq 0 ]; then
echo "Connection made successfully to $HOST"
else
echo "Failed to make connection to $HOST"
fi
