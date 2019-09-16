import ROOT
import json
import math


#write_file = open("xiPlus.json", "w")
#write_file_pt = open("pt_xiPlus.json", "w")
#write_file_sys = open("sys_xiPlus.json", "w")
#write_file_stat = open("stat_xiPlus.json", "w")
#write_file_error = open("fullError.json", "w")

write_file =       open("omegaMinus.json", "w")
write_file_pt =    open("pt_omegaMinus.json", "w")
write_file_sys =   open("sys_omegaMinus.json", "w")
write_file_stat =  open("stat_omegaMinus.json", "w")
write_file_error = open("fullError.json", "w")

f = ROOT.TFile("HEPData-ins1243865-v1-root.root", "READ")

#dir = f.GetDirectory("Table 1"); # Xi    0-10%
dir = f.GetDirectory("Table 6"); #  Omega 0-10%

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

