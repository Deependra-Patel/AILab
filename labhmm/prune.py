#!/usr/bin/python2.7
import sys
reload(sys)
sys.setdefaultencoding('Cp1252')
f = open("cmudict-0.7b.txt", 'r')
output = open("data.txt", 'w+')
def hasSpecial(inputString):
    return any(char.isdigit() or char == '-' for char in inputString)

for line in f:
	if line.startswith(";;;") or "'" in line:
		continue
	tokens = line.split(" ")
	if (len(tokens) == 0) or hasSpecial(tokens[0]):
		continue
	if len(tokens) == len(tokens[0])+2:
		output.write(tokens[0]+" "+' '.join(tokens[2:]))

print "Done"
