import json



dataPion =   json.load(open("./pionPlus/0-5/pt_pi0139plu.json", "r"))
dataKaon =   json.load(open("./kaonPlus/0-5/pt_Ka0492plu.json", "r"))
dataProton = json.load(open("./protonPlus/0-5/pt_pr0938plu.json", "r"))

rangePion =   [0.5, 1.0]
rangeKaon =   [0.2, 1.5]
rangeProton = [0.3, 3.0]

binPion = []
binKaon = []
binProton = []

for x in dataPion:

  if (rangePion[0]<=x and x<=rangePion[1]): 
    binPion.append((x, dataPion.index(x)))

for x in dataKaon:

  if (rangeKaon[0]<=x and x<=rangeKaon[1]): 
    binKaon.append((x, dataKaon.index(x)))

for x in dataProton:

  if (rangeProton[0]<=x and x<=rangeProton[1]): 
    binProton.append((x, dataProton.index(x)))

print binPion, len(binPion), "\n"
print binKaon, len(binKaon), "\n"
print binProton, len(binProton), "\n" 




