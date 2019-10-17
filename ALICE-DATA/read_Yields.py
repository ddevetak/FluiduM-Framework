import ROOT
import json
import math


write_file = open("TotalYields.json", "w")
write_file_pt = open("cent_TotalYields.json", "w")
write_file_stat = open("stat_TotalYields.json", "w")

f = ROOT.TFile("HEPData-ins1222333-v1-root.root", "READ")
dir = f.GetDirectory("Table 31"); # Total Charged Yields

Graph = ROOT.TGraphAsymmErrors() 
StatErrors = ROOT.TH1F() 

dir.GetObject("Graph1D_y1", Graph)
dir.GetObject("Hist1D_y1_e1plus", StatErrors)

Values = Graph.GetY()
CENT = Graph.GetX()

ValuesList = []

StatErrorsList = []

CentList = [] 

for x in Values: ValuesList.append(x)
for x in CENT: CentList.append(round(x,4))

BINS = len(ValuesList)

for i in range(1, BINS+1): StatErrorsList.append(StatErrors.GetBinContent(i))

json.dump(ValuesList, write_file, indent = 4)
json.dump(CentList, write_file_pt)
json.dump(StatErrorsList, write_file_stat, indent = 4)



