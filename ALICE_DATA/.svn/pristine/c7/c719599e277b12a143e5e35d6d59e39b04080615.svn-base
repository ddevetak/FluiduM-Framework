import json
import os
from sys import argv, exit


def pointNumber(list1, l, r): 
      
    return ([x for x in list1 if l <= x <= r]) 

def main():

  try:
    # set parameters
    whichParticle = int(argv[1])
    low = float(argv[2])
    high = float(argv[3])

  except:
    print('Didnt set number of files or jobs!')
    exit()


  ptPion =   json.load(open("pt_pi0139plu.json", "r"))
  ptKaon =   json.load(open("pt_Ka0492plu.json", "r"))
  ptProton = json.load(open("pt_pr0938plu.json", "r"))

  DATA = []

  if whichParticle == 1: DATA = ptPion
  if whichParticle == 2: DATA = ptKaon
  if whichParticle == 3: DATA = ptProton

  points = pointNumber(DATA, low, high)
  FirstIndex = DATA.index(points[0])
  LastIndex =  DATA.index(points[-1])

  if whichParticle == 1: print "PION"
  if whichParticle == 2: print "KAON"
  if whichParticle == 3: print "PROTON"
  print "##########################\n"
  print "PT BINNING = ", DATA
  print "##########################\n"
  print "[number of points, first bin, last bin ] = ", len(points), " | ", FirstIndex, " | ", LastIndex 
  print "##########################\n"

  


main()


