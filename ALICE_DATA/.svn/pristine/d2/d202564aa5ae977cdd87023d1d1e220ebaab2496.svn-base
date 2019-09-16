import json


f = open("fullError_mult5Cent.json", "r")
fw = open("fullError_mult5CentScaled.json", "w")


data = json.load(f)

scaledData = []
print data

for x in range(0,5):

    if x ==0: scaledData.append(data[x]*1.1)
    else: scaledData.append(data[x]*1.12)

print scaledData
json.dump(scaledData, fw)    
