#! /bin/sh

# Check if a python package exists
PKGNAME=$1

python -c "import ${1}" 2>&1 > /dev/null 2>/dev/null
test $? -eq 0 && ( echo "exists" ) || ( echo "does not exist" )

