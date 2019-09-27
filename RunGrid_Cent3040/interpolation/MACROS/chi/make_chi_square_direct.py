from ROOT import TF1, TGraphErrors, TH1F, TFile, TH1D, TGraph, TCanvas
import glob
import json
import yaml
import operator
from collections import OrderedDict
from operator import itemgetter
from sys import argv, exit

def missing_numbers(num_list):
      original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
      num_list = set(num_list)
      return (list(num_list ^ set(original_list)))


def DirectChi(dataList, dataErrorList, hydroList, graphName, minBin, maxBin):


  ZIP = zip(dataList[minBin:maxBin+1], hydroList[minBin:maxBin+1], dataErrorList[minBin:maxBin+1])
  
  ChiSqr = sum([ pow(x[0]-x[1], 2)/(x[2]*x[2]) for x in ZIP ])

  NDF = len(dataList[minBin:maxBin+1]) -5

  #return (ChiSqr0/ndf0, ChiSqr1/ndf1, ChiSqr2/ndf2, ChiSqr3/ndf3, ChiSqr4/ndf4, ChiSqr5/ndf5)
  #return (ChiSqr0, ChiSqr1, ChiSqr2, ChiSqr3, ChiSqr4, ChiSqr5)
  #return ChiSqr/NDF
  return ChiSqr

#############################################

def main():

   try:
    # set parameters
     Which_particle = int(argv[1])

   except:
     print('Didnt set particle')
     exit()


   #combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/multiBatchRun/GRID_11.dat", "r")
   #combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/multiBatchRun/conf.dat", "r")
   #combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/run_batch_jobs/0-5/confs/conf_entropy_15_28_etaS_0.08_0.2_bulkS_0.01_0.20_Tk_105_150_tau_0.2_0.6_10K.dat", "r")
   #combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/run_batch_jobs/0-5/GRID_BIN7.dat", "r")
   combinations = open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/conf_norm_80_110_etaS_0.08_0.2_bulkS_0.01_0.20_Tk_135_150_tau_0.6_5K.dat", "r")

   DICT_COMB = dict()
   lineIndex = 0

   for line in combinations:

      lineIndex = lineIndex + 1
      temp = [float(x) for x in line.split(" ")]
      DICT_COMB[lineIndex] = temp


   ####################################################################################
   # DIRECT CHI CALCULATION

   #data_set_path = '/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/multiBatchRun/JOBS_PCE_10K'
   #data_set_path = '/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/multiBatchRun/JOBS_GRID_11BINS'
   #data_set_path = '/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/JOBS_cent05_19_05_2019_NO_DC'
   data_set_path = '/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/TRENTO/5-10/JOBS'

   which_particle  = Which_particle   # pion = 1; kaon = 2; proton = 3

   FILES = ''
   Data = ''
   DataError = ''
   WriteJsonDirect = ''

   if which_particle == 1:

      FILES = (glob.glob(data_set_path + "/job-*/pion/eval_fit*"))
      Data = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/pionPlus/0-5/pi0139plu.json", "r"))
      DataError = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/pionPlus/0-5/fullError.json", "r"))
      WriteYaml = open("./json_trento_510_WITH_DC/chi_pion.yml", "w")
      WriteYamlSorted = open("./json_trento_510_WITH_DC/chi_pion_sorted.yml", "w")

   if which_particle == 2:

      FILES = (glob.glob(data_set_path + "/job-*/kaon/eval_fit*"))
      Data = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/kaonPlus/0-5/Ka0492plu.json", "r"))
      DataError = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/kaonPlus/0-5/fullError.json", "r"))
      WriteYaml = open("./json_trento_510_WITH_DC/chi_kaon.yml", "w")
      WriteYamlSorted = open("./json_trento_510_WITH_DC/chi_kaon_sorted.yml", "w")

   if which_particle == 3:

      FILES = (glob.glob(data_set_path + "/job-*/proton/eval_fit*"))
      Data = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/protonPlus/0-5/pr0938plu.json", "r"))
      DataError = json.load(open("/lustre/nyx/alice/users/ddevetak/FluiduM/ALICE/ALICE_DATA/protonPlus/0-5/fullError.json", "r"))
      WriteYaml = open("./json_trento_510_WITH_DC/chi_proton.yml", "w")
      WriteYamlSorted = open("./json_trento_510_WITH_DC/chi_proton_sorted.yml", "w")


   Chi2Direct = dict()
   minChi = []
   CurrentChi2 = ''

   COUNT = 0

   for x in FILES[0:]:

       if "json" in x:

          COUNT = COUNT +1 
          print "looping file count.... = ", COUNT

          parseName = x.split("/")[-1]
          parseName = parseName.split(".")[0]

          spectraList = json.load(open(x, "r"))     
          if which_particle==1: CurrentChi2 = DirectChi(Data, DataError, spectraList, parseName, 0, 41)  # PION      max = 41 ; BW = 11 - 20 +1
          if which_particle==2: CurrentChi2 = DirectChi(Data, DataError, spectraList, parseName, 0, 36)  # KAON      max = 36 ; BW = 0  - 20 +1
          if which_particle==3: CurrentChi2 = DirectChi(Data, DataError, spectraList, parseName, 0, 34)  # PROTON    max = 34 ; BW = 0  - 33 +1

          confLine = [int(x) for x in parseName.split("_") if x.isdigit()][0]  # WHICH INDEX COMBINATION
          Parameters = DICT_COMB[confLine]                                     # PARAMETERS

          DATA = {
                  "chi2": CurrentChi2, 
                  "parameters": Parameters
                 }
          
          Chi2Direct[confLine] = DATA
          minChi.append(confLine)

   #################################
   Chi2DirectSorted = OrderedDict(sorted(Chi2Direct.items(), key=lambda x: x[1]['chi2'], reverse=False))
   yaml.dump(Chi2Direct, WriteYaml) 
   yaml.dump(Chi2DirectSorted, WriteYamlSorted) 
   #yaml.dump(minChi, WriteYamlSorted) 

   print "NUMBER OF FILES = ", len(FILES)
   print "NUMBER OF MinChi = ", len(minChi)

   KEYS = []

   for key in Chi2Direct:

       #print "key = ", key
       KEYS.append(key)

   MIS = (missing_numbers(KEYS))

     
main()
 
