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

   CONF = json.load(open("Configure.json", "r"))
   WORKING_FOLDER =  CONF["workingFolder"]
   ALICE_DATA_PATH = CONF["aliceFolder"]

   PT = ALICE_DATA_PATH + "/fullPtRange.json"

   workFolderPion =    WORKING_FOLDER + "/interpolation/JOBS/" + jobFolder + "/pion/" 
   workFolderKaon =    WORKING_FOLDER + "/interpolation/JOBS/" + jobFolder + "/kaon/" 
   workFolderProton =  WORKING_FOLDER + "/interpolation/JOBS/" + jobFolder + "/proton/" 

   # LOAD GRID DATA
   SpectraPathPion =   glob.glob(WORKING_FOLDER + "/JOBS/job-*/pion/spectra_*")
   SpectraPathKaon =   glob.glob(WORKING_FOLDER + "/JOBS/job-*/kaon/spectra_*")
   SpectraPathProton = glob.glob(WORKING_FOLDER + "/JOBS/job-*/proton/spectra_*")

   ###############################
   # load Alice DATA 

   PionAlicePT =   ALICE_DATA_PATH + "/pion/pt_pi0139plu.json"
   KaonAlicePT =   ALICE_DATA_PATH + "/kaon/pt_Ka0492plu.json"
   ProtonAlicePT = ALICE_DATA_PATH + "/proton/pt_pr0938plu.json"

   ###############################
   # Sort ascending 1,2,3...

   SpectraPathPion.sort(key=sortKeyFunc)
   SpectraPathKaon.sort(key=sortKeyFunc)
   SpectraPathProton.sort(key=sortKeyFunc)

   FILES1 = SpectraPathPion[Low-1:High]
   FILES2 = SpectraPathKaon[Low-1:High]
   FILES3 = SpectraPathProton[Low-1:High]

   ################################
   # MACROS commands

   graph =       "python " + WORKING_FOLDER + "/interpolation/MACROS/graph/make_graph.py "
   fit =         "python " + WORKING_FOLDER + "/interpolation/MACROS/fit/make_fit.py "
   chi =         "python " + WORKING_FOLDER + "/interpolation/MACROS/chi/make_chi_square_batch_510.py " + WORKING_FOLDER  + " "
   writeToTree = "python " + WORKING_FOLDER + "/interpolation/MACROS/chi/write_to_tree_510.py " + WORKING_FOLDER + "/interpolation/JOBS/ " + jobFolder


   for iFile in FILES1:

       GraphFile = workFolderPion + "graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".root"
       EvalGraphFile = workFolderPion + "eval_fit_graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".json"

       commandGraph =    graph + workFolderPion + " " + PT + " " + iFile + " -b"   # the iFile gives the index in output
       commandFit =      fit + workFolderPion + " " + GraphFile + " " + PionAlicePT + " -b"
       commandCHI =      chi + workFolderPion + " " + str(1) + " " + EvalGraphFile + " " + iFile + " -b"    # 1 = PION
       
       os.system(commandGraph)     
       os.system(commandFit)     
       os.system(commandCHI)     

   os.system(writeToTree + " pion")     
     
   for iFile in FILES2:

       GraphFile = workFolderKaon + "graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".root"
       EvalGraphFile = workFolderKaon + "eval_fit_graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".json"

       commandGraph =    graph + workFolderKaon + " " + PT + " " + iFile + " -b"
       commandFit =      fit + workFolderKaon + " " + GraphFile + " " + KaonAlicePT + " -b"
       commandCHI =      chi + workFolderKaon + " " + str(2) + " " + EvalGraphFile + " " + iFile + " -b"    # 1 = PION
       
       os.system(commandGraph)     
       os.system(commandFit)     
       os.system(commandCHI)     

   os.system(writeToTree + " kaon")     
     
   for iFile in FILES3:

       GraphFile = workFolderProton + "graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".root"
       EvalGraphFile = workFolderProton + "eval_fit_graph_" + iFile.rsplit('/', 1)[1].split(".")[0] + ".json"

       commandGraph =    graph + workFolderProton + " " + PT + " " + iFile + " -b"
       commandFit =      fit + workFolderProton + " " + GraphFile + " " + ProtonAlicePT + " -b"
       commandCHI =      chi + workFolderProton + " " + str(3) + " " + EvalGraphFile + " " + iFile + " -b"    # 1 = PION
       
       os.system(commandGraph)     
       os.system(commandFit)     
       os.system(commandCHI)     

   os.system(writeToTree + " proton")     
     

main()
