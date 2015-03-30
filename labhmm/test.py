#!/usr/bin/python
from train import getPhonemesFromWord, generateTables
generateTables()
f = open("testData.txt", 'r')

def matchList(list1, list2):
	matched = 0
	for i in range(len(list1)):
		if list1[i]==list2[i]:
			matched += 1
	return matched
    
passed = 0
failed = 0
for line in f:
    line = line.rstrip()
    tokens = line.split(" ")
    phonemes = getPhonemesFromWord(tokens[0])
    matched =  matchList(phonemes, tokens[1:])
    passed += matched
    failed += len(tokens[1:]) - matched
    print line + " " + " ".join(phonemes) #str(passed) + str(failed)

print "Passed: "+str(passed)
print "Failed: "+str(failed)
print "Pass% = "+str(float(passed)/(passed+failed))
