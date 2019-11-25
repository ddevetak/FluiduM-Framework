#!/bin/bash

cd JOBS
dir=$(pwd)

for filename in $dir/*.sh; do

     if [[ $filename = *"pre"* ]]; then
     source $filename
     fi
done

cd ..


cd JOBS
dir=$PWD

for filename in $dir/job-*.sh; do

     sbatch $filename
done

cd ../
