#!/bin/bash

source changeDir510.sh 

cd JOBS
dir=$PWD

for filename in $dir/job-*.sh; do

     source $filename
done

cd ../..
