#!/bin/bash

source changeDir05.sh 

cd JOBS
dir=$PWD

for filename in $dir/job-*.sh; do

     source $filename
done

cd ../..
