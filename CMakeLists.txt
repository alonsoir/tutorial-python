cmake_minimum_required(VERSION 3.12)

project(sieve)

set(CMAKE_CXX_STANDARD 11)

add_executable(sieve_multithread sieve_multithread.cpp)

target_compile_options(sieve_multithread PRIVATE -O3 -Wno-c++11-extensions)
