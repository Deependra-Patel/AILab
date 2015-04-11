#!/usr/bin/python2.7
import subprocess
from random import sample
bashCommand = "wc -l data.txt"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
numLines = int(process.communicate()[0].split(' ')[0])
fData = open("data.txt",'r')
fTest = open("testData.txt", 'w+')
fTrain = open("trainData.txt", 'w+')
forTrain = sample(range(0,numLines), int(0.001*numLines))
lines = fData.readlines()
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
for x in forTrain:
    if (is_ascii(lines[x])):
        fTrain.write(lines[x])
for i in range(numLines):
    if i in forTrain:
        continue
    elif (is_ascii(lines[i])):
         fTest.write(lines[i])
    
    
