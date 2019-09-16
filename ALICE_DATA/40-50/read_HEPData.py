import ROOT
import json
import math


#write_file = open("pi0139plu.json", "w")
#write_file_pt = open("pt_pi0139plu.json", "w")
#write_file_sys = open("sys_pi0139plu.json", "w")
#write_file_stat = open("stat_pi0139plu.json", "w")
#write_file_error = open("fullError_pi0139plu.json", "w")

#write_file = open("Ka0492plu.json", "w")
#write_file_pt = open("pt_Ka0492plu.json", "w")
#write_file_sys = open("sys_Ka0492plu.json", "w")
#write_file_stat = open("stat_Ka0492plu.json", "w")
#write_file_error = open("fullError_Ka0492plu.json", "w")

write_file = open("pr0938plu.json", "w")
write_file_pt = open("pt_pr0938plu.json", "w")
write_file_sys = open("sys_pr0938plu.json", "w")
write_file_stat = open("stat_pr0938plu.json", "w")
write_file_error = open("fullError_pr0938plu.json", "w")

f = ROOT.TFile("HEPData-ins1222333-v1-root.root", "READ")

#dir = f.GetDirectory("Table 6"); #  pion 40-50%
#dir = f.GetDirectory("Table 16"); # kaon 40-50%
dir = f.GetDirectory("Table 26"); # proton 40-50%

Graph = ROOT.TGraphAsymmErrors() 
StatErrors = ROOT.TH1F() 
SysErrors  = ROOT.TH1F() 

dir.GetObject("Graph1D_y1", Graph)
dir.GetObject("Hist1D_y1_e1", StatErrors)
dir.GetObject("Hist1D_y1_e2", SysErrors)

Values = Graph.GetY()
PT = Graph.GetX()

ValuesList = []

StatErrorsList = []
SysErrorsList = []
FullErrorsList = []

PtList = [] 

for x in Values: ValuesList.append(x)
for x in PT: PtList.append(round(x,4))

BINS = len(ValuesList)

for i in range(1, BINS+1): StatErrorsList.append(StatErrors.GetBinContent(i))
for i in range(1, BINS+1): SysErrorsList.append(SysErrors.GetBinContent(i))


for i in range(0, BINS): 

    temp =math.sqrt( StatErrorsList[i]*StatErrorsList[i] + SysErrorsList[i]*SysErrorsList[i] ) 
    FullErrorsList.append(temp)


json.dump(ValuesList, write_file, indent = 4)
json.dump(PtList, write_file_pt)
json.dump(StatErrorsList, write_file_stat, indent = 4)
json.dump(SysErrorsList, write_file_sys, indent = 4)
json.dump(FullErrorsList, write_file_error, indent = 4)

