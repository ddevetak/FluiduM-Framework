#!/bin/bash

source changeDir3040.sh 

cd JOBS
dir=$PWD

for filename in $dir/job-*.sh; do

     source $filename
done

cd ../
