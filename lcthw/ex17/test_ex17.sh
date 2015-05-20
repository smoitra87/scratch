#!/bin/sh

set -e

make clean all
[ -e test.dat ] && rm test.dat

./ex17 test.dat c
./ex17 test.dat s 1 zed zed@zedshaw.com
./ex17 test.dat s 2 frank frank@zedshaw.com
./ex17 test.dat s 3 joe joe@zedshaw.com
./ex17 test.dat l
./ex17 test.dat l
./ex17 test.dat g 2
