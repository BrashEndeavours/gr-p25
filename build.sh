#!/bin/bash

set -x

sudo rm -rf /home/brash/gnuradio/default/lib/python2.7/dist-packages/thesis
rm -rf build
mkdir build
cd build
cmake ..
make -j8
sudo make install
