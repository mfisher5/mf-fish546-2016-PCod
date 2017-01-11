###### Produce Shell script to run process_radtags to ustacks, for single read data ######
## MF 11/15/2016

###############
## At the command line: python radtags_ustacks_genShellSR.py ARG1 ARG2
#ARG 1: input file. line format: <barcode> \t <sampleID>
#ARG 2: new script name. Use file extension ".sh"

#should be run from within the "scripts" folder

###############
## Each time the script is run, make sure to change:
## (1) "process_radtags" input and output file paths, trim (-t), barcodes file, and output file type (if you want a fasta v. fastq file)
## (2) "renaming files" path redirection
## (3) "ustacks" input and output file paths within ustacks code, input file type if necessary
## (4) "cstacks counting sequences" path redirection, 



import sys
myfile = open(sys.argv[1], "r") #input file should have "mv" \t barcode \t sampleID
newfile = open(sys.argv[2], "w")	#create a new file where the ustacks code will go
newfile.write("#!/bin/bash\n")

#process_radtags 
newfile.write("\n"+"#process_radtags"+"\n")
newfile.write("mkdir L2samplesT142" + "\n")
process_radtags = "process_radtags -p /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/raw_data/L2_SR150/ -i gzfastq -y gzfastq -o /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/L2samplesT142 -b /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/scripts/" + sys.argv[1] + " -e sbfI -E phred33 -r -c -q -t 142" + "\n\n"
newfile.write(process_radtags)

#ustacks 
newfile.write("\n"+"#ustacks"+"\n")
newfile.write("cd /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis"+"\n")
newfile.write("mkdir L2samplesT142" + "\n")
ID_int = 1
myfile = open(sys.argv[1], "r")
for line in myfile: 			#for each line in the barcode file	
	linelist=line.strip().split()	
	sampID = linelist[1] 		#save the third object as "sampID"
	if ID_int < 10: 
		ustacks_code = "ustacks -t gzfastq -f L2samplesT142/" + sampID + ".fq.gz -r -d -o stacksCombo_m10 -i 00" + str(ID_int) + " -m 10 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 2 leading 0s)
	elif ID_int >= 10 & ID_int < 100: 
		ustacks_code = "ustacks -t gzfastq -f L2samplesT142/" + sampID + ".fq.gz -r -d -o stacksCombo_m10 -i 0" + str(ID_int) + " -m 10 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 1 leading 0)
	else: 
		ustacks_code = "ustacks -t gzfastq -f L2samplesT142/" + sampID + ".fq.gz -r -d -o stacksCombo_m10 -i " + str(ID_int) + " -m 10 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with no leading 0s)
	newfile.write(ustacks_code)	#append this new line of code to the output file
	ID_int += 1
myfile.close()
newfile.write("\n\n")

#Read counts for cstacks
newfile.write("cd L2samplesT142" + "\n")
myfile = open(sys.argv[1], "r")
filestring = ""
for line in myfile: 			#for each line in the barcode file
	linelist = line.strip().split()	
	sampID = linelist[1]
	newstring = "zcat " + sampID + ".fq.gz | awk '((NR-2)%4==0){read=$1;total++;count[read]++}END{for(read in count){if(!max||count[read]>max) {max=count[read];maxRead=read};if(count[read]==1){unique++}};print total}' >> FastqReadCounts.txt\n"
	filestring += newstring
newfile.write(filestring + "\n\n")
myfile.close()
newfile.close()

