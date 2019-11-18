"""
  script for making separate jobs and running on batch system.

# job-i.sh contains executable commands; pre-job-i.sh moves to the job-i folder and copies files if necessary!

"""

from sys import argv, exit
from os import makedirs, path, unlink
from shutil import copytree, copy, rmtree
import subprocess
import os
import json

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in xrange(n))


#################################

try:
    # set parameters
    numberOfFiles = int(argv[1])
    numberOfJobs =  int(argv[2])

except:
    print('Didnt set number of files or jobs!')
    exit()

#################################

CONF = json.load(open("Configure.json", "r"))
WORKING_FOLDER = CONF["workingFolder"]
JobsFolder = "JOBS"

if not os.path.exists(JobsFolder):
    os.makedirs(JobsFolder)
    

Intervals = list(split( range(1, numberOfFiles+1), numberOfJobs))
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

(time nohup /cvmfs/theory.gsi.de/bin/math11 -u -script HYDRO.wl -- %s %s '%s') >  %s/JOBS/%s.out 2>&1 &


""" % (min_index, max_index, job_folder, WORKING_FOLDER, job_folder)

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
mkdir -p lambda
mkdir -p xi
mkdir -p omega 
cd ..

""" % (job_folder, job_folder)

    )




