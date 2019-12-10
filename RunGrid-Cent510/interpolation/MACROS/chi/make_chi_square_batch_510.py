from ROOT import TF1, TGraphErrors, TH1F, TFile, TH1D, TGraph, TCanvas
import glob
import json
import yaml
import math
import operator
from collections import OrderedDict
from operator import itemgetter
from sys import argv, exit


def pointNumber(list1, l, r):

    return ([x for x in list1 if l <= x <= r])



################################################

def DirectChi(dataList, dataErrorList, hydroList, minBin, maxBin):


  ZIP = zip(dataList[minBin:maxBin], hydroList[minBin:maxBin], dataErrorList[minBin:maxBin])
  
  ChiSqr = sum([ pow(x[0]-x[1], 2)/(x[2]*x[2]) for x in ZIP ])

  NDF = len(dataList[minBin:maxBin]) -5    # list[a:b] = [)

  return (ChiSqr/NDF, ChiSqr)
  #return ChiSqr

   #############################################

def main():

   try:
    # set parameters
     MainFolder = str(argv[1])
     WorkFolder = str(argv[2])
     Which_particle = int(argv[3])
     hydroDataFile = str(argv[4])
     hydroNoInter = str(argv[5])

   except:
     print('Didnt set input parameters!')
     exit()

   #############################################


   CONF = json.load(open(MainFolder + "/interpolation/Configure.json", "r"))

   MainFolder =  str(CONF["workingFolder"])
   aliceFolder = str(CONF["aliceFolder"]) 
   GRID = str(CONF["gridFile"]) 

   lowPtPion = float(CONF["ptRangePion"][0]) 
   highPtPion = float(CONF["ptRangePion"][1]) 

   lowPtKaon = float(CONF["ptRangeKaon"][0]) 
   highPtKaon = float(CONF["ptRangeKaon"][1]) 

   lowPtProton = float(CONF["ptRangeProton"][0]) 
   highPtProton = float(CONF["ptRangeProton"][1]) 


   #############################################
   
   Which_combination = [int(x) for x in hydroDataFile.split("/")[-1].split(".")[0].split("_") if x.isdigit()][0]

   combinations = open(MainFolder + "/" + GRID, "r")

   DICT_COMB = dict()
   lineIndex = 0

   for line in combinations:

      lineIndex = lineIndex + 1
      temp = [float(x) for x in line.split(" ")]
      DICT_COMB[lineIndex] = temp

   ####################################################################################
   # DIRECT CHI CALCULATION
 
   PERCENT = 0.0

   spectraList = json.load(open(hydroDataFile, "r"))
   hydroNoInter = json.load(open(hydroNoInter, "r"))
   which_particle  = Which_particle   # pion = 1; kaon = 2; proton = 3

   if which_particle == 1:

      pt = json.load(open(aliceFolder + "/pion/pt_pi0139plu.json", "r"))
      Data = json.load(open(aliceFolder + "/pion/pi0139plu.json", "r"))
      DataError = json.load(open(aliceFolder + "/pion/fullError.json", "r"))

      FirstIndexPion = pt.index(pointNumber(pt, lowPtPion, highPtPion)[0])
      LastIndexPion =  pt.index(pointNumber(pt, lowPtPion, highPtPion)[-1]) + 1

      HydroError =   list(map(lambda x: x*PERCENT, spectraList))
      tempFullError = zip( map(lambda x: x*x, HydroError), map(lambda x: x*x, DataError) )
      FullError = [ math.sqrt(x[0] + x[1]) for x in tempFullError ]

   if which_particle == 2:

      pt = json.load(open(aliceFolder + "/kaon/pt_Ka0492plu.json", "r"))
      Data = json.load(open(aliceFolder + "/kaon/Ka0492plu.json", "r"))
      DataError = json.load(open(aliceFolder + "/kaon/fullError.json", "r"))

      FirstIndexKaon = pt.index(pointNumber(pt, lowPtKaon, highPtKaon)[0])
      LastIndexKaon =  pt.index(pointNumber(pt, lowPtKaon, highPtKaon)[-1]) + 1

      HydroError =   list(map(lambda x: x*PERCENT, spectraList))
      tempFullError = zip( map(lambda x: x*x, HydroError), map(lambda x: x*x, DataError) )
      FullError = [ math.sqrt(x[0] + x[1]) for x in tempFullError ]

   if which_particle == 3:

      pt = json.load(open(aliceFolder + "/proton/pt_pr0938plu.json", "r"))
      Data = json.load(open(aliceFolder + "/proton/pr0938plu.json", "r"))
      DataError = json.load(open(aliceFolder + "/proton/fullError.json", "r"))

      FirstIndexProton = pt.index(pointNumber(pt, lowPtProton, highPtProton)[0])
      LastIndexProton =  pt.index(pointNumber(pt, lowPtProton, highPtProton)[-1]) + 1

      HydroError =   list(map(lambda x: x*PERCENT, spectraList))
      tempFullError = zip( map(lambda x: x*x, HydroError), map(lambda x: x*x, DataError) )
      FullError = [ math.sqrt(x[0] + x[1]) for x in tempFullError ]

   ########################################

   if which_particle==1: print "pion = ", FirstIndexPion, " ", LastIndexPion 
   if which_particle==2: print "kaon = ", FirstIndexKaon, " ", LastIndexKaon
   if which_particle==3: print "proton = ", FirstIndexProton, " ", LastIndexProton 

   CurrentChi2 = 0

   if which_particle==1: CurrentChi2 = DirectChi(Data, FullError, spectraList, FirstIndexPion, LastIndexPion)  # PION      list format [)
   if which_particle==2: CurrentChi2 = DirectChi(Data, FullError, spectraList, FirstIndexKaon, LastIndexKaon)  # KAON      
   if which_particle==3: CurrentChi2 = DirectChi(Data, FullError, spectraList, FirstIndexProton, LastIndexProton)  # PROTON    
 
   chiPlusComb = {Which_combination: [CurrentChi2[0], CurrentChi2[1], DICT_COMB[Which_combination], pt, Data, DataError, hydroNoInter, spectraList] }
   
   #print WorkFolder + "chi_" + str(Which_combination) + ".yml"  
   WriteYaml = open( WorkFolder + "chi_" + str(Which_combination) + ".yml", "w")
   yaml.dump(chiPlusComb, WriteYaml)
     
main()
 
