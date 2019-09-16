#!/bin/bash

scp HYDRO.wl JOBS 
cd JOBS
dir=$(pwd)

for filename in $dir/*.sh; do

     if [[ $filename = *"pre"* ]]; then
     source $filename
     fi
done

cd ..
