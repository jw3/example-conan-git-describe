cmake_minimum_required(VERSION 3.10)
project(example_conan_git_describe)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

include(version)

add_library(example_conan_git_describe library.cpp library.h)

file(WRITE ${CMAKE_BINARY_DIR}/NAME ${CMAKE_PROJECT_NAME})
