from ROOT import TCanvas, TGraph
from ROOT import TFile
from ROOT import gROOT
from math import sin
from array import array
import json 
from sys import argv, exit

try:
    arg1 = str(argv[1])  # path to output folder
    arg2 = str(argv[2])  # path to DATA json
    arg3 = str(argv[3])  # path to HYDRO json

except:
    print('Some input parameter is missing!!!')
    exit()


f_data = open(arg2, "r")
f_hydro = open(arg3, "r")

sys_path = arg2.rsplit('/', 1)[0] + "/fullError.json"

f_data_sys = open(sys_path, "r")

############################ 
# parse

tempStr = arg3.split("/")
tempStr = tempStr[-1].split(".")

tempStr = "ratio_" + tempStr[0] + ".json"


############################

f_ratio = open(arg1 + tempStr, "w")

hydro = json.load(f_hydro)
data = json.load(f_data)
sys = json.load(f_data_sys)

FULL_LIST = []

ratio = [x[0]/x[1] for x in zip(data, hydro)]
sys_ratio = [x[0]/x[1] for x in zip(sys, hydro)]

FULL_LIST.append(ratio)
FULL_LIST.append(sys_ratio)


json.dump(FULL_LIST, f_ratio, indent = 4)




