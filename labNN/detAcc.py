import ast
f = open('output.txt', 'r')
fl = f.readlines()
totcount = 0
success = 0
for line in fl:
    line = line.strip()
    ls = line.split("] [")
    first = ls[0] + "]"
    second = "[" + ls[1]
    flist = ast.literal_eval(first)
    slist = ast.literal_eval(second)
    for i in range(0, len(flist)):
        if flist[i] == slist[i]:
            success += 1
        totcount += 1
success *= 1.0
totcount *= 1.0
print success/totcount
