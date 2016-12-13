##### This python script takes the list of Fastq sequence counts and extracts JUST the total sequence count ##############
## MF 12/4/2016

import sys
countsfile = open(sys.argv[1], "r")
newfile = open("FastqTotalSeqCounts.txt", "w")

for line in countsfile: 
	linelist = line.strip().split()
	newfile.write(linelist[0] + "\n")
countsfile.close()
newfile.close()
	
