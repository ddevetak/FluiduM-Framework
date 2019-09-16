import json


f = open("totalMult.json", "r")
fw = open("totalMultScaled.json", "w")


data = json.load(f)[0:7]

scaledData = []
print data

for x in range(0,7):

    if x ==0: scaledData.append(data[x]*1.1)
    if x ==1: scaledData.append(data[x]*1.1)
    if x ==2: scaledData.append(data[x]*1.12)
    if x ==3: scaledData.append(data[x]*1.12)
    if x ==4: scaledData.append(data[x]*1.12)
    if x ==5: scaledData.append(data[x]*1.12)
    if x ==6: scaledData.append(data[x]*1.12)

print scaledData
json.dump(scaledData, fw)    
