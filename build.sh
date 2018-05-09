#!/usr/bin/env bash

rm -rf build
mkdir build
conan install . -if build
cd build
cmake ..
make
conan export-pkg .. foo/bar -f
