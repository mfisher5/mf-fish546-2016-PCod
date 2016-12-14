###### Produce Shell script to run process_radtags to ustacks ######

import sys
myfile = open(sys.argv[1], "r") #input file should have "mv" \t barcode \t sampleID
newfile = open("new_stacks_shell", "w")	#create a new file where the ustacks code will go
newfile.write("#!/bin/bash\n")

#process_radtags 
newfile.write("\n"+"#process_radtags"+"\n")
process_radtags = "process_radtags -p /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/raw_data/L1_PE150/ -P -i gzfastq -y gzfasta -o /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/samplesT142 -b /mnt/hgfs/Shared\ Drive\ D/Pacific\ cod/DataAnalysis/barcodesL1.txt -e sbfI -E phred33 -r -c -q -t 142" + "\n\n"
newfile.write(process_radtags)


#renaming files
newfile.write("\n"+"#rename files"+"\n")
newfile.write("cd ../../samplesT142" + "\n")
for line in myfile: 
	linelist=line.strip().split()
	barcodefile = "sample_" + linelist[1] + ".1.fa.gz"
	samplefile = linelist[2] + ".1.fa.gz"
	newstring = linelist[0] + "\t" + barcodefile + "\t" + samplefile + "\n"
	newfile.write(newstring)
newfile.write("\n\n")
myfile.close()

#ustacks 
newfile.write("cd ../\n")
ID_int = 1
myfile = open(sys.argv[1], "r")
for line in myfile: 			#for each line in the barcode file	
	linelist=line.strip().split()	
	sampID = linelist[2] 		#save the third object as "sampID"
	if ID_int < 10: 
		ustacks_code = "ustacks -t gzfasta -f samplesT142/" + sampID + ".1.fa.gz -r -d -o UCstacksL1/stacks_M2 -i 00" + str(ID_int) + " -m 5 -M 2 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 2 leading 0s)
	elif ID_int >= 10 & ID_int < 100: 
		ustacks_code = "ustacks -t gzfasta -f samplesT142/" + sampID + ".1.fa.gz -r -d -o UCstacksL1/stacks_M2 -i 0" + str(ID_int) + " -m 5 -M 2 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 1 leading 0)
	else: 
		ustacks_code = "ustacks -t gzfasta -f samplesT142/" + sampID + ".1.fa.gz -r -d -o UCstacksL1/stacks_M2 -i " + str(ID_int) + " -m 5 -M 2 -p 6" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with no leading 0s)
	newfile.write(ustacks_code)	#append this new line of code to the output file
	ID_int += 1
myfile.close()
newfile.write("\n\n")

#Sequence counts for cstacks
newfile.write("cd samplesT142\n")
myfile = open(sys.argv[1], "r")
namesfile = open("cstacks_seqcountSamples","w") #create a new file where the list of sample files in order will go
filestring = ""
for line in myfile: 			#for each line in the barcode file
	linelist = line.strip().split()	
	sampID = linelist[2]
	namesfile.write(sampID + ".1.fa.gz\n")
	newstring = "zcat " + sampID + ".1.fa.gz | wc -l >> ../new_WordCounts.txt\n"
	filestring += newstring
newfile.write(filestring + "\n\n")
myfile.close()
newfile.close()
namesfile.close()


#Running cstacks









