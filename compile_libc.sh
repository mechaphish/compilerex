#!/bin/bash

./compile.sh -O3 -c src/*.c

./bin/ar rcs libc.a *.o

md5sum libc.a
mv libc.a lib

rm *.o
