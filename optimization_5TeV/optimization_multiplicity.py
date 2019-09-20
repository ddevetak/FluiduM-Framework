import rbfopt
import json
import numpy as np
import subprocess as sb
import sys
import os
from subprocess import call


WORKING_FOLDER = "/lustre/nyx/alice/users/ddevetak/ProbeRun"

class AliceData:

  multPerCent = "../ALICE_DATA/5TeV/json/totalChMultiplicity5centsScaled.json"
  multPerCentError = "../ALICE_DATA/5TeV/json/fullError_mult5CentScaled.json"
  
############################

class HydroData:

  HydroMultPerCent = WORKING_FOLDER  + "/optimization_5TeV/mul_output_folder/totalMult.json"


#############################

def DirectChi(dataList, dataErrorList, hydroList):

  ZIP = zip(dataList[0:5], hydroList[0:5], dataErrorList[0:5])
  ChiSqr = sum([ pow(x[0]-x[1], 2)/(x[2]*x[2]) for x in ZIP ])

  return ( ChiSqr)

##############################

def HydroSpectra(array):

  print ("#################\n"),
  print ("running Hydro for Alg input.....\n")
  print ("INPUT = ", array)

  norm1 = str(array[0])
  norm2 = str(array[1])
  norm3 = str(array[2])
  norm4 = str(array[3])
  norm5 = str(array[4])
  eta =  "0.216"
  bulk = "0.0511"
  temp = "0.1369"
  tau =  "0.2667"
  
  command = "/cvmfs/theory.gsi.de/bin/math11 -script hydro_multiplicity.wl -- " + norm1 + " " + norm2 + " " + norm3 + " " + norm4 + " " + norm5 + " " + eta + " " + bulk + " " + temp + " " + tau
  sb.call(command, shell=True)  # automatically waits for the process to finish

  AliceDataCent = json.load(open(AliceData.multPerCent, "r"))
  AliceDataCentError = json.load(open(AliceData.multPerCentError, "r"))
  HydroDataCent =  json.load(open(HydroData.HydroMultPerCent, "r"))


  CHI2 = DirectChi(AliceDataCent, AliceDataCentError, HydroDataCent)  # rLow, rHigh, paraNumber

  print ("AliceYields = ", AliceDataCent)
  print ("HydroYields = ", HydroDataCent)
  print ("CHI2 = ", CHI2)
  print ("########################\n\n\n")

  return CHI2
    
########################################

bb = rbfopt.RbfoptUserBlackBox(5, [30, 30, 30, 30, 30], [90, 90, 90, 90, 90], np.array(['R', 'R', 'R', 'R', 'R']), HydroSpectra)
settings = rbfopt.RbfoptSettings(max_evaluations=3000, max_iterations=100)


alg = rbfopt.RbfoptAlgorithm(settings, bb)
val, x, itercount, evalcount, fast_evalcount = alg.optimize()

print ("final = ", val, x)



