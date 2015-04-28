#!/usr/bin/python
import random
import math
import sys
from bits import *
def sigmoid_func(w):
    return 1.0 / (1.0 + math.exp(-w))
debug = False

class Node:
    def __init__(self):
        self.out = None
        self.err = None
        self.inp = None
        global gNode
        self.count = gNode
        gNode += 1
        self.in_edges = []
        self.out_edges = []
        self.addDummyNode()
        self.index = 0
        
    def getOutput(self, inp):
        if self.out is not None:
            return self.out
            
        self.inp = []
        w = 0.0
        for edge in self.in_edges:
            val = edge.source.getOutput(inp)
            self.inp.append(val)
            global debug
            if debug:
                print "ehllo"
                print val, edge.weight
            w += edge.weight * val
            
        self.out = sigmoid_func(w)
        return self.out

    def getError(self, label):
        if self.err is not None:
            return self.err
            
        if self.out_edges == []:
            self.err =  label[self.index] - self.out
        else:
            val = 0.0
            for edge in self.out_edges:
                val += edge.weight * edge.dest.getError(label)
            self.err = val

        return self.err
        
    def updateWeights(self, param):
        if self.err is not None and self.out is not None and self.inp is not None:
            i = 0
            for edge in self.in_edges:
                edge.weight += param * self.out * (1.0 - self.out) * self.err * self.inp[i]
                i += 1

            for edge in self.out_edges:
                edge.dest.updateWeights(param)
                
            self.err = None
            self.out = None
            self.inp = None
        
            
    def addDummyNode(self):
        self.in_edges.append(Edge(TrueNode(), self))
        
    def flushOutput(self):
        self.out = None
        for edge in self.in_edges:
            edge.source.flushOutput()
            
    def printInfo(self):
        print "count = " + str(self.count) + "o = " + str(self.out)
        for edge in self.in_edges:
            edge.printInfo()
        
    def setIndex(self, x):
        self.index = x

class Edge:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self.weight = random.uniform(0, 1)
        
        source.out_edges.append(self)
        dest.in_edges.append(self)

    def printInfo(self):
        print "w = " + str(self.weight)
        self.source.printInfo()


        
class InputNode(Node):
    def __init__(self, idx):
        Node.__init__(self)
        self.idx = idx

    def getOutput(self, inp):
        self.out = inp[self.idx]
        return self.out
        
    def updateWeights(self, param):
        for edge in self.out_edges:
            edge.dest.updateWeights(param)

    def getError(self, label):
        for edge in self.out_edges:
            edge.dest.getError(label)
    
    def addDummyNode(self):
        pass


class TrueNode(Node):
    def __init_(self):
        Node.__init__(self)
        
    def getOutput(self, inp):
        return 1.0
        
    def addDummyNode(self):
        pass



class Network:
    def __init__(self):
        self.in_nodes = []
        self.out_nodes = []

    def getOutput(self, inp):
        output = []
        for node in self.out_nodes:
            node.flushOutput()
            output.append(node.getOutput(inp))
        return output
        
    def updateWeights(self, param):
        for node in self.in_nodes:
            node.updateWeights(param)
        
    def findError(self, label):
        for node in self.in_nodes:
            node.getError(label)

    def printInfo(self):
        print "-------- Print Info Begins--------"
        for node in self.out_nodes:
            node.printInfo()
        print "-------- Print Info Ends --------"

    def train_model(self, examples, param, max_itr):
        while max_itr > 0:
            i = 0
            for example, label in examples:
                #print i
                i += 1
                self.getOutput(example)
                self.findError(label)
                self.updateWeights(param)
            max_itr -= 1

network = Network()    
gNode = 0
MAX = 0
def initNetwork():
    global MAX
    MAX = initBits()
    output_nodes = []
    input_nodes = []
    numInput = MAX*bitsG
    numOutput = MAX*bitsP
    numHidden = (numInput+numOutput)/30
    print bitsG, MAX, numInput, numHidden
    for i in range(numInput):
        input_nodes.append(InputNode(i))

    for i in range(numOutput):
        output_nodes.append(Node())
        output_nodes[i].setIndex(i)
    
    hidden_nodes = []
    for i in range(numHidden):
        hidden_nodes.append(Node())

    for src in input_nodes:
        for dst in hidden_nodes:
            Edge(src, dst)

    for src in hidden_nodes:
        for dst in output_nodes:
            Edge(src, dst)
    network.out_nodes = output_nodes
    network.in_nodes = input_nodes
    """
    output_nodes = []
    input_nodes = []
    numInput = 4
    numOutput = 4
    numHidden = 4
    for i in range(numInput):
        input_nodes.append(InputNode(i))

    for i in range(numOutput):
        output_nodes.append(Node())
        output_nodes[i].setIndex(i)
    
    hidden_nodes = []
    for i in range(numHidden):
        hidden_nodes.append(Node())

    for src in input_nodes:
        for dst in hidden_nodes:
            Edge(src, dst)

    for src in hidden_nodes:
        for dst in output_nodes:
            Edge(src, dst)
    network.out_nodes = output_nodes
    network.in_nodes = input_nodes
    """
    
examples = [((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0,0,0,0)),
            ((0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0,0,0,0)),
            ((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0,0,0,0)),
            ((1, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1,0,0,0))]
def trainNetwork():
    f = open("trainData.txt", 'r')
    trainData = []
    for line in f:
        line = (line.strip()).split()
        graphemes = [c for c in line[0]]
        phonemes = line[1:]
        grBits = tuple(graphemeToBits(graphemes))
        phBits = tuple(phonemeToBits(phonemes))
        grBits = grBits + tuple([float(c) for c in '0'*(MAX*bitsG - len(grBits))])
        phBits = phBits + tuple([float(c) for c in '0'*(MAX*bitsP - len(phBits))])
       # print grBits
       # print MAX*bitsG, bitsG
        if len(phBits)!=MAX*bitsP:
            print len(phBits),"dfsd", phBits
            sys.exit(0)
            break
        trainData.append(tuple([grBits, phBits]))
    
    network.train_model(trainData, 0.80, 500)

def testNetwork():
    tFile = open('testData.txt', 'r')
    testLines = tFile.readlines()
    testLines = testLines[0:1500]
    outFile = open('output.txt', 'w')
    for line in testLines:
        d = line.split()[0]
        inp = graphemeToBits([c for c in d])
        for i in range(0, bitsG*MAX - len(inp)):
            inp.append(0.0)
        #print inp
        inp = tuple(inp)
        output = (d, network.getOutput(inp))
        #print output
        #print bitsP
        print bitsToPhonemes(output[1], len(line.split())-1), "ACTUAL: ", line.split()[1:]
        outFile.write(str(bitsToPhonemes(output[1], len(line.split())-1)))
        outFile.write(" " + str(line.split()[1:]) + "\n")
   # print "Test = %r, Output = %r" % output
   
    #output = ("rand", network.getOutput((1,1,0,0)))
    #print output[1]
        
def main():
    initNetwork()
    trainNetwork()
    #network.printInfo()
    global debug
    debug = False
    print "dfasd"
    testNetwork()
if __name__ == "__main__":
    main()
