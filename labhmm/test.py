#!/usr/bin/python
from train import getPhonemesFromInputList, generateTables, graphemeTophoneme
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
    if graphemeTophoneme is True:
        expectedOutput = tokens[1:]
        inputList = [char for char in tokens[0]]
    else:
        expectedOutput = [char for char in tokens[0]]
        inputList = tokens[1:]
    outputList = getPhonemesFromInputList(inputList)
    matched =  matchList(outputList, expectedOutput)
    passed += matched
    failed += len(tokens[1:]) - matched
    if graphemeTophoneme is True:
        print line + " Ouput:- " + " ".join(outputList) 
    else:
        print line + " Ouput:- " + "".join(outputList)

print "Passed: "+str(passed)
print "Failed: "+str(failed)
print "Pass% = "+str(float(passed)/(passed+failed))
