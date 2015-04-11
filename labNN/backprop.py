import random
import math

def sigmoid_func(w):
    return 1.0 / (1.0 + math.exp(-w))

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

    def getOutput(self, inp):
        if self.out is not None:
            return self.out
            
        self.inp = []
        w = 0.0
        for edge in self.in_edges:
            val = edge.source.getOutput(inp)
            self.inp.append(val)
            w += edge.weight * val
            
        self.out = sigmoid_func(w)
        return self.out

    def getError(self, label):
        if self.err is not None:
            return self.err
            
        if self.out_edges == []:
            self.err =  label - self.out
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
            for example, label in examples:
                self.getOutput(example)
                self.findError(label)
                self.updateWeights(param)
                
            max_itr -= 1



gNode = 0
print "Estimating the XOR function :- "
network = Network()

output_nodes = []
input_nodes = []
for i in range(2):
    input_nodes.append(InputNode(i))

for i in range(2):
    output_nodes.append(Node())
    
hidden_nodes = []
for i in range(2):
    hidden_nodes.append(Node())

for src in input_nodes:
    for dst in hidden_nodes:
        Edge(src, dst)

for src in hidden_nodes:
    for dst in output_nodes:
        Edge(src, dst)

network.out_nodes = output_nodes
network.in_nodes = input_nodes

examples = [((0, 0), 0),
            ((0, 1), 0),
            ((1, 0), 0),
            ((1, 1), 1)]

network.train_model(examples, 0.99, 5000)

for example, label in examples:
    print "Test = %r, Output = %0.2f, Error  = %0.2f" % (example, network.getOutput(example), label - network.getOutput(example))
        
