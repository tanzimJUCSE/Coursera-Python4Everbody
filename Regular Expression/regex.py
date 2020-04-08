#From given file you have to extract the floating point numbers
#The given file is new.txt and the given line starts from "X-DSPAM-Confidence" 
import re
fname = input("Enter file name: ")
fh = open(fname)
c=0
res=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    c=c+1
    li=re.findall("[-+]?[0-9]*\.?[0-9]+",line)
    x=float(li[0])
    res=res+x

fin=res/c
print("Average spam confidence: %.12f" %fin)