###### Produce Shell script to run process_radtags to ustacks for PAIRED END DATA ######
##MF 11/15/2016

## Arguments / replacements in the script are the same as for Single Read

################################################################################

import sys
myfile = open(sys.argv[1], "r") #input file should have barcode \t sampleID
newfile = open(sys.argv[2], "w")	#create a new file where the ustacks code will go
newfile.write("#!/bin/bash\n")

#process_radtags 
newfile.write("\n"+"#process_radtags"+"\n")
newfile.write("mkdir samplesT142" + "\n")
process_radtags = "process_radtags -p /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/raw_data/L1_PE150/ -P -i gzfastq -y gzfastq -o /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/samplesT142 -b /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/" + sys.argv[1] + " -e sbfI -E phred33 -r -c -q -t 142" + "\n\n"
newfile.write(process_radtags)


#ustacks 
newfile.write("cd /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis\n")
newfile.write("mkdir samplesT142" + "\n")
ID_int = 1
myfile = open(sys.argv[1], "r")
for line in myfile: 			#for each line in the barcode file	
	linelist=line.strip().split()	
	sampID = linelist[1] 		#save the third object as "sampID"
	if ID_int < 10: 
		ustacks_code = "ustacks -t gzfastq -f samplesT142/" + sampID + ".1.fq.gz -r -d -o UCstacksL1/stacks_M2 -i 00" + str(ID_int) + " -m 5 -M 2 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 2 leading 0s)
	elif ID_int >= 10 & ID_int < 100: 
		ustacks_code = "ustacks -t gzfastq -f samplesT142/" + sampID + ".1.fq.gz -r -d -o UCstacksL1/stacks_M2 -i 0" + str(ID_int) + " -m 5 -M 2 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 1 leading 0)
	else: 
		ustacks_code = "ustacks -t gzfastq -f samplesT142/" + sampID + ".1.fq.gz -r -d -o UCstacksL1/stacks_M2 -i " + str(ID_int) + " -m 5 -M 2 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with no leading 0s)
	newfile.write(ustacks_code)	#append this new line of code to the output file
	ID_int += 1
myfile.close()
newfile.write("\n\n")

#Sequence counts for cstacks
newfile.write("cd samplesT142\n")
myfile = open(sys.argv[1], "r")
filestring = ""
for line in myfile: 			#for each line in the barcode file
	linelist = line.strip().split()	
	sampID = linelist[2]
	namesfile.write(sampID + ".1.fq.gz\n")
	newstring = "zcat " + sampID + ".1.fq.gz | awk '((NR-2)%4==0){read=$1;total++;count[read]++}END{for(read in count){if(!max||count[read]>max) {max=count[read];maxRead=read};if(count[read]==1){unique++}};print total}' >> FastqReadCounts_PEforward.txt\n"
	filestring += newstring
newfile.write(filestring + "\n\n")
myfile.close()
newfile.close()
