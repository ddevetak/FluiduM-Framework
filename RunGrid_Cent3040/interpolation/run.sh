#!/bin/bash

cd JOBS
dir=$PWD

for filename in $dir/job-*.sh; do

     sbatch $filename
done

cd ../..
