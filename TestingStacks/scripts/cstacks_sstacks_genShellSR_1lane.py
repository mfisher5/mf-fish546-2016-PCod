####### Generate Shell Script that will run cstacks and sstacks on ONE LANE of samples #######
## MF modified from original genShellSR on 11/30/2016
## Command Line Arguments: 
#ARG1 = samples_for_cstacks file
#ARG2 = barcode file

#Run from scripts folder
##########################################################################


import sys
newfile = open("cstacks_sstacks_shell_11-30.sh", "w")
## cstacks ##
catFile = open(sys.argv[1], "r")	#open the file with your list of samples to use in cstacks

filestring = "cstacks -b 2 "
for line in catFile: 			#for each sample file listed in the cstacks catalog file
	sampID = line.strip()	
	if sampID.startswith("#"): 
		newstring = ""
	else: 	
		linelist = line.strip().split(".")		
		newSampID = linelist[0]
		newstring = "-s stacks_v44/" + newSampID + " "
	filestring += newstring
catFile.close()
filestring += "-o stacks_v44 -n 3 -p 6"
newfile.write(filestring)
newfile.write("\n\n")



## sstacks ##

myfile = open(sys.argv[2], "r")	#open the first barcodes list file: "mv" \t barcode \t sampleID
filestring = "sstacks -b 2 -c stacks_v44/batch_2 " #choose batch ID and catalog files
for line in myfile: 			#for each line in the barcode file
	linelist=line.strip().split()	
	samplefile = linelist[1]	#creates name of sample input file based on sample list in myfile
	newstring = "-s stacks_v44/" + samplefile + " "	#creates a new -s entry for that sample input file
	filestring += newstring			# appends new -s string to "filestring"
myfile.close()
filestring += "-o stacks_v44 -p 6 2>> sstacks_out_b2 "   #choose output folder and processor # and std.err out file
newfile.write(filestring + "\n\n\n")		#write entire string to the new file
newfile.close()
