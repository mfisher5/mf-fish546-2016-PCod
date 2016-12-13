import sys
lane1 = open(sys.argv[1], "r")
lane2 = open(sys.argv[2], "r")
newshell = open("CountFASTQseqs_12-4.sh", "w")

newshell.write("#!/bin/bash" + "\n\n")

for line in lane1: 
	linelist = line.strip().split()	
	filestring = "zcat L1L2samples/" + linelist[1] + ".1.fq.gz | awk '((NR-2)%4==0){read=$1;total++;count[read]++}END{for(read in count){if(!max||count[read]>max) {max=count[read];maxRead=read};if(count[read]==1){unique++}};print total,unique,unique*100/total,maxRead,count[maxRead],count[maxRead]*100/total}' >> FastQsequenceCounts.txt"
	newshell.write(filestring + "\n")
lane1.close()

for line in lane2: 
	linelist = line.strip().split()	
	filestring = "zcat L1L2samples/" + linelist[1] + ".fq.gz | awk '((NR-2)%4==0){read=$1;total++;count[read]++}END{for(read in count){if(!max||count[read]>max) {max=count[read];maxRead=read};if(count[read]==1){unique++}};print total,unique,unique*100/total,maxRead,count[maxRead],count[maxRead]*100/total}' >> FastQsequenceCounts.txt"
	newshell.write(filestring + "\n")
lane2.close()
newshell.close()
