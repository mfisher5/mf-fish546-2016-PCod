#### Counts the number of reads in the `.matches` file output from sstacks ####

## MF 12/12/2016

## ARG1 : list of all samples (for paired end, make sure that `.1` is already on the end). I used my population map
## ARG2 : list of all the final loci (biallelic, filtered for MAF and missing data). I used a text file created from my final .csv file

import sys
lociFile = open(sys.argv[2], "r")

#create list of loci
lociList = []
for line in lociFile: 
	templocus = line.strip()
	lociList.append(templocus)
print lociList

lociFile.close()

#according to the stacks website, the stack depth (n. reads) for each identified haplotype is in column 7.
#for each sample identified in the input file...

seqcounts = open ("SSTACKS_SeqCounts_L1L2.txt", "w")
matchesFiles = open(sys.argv[1], "r")

for sample in matchesFiles: 
	sampleID = sample.strip().split()[0]
	matchfile = "../L1L2stacks_m10/" + sampleID + ".matches.tsv"
	newMatchFile = open(matchfile, "r")  #open the .matches file for that sample
	count = 0 #initiate line count
	stackdepth = 0 #initiate stack depth count
	for line in newMatchFile: 
		if count == 0: 		#to skip the sstacks header at the top of the file
			seqcounts.write(sampleID + "\n")
			count += 1
		else: 
			linelist = line.strip().split()  	#create list of each line's contents
			if linelist[2] in lociList: 		#if the catalog locus is in the final filtered list of biallelic loci
				newdepth = int(linelist[6])       #the next stack depth to add is the integer of the 6th component of the list
				stackdepth += newdepth            #add this stack depth to the total stack depth
				count += 1                        #add 1 to the count
	seqcounts.write(str(stackdepth) + "\n")
	print("Reads in " + sampleID + " counted")
matchesFiles.close()
seqcounts.close()
