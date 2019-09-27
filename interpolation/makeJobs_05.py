"""
  script for making separate jobs and running on batch system.

# job-i.sh contains executable commands; pre-job-i.sh moves to the job-i folder and copies files if necessary!

"""

from sys import argv, exit
from os import makedirs, path, unlink
from shutil import copytree, copy, rmtree
import subprocess
import os

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in xrange(n))

try:
    # set parameters
    numberOfFiles = int(argv[1])
    blocks = int(argv[2])
    numberOfJobs = int(argv[3])

except:
    print('Didnt set number of files or jobs!')
    exit()

JobsFolder = "JOBS"

if not os.path.exists(JobsFolder):
    os.makedirs(JobsFolder)
    

Intervals = list(split( range(1, numberOfFiles+1), blocks*numberOfJobs))
print "num. jobs = ", len(Intervals), Intervals[0], Intervals[-1]
CorrectedNumberOfJobs = len(Intervals)

for i in range(1, CorrectedNumberOfJobs+1):

   job_folder='job'+'-'+str(i)    
   j = '%j'
   N = '%N'
   min_index = Intervals[i-1][0]  
   max_index = Intervals[i-1][-1] 
   #print min_index, max_index

   open(path.join(JobsFolder, "job-%d.sh" % i), "w").write(
"""#!/bin/bash

# Task name
#SBATCH -J doMacros

# Run time limit
#SBATCH --time=0-1:60:00

# Working directory on shared storage
#SBATCH -D /lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/macro_batch/RUN3_GRID10/interpolation/JOBS/%s

# Standard and error output in different files
#SBATCH -o %s_%s.out.log
#SBATCH -e %s_%s.err.log

source /lustre/nyx/alice/users/ddevetak/root6/bin/thisroot.sh
module load /cvmfs/it.gsi.de/modulefiles/compiler/gcc/6.3.0
time python do_macros_05.py %s %s '%s' 


""" % (job_folder, j, N, j, N, min_index, max_index, job_folder)

    )

for i in range(1, CorrectedNumberOfJobs+1):

   job_folder='job'+'-'+str(i)

   open(path.join(JobsFolder, "pre-job-%d.sh" % i), "w").write(

"""#!/bin/bash
mkdir %s
cd %s
mkdir -p pion
mkdir -p kaon
mkdir -p proton
scp ../../do_macros_05.py ./
cd ..

""" % (job_folder, job_folder)

    )

