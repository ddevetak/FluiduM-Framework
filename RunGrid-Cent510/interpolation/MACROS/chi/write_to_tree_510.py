import glob
import json

from sys import argv, exit
from os import makedirs, path, unlink
from shutil import copytree, copy, rmtree
import subprocess
import os
from array import array

from ROOT import TFile, TTree
from ROOT import gROOT, AddressOf
import yaml


##############################


def sortKeyFunc(s):
    return int(os.path.basename(s)[4:-4])  # 4 for "chi_" & 4 for ".yml"

##############################

def main():

   try:
     # set parameters
     workingFolder = str(argv[1])
     jobFolder = str(argv[2])
     particleFolder = str(argv[3])

   except:
     print('Didnt set number of files or jobs!')
     exit()

   ########################
 
   f = TFile( workingFolder + jobFolder + "/" + particleFolder + "/" + 'tree-' + jobFolder + '.root', 'RECREATE' )
   tree = TTree("tree", "spectra data")

   conf =        array( 'i', [ 0 ] ) 
   points =      array( 'i', [ 0 ] ) 
   reducedChi =  array( 'd', [ 0 ] ) 
   chi =         array( 'd', [ 0 ] ) 
   norm =        array( 'd', [ 0 ] ) 
   eta =         array( 'd', [ 0 ] ) 
   bulk =        array( 'd', [ 0 ] ) 
   temp =        array( 'd', [ 0 ] ) 
   tau0 =        array( 'd', [ 0 ] ) 

   dNdpt =       array( 'd', 100*[ 0 ] ) 
   
   tree.Branch( 'conf', conf, 'conf/I' )
   tree.Branch( 'points', points, 'points/I' )
   tree.Branch( 'reducedChi', reducedChi, 'reducedChi/D' )
   tree.Branch( 'chi', chi,  'chi/D' )
   tree.Branch( 'norm', norm, 'norm/D' )
   tree.Branch( 'eta', eta,  'eta/D' )
   tree.Branch( 'bulk', bulk, 'bulk/D' )
   tree.Branch( 'temp', temp, 'temp/D' )
   tree.Branch( 'tau0', tau0, 'tau0/D' )

   tree.Branch( 'dNdpt', dNdpt, 'dNdpt[points]/D' )

   ChiYaml =   glob.glob(workingFolder + "/" + jobFolder + "/" + particleFolder + "/chi_*")
   ChiYaml.sort(key=sortKeyFunc)  # sort chi_i files

   for iFile in ChiYaml[0:]:

       CONF = int(iFile.rsplit('/', 1)[1].split(".")[0][4:])
       iDATA = yaml.load(open(iFile, "r"))
       conf[0] = CONF 
       reducedChi[0] = iDATA[CONF][0]
       chi[0] = iDATA[CONF][1]
       par = iDATA[CONF][2]
       points[0] = len(iDATA[CONF][3])

       norm[0] = par[0] 
       eta[0] =  par[1] 
       bulk[0] = par[2] 
       temp[0] = par[3] 
       tau0[0] = par[4] 
       for i in range(0, len(iDATA[CONF][3]) ): dNdpt[i] = iDATA[CONF][3][i]
   
       tree.Fill()
 
   #f.Write()
   f.Write("",TFile.kOverwrite)
   f.Close()



main()
