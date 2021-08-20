#!/usr/bin/env bash
g++ $1 #filename without input, 1st arg passed
./a.out
rm -f ./a.out
