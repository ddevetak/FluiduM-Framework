from ROOT import TF1, TGraphErrors, TH1F, TFile, TH1D, TGraph, TCanvas
import glob
import json
import math
import yaml
import operator
from collections import OrderedDict
from operator import itemgetter
from sys import argv, exit

def DirectChi(dataList, dataErrorList, hydroList, minBin, maxBin):


  ZIP = zip(dataList[minBin:maxBin], hydroList[minBin:maxBin], dataErrorList[minBin:maxBin])
  
  ChiSqr = sum([ pow(x[0]-x[1], 2)/(x[2]*x[2]) for x in ZIP ])

  NDF = len(dataList[minBin:maxBin]) -5

  return (ChiSqr/NDF, ChiSqr)
  #return ChiSqr

#############################################

def main():

   try:
    # set parameters
     WorkFolder = str(argv[1])
     Which_particle = int(argv[2])
     hydroDataFile = str(argv[3])

   except:
     print('Didnt set input parameters!')
     exit()

   ###########################
   
   Which_combination = [int(x) for x in hydroDataFile.split("/")[-1].split(".")[0].split("_") if x.isdigit()][0]
   print Which_combination

   #combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/grid_9bins.dat", "r")
   #combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/grid_10bins.dat", "r")
   #combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/grid_10bins_localized.dat", "r")
   #combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/confs_9D/grid_3bins_norm5.dat", "r")
   combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/parralel_batch/grid_10bins_27_08.dat", "r")

   DICT_COMB = dict()
   lineIndex = 0

   for line in combinations:

      lineIndex = lineIndex + 1
      temp = [float(x) for x in line.split(" ")]
      DICT_COMB[lineIndex] = temp

   ####################################################################################
   # DIRECT CHI CALCULATION

   spectraList = json.load(open(hydroDataFile, "r"))
   which_particle  = Which_particle   # pion = 1; kaon = 2; proton = 3

   PERCENT = 0.0

   if which_particle == 1:

      Data = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/30-40/pion/pi0139plu.json", "r"))
      DataError = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/30-40/pion/fullError.json", "r"))

      HydroError =   list(map(lambda x: x*PERCENT, spectraList))
      tempFullError = zip( map(lambda x: x*x, HydroError), map(lambda x: x*x, DataError) )
      FullError = [ math.sqrt(x[0] + x[1]) for x in tempFullError ]

   if which_particle == 2:

      Data = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/30-40/kaon/Ka0492plu.json", "r"))
      DataError = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/30-40/kaon/fullError.json", "r"))

      HydroError =   list(map(lambda x: x*PERCENT, spectraList))
      tempFullError = zip( map(lambda x: x*x, HydroError), map(lambda x: x*x, DataError) )
      FullError = [ math.sqrt(x[0] + x[1]) for x in tempFullError ]

   if which_particle == 3:

      Data = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/30-40/proton/pr0938plu.json", "r"))
      DataError = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/30-40/proton/fullError.json", "r"))

      HydroError =   list(map(lambda x: x*PERCENT, spectraList))
      tempFullError = zip( map(lambda x: x*x, HydroError), map(lambda x: x*x, DataError) )
      FullError = [ math.sqrt(x[0] + x[1]) for x in tempFullError ]

   ########################################

   CurrentChi2 = 0

   if which_particle==1: CurrentChi2 = DirectChi(Data, FullError, spectraList, 0, 41)  # PION      max = 41 ; BW = 11 - 20 +1
   if which_particle==2: CurrentChi2 = DirectChi(Data, FullError, spectraList, 0, 36)  # KAON      max = 36 ; BW = 0  - 20 +1
   if which_particle==3: CurrentChi2 = DirectChi(Data, FullError, spectraList, 0, 34)  # PROTON    max = 34 ; BW = 0  - 33 +1
 
   chiPlusComb = {Which_combination: [CurrentChi2[0], CurrentChi2[1], DICT_COMB[Which_combination]] }
   
   print WorkFolder + "chi_" + str(Which_combination) + ".yml"  
   WriteYaml = open( WorkFolder + "chi_" + str(Which_combination) + ".yml", "w")
   yaml.dump(chiPlusComb, WriteYaml)
     
main()
 
