cmake_minimum_required(VERSION 3.10)
project(example_conan_git_describe)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup(NO_OUTPUT_DIRS TARGETS)
else()
    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif()

include(version)

add_library(example_conan_git_describe STATIC library.cpp library.h)
target_include_directories(example_conan_git_describe PRIVATE ${CONAN_INCLUDE_DIRS})

file(WRITE ${CMAKE_BINARY_DIR}/NAME ${CMAKE_PROJECT_NAME})
