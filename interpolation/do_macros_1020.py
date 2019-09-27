import glob
import json

from sys import argv, exit
from os import makedirs, path, unlink
from shutil import copytree, copy, rmtree
import subprocess
import os


def sortKeyFunc(s):
    return int(os.path.basename(s)[8:-5])

def main():

   try:
     # set parameters
     Low =  int(argv[1]) 
     High = int(argv[2])
     jobFolder = str(argv[3])

   except:
     print('Didnt set number of files or jobs!')
     exit()

   ###############################
   # SET PATHS and load HYDRO DATA
   
   WORKING_FOLDER_PATH = "/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/macro_batch/RUN3_GRID10"
   GRID_DATA_PATH = "/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/10-20/JOBS_GRID10_RUN3"
   ALICE_DATA_PATH = "/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/10-20"
   MACROS_PATH = "/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/MACROS"

   PT = "/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/fullPtRange.json"

   workFolderPion =    WORKING_FOLDER_PATH + "/JOBS/" + jobFolder + "/pion/" 
   workFolderKaon =    WORKING_FOLDER_PATH + "/JOBS/" + jobFolder + "/kaon/" 
   workFolderProton =  WORKING_FOLDER_PATH + "/JOBS/" + jobFolder + "/proton/" 

   # LOAD GRID DATA
   SpectraPathPion =   glob.glob(GRID_DATA_PATH + "/job-*/pion/spectra_*")
   SpectraPathKaon =   glob.glob(GRID_DATA_PATH + "/job-*/kaon/spectra_*")
   SpectraPathProton = glob.glob(GRID_DATA_PATH + "/job-*/proton/spectra_*")

   ###############################
   # LOAD Alice DATA 

   PionAlicePT =   ALICE_DATA_PATH + "/pion/pt_pi0139plu.json"
   KaonAlicePT =   ALICE_DATA_PATH + "/kaon/pt_Ka0492plu.json"
   ProtonAlicePT = ALICE_DATA_PATH + "/proton/pt_pr0938plu.json"

   ###############################

   # Sort
   SpectraPathPion.sort(key=sortKeyFunc)
   SpectraPathKaon.sort(key=sortKeyFunc)
   SpectraPathProton.sort(key=sortKeyFunc)

   FILES1 = SpectraPathPion[Low-1:High]
   FILES2 = SpectraPathKaon[Low-1:High]
   FILES3 = SpectraPathProton[Low-1:High]

   ################################

   graph = "python2 " + MACROS_PATH + "/graph/make_graph.py "
   fit = "python2 " + MACROS_PATH + "/fit/make_fit.py "
   chi = "python2 " + MACROS_PATH + "/chi/make_chi_square_batch_1020.py "
   writeToTree = "python2 " + MACROS_PATH + "/chi/write_to_tree_1020.py " + WORKING_FOLDER_PATH + " " + jobFolder + " pion" 

   HaddPion =   "hadd " + workFolderPion +   "full_spectra.root " + workFolderPion   + "graph_spectra_*" 
   HaddKaon =   "hadd " + workFolderKaon +   "full_spectra.root " + workFolderKaon   + "graph_spectra_*" 
   HaddProton = "hadd " + workFolderProton + "full_spectra.root " + workFolderProton   + "graph_spectra_*" 

   rmPion =   "rm " + workFolderPion   + "graph_spectra_*" 
   rmKaon =   "rm " + workFolderKaon   + "graph_spectra_*" 
   rmProton = "rm " + workFolderProton + "graph_spectra_*" 

   for iFile in FILES1:

       GraphFile = workFolderPion + "graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".root"
       EvalGraphFile = workFolderPion + "eval_fit_graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".json"

       commandGraph =    graph + workFolderPion + " " + PT + " " + iFile + " -b"   # the iFile gives the index in output
       commandFit =      fit + workFolderPion + " " + GraphFile + " " + PionAlicePT + " -b"
       commandCHI =      chi + workFolderPion + " " + str(1) + " " + EvalGraphFile + " -b"    # 1 = PION
       
       os.system(commandGraph)     
       os.system(commandFit)     
       os.system(commandCHI)     

   os.system(writeToTree)     
   os.system(HaddPion)     
   os.system(rmPion)     
     
   for iFile in FILES2:

       GraphFile = workFolderKaon + "graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".root"
       EvalGraphFile = workFolderKaon + "eval_fit_graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".json"

       commandGraph =    graph + workFolderKaon + " " + PT + " " + iFile + " -b"
       commandFit =      fit + workFolderKaon + " " + GraphFile + " " + KaonAlicePT + " -b"
       commandCHI =      chi + workFolderKaon + " " + str(2) + " " + EvalGraphFile + " -b"    # 1 = PION
       
       os.system(commandGraph)     
       os.system(commandFit)     
       os.system(commandCHI)     

   os.system(writeToTree + " kaon")     
   os.system(HaddKaon)     
   os.system(rmKaon)     
     
     
   for iFile in FILES3:

       GraphFile = workFolderProton + "graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".root"
       EvalGraphFile = workFolderProton + "eval_fit_graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".json"

       commandGraph =    graph + workFolderProton + " " + PT + " " + iFile + " -b"
       commandFit =      fit + workFolderProton + " " + GraphFile + " " + ProtonAlicePT + " -b"
       commandCHI =      chi + workFolderProton + " " + str(3) + " " + EvalGraphFile + " -b"    # 1 = PION
       
       os.system(commandGraph)     
       os.system(commandFit)     
       os.system(commandCHI)     

   os.system(writeToTree + " proton")     
   os.system(HaddProton)     
   os.system(rmProton)     
     

main()
