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

#dir = f.GetDirectory("Table 1"); #  pion 0-5%
#dir = f.GetDirectory("Table 2"); #  pion 5-10%
#dir = f.GetDirectory("Table 3"); #  pion 10-20%
#dir = f.GetDirectory("Table 4"); #  pion 20-30%
#dir = f.GetDirectory("Table 5"); #  pion 30-40%

#dir = f.GetDirectory("Table 11"); # kaon 0-5%
#dir = f.GetDirectory("Table 12"); # kaon 5-10%
#dir = f.GetDirectory("Table 13"); # kaon 10-20%
#dir = f.GetDirectory("Table 14"); # kaon 20-30%
#dir = f.GetDirectory("Table 15"); # kaon 30-40%

#dir = f.GetDirectory("Table 21"); # proton 0-5%
#dir = f.GetDirectory("Table 22"); #  proton 5-10%
#dir = f.GetDirectory("Table 23"); # proton 10-20%
#dir = f.GetDirectory("Table 24"); # proton 20-30%
dir = f.GetDirectory("Table 25"); # proton 30-40%

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

