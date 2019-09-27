import glob
import json

from sys import argv, exit
from os import makedirs, path, unlink
from shutil import copytree, copy, rmtree
import subprocess
import os

from ROOT import TFile, TTree
from ROOT import gROOT, AddressOf
import yaml

##############################

gROOT.ProcessLine(
"struct MyStruct {\
   int       conf;\
   float     reducedChi;\
   float     chi;\
   float     norm;\
   float     eta;\
   float     bulk;\
   float     temp;\
   float     tau0;\
};" );

##############################


def sortKeyFunc(s):
    return int(os.path.basename(s)[4:-4])  # 4 for "chi_" & 4 for ".yml"

##############################

from ROOT import MyStruct
Struct = MyStruct()

def main():

   try:
     # set parameters
     jobFolder = str(argv[1])
     particleFolder = str(argv[2])

   except:
     print('Didnt set number of files or jobs!')
     exit()

   ########################
 
   f = TFile( "/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/macro_batch/JOBS/" + jobFolder + "/" + particleFolder + "/" + 'tree.root', 'RECREATE' )
   tree = TTree( 'Tree', 'chi data' )
   tree.Branch( 'Data', Struct, 'conf/I:reducedChi/F:chi/F:norm/F:eta/F:bulk/F:temp/F:tau0/F' )

   ChiPionYaml =   glob.glob("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/macro_batch/JOBS/" + jobFolder + "/" + particleFolder + "/chi_*")
   ChiPionYaml.sort(key=sortKeyFunc)

   for iFile in ChiPionYaml[0:]:

       CONF = int(iFile.rsplit('/', 1)[1].split(".")[0][4:])
       print "conf = ", CONF
       iDATA = yaml.load(open(iFile, "r"))
 
       reducedChi = iDATA[CONF][0]
       chi = iDATA[CONF][1]
       par = iDATA[CONF][2]

       Struct.conf = CONF 
       Struct.reducedChi = reducedChi 
       Struct.chi = chi 
       Struct.norm = par[0] 
       Struct.eta =  par[1] 
       Struct.bulk = par[2] 
       Struct.temp = par[3] 
       Struct.tau0 = par[4] 
       tree.Fill()
 
   f.Write()
   f.Close()



main()
