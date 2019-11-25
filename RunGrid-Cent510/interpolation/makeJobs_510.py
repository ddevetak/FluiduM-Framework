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


####################################

try:
    # set parameters
    numberOfFiles = int(argv[1])
    numberOfJobs = int(argv[2])

except:
    print('Didnt set number of files or jobs!')
    exit()


#####################################

CONF = json.load(open("Configure.json", "r"))
WORKING_FOLDER = CONF["workingFolder"]
SOURCE_ROOT = CONF["sourceRoot"]
JobsFolder = "JOBS"


if not os.path.exists(JobsFolder):
    os.makedirs(JobsFolder)
    

Intervals = list(split( range(1, numberOfFiles+1), numberOfJobs))
CorrectedNumberOfJobs = len(Intervals)

min_index, max_index = '', ''

for i in range(1, CorrectedNumberOfJobs+1):

   #arguments = {'wf': WORKING_FOLDER, 'jb': JobsFolder, 'minI': min_index, 'maxI': max_index, 'sr': SOURCE_ROOT}
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
#SBATCH --time=0-0:20:00

# Working directory on shared storage
#SBATCH -D %(wf)s/interpolation/JOBS/%(jb)s

# Standard and error output in different files
#SBATCH -o %(j)s_%(N)s.out.log
#SBATCH -e %(j)s_%(N)s.err.log

%(sr)s
module use /cvmfs/it.gsi.de/modulefiles/
module load /cvmfs/it.gsi.de/modulefiles/compiler/gcc/6.3.0
time python do_macros_510.py %(minI)s %(maxI)s '%(jb)s' 

rm %(wf)s/interpolation/JOBS/%(jb)s/*/{eval_fit_graph_spectra_*,fit_graph_spectra_*,graph_spectra_*,chi_*}


""" % {'wf': WORKING_FOLDER, 'jb': job_folder , 'minI': min_index, 'maxI': max_index, 'sr': SOURCE_ROOT, 'j': j, 'N': N} 

#(WORKING_FOLDER, job_folder, j, N, j, N, SOURCE_ROOT, min_index, max_index, job_folder, WORKING_FOLDER, job_folder, WORKING_FOLDER, WORKING_FOLDER, 
#WORKING_FOLDER, WORKING_FOLDER, )

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
scp ../../do_macros_510.py ./
scp ../../Configure.json ./
cd ..

""" % (job_folder, job_folder)

    )


open(path.join(JobsFolder, "merge_root_files.sh"), "w").write(

"""#!/bin/bash

ls -1v %(wf)s/interpolation/JOBS/job-*/pion/tree* > listPion.txt
ls -1v %(wf)s/interpolation/JOBS/job-*/kaon/tree* > listKaon.txt
ls -1v %(wf)s/interpolation/JOBS/job-*/proton/tree* > listProton.txt

hadd PionFull.root @listPion.txt
hadd KaonFull.root @listKaon.txt
hadd ProtonFull.root @listProton.txt


""" % {'wf': WORKING_FOLDER}

)
