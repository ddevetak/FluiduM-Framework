import ROOT
import json
from sys import argv, exit


def main():

  try:
    # set parameters
    PUT_FILE = str(argv[1])   # path to folder output
    ROOT_FILE = str(argv[2])  # path to root file
    ptDATA = str(argv[3])     # pt data

  except:
    print('Some input parameter is missing!!!')
    exit()

  #################
  # parse name

  fileName = ROOT_FILE.split("/")[-1]    # graph_spectra_i.root
  fileName = "fit_" + fileName

  fileNameEval = "eval_" + fileName.split(".")[0] + ".json"

  #################

  fdata = ROOT.TFile(ROOT_FILE, "READ");
  fwrite = ROOT.TFile(PUT_FILE + fileName, "RECREATE");

  PT_DATA = json.load(open(ptDATA, "r"))
  FileEvalValues = open(PUT_FILE + fileNameEval, "w")

  Graph = ROOT.TGraph()

  graphName = ROOT_FILE.split("/")[-1].split(".")[0]  # graph_name = graph_spectra_i
  fdata.GetObject(graphName, Graph)
 
  #use a cubic spline to smooth the graph

  s = ROOT.TSpline3("name", Graph)
  s.SetLineColor(3)

  Graph.Write()   # fit TGraph with "Graph" name

  EVAL_VALUES = []

  for i in PT_DATA:
 
      temp = round(s.Eval(i), 8)
      EVAL_VALUES.append(temp)

  json.dump(EVAL_VALUES, FileEvalValues, indent = 4)

main()
