#!/usr/bin/python2.7
import subprocess
from random import sample
bashCommand = "wc -l data.txt"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
numLines = int(process.communicate()[0].split(' ')[0])
fData = open("data.txt",'r')
fTest = open("testData.txt", 'w+')
fTrain = open("trainData.txt", 'w+')
forTrain = sample(range(0,numLines), int(0.80*numLines))
lines = fData.readlines()
for x in forTrain:
    fTrain.write(lines[x])
for i in range(numLines):
    if i in forTrain:
        continue
    else :
        fTest.write(lines[i])
    
    
