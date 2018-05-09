#!/usr/bin/env bash


fix() {
  echo -n "example_conan_git_describe" > build/NAME
  echo -n "0.0.0" > build/VERSION
}


rm -rf build
mkdir build

if [[ "$1" == "fix" ]]; then fix; fi

conan install . -if build
cd build
cmake ..
make
cd -

if [[ "$1" == "fix" ]]; then fix; fi

conan export-pkg . foo/bar -f
