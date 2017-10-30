#!/bin/bash

set -x

rm -rf build
mkdir build
cd build
cmake ..
make -j8
sudo make install
cd ..
rm -rf build
