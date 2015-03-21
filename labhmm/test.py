#!/usr/bin/python
from train import getPhonemesFromWord, generateTables
generateTables()
f = open("testData.txt", 'r')

def matchList(list1, list2):
    if len(list1)!= len(list2):
        return False
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            return False
    return True
    
passed = 0
failed = 0
for line in f:
    line = line.rstrip()
    tokens = line.split(" ")
    phonemes = getPhonemesFromWord(tokens[0])
    if matchList(phonemes, tokens[1:]):
        passed += 1
    else :
        failed += 1
        print "-----"
    print line + " ".join(phonemes)

print "Passed: "+str(passed)
print "Failed: "+str(failed)
print "Pass% = "+str(float(passed)/(passed+failed))
