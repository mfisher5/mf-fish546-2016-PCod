### Generate a shell script that will run cstacks ###

##MF 1/10/2017

## Command Line: python cstacks_genShell.py ARG1
##   ARG1 = samples for cstacks text file

## Change in script: 
# 1. name of new shell script
# 2. absolute path from which to run the script
# 3. cstacks arguments, including folder containing .tsv files for all samples
######################################################################

import sys

newfile = open("cstacks_shell.sh", "w")

newfile.write("#!/bin/bash"+"\n")
newfile.write("cd /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis"+"\n")

catFile = open(sys.argv[1], "r")

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
