import sys 
myfile = open(sys.argv[1], "r")
newfile = open("sstacks_byline_12-4.sh", "w")

newfile.write("#!/bin/bash" + "\n")

for line in myfile: 
	linelist = line.strip().split()
	filestring = "sstacks -b 1 -c L1L2stacks_m10/batch_1 -s L1L2stacks_m10/" + linelist[0] + " -o L1L2stacks_m10 -p 6 2>> sstacks_out_b1b"
	newfile.write(filestring + "\n")

myfile.close()
newfile.close()
