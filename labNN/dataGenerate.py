#!/usr/bin/python2.7
import subprocess
from random import sample, shuffle

fData = open("data.txt",'r')

nData = open("newData.txt" ,'w')
for lines in fData:
    if len(lines.split()) <=6:
        nData.write(lines)

nData.close()
nData = open("newData.txt" ,'r')
bashCommand = "wc -l newData.txt"

process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
numLines = int(process.communicate()[0].split(' ')[0])

fTest = open("testData.txt", 'w+')
fTrain = open("trainData.txt", 'w+')
forTrain = sample(range(0,numLines), int(0.01*numLines))
lines = nData.readlines()
forTrain = range(0,100)
#shuffle(lines)
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
for x in forTrain:
    if (is_ascii(lines[x])):
        if len(lines[x].split()) <= 6:
            fTrain.write(lines[x])
for i in range(numLines):
    if i in forTrain:
        continue
    elif (is_ascii(lines[i])) and len(lines[i].split()) <= 6:
        fTest.write(lines[i])
    
    
