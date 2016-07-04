#!/bin/bash -e

pushd boolector/lingeling/
./configure.sh
make
popd

./compile.sh -Wall -O3 -DNLGLOG -DNDEBUG -DNCHKSOL -DNLGLDRUPLIG -DNLGLYALSAT -DNLGLFILES -DNLGLDEMA -c boolector/lingeling/lglbnr.c
./compile.sh -Wall -O3 -DNLGLOG -DNDEBUG -DNCHKSOL -DNLGLDRUPLIG -DNLGLYALSAT -DNLGLFILES -DNLGLDEMA -c boolector/lingeling/lglopts.c
./compile.sh -Wall -O3 -DNLGLOG -DNDEBUG -DNCHKSOL -DNLGLDRUPLIG -DNLGLYALSAT -DNLGLFILES -DNLGLDEMA -c boolector/lingeling/lglib.c

./bin/ar rcs liblgl.a lglbnr.o lglopts.o lglib.o
mv liblgl.a lib/

pushd boolector/boolector
./configure
make
cp ./libboolector.a ../../lib/libboolector.a
popd

echo "DONE"
