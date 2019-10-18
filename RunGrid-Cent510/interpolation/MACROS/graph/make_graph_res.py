from ROOT import TCanvas, TGraph
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
    DATA_LIST = str(argv[3])   # path + json data list

except:
    print('Some input parameter is missing!!!')
    exit()

# exclude path only file
file_name = DATA_LIST.split("/")
file_name = file_name[-1]
# excluded json
file_name = file_name.split(".")
file_name = file_name[0]


file = TFile(PUT_FOLDER + "graph_" + file_name + '.root', "RECREATE");

X = list(json.load(open(PT_LIST, "r")))
Y = list(json.load(open(DATA_LIST, "r")))

n = len(X)
x, y = array( 'd' ), array( 'd' )

for i in range( n ):
    x.append( X[i] )
    y.append( Y[i] )

gr = TGraph(n, x, y)
gr.SetMarkerColor(4);
gr.SetMarkerStyle(21);
#gr.Write("graph_" + file_name)
gr.Write("Graph")
