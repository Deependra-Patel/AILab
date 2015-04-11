#!/usr/bin/python
from train import getPhonemesFromInputList, generateTables, graphemeTophoneme, getStates
generateTables()
states = getStates()
confusionMatrix = {}
for state in states:
        confusionMatrix[state] = {}
        for state2 in states:
                confusionMatrix[state][state2] = 0

f = open("testData.txt", 'r')

def printConfusionMat():
        print "\t",
        for state in states:
                print state + "\t",
        print ""
        for state in states:
                print state + "\t",
                for state2 in states:
                        print str(confusionMatrix[state][state2]) + "\t",
                print ""
                
def matchList(list1, list2):
	matched = 0
	for i in range(len(list1)):
                confusionMatrix[list2[i]][list1[i]] += 1
		if list1[i]==list2[i]:# or list1[i][0]==list2[i][0]:# (len(list1[i])>=2 and len(list2[i])>=2 and  list1[i][0:2]==list2[i][0:2]):
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
printConfusionMat()
print "Passed: "+str(passed)
print "Failed: "+str(failed)
print "Pass% = "+str(float(passed)/(passed+failed))
