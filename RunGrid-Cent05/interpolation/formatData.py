import ROOT
from ROOT import TFile, TTree
from ROOT import gROOT, AddressOf
from array import array

######################

class Parameters:
     def __init__(self):

        self.p1, self.p2, self.p3, self.p4, self.p5 = [], [], [], [], []
        self.reducedChi =[]
        self.chi = []

#######################    

def GetData(TreeData, Object):

    for evt in TreeData:
          Object.reducedChi.append(evt.reducedChi)
          Object.chi.append(evt.chi)
          Object.p1.append(evt.norm) 
          Object.p2.append(evt.eta) 
          Object.p3.append(evt.bulk) 
          Object.p4.append(evt.temp) 
          Object.p5.append(evt.tau0) 

   
############################
# GRID_10BINS_05

data = [   "./FULL_05/PionFull.root",
           "./FULL_05/KaonFull.root",
           "./FULL_05/ProtonFull.root"
         ]



fData =   [ ROOT.TFile.Open(x) for x in data] # list of TFile for pion centralities

treePion =   fData[0].Get("tree")    #  list of Tree's for pion centralities
treeKaon =   fData[1].Get("tree")    #  list of Tree's for pion centralities
treeProton = fData[2].Get("tree")    #  list of Tree's for pion centralities

ParPion,   ParKaon,   ParProton =   Parameters(), Parameters(), Parameters()


GetData(treePion, ParPion)  # tree for 0-5% and list and class object
GetData(treeKaon, ParKaon)
GetData(treeProton, ParProton)

################################


#print ParPion.chi, ParKaon.chi, ParProton.chi   

ZipFull = zip( ParPion.chi,   ParKaon.chi,   ParProton.chi)

#####################################################################
# MAKE FULL TREE


SumZipFull = [sum(x) for x in ZipFull]


count = -1
for event in treePion:

      count += 1      
      norm = float("{:.6g}".format(event.norm))
      eta =  float("{:.6g}".format(event.eta))
      bulk = float("{:.6g}".format(event.bulk))
      temp = float("{:.6g}".format(event.temp))
      tau =  float("{:.6g}".format(event.tau0))

      chi = round(SumZipFull[count]/106, 5)
      chi2 = round(SumZipFull[count], 5)

      #print norm, eta, bulk, temp, tau, chi, chi2
      print norm, eta, bulk, temp, tau, chi








