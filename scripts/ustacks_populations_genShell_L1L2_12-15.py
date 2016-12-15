###### Produce Shell script to run ustacks to populations, for Lanes 1 and 2 combined data ######
## MF 11/15/2016
## Edited MF 12/15/2016

###############
## At the command line: python radtags_ustacks_genShellSR.py ARG1
#ARG 1: input file, lane 1 barcodes. line format: <barcode> \t <sampleID>
#ARG 2: input file, lane 2 barcodes
#ARG 3: input file for cstacks, with list of samples to build catalog. 

#should be run from within the "scripts" folder

###############
## Each time the script is run, make sure to change:
## (1) output shell name
## (2) absolute path to root directory, from which all local paths will be run. 
## (3) combined sample list name (3x , one for writing in beginning, and two for reading in ustacks and sstacks)
## (4) "ustacks" input and output file paths within ustacks code, input file type if necessary
## (5) "ustacks" stack depth !!! AS OF 12/15, STACK DEPTH = 5
## (6) "cstacks" local path direction of output
## (7) "cstacks" "sstacks" and "populations" batch number
## (8) "sstacks" local paths
## (9) "populations" local paths, batch number and population map name


import sys
newfile = open("ustacks_populations_shell_12-15.sh", "w")	#create a new file where the ustacks code will go
newfile.write("#!/bin/bash\n")

newfile.write("cd /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis"+"\n")

#Take the two input files and make a master list of sample names, including adding ".1" to the end of the paired end samples. 
samplefile = open("L1L2_sampleList.txt", "w")

#=== Lane 1: forward sequences of paired end
myfile = open(sys.argv[1], "r")
for line in myfile: 			#for each line in the barcode file	
	linelist=line.strip().split()	
	sampID = linelist[1] + ".1" 		#save the third object as "sampID"
	samplefile.write(sampID + "\n")
myfile.close()
#=== Lane 2: single read
myfile2 = open(sys.argv[2], "r")
for line in myfile2: 			#for each line in the barcode file	
	linelist=line.strip().split()	 	
	samplefile.write(linelist[1] + "\n")
myfile2.close()	
samplefile.close()


#Make directory for stacks output
newfile.write("mkdir L1L2stacks_m5" + "\n")


#ustacks 
newfile.write("\n"+"#ustacks"+"\n")
samplefile = open("L1L2_sampleList.txt", "r")

ID_int = 1
for line in samplefile: 			#for each line in the barcode file	
	sampID = line.strip()	
	if ID_int < 10: 
		ustacks_code = "ustacks -t gzfastq -f L1L2samplesT142/" + sampID + ".fq.gz -r -d -o L1L2stacks_m5 -i 00" + str(ID_int) + " -m 5 -M 3 -p 6" + "\n"
	elif ID_int >= 10 and ID_int < 100: 
		ustacks_code = "ustacks -t gzfastq -f L1L2samplesT142/" + sampID + ".fq.gz -r -d -o L1L2stacks_m5 -i 0" + str(ID_int) + " -m 5 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 1 leading 0)
	else: 
		ustacks_code = "ustacks -t gzfastq -f L1L2samplesT142/" + sampID + ".fq.gz -r -d -o L1L2stacks_m5 -i " + str(ID_int) + " -m 5 -M 3 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with no leading 0s)
	newfile.write(ustacks_code)	#append this new line of code to the output file
	ID_int += 1
samplefile.close()



newfile.write("\n\n")



#cstacks
newfile.write("\n"+"#ustacks"+"\n")
catFile = open(sys.argv[3], "r")

filestring = "cstacks -b 2 "
for line in catFile: 			#for each sample file listed in the cstacks catalog file
	sampID = line.strip()	
	if sampID.startswith("#"): 
		newstring = ""
	else: 		
		newstring = "-s L1L2stacks_m5/" + sampID + " "
	filestring += newstring
catFile.close()
filestring += "-o L1L2stacks_m5 -n 3 -p 6"
newfile.write(filestring)



newfile.write("\n\n")



##sstacks: run by line
newfile.write("\n"+"#sstacks"+"\n")
samplefile = open("L1L2_sampleList.txt", "r")

for line in samplefile: 			#for each line in the barcode file
	linelist=line.strip().split()
	newstring = "sstacks -b 2 -c L1L2stacks_m5/batch_2 -s L1L2stacks_m5/" + linelist[0] + " -o L1L2stacks_m5 -p 6 2>> sstacks_out_b2"	#creates a new -s entry for that sample input file
	newfile.write(newstring + "\n")		# appends new -s string to "filestring"
samplefile.close()



newfile.write("\n\n")



##populations
newfile.write("populations -b 2 -P L1L2stacks_m5 -M scripts/PopMap_L1L2stacks.txt -t 36 -r 0.75 -p 2 -m 5 --genepop --fasta 2>> populations_out_batch2")



