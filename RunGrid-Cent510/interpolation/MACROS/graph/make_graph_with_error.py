from ROOT import TCanvas, TGraphErrors
from ROOT import TFile
from ROOT import gROOT
from math import sin
from array import array
import json 
from sys import argv, exit

try:
    # set parameters
    PUT_FOLDER = str(argv[1])  # path to folder output
    PT_LIST = str(argv[2])     # path + json pt list
    DATA_LIST = str(argv[3])   # path + data plus sys

except:
    print('Some input parameter is missing!!!')
    exit()

file_name = ''

if "/" in DATA_LIST:
# exclude path only file
   file_name = DATA_LIST.split("/")
   file_name = file_name[-1]

else:

   file_name = DATA_LIST

file_name = file_name.split(".")
file_name = file_name[0]



file = TFile(PUT_FOLDER + file_name + '.root', "RECREATE");


X = list(json.load(open(PT_LIST, "r")))
Y = list(json.load(open(DATA_LIST, "r")))[0]
SYSY = list(json.load(open(DATA_LIST, "r")))[1]


n = len(X)
x, y = array( 'd' ), array( 'd' )
SysX = array( 'd' )
SysY = array( 'd' )


for i in range( n ):
    x.append( X[i] )
    y.append( Y[i] )
    SysY.append(SYSY[i])
    SysX.append(0)

gr = TGraphErrors(n, x, y, SysX, SysY)
gr.SetMarkerColor(4)
gr.SetMarkerStyle(21)
gr.Write()



