# FASTQ File pairing program in Python
    
import fileinput

pairedData = {}

for line in fileinput.input():
    lineSplit = line.split('_');
    if lineSplit[0] in pairedData:
        line2 = pairedData.get(lineSplit[0])
        pairedData[lineSplit[0]] = [line,line2]
    else:
        pairedData.update({lineSplit[0]:line})

pairedData = pairedData.items()
pairedData.sort(key=lambda item: (item[1], item[0]))

print pairedData
