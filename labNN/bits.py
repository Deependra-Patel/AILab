#!/usr/bin/python
g2p = True
graphM = {}
phoneM = {}
MAX = 0
bitsG = 5
bitsP = 7
def initBits():
    global g2p
    g2p = True
    global graphM
    graphM = {}
    global phoneM
    phoneM = {}
    global MAX
    MAX = 0
    global bitsG
    bitsG = 5
    global bitsP
    bitsP = 7
    
    fg = open("states2.txt", 'r')
    fp = open("states.txt", 'r')
    glines = fg.readlines()
    plines = fp.readlines()
    for i in range(0, len(glines)):
        line = glines[i].strip()
        st = str(bin(i)[2:])
        st = "0"*(bitsG-len(st))+st
        graphM[line] = [float(c) for c in st]
    for i in range(0, len(plines)):
        line = plines[i].strip()
        st = str(bin(i)[2:])
        st = "0"*(bitsP-len(st))+st
        phoneM[line] = [float(c) for c in st]

    f = open("newData.txt", 'r')
    for line in f:
        gr = len(line.split())-1
        if MAX < gr:
            MAX = gr
            print line
    return MAX

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

def bitsToPhonemes(bits,length):
    i = 0
    app = []
    ans = []
    bits = list(bits)
    print bits, len(bits)
    for j in range(0, len(bits)):
        if bits[j]>0.5:
            bits[j] = '1'
        else:
            bits[j] = '0'
    print bits, len(bits)
    for bit in bits:
        if i%bitsP == 0 and i != 0:
            index = int(''.join(app), 2)
            print "INDEX: ", index, ''.join(app)
            for key in phoneM:
                index2 = int(''.join([str(int(c)) for c in phoneM[key]]), 2)
                if(index2 == index):
                    ans.append(key)
                    break
            app = []
        i += 1
        app.append(bit)
    index = int(''.join(app), 2)
    print "INDEX: ", index, ''.join(app)
    for key in phoneM:
        index2 = int(''.join([str(int(c)) for c in phoneM[key]]), 2)
        if(index2 == index):
            ans.append(key)
            break
#    print ans
    return ans[:length]
    
def main():
    initBits()
    print phonemeToBits("K AE2 F EY1 Z".split())


if __name__ == "__main__":
    main()
