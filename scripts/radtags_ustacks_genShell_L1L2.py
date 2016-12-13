###### Produce Shell script to run process_radtags to ustacks, for single read data. Will also count sequences for cstacks run. ######
## MF 11/15/2016
## EDITED on 12/3/2016 to run on lane 1 and lane 2 data combined

###############
## At the command line: python radtags_ustacks_genShellSR.py ARG1
#ARG 1: Lane 1 input file. line format: <barcode> \t <sampleID>
#ARG 2: Lane 2 input file. line format: <barcode> \t <sampleID>

#should be run from within the "scripts" folder
#NOTE: ARG 1 MUST BE LANE 1 AND ARG2, LANE 2 BECAUSE OF ID NUMBER ORDER IN USTACKS

###############
## Each time the script is run, make sure to change:
## (1) "process_radtags" input and output file paths, trim (-t), barcodes file, and output file type (if you want a fasta v. fastq file)
## (2) "renaming files" path redirection
## (3) "ustacks" input and output file paths within ustacks code, input file type if necessary
## (4) "cstacks counting sequences" path redirection, 



import sys
myfile = open(sys.argv[1], "r") #input file should have "mv" \t barcode \t sampleID
newfile = open("new_radtags_ustacks_shell.sh", "w")	#create a new file where the ustacks code will go
newfile.write("#!/bin/bash\n")

newfile.write("cd /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis"+"\n")

#process_radtags 
newfile.write("\n"+"#process_radtags"+"\n")
process_radtags = "process_radtags -p /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/raw_data/L2_SR150/ -i gzfastq -y gzfastq -o /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/L2samplesT142 -b /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/scripts/barcodesL2.txt -e sbfI -E phred33 -r -c -q -t 142" + "\n\n"
newfile.write(process_radtags + "\n")

#make new directory for stacks output
newfile.write("mkdir L1L2stacks_m10" + "\n")

#ustacks 
newfile.write("\n"+"#ustacks"+"\n")
#=== Lane 1: forward sequences only
ID_int = 1
myfile = open(sys.argv[1], "r")
for line in myfile: 			#for each line in the barcode file	
	linelist=line.strip().split()	
	sampID = linelist[1] 		#save the third object as "sampID"	
	if ID_int < 10: 
		ustacks_code = "ustacks -t gzfastq -f L1L2samples/" + sampID + ".1.fq.gz -r -d -o L1L2stacks_m10 -i 00" + str(ID_int) + " -m 10 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 2 leading 0s)
	elif ID_int >= 10 & ID_int < 100: 
		ustacks_code = "ustacks -t gzfastq -f L1L2samples/" + sampID + ".1.fq.gz -r -d -o L1L2stacks_m10 -i 0" + str(ID_int) + " -m 10 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 1 leading 0)
	else: 
		ustacks_code = "ustacks -t gzfastq -f L1L2samples/" + sampID + ".1.fq.gz -r -d -o L1L2stacks_m10 -i " + str(ID_int) + " -m 10 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with no leading 0s)
	newfile.write(ustacks_code)	#append this new line of code to the output file
	ID_int += 1
myfile.close()
newfile.write("#Set Variable" + "\n")
newfile.write("N_FILES = " + str(ID_int - 1) + "\n")
newfile.write('echo "ustacks run on $N_FILES files"' + "\n\n")

#=== Lane 2: single read
myfile2 = open(sys.argv[2], "r")
for line in myfile2: 			#for each line in the barcode file	
	linelist=line.strip().split()	
	sampID = linelist[1] 		#save the third object as "sampID"	
	if ID_int >= 10 & ID_int < 100: 
		ustacks_code = "ustacks -t gzfastq -f L1L2samples/" + sampID + ".fq.gz -r -d -o L1L2stacks_m10 -i 0" + str(ID_int) + " -m 10 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 1 leading 0)
	else: 
		ustacks_code = "ustacks -t gzfastq -f L1L2samples/" + sampID + ".fq.gz -r -d -o L1L2stacks_m10 -i " + str(ID_int) + " -m 10 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with no leading 0s)
	newfile.write(ustacks_code)	#append this new line of code to the output file
	ID_int += 1
myfile2.close()
newfile.write("#Set Variable" + "\n")
newfile.write("N_FILES = " + str(ID_int - 1) + "\n")
newfile.write('echo "ustacks run on $N_FILES files"')


newfile.write("\n\n")


### Sequence counts for cstacks ###
newfile.write("chmod +x CountSeqs_BASHscript.sh" + "\n")
newfile.write("./CountSeqs_BASHscript.sh" + "\n\n")

#==wait for confirmation that samples_for_cstacks file has been made
newfile.write('echo "What is the file name for the cstacks catalog?"'+ "\n")
newfile.write('read CAT_FILE' + "\n")
newfile.write('echo "Does this match the file name in the shell script?"'+ "\n")
newfile.write('read ANSWER' + "\n")
newfile.write('echo "Continue with cstacks using samples in $CAT_FILE by generating next shell script."' + "\n")

