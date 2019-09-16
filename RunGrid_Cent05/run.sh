#!/bin/bash

echo "before = ", $PWD
source /lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/0-5/changeDir05.sh 
echo "after = ", $PWD
#trento05
cd JOBS
dir=$PWD

for filename in $dir/job-*.sh; do

     source $filename
done

cd ../..
