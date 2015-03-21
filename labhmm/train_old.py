#!/usr/bin/python2.7
fStates = open("states.txt", 'r')
fTrain = open("trainData.txt", 'r')
states = fStates.readlines()
states = [state.strip() for state in states]
mymap = {}
transitionFreq = {}
transitionFreq["^"] = {}
for state in states:
    transitionFreq["^"][state] = 0
for state in states:
    mymap[state] = {}
    transitionFreq[state] = {}
    for state2 in states:
        transitionFreq[state][state2] = 0
    
lines = fTrain.readlines()
lines = [line.strip() for line in lines]

for line in lines:
    tokens = line.split(" ")
    graphemes = [char for char in tokens[0]]
    phonemes = tokens[1:]
    if len(phonemes) != len(graphemes):
        continue
    else:
        for i in range(len(phonemes)):
            if (i == 0):
                transitionFreq["^"][phonemes[i]] += 1
            else :
                transitionFreq[phonemes[i-1]][phonemes[i]] += 1
                
            if graphemes[i] in mymap[phonemes[i]]:
                mymap[phonemes[i]][graphemes[i]]+=1
            else :
                mymap[phonemes[i]][graphemes[i]] = 1
                
print transitionFreq

def getTransitionProb(transitionFreq):
    transitionProb = {}
    mystates = states + ["^"]
    for state in mystates:
        transitionProb[state] = {}
        for state2 in mystates:
            transitionProb[state][state2] = 0.0

    for state in mystates:
        sum = 0
        for state2 in states:
            sum += transitionFreq[state][state2]
        for state2 in states:
            if sum == 0:
                transitionProb[state][state2] = 0    
            else:
                transitionProb[state][state2] = transitionFreq[state][state2]/sum
    return transitionProb
        
print getTransitionProb(transitionFreq)

    
