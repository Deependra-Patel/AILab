#!/usr/bin/python
g2p = True
graphM = {}
phoneM = {}
def init():
    fg = open("states2.txt", 'r')
    fp = open("states.txt", 'r')
    glines = fg.readlines()
    plines = fp.readlines()
    for i in range(0, len(glines)):
        line = glines[i].strip()
        st = str(bin(i)[2:])
        st = "0"*(5-len(st))+st
        graphM[line] = [c for c in st]
    for i in range(0, len(plines)):
        line = plines[i].strip()
        st = str(bin(i)[2:])
        st = "0"*(8-len(st))+st
        phoneM[line] = [c for c in st]
    
def graphemeToBits(grapheme):
    st = []
    for c in grapheme:
        st += graphM[c]
    return st

def phonemeToBits(phoneme):
    st = []
    for c in phoneme:
        st += phoneM[c]
    return st
    
def main():
    init()
    print phonemeToBits("AA AE1".split())


if __name__ == "__main__":
    main()
